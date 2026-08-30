import typing, nations
from items import _xml
from constants import IS_CLIENT, ITEM_DEFS_PATH
from soft_exception import SoftException
from intervals import Interval
if IS_CLIENT:
    import ResMgr
    from helpers import i18n
else:
    from realm_utils import ResMgr
_g_itemTypes = None
UNDEFINED_ITEM_CD = 0
ITEM_TYPE_NAMES = (b'_reserved', b'vehicle', b'vehicleChassis', b'vehicleTurret', b'vehicleGun', b'vehicleEngine', b'vehicleFuelTank', b'vehicleRadio', b'tankman', b'optionalDevice', b'shell', b'equipment', b'customizationItem', b'crewSkin', b'crewBook')

class ITEM_TYPES(dict):

    def __init__(self):
        super(dict, self).__init__()
        for idx, name in enumerate(ITEM_TYPE_NAMES):
            if not name.startswith(b'_'):
                self[name] = idx
                setattr(self, name, idx)

        return


ITEM_TYPES = ITEM_TYPES()
ITEM_TYPE_INDICES = ITEM_TYPES
SIMPLE_ITEM_TYPE_NAMES = (b'vehicleChassis', b'vehicleTurret', b'vehicleGun', b'vehicleEngine', b'vehicleFuelTank', b'vehicleRadio', b'optionalDevice', b'shell', b'equipment', b'crewBook')
SIMPLE_ITEM_TYPE_INDICES = tuple(ITEM_TYPE_INDICES[x] for x in SIMPLE_ITEM_TYPE_NAMES)
VEHICLE_COMPONENT_TYPE_NAMES = (b'vehicleChassis', b'vehicleTurret', b'vehicleGun', b'vehicleEngine', b'vehicleFuelTank', b'vehicleRadio')
VEHICLE_COMPONENT_TYPE_INDICES = tuple(ITEM_TYPE_INDICES[x] for x in VEHICLE_COMPONENT_TYPE_NAMES)
EQUIPMENT_TYPE_NAMES = (b'regular', b'battleBoosters', b'battleAbilities', b'abilities', b'aux', b'passives')

class EQUIPMENT_TYPES(dict):

    def __init__(self):
        super(dict, self).__init__()
        for idx, name in enumerate(EQUIPMENT_TYPE_NAMES):
            self[name] = idx
            setattr(self, name, idx)

        return


EQUIPMENT_TYPES = EQUIPMENT_TYPES()

class ITEM_OPERATION:
    UPGRADE = b'upgrade'
    ALL = (
     UPGRADE,)


HEAL_GROUP_HEAL_POINT = 100
HEAL_GROUP_HOT = 101
PREDEFINED_HEAL_GROUPS = (
 HEAL_GROUP_HEAL_POINT, HEAL_GROUP_HOT)

