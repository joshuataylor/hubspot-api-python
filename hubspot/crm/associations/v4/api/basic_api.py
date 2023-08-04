# coding: utf-8

"""
    CrmPublicObjectsService

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v4
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.associations.v4.api_client import ApiClient
from hubspot.crm.associations.v4.exceptions import ApiTypeError, ApiValueError  # noqa: F401


class BasicApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, object_type, object_id, to_object_type, to_object_id, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        deletes all associations between two records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive(object_type, object_id, to_object_type, to_object_id, async_req=True)
        >>> result = thread.get()

        :param object_type: (required)
        :type object_type: str
        :param object_id: (required)
        :type object_id: int
        :param to_object_type: (required)
        :type to_object_type: str
        :param to_object_id: (required)
        :type to_object_id: int
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
        return self.archive_with_http_info(object_type, object_id, to_object_type, to_object_id, **kwargs)  # noqa: E501

    def archive_with_http_info(self, object_type, object_id, to_object_type, to_object_id, **kwargs):  # noqa: E501
        """Delete  # noqa: E501

        deletes all associations between two records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.archive_with_http_info(object_type, object_id, to_object_type, to_object_id, async_req=True)
        >>> result = thread.get()

        :param object_type: (required)
        :type object_type: str
        :param object_id: (required)
        :type object_id: int
        :param to_object_type: (required)
        :type to_object_type: str
        :param to_object_id: (required)
        :type to_object_id: int
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

        all_params = ["object_type", "object_id", "to_object_type", "to_object_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method archive" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and local_var_params.get("object_type") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `archive`")  # noqa: E501
        # verify the required parameter 'object_id' is set
        if self.api_client.client_side_validation and local_var_params.get("object_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_id` when calling `archive`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and local_var_params.get("to_object_type") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `archive`")  # noqa: E501
        # verify the required parameter 'to_object_id' is set
        if self.api_client.client_side_validation and local_var_params.get("to_object_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_id` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501
        if "object_id" in local_var_params:
            path_params["objectId"] = local_var_params["object_id"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501
        if "to_object_id" in local_var_params:
            path_params["toObjectId"] = local_var_params["to_object_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {}

        return self.api_client.call_api(
            "/crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}",
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

    def create(self, object_type, object_id, to_object_type, to_object_id, association_spec, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Set association labels between two records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(object_type, object_id, to_object_type, to_object_id, association_spec, async_req=True)
        >>> result = thread.get()

        :param object_type: (required)
        :type object_type: str
        :param object_id: (required)
        :type object_id: int
        :param to_object_type: (required)
        :type to_object_type: str
        :param to_object_id: (required)
        :type to_object_id: int
        :param association_spec: (required)
        :type association_spec: list[AssociationSpec]
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
        :rtype: LabelsBetweenObjectPair
        """
        kwargs["_return_http_data_only"] = True
        return self.create_with_http_info(object_type, object_id, to_object_type, to_object_id, association_spec, **kwargs)  # noqa: E501

    def create_with_http_info(self, object_type, object_id, to_object_type, to_object_id, association_spec, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Set association labels between two records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_with_http_info(object_type, object_id, to_object_type, to_object_id, association_spec, async_req=True)
        >>> result = thread.get()

        :param object_type: (required)
        :type object_type: str
        :param object_id: (required)
        :type object_id: int
        :param to_object_type: (required)
        :type to_object_type: str
        :param to_object_id: (required)
        :type to_object_id: int
        :param association_spec: (required)
        :type association_spec: list[AssociationSpec]
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
        :rtype: tuple(LabelsBetweenObjectPair, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["object_type", "object_id", "to_object_type", "to_object_id", "association_spec"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and local_var_params.get("object_type") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `create`")  # noqa: E501
        # verify the required parameter 'object_id' is set
        if self.api_client.client_side_validation and local_var_params.get("object_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_id` when calling `create`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and local_var_params.get("to_object_type") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `create`")  # noqa: E501
        # verify the required parameter 'to_object_id' is set
        if self.api_client.client_side_validation and local_var_params.get("to_object_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_id` when calling `create`")  # noqa: E501
        # verify the required parameter 'association_spec' is set
        if self.api_client.client_side_validation and local_var_params.get("association_spec") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `association_spec` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501
        if "object_id" in local_var_params:
            path_params["objectId"] = local_var_params["object_id"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501
        if "to_object_id" in local_var_params:
            path_params["toObjectId"] = local_var_params["to_object_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        if "association_spec" in local_var_params:
            body_params = local_var_params["association_spec"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # HTTP header `Content-Type`
        content_types_list = local_var_params.get("_content_type", self.api_client.select_header_content_type(["application/json"], "PUT", body_params))  # noqa: E501
        if content_types_list:
            header_params["Content-Type"] = content_types_list

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            201: "LabelsBetweenObjectPair",
        }

        return self.api_client.call_api(
            "/crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}/{toObjectId}",
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

    def create_default(self, from_object_type, from_object_id, to_object_type, to_object_id, **kwargs):  # noqa: E501
        """Create Default  # noqa: E501

        Create the default (most generic) association type between two object types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_default(from_object_type, from_object_id, to_object_type, to_object_id, async_req=True)
        >>> result = thread.get()

        :param from_object_type: (required)
        :type from_object_type: str
        :param from_object_id: (required)
        :type from_object_id: int
        :param to_object_type: (required)
        :type to_object_type: str
        :param to_object_id: (required)
        :type to_object_id: int
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
        :rtype: BatchResponsePublicDefaultAssociation
        """
        kwargs["_return_http_data_only"] = True
        return self.create_default_with_http_info(from_object_type, from_object_id, to_object_type, to_object_id, **kwargs)  # noqa: E501

    def create_default_with_http_info(self, from_object_type, from_object_id, to_object_type, to_object_id, **kwargs):  # noqa: E501
        """Create Default  # noqa: E501

        Create the default (most generic) association type between two object types  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_default_with_http_info(from_object_type, from_object_id, to_object_type, to_object_id, async_req=True)
        >>> result = thread.get()

        :param from_object_type: (required)
        :type from_object_type: str
        :param from_object_id: (required)
        :type from_object_id: int
        :param to_object_type: (required)
        :type to_object_type: str
        :param to_object_id: (required)
        :type to_object_id: int
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
        :rtype: tuple(BatchResponsePublicDefaultAssociation, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["from_object_type", "from_object_id", "to_object_type", "to_object_id"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method create_default" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'from_object_type' is set
        if self.api_client.client_side_validation and local_var_params.get("from_object_type") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_type` when calling `create_default`")  # noqa: E501
        # verify the required parameter 'from_object_id' is set
        if self.api_client.client_side_validation and local_var_params.get("from_object_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `from_object_id` when calling `create_default`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and local_var_params.get("to_object_type") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `create_default`")  # noqa: E501
        # verify the required parameter 'to_object_id' is set
        if self.api_client.client_side_validation and local_var_params.get("to_object_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_id` when calling `create_default`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "from_object_type" in local_var_params:
            path_params["fromObjectType"] = local_var_params["from_object_type"]  # noqa: E501
        if "from_object_id" in local_var_params:
            path_params["fromObjectId"] = local_var_params["from_object_id"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501
        if "to_object_id" in local_var_params:
            path_params["toObjectId"] = local_var_params["to_object_id"]  # noqa: E501

        query_params = []

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "BatchResponsePublicDefaultAssociation",
        }

        return self.api_client.call_api(
            "/crm/v4/objects/{fromObjectType}/{fromObjectId}/associations/default/{toObjectType}/{toObjectId}",
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

    def get_page(self, object_type, object_id, to_object_type, **kwargs):  # noqa: E501
        """List  # noqa: E501

        List all associations of an object by object type. Limit 500 per call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page(object_type, object_id, to_object_type, async_req=True)
        >>> result = thread.get()

        :param object_type: (required)
        :type object_type: str
        :param object_id: (required)
        :type object_id: int
        :param to_object_type: (required)
        :type to_object_type: str
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
        :param limit: The maximum number of results to display per page.
        :type limit: int
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
        :rtype: CollectionResponseMultiAssociatedObjectWithLabelForwardPaging
        """
        kwargs["_return_http_data_only"] = True
        return self.get_page_with_http_info(object_type, object_id, to_object_type, **kwargs)  # noqa: E501

    def get_page_with_http_info(self, object_type, object_id, to_object_type, **kwargs):  # noqa: E501
        """List  # noqa: E501

        List all associations of an object by object type. Limit 500 per call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_page_with_http_info(object_type, object_id, to_object_type, async_req=True)
        >>> result = thread.get()

        :param object_type: (required)
        :type object_type: str
        :param object_id: (required)
        :type object_id: int
        :param to_object_type: (required)
        :type to_object_type: str
        :param after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :type after: str
        :param limit: The maximum number of results to display per page.
        :type limit: int
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
        :rtype: tuple(CollectionResponseMultiAssociatedObjectWithLabelForwardPaging, status_code(int), headers(HTTPHeaderDict))
        """

        local_var_params = locals()

        all_params = ["object_type", "object_id", "to_object_type", "after", "limit"]
        all_params.extend(["async_req", "_return_http_data_only", "_preload_content", "_request_timeout", "_request_auth", "_content_type", "_headers"])

        for key, val in six.iteritems(local_var_params["kwargs"]):
            if key not in all_params:
                raise ApiTypeError("Got an unexpected keyword argument '%s'" " to method get_page" % key)
            local_var_params[key] = val
        del local_var_params["kwargs"]
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and local_var_params.get("object_type") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `get_page`")  # noqa: E501
        # verify the required parameter 'object_id' is set
        if self.api_client.client_side_validation and local_var_params.get("object_id") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_id` when calling `get_page`")  # noqa: E501
        # verify the required parameter 'to_object_type' is set
        if self.api_client.client_side_validation and local_var_params.get("to_object_type") is None:  # noqa: E501
            raise ApiValueError("Missing the required parameter `to_object_type` when calling `get_page`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "object_type" in local_var_params:
            path_params["objectType"] = local_var_params["object_type"]  # noqa: E501
        if "object_id" in local_var_params:
            path_params["objectId"] = local_var_params["object_id"]  # noqa: E501
        if "to_object_type" in local_var_params:
            path_params["toObjectType"] = local_var_params["to_object_type"]  # noqa: E501

        query_params = []
        if local_var_params.get("after") is not None:  # noqa: E501
            query_params.append(("after", local_var_params["after"]))  # noqa: E501
        if local_var_params.get("limit") is not None:  # noqa: E501
            query_params.append(("limit", local_var_params["limit"]))  # noqa: E501

        header_params = dict(local_var_params.get("_headers", {}))

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(["application/json", "*/*"])  # noqa: E501

        # Authentication setting
        auth_settings = ["oauth2"]  # noqa: E501

        response_types_map = {
            200: "CollectionResponseMultiAssociatedObjectWithLabelForwardPaging",
        }

        return self.api_client.call_api(
            "/crm/v4/objects/{objectType}/{objectId}/associations/{toObjectType}",
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