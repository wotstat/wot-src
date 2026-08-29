from collections import namedtuple
from copy import deepcopy
import typing
if typing.TYPE_CHECKING:
    from typing import Optional
USABLE_COLLECTION_ENTITIES = {
 b'customizationItem', b'dossier', b'tankman'}
UNUSABLE_COLLECTION_ENTITIES = {
 b'photo', b'video', b'note'}
COLLECTION_ITEM_TYPE_NAMES = USABLE_COLLECTION_ENTITIES.union(UNUSABLE_COLLECTION_ENTITIES)
COLLECTIONS_PREFIX = b'cllc'

class CollectionItem(namedtuple(b'CollectionItem', (b'itemId', b'type', b'isSpecial', b'url', b'cdn', b'relatedId'))):

    def __new__(cls, **kwargs):
        defaults = dict(relatedId=0, itemId=0, type=b'', isSpecial=False, url=b'', cdn={})
        defaults.update(kwargs)
        return super(CollectionItem, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()


class Collection(namedtuple(b'Collection', (b'collectionId', b'name', b'items', b'tags', b'rewards', b'isRelatedEventActive', b'isActive', b'year'))):

    def __new__(cls, **kwargs):
        defaults = dict(collectionId=0, items={}, tags=set(), rewards={}, name=b'', isRelatedEventActive=False, isActive=False, year=0)
        defaults.update(kwargs)
        cls.__packItemConfigs(defaults)
        return super(Collection, cls).__new__(cls, **defaults)

    @classmethod
    def defaults(cls):
        return cls()

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        self.__packItemConfigs(dataToUpdate)
        return self._replace(**dataToUpdate)

    @classmethod
    def __packItemConfigs(cls, dataToUpdate):
        items = {}
        for itemId, item in dataToUpdate[b'items'].iteritems():
            items[itemId] = CollectionItem(itemId=itemId, **item)

        dataToUpdate[b'items'] = items
        return


class CollectionsConfig(namedtuple(b'CollectionsConfig', (b'isEnabled', b'useCdnResourceCache', b'collections', b'linkedCollections'))):

    def __new__(cls, **kwargs):
        cls.__rawData = kwargs
        defaults = dict(isEnabled=False, useCdnResourceCache=True, collections={}, linkedCollections=[])
        defaults.update(kwargs)
        cls.__packCollectionConfigs(defaults)
        return super(CollectionsConfig, cls).__new__(cls, **defaults)

    def getCollection(self, collectionId):
        return self.collections.get(collectionId)

    def replace(self, data):
        allowedFields = self._fields
        dataToUpdate = dict((k, v) for k, v in data.iteritems() if k in allowedFields)
        self.__packCollectionConfigs(dataToUpdate)
        return self._replace(**dataToUpdate)

    def getRawData(self):
        return deepcopy(self.__rawData)

    @classmethod
    def __packCollectionConfigs(cls, dataToUpdate):
        dataToUpdate[b'collections'] = {collectionID: Collection(collectionId=collectionID, **collection) for collectionID, collection in dataToUpdate[b'collections'].iteritems()}
        return


def isCollectionsPrefix(itemName):
    return itemName.startswith(COLLECTIONS_PREFIX)


def makeCollectionItemEntitlementName(collectionId, itemId):
    return (b'_').join((COLLECTIONS_PREFIX, b'item', str(collectionId), str(itemId)))


def makeCollectionRewardEntitlementName(collectionId, requiredCount):
    return (b'_').join((COLLECTIONS_PREFIX, b'reward', str(collectionId), str(requiredCount)))


class CollectionRelatedItems:

    def __init__(self):
        self.__items = {}
        return

    def setData(self, data):
        relatedItemsCfg = {}
        for collectionId, collectionCfg in data[b'collections'].iteritems():
            for itemId, itemCfg in collectionCfg[b'items'].iteritems():
                if b'relatedId' in itemCfg:
                    relatedItemsCfg[itemCfg[b'relatedId']] = (
                     collectionId, itemId)

        self.__items = relatedItemsCfg
        return

    @property
    def items(self):
        return self.__items


g_collectionsRelatedItems = CollectionRelatedItems()
