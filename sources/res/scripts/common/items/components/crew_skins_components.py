from __future__ import absolute_import
import items, nations
from items.components.crew_skins_constants import CrewSkinType, TANKMAN_SEX, CREW_SKIN_PROPERTIES_MASKS

class CrewSkin(object):
    itemType = CrewSkinType.CREW_SKIN
    __slots__ = (b'id', b'tags', b'priceGroup', b'firstNameID', b'lastNameID', b'iconID', b'description', b'nation', b'sex', b'rarity', b'historical', b'soundSetID', b'priceGroupTags', b'realms')

    def __init__(self, ID, priceGroup, firstNameID, lastNameID, iconID, description, rarity, tags, historical, soundSetID, realms):
        self.id = ID
        self.priceGroup = priceGroup
        self.tags = tags
        self.firstNameID = firstNameID
        self.lastNameID = lastNameID
        self.iconID = iconID
        self.description = description
        self.sex = b''
        self.nation = None
        self.rarity = rarity
        self.historical = historical
        self.soundSetID = soundSetID if soundSetID else b'-'
        self.priceGroupTags = frozenset()
        self.realms = realms
        return

    @property
    def compactDescr(self):
        return items.makeIntCompactDescrByID(b'crewSkin', self.itemType, self.id)


class PriceGroup(object):
    itemType = CrewSkinType.ITEM_GROUP
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
        return items.makeIntCompactDescrByID(b'crewSkin', self.itemType, self.id)


class CrewSkinsCache(object):
    __slots__ = (b'priceGroups', b'priceGroupNames', b'skins', b'priceGroupTags', b'itemToPriceGroup')

    def __init__(self):
        self.priceGroupTags = {}
        self.skins = {}
        self.priceGroups = {}
        self.priceGroupNames = {}
        self.itemToPriceGroup = {}
        return

    def validateCrewSkin(self, tmanDescr, itemId):
        item = self.skins.get(itemId, None)
        if item is None:
            return (False, CREW_SKIN_PROPERTIES_MASKS.EMPTY_MASK, (b'{} not found').format(itemId))
        else:
            return self._validateItem(tmanDescr, item)

    @staticmethod
    def _validateItem(tmanDescr, item):
        resultMask = CREW_SKIN_PROPERTIES_MASKS.EMPTY_MASK
        resultMsg = b''
        tmanSex = TANKMAN_SEX.getTankmanSex(tmanDescr)
        if item.sex and item.sex != tmanSex:
            resultMask = resultMask | CREW_SKIN_PROPERTIES_MASKS.SEX
            resultMsg += (b'{} {} incompatible sex {};').format(item.sex, item.id, tmanSex)
        nation = nations.NAMES[tmanDescr.nationID]
        if item.nation and item.nation != nation:
            resultMask = resultMask | CREW_SKIN_PROPERTIES_MASKS.NATION
            resultMsg += (b'{} {} incompatible nation {};').format(item.nation, item.id, nation)
        return (resultMask == 0, resultMask, resultMsg)
