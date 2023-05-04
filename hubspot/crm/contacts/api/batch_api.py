# coding: utf-8

"""
    Contacts

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.contacts.api_client import ApiClient
from hubspot.crm.contacts.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class BatchApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, batch_input_simple_public_object_id, **kwargs):  # noqa: E501
        """Archive a batch of contacts by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive(batch_input_simple_public_object_id, async_req=True)
        >>> result = thread.get()

        :param batch_input_simple_public_object_id: (required)
        :type batch_input_simple_public_object_id: BatchInputSimplePublicObjectId
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
        return self.archive_with_http_info(batch_input_simple_public_object_id, **kwargs)  # noqa: E501

    def archive_with_http_info(self, batch_input_simple_public_object_id, **kwargs):  # noqa: E501
        """Archive a batch of contacts by ID  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive_with_http_info(batch_input_simple_public_object_id, async_req=True)
        >>> result = thread.get()

        :param batch_input_simple_public_object_id: (required)
        :type batch_input_simple_public_object_id: BatchInputSimplePublicObjectId
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

        all_params = ["batch_input_simple_public_object_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_input_simple_public_object_id' is set
        if self.api_client.client_side_validation and local_var_params.get("batch_input_simple_public_object_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_simple_public_object_id` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_simple_public_object_id" in local_var_params:
            body_params = local_var_params["batch_input_simple_public_object_id"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            "/crm/v3/objects/contacts/batch/archive",
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

    def create(self, batch_input_simple_public_object_input_for_create, **kwargs):  # noqa: E501
        """Create a batch of contacts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(batch_input_simple_public_object_input_for_create, async_req=True)
        >>> result = thread.get()

        :param batch_input_simple_public_object_input_for_create: (required)
        :type batch_input_simple_public_object_input_for_create: BatchInputSimplePublicObjectInputForCreate
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
        :rtype: BatchResponseSimplePublicObject
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(batch_input_simple_public_object_input_for_create, **kwargs)  # noqa: E501

    def create_with_http_info(self, batch_input_simple_public_object_input_for_create, **kwargs):  # noqa: E501
        """Create a batch of contacts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_with_http_info(batch_input_simple_public_object_input_for_create, async_req=True)
        >>> result = thread.get()

        :param batch_input_simple_public_object_input_for_create: (required)
        :type batch_input_simple_public_object_input_for_create: BatchInputSimplePublicObjectInputForCreate
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
        :rtype: tuple(BatchResponseSimplePublicObject, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["batch_input_simple_public_object_input_for_create"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_input_simple_public_object_input_for_create' is set
        if self.api_client.client_side_validation and local_var_params.get("batch_input_simple_public_object_input_for_create") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_simple_public_object_input_for_create` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_simple_public_object_input_for_create" in local_var_params:
            body_params = local_var_params["batch_input_simple_public_object_input_for_create"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        response_types_map = {
            201: "BatchResponseSimplePublicObject",
            207: "BatchResponseSimplePublicObjectWithErrors",
        }

        return self.api_client.call_api(
            "/crm/v3/objects/contacts/batch/create",
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

    def read(self, batch_read_input_simple_public_object_id, **kwargs):  # noqa: E501
        """Read a batch of contacts by internal ID, or unique property values  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read(batch_read_input_simple_public_object_id, async_req=True)
        >>> result = thread.get()

        :param batch_read_input_simple_public_object_id: (required)
        :type batch_read_input_simple_public_object_id: BatchReadInputSimplePublicObjectId
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
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
        :rtype: BatchResponseSimplePublicObject
        """
        kwargs["_return_http_data_only"] = True
        return self.read_with_http_info(batch_read_input_simple_public_object_id, **kwargs)  # noqa: E501

    def read_with_http_info(self, batch_read_input_simple_public_object_id, **kwargs):  # noqa: E501
        """Read a batch of contacts by internal ID, or unique property values  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.read_with_http_info(batch_read_input_simple_public_object_id, async_req=True)
        >>> result = thread.get()

        :param batch_read_input_simple_public_object_id: (required)
        :type batch_read_input_simple_public_object_id: BatchReadInputSimplePublicObjectId
        :param archived: Whether to return only results that have been archived.
        :type archived: bool
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
        :rtype: tuple(BatchResponseSimplePublicObject, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["batch_read_input_simple_public_object_id", "archived"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method read" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_read_input_simple_public_object_id' is set
        if self.api_client.client_side_validation and local_var_params.get("batch_read_input_simple_public_object_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_read_input_simple_public_object_id` when calling `read`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get("archived") is not None:  # noqa: E501
            query_params.append(("archived", local_var_params["archived"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_read_input_simple_public_object_id" in local_var_params:
            body_params = local_var_params["batch_read_input_simple_public_object_id"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        response_types_map = {
            200: "BatchResponseSimplePublicObject",
            207: "BatchResponseSimplePublicObjectWithErrors",
        }

        return self.api_client.call_api(
            "/crm/v3/objects/contacts/batch/read",
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

    def update(self, batch_input_simple_public_object_batch_input, **kwargs):  # noqa: E501
        """Update a batch of contacts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update(batch_input_simple_public_object_batch_input, async_req=True)
        >>> result = thread.get()

        :param batch_input_simple_public_object_batch_input: (required)
        :type batch_input_simple_public_object_batch_input: BatchInputSimplePublicObjectBatchInput
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
        :rtype: BatchResponseSimplePublicObject
        """
        kwargs["_return_http_data_only"] = True
        return self.update_with_http_info(batch_input_simple_public_object_batch_input, **kwargs)  # noqa: E501

    def update_with_http_info(self, batch_input_simple_public_object_batch_input, **kwargs):  # noqa: E501
        """Update a batch of contacts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_with_http_info(batch_input_simple_public_object_batch_input, async_req=True)
        >>> result = thread.get()

        :param batch_input_simple_public_object_batch_input: (required)
        :type batch_input_simple_public_object_batch_input: BatchInputSimplePublicObjectBatchInput
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
        :rtype: tuple(BatchResponseSimplePublicObject, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["batch_input_simple_public_object_batch_input"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method update" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'batch_input_simple_public_object_batch_input' is set
        if self.api_client.client_side_validation and local_var_params.get("batch_input_simple_public_object_batch_input") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `batch_input_simple_public_object_batch_input` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "batch_input_simple_public_object_batch_input" in local_var_params:
            body_params = local_var_params["batch_input_simple_public_object_batch_input"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        response_types_map = {
            200: "BatchResponseSimplePublicObject",
            207: "BatchResponseSimplePublicObjectWithErrors",
        }

        return self.api_client.call_api(
            "/crm/v3/objects/contacts/batch/update",
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
