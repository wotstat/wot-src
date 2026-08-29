import itertools, typing, logging
from copy import copy
from enum import Enum
from constants import LootBoxTiers, LOOTBOX_LIMIT_ITEM_PREFIX
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.gen.view_models.constants.loot_box_bonus_group import LootBoxBonusGroup as BonusGroup
from gui.impl.lobby.loot_box.loot_box_bonus_parsers.default_parser import parseAllOfBonusInfoSection
from gui.impl.lobby.loot_box.loot_box_bonus_parsers.rotation_parser import parseBonusSection
from gui.impl.lobby.loot_box.loot_box_helper import isAllVehiclesObtainedInSlot
from gui.shared.gui_items.gui_item import GUIItem
from helpers import time_utils
from lootboxes_common import makeLBKeyID
from preferred_maps import SlotTypeName
from shared_utils import CONST_CONTAINER, findFirst
from web.web_client_api.common import ItemPackType as ipType, ItemPackTypeGroup as ipTypeGroup
if typing.TYPE_CHECKING:
    from typing import Dict, Optional
    from gui.server_events.bonuses import SimpleBonus
_logger = logging.getLogger(__name__)

class NewYearLootBoxes(CONST_CONTAINER):
    PREMIUM = b'newYear_premium'
    SPECIAL = b'newYear_special'
    SPECIAL_AUTO = b'newYear_special_auto'
    COMMON = b'newYear_usual'
    SURPRISE_COIN = b'ny_2025_surprise'


class NewYearCategories(CONST_CONTAINER):
    NEWYEAR = b'NewYear'
    CHRISTMAS = b'Christmas'
    ORIENTAL = b'Oriental'
    FAIRYTALE = b'Fairytale'


class EventCategories(CONST_CONTAINER):
    EVENT = b'Event'


class WTLootBoxes(CONST_CONTAINER):
    WT_HUNTER = b'wt_hunter'
    WT_BOSS = b'wt_boss'
    WT_SPECIAL = b'wt_special'


class LunarNYLootBoxTypes(Enum):
    BASE = b'lunar_base'
    SIMPLE = b'lunar_simple'
    SPECIAL = b'lunar_special'


class EventLootBoxes(CONST_CONTAINER):
    PREMIUM = b'event_premium'
    COMMON = b'event_common'


class ReferralProgramLootBoxes(CONST_CONTAINER):
    SMALL = b'small_referral'
    BIG = b'big_referral'
    SPECIAL = b'special_referral'


ALL_LUNAR_NY_LOOT_BOX_TYPES = (
 b'lunar_base', b'lunar_simple', b'lunar_special')
LUNAR_NY_LOOT_BOXES_CATEGORIES = b'LunarNY'
SENIORITY_AWARDS_LOOT_BOXES_TYPE = b'seniorityAwards'
EVENT_LOOT_BOXES_CATEGORY = b'eventLootBoxes'
REFERRAL_PROGRAM_CATEGORY = b'referralProgram'
GUI_ORDER_NY = (
 NewYearLootBoxes.COMMON,
 NewYearLootBoxes.PREMIUM)
CATEGORIES_GUI_ORDER_NY = (
 NewYearCategories.NEWYEAR,
 NewYearCategories.CHRISTMAS,
 NewYearCategories.ORIENTAL,
 NewYearCategories.FAIRYTALE)
GROUP_PRIORITIES = [
 BonusGroup.LOOTBOX_STAGE_ROTATION, BonusGroup.VEHICLE, BonusGroup.PREMIUM, BonusGroup.CURRENCY,
 BonusGroup.LOOTBOXES, BonusGroup.VEHICLECUSTOMIZATIONS, BonusGroup.CREW, BonusGroup.BOOSTERS,
 BonusGroup.EQUIPMENTS, BonusGroup.ACCOUNTCUSTOMIZATIONS, BonusGroup.FEATUREITEMS]
