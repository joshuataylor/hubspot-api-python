# coding: utf-8

"""
    URL redirects

    URL redirect operations  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.cms.url_redirects.api_client import ApiClient
from hubspot.cms.url_redirects.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class RedirectsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, url_redirect_id, **kwargs):  # noqa: E501
        """Delete a redirect  # noqa: E501

        Delete one existing redirect, so it is no longer mapped.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive(url_redirect_id, async_req=True)
        >>> result = thread.get()

        :param url_redirect_id: The ID of the target redirect. (required)
        :type url_redirect_id: str
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
        return self.archive_with_http_info(url_redirect_id, **kwargs)  # noqa: E501

    def archive_with_http_info(self, url_redirect_id, **kwargs):  # noqa: E501
        """Delete a redirect  # noqa: E501

        Delete one existing redirect, so it is no longer mapped.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive_with_http_info(url_redirect_id, async_req=True)
        >>> result = thread.get()

        :param url_redirect_id: The ID of the target redirect. (required)
        :type url_redirect_id: str
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

        all_params = ["url_redirect_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'url_redirect_id' is set
        if self.api_client.client_side_validation and local_var_params.get("url_redirect_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `url_redirect_id` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "url_redirect_id" in local_var_params:
            path_params["urlRedirectId"] = local_var_params["url_redirect_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            "/cms/v3/url-redirects/{urlRedirectId}",
            "DELETE",
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

    def create(self, url_mapping_create_request_body, **kwargs):  # noqa: E501
        """Create a redirect  # noqa: E501

        Creates and configures a new URL redirect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(url_mapping_create_request_body, async_req=True)
        >>> result = thread.get()

        :param url_mapping_create_request_body: (required)
        :type url_mapping_create_request_body: UrlMappingCreateRequestBody
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
        :rtype: UrlMapping
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(url_mapping_create_request_body, **kwargs)  # noqa: E501

    def create_with_http_info(self, url_mapping_create_request_body, **kwargs):  # noqa: E501
        """Create a redirect  # noqa: E501

        Creates and configures a new URL redirect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_with_http_info(url_mapping_create_request_body, async_req=True)
        >>> result = thread.get()

        :param url_mapping_create_request_body: (required)
        :type url_mapping_create_request_body: UrlMappingCreateRequestBody
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
        :rtype: tuple(UrlMapping, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["url_mapping_create_request_body"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'url_mapping_create_request_body' is set
        if self.api_client.client_side_validation and local_var_params.get("url_mapping_create_request_body") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `url_mapping_create_request_body` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "url_mapping_create_request_body" in local_var_params:
            body_params = local_var_params["url_mapping_create_request_body"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "POST", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        response_types_map = {
            201: "UrlMapping",
        }

        return self.api_client.call_api(
            "/cms/v3/url-redirects/",
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

    def get_by_id(self, url_redirect_id, **kwargs):  # noqa: E501
        """Get details for a redirect  # noqa: E501

        Returns the details for a single existing URL redirect by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id(url_redirect_id, async_req=True)
        >>> result = thread.get()

        :param url_redirect_id: The ID of the target redirect. (required)
        :type url_redirect_id: str
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
        :rtype: UrlMapping
        """
        kwargs["_return_http_data_only"] = True
        return self.get_by_id_with_http_info(url_redirect_id, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, url_redirect_id, **kwargs):  # noqa: E501
        """Get details for a redirect  # noqa: E501

        Returns the details for a single existing URL redirect by ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_by_id_with_http_info(url_redirect_id, async_req=True)
        >>> result = thread.get()

        :param url_redirect_id: The ID of the target redirect. (required)
        :type url_redirect_id: str
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
        :rtype: tuple(UrlMapping, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["url_redirect_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_by_id" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'url_redirect_id' is set
        if self.api_client.client_side_validation and local_var_params.get("url_redirect_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `url_redirect_id` when calling `get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "url_redirect_id" in local_var_params:
            path_params["urlRedirectId"] = local_var_params["url_redirect_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        response_types_map = {
            200: "UrlMapping",
        }

        return self.api_client.call_api(
            "/cms/v3/url-redirects/{urlRedirectId}",
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

    def get_page(self, **kwargs):  # noqa: E501
        """Get current redirects  # noqa: E501

        Returns all existing URL redirects. Results can be limited and filtered by creation or updated date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page(async_req=True)
        >>> result = thread.get()

        :param created_at: Only return redirects created on exactly this date.
        :type created_at: datetime
        :param created_after: Only return redirects created after this date.
        :type created_after: datetime
        :param created_before: Only return redirects created before this date.
        :type created_before: datetime
        :param updated_at: Only return redirects last updated on exactly this date.
        :type updated_at: datetime
        :param updated_after: Only return redirects last updated after this date.
        :type updated_after: datetime
        :param updated_before: Only return redirects last updated before this date.
        :type updated_before: datetime
        :param sort:
        :type sort: list[str]
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
        :param limit: Maximum number of result per page
        :type limit: int
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
        :rtype: CollectionResponseWithTotalUrlMappingForwardPaging
        """
        kwargs["_return_http_data_only"] = True
        return self.get_page_with_http_info(**kwargs)  # noqa: E501

    def get_page_with_http_info(self, **kwargs):  # noqa: E501
        """Get current redirects  # noqa: E501

        Returns all existing URL redirects. Results can be limited and filtered by creation or updated date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page_with_http_info(async_req=True)
        >>> result = thread.get()

        :param created_at: Only return redirects created on exactly this date.
        :type created_at: datetime
        :param created_after: Only return redirects created after this date.
        :type created_after: datetime
        :param created_before: Only return redirects created before this date.
        :type created_before: datetime
        :param updated_at: Only return redirects last updated on exactly this date.
        :type updated_at: datetime
        :param updated_after: Only return redirects last updated after this date.
        :type updated_after: datetime
        :param updated_before: Only return redirects last updated before this date.
        :type updated_before: datetime
        :param sort:
        :type sort: list[str]
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
        :param limit: Maximum number of result per page
        :type limit: int
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
        :rtype: tuple(CollectionResponseWithTotalUrlMappingForwardPaging, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["created_at", "created_after", "created_before", "updated_at", "updated_after", "updated_before", "sort", "after", "limit", "archived"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_page" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if local_var_params.get("created_at") is not None:  # noqa: E501
            query_params.append(("createdAt", local_var_params["created_at"]))  # noqa: E501
        if local_var_params.get("created_after") is not None:  # noqa: E501
            query_params.append(("createdAfter", local_var_params["created_after"]))  # noqa: E501
        if local_var_params.get("created_before") is not None:  # noqa: E501
            query_params.append(("createdBefore", local_var_params["created_before"]))  # noqa: E501
        if local_var_params.get("updated_at") is not None:  # noqa: E501
            query_params.append(("updatedAt", local_var_params["updated_at"]))  # noqa: E501
        if local_var_params.get("updated_after") is not None:  # noqa: E501
            query_params.append(("updatedAfter", local_var_params["updated_after"]))  # noqa: E501
        if local_var_params.get("updated_before") is not None:  # noqa: E501
            query_params.append(("updatedBefore", local_var_params["updated_before"]))  # noqa: E501
        if local_var_params.get("sort") is not None:  # noqa: E501
            query_params.append(("sort", local_var_params["sort"]))  # noqa: E501
            collection_formats["sort"] = "multi"  # noqa: E501
        if local_var_params.get("after") is not None:  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501
        if local_var_params.get("limit") is not None:  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501
        if local_var_params.get("archived") is not None:  # noqa: E501
            query_params.append(("archived", local_var_params["archived"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        response_types_map = {
            200: "CollectionResponseWithTotalUrlMappingForwardPaging",
        }

        return self.api_client.call_api(
            "/cms/v3/url-redirects/",
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

    def update(self, url_redirect_id, url_mapping, **kwargs):  # noqa: E501
        """Update a redirect  # noqa: E501

        Updates the settings for an existing URL redirect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update(url_redirect_id, url_mapping, async_req=True)
        >>> result = thread.get()

        :param url_redirect_id: (required)
        :type url_redirect_id: str
        :param url_mapping: (required)
        :type url_mapping: UrlMapping
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
        :rtype: UrlMapping
        """
        kwargs["_return_http_data_only"] = True
        return self.update_with_http_info(url_redirect_id, url_mapping, **kwargs)  # noqa: E501

    def update_with_http_info(self, url_redirect_id, url_mapping, **kwargs):  # noqa: E501
        """Update a redirect  # noqa: E501

        Updates the settings for an existing URL redirect.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_with_http_info(url_redirect_id, url_mapping, async_req=True)
        >>> result = thread.get()

        :param url_redirect_id: (required)
        :type url_redirect_id: str
        :param url_mapping: (required)
        :type url_mapping: UrlMapping
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
        :rtype: tuple(UrlMapping, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["url_redirect_id", "url_mapping"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method update" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'url_redirect_id' is set
        if self.api_client.client_side_validation and local_var_params.get("url_redirect_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `url_redirect_id` when calling `update`")  # noqa: E501
        # verify the required parameter 'url_mapping' is set
        if self.api_client.client_side_validation and local_var_params.get("url_mapping") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `url_mapping` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "url_redirect_id" in local_var_params:
            path_params["urlRedirectId"] = local_var_params["url_redirect_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "url_mapping" in local_var_params:
            body_params = local_var_params["url_mapping"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "PATCH", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["hapikey", "oauth2"]  # noqa: E501

        response_types_map = {
            200: "UrlMapping",
        }

        return self.api_client.call_api(
            "/cms/v3/url-redirects/{urlRedirectId}",
            "PATCH",
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
