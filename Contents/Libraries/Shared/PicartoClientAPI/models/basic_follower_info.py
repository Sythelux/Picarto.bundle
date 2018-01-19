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


class BasicFollowerInfo(object):
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
        'online': 'bool',
        'subscriber': 'bool',
        'subscribe_can_expire': 'bool',
        'subscribe_expires': 'date'
    }

    attribute_map = {
        'user_id': 'user_id',
        'name': 'name',
        'avatar': 'avatar',
        'online': 'online',
        'subscriber': 'subscriber',
        'subscribe_can_expire': 'subscribe_can_expire',
        'subscribe_expires': 'subscribe_expires'
    }

    def __init__(self, user_id=None, name=None, avatar=None, online=None, subscriber=None, subscribe_can_expire=None, subscribe_expires=None):
        """
        BasicFollowerInfo - a model defined in Swagger
        """

        self._user_id = None
        self._name = None
        self._avatar = None
        self._online = None
        self._subscriber = None
        self._subscribe_can_expire = None
        self._subscribe_expires = None

        if user_id is not None:
          self.user_id = user_id
        if name is not None:
          self.name = name
        if avatar is not None:
          self.avatar = avatar
        if online is not None:
          self.online = online
        if subscriber is not None:
          self.subscriber = subscriber
        if subscribe_can_expire is not None:
          self.subscribe_can_expire = subscribe_can_expire
        if subscribe_expires is not None:
          self.subscribe_expires = subscribe_expires

    @property
    def user_id(self):
        """
        Gets the user_id of this BasicFollowerInfo.
        The channel's user ID

        :return: The user_id of this BasicFollowerInfo.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this BasicFollowerInfo.
        The channel's user ID

        :param user_id: The user_id of this BasicFollowerInfo.
        :type: int
        """

        self._user_id = user_id

    @property
    def name(self):
        """
        Gets the name of this BasicFollowerInfo.
        The name of the channel

        :return: The name of this BasicFollowerInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this BasicFollowerInfo.
        The name of the channel

        :param name: The name of this BasicFollowerInfo.
        :type: str
        """

        self._name = name

    @property
    def avatar(self):
        """
        Gets the avatar of this BasicFollowerInfo.
        The URI of the user's avatar

        :return: The avatar of this BasicFollowerInfo.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """
        Sets the avatar of this BasicFollowerInfo.
        The URI of the user's avatar

        :param avatar: The avatar of this BasicFollowerInfo.
        :type: str
        """

        self._avatar = avatar

    @property
    def online(self):
        """
        Gets the online of this BasicFollowerInfo.
        If the user is online

        :return: The online of this BasicFollowerInfo.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """
        Sets the online of this BasicFollowerInfo.
        If the user is online

        :param online: The online of this BasicFollowerInfo.
        :type: bool
        """

        self._online = online

    @property
    def subscriber(self):
        """
        Gets the subscriber of this BasicFollowerInfo.
        If this user is a subscriber

        :return: The subscriber of this BasicFollowerInfo.
        :rtype: bool
        """
        return self._subscriber

    @subscriber.setter
    def subscriber(self, subscriber):
        """
        Sets the subscriber of this BasicFollowerInfo.
        If this user is a subscriber

        :param subscriber: The subscriber of this BasicFollowerInfo.
        :type: bool
        """

        self._subscriber = subscriber

    @property
    def subscribe_can_expire(self):
        """
        Gets the subscribe_can_expire of this BasicFollowerInfo.
        If the subscription has an expiry (i.e. is a legacy subscription)

        :return: The subscribe_can_expire of this BasicFollowerInfo.
        :rtype: bool
        """
        return self._subscribe_can_expire

    @subscribe_can_expire.setter
    def subscribe_can_expire(self, subscribe_can_expire):
        """
        Sets the subscribe_can_expire of this BasicFollowerInfo.
        If the subscription has an expiry (i.e. is a legacy subscription)

        :param subscribe_can_expire: The subscribe_can_expire of this BasicFollowerInfo.
        :type: bool
        """

        self._subscribe_can_expire = subscribe_can_expire

    @property
    def subscribe_expires(self):
        """
        Gets the subscribe_expires of this BasicFollowerInfo.
        The date of which this subscription expires - \"0001-01-01\" is no expiry (legacy subscription, recurring)

        :return: The subscribe_expires of this BasicFollowerInfo.
        :rtype: date
        """
        return self._subscribe_expires

    @subscribe_expires.setter
    def subscribe_expires(self, subscribe_expires):
        """
        Sets the subscribe_expires of this BasicFollowerInfo.
        The date of which this subscription expires - \"0001-01-01\" is no expiry (legacy subscription, recurring)

        :param subscribe_expires: The subscribe_expires of this BasicFollowerInfo.
        :type: date
        """

        self._subscribe_expires = subscribe_expires

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
        if not isinstance(other, BasicFollowerInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