_BONUS_GROUPS = {(BonusGroup.VEHICLE): (ipTypeGroup.VEHICLE), 
   (BonusGroup.PREMIUM): (
                        ipType.CUSTOM_PREMIUM_PLUS,), 
   (BonusGroup.CURRENCY): (
                         ipType.CUSTOM_CREDITS, ipType.CUSTOM_GOLD, ipType.CUSTOM_FREE_XP, ipType.CUSTOM_CRYSTAL,
                         ipType.EQUIP_COIN), 
   (BonusGroup.VEHICLECUSTOMIZATIONS): (ipTypeGroup.CUSTOMIZATION), 
   (BonusGroup.CREW): (ipTypeGroup.CREW + ipTypeGroup.CREW_BOOKS + tuple(ipTypeGroup.TMAN_TOKEN) + (
                     ipType.GOODIE_RECERTIFICATIONFORM, ipType.ITEM_CREW_SKIN)), 
   (BonusGroup.BOOSTERS): (ipTypeGroup.GOODIE + (ipType.CUSTOM_X5_BATTLE_BONUS,) + ipTypeGroup.BLUEPRINTS), 
   (BonusGroup.EQUIPMENTS): (ipTypeGroup.ITEM + (ipType.DEMOUNT_KITS, ipType.CUSTOM_SEVERAL_SLOTS)), 
   (BonusGroup.ACCOUNTCUSTOMIZATIONS): ((
                                      ipType.ACHIEVEMENT, ipType.BADGE, ipType.SINGLE_ACHIEVEMENTS, ipType.PLAYER_BADGE, ipType.CUSTOM_DOG_TAG) + tuple((b'custom/{}').format(slotTypeName.value) for slotTypeName in SlotTypeName)), 
   (BonusGroup.FEATUREITEMS): (
                             ipType.CUSTOM_COLLECTION_ENTITLEMENT, ipType.CUSTOM_ANY_COLLECTION_ITEM,
                             ipType.CUSTOM_LOOTBOXKEY, ipType.ENTITLEMENTS, ipType.CUSTOM_GOLDENTICKET,
                             ipType.CUSTOM_CURRENCIES), 
   (BonusGroup.LOOTBOXES): (
                          ipType.CUSTOM_LOOTBOX,)}

class ClientLootBoxTags(Enum):
    HIDDEN_COUNT = b'hiddenCount'
    HIDDEN = b'hidden'
    ALWAYS_SHOW = b'alwaysShow'
    EXTENDED_TOOLTIP = b'extendedTooltip'
    HAS_UNIQUE_BACK = b'hasUniqueBack'


def addBonusesToGroup(bonusGroup, bonuses):
    _BONUS_GROUPS[bonusGroup] += bonuses
    return


