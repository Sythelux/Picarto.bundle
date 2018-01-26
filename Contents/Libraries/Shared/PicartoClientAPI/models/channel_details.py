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


class ChannelDetails(object):
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
        'viewers': 'int',
        'viewers_total': 'int',
        'thumbnails': 'Thumbnail',
        'followers': 'int',
        'subscribers': 'int',
        'adult': 'bool',
        'category': 'str',
        'account_type': 'str',
        'commissions': 'bool',
        'recordings': 'bool',
        'title': 'str',
        'description_panels': 'list[DescriptionPanel]',
        'private': 'bool',
        'gaming': 'bool',
        'guest_chat': 'bool',
        'last_live': 'datetime',
        'tags': 'list[str]',
        'multistream': 'list[MultiParticipant]',
        'languages': 'Languages'
    }

    attribute_map = {
        'user_id': 'user_id',
        'name': 'name',
        'avatar': 'avatar',
        'online': 'online',
        'viewers': 'viewers',
        'viewers_total': 'viewers_total',
        'thumbnails': 'thumbnails',
        'followers': 'followers',
        'subscribers': 'subscribers',
        'adult': 'adult',
        'category': 'category',
        'account_type': 'account_type',
        'commissions': 'commissions',
        'recordings': 'recordings',
        'title': 'title',
        'description_panels': 'description_panels',
        'private': 'private',
        'gaming': 'gaming',
        'guest_chat': 'guest_chat',
        'last_live': 'last_live',
        'tags': 'tags',
        'multistream': 'multistream',
        'languages': 'languages'
    }

    def __init__(self, user_id=None, name=None, avatar=None, online=None, viewers=None, viewers_total=None, thumbnails=None, followers=None, subscribers=None, adult=None, category=None, account_type=None, commissions=None, recordings=None, title=None, description_panels=None, private=None, gaming=None, guest_chat=None, last_live=None, tags=None, multistream=None, languages=None):
        """
        ChannelDetails - a model defined in Swagger
        """

        self._user_id = None
        self._name = None
        self._avatar = None
        self._online = None
        self._viewers = None
        self._viewers_total = None
        self._thumbnails = None
        self._followers = None
        self._subscribers = None
        self._adult = None
        self._category = None
        self._account_type = None
        self._commissions = None
        self._recordings = None
        self._title = None
        self._description_panels = None
        self._private = None
        self._gaming = None
        self._guest_chat = None
        self._last_live = None
        self._tags = None
        self._multistream = None
        self._languages = None

        if user_id is not None:
          self.user_id = user_id
        if name is not None:
          self.name = name
        if avatar is not None:
          self.avatar = avatar
        if online is not None:
          self.online = online
        if viewers is not None:
          self.viewers = viewers
        if viewers_total is not None:
          self.viewers_total = viewers_total
        if thumbnails is not None:
          self.thumbnails = thumbnails
        if followers is not None:
          self.followers = followers
        if subscribers is not None:
          self.subscribers = subscribers
        if adult is not None:
          self.adult = adult
        if category is not None:
          self.category = category
        if account_type is not None:
          self.account_type = account_type
        if commissions is not None:
          self.commissions = commissions
        if recordings is not None:
          self.recordings = recordings
        if title is not None:
          self.title = title
        if description_panels is not None:
          self.description_panels = description_panels
        if private is not None:
          self.private = private
        if gaming is not None:
          self.gaming = gaming
        if guest_chat is not None:
          self.guest_chat = guest_chat
        if last_live is not None:
          self.last_live = last_live
        if tags is not None:
          self.tags = tags
        if multistream is not None:
          self.multistream = multistream
        if languages is not None:
          self.languages = languages

    @property
    def user_id(self):
        """
        Gets the user_id of this ChannelDetails.
        The channel's user ID

        :return: The user_id of this ChannelDetails.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """
        Sets the user_id of this ChannelDetails.
        The channel's user ID

        :param user_id: The user_id of this ChannelDetails.
        :type: int
        """

        self._user_id = user_id

    @property
    def name(self):
        """
        Gets the name of this ChannelDetails.
        The name of the channel

        :return: The name of this ChannelDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ChannelDetails.
        The name of the channel

        :param name: The name of this ChannelDetails.
        :type: str
        """

        self._name = name

    @property
    def avatar(self):
        """
        Gets the avatar of this ChannelDetails.
        The URI of the user's avatar

        :return: The avatar of this ChannelDetails.
        :rtype: str
        """
        return self._avatar

    @avatar.setter
    def avatar(self, avatar):
        """
        Sets the avatar of this ChannelDetails.
        The URI of the user's avatar

        :param avatar: The avatar of this ChannelDetails.
        :type: str
        """

        self._avatar = avatar

    @property
    def online(self):
        """
        Gets the online of this ChannelDetails.
        If the channel is online

        :return: The online of this ChannelDetails.
        :rtype: bool
        """
        return self._online

    @online.setter
    def online(self, online):
        """
        Sets the online of this ChannelDetails.
        If the channel is online

        :param online: The online of this ChannelDetails.
        :type: bool
        """

        self._online = online

    @property
    def viewers(self):
        """
        Gets the viewers of this ChannelDetails.
        The number of current viewers watching this stream (0 if offline)

        :return: The viewers of this ChannelDetails.
        :rtype: int
        """
        return self._viewers

    @viewers.setter
    def viewers(self, viewers):
        """
        Sets the viewers of this ChannelDetails.
        The number of current viewers watching this stream (0 if offline)

        :param viewers: The viewers of this ChannelDetails.
        :type: int
        """

        self._viewers = viewers

    @property
    def viewers_total(self):
        """
        Gets the viewers_total of this ChannelDetails.
        The total number of viewers this channel has had since the beginning of time

        :return: The viewers_total of this ChannelDetails.
        :rtype: int
        """
        return self._viewers_total

    @viewers_total.setter
    def viewers_total(self, viewers_total):
        """
        Sets the viewers_total of this ChannelDetails.
        The total number of viewers this channel has had since the beginning of time

        :param viewers_total: The viewers_total of this ChannelDetails.
        :type: int
        """

        self._viewers_total = viewers_total

    @property
    def thumbnails(self):
        """
        Gets the thumbnails of this ChannelDetails.

        :return: The thumbnails of this ChannelDetails.
        :rtype: Thumbnail
        """
        return self._thumbnails

    @thumbnails.setter
    def thumbnails(self, thumbnails):
        """
        Sets the thumbnails of this ChannelDetails.

        :param thumbnails: The thumbnails of this ChannelDetails.
        :type: Thumbnail
        """

        self._thumbnails = thumbnails

    @property
    def followers(self):
        """
        Gets the followers of this ChannelDetails.
        The total number of people following this streamer

        :return: The followers of this ChannelDetails.
        :rtype: int
        """
        return self._followers

    @followers.setter
    def followers(self, followers):
        """
        Sets the followers of this ChannelDetails.
        The total number of people following this streamer

        :param followers: The followers of this ChannelDetails.
        :type: int
        """

        self._followers = followers

    @property
    def subscribers(self):
        """
        Gets the subscribers of this ChannelDetails.
        The total number of people subscribed to this streamer

        :return: The subscribers of this ChannelDetails.
        :rtype: int
        """
        return self._subscribers

    @subscribers.setter
    def subscribers(self, subscribers):
        """
        Sets the subscribers of this ChannelDetails.
        The total number of people subscribed to this streamer

        :param subscribers: The subscribers of this ChannelDetails.
        :type: int
        """

        self._subscribers = subscribers

    @property
    def adult(self):
        """
        Gets the adult of this ChannelDetails.
        If this channel is an adult channel

        :return: The adult of this ChannelDetails.
        :rtype: bool
        """
        return self._adult

    @adult.setter
    def adult(self, adult):
        """
        Sets the adult of this ChannelDetails.
        If this channel is an adult channel

        :param adult: The adult of this ChannelDetails.
        :type: bool
        """

        self._adult = adult

    @property
    def category(self):
        """
        Gets the category of this ChannelDetails.
        The name of the category this stream is in

        :return: The category of this ChannelDetails.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this ChannelDetails.
        The name of the category this stream is in

        :param category: The category of this ChannelDetails.
        :type: str
        """

        self._category = category

    @property
    def account_type(self):
        """
        Gets the account_type of this ChannelDetails.
        The account type of the channel

        :return: The account_type of this ChannelDetails.
        :rtype: str
        """
        return self._account_type

    @account_type.setter
    def account_type(self, account_type):
        """
        Sets the account_type of this ChannelDetails.
        The account type of the channel

        :param account_type: The account_type of this ChannelDetails.
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
    def commissions(self):
        """
        Gets the commissions of this ChannelDetails.
        If this channel is accepting commissions

        :return: The commissions of this ChannelDetails.
        :rtype: bool
        """
        return self._commissions

    @commissions.setter
    def commissions(self, commissions):
        """
        Sets the commissions of this ChannelDetails.
        If this channel is accepting commissions

        :param commissions: The commissions of this ChannelDetails.
        :type: bool
        """

        self._commissions = commissions

    @property
    def recordings(self):
        """
        Gets the recordings of this ChannelDetails.
        If recordings are enabled and videos are accessible

        :return: The recordings of this ChannelDetails.
        :rtype: bool
        """
        return self._recordings

    @recordings.setter
    def recordings(self, recordings):
        """
        Sets the recordings of this ChannelDetails.
        If recordings are enabled and videos are accessible

        :param recordings: The recordings of this ChannelDetails.
        :type: bool
        """

        self._recordings = recordings

    @property
    def title(self):
        """
        Gets the title of this ChannelDetails.
        This channel's title

        :return: The title of this ChannelDetails.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """
        Sets the title of this ChannelDetails.
        This channel's title

        :param title: The title of this ChannelDetails.
        :type: str
        """

        self._title = title

    @property
    def description_panels(self):
        """
        Gets the description_panels of this ChannelDetails.
        This channel's description panels

        :return: The description_panels of this ChannelDetails.
        :rtype: list[DescriptionPanel]
        """
        return self._description_panels

    @description_panels.setter
    def description_panels(self, description_panels):
        """
        Sets the description_panels of this ChannelDetails.
        This channel's description panels

        :param description_panels: The description_panels of this ChannelDetails.
        :type: list[DescriptionPanel]
        """

        self._description_panels = description_panels

    @property
    def private(self):
        """
        Gets the private of this ChannelDetails.
        If this channel is in private mode

        :return: The private of this ChannelDetails.
        :rtype: bool
        """
        return self._private

    @private.setter
    def private(self, private):
        """
        Sets the private of this ChannelDetails.
        If this channel is in private mode

        :param private: The private of this ChannelDetails.
        :type: bool
        """

        self._private = private

    @property
    def gaming(self):
        """
        Gets the gaming of this ChannelDetails.
        If this channel is in game mode

        :return: The gaming of this ChannelDetails.
        :rtype: bool
        """
        return self._gaming

    @gaming.setter
    def gaming(self, gaming):
        """
        Sets the gaming of this ChannelDetails.
        If this channel is in game mode

        :param gaming: The gaming of this ChannelDetails.
        :type: bool
        """

        self._gaming = gaming

    @property
    def guest_chat(self):
        """
        Gets the guest_chat of this ChannelDetails.
        If guest (unregistered) users can talk in chat

        :return: The guest_chat of this ChannelDetails.
        :rtype: bool
        """
        return self._guest_chat

    @guest_chat.setter
    def guest_chat(self, guest_chat):
        """
        Sets the guest_chat of this ChannelDetails.
        If guest (unregistered) users can talk in chat

        :param guest_chat: The guest_chat of this ChannelDetails.
        :type: bool
        """

        self._guest_chat = guest_chat

    @property
    def last_live(self):
        """
        Gets the last_live of this ChannelDetails.
        The date/time this user was last live

        :return: The last_live of this ChannelDetails.
        :rtype: datetime
        """
        return self._last_live

    @last_live.setter
    def last_live(self, last_live):
        """
        Sets the last_live of this ChannelDetails.
        The date/time this user was last live

        :param last_live: The last_live of this ChannelDetails.
        :type: datetime
        """

        self._last_live = last_live

    @property
    def tags(self):
        """
        Gets the tags of this ChannelDetails.
        A list of tags

        :return: The tags of this ChannelDetails.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """
        Sets the tags of this ChannelDetails.
        A list of tags

        :param tags: The tags of this ChannelDetails.
        :type: list[str]
        """

        self._tags = tags

    @property
    def multistream(self):
        """
        Gets the multistream of this ChannelDetails.
        A list of channels we are multistreaming with

        :return: The multistream of this ChannelDetails.
        :rtype: list[MultiParticipant]
        """
        return self._multistream

    @multistream.setter
    def multistream(self, multistream):
        """
        Sets the multistream of this ChannelDetails.
        A list of channels we are multistreaming with

        :param multistream: The multistream of this ChannelDetails.
        :type: list[MultiParticipant]
        """

        self._multistream = multistream

    @property
    def languages(self):
        """
        Gets the languages of this ChannelDetails.

        :return: The languages of this ChannelDetails.
        :rtype: Languages
        """
        return self._languages

    @languages.setter
    def languages(self, languages):
        """
        Sets the languages of this ChannelDetails.

        :param languages: The languages of this ChannelDetails.
        :type: Languages
        """

        self._languages = languages

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
        if not isinstance(other, ChannelDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
