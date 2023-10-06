# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from nethsm.client.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .content.application_json import schema as application_json_schema


class ApiResponse(api_response.ApiResponse):
    def __init__(
        self,
        *,
        response: urllib3.HTTPResponse,
        body: application_json_schema.sign_data.SignDataDict,
        headers: schemas.Unset = schemas.unset
    ):
        self.response = response
        self.body = body
        self.headers = headers


class ResponseFor200(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)


    class ApplicationJsonMediaType(api_client.MediaType):
        schema: typing_extensions.TypeAlias = application_json_schema.Schema
    content = {
        'application/json': ApplicationJsonMediaType,
    }