class ItemsPrices(object):

    def __init__(self, prices=None):
        self._itemsPriceInfo = {}
        if prices:
            self.update(prices)
        return

    def __getitem__(self, descriptor):
        info = self.getPrices(descriptor)
        return self._tuplePrice(info)

    def __setitem__(self, descriptor, prices):
        if isinstance(prices, tuple):
            info = {}
            if prices[0] != 0:
                info[b'credits'] = prices[0]
            if prices[1] != 0:
                info[b'gold'] = prices[1]
            if len(prices) > 2 and prices[2] != 0:
                info[b'crystal'] = prices[2]
            if len(prices) > 3:
                info[b'eventCoin'] = prices[3]
            if len(prices) > 4:
                info[b'bpcoin'] = prices[4]
            if len(prices) > 5:
                info[b'equipCoin'] = prices[5]
            self._itemsPriceInfo[descriptor] = info
        elif isinstance(prices, dict):
            self._itemsPriceInfo[descriptor] = prices
        else:
            raise TypeError(b'price info could be tuple or dict!')
        return

    def __delitem__(self, descriptor):
        del self._itemsPriceInfo[descriptor]
        return

    def __contains__(self, key):
        return key in self._itemsPriceInfo

    def __len__(self):
        return len(self._itemsPriceInfo)

    def __eq__(self, obj):
        return isinstance(obj, ItemsPrices) and obj._itemsPriceInfo == self._itemsPriceInfo

    def get(self, key, defaultValue=None):
        if key in self._itemsPriceInfo:
            return self.__getitem__(key)
        return defaultValue

    def items(self):
        return [(compDescr, self._tuplePrice(prices)) for compDescr, prices in self._itemsPriceInfo.iteritems()]

    def update(self, other):
        for d, p in other.iteritems():
            self.__setitem__(d, p)

        return

    def copy(self):
        return ItemsPrices(self._itemsPriceInfo)

    def getSpecialItemPrices(self, currencyCode):
        return {compDescr: prices for compDescr, prices in self._itemsPriceInfo.iteritems() if currencyCode in prices}

    @staticmethod
    def _tuplePrice(priceInfo):
        return (priceInfo.get(b'credits', 0), priceInfo.get(b'gold', 0))

    def getPrices(self, descriptor):
        return self._itemsPriceInfo[descriptor]

    def tryGetPrice(self, descriptor, defaultValue=None):
        return self._itemsPriceInfo.get(descriptor, defaultValue)

    def getPrice(self, descriptor, currencyCode):
        return self._itemsPriceInfo[descriptor].get(currencyCode, 0)

    def getCrystalPrice(self, descriptor):
        return self._itemsPriceInfo[descriptor].get(b'crystal', 0)

    def hasPriceIn(self, descriptor, currencyCode):
        return currencyCode in self._itemsPriceInfo[descriptor]

    def __repr__(self):
        return repr(self._itemsPriceInfo)

    def intersect(self, other):
        otherStorage = other._itemsPriceInfo
        result = {}
        for k, v in self._itemsPriceInfo.iteritems():
            if k in otherStorage and otherStorage[k] != v:
                result[k] = v

        return ItemsPrices(result)

    def override(self, other, itemToPriceGroup=None):
        myStorage = self._itemsPriceInfo
        otherStorage = other._itemsPriceInfo if other else {}
        result = {}
        for compDescr, priceInfo in myStorage.iteritems():
            if compDescr in otherStorage:
                result[compDescr] = otherStorage[compDescr]
            elif compDescr in itemToPriceGroup and itemToPriceGroup[compDescr] in otherStorage:
                result[compDescr] = otherStorage[itemToPriceGroup[compDescr]]
            else:
                result[compDescr] = priceInfo

        return ItemsPrices(result)


def init(preloadEverything, pricesToCollect=None, step=None):
    global _g_itemTypes
    _g_itemTypes = _readItemTypes()
    if pricesToCollect is not None:
        pricesToCollect[b'itemPrices'] = ItemsPrices()
        pricesToCollect[b'vehiclesRentPrices'] = {}
        pricesToCollect[b'notInShopItems'] = set()
        pricesToCollect[b'vehiclesNotToBuy'] = set()
        pricesToCollect[b'vehiclesToSellForGold'] = set()
        pricesToCollect[b'vehicleSellPriceFactors'] = {}
        pricesToCollect[b'vehicleCamouflagePriceFactors'] = {}
        pricesToCollect[b'camouflagePriceFactors'] = [{} for x in nations.NAMES]
        pricesToCollect[b'notInShopCamouflages'] = [set() for x in nations.NAMES]
        pricesToCollect[b'inscriptionGroupPriceFactors'] = [{} for x in nations.NAMES]
        pricesToCollect[b'notInShopInscriptionGroups'] = [set() for x in nations.NAMES]
        pricesToCollect[b'playerEmblemGroupPriceFactors'] = {}
        pricesToCollect[b'notInShopPlayerEmblemGroups'] = set()
        pricesToCollect[b'operationPrices'] = {}
        pricesToCollect[b'progressionLvlPrices'] = {}
        pricesToCollect[b'notInShopProgressionLvlItems'] = {}
        pricesToCollect[b'forbiddenToSellItems'] = set()
    from items import stun
    stun.init()
    from items import vehicles
    vehicles.init(preloadEverything, pricesToCollect, step)
    from items import avatars
    avatars.init()
    from items import tankmen
    tankmen.init(preloadEverything, pricesToCollect)
    from items import perks
    perks.init(preloadEverything)
    return


def getTypeInfoByName(typeName):
    return _g_itemTypes[typeName]


def getTypeInfoByIndex(typeIndex):
    return _g_itemTypes[ITEM_TYPE_NAMES[typeIndex]]


