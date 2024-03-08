# coding: utf-8

"""
    Marketing Events

    These APIs allow you to interact with HubSpot's Marketing Events Extension. It allows you to: * Create, Read or update Marketing Event information in HubSpot * Specify whether a HubSpot contact has registered, attended or cancelled a registration to a Marketing Event. * Specify a URL that can be called to get the details of a Marketing Event.   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.marketing.events.api_client import ApiClient
from hubspot.marketing.events.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class BatchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, batch_input_marketing_event_external_unique_identifier, **kwargs):  # noqa: E501
        """Delete multiple marketing events  # noqa: E501

        Bulk delete a number of marketing events in HubSpot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive(batch_input_marketing_event_external_unique_identifier, async_req=True)
        >>> result = thread.get()

        :param batch_input_marketing_event_external_unique_identifier: The details of the marketing events to delete (required)
        :type batch_input_marketing_event_external_unique_identifier: BatchInputMarketingEventExternalUniqueIdentifier
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
        :rtype: Error
        """
        kwargs["_return_http_data_only"] = True
        return self.archive_with_http_info(batch_input_marketing_event_external_unique_identifier, **kwargs)  # noqa: E501

    def archive_with_http_info(self, batch_input_marketing_event_external_unique_identifier, **kwargs):  # noqa: E501
        """Delete multiple marketing events  # noqa: E501

        Bulk delete a number of marketing events in HubSpot  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive_with_http_info(batch_input_marketing_event_external_unique_identifier, async_req=True)
        >>> result = thread.get()

        :param batch_input_marketing_event_external_unique_identifier: The details of the marketing events to delete (required)
        :type batch_input_marketing_event_external_unique_identifier: BatchInputMarketingEventExternalUniqueIdentifier
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
        :rtype: tuple(Error, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["batch_input_marketing_event_external_unique_identifier"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_input_marketing_event_external_unique_identifier' is set
        if self.api_client.client_side_validation and local_var_params.get("batch_input_marketing_event_external_unique_identifier") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_marketing_event_external_unique_identifier` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_marketing_event_external_unique_identifier" in local_var_params:
            body_params = local_var_params["batch_input_marketing_event_external_unique_identifier"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            "/marketing/v3/marketing-events/events/delete",
            "POST",
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

    def do_upsert(self, batch_input_marketing_event_create_request_params, **kwargs):  # noqa: E501
        """Create or update multiple marketing events  # noqa: E501

        Upset multiple Marketing Event. If there is an existing Marketing event with the specified id, it will be updated; otherwise a new event will be created.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.do_upsert(batch_input_marketing_event_create_request_params, async_req=True)
        >>> result = thread.get()

        :param batch_input_marketing_event_create_request_params: The details of the marketing events to upsert (required)
        :type batch_input_marketing_event_create_request_params: BatchInputMarketingEventCreateRequestParams
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
        :rtype: BatchResponseMarketingEventPublicDefaultResponse
        """
        kwargs["_return_http_data_only"] = True
        return self.do_upsert_with_http_info(batch_input_marketing_event_create_request_params, **kwargs)  # noqa: E501

    def do_upsert_with_http_info(self, batch_input_marketing_event_create_request_params, **kwargs):  # noqa: E501
        """Create or update multiple marketing events  # noqa: E501

        Upset multiple Marketing Event. If there is an existing Marketing event with the specified id, it will be updated; otherwise a new event will be created.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.do_upsert_with_http_info(batch_input_marketing_event_create_request_params, async_req=True)
        >>> result = thread.get()

        :param batch_input_marketing_event_create_request_params: The details of the marketing events to upsert (required)
        :type batch_input_marketing_event_create_request_params: BatchInputMarketingEventCreateRequestParams
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
        :rtype: tuple(BatchResponseMarketingEventPublicDefaultResponse, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["batch_input_marketing_event_create_request_params"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method do_upsert" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_input_marketing_event_create_request_params' is set
        if self.api_client.client_side_validation and local_var_params.get("batch_input_marketing_event_create_request_params") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_marketing_event_create_request_params` when calling `do_upsert`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_marketing_event_create_request_params" in local_var_params:
            body_params = local_var_params["batch_input_marketing_event_create_request_params"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "BatchResponseMarketingEventPublicDefaultResponse",
        }

        return self.api_client.call_api(
            "/marketing/v3/marketing-events/events/upsert",
            "POST",
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
