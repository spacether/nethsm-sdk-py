# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

AdditionalProperties: typing_extensions.TypeAlias = schemas.NotAnyTypeSchema

from nethsm.client.paths.keys_key_id.put.parameters.parameter_0 import schema
from nethsm.client.paths.keys_key_id.put.parameters.parameter_1 import schema as schema_2
Properties = typing.TypedDict(
    'Properties',
    {
        "mechanisms": typing.Type[schema.Schema],
        "tags": typing.Type[schema_2.Schema],
    }
)


class QueryParametersDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "mechanisms",
        "tags",
    })
    
    def __new__(
        cls,
        *,
        mechanisms: typing.Union[
            schema.SchemaTupleInput,
            schema.SchemaTuple,
            schemas.Unset
        ] = schemas.unset,
        tags: typing.Union[
            schema_2.SchemaTupleInput,
            schema_2.SchemaTuple,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("mechanisms", mechanisms),
            ("tags", tags),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        used_arg_ = typing.cast(QueryParametersDictInput, arg_)
        return QueryParameters.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> QueryParametersDict:
        return QueryParameters.validate(arg, configuration=configuration)
    
    @property
    def mechanisms(self) -> typing.Union[schema.SchemaTuple, schemas.Unset]:
        val = self.get("mechanisms", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schema.SchemaTuple,
            val
        )
    
    @property
    def tags(self) -> typing.Union[schema_2.SchemaTuple, schemas.Unset]:
        val = self.get("tags", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            schema_2.SchemaTuple,
            val
        )
QueryParametersDictInput = typing.TypedDict(
    'QueryParametersDictInput',
    {
        "mechanisms": typing.Union[
            schema.SchemaTupleInput,
            schema.SchemaTuple
        ],
        "tags": typing.Union[
            schema_2.SchemaTupleInput,
            schema_2.SchemaTuple
        ],
    },
    total=False
)


@dataclasses.dataclass(frozen=True)
class QueryParameters(
    schemas.Schema[QueryParametersDict, tuple]
):
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    additional_properties: typing.Type[AdditionalProperties] = dataclasses.field(default_factory=lambda: AdditionalProperties) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: QueryParametersDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            QueryParametersDictInput,
            QueryParametersDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> QueryParametersDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

