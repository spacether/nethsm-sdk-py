# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from nethsm.client.shared_imports.response_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]


@dataclasses.dataclass(frozen=True)
class ApiResponse(api_response.ApiResponse):
    body: schemas.Unset
    headers: schemas.Unset


class ResponseFor415(api_client.OpenApiResponse[ApiResponse]):
    @classmethod
    def get_response(cls, response, headers, body) -> ApiResponse:
        return ApiResponse(response=response, body=body, headers=headers)
