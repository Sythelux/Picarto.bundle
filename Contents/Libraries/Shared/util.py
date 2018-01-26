# from PicartoClientAPI import Language, ApiClient


def Lang(string):  # fallback
    return string


L = Lang


def generateTagline(details):
    ret_string = L("viewers") + ": "
    ret_string = "%s %d (%s: %d)" % (ret_string, details.viewers, L("total"), details.viewers_total)
    return ret_string


def generateSummary(details):
    ret_string = ""
    for panel in details.description_panels:
        ret_string += panel.title + "\r\n" + panel.body + "\r\n" + "\r\n"
    return ret_string


def generateCountries(languages):
    oc = ObjectContainer(
        title2=u'%s' % "multistreams and records",
        art=None,
        content=ContainerContent.GenericVideos
    )
    ret_string = ""
    # for lang_dict in languages:
    # lang = ApiClient().deserialize_model(lang_dict, Language)
    # ret_string += lang.name + "\r\n"
    return oc


def generateExtras(details):
    oc = ObjectContainer(
        title2=u'%s' % "multistreams and records",
        art=None,
        content=ContainerContent.GenericVideos
    )
    for lang in details.languages:
        ret_string += lang.name + "\r\n"
    return oc
