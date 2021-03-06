# coding: utf-8

"""
    Picarto.TV API Documentation

    The Picarto.TV API documentation  Note, for fixed access tokens, the header that needs to be sent is of the format: `Authorization: Bearer yourTokenHere`  This can be generated at https://oauth.picarto.tv/  For chat API, see https://docs.picarto.tv/chat/chat.proto - contact via the email below for implementation details 

    OpenAPI spec version: 1.2.5
    Contact: api@picarto.tv
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


class ChannelApi(object):
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

    def channel_id_channel_id_get(self, channel_id, **kwargs):
        """
        Gets information about a channel by ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.channel_id_channel_id_get(channel_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int channel_id: Channel ID of user you wish to read (required)
        :return: ChannelDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.channel_id_channel_id_get_with_http_info(channel_id, **kwargs)
        else:
            (data) = self.channel_id_channel_id_get_with_http_info(channel_id, **kwargs)
            return data

    def channel_id_channel_id_get_with_http_info(self, channel_id, **kwargs):
        """
        Gets information about a channel by ID
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.channel_id_channel_id_get_with_http_info(channel_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int channel_id: Channel ID of user you wish to read (required)
        :return: ChannelDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channel_id_channel_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params) or (params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `channel_id_channel_id_get`")


        collection_formats = {}

        path_params = {}
        if 'channel_id' in params:
            path_params['channel_id'] = params['channel_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/channel/id/{channel_id}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ChannelDetails',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def channel_id_channel_id_videos_get(self, channel_id, **kwargs):
        """
        Get all videos for a channel by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.channel_id_channel_id_videos_get(channel_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int channel_id: Channel ID of the user you want to get videos for (required)
        :return: ChannelVideos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.channel_id_channel_id_videos_get_with_http_info(channel_id, **kwargs)
        else:
            (data) = self.channel_id_channel_id_videos_get_with_http_info(channel_id, **kwargs)
            return data

    def channel_id_channel_id_videos_get_with_http_info(self, channel_id, **kwargs):
        """
        Get all videos for a channel by id
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.channel_id_channel_id_videos_get_with_http_info(channel_id, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param int channel_id: Channel ID of the user you want to get videos for (required)
        :return: ChannelVideos
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_id']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channel_id_channel_id_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_id' is set
        if ('channel_id' not in params) or (params['channel_id'] is None):
            raise ValueError("Missing the required parameter `channel_id` when calling `channel_id_channel_id_videos_get`")


        collection_formats = {}

        path_params = {}
        if 'channel_id' in params:
            path_params['channel_id'] = params['channel_id']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/channel/id/{channel_id}/videos', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ChannelVideos',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def channel_name_channel_name_get(self, channel_name, **kwargs):
        """
        Gets information about a channel by name
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.channel_name_channel_name_get(channel_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str channel_name: Channel name of user you wish to read (required)
        :return: ChannelDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.channel_name_channel_name_get_with_http_info(channel_name, **kwargs)
        else:
            (data) = self.channel_name_channel_name_get_with_http_info(channel_name, **kwargs)
            return data

    def channel_name_channel_name_get_with_http_info(self, channel_name, **kwargs):
        """
        Gets information about a channel by name
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.channel_name_channel_name_get_with_http_info(channel_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str channel_name: Channel name of user you wish to read (required)
        :return: ChannelDetails
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channel_name_channel_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_name' is set
        if ('channel_name' not in params) or (params['channel_name'] is None):
            raise ValueError("Missing the required parameter `channel_name` when calling `channel_name_channel_name_get`")


        collection_formats = {}

        path_params = {}
        if 'channel_name' in params:
            path_params['channel_name'] = params['channel_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/channel/name/{channel_name}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ChannelDetails',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def channel_name_channel_name_videos_get(self, channel_name, **kwargs):
        """
        Get all videos for a channel by name
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.channel_name_channel_name_videos_get(channel_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str channel_name: Channel name of the user you want to get videos for (required)
        :return: ChannelVideos
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.channel_name_channel_name_videos_get_with_http_info(channel_name, **kwargs)
        else:
            (data) = self.channel_name_channel_name_videos_get_with_http_info(channel_name, **kwargs)
            return data

    def channel_name_channel_name_videos_get_with_http_info(self, channel_name, **kwargs):
        """
        Get all videos for a channel by name
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.channel_name_channel_name_videos_get_with_http_info(channel_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str channel_name: Channel name of the user you want to get videos for (required)
        :return: ChannelVideos
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['channel_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method channel_name_channel_name_videos_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'channel_name' is set
        if ('channel_name' not in params) or (params['channel_name'] is None):
            raise ValueError("Missing the required parameter `channel_name` when calling `channel_name_channel_name_videos_get`")


        collection_formats = {}

        path_params = {}
        if 'channel_name' in params:
            path_params['channel_name'] = params['channel_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.\
            select_header_accept(['application/json; charset=utf-8', 'text/plain; charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api('/channel/name/{channel_name}/videos', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ChannelVideos',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
