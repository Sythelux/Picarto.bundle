# coding: utf-8

"""
    Picarto.TV API Documentation

    The Picarto.TV API documentation  Note, for fixed access tokens, the header that needs to be sent is of the format: `Authorization: Bearer yourTokenHere`  This can be generated at https://oauth.picarto.tv/  For chat API, see https://docs.picarto.tv/chat/chat.proto - contact via the email below for implementation details 

    OpenAPI spec version: 1.2.5
    Contact: api@picarto.tv
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
import re


class VideoSearchResult(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'channel': 'BasicChannelInfo',
        'video': 'ChannelVideo'
    }

    attribute_map = {
        'channel': 'channel',
        'video': 'video'
    }

    def __init__(self, channel=None, video=None):
        """
        VideoSearchResult - a model defined in Swagger
        """

        self._channel = None
        self._video = None

        if channel is not None:
          self.channel = channel
        if video is not None:
          self.video = video

    @property
    def channel(self):
        """
        Gets the channel of this VideoSearchResult.

        :return: The channel of this VideoSearchResult.
        :rtype: BasicChannelInfo
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """
        Sets the channel of this VideoSearchResult.

        :param channel: The channel of this VideoSearchResult.
        :type: BasicChannelInfo
        """

        self._channel = channel

    @property
    def video(self):
        """
        Gets the video of this VideoSearchResult.

        :return: The video of this VideoSearchResult.
        :rtype: ChannelVideo
        """
        return self._video

    @video.setter
    def video(self, video):
        """
        Sets the video of this VideoSearchResult.

        :param video: The video of this VideoSearchResult.
        :type: ChannelVideo
        """

        self._video = video

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in self.swagger_types.iteritems():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, VideoSearchResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
