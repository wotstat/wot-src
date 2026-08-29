from typing import *
import ResMgr
from ResMgr import DataSection
from WeakMixin import WeakMixin
from items import ITEM_TYPES, parseIntCompactDescr, makeIntCompactDescrByID, EQUIPMENT_TYPES, vehicles
from items.basic_item import BasicItem
from items.vehicles import getItemByCompactDescr
from nations import NONE_INDEX
from soft_exception import SoftException
from supply_slot_categories import CategoriesHolder, SlotCategories
if TYPE_CHECKING:
    from items.artefacts import Equipment

class SupplySlot(CategoriesHolder):
    __slots__ = (b'slotID', b'tags', b'__weakref__')
    itemType = None

    def __init__(self):
        super(SupplySlot, self).__init__()
        self.slotID = None
        self.categories = set()
        self.tags = set()
        return

    def __eq__(self, other):
        if other is None or not isinstance(other, SupplySlot):
            return False
        return self.slotID == other.slotID

    def __ne__(self, other):
        return not self == other

    def readFromSection(self, section):
        self.slotID = section.readInt(b'id')
        categories = section.readString(b'categories')
        if categories:
            self.categories = set(categories.split(b' '))
        self.tags = set(section.readString(b'tags').split(b' '))
        self._readMeta(section[b'meta'])
        return

    def checkSlotCompatibility(self, compDescr=None, descr=None):
        if compDescr is None and descr is None:
            raise SoftException(b"One of 'compDescr' or 'descr' arguments must be specified.")
        if compDescr is None:
            compDescr = descr.compactDescr
        itemTypeID, nationID, itemID = parseIntCompactDescr(compDescr)
        if itemTypeID != self.itemType:
            return (False, (b'Item type of slot ({}) does not match type of item ({})').format(self.itemType, itemTypeID))
        else:
            return self._checkSlotCompatibility((itemTypeID, nationID, itemID), descr)

    def _checkSlotCompatibility(self, parsedCompDescr=None, descr=None):
        return (
         True, None)

    def getSubType(self):
        return

    @staticmethod
    def initSlot(slotSection):
        slotType = slotSection.readString(b'type')
        slotObj = getSlotByItemTypeName(slotType)()
        slotObj.readFromSection(slotSection)
        return slotObj

    @staticmethod
    def makeCompactDescr(itemTypeID, idxWithinItemType):
        return makeIntCompactDescrByID(itemTypeID, NONE_INDEX, idxWithinItemType)

    @staticmethod
    def parseCompactDescr(compDescr):
        itemTypeId, _, idxWithinItemType = parseIntCompactDescr(compDescr)
        return (itemTypeId, idxWithinItemType)

    def _readMeta(self, metaSection):
        return


class OptionalDeviceSlot(SupplySlot):
    itemType = ITEM_TYPES.optionalDevice


class EquipmentSlot(SupplySlot):
    __slots__ = (b'equipmentType',)
    itemType = ITEM_TYPES.equipment

    def _checkSlotCompatibility(self, parsedCompDescr=None, descr=None):
        if descr is None:
            _, _, itemID = parsedCompDescr
            descr = vehicles.g_cache.equipments()[itemID]
        if descr.equipmentType != self.equipmentType:
            return (False,
             (b'Equipment type of slot ({}) does not match type of item ({})').format(self.equipmentType, descr.equipmentType))
        else:
            return (
             True, None)

    def _readMeta(self, metaSection):
        equipmentType = metaSection.readString(b'equipmentType')
        self.equipmentType = EQUIPMENT_TYPES[equipmentType]
        return

    def getSubType(self):
        return self.equipmentType


class EpicEquipmentSlot(WeakMixin):
    FL_AVATAR_TAGS = frozenset((b'avatar', b'fl'))
    JOINING_TAGS = frozenset((b'reconnaissance', b'tactics', b'firesupport'))

    @classmethod
    def fromEquipmentSlot(cls, equipmentSlot):
        if isinstance(equipmentSlot, EquipmentSlot) and cls.FL_AVATAR_TAGS.issubset(equipmentSlot.tags):
            return EpicEquipmentSlot(equipmentSlot)
        else:
            return

    def _checkSlotCompatibility(self, parsedCompDescr=None, descr=None):
        res, _ = super(EpicEquipmentSlot, self)._checkSlotCompatibility(parsedCompDescr, descr)
        if not res:
            return (res, _)
        item = descr or getItemByCompactDescr(parsedCompDescr)
        return (self.tags.intersection(self.JOINING_TAGS).issubset(getattr(item, b'tags', ())), b'')


class ShellSlot(SupplySlot):
    itemType = ITEM_TYPES.shell


class SupplySlotsCache(object):
    __slots__ = (b'__slotDescrs', b'__categories')

    def __init__(self, xmlPath=None):
        self.__slotDescrs = None
        self.__categories = None
        if xmlPath is not None:
            self.readCacheFromFile(xmlPath)
        return

    def readCacheFromFile(self, xmlPath):
        slotsSection = ResMgr.openSection(xmlPath)[b'slots']
        cache = {}
        for name, section in slotsSection.items():
            slotDescr = SupplySlot.initSlot(section)
            cache[slotDescr.slotID] = slotDescr

        self.__slotDescrs = cache
        self.__categories = SlotCategories.ALL
        return

    @property
    def slotDescrs(self):
        return self.__slotDescrs

    def getSlotDescr(self, slotID):
        return self.slotDescrs[slotID]

    def getSlotDescrsByTags(self, itags=(), etags=()):
        itags, etags = set(itags), etags
        if not itags.isdisjoint(etags):
            return {}
        return {i: sd for i, sd in self.__slotDescrs.iteritems() if sd.tags.isdisjoint(etags) and bool(itags) ^ sd.tags.isdisjoint(itags)}

    @property
    def categories(self):
        return self.__categories


_ITEM_TYPE_TO_SLOT_TYPE = {t.itemType: t for t in SupplySlot.__subclasses__()}

def getSlotByItemTypeName(itemType):
    global _ITEM_TYPE_TO_SLOT_TYPE
    itemTypeID = ITEM_TYPES[itemType]
    slotType = _ITEM_TYPE_TO_SLOT_TYPE.get(itemTypeID, None)
    if slotType is not None:
        return slotType
    else:
        raise SoftException((b"No supplySlot for type '{}'").format(itemType))
        return
