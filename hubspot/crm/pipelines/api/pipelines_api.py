# coding: utf-8

"""
    CRM Pipelines

    Pipelines represent distinct stages in a workflow, like closing a deal or servicing a support ticket. These endpoints provide access to read and modify pipelines in HubSpot. Pipelines support `deals` and `tickets` object types.  ## Pipeline ID validation  When calling endpoints that take pipelineId as a parameter, that ID must correspond to an existing, un-archived pipeline. Otherwise the request will fail with a `404 Not Found` response.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.pipelines.api_client import ApiClient
from hubspot.crm.pipelines.exceptions import (
    ApiTypeError,
    ApiValueError
)


class PipelinesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def archive(self, object_type, pipeline_id, **kwargs):  # noqa: E501
        """Delete a pipeline  # noqa: E501

        Delete the pipeline identified by `{pipelineId}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive(object_type, pipeline_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str pipeline_id: (required)
        :param bool validate_references_before_delete:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.archive_with_http_info(object_type, pipeline_id, **kwargs)  # noqa: E501

    def archive_with_http_info(self, object_type, pipeline_id, **kwargs):  # noqa: E501
        """Delete a pipeline  # noqa: E501

        Delete the pipeline identified by `{pipelineId}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.archive_with_http_info(object_type, pipeline_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str pipeline_id: (required)
        :param bool validate_references_before_delete:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['object_type', 'pipeline_id', 'validate_references_before_delete']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method archive" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `archive`")  # noqa: E501
        # verify the required parameter 'pipeline_id' is set
        if self.api_client.client_side_validation and ('pipeline_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_id` when calling `archive`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501
        if 'pipeline_id' in local_var_params:
            path_params['pipelineId'] = local_var_params['pipeline_id']  # noqa: E501

        query_params = []
        if 'validate_references_before_delete' in local_var_params and local_var_params['validate_references_before_delete'] is not None:  # noqa: E501
            query_params.append(('validateReferencesBeforeDelete', local_var_params['validate_references_before_delete']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/pipelines/{objectType}/{pipelineId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create(self, object_type, pipeline_input, **kwargs):  # noqa: E501
        """Create a pipeline  # noqa: E501

        Create a new pipeline with the provided property values. The entire pipeline object, including its unique ID, will be returned in the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(object_type, pipeline_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param PipelineInput pipeline_input: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Pipeline
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_with_http_info(object_type, pipeline_input, **kwargs)  # noqa: E501

    def create_with_http_info(self, object_type, pipeline_input, **kwargs):  # noqa: E501
        """Create a pipeline  # noqa: E501

        Create a new pipeline with the provided property values. The entire pipeline object, including its unique ID, will be returned in the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(object_type, pipeline_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param PipelineInput pipeline_input: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Pipeline, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['object_type', 'pipeline_input']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `create`")  # noqa: E501
        # verify the required parameter 'pipeline_input' is set
        if self.api_client.client_side_validation and ('pipeline_input' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_input'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_input` when calling `create`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'pipeline_input' in local_var_params:
            body_params = local_var_params['pipeline_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/pipelines/{objectType}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Pipeline',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_all(self, object_type, **kwargs):  # noqa: E501
        """Retrieve all pipelines  # noqa: E501

        Return all pipelines for the object type specified by `{objectType}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all(object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponsePipelineNoPaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_all_with_http_info(object_type, **kwargs)  # noqa: E501

    def get_all_with_http_info(self, object_type, **kwargs):  # noqa: E501
        """Retrieve all pipelines  # noqa: E501

        Return all pipelines for the object type specified by `{objectType}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_all_with_http_info(object_type, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionResponsePipelineNoPaging, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['object_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_all" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `get_all`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/pipelines/{objectType}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionResponsePipelineNoPaging',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_by_id(self, object_type, pipeline_id, **kwargs):  # noqa: E501
        """Return a pipeline by ID  # noqa: E501

        Return a single pipeline object identified by its unique `{pipelineId}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id(object_type, pipeline_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str pipeline_id: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Pipeline
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_by_id_with_http_info(object_type, pipeline_id, **kwargs)  # noqa: E501

    def get_by_id_with_http_info(self, object_type, pipeline_id, **kwargs):  # noqa: E501
        """Return a pipeline by ID  # noqa: E501

        Return a single pipeline object identified by its unique `{pipelineId}`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_by_id_with_http_info(object_type, pipeline_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str pipeline_id: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Pipeline, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['object_type', 'pipeline_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `get_by_id`")  # noqa: E501
        # verify the required parameter 'pipeline_id' is set
        if self.api_client.client_side_validation and ('pipeline_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_id` when calling `get_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501
        if 'pipeline_id' in local_var_params:
            path_params['pipelineId'] = local_var_params['pipeline_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/pipelines/{objectType}/{pipelineId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Pipeline',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def replace(self, object_type, pipeline_id, pipeline_input, **kwargs):  # noqa: E501
        """Replace a pipeline  # noqa: E501

        Replace all the properties of an existing pipeline with the values provided. This will overwrite any existing pipeline stages. The updated pipeline will be returned in the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace(object_type, pipeline_id, pipeline_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str pipeline_id: (required)
        :param PipelineInput pipeline_input: (required)
        :param bool validate_references_before_delete:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Pipeline
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.replace_with_http_info(object_type, pipeline_id, pipeline_input, **kwargs)  # noqa: E501

    def replace_with_http_info(self, object_type, pipeline_id, pipeline_input, **kwargs):  # noqa: E501
        """Replace a pipeline  # noqa: E501

        Replace all the properties of an existing pipeline with the values provided. This will overwrite any existing pipeline stages. The updated pipeline will be returned in the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.replace_with_http_info(object_type, pipeline_id, pipeline_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str pipeline_id: (required)
        :param PipelineInput pipeline_input: (required)
        :param bool validate_references_before_delete:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Pipeline, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['object_type', 'pipeline_id', 'pipeline_input', 'validate_references_before_delete']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method replace" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `replace`")  # noqa: E501
        # verify the required parameter 'pipeline_id' is set
        if self.api_client.client_side_validation and ('pipeline_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_id` when calling `replace`")  # noqa: E501
        # verify the required parameter 'pipeline_input' is set
        if self.api_client.client_side_validation and ('pipeline_input' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_input'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_input` when calling `replace`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501
        if 'pipeline_id' in local_var_params:
            path_params['pipelineId'] = local_var_params['pipeline_id']  # noqa: E501

        query_params = []
        if 'validate_references_before_delete' in local_var_params and local_var_params['validate_references_before_delete'] is not None:  # noqa: E501
            query_params.append(('validateReferencesBeforeDelete', local_var_params['validate_references_before_delete']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'pipeline_input' in local_var_params:
            body_params = local_var_params['pipeline_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/pipelines/{objectType}/{pipelineId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Pipeline',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update(self, object_type, pipeline_id, pipeline_patch_input, **kwargs):  # noqa: E501
        """Update a pipeline  # noqa: E501

        Perform a partial update of the pipeline identified by `{pipelineId}`. The updated pipeline will be returned in the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(object_type, pipeline_id, pipeline_patch_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str pipeline_id: (required)
        :param PipelinePatchInput pipeline_patch_input: (required)
        :param bool validate_references_before_delete:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: Pipeline
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.update_with_http_info(object_type, pipeline_id, pipeline_patch_input, **kwargs)  # noqa: E501

    def update_with_http_info(self, object_type, pipeline_id, pipeline_patch_input, **kwargs):  # noqa: E501
        """Update a pipeline  # noqa: E501

        Perform a partial update of the pipeline identified by `{pipelineId}`. The updated pipeline will be returned in the response.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(object_type, pipeline_id, pipeline_patch_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str object_type: (required)
        :param str pipeline_id: (required)
        :param PipelinePatchInput pipeline_patch_input: (required)
        :param bool validate_references_before_delete:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(Pipeline, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['object_type', 'pipeline_id', 'pipeline_patch_input', 'validate_references_before_delete']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'object_type' is set
        if self.api_client.client_side_validation and ('object_type' not in local_var_params or  # noqa: E501
                                                        local_var_params['object_type'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `object_type` when calling `update`")  # noqa: E501
        # verify the required parameter 'pipeline_id' is set
        if self.api_client.client_side_validation and ('pipeline_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_id` when calling `update`")  # noqa: E501
        # verify the required parameter 'pipeline_patch_input' is set
        if self.api_client.client_side_validation and ('pipeline_patch_input' not in local_var_params or  # noqa: E501
                                                        local_var_params['pipeline_patch_input'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `pipeline_patch_input` when calling `update`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'object_type' in local_var_params:
            path_params['objectType'] = local_var_params['object_type']  # noqa: E501
        if 'pipeline_id' in local_var_params:
            path_params['pipelineId'] = local_var_params['pipeline_id']  # noqa: E501

        query_params = []
        if 'validate_references_before_delete' in local_var_params and local_var_params['validate_references_before_delete'] is not None:  # noqa: E501
            query_params.append(('validateReferencesBeforeDelete', local_var_params['validate_references_before_delete']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'pipeline_patch_input' in local_var_params:
            body_params = local_var_params['pipeline_patch_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/pipelines/{objectType}/{pipelineId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Pipeline',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
