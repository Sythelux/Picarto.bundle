import util
from PicartoClientAPI import PublicApi, rest, logger, OnlineDetails, ApiClient, Category, Configuration, ChannelDetails
from pagination import PaginationStore

configuration = Configuration()
public_api = PublicApi()
api_client = ApiClient()
pages = PaginationStore()

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

RE_LIST_ID = Regex('listId: "(.+?)", pagesConfig: ')
RE_CONTENT_ID = Regex('CONTENT_ID = "(.+?)";')
P_API = "https://api.picarto.tv/v1"
CATEGORY_THUMB = "https://picarto.tv/images/explore/communitys/%s.jpg"
STREAM_BASE = "https://1-edge5-us-east.picarto.tv/mp4/%s.mp4"


def Start():
    configuration.username = Prefs['username']
    configuration.password = Prefs['password']
    util.Lang = L

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
        key=Callback(OnlineSubMenu, title=L('Online')),
        title=u'%s' % L('Online'),
    ))
    Log.Debug("SubMenu: online")

    oc.add(DirectoryObject(
        key=Callback(CategoriesSubMenu, title=L('Categories')),
        title=u'%s' % L('Categories'),
    ))
    Log.Debug("SubMenu: categories")

    oc.add(DirectoryObject(
        key=Callback(EventsSubMenu, title=L('Events')),
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


def buildSummary(details):
    """ :type details OnlineDetails"""
    Log.Debug("buildSummary " + "")
    return "\r\n".join('%s' % x for x in details.languages)


@route(PREFIX + '/online')
def OnlineSubMenu(title, page=1, categories=None, **kwargs):
    try:
        Log.Debug("OnlineSubMenu " + str(page) + ", " + str(categories))
        page = int(page)
        if not pages.online_pages:
            buffer_list = list()
            online_channels_list = public_api.online_get(adult=Prefs['filter_adult'],
                                                         gaming=Prefs['filter_gaming'],
                                                         categories=categories)  # type: list

            for channel_dict in online_channels_list:
                # Log.Debug(channel_dict)
                details = api_client.deserialize_model(channel_dict, OnlineDetails)  # type: OnlineDetails
                # Log.Debug(details)

                buffer_list.append(details)
            pages.online_pages = list(PaginationStore.grouper(int(Prefs['elements_per_side']), buffer_list))

        online_page_length = len(pages.online_pages)
        page = abs(page) % online_page_length
        oc = ObjectContainer(
            title2=u'%s' % title + " (" + str(page) + "/" + str(online_page_length) + ")",
            art=None,
            content=ContainerContent.Albums
        )
        # Log.Debug(str(page) + ", " + str(pages.online_pages[page]))
        for details in pages.online_pages[page]:
            if details:
                oc.add(VideoClipObject(url=StreamURLForName(details.name),
                                       title=details.name + " - " + details.title,
                                       thumb=details.thumbnails.mobile,
                                       summary=buildSummary(details),
                                       # rating=, <-stars rating
                                       content_rating=L("adult") if details.adult else L("everyone"),
                                       # duration=float('inf'),# needs int
                                       # year=current,
                                       # genres=details.category,
                                       # writers=writers_a,
                                       # directors=directors_a,
                                       # roles=roles_a,
                                       studio=details.name
                                       ))
        if page < online_page_length:
            page += 1
            oc.add(NextPageObject(key=Callback(OnlineSubMenu, title=L("back"), page=page, categories=categories)))
        return oc
    except Exception as e:
        Log.Exception("OnlineSubMenu had an exception")
    return ContentNotFound()


@route(PREFIX + '/categories')
def Categories(name):
    return OnlineSubMenu(name, 1, name)


def buildCategorySummary(details):
    return "online: " + str(details.online_channels) + \
           " total: " + str(details.total_channels) + \
           " viewers: " + str(details.viewers)


def buildCategoryThumb(name):
    return CATEGORY_THUMB % name.lower().replace(" ", "").replace("&", "")


@route(PREFIX + '/categories_list')
def CategoriesSubMenu(title, **kwargs):
    Log.Debug("CategoriesSubMenu")
    oc = ObjectContainer(
        title2=u'%s' % title,
        art=None,
        content=ContainerContent.Albums
    )
    try:
        categories_list = public_api.categories_get()  # type: list

        for categories_dict in categories_list:
            # Log.Debug(channel_dict)
            details = api_client.deserialize_model(categories_dict, Category)  # type: Category
            # Log.Debug(details)
            oc.add(DirectoryObject(key=Callback(Categories, name=details.name),
                                   title=details.name,
                                   summary=buildCategorySummary(details),
                                   tagline=L("adult") if details.adult else L("everyone"),
                                   thumb=buildCategoryThumb(details.name)
                                   ))
        return oc
    except Exception as e:
        Log.Exception("OnlineSubMenu had an exception")
    return ContentNotFound()


@route(PREFIX + '/events')
def EventsSubMenu(title, **kwargs):
    Log.Debug("EventsSubMenu")
    return ContentNotFound()


@route(PREFIX + '/artist')
def showArtist(name, **kwargs):
    Log.Debug("showArtist " + name + ", ".join('%s=%r' % x for x in kwargs.iteritems()))
    oc = ObjectContainer(title2=u'%s' % name)
    try:
        oc.add(URLService.MediaObjectsForURL(
            "https://1-edge1-eu-west.picarto.tv/mp4/LiLaiRa.mp4?token=public&ticket=0&con=1516735777815&type=0&scope=0"))
        # oc.add(URLService.MediaObjectsForURL(StreamURLForName(name)))
    except Exception as e:
        Log.Exception("showArtist had an exception")
        return ContentNotFound()
    return oc


def StreamURLForName(name):
    # Log.Debug("StreamURLForName " + STREAM_BASE % name)
    return STREAM_BASE % name
    # the following is not working without javascript
    # Log.Debug("StreamURLForName "+name)
    # search_page = HTML.ElementFromURL("https://picarto.tv/" + name)
    # Log.Debug(search_page)
    # items = search_page.xpath("//*[@id='picarto-player-1_html5_api']")
    # Log.Debug(items)
    # for item in items:
    #     Log.Debug(item)
    #     return item.get("src")
    # return ""


def ContentNotFound():
    return MessageContainer(
        L('Error'),
        L('No entries found')
    )
