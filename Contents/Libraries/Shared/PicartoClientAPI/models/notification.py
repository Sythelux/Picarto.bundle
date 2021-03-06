# coding: utf-8

"""
    Picarto.TV API Documentation

    The Picarto.TV API documentation  Note, for fixed access tokens, the header that needs to be sent is of the format: `Authorization: Bearer yourTokenHere`  This can be generated at https://oauth.picarto.tv/  For chat API, see https://docs.picarto.tv/chat/chat.proto - contact via the email below for implementation details 

    OpenAPI spec version: 1.2.5
    Contact: api@picarto.tv
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class Notification(object):
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
        'type': 'str',
        'uuid': 'str',
        'body': 'str',
        'uri': 'str',
        'timestamp': 'int'
    }

    attribute_map = {
        'type': 'type',
        'uuid': 'uuid',
        'body': 'body',
        'uri': 'uri',
        'timestamp': 'timestamp'
    }

    def __init__(self, type=None, uuid=None, body=None, uri=None, timestamp=None):
        """
        Notification - a model defined in Swagger
        """

        self._type = None
        self._uuid = None
        self._body = None
        self._uri = None
        self._timestamp = None

        if type is not None:
          self.type = type
        if uuid is not None:
          self.uuid = uuid
        if body is not None:
          self.body = body
        if uri is not None:
          self.uri = uri
        if timestamp is not None:
          self.timestamp = timestamp

    @property
    def type(self):
        """
        Gets the type of this Notification.
        The notification type

        :return: The type of this Notification.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this Notification.
        The notification type

        :param type: The type of this Notification.
        :type: str
        """

        self._type = type

    @property
    def uuid(self):
        """
        Gets the uuid of this Notification.
        The notification UUID

        :return: The uuid of this Notification.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """
        Sets the uuid of this Notification.
        The notification UUID

        :param uuid: The uuid of this Notification.
        :type: str
        """

        self._uuid = uuid

    @property
    def body(self):
        """
        Gets the body of this Notification.
        The content of the notification (HTML)

        :return: The body of this Notification.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this Notification.
        The content of the notification (HTML)

        :param body: The body of this Notification.
        :type: str
        """

        self._body = body

    @property
    def uri(self):
        """
        Gets the uri of this Notification.
        URI this notification links to (may be unused)

        :return: The uri of this Notification.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        """
        Sets the uri of this Notification.
        URI this notification links to (may be unused)

        :param uri: The uri of this Notification.
        :type: str
        """

        self._uri = uri

    @property
    def timestamp(self):
        """
        Gets the timestamp of this Notification.
        Unix timestamp of when this notification was created

        :return: The timestamp of this Notification.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """
        Sets the timestamp of this Notification.
        Unix timestamp of when this notification was created

        :param timestamp: The timestamp of this Notification.
        :type: int
        """

        self._timestamp = timestamp

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        if not isinstance(other, Notification):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
