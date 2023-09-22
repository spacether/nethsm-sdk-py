# coding: utf-8

"""
    Generated by: https://github.com/openapi-json-schema-tools/openapi-json-schema-generator
"""

from pynitrokey.nethsm.client import api_client, exceptions, security_schemes
from pynitrokey.nethsm.client.shared_imports.operation_imports import *  # pyright: ignore [reportWildcardImportFromLibrary]

from .. import path
from .responses import (
    response_204,
    response_401,
    response_403,
    response_406,
    response_412,
)
from .security import security_requirement_object_0

_security: typing.List[security_schemes.SecurityRequirementObject] = [
    security_requirement_object_0.security_requirement_object,
]


__StatusCodeToResponse = typing.TypedDict(
    '__StatusCodeToResponse',
    {
        '204': typing.Type[response_204.ResponseFor204],
        '401': typing.Type[response_401.ResponseFor401],
        '403': typing.Type[response_403.ResponseFor403],
        '406': typing.Type[response_406.ResponseFor406],
        '412': typing.Type[response_412.ResponseFor412],
    }
)
_status_code_to_response: __StatusCodeToResponse = {
    '204': response_204.ResponseFor204,
    '401': response_401.ResponseFor401,
    '403': response_403.ResponseFor403,
    '406': response_406.ResponseFor406,
    '412': response_412.ResponseFor412,
}
_non_error_status_codes = frozenset({
    '204',
})
_error_status_codes = frozenset({
    '401',
    '403',
    '406',
    '412',
})


class BaseApi(api_client.Api):
    @typing.overload
    def _system_reboot_post(
        self,
        *,
        skip_deserialization: typing.Literal[False] = False,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> response_204.ApiResponse: ...

    @typing.overload
    def _system_reboot_post(
        self,
        *,
        skip_deserialization: typing.Literal[True],
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ) -> api_response.ApiResponseWithoutDeserialization: ...

    def _system_reboot_post(
        self,
        *,
        skip_deserialization: bool = False,
        security_index: typing.Optional[int] = None,
        server_index: typing.Optional[int] = None,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, float, typing.Tuple]] = None,
    ):
        """
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path
        # TODO add cookie handling
        host = self.api_client.configuration.get_server_url(
            "servers", server_index
        )
        security_requirement_object = self.api_client.configuration.get_security_requirement_object(
            "paths//system/reboot/post/security",
            _security,
            security_index
        )

        raw_response = self.api_client.call_api(
            resource_path=used_path,
            method='post',
            host=host,
            security_requirement_object=security_requirement_object,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            skip_deser_response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
            self._verify_response_status(skip_deser_response)
            return skip_deser_response

        status = str(raw_response.status)
        if status in _non_error_status_codes:
            status_code = typing.cast(
                typing.Literal[
                    '204',
                ],
                status
            )
            return _status_code_to_response[status_code].deserialize(
                raw_response, self.api_client.schema_configuration)
        elif status in _error_status_codes:
            error_status_code = typing.cast(
                typing.Literal[
                    '401',
                    '403',
                    '406',
                    '412',
                ],
                status
            )
            error_response = _status_code_to_response[error_status_code].deserialize(
                raw_response, self.api_client.schema_configuration)
            raise exceptions.ApiException(
                status=error_response.response.status,
                reason=error_response.response.reason,
                api_response=error_response
            )

        response = api_response.ApiResponseWithoutDeserialization(response=raw_response)
        self._verify_response_status(response)
        return response


class SystemRebootPost(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId.snakeCase fn names
    system_reboot_post = BaseApi._system_reboot_post


class ApiForPost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names
    post = BaseApi._system_reboot_post