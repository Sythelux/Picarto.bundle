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


class ChannelVideo(object):
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
        'title': 'str',
        'thumbnails': 'Thumbnail',
        'file': 'str',
        'filesize': 'int',
        'duration': 'int',
        'views': 'int',
        'timestamp': 'datetime',
        'adult': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'thumbnails': 'thumbnails',
        'file': 'file',
        'filesize': 'filesize',
        'duration': 'duration',
        'views': 'views',
        'timestamp': 'timestamp',
        'adult': 'adult'
    }

    def __init__(self, title=None, thumbnails=None, file=None, filesize=None, duration=None, views=None, timestamp=None, adult=None):
        """
        ChannelVideo - a model defined in Swagger
        """

        self._title = None
        self._thumbnails = None
        self._file = None
        self._filesize = None
        self._duration = None
        self._views = None
        self._timestamp = None
        self._adult = None

        if title is not None:
          self.title = title
        if thumbnails is not None:
          self.thumbnails = thumbnails
        if file is not None:
          self.file = file
        if filesize is not None:
          self.filesize = filesize
        if duration is not None:
          self.duration = duration
        if views is not None:
          self.views = views
        if timestamp is not None:
          self.timestamp = timestamp
        if adult is not None:
          self.adult = adult

    @property
    def title(self):
        """
        Gets the title of this ChannelVideo.
        The video title

        :return: The title of this ChannelVideo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ChannelVideo.
        The video title

        :param title: The title of this ChannelVideo.
        :type: str
        """

        self._title = title

    @property
    def thumbnails(self):
        """
        Gets the thumbnails of this ChannelVideo.

        :return: The thumbnails of this ChannelVideo.
        :rtype: Thumbnail
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """
        Sets the thumbnails of this ChannelVideo.

        :param thumbnails: The thumbnails of this ChannelVideo.
        :type: Thumbnail
        """

        self._thumbnails = thumbnails

    @property
    def file(self):
        """
        Gets the file of this ChannelVideo.
        The location of the file

        :return: The file of this ChannelVideo.
        :rtype: str
        """
        return self._file

    @file.setter
    def file(self, file):
        """
        Sets the file of this ChannelVideo.
        The location of the file

        :param file: The file of this ChannelVideo.
        :type: str
        """

        self._file = file

    @property
    def filesize(self):
        """
        Gets the filesize of this ChannelVideo.
        Size (in bytes) of the video file

        :return: The filesize of this ChannelVideo.
        :rtype: int
        """
        return self._filesize

    @filesize.setter
    def filesize(self, filesize):
        """
        Sets the filesize of this ChannelVideo.
        Size (in bytes) of the video file

        :param filesize: The filesize of this ChannelVideo.
        :type: int
        """

        self._filesize = filesize

    @property
    def duration(self):
        """
        Gets the duration of this ChannelVideo.
        Duration (in seconds) of the video

        :return: The duration of this ChannelVideo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """
        Sets the duration of this ChannelVideo.
        Duration (in seconds) of the video

        :param duration: The duration of this ChannelVideo.
        :type: int
        """

        self._duration = duration

    @property
    def views(self):
        """
        Gets the views of this ChannelVideo.
        The total number of views this video has

        :return: The views of this ChannelVideo.
        :rtype: int
        """
        return self._views

    @views.setter
    def views(self, views):
        """
        Sets the views of this ChannelVideo.
        The total number of views this video has

        :param views: The views of this ChannelVideo.
        :type: int
        """

        self._views = views

    @property
    def timestamp(self):
        """
        Gets the timestamp of this ChannelVideo.
        The date/time this recording was made

        :return: The timestamp of this ChannelVideo.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this ChannelVideo.
        The date/time this recording was made

        :param timestamp: The timestamp of this ChannelVideo.
        :type: datetime
        """

        self._timestamp = timestamp

    @property
    def adult(self):
        """
        Gets the adult of this ChannelVideo.
        If this video is adult

        :return: The adult of this ChannelVideo.
        :rtype: bool
        """
        return self._adult

    @adult.setter
    def adult(self, adult):
        """
        Sets the adult of this ChannelVideo.
        If this video is adult

        :param adult: The adult of this ChannelVideo.
        :type: bool
        """

        self._adult = adult

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
        if not isinstance(other, ChannelVideo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
