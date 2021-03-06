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


class DescriptionPanel(object):
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
        'body': 'str',
        'image': 'str',
        'image_link': 'str',
        'button_text': 'str',
        'button_link': 'str',
        'position': 'int'
    }

    attribute_map = {
        'title': 'title',
        'body': 'body',
        'image': 'image',
        'image_link': 'image_link',
        'button_text': 'button_text',
        'button_link': 'button_link',
        'position': 'position'
    }

    def __init__(self, title=None, body=None, image=None, image_link=None, button_text=None, button_link=None, position=None):
        """
        DescriptionPanel - a model defined in Swagger
        """

        self._title = None
        self._body = None
        self._image = None
        self._image_link = None
        self._button_text = None
        self._button_link = None
        self._position = None

        if title is not None:
          self.title = title
        if body is not None:
          self.body = body
        if image is not None:
          self.image = image
        if image_link is not None:
          self.image_link = image_link
        if button_text is not None:
          self.button_text = button_text
        if button_link is not None:
          self.button_link = button_link
        if position is not None:
          self.position = position

    @property
    def title(self):
        """
        Gets the title of this DescriptionPanel.
        The description panel's title

        :return: The title of this DescriptionPanel.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this DescriptionPanel.
        The description panel's title

        :param title: The title of this DescriptionPanel.
        :type: str
        """

        self._title = title

    @property
    def body(self):
        """
        Gets the body of this DescriptionPanel.
        The description panel's body

        :return: The body of this DescriptionPanel.
        :rtype: str
        """
        return self._body

    @body.setter
    def body(self, body):
        """
        Sets the body of this DescriptionPanel.
        The description panel's body

        :param body: The body of this DescriptionPanel.
        :type: str
        """

        self._body = body

    @property
    def image(self):
        """
        Gets the image of this DescriptionPanel.
        The description panel's attached image URL, if it exists

        :return: The image of this DescriptionPanel.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """
        Sets the image of this DescriptionPanel.
        The description panel's attached image URL, if it exists

        :param image: The image of this DescriptionPanel.
        :type: str
        """

        self._image = image

    @property
    def image_link(self):
        """
        Gets the image_link of this DescriptionPanel.
        The attached image's link, if the image is set.

        :return: The image_link of this DescriptionPanel.
        :rtype: str
        """
        return self._image_link

    @image_link.setter
    def image_link(self, image_link):
        """
        Sets the image_link of this DescriptionPanel.
        The attached image's link, if the image is set.

        :param image_link: The image_link of this DescriptionPanel.
        :type: str
        """

        self._image_link = image_link

    @property
    def button_text(self):
        """
        Gets the button_text of this DescriptionPanel.
        The button's text, if enabled

        :return: The button_text of this DescriptionPanel.
        :rtype: str
        """
        return self._button_text

    @button_text.setter
    def button_text(self, button_text):
        """
        Sets the button_text of this DescriptionPanel.
        The button's text, if enabled

        :param button_text: The button_text of this DescriptionPanel.
        :type: str
        """

        self._button_text = button_text

    @property
    def button_link(self):
        """
        Gets the button_link of this DescriptionPanel.
        The button's url, if enabled (can be an email)

        :return: The button_link of this DescriptionPanel.
        :rtype: str
        """
        return self._button_link

    @button_link.setter
    def button_link(self, button_link):
        """
        Sets the button_link of this DescriptionPanel.
        The button's url, if enabled (can be an email)

        :param button_link: The button_link of this DescriptionPanel.
        :type: str
        """

        self._button_link = button_link

    @property
    def position(self):
        """
        Gets the position of this DescriptionPanel.
        The order at which this is sorted (just for convenience, can just use array index)

        :return: The position of this DescriptionPanel.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """
        Sets the position of this DescriptionPanel.
        The order at which this is sorted (just for convenience, can just use array index)

        :param position: The position of this DescriptionPanel.
        :type: int
        """

        self._position = position

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
        if not isinstance(other, DescriptionPanel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
