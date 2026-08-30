from __future__ import absolute_import
import logging, typing, ResMgr
from dict2model import fields, schemas, validate
from dict2model.models import Model
from gui.impl.lobby.offers import getGfImagePath
from helpers import getClientLanguage
from web.cache.web_cache import generateKey
if typing.TYPE_CHECKING:
    from typing import Any, Dict, List, Optional
    from web.cache.web_cache import BaseExternalCache
_logger = logging.getLogger(__name__)

class RibbonUrls(Model):
    __slots__ = (b'base', b'icon', b'small', b'large', b'_urlHashes', b'_fileCache')

    def __init__(self, base, icon, small, large):
        super(RibbonUrls, self).__init__()
        self.base = base
        self.icon = icon
        self.small = small
        self.large = large
        self._fileCache = None
        self._urlHashes = [
         generateKey(base),
         generateKey(icon),
         generateKey(small),
         generateKey(large)]
        return

    def getBaseAsset(self):
        return self._getGFPath(self.base)

    def getIconAsset(self):
        return self._getGFPath(self.icon)

    def getSmallAsset(self):
        return self._getGFPath(self.small)

    def getLargeAsset(self):
        return self._getGFPath(self.large)

    def isDownloaded(self):
        return all(_hash in self._fileCache.getLoaded() for _hash in self._urlHashes)

    def setFileCache(self, fileCache):
        self._fileCache = fileCache
        return

    def _getGFPath(self, url):
        path = self._fileCache.get(url)
        return getGfImagePath(path)


class BackgroundModel(Model):
    __slots__ = (b'id', b'url', b'name', b'localization', b'_langCode', b'_localizationText', b'_urlHash', b'_fileCache')

    def __init__(self, id, name, url, localization):
        super(BackgroundModel, self).__init__()
        self.id = id
        self.url = url
        self.localization = localization
        self.name = name
        self._langCode = getClientLanguage()
        self._localizationText = None
        self._urlHash = generateKey(url)
        return

    def isDownloaded(self):
        return self._urlHash in self._fileCache.getLoaded()

    def getAsset(self):
        path = self._fileCache.get(self.url)
        return getGfImagePath(path)

    def getLocalization(self):
        if self._localizationText is not None:
            return self._localizationText
        else:
            return self._loadLocalizationText()

    def setFileCache(self, fileCache):
        self._fileCache = fileCache
        return

    def _loadLocalizationText(self):
        try:
            localizationPath = self._fileCache.get(self.localization)
            localizationRes = ResMgr.openSection(localizationPath)
            titleSection = localizationRes[b'title']
            if titleSection:
                text = titleSection.readString(self._langCode, default=None)
                if text is None:
                    _logger.warning(b'Cannot find text for background with id %s for lang code %s', self.id, self._langCode)
                self._localizationText = text or b''
        except IOError:
            _logger.exception(b'Failed to load localization text for background with id %s for lang code %s', self.id, self._langCode)

        return self._localizationText


class RibbonModel(Model):
    __slots__ = (b'id', b'urls', b'name', b'_urls')

    def __init__(self, id, name, urls):
        super(RibbonModel, self).__init__()
        self.id = id
        self.urls = urls
        self.name = name
        self._urls = [
         self.urls.base,
         self.urls.small,
         self.urls.large,
         self.urls.icon]
        return

    @property
    def allURLs(self):
        return self._urls

    def isDownloaded(self):
        return self.urls.isDownloaded()

    def setFileCache(self, fileCache):
        self.urls.setFileCache(fileCache)
        return


class RibbonUrlsLocal(RibbonUrls):
    __slots__ = ()

    def __init__(self, base, icon, small, large):
        super(RibbonUrlsLocal, self).__init__(base, icon, small, large)
        self._fileCache = None
        self._urlHashes = []
        return

    def getBaseAsset(self):
        return self.base

    def getIconAsset(self):
        return self.icon

    def getSmallAsset(self):
        return self.small

    def getLargeAsset(self):
        return self.large

    def isDownloaded(self):
        return True

    def setFileCache(self, fileCache):
        return


