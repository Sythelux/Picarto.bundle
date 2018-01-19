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


class BasicChannelInfo(object):
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
        'user_id': 'int',
        'name': 'str',
        'avatar': 'str',
        'online': 'bool'
    }

    attribute_map = {
        'user_id': 'user_id',
        'name': 'name',
        'avatar': 'avatar',
        'online': 'online'
    }

    def __init__(self, user_id=None, name=None, avatar=None, online=None):
        """
        BasicChannelInfo - a model defined in Swagger
        """

        self._user_id = None
        self._name = None
        self._avatar = None
        self._online = None

        if user_id is not None:
          self.user_id = user_id
        if name is not None:
          self.name = name
        if avatar is not None:
          self.avatar = avatar
        if online is not None:
          self.online = online

    @property
    def user_id(self):
        """
        Gets the user_id of this BasicChannelInfo.
        The channel's user ID

        :return: The user_id of this BasicChannelInfo.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this BasicChannelInfo.
        The channel's user ID

        :param user_id: The user_id of this BasicChannelInfo.
        :type: int
        """

        self._user_id = user_id

    @property
    def name(self):
        """
        Gets the name of this BasicChannelInfo.
        The name of the channel

        :return: The name of this BasicChannelInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BasicChannelInfo.
        The name of the channel

        :param name: The name of this BasicChannelInfo.
        :type: str
        """

        self._name = name

    @property
    def avatar(self):
        """
        Gets the avatar of this BasicChannelInfo.
        The URI of the user's avatar

        :return: The avatar of this BasicChannelInfo.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """
        Sets the avatar of this BasicChannelInfo.
        The URI of the user's avatar

        :param avatar: The avatar of this BasicChannelInfo.
        :type: str
        """

        self._avatar = avatar

    @property
    def online(self):
        """
        Gets the online of this BasicChannelInfo.
        If the user is online

        :return: The online of this BasicChannelInfo.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """
        Sets the online of this BasicChannelInfo.
        If the user is online

        :param online: The online of this BasicChannelInfo.
        :type: bool
        """

        self._online = online

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
        if not isinstance(other, BasicChannelInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
