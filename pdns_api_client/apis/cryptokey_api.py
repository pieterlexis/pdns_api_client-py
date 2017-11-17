# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.0.10
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class CryptokeyApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_crypto_key(self, server_id, zone_id, metadata, **kwargs):
        """
        Creates a Cryptokey
        This method adds a new key to a zone. The key can either be generated or imported by supplying the content parameter. if content, bits and algo are null, a key will be generated based on the default-ksk-algorithm and default-ksk-size settings for a KSK and the default-zsk-algorithm and default-zsk-size options for a ZSK.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_crypto_key(server_id, zone_id, metadata, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: (required)
        :param Cryptokey metadata: List of metadata to add/create (required)
        :return: Cryptokey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_crypto_key_with_http_info(server_id, zone_id, metadata, **kwargs)
        else:
            (data) = self.create_crypto_key_with_http_info(server_id, zone_id, metadata, **kwargs)
            return data

    def create_crypto_key_with_http_info(self, server_id, zone_id, metadata, **kwargs):
        """
        Creates a Cryptokey
        This method adds a new key to a zone. The key can either be generated or imported by supplying the content parameter. if content, bits and algo are null, a key will be generated based on the default-ksk-algorithm and default-ksk-size settings for a KSK and the default-zsk-algorithm and default-zsk-size options for a ZSK.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_crypto_key_with_http_info(server_id, zone_id, metadata, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: (required)
        :param Cryptokey metadata: List of metadata to add/create (required)
        :return: Cryptokey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'zone_id', 'metadata']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_crypto_key" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params) or (params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `create_crypto_key`")
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params) or (params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `create_crypto_key`")
        # verify the required parameter 'metadata' is set
        if ('metadata' not in params) or (params['metadata'] is None):
            raise ValueError("Missing the required parameter `metadata` when calling `create_crypto_key`")


        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']
        if 'zone_id' in params:
            path_params['zone_id'] = params['zone_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'metadata' in params:
            body_params = params['metadata']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APIKeyHeader']

        return self.api_client.call_api('/servers/{server_id}/zones/{zone_id}/cryptokeys', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Cryptokey',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_cryptokey(self, server_id, zone_id, cryptokey_id, **kwargs):
        """
        This method deletes a key specified by cryptokey_id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_cryptokey(server_id, zone_id, cryptokey_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :param str cryptokey_id: The id value of the Cryptokey (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, **kwargs)
        else:
            (data) = self.delete_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, **kwargs)
            return data

    def delete_cryptokey_with_http_info(self, server_id, zone_id, cryptokey_id, **kwargs):
        """
        This method deletes a key specified by cryptokey_id.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :param str cryptokey_id: The id value of the Cryptokey (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'zone_id', 'cryptokey_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_cryptokey" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params) or (params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `delete_cryptokey`")
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params) or (params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `delete_cryptokey`")
        # verify the required parameter 'cryptokey_id' is set
        if ('cryptokey_id' not in params) or (params['cryptokey_id'] is None):
            raise ValueError("Missing the required parameter `cryptokey_id` when calling `delete_cryptokey`")


        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']
        if 'zone_id' in params:
            path_params['zone_id'] = params['zone_id']
        if 'cryptokey_id' in params:
            path_params['cryptokey_id'] = params['cryptokey_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APIKeyHeader']

        return self.api_client.call_api('/servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_cryptokey(self, server_id, zone_id, cryptokey_id, **kwargs):
        """
        Returns all data about the CryptoKey, including the privatekey.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_cryptokey(server_id, zone_id, cryptokey_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :param str cryptokey_id: The id value of the CryptoKey (required)
        :return: Cryptokey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, **kwargs)
        else:
            (data) = self.list_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, **kwargs)
            return data

    def list_cryptokey_with_http_info(self, server_id, zone_id, cryptokey_id, **kwargs):
        """
        Returns all data about the CryptoKey, including the privatekey.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :param str cryptokey_id: The id value of the CryptoKey (required)
        :return: Cryptokey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'zone_id', 'cryptokey_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_cryptokey" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params) or (params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `list_cryptokey`")
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params) or (params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `list_cryptokey`")
        # verify the required parameter 'cryptokey_id' is set
        if ('cryptokey_id' not in params) or (params['cryptokey_id'] is None):
            raise ValueError("Missing the required parameter `cryptokey_id` when calling `list_cryptokey`")


        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']
        if 'zone_id' in params:
            path_params['zone_id'] = params['zone_id']
        if 'cryptokey_id' in params:
            path_params['cryptokey_id'] = params['cryptokey_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APIKeyHeader']

        return self.api_client.call_api('/servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='Cryptokey',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def list_zone_crypto_keys(self, server_id, zone_id, **kwargs):
        """
        Get all CryptoKeys for a zone, except the privatekey
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_zone_crypto_keys(server_id, zone_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :return: list[Cryptokey]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.list_zone_crypto_keys_with_http_info(server_id, zone_id, **kwargs)
        else:
            (data) = self.list_zone_crypto_keys_with_http_info(server_id, zone_id, **kwargs)
            return data

    def list_zone_crypto_keys_with_http_info(self, server_id, zone_id, **kwargs):
        """
        Get all CryptoKeys for a zone, except the privatekey
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.list_zone_crypto_keys_with_http_info(server_id, zone_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: The id of the zone to retrieve (required)
        :return: list[Cryptokey]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'zone_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_zone_crypto_keys" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params) or (params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `list_zone_crypto_keys`")
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params) or (params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `list_zone_crypto_keys`")


        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']
        if 'zone_id' in params:
            path_params['zone_id'] = params['zone_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APIKeyHeader']

        return self.api_client.call_api('/servers/{server_id}/zones/{zone_id}/cryptokeys', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[Cryptokey]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def modify_cryptokey(self, server_id, zone_id, cryptokey_id, cryptokey, **kwargs):
        """
        This method (de)activates a key from zone_name specified by cryptokey_id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.modify_cryptokey(server_id, zone_id, cryptokey_id, cryptokey, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: (required)
        :param str cryptokey_id: Cryptokey to manipulate (required)
        :param Cryptokey cryptokey: the Cryptokey (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.modify_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, cryptokey, **kwargs)
        else:
            (data) = self.modify_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, cryptokey, **kwargs)
            return data

    def modify_cryptokey_with_http_info(self, server_id, zone_id, cryptokey_id, cryptokey, **kwargs):
        """
        This method (de)activates a key from zone_name specified by cryptokey_id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.modify_cryptokey_with_http_info(server_id, zone_id, cryptokey_id, cryptokey, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str zone_id: (required)
        :param str cryptokey_id: Cryptokey to manipulate (required)
        :param Cryptokey cryptokey: the Cryptokey (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'zone_id', 'cryptokey_id', 'cryptokey']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method modify_cryptokey" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params) or (params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `modify_cryptokey`")
        # verify the required parameter 'zone_id' is set
        if ('zone_id' not in params) or (params['zone_id'] is None):
            raise ValueError("Missing the required parameter `zone_id` when calling `modify_cryptokey`")
        # verify the required parameter 'cryptokey_id' is set
        if ('cryptokey_id' not in params) or (params['cryptokey_id'] is None):
            raise ValueError("Missing the required parameter `cryptokey_id` when calling `modify_cryptokey`")
        # verify the required parameter 'cryptokey' is set
        if ('cryptokey' not in params) or (params['cryptokey'] is None):
            raise ValueError("Missing the required parameter `cryptokey` when calling `modify_cryptokey`")


        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']
        if 'zone_id' in params:
            path_params['zone_id'] = params['zone_id']
        if 'cryptokey_id' in params:
            path_params['cryptokey_id'] = params['cryptokey_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'cryptokey' in params:
            body_params = params['cryptokey']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['application/json'])

        # Authentication setting
        auth_settings = ['APIKeyHeader']

        return self.api_client.call_api('/servers/{server_id}/zones/{zone_id}/cryptokeys/{cryptokey_id}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type=None,
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)