class BackgroundModelLocal(BackgroundModel):
    __slots__ = ()

    def __init__(self, id, name, url, localization):
        super(BackgroundModelLocal, self).__init__(id, name, url, localization)
        self._localizationText = None
        self._urlHash = None
        return

    def getAsset(self):
        return self.url

    def getLocalization(self):
        return self.localization

    def isDownloaded(self):
        return True

    def setFileCache(self, fileCache):
        return


class ConfigModel(Model):
    __slots__ = (b'ribbons', b'backgrounds', b'_ribbonURLs', b'_backgroundIDsMap', b'_ribbonsIDsMap', b'_fileCache')

    def __init__(self, ribbons, backgrounds):
        super(ConfigModel, self).__init__()
        self.ribbons = sorted(ribbons, key=(lambda ribbon: ribbon.id))
        self.backgrounds = sorted(backgrounds, key=(lambda background: background.id))
        self._fileCache = None
        self._ribbonURLs = [url for ribbon in ribbons for url in ribbon.allURLs]
        self._backgroundIDsMap = {background.id: background for background in backgrounds}
        self._ribbonsIDsMap = {ribbon.id: ribbon for ribbon in ribbons}
        return

    @property
    def ribbonURLs(self):
        return self._ribbonURLs

    def getBackground(self, id_):
        return self._backgroundIDsMap.get(id_, None)

    def getRibbon(self, id_):
        return self._ribbonsIDsMap.get(id_, None)

    def setFileCache(self, fileCache):
        self._fileCache = fileCache
        self._setFileCacheForChildren(fileCache)
        return

    def _setFileCacheForChildren(self, fileCache):
        for background in self.backgrounds:
            background.setFileCache(fileCache)

        for ribbon in self.ribbons:
            ribbon.setFileCache(fileCache)

        return


backgroundSchema = schemas.Schema(fields={b'id': (fields.Integer(required=True)), 
   b'name': (fields.String(required=True)), 
   b'url': (fields.String(required=True, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1))), 
   b'localization': (fields.String(required=True, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1)))}, modelClass=BackgroundModel, checkUnknown=True)
ribbonUrlsSchema = schemas.Schema(fields={b'base': (fields.String(required=True, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1))), 
   b'icon': (fields.String(required=True, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1))), 
   b'small': (fields.String(required=True, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1))), 
   b'large': (fields.String(required=True, serializedValidators=validate.Length(minValue=1), deserializedValidators=validate.Length(minValue=1)))}, modelClass=RibbonUrls, checkUnknown=True)
ribbonSchema = schemas.Schema(fields={b'id': (fields.Integer(required=True)), 
   b'name': (fields.String(required=True)), 
   b'urls': ribbonUrlsSchema}, modelClass=RibbonModel, checkUnknown=True)
configSchema = schemas.Schema(fields={b'ribbons': (fields.List(fieldOrSchema=ribbonSchema, required=True)), 
   b'backgrounds': (fields.List(fieldOrSchema=backgroundSchema, required=True))}, modelClass=ConfigModel, checkUnknown=True)
backgroundLocalSchema = schemas.Schema(fields={b'id': (fields.Integer(required=True)), 
   b'name': (fields.String(required=True)), 
   b'url': (fields.String(required=True)), 
   b'localization': (fields.String(required=True))}, modelClass=BackgroundModelLocal, checkUnknown=True)
ribbonUrlsLocalSchema = schemas.Schema(fields={b'base': (fields.String(required=True)), 
   b'icon': (fields.String(required=True)), 
   b'small': (fields.String(required=True)), 
   b'large': (fields.String(required=True))}, modelClass=RibbonUrlsLocal, checkUnknown=True)
ribbonLocalSchema = schemas.Schema(fields={b'id': (fields.Integer(required=True)), 
   b'name': (fields.String(required=True)), 
   b'urls': ribbonUrlsLocalSchema}, modelClass=RibbonModel, checkUnknown=True)
localConfigSchema = schemas.Schema(fields={b'ribbons': (fields.List(fieldOrSchema=ribbonLocalSchema, required=True)), 
   b'backgrounds': (fields.List(fieldOrSchema=backgroundLocalSchema, required=True))}, modelClass=ConfigModel, checkUnknown=True)

def createConfigModel(rawData):
    return configSchema.deserialize(rawData, silent=True)


def createLocalConfigModel(rawData):
    return localConfigSchema.deserialize(rawData, silent=True)
