# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from pynitrokey.nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

Operations: typing_extensions.TypeAlias = schemas.IntSchema

from pynitrokey.nethsm.client.components.schema import key_mechanisms
from pynitrokey.nethsm.client.components.schema import key_public_data
from pynitrokey.nethsm.client.components.schema import key_restrictions
from pynitrokey.nethsm.client.components.schema import key_type
Properties = typing.TypedDict(
    'Properties',
    {
        "mechanisms": typing.Type[key_mechanisms.KeyMechanisms],
        "type": typing.Type[key_type.KeyType],
        "restrictions": typing.Type[key_restrictions.KeyRestrictions],
        "key": typing.Type[key_public_data.KeyPublicData],
        "operations": typing.Type[Operations],
    }
)


class PublicKeyDict(schemas.immutabledict[str, int]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "mechanisms",
        "operations",
        "restrictions",
        "type",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "key",
    })
    
    def __new__(
        cls,
        *,
        mechanisms: typing.Union[
            key_mechanisms.KeyMechanismsTupleInput,
            key_mechanisms.KeyMechanismsTuple
        ],
        operations: int,
        restrictions: typing.Union[
            key_restrictions.KeyRestrictionsDictInput,
            key_restrictions.KeyRestrictionsDict,
        ],
        type: typing.Literal[
            "RSA",
            "Curve25519",
            "EC_P224",
            "EC_P256",
            "EC_P384",
            "EC_P521",
            "Generic"
        ],
        key: typing.Union[
            key_public_data.KeyPublicDataDictInput,
            key_public_data.KeyPublicDataDict,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "mechanisms": mechanisms,
            "operations": operations,
            "restrictions": restrictions,
            "type": type,
        }
        for key, val in (
            ("key", key),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(PublicKeyDictInput, arg_)
        return PublicKey.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            PublicKeyDictInput,
            PublicKeyDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PublicKeyDict:
        return PublicKey.validate(arg, configuration=configuration)
    
    @property
    def mechanisms(self) -> key_mechanisms.KeyMechanismsTuple:
        return typing.cast(
            key_mechanisms.KeyMechanismsTuple,
            self.__getitem__("mechanisms")
        )
    
    @property
    def operations(self) -> int:
        return typing.cast(
            int,
            self.__getitem__("operations")
        )
    
    @property
    def restrictions(self) -> key_restrictions.KeyRestrictionsDict:
        return typing.cast(
            key_restrictions.KeyRestrictionsDict,
            self.__getitem__("restrictions")
        )
    
    @property
    def type(self) -> typing.Literal["RSA", "Curve25519", "EC_P224", "EC_P256", "EC_P384", "EC_P521", "Generic"]:
        return typing.cast(
            typing.Literal["RSA", "Curve25519", "EC_P224", "EC_P256", "EC_P384", "EC_P521", "Generic"],
            self.__getitem__("type")
        )
    
    @property
    def key(self) -> typing.Union[key_public_data.KeyPublicDataDict, schemas.Unset]:
        val = self.get("key", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            key_public_data.KeyPublicDataDict,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
PublicKeyDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class PublicKey(
    schemas.Schema[PublicKeyDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "mechanisms",
        "operations",
        "restrictions",
        "type",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: PublicKeyDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            PublicKeyDictInput,
            PublicKeyDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> PublicKeyDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )
