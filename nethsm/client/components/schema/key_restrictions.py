# coding: utf-8

"""
    NetHSM
    All endpoints expect exactly the specified JSON. Additional properties will cause a Bad Request Error (400). All HTTP errors contain a JSON structure with an explanation of type string. All [base64](https://tools.ietf.org/html/rfc4648#section-4) encoded values are Big Endian.   # noqa: E501
    The version of the OpenAPI document: v1
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from __future__ import annotations
from nethsm.client.shared_imports.schema_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]


from nethsm.client.components.schema import tag_list
Properties = typing.TypedDict(
    'Properties',
    {
        "tags": typing.Type[tag_list.TagList],
    }
)


class KeyRestrictionsDict(schemas.immutabledict[str, schemas.OUTPUT_BASE_TYPES]):
    __required_keys__: typing.FrozenSet[str] = frozenset({
    })
    __optional_keys__: typing.FrozenSet[str] = frozenset({
        "tags",
    })
    
    def __new__(
        cls,
        *,
        tags: typing.Union[
            tag_list.TagListTupleInput,
            tag_list.TagListTuple,
            schemas.Unset
        ] = schemas.unset,
        configuration_: typing.Optional[schema_configuration.SchemaConfiguration] = None,
        **kwargs: schemas.INPUT_TYPES_ALL,
    ):
        arg_: typing.Dict[str, typing.Any] = {}
        for key_, val in (
            ("tags", tags),
        ):
            if isinstance(val, schemas.Unset):
                continue
            arg_[key_] = val
        arg_.update(kwargs)
        used_arg_ = typing.cast(KeyRestrictionsDictInput, arg_)
        return KeyRestrictions.validate(used_arg_, configuration=configuration_)
    
    @staticmethod
    def from_dict_(
        arg: typing.Union[
            KeyRestrictionsDictInput,
            KeyRestrictionsDict
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> KeyRestrictionsDict:
        return KeyRestrictions.validate(arg, configuration=configuration)
    
    @property
    def tags(self) -> typing.Union[tag_list.TagListTuple, schemas.Unset]:
        val = self.get("tags", schemas.unset)
        if isinstance(val, schemas.Unset):
            return val
        return typing.cast(
            tag_list.TagListTuple,
            val
        )
    
    def get_additional_property_(self, name: str) -> typing.Union[schemas.OUTPUT_BASE_TYPES, schemas.Unset]:
        schemas.raise_if_key_known(name, self.__required_keys__, self.__optional_keys__)
        return self.get(name, schemas.unset)
KeyRestrictionsDictInput = typing.Mapping[str, schemas.INPUT_TYPES_ALL]


@dataclasses.dataclass(frozen=True)
class KeyRestrictions(
    schemas.Schema[KeyRestrictionsDict, tuple]
):
    """NOTE: This class is auto generated by OpenAPI JSON Schema Generator.
    Ref: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator

    Do not edit the class manually.
    """
    types: typing.FrozenSet[typing.Type] = frozenset({schemas.immutabledict})
    properties: Properties = dataclasses.field(default_factory=lambda: schemas.typed_dict_to_instance(Properties)) # type: ignore
    type_to_output_cls: typing.Mapping[
        typing.Type,
        typing.Type
    ] = dataclasses.field(
        default_factory=lambda: {
            schemas.immutabledict: KeyRestrictionsDict
        }
    )

    @classmethod
    def validate(
        cls,
        arg: typing.Union[
            KeyRestrictionsDictInput,
            KeyRestrictionsDict,
        ],
        configuration: typing.Optional[schema_configuration.SchemaConfiguration] = None
    ) -> KeyRestrictionsDict:
        return super().validate_base(
            arg,
            configuration=configuration,
        )

