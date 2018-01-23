import six
from PicartoClientAPI import PublicApi, rest, logger, OnlineChannels

from six import iteritems

publicApi = PublicApi()
rest.HTTP = HTTP
logger.Log = Log

THUMB_BASE = "https://thumb-us1.picarto.tv/thumbnail/%s.jpg"

TITLE = 'Picarto'
PREFIX = '/video/picarto'

ART = 'art-default.jpg'
ICON = 'icon-default.jpg'

WebsiteURL = 'https://picarto.tv/'
http = 'http:'
WebsitePopOutURL = 'https://picarto.tv/streampopout/{0}/public'

HTTP_HEADERS = {
    'Authorization': 'Bearer bla'
}

RE_LIST_ID = Regex('listId: "(.+?)", pagesConfig: ')
RE_CONTENT_ID = Regex('CONTENT_ID = "(.+?)";')
P_API = "https://api.picarto.tv/v1"
CATEGORY_THUMB = "https://picarto.tv/images/explore/communitys/%s.jpg"
STREAM_BASE = "https://1-edge5-us-east.picarto.tv/mp4/%s.mp4"


def Start():
    HTTP.ClearCookies()
    HTTP.ClearCache()
    HTTP.CacheTime = 30000


@handler(
    PREFIX,
    L(TITLE),
    ICON,
    ART
)
def MainMenu():
    Log.Debug("MainMenu")
    oc = ObjectContainer(
        title2=L(TITLE),
        no_cache=True,
        content=ContainerContent.Genres
    )

    oc.add(DirectoryObject(
        key=Callback(OnlineSubMenu, key='/c', title=L('Online')),
        title=u'%s' % L('Online'),
    ))
    Log.Debug("SubMenu: online")

    oc.add(DirectoryObject(
        key=Callback(CategoriesSubMenu, key='/categories', title=L('Categories')),
        title=u'%s' % L('Categories'),
    ))
    Log.Debug("SubMenu: categories")

    oc.add(DirectoryObject(
        key=Callback(EventsSubMenu, key='/events', title=L('Events')),
        title=u'%s' % L('Events'),
    ))
    Log.Debug("SubMenu: events")

    # oc.add(InputDirectoryObject(
    #     key=Callback(
    #         Search
    #     ),
    #     title=u'%s' % L('Search'), prompt=u'%s' % L('Search user'),
    # ))
    return oc


@route(PREFIX + '/c')
def OnlineSubMenu(key, title, **kwargs):
    try:
        Log.Debug("OnlineSubMenu")
        Log.Debug("Online: " + str(key) + ", " + str(title))
        onlineChannels = publicApi.online_get(adult=Prefs['filter_adult'],
                                              gaming=Prefs['filter_gaming'])  # type: OnlineChannels
        for key, val in onlineChannels.to_dict():
            Log.Debug(key, val)
    except Exception as e:
        Log.Exception("OnlineSubMenu had an exception")
        return ContentNotFound()

    # params = 'adult=%s' % Prefs['filter_adult']
    # params = params + '&gaming=%s' % Prefs['filter_gaming']
    # params = params + '&categories='  # TODO: later
    # items = Api.Request(key, params)
    #
    # if not items:
    # Log.Debug(items)
    #
    # oc = ObjectContainer(
    #     title2=u'%s' % title,
    #     art=None,
    #     content=ContainerContent.Shows
    # )
    # Log.Debug("ObjectContainer")
    #
    # for item in items:
    #     Log.Debug(item)
    #     oc.add(URLService.MetadataObjectForURL(STREAM_BASE % item['name']))
    # oc.add(DirectoryObject(key=Callback(showArtist, id=item['name']),
    #                        title=item['name'],
    #                        tagline=item['category'],
    #                        art=THUMB_BASE % item['name'].lower()
    #                        )
    #        )

    Log.Debug("return")
    return ContentNotFound()
    # return oc


@route(PREFIX + '/categories')
def CategoriesSubMenu(key, title, **kwargs):
    Log.Debug("CategoriesSubMenu")
    return ContentNotFound()


@route(PREFIX + '/events')
def EventsSubMenu(key, title, **kwargs):
    Log.Debug("EventsSubMenu")
    return ContentNotFound()


@route(PREFIX + '/artist')
def showArtist(id, **kwargs):
    #     # oc = ObjectContainer(title2=u'%s' % id)
    #     # oc.add(URLService.MetadataObjectForURL("https://1-edge5-us-east.picarto.tv/mp4/Swizzlestix.mp4?token=public&con=1503173554275&ticket=0&type=0&scope=0"))
    oc = ObjectContainer(title2=u'%s' % id)
    oc.add()
    return oc


class Api(object):
    @classmethod
    def Request(cls, uri, params=None):
        Log.Debug("Request")
        uri = P_API + uri

        if not params is None:
            uri = uri + '?' + params

        try:
            Log.Debug(uri)
            ret = JSON.ObjectFromURL(uri)
            if 'error' in ret:
                Log.Error(ret['error']['message'])
                return None
            return ret
        except:
            return None


def ContentNotFound():
    return MessageContainer(
        L('Error'),
        L('No entries found')
    )
