import base64
import contextlib
import datetime
import os
import subprocess
from time import sleep

import docker
import pytest
import urllib3
from conftest import Constants as C
from Crypto.Cipher import PKCS1_v1_5 as PKCS115_Cipher
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_PSS
from cryptography import x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.serialization import (
    Encoding,
)
from cryptography.x509.oid import NameOID

import nethsm as nethsm_module


@pytest.fixture(scope="module")
def nethsm():
    """Start Docker container with Nethsm image and connect to Nethsm

    This Pytest Fixture will run before the tests to provide the tests with
    a nethsm instance via Docker container, also the first provision of the
    NetHSM will be done in here"""

    container = start_nethsm()

    with connect(C.AdminUser) as nethsm:
        provision(nethsm)
        yield nethsm

    try:
        container.kill()
    except docker.errors.APIError:
        pass


class KeyfenderManager:
    def __init__():
        ...

    def kill():
        ...


class KeyfenderDockerManager(KeyfenderManager):
    def __init__(self):
        client = docker.from_env()

        while True:
            containers = client.containers.list(
                filters={"ancestor": C.IMAGE}, ignore_removed=True
            )
            print(containers)
            if len(containers) == 0:
                break

            for container in containers:
                try:
                    container.remove(force=True)
                except docker.errors.APIError as e:
                    print(e)
                    pass
            sleep(1)

        container = client.containers.run(
            C.IMAGE,
            "",
            ports={"8443": 8443},
            remove=True,
            detach=True,
        )
        self.container = container

    def kill(self):
        try:
            self.container.kill()
        except docker.errors.APIError:
            pass


class KeyfenderCIManager(KeyfenderManager):
    def __init__(self):
        os.system("pkill keyfender.unix")
        os.system("pkill etcd")
        os.system("rm -rf /data")

        self.process = subprocess.Popen(
            [
                "/bin/sh",
                "-c",
                "/start.sh",
            ]
        )

    def kill(self):
        self.process.kill()


def start_nethsm():

    if C.TEST_MODE == "docker":
        context = KeyfenderDockerManager()
    elif C.TEST_MODE == "ci":
        context = KeyfenderCIManager()
    else:
        raise Exception("Invalid Test Mode")

    http = urllib3.PoolManager(cert_reqs="CERT_NONE")
    print("Waiting for container to be ready")
    while True:
        try:
            response = http.request("GET", f"https://{C.HOST}/api/v1/health/alive")
            print(f"Response: {response.status}")
            if response.status == 200:
                break
        except Exception as e:
            print(e)
            pass
        sleep(0.5)

    return context


@contextlib.contextmanager
def connect(username):
    with nethsm_module.connect(
        C.HOST, C.VERSION, username.USER_ID, C.PASSWORD, C.VERIFY_TLS
    ) as nethsm_out:
        yield nethsm_out


def provision(nethsm):
    """Initial provisioning of a NetHSM.

    If unlock or admin passphrases are not set, they have to be entered
    interactively.  If the system time is not set, the current system time is
    used."""
    if nethsm.get_state().value == "Unprovisioned":
        system_time = datetime.datetime.now(datetime.timezone.utc)
        nethsm.provision("unlockunlock", "adminadmin", system_time)


def add_user(nethsm, username):
    """Create a new user on the NetHSM.

    If the real name, role or passphrase are not specified, they have to be
    specified interactively.  If the user ID is not set, it is generated by the
    NetHSM.

    This command requires authentication as a user with the Administrator
    role."""
    try:
        nethsm.get_user(user_id=username.USER_ID)
    except nethsm_module.NetHSMError:
        nethsm.add_user(
            username.REAL_NAME, username.ROLE, C.PASSPHRASE, username.USER_ID
        )


def generate_rsa_key_pair(length_in_bit):
    key_pair = RSA.generate(length_in_bit)
    length_in_byte = int(length_in_bit / 8)
    # "big" byteorder is needed, it's the dominant order in networking
    p = base64.b64encode(key_pair.p.to_bytes(length_in_byte, "big"))
    q = base64.b64encode(key_pair.q.to_bytes(length_in_byte, "big"))
    e = base64.b64encode(key_pair.e.to_bytes(length_in_byte, "big"))
    p = str(p, "utf-8").strip()
    q = str(q, "utf-8").strip()
    e = str(e, "utf-8").strip()
    return p, q, e


def verify_rsa_signature(public_key: str, message: SHA256.SHA256Hash, signature: bytes):
    key = RSA.importKey(public_key)
    return PKCS1_PSS.new(key).verify(message, signature)


def encrypt_rsa(public_key: str, message: str):
    public_key = RSA.importKey(public_key)
    cipher = PKCS115_Cipher.new(public_key)
    return cipher.encrypt(bytes(message, "utf-8"))


def lock(nethsm):
    if nethsm.get_state().value == "Operational":
        nethsm.lock()
    assert nethsm.get_state().value == "Locked"


def unlock(nethsm, unlock_passphrase):
    if nethsm.get_state().value == "Locked":
        nethsm.unlock(unlock_passphrase)
    assert nethsm.get_state().value == "Operational"


def set_backup_passphrase(nethsm):
    """Set the backup passphrase of a NetHSM.

    This command requires authentication as a user with the Administrator
    role.
    """
    nethsm.set_backup_passphrase(C.BACKUP_PASSPHRASE)


def update(nethsm):
    """Load an update to a NetHSM instance.

    This command requires authentication as a user with the Administrator
    role.

    Todo Further Optimization would download the latest.zip, unzip it and
    get the update from there"""

    try:
        with open(C.FILENAME_UPDATE_IN_TEST, "rb") as f:
            nethsm.update(f)
    except OSError as e:
        print(e, type(e))
        assert False


def self_sign_csr(csr: str):
    # Generate a private key
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    parsed_csr = x509.load_pem_x509_csr(csr.encode("utf-8"))

    subject = parsed_csr.subject
    issuer = subject
    public_key = parsed_csr.public_key()
    now = datetime.datetime.utcnow()
    cert = (
        x509.CertificateBuilder()
        .subject_name(subject)
        .issuer_name(issuer)
        .public_key(public_key)
        .serial_number(x509.random_serial_number())
        .not_valid_before(now)
        .not_valid_after(now + datetime.timedelta(days=365))
        .add_extension(x509.BasicConstraints(ca=False, path_length=None), critical=True)
        .add_extension(
            x509.SubjectKeyIdentifier.from_public_key(public_key), critical=False
        )
        .add_extension(
            x509.AuthorityKeyIdentifier.from_issuer_public_key(public_key),
            critical=False,
        )
        .sign(private_key, hashes.SHA256())
    )
    return cert.public_bytes(Encoding.PEM)
