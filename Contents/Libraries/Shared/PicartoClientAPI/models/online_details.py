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


class OnlineDetails(object):
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
        'title': 'str',
        'viewers': 'int',
        'thumbnails': 'Thumbnail',
        'category': 'str',
        'account_type': 'str',
        'adult': 'bool',
        'gaming': 'bool',
        'commissions': 'bool',
        'multistream': 'bool',
        'languages': 'Languages'
    }

    attribute_map = {
        'user_id': 'user_id',
        'name': 'name',
        'title': 'title',
        'viewers': 'viewers',
        'thumbnails': 'thumbnails',
        'category': 'category',
        'account_type': 'account_type',
        'adult': 'adult',
        'gaming': 'gaming',
        'commissions': 'commissions',
        'multistream': 'multistream',
        'languages': 'languages'
    }

    def __init__(self, user_id=None, name=None, title=None, viewers=None, thumbnails=None, category=None, account_type=None, adult=None, gaming=None, commissions=None, multistream=None, languages=None):
        """
        OnlineDetails - a model defined in Swagger
        """

        self._user_id = None
        self._name = None
        self._title = None
        self._viewers = None
        self._thumbnails = None
        self._category = None
        self._account_type = None
        self._adult = None
        self._gaming = None
        self._commissions = None
        self._multistream = None
        self._languages = None

        if user_id is not None:
          self.user_id = user_id
        if name is not None:
          self.name = name
        if title is not None:
          self.title = title
        if viewers is not None:
          self.viewers = viewers
        if thumbnails is not None:
          self.thumbnails = thumbnails
        if category is not None:
          self.category = category
        if account_type is not None:
          self.account_type = account_type
        if adult is not None:
          self.adult = adult
        if gaming is not None:
          self.gaming = gaming
        if commissions is not None:
          self.commissions = commissions
        if multistream is not None:
          self.multistream = multistream
        if languages is not None:
          self.languages = languages

    @property
    def user_id(self):
        """
        Gets the user_id of this OnlineDetails.
        The channel's user ID

        :return: The user_id of this OnlineDetails.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this OnlineDetails.
        The channel's user ID

        :param user_id: The user_id of this OnlineDetails.
        :type: int
        """

        self._user_id = user_id

    @property
    def name(self):
        """
        Gets the name of this OnlineDetails.
        The name of the channel

        :return: The name of this OnlineDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this OnlineDetails.
        The name of the channel

        :param name: The name of this OnlineDetails.
        :type: str
        """

        self._name = name

    @property
    def title(self):
        """
        Gets the title of this OnlineDetails.
        The channel title

        :return: The title of this OnlineDetails.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this OnlineDetails.
        The channel title

        :param title: The title of this OnlineDetails.
        :type: str
        """

        self._title = title

    @property
    def viewers(self):
        """
        Gets the viewers of this OnlineDetails.
        The number of current viewers watching this stream

        :return: The viewers of this OnlineDetails.
        :rtype: int
        """
        return self._viewers

    @viewers.setter
    def viewers(self, viewers):
        """
        Sets the viewers of this OnlineDetails.
        The number of current viewers watching this stream

        :param viewers: The viewers of this OnlineDetails.
        :type: int
        """

        self._viewers = viewers

    @property
    def thumbnails(self):
        """
        Gets the thumbnails of this OnlineDetails.

        :return: The thumbnails of this OnlineDetails.
        :rtype: Thumbnail
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """
        Sets the thumbnails of this OnlineDetails.

        :param thumbnails: The thumbnails of this OnlineDetails.
        :type: Thumbnail
        """

        self._thumbnails = thumbnails

    @property
    def category(self):
        """
        Gets the category of this OnlineDetails.
        The category this stream is in

        :return: The category of this OnlineDetails.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this OnlineDetails.
        The category this stream is in

        :param category: The category of this OnlineDetails.
        :type: str
        """

        self._category = category

    @property
    def account_type(self):
        """
        Gets the account_type of this OnlineDetails.
        The account type of the channel

        :return: The account_type of this OnlineDetails.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this OnlineDetails.
        The account type of the channel

        :param account_type: The account_type of this OnlineDetails.
        :type: str
        """
        allowed_values = ["free", "basic", "premium"]
        if account_type not in allowed_values:
            raise ValueError(
                "Invalid value for `account_type` ({0}), must be one of {1}"
                .format(account_type, allowed_values)
            )

        self._account_type = account_type

    @property
    def adult(self):
        """
        Gets the adult of this OnlineDetails.
        If this channel is marked as adult

        :return: The adult of this OnlineDetails.
        :rtype: bool
        """
        return self._adult

    @adult.setter
    def adult(self, adult):
        """
        Sets the adult of this OnlineDetails.
        If this channel is marked as adult

        :param adult: The adult of this OnlineDetails.
        :type: bool
        """

        self._adult = adult

    @property
    def gaming(self):
        """
        Gets the gaming of this OnlineDetails.
        If this channel is gaming

        :return: The gaming of this OnlineDetails.
        :rtype: bool
        """
        return self._gaming

    @gaming.setter
    def gaming(self, gaming):
        """
        Sets the gaming of this OnlineDetails.
        If this channel is gaming

        :param gaming: The gaming of this OnlineDetails.
        :type: bool
        """

        self._gaming = gaming

    @property
    def commissions(self):
        """
        Gets the commissions of this OnlineDetails.
        If this channel is accepting commissions

        :return: The commissions of this OnlineDetails.
        :rtype: bool
        """
        return self._commissions

    @commissions.setter
    def commissions(self, commissions):
        """
        Sets the commissions of this OnlineDetails.
        If this channel is accepting commissions

        :param commissions: The commissions of this OnlineDetails.
        :type: bool
        """

        self._commissions = commissions

    @property
    def multistream(self):
        """
        Gets the multistream of this OnlineDetails.
        If this channel is hosting or participating in a multistream

        :return: The multistream of this OnlineDetails.
        :rtype: bool
        """
        return self._multistream

    @multistream.setter
    def multistream(self, multistream):
        """
        Sets the multistream of this OnlineDetails.
        If this channel is hosting or participating in a multistream

        :param multistream: The multistream of this OnlineDetails.
        :type: bool
        """

        self._multistream = multistream

    @property
    def languages(self):
        """
        Gets the languages of this OnlineDetails.

        :return: The languages of this OnlineDetails.
        :rtype: Languages
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """
        Sets the languages of this OnlineDetails.

        :param languages: The languages of this OnlineDetails.
        :type: Languages
        """

        self._languages = languages

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
        if not isinstance(other, OnlineDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
