# coding: utf-8

"""
    PowerDNS Authoritative HTTP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 0.0.12
    
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


class SearchApi(object):
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

    def search_data(self, server_id, q, max, **kwargs):
        """
        Search the data inside PowerDNS
        Search the data inside PowerDNS for search_term and return at most max_results. This includes zones, records and comments. The * character can be used in search_term as a wildcard character and the ? character can be used as a wildcard for a single character.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_data(server_id, q, max, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str q: The string to search for (required)
        :param int max: Maximum number of entries to return (required)
        :return: SearchResults
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_data_with_http_info(server_id, q, max, **kwargs)
        else:
            (data) = self.search_data_with_http_info(server_id, q, max, **kwargs)
            return data

    def search_data_with_http_info(self, server_id, q, max, **kwargs):
        """
        Search the data inside PowerDNS
        Search the data inside PowerDNS for search_term and return at most max_results. This includes zones, records and comments. The * character can be used in search_term as a wildcard character and the ? character can be used as a wildcard for a single character.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_data_with_http_info(server_id, q, max, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str q: The string to search for (required)
        :param int max: Maximum number of entries to return (required)
        :return: SearchResults
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'q', 'max']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_data" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params) or (params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `search_data`")
        # verify the required parameter 'q' is set
        if ('q' not in params) or (params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `search_data`")
        # verify the required parameter 'max' is set
        if ('max' not in params) or (params['max'] is None):
            raise ValueError("Missing the required parameter `max` when calling `search_data`")


        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))
        if 'max' in params:
            query_params.append(('max', params['max']))

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

        return self.api_client.call_api('/servers/{server_id}/search-data', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='SearchResults',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def search_log(self, server_id, q, **kwargs):
        """
        Query the log, filtered by search_term.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_log(server_id, q, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str q: The string to search for (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.search_log_with_http_info(server_id, q, **kwargs)
        else:
            (data) = self.search_log_with_http_info(server_id, q, **kwargs)
            return data

    def search_log_with_http_info(self, server_id, q, **kwargs):
        """
        Query the log, filtered by search_term.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.search_log_with_http_info(server_id, q, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str server_id: The id of the server to retrieve (required)
        :param str q: The string to search for (required)
        :return: list[str]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['server_id', 'q']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search_log" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'server_id' is set
        if ('server_id' not in params) or (params['server_id'] is None):
            raise ValueError("Missing the required parameter `server_id` when calling `search_log`")
        # verify the required parameter 'q' is set
        if ('q' not in params) or (params['q'] is None):
            raise ValueError("Missing the required parameter `q` when calling `search_log`")


        collection_formats = {}

        path_params = {}
        if 'server_id' in params:
            path_params['server_id'] = params['server_id']

        query_params = []
        if 'q' in params:
            query_params.append(('q', params['q']))

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

        return self.api_client.call_api('/servers/{server_id}/search-log', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='list[str]',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
