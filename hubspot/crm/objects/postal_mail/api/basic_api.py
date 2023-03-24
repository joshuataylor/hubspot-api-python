# coding: utf-8

"""
    Postal Mail

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from hubspot.crm.objects.postal_mail.api_client import ApiClient
from hubspot.crm.objects.postal_mail.exceptions import (
    ApiTypeError,
    ApiValueError
)


class BasicApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_crm_v3_objects_postal_mail_postal_mail(self, postal_mail, **kwargs):  # noqa: E501
        """Archive  # noqa: E501

        Move an Object identified by `{postalMail}` to the recycling bin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_crm_v3_objects_postal_mail_postal_mail(postal_mail, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str postal_mail: (required)
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
        return self.delete_crm_v3_objects_postal_mail_postal_mail_with_http_info(postal_mail, **kwargs)  # noqa: E501

    def delete_crm_v3_objects_postal_mail_postal_mail_with_http_info(self, postal_mail, **kwargs):  # noqa: E501
        """Archive  # noqa: E501

        Move an Object identified by `{postalMail}` to the recycling bin.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_crm_v3_objects_postal_mail_postal_mail_with_http_info(postal_mail, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str postal_mail: (required)
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

        all_params = ['postal_mail']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_crm_v3_objects_postal_mail_postal_mail" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'postal_mail' is set
        if self.api_client.client_side_validation and ('postal_mail' not in local_var_params or  # noqa: E501
                                                        local_var_params['postal_mail'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `postal_mail` when calling `delete_crm_v3_objects_postal_mail_postal_mail`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'postal_mail' in local_var_params:
            path_params['postalMail'] = local_var_params['postal_mail']  # noqa: E501

        query_params = []

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
            '/crm/v3/objects/postal mail/{postalMail}', 'DELETE',
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

    def get_crm_v3_objects_postal_mail(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        Read a page of postal mail. Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_crm_v3_objects_postal_mail(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: The maximum number of results to display per page.
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool archived: Whether to return only results that have been archived.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CollectionResponseSimplePublicObjectWithAssociationsForwardPaging
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_crm_v3_objects_postal_mail_with_http_info(**kwargs)  # noqa: E501

    def get_crm_v3_objects_postal_mail_with_http_info(self, **kwargs):  # noqa: E501
        """List  # noqa: E501

        Read a page of postal mail. Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_crm_v3_objects_postal_mail_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit: The maximum number of results to display per page.
        :param str after: The paging cursor token of the last successfully read resource will be returned as the `paging.next.after` JSON property of a paged response containing more results.
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored. Usage of this parameter will reduce the maximum number of objects that can be read by a single request.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool archived: Whether to return only results that have been archived.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CollectionResponseSimplePublicObjectWithAssociationsForwardPaging, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit', 'after', 'properties', 'properties_with_history', 'associations', 'archived']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_crm_v3_objects_postal_mail" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in local_var_params and local_var_params['limit'] is not None:  # noqa: E501
            query_params.append(('limit', local_var_params['limit']))  # noqa: E501
        if 'after' in local_var_params and local_var_params['after'] is not None:  # noqa: E501
            query_params.append(('after', local_var_params['after']))  # noqa: E501
        if 'properties' in local_var_params and local_var_params['properties'] is not None:  # noqa: E501
            query_params.append(('properties', local_var_params['properties']))  # noqa: E501
            collection_formats['properties'] = 'multi'  # noqa: E501
        if 'properties_with_history' in local_var_params and local_var_params['properties_with_history'] is not None:  # noqa: E501
            query_params.append(('propertiesWithHistory', local_var_params['properties_with_history']))  # noqa: E501
            collection_formats['propertiesWithHistory'] = 'multi'  # noqa: E501
        if 'associations' in local_var_params and local_var_params['associations'] is not None:  # noqa: E501
            query_params.append(('associations', local_var_params['associations']))  # noqa: E501
            collection_formats['associations'] = 'multi'  # noqa: E501
        if 'archived' in local_var_params and local_var_params['archived'] is not None:  # noqa: E501
            query_params.append(('archived', local_var_params['archived']))  # noqa: E501

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
            '/crm/v3/objects/postal mail', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionResponseSimplePublicObjectWithAssociationsForwardPaging',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_crm_v3_objects_postal_mail_postal_mail(self, postal_mail, **kwargs):  # noqa: E501
        """Read  # noqa: E501

        Read an Object identified by `{postalMail}`. `{postalMail}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_crm_v3_objects_postal_mail_postal_mail(postal_mail, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str postal_mail: (required)
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool archived: Whether to return only results that have been archived.
        :param str id_property: The name of a property whose values are unique for this object type
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SimplePublicObjectWithAssociations
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.get_crm_v3_objects_postal_mail_postal_mail_with_http_info(postal_mail, **kwargs)  # noqa: E501

    def get_crm_v3_objects_postal_mail_postal_mail_with_http_info(self, postal_mail, **kwargs):  # noqa: E501
        """Read  # noqa: E501

        Read an Object identified by `{postalMail}`. `{postalMail}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param.  Control what is returned via the `properties` query param.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_crm_v3_objects_postal_mail_postal_mail_with_http_info(postal_mail, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str postal_mail: (required)
        :param list[str] properties: A comma separated list of the properties to be returned in the response. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] properties_with_history: A comma separated list of the properties to be returned along with their history of previous values. If any of the specified properties are not present on the requested object(s), they will be ignored.
        :param list[str] associations: A comma separated list of object types to retrieve associated IDs for. If any of the specified associations do not exist, they will be ignored.
        :param bool archived: Whether to return only results that have been archived.
        :param str id_property: The name of a property whose values are unique for this object type
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SimplePublicObjectWithAssociations, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['postal_mail', 'properties', 'properties_with_history', 'associations', 'archived', 'id_property']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_crm_v3_objects_postal_mail_postal_mail" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'postal_mail' is set
        if self.api_client.client_side_validation and ('postal_mail' not in local_var_params or  # noqa: E501
                                                        local_var_params['postal_mail'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `postal_mail` when calling `get_crm_v3_objects_postal_mail_postal_mail`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'postal_mail' in local_var_params:
            path_params['postalMail'] = local_var_params['postal_mail']  # noqa: E501

        query_params = []
        if 'properties' in local_var_params and local_var_params['properties'] is not None:  # noqa: E501
            query_params.append(('properties', local_var_params['properties']))  # noqa: E501
            collection_formats['properties'] = 'multi'  # noqa: E501
        if 'properties_with_history' in local_var_params and local_var_params['properties_with_history'] is not None:  # noqa: E501
            query_params.append(('propertiesWithHistory', local_var_params['properties_with_history']))  # noqa: E501
            collection_formats['propertiesWithHistory'] = 'multi'  # noqa: E501
        if 'associations' in local_var_params and local_var_params['associations'] is not None:  # noqa: E501
            query_params.append(('associations', local_var_params['associations']))  # noqa: E501
            collection_formats['associations'] = 'multi'  # noqa: E501
        if 'archived' in local_var_params and local_var_params['archived'] is not None:  # noqa: E501
            query_params.append(('archived', local_var_params['archived']))  # noqa: E501
        if 'id_property' in local_var_params and local_var_params['id_property'] is not None:  # noqa: E501
            query_params.append(('idProperty', local_var_params['id_property']))  # noqa: E501

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
            '/crm/v3/objects/postal mail/{postalMail}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimplePublicObjectWithAssociations',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def patch_crm_v3_objects_postal_mail_postal_mail(self, postal_mail, simple_public_object_input, **kwargs):  # noqa: E501
        """Update  # noqa: E501

        Perform a partial update of an Object identified by `{postalMail}`. `{postalMail}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param. Provided property values will be overwritten. Read-only and non-existent properties will be ignored. Properties values can be cleared by passing an empty string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_crm_v3_objects_postal_mail_postal_mail(postal_mail, simple_public_object_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str postal_mail: (required)
        :param SimplePublicObjectInput simple_public_object_input: (required)
        :param str id_property: The name of a property whose values are unique for this object type
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.patch_crm_v3_objects_postal_mail_postal_mail_with_http_info(postal_mail, simple_public_object_input, **kwargs)  # noqa: E501

    def patch_crm_v3_objects_postal_mail_postal_mail_with_http_info(self, postal_mail, simple_public_object_input, **kwargs):  # noqa: E501
        """Update  # noqa: E501

        Perform a partial update of an Object identified by `{postalMail}`. `{postalMail}` refers to the internal object ID by default, or optionally any unique property value as specified by the `idProperty` query param. Provided property values will be overwritten. Read-only and non-existent properties will be ignored. Properties values can be cleared by passing an empty string.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.patch_crm_v3_objects_postal_mail_postal_mail_with_http_info(postal_mail, simple_public_object_input, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str postal_mail: (required)
        :param SimplePublicObjectInput simple_public_object_input: (required)
        :param str id_property: The name of a property whose values are unique for this object type
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['postal_mail', 'simple_public_object_input', 'id_property']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method patch_crm_v3_objects_postal_mail_postal_mail" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'postal_mail' is set
        if self.api_client.client_side_validation and ('postal_mail' not in local_var_params or  # noqa: E501
                                                        local_var_params['postal_mail'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `postal_mail` when calling `patch_crm_v3_objects_postal_mail_postal_mail`")  # noqa: E501
        # verify the required parameter 'simple_public_object_input' is set
        if self.api_client.client_side_validation and ('simple_public_object_input' not in local_var_params or  # noqa: E501
                                                        local_var_params['simple_public_object_input'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `simple_public_object_input` when calling `patch_crm_v3_objects_postal_mail_postal_mail`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'postal_mail' in local_var_params:
            path_params['postalMail'] = local_var_params['postal_mail']  # noqa: E501

        query_params = []
        if 'id_property' in local_var_params and local_var_params['id_property'] is not None:  # noqa: E501
            query_params.append(('idProperty', local_var_params['id_property']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'simple_public_object_input' in local_var_params:
            body_params = local_var_params['simple_public_object_input']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/objects/postal mail/{postalMail}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimplePublicObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def post_crm_v3_objects_postal_mail(self, simple_public_object_input_for_create, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Create a postal mail with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard postal mail is provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_crm_v3_objects_postal_mail(simple_public_object_input_for_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SimplePublicObjectInputForCreate simple_public_object_input_for_create: (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: SimplePublicObject
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.post_crm_v3_objects_postal_mail_with_http_info(simple_public_object_input_for_create, **kwargs)  # noqa: E501

    def post_crm_v3_objects_postal_mail_with_http_info(self, simple_public_object_input_for_create, **kwargs):  # noqa: E501
        """Create  # noqa: E501

        Create a postal mail with the given properties and return a copy of the object, including the ID. Documentation and examples for creating standard postal mail is provided.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.post_crm_v3_objects_postal_mail_with_http_info(simple_public_object_input_for_create, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param SimplePublicObjectInputForCreate simple_public_object_input_for_create: (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(SimplePublicObject, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['simple_public_object_input_for_create']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method post_crm_v3_objects_postal_mail" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'simple_public_object_input_for_create' is set
        if self.api_client.client_side_validation and ('simple_public_object_input_for_create' not in local_var_params or  # noqa: E501
                                                        local_var_params['simple_public_object_input_for_create'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `simple_public_object_input_for_create` when calling `post_crm_v3_objects_postal_mail`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'simple_public_object_input_for_create' in local_var_params:
            body_params = local_var_params['simple_public_object_input_for_create']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', '*/*'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['hapikey', 'oauth2']  # noqa: E501

        return self.api_client.call_api(
            '/crm/v3/objects/postal mail', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SimplePublicObject',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