class LootBox(GUIItem):
    __slots__ = (b'__id', b'__invCount', b'__type', b'__category', b'__historyName', b'__guaranteedFrequency', b'__slotBonuses', b'__guaranteedFrequencyName', b'__tier', b'__isEnabled', b'__userNameKey', b'__iconName', b'__description', b'__videoKey', b'__weight', b'__bonusGroups', b'__autoOpenTime', b'__rotationLists', b'__config', b'__rotationStage', b'__tags', b'__unlockKeys', b'__manualMaxOpenCount', b'__lootBoxInfoPageURL', b'__lootBoxShopURL', b'__isStatCollected', b'__immediatelyOpen')

    def __init__(self, lootBoxID, lootBoxConfig, invCount):
        super(LootBox, self).__init__()
        self.__id = lootBoxID
        self.__invCount = invCount
        self.__rotationStage = 0
        self.__updateByConfig(lootBoxConfig)
        return

    def __repr__(self):
        return (b'LootBox(lootBoxID={}, lootBoxConfig={}, invCount={})').format(self.getID(), self.__getConfig(), self.getInventoryCount())

    def __cmp__(self, other):
        if other is None:
            return 1
        else:
            if isinstance(other, LootBox):
                return cmp((not self.isEnabled(), -self.getWeight()), (not other.isEnabled(), -other.getWeight()))
            return super(LootBox, self).__cmp__(other)

    def isActiveHiddenCount(self):
        return self.isHiddenCount() and self.__getTimeToAutoOpen() > 0

    def isActiveAlwaysShow(self):
        return self.isAlwaysShow() and self.__getTimeToAutoOpen() > 0

    def isHiddenCount(self):
        return ClientLootBoxTags.HIDDEN_COUNT.value in self.__tags

    def isAlwaysShow(self):
        return ClientLootBoxTags.ALWAYS_SHOW.value in self.__tags

    def hasUniqueBack(self):
        return ClientLootBoxTags.HAS_UNIQUE_BACK.value in self.__tags

    def isExtendedTooltip(self):
        return ClientLootBoxTags.EXTENDED_TOOLTIP.value in self.__tags

    def isTagExist(self, tag):
        return tag in self.__tags

    def isVisible(self):
        return ClientLootBoxTags.HIDDEN.value not in self.__tags

    def isVisibleInStorage(self):
        return self.isVisible() and (self.getInventoryCount() > 0 or self.isActiveHiddenCount() or self.isActiveAlwaysShow())

    def openedWithKey(self, keyID=None):
        if keyID:
            return keyID in self.__unlockKeys
        return bool(self.__unlockKeys)

    def getUnlockKeyIDs(self):
        return copy(self.__unlockKeys)

    def updateCount(self, invCount):
        self.__invCount = invCount
        return

    def updateRotationStage(self, rotationStage):
        self.__rotationStage = rotationStage
        return

    def update(self, lootBoxConfig):
        self.__updateByConfig(lootBoxConfig)
        return

    def getInventoryCount(self):
        return self.__invCount

    def getID(self):
        return self.__id

    def getUserName(self):
        return backport.text(R.strings.lootboxes.userName.dyn(self.__userNameKey)())

    def getUserNameKey(self):
        return self.__userNameKey

    def getDesrciption(self):
        return self.__description

    def getDescriptionText(self):
        return backport.text(R.strings.lootboxes.desctiptions.dyn(self.__description)())

    def getIconName(self):
        return self.__iconName

    def getVideoRes(self):
        resource = R.videos
        resPath = self.__videoKey.split(b'/')
        if resPath:
            for pathItem in resPath:
                resource = resource.dyn(pathItem)
                if not resource:
                    return R.invalid()

            return resource()
        return R.invalid()

    def getType(self):
        return self.__type

    def getAutoOpenTime(self):
        if self.__autoOpenTime:
            return self.__autoOpenTime
        return 0

    def isStatCollected(self):
        return self.__isStatCollected

    def isImmediatelyOpen(self):
        return self.__immediatelyOpen

    def getManualMaxOpenCount(self):
        if self.__manualMaxOpenCount:
            return self.__manualMaxOpenCount
        return 0

    def getLootBoxInfoPageURL(self):
        if self.__lootBoxInfoPageURL:
            return self.__lootBoxInfoPageURL
        return b''

    def getLootBoxShopURL(self):
        if self.__lootBoxShopURL:
            return self.__lootBoxShopURL
        return b''

    def getCategory(self):
        return self.__category

    def getTier(self):
        return self.__tier

    def getWeight(self):
        return self.__weight

    def isFree(self):
        return self.__type == NewYearLootBoxes.COMMON

    def isEnabled(self):
        return self.__isEnabled

    def getGuaranteedFrequency(self, multiple=False):
        if multiple:
            return self.__guaranteedFrequency
        if len(self.__guaranteedFrequency) == 1:
            return self.__guaranteedFrequency[0]
        return self.__guaranteedFrequency[self.predictRotationStage()]

    def getGuaranteedFrequencyName(self):
        if len(self.__guaranteedFrequencyName) == 1:
            return self.__guaranteedFrequencyName[0]
        return self.__guaranteedFrequencyName[self.predictRotationStage()]

    def predictRotationStage(self):
        if not self.hasLootLists():
            return self._getRotationStage()
        rotationStage = self.getCurrentRotationStage()
        if rotationStage > 0:
            return rotationStage - 1
        return rotationStage

    def getGuaranteedVehicleLevelsRange(self):
        levels = set()
        for slot in self.__iterateAllSlots():
            guaranteedRewards = slot[b'limitIDsMap'].get(self.getGuaranteedFrequencyName(), [])
            for reward in guaranteedRewards:
                if reward.getName() == b'vehicles':
                    for vehicle, _ in reward.getVehicles():
                        levels.add(vehicle.level)

        if levels:
            return [min(levels), max(levels)]
        return []

    def getHistoryName(self):
        return self.__historyName

    def getBonusGroups(self):
        if self.__bonusGroups is None:
            self.__bonusGroups = self.__formBonusGroups()
        return sorted(self.__bonusGroups.keys(), key=GROUP_PRIORITIES.index)

    @staticmethod
    def getBonusGroupsWithBonuses(bonuses):
        bonusesGroups = dict()
        for bonus in bonuses:
            bonusGroup = LootBox.findGroupForBonus(bonus)
            if bonusGroup is None:
                continue
            bonusesGroups.setdefault(bonusGroup, []).append(bonus)

        return bonusesGroups

    def getBonusesByGroup(self, group):
        if self.__bonusGroups is None:
            self.__bonusGroups = self.__formBonusGroups()
        return self.__bonusGroups[group]

    def getBonusSlots(self):
        return self.__slotBonuses

    def hasLootLists(self):
        return self.__config.get(b'showProbabilitiesInfo', False) and self.__config.get(b'showBonusInfo', False) and self.__config.get(b'rotationLevelCount', 1) > 1

    def getLootLists(self):
        return self.__rotationLists

    def _getRotationStage(self):
        return self.__rotationStage

    def isMultipleStage(self):
        return len(self.__rotationLists) > 1

    def isVehicleGuaranteedOnly(self):
        for slot in self.__iterateAllSlots():
            guaranteedRewards = slot[b'limitIDsMap'].get(self.getGuaranteedFrequencyName(), [])
            for reward in guaranteedRewards:
                if reward.getName() not in (b'vehicles', b'battleToken'):
                    return False

        return True

    def __getTimeToAutoOpen(self):
        if self.__autoOpenTime:
            return max(self.__autoOpenTime - time_utils.getServerUTCTime(), 0)
        return float(b'inf')

    def __updateByConfig(self, lootBoxConfig):
        self.__autoOpenTime = lootBoxConfig.get(b'autoOpenTime', None)
        self.__isStatCollected = True if lootBoxConfig.get(b'statisticsStorage', None) else False
        self.__type = lootBoxConfig.get(b'type', b'')
        self.__category = lootBoxConfig.get(b'category', b'')
        self.__tier = LootBoxTiers(lootBoxConfig.get(b'tier', 1))
        self.__historyName = lootBoxConfig.get(b'historyName', b'')
        self.__config = lootBoxConfig.get(b'config', {})
        self.__rotationLists = []
        if self.hasLootLists():
            self.__rotationLists, self.__slotBonuses = parseBonusSection(lootBoxConfig[b'bonus'], self.__config[b'rotationLevelCount'])
        else:
            self.__slotBonuses = parseAllOfBonusInfoSection(lootBoxConfig.get(b'bonus', {}).get(b'allof', []))
        self.__bonusGroups = None
        self.__guaranteedFrequencyName, self.__guaranteedFrequency = self.__readLimits(lootBoxConfig.get(b'limits', {}))
        self.__isEnabled = lootBoxConfig.get(b'enabled', False)
        self.__weight = lootBoxConfig.get(b'weight', 0.0)
        assetsConfig = lootBoxConfig.get(b'assets', {})
        self.__userNameKey = assetsConfig.get(b'userName', self.__type)
        iconName = assetsConfig.get(b'iconName', self.__type)
        self.__iconName = iconName if iconName else b'default'
        self.__description = assetsConfig.get(b'description', self.__type)
        self.__videoKey = assetsConfig.get(b'video', b'')
        self.__tags = assetsConfig.get(b'tags', set())
        self.__lootBoxInfoPageURL = assetsConfig.get(b'lootBoxInfoPageURL', b'')
        self.__lootBoxShopURL = assetsConfig.get(b'lootBoxShopURL', b'')
        self.__unlockKeys = lootBoxConfig.get(b'unlockKeys', set())
        self.__manualMaxOpenCount = lootBoxConfig.get(b'manualMaxOpenCount')
        self.__immediatelyOpen = lootBoxConfig.get(b'immediatelyOpen')
        return

    def __iterateAllSlots(self):
        return itertools.chain(self.__slotBonuses.itervalues(), *(rotationList.itervalues() for rotationList in self.__rotationLists))

    def __itearateSlotsWithoutRotationDependence(self):
        rotationGenerators = [rotationList.itervalues() for rotationList in self.__rotationLists]
        for generator in rotationGenerators:
            next(generator)

        return itertools.chain(self.__slotBonuses.itervalues(), *rotationGenerators)

    def __getConfig(self):
        config = {b'type': (self.__type), 
           b'category': (self.__category), 
           b'tier': (self.__tier), 
           b'enabled': (self.__isEnabled), 
           b'weight': (self.__weight), 
           b'assets': {b'userName': (self.__userNameKey), 
                       b'iconName': (self.__iconName), 
                       b'description': (self.__description), 
                       b'video': (self.__videoKey)}}
        if self.__autoOpenTime:
            config[b'autoOpenTime'] = self.__autoOpenTime
        return config

    @staticmethod
    def __readLimits(limitsCfg):
        guaranteedFrequencies = []
        guaranteedFrequenciesNames = []
        for limitName, limit in limitsCfg.iteritems():
            if b'useBonusProbabilityAfter' in limit:
                guaranteedFrequencies.append(limit[b'useBonusProbabilityAfter'] + 1)
                guaranteedFrequenciesNames.append(limitName)
            if b'guaranteedFrequency' in limit:
                guaranteedFrequencies.append(limit[b'guaranteedFrequency'])
                guaranteedFrequenciesNames.append(limitName)

        if guaranteedFrequencies and guaranteedFrequenciesNames:
            return (guaranteedFrequenciesNames, guaranteedFrequencies)
        else:
            return (
             [
              None], [0])

    def getCurrentRotationStage(self):
        rotationStage = self._getRotationStage()
        if self.hasLootLists():
            lootLists = self.getLootLists()
            for lootList in lootLists[rotationStage:]:
                firstSlot = findFirst((lambda x: x is not None), lootList)
                if firstSlot is not None:
                    if isAllVehiclesObtainedInSlot(lootList[firstSlot]):
                        rotationStage += 1
                    else:
                        break

            rotationStage += 1
            rotationStage = min(rotationStage, len(lootLists))
        return rotationStage

    def __formBonusGroups(self):
        bonusGroups = dict()
        for slot in self.__itearateSlotsWithoutRotationDependence():
            for bonus in slot.get(b'bonuses', {}):
                bonusGroup = LootBox.findGroupForBonus(bonus)
                if bonusGroup is None:
                    if not self.__isExcludedBonus(bonus):
                        _logger.warning(b'Could not find a proper BonusGroup for bonus: %s', bonus.getName())
                    continue
                bonusGroups.setdefault(bonusGroup, []).append(bonus)

        if self.hasLootLists():
            bonusGroups[BonusGroup.LOOTBOX_STAGE_ROTATION] = []
        return bonusGroups

    @staticmethod
    def findGroupForBonus(bonus):
        for bns in bonus.getWrappedLootBoxesBonusList():
            bonusType = bns[b'type']
            for bonusGroup, bonusTypes in _BONUS_GROUPS.items():
                if bonusType in bonusTypes:
                    return bonusGroup

        return

    def __isExcludedBonus(self, bonus):
        value = bonus.getValue()
        if isinstance(value, dict):
            for k in value.keys():
                if LOOTBOX_LIMIT_ITEM_PREFIX in str(k):
                    return True

        return False


class LootBoxKeyType(Enum):
    SIMPLE = b'simpleKey'
    LOCKPICK = b'lockpick'


class LootBoxKey(object):
    __slots__ = (b'__token', b'__id', b'__keyData', b'__count')

    def __init__(self, token, count, lootBoxKeyConfig):
        super(LootBoxKey, self).__init__()
        self.__token = token
        self.__id = makeLBKeyID(token)
        self.__count = count
        self.__keyData = lootBoxKeyConfig
        return

    @property
    def keyID(self):
        return self.__id

    @property
    def tokenID(self):
        return self.__token

    @property
    def iconName(self):
        return self.__keyData.get(b'assets', {}).get(b'iconName', b'')

    @property
    def userName(self):
        return self.__keyData.get(b'assets', {}).get(b'userName', b'')

    @property
    def openProbability(self):
        return self.__keyData.get(b'openProbability', 100.0)

    @property
    def keyType(self):
        if self.openProbability >= 100.0:
            return LootBoxKeyType.SIMPLE
        return LootBoxKeyType.LOCKPICK

    @property
    def count(self):
        return self.__count