def getTypeOfCompactDescr(compactDescr):
    cdType = compactDescr.__class__
    if cdType is int or cdType is long:
        itemTypeID = int(compactDescr & 15)
        if itemTypeID == 0:
            itemTypeID = int(compactDescr >> 24 & 255)
            if 0 != itemTypeID <= 15:
                raise SoftException(b"value is not a 'compact descriptor'")
    else:
        itemTypeID = ord(compactDescr[0]) & 15
        if itemTypeID == 0:
            itemTypeID = ord(compactDescr[1])
        elif itemTypeID in SIMPLE_ITEM_TYPE_INDICES:
            itemTypeID = itemTypeID - 2
    if itemTypeID >= len(ITEM_TYPE_NAMES):
        raise SoftException(b"value is not a 'compact descriptor'")
    return itemTypeID


def makeIntCompactDescrByID(itemTypeName, nationID, itemID):
    itemTypeID = ITEM_TYPES[itemTypeName]
    if itemTypeID <= 15:
        return (itemID << 8) + itemTypeID + (nationID << 4)
    if itemTypeID <= 255:
        return (itemTypeID << 24) + (itemID << 8) + (nationID << 4)
    return


def parseIntCompactDescr(compactDescr):
    itemTypeID = compactDescr & 15
    if itemTypeID == 0:
        itemTypeID = compactDescr >> 24 & 255
    return (
     itemTypeID,
     compactDescr >> 4 & 15,
     compactDescr >> 8 & 65535)


def filterIntCDsByItemType(intCDs, itemTypeID):
    return [cd for cd in intCDs if parseIntCompactDescr(cd)[0] == itemTypeID]


def allianceFromVehicleCD(compactDescr):
    _, nation, _ = parseIntCompactDescr(compactDescr)
    return nations.NATION_TO_ALLIANCE_IDS_MAP[nation]


def getVehicleAlliance(vehTypeCompDescr):
    return nations.ALLIANCES_TAGS_ORDER[allianceFromVehicleCD(vehTypeCompDescr)]


def isFromSameAlliance(typeCD1, typeCD2):
    return allianceFromVehicleCD(typeCD1) == allianceFromVehicleCD(typeCD2)


def clearXMLCache():
    _xml.clearCaches()
    return


def _readItemTypes():
    xmlPath = ITEM_DEFS_PATH + b'item_types.xml'
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (
     None, xmlPath)
    res = {}
    for index, name in enumerate(ITEM_TYPE_NAMES):
        if name.startswith(b'_'):
            continue
        itemSection = _xml.getSubsection(xmlCtx, section, name)
        ctx = (xmlCtx, name)
        tagNames = []
        tags = {}
        if itemSection.has_key(b'tags'):
            for tagSection in itemSection[b'tags'].values():
                tagName = intern(tagSection.name)
                if tags.has_key(tagName):
                    _xml.raiseWrongXml(xmlCtx, b'tags' + tagName, b'tag name is not unique')
                tagDescr = {b'name': tagName, 
                   b'index': (len(tagNames))}
                if IS_CLIENT:
                    tagDescr[b'userString'] = i18n.makeString(tagSection.readString(b'userString'))
                    tagDescr[b'description'] = i18n.makeString(tagSection.readString(b'description'))
                tags[tagName] = tagDescr
                tagNames.append(tagName)

        itemType = {b'index': index, b'tags': tags, 
           b'tagNames': (tuple(tagNames))}
        if IS_CLIENT:
            itemType[b'userString'] = i18n.makeString(itemSection.readString(b'userString'))
            itemType[b'description'] = i18n.makeString(itemSection.readString(b'description'))
        res[name] = itemType

    section = None
    itemSection = None
    tagSection = None
    ResMgr.purge(xmlPath, True)
    return res


def decodeEnum(value, enum):
    result = []
    splitted = value.split()
    for item in splitted:
        try:
            itemValue = int(item)
        except:
            itemValue = getattr(enum, item, None)
            if not isinstance(itemValue, int):
                raise SoftException((b"Invalid item '{0}'").format(item))
            if itemValue is None or itemValue not in enum.RANGE:
                raise SoftException((b"Unsupported item '{0}'").format(item))

        if itemValue in result:
            raise SoftException((b'Duplicated item {0} with value {1}').format(item, itemValue))
        result.append(itemValue)

    return (
     reduce(int.__or__, result, 0), tuple(splitted))
