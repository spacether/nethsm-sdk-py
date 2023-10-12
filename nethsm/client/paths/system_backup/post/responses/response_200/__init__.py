# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from nethsm.client.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.application_octet_stream import schema as application_octet_stream_schema


@dataclasses.dataclass(frozen=True)
class ApiResponse(api_response.ApiResponse):
    body: typing.Union[bytes, schemas.FileIO]
    headers: schemas.Unset


class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)


    class ApplicationOctetStreamMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_octet_stream_schema.Schema
    content = {
        'application/octet-stream': ApplicationOctetStreamMediaType,
    }
