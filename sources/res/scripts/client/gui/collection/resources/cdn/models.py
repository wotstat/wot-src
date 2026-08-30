import typing
from enum import Enum, unique
from dict2model.models import Model
from gui.impl.utils.path import normalizeGfImagePath
from web.cache.web_cache import generateKey
if typing.TYPE_CHECKING:
    from typing import List
    from gui.collection.resources.cdn.cache import CollectionsCdnCache

@unique
class Group(str, Enum):
    ITEM = b'items'
    BG = b'backgrounds'


@unique
class Sub(str, Enum):
    ICON = b'48x48'
    SMALLEST = b'232x174'
    SMALL = b'296x222'
    MEDIUM = b'400x300'
    LARGE = b'600x450'
    LARGEST = b'1000x680'
    RECEIVED = b'received'
    UNRECEIVED = b'unreceived'
    BP_10 = b'battle_pass_10'
    BP_11 = b'battle_pass_11'
    BP_12 = b'battle_pass_12'
    MT_BIRTHDAY_2023 = b'mt_birthday2023'


class ImageModel(Model):
    __slots__ = (b'group', b'sub', b'name', b'url', b'__id', b'__imageCacheKey')

    def __init__(self, group, sub, name, url=None):
        super(ImageModel, self).__init__()
        self.group = group
        self.sub = sub
        self.name = name
        self.url = url
        self.__id = makeImageID(group, sub, name)
        self.__imageCacheKey = generateKey(self.url)
        return

    @property
    def id(self):
        return self.__id

    def isDownloaded(self, fileCache):
        return self.__imageCacheKey in fileCache.getLoaded()

    def getGFPath(self, fileCache):
        return normalizeGfImagePath(fileCache.getRelativePath(self.url))

    def __repr__(self):
        return (b'<ImageModel(group={}, sub={}, name={})>').format(self.group, self.sub, self.name)


class ConfigModel(Model):
    __slots__ = (b'images',)

    def __init__(self, images):
        super(ConfigModel, self).__init__()
        self.images = images
        return

    def __repr__(self):
        return (b'<ConfigModel(images={})>').format(len(self.images))


class CdnCacheParamsModel(object):
    __slots__ = (b'configUrl',)

    def __init__(self, configUrl=None):
        self.configUrl = configUrl
        return

    @property
    def isReady(self):
        return bool(self.configUrl)

    def reset(self):
        self.configUrl = None
        return

    def __repr__(self):
        return (b'<CdnCacheParamsModel(configUrl={})>').format(self.configUrl)


def makeImageID(group, sub, name):
    return (b'/').join((Group(group), Sub(sub), name))
