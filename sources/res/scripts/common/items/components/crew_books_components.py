from __future__ import absolute_import
import items, nations
from items.components.crew_books_constants import CrewBookCacheType, CREW_BOOK_RARITY

class CrewBook(object):
    itemType = CrewBookCacheType.CREW_BOOK
    __slots__ = (b'id', b'tags', b'priceGroup', b'iconID', b'name', b'description', b'nation', b'type', b'priceGroupTags')

    def __init__(self, ID, priceGroup, name, description, iconID, type, tags):
        self.id = ID
        self.priceGroup = priceGroup
        self.tags = tags
        self.name = name
        self.description = description
        self.iconID = iconID
        self.nation = None
        self.type = type
        self.priceGroupTags = frozenset()
        return

    @property
    def itemTypeName(self):
        return b'crewBook'

    @property
    def compactDescr(self):
        return items.makeIntCompactDescrByID(b'crewBook', self.itemType, self.id)

    @property
    def level(self):
        return

    def getExtensionLessIcon(self):
        return self.iconID.split(b'.png')[0]

    def getUserName(self):
        name = self.type
        if name not in CREW_BOOK_RARITY.NO_NATION_TYPES:
            name += b':' + self.nation
        return name


class PriceGroup(object):
    itemType = CrewBookCacheType.ITEM_GROUP
    __slots__ = (b'price', b'notInShop', b'id', b'name', b'tags')

    def __init__(self):
        self.price = (0, 0, 0)
        self.name = None
        self.id = 0
        self.notInShop = False
        self.tags = []
        return

    @property
    def compactDescr(self):
        return items.makeIntCompactDescrByID(b'crewBook', self.itemType, self.id)


class CrewBooksCache(object):
    __slots__ = (b'priceGroups', b'priceGroupNames', b'books', b'rarityGroups', b'priceGroupTags', b'itemToPriceGroup')

    def __init__(self):
        self.priceGroupTags = {}
        self.books = {}
        self.rarityGroups = {}
        self.priceGroups = {}
        self.priceGroupNames = {}
        self.itemToPriceGroup = {}
        return

    def getCrewBookExp(self, id):
        crewBookItem = self.books[id]
        rarityGroup = crewBookItem.type
        return self.rarityGroups[rarityGroup]

    def validateCrewBookNation(self, itemId, nationID):
        item = self.books.get(itemId, None)
        if item is None:
            return False
        else:
            nation = nations.NAMES[nationID]
            if item.nation and item.nation != nation:
                return False
            return True

    def validateBookPersonality(self, itemId, tmanInvID):
        item = self.books.get(itemId, None)
        if item is None:
            return False
        else:
            isPersonal = item.type == CREW_BOOK_RARITY.PERSONAL
            return not bool(tmanInvID) ^ isPersonal
