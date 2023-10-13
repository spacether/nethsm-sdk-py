# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]



@dataclasses.dataclass(frozen=True)
class Length(
    schemas.IntSchema
):
    types: typing.FrozenSet[typing.Type] = frozenset({
        int,
    })
    format: str = 'int'
    inclusive_maximum: typing.Union[int, float] = 8192
    inclusive_minimum: typing.Union[int, float] = 128

from nethsm.client.components.schema import tls_key_type
Properties = typing.TypedDict(
    'Properties',
    {
        "type": typing.Type[tls_key_type.TlsKeyType],
        "length": typing.Type[Length],
    }
)


class TlsKeyGenerateRequestDataDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):

    __required_keys__: typing.FrozenSet[str] = frozenset({
        "type",
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "length",
    })
    
    def __new__(
        cls,
        *,
        type: typing.Literal[
            "RSA",
            "Curve25519",
            "EC_P224",
            "EC_P256",
            "EC_P384",
            "EC_P521"
        ],
        length: typing.Union[
            int,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        for key_, val in (
            ("length", length),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(TlsKeyGenerateRequestDataDictInput, arg_)
        return TlsKeyGenerateRequestData.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            TlsKeyGenerateRequestDataDictInput,
            TlsKeyGenerateRequestDataDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> TlsKeyGenerateRequestDataDict:
        return TlsKeyGenerateRequestData.validate(arg, configuration=configuration)
    
    @property
    def type(self) -> typing.Literal["RSA", "Curve25519", "EC_P224", "EC_P256", "EC_P384", "EC_P521"]:
        return typing.cast(
            typing.Literal["RSA", "Curve25519", "EC_P224", "EC_P256", "EC_P384", "EC_P521"],
            self.__getitem__("type")
        )
    
    @property
    def length(self) -> typing.Union[int, schemas.Unset]:
        val = self.get("length", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            int,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
TlsKeyGenerateRequestDataDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class TlsKeyGenerateRequestData(
    schemas.Schema[TlsKeyGenerateRequestDataDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    required: typing.FrozenSet[str] = frozenset({
        "type",
    })
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: TlsKeyGenerateRequestDataDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            TlsKeyGenerateRequestDataDictInput,
            TlsKeyGenerateRequestDataDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> TlsKeyGenerateRequestDataDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

