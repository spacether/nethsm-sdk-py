# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]


from nethsm.client.components.schema import base64
from nethsm.client.components.schema import decrypt_mode
Properties = typing.TypedDict(
    'Properties',
    {
        "mode": typing.Type[decrypt_mode.DecryptMode],
        "encrypted": typing.Type[base64.Base64],
        "iv": typing.Type[base64.Base64],
    }
)


class DecryptRequestDataDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "encrypted",
        "mode",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "iv",
    })
    
    def __new__(
        cls,
        *,
        encrypted: str,
        mode: typing.Literal[
            "RAW",
            "PKCS1",
            "OAEP_MD5",
            "OAEP_SHA1",
            "OAEP_SHA224",
            "OAEP_SHA256",
            "OAEP_SHA384",
            "OAEP_SHA512",
            "AES_CBC"
        ],
        iv: typing.Union[
            str,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "encrypted": encrypted,
            "mode": mode,
        }
        for key_, val in (
            ("iv", iv),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(DecryptRequestDataDictInput, arg_)
        return DecryptRequestData.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            DecryptRequestDataDictInput,
            DecryptRequestDataDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> DecryptRequestDataDict:
        return DecryptRequestData.validate(arg, configuration=configuration)
    
    @property
    def encrypted(self) -> str:
        return typing.cast(
            str,
            self.__getitem__("encrypted")
        )
    
    @property
    def mode(self) -> typing.Literal["RAW", "PKCS1", "OAEP_MD5", "OAEP_SHA1", "OAEP_SHA224", "OAEP_SHA256", "OAEP_SHA384", "OAEP_SHA512", "AES_CBC"]:
        return typing.cast(
            typing.Literal["RAW", "PKCS1", "OAEP_MD5", "OAEP_SHA1", "OAEP_SHA224", "OAEP_SHA256", "OAEP_SHA384", "OAEP_SHA512", "AES_CBC"],
            self.__getitem__("mode")
        )
    
    @property
    def iv(self) -> typing.Union[str, schemas.Unset]:
        val = self.get("iv", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            str,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
DecryptRequestDataDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class DecryptRequestData(
    schemas.Schema[DecryptRequestDataDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "encrypted",
        "mode",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: DecryptRequestDataDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            DecryptRequestDataDictInput,
            DecryptRequestDataDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> DecryptRequestDataDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

