# coding: utf-8

"""
    Accounting Extension

    These APIs allow you to interact with HubSpot's Accounting Extension. It allows you to: * Specify the URLs that HubSpot will use when making webhook requests to your external accounting system. * Respond to webhook calls made to your external accounting system by HubSpot   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.extensions.accounting.api_client import ApiClient
from hubspot.crm.extensions.accounting.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class SettingsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_by_id(self, app_id, **kwargs):  # noqa: E501
        """Get URL settings  # noqa: E501

        Returns the URL settings for an accounting app with the specified ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id(app_id, async_req=True)
        >>> result = thread.get()

        :param app_id: The ID of the accounting app. This is the identifier of the application created in your HubSpot developer portal. (required)
        :type app_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: AccountingAppSettings
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(app_id, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, app_id, **kwargs):  # noqa: E501
        """Get URL settings  # noqa: E501

        Returns the URL settings for an accounting app with the specified ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id_with_http_info(app_id, async_req=True)
        >>> result = thread.get()

        :param app_id: The ID of the accounting app. This is the identifier of the application created in your HubSpot developer portal. (required)
        :type app_id: int
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: tuple(AccountingAppSettings, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["app_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_by_id" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and local_var_params.get("app_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        response_types_map = {
            200: "AccountingAppSettings",
        }

        return self.api_client.call_api(
            "/crm/v3/extensions/accounting/settings/{appId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )

    def replace(self, app_id, accounting_app_settings, **kwargs):  # noqa: E501
        """Add/Update URL Settings  # noqa: E501

        Add/Update the URL settings for an accounting app with the specified ID.  All URLs must use the `https` protocol.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.replace(app_id, accounting_app_settings, async_req=True)
        >>> result = thread.get()

        :param app_id: The ID of the accounting app. This is the identifier of the application created in your HubSpot developer portal. (required)
        :type app_id: int
        :param accounting_app_settings: (required)
        :type accounting_app_settings: AccountingAppSettings
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """
        kwargs["_return_http_data_only"] = True
        return self.replace_with_http_info(app_id, accounting_app_settings, **kwargs)  # noqa: E501

    def replace_with_http_info(self, app_id, accounting_app_settings, **kwargs):  # noqa: E501
        """Add/Update URL Settings  # noqa: E501

        Add/Update the URL settings for an accounting app with the specified ID.  All URLs must use the `https` protocol.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.replace_with_http_info(app_id, accounting_app_settings, async_req=True)
        >>> result = thread.get()

        :param app_id: The ID of the accounting app. This is the identifier of the application created in your HubSpot developer portal. (required)
        :type app_id: int
        :param accounting_app_settings: (required)
        :type accounting_app_settings: AccountingAppSettings
        :param async_req: Whether to execute the request asynchronously.
        :type async_req: bool, optional
        :param _return_http_data_only: response data without head status code
                                       and headers
        :type _return_http_data_only: bool, optional
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :type _preload_content: bool, optional
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the authentication
                              in the spec for a single request.
        :type _request_auth: dict, optional
        :type _content_type: string, optional: force content-type for the request
        :return: Returns the result object.
                 If the method is called asynchronously,
                 returns the request thread.
        :rtype: None
        """

        local_var_params = locals()

        all_params = ["app_id", "accounting_app_settings"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method replace" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'app_id' is set
        if self.api_client.client_side_validation and local_var_params.get("app_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `app_id` when calling `replace`")  # noqa: E501
        # verify the required parameter 'accounting_app_settings' is set
        if self.api_client.client_side_validation and local_var_params.get("accounting_app_settings") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `accounting_app_settings` when calling `replace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "app_id" in local_var_params:
            path_params["appId"] = local_var_params["app_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "accounting_app_settings" in local_var_params:
            body_params = local_var_params["accounting_app_settings"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "PUT", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["hapikey"]  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            "/crm/v3/extensions/accounting/settings/{appId}",
            "PUT",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_types_map=response_types_map,
            auth_settings=auth_settings,
            async_req=local_var_params.get("async_req"),
            _return_http_data_only=local_var_params.get("_return_http_data_only"),  # noqa: E501
            _preload_content=local_var_params.get("_preload_content", True),
            _request_timeout=local_var_params.get("_request_timeout"),
            collection_formats=collection_formats,
            _request_auth=local_var_params.get("_request_auth"),
        )
