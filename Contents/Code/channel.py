THUMB_BASE = "https://thumb-us1.picarto.tv/thumbnail/%s.jpg"
USRIMG_BASE = "https://picarto.tv/user_data/usrimg/%s/dsdefault.jpg"
CHANNEL_BASE = "https://api.picarto.tv/v1/channel/id/"


class Channel(object):
    channels = {}

    def __init__(self, channel):
        self.channel = channel
        # self.artist = JSON.ObjectFromURL(LIST_ONLINE_URL, cacheTime=0, headers=HTTP_HEADERS)

    def createArtistObject(self, showArtist):
        Log.Debug("createArtistObject")
        summary = self.createSummary()
        name = self.channel['name']
        category = self.channel['category']
        user_id = self.channel['user_id']
        return DirectoryObject(key=Callback(showArtist, id=user_id),
                               title=name,
                               tagline=category,
                               summary=summary,
                               art=self.thumbnail()
                               )

        # return ObjectContainer(
        #     # title1=Callback(showArtist, id=user_id),
        #     # genres="gaming" if self.channel['gaming'] else "art",
        #     # tags=category,
        #     # rating=self.rating(),
        #     # source_title="picarto",
        #     title1=name,
        #     # summary=summary,
        #     # thumb=USRIMG_BASE % self.channel['name'].lower(),
        #     art=self.thumbnail()
        # )

    def thumbnail(self):
        return Resource.ContentsOfURLWithFallback(url=THUMB_BASE % self.channel['name'].lower())

    def rating(self):
        pass  # they need a float rating (stars)
        # return "adult" if self.channel['adult'] else "non-adult"

    def createSummary(self):
        retStr = "viewers: " + str(self.channel['viewers'])
        retStr = retStr + " in multistream mode: " + "yes" if self.channel['multistream'] else "no"
        return retStr

    def createStreamObject(self):
        return VideoClipObject(
            title=self.channel['name'],
            summary=self.createSummary(),
            thumb=self.thumbnail(),
            content_rating=self.rating(),
            # originally_available_at="", #expects date
            # duration="live" #expects a number
        )

    @classmethod
    def lazyLoad(cls, channel):
        id_ = channel['user_id']
        if id_ not in cls.channels or cls.channels[id_] is None:
            cls.channels[id_] = Channel(channel)
        return cls.channels[id_]
