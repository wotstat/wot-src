from __future__ import absolute_import
from enum import Enum
from future.utils import iteritems
from past.builtins import cmp
from typing import TYPE_CHECKING
from gui.impl import backport
from gui.impl.gen import R
from gui.lootbox_system.base.common import getTextResource
from gui.shared.gui_items.gui_item import GUIItem
from helpers import dependency
from shared_utils import CONST_CONTAINER
from skeletons.gui.game_control import ILootBoxSystemController
if TYPE_CHECKING:
    from typing import Dict, Optional, Tuple

class NewYearLootBoxes(CONST_CONTAINER):
    PREMIUM = b'newYear_premium'


class WTLootBoxes(CONST_CONTAINER):
    WT_HUNTER = b'wt_hunter'
    WT_BOSS = b'wt_boss'
    WT_SPECIAL = b'wt_special'


class LunarNYLootBoxTypes(Enum):
    BASE = b'lunar_base'
    SIMPLE = b'lunar_simple'
    SPECIAL = b'lunar_special'


ALL_LUNAR_NY_LOOT_BOX_TYPES = (b'lunar_base', b'lunar_simple', b'lunar_special')
LUNAR_NY_LOOT_BOXES_CATEGORIES = b'LunarNY'
SENIORITY_AWARDS_LOOT_BOXES_TYPE = b'seniorityAwards'

class LootBox(GUIItem):
    __slots__ = (b'__id', b'__invCount', b'__isEnabled', b'__type', b'__category', b'__bonus', b'__historyName', b'__statsName', b'__guaranteedFrequency', b'__guaranteedFrequencyName', b'__probabilityBonusName', b'__probabilityBonusLimit', b'__rerollCurrency', b'__rerollPrices', b'__rerollMaxAttempts', b'__bonuses')
    __lootBoxSystem = dependency.descriptor(ILootBoxSystemController)

    def __init__(self, lootBoxID, lootBoxConfig, invCount):
        super(LootBox, self).__init__()
        self.__id = lootBoxID
        self.__invCount = invCount
        self.__updateByConfig(lootBoxConfig)
        return

    def __repr__(self):
        return b'LootBox(id=%d, type=%s, category=%s, count=%d)' % (self.getID(), self.getType(),
         self.getCategory(), self.getInventoryCount())

    def updateCount(self, invCount):
        self.__invCount = invCount
        return

    def update(self, lootBoxConfig):
        self.__updateByConfig(lootBoxConfig)
        return

    def getInventoryCount(self):
        return self.__invCount

    def isEnabled(self):
        return self.__isEnabled

    def getID(self):
        return self.__id

    def getUserName(self):
        if self.__type in self.__lootBoxSystem.eventNames:
            name = getTextResource([b'common', b'boxCategory', b'lowerCase'] + [self.__category], self.__type)
            return backport.text(name() if name.exists() else R.strings.lootbox_system.common.boxCategory.lowerCase.default())
        return backport.text(R.strings.lootboxes.type.dyn(self.__type)())

    def getType(self):
        return self.__type

    def getCategory(self):
        return self.__category

    def isFree(self):
        return self.__type != NewYearLootBoxes.PREMIUM

    def getBonusInfo(self):
        return self.__bonus

    def getGuaranteedFrequency(self):
        return self.__guaranteedFrequency

    def getGuaranteedFrequencyName(self):
        return self.__guaranteedFrequencyName

    def getProbabilityBonusLimit(self):
        return self.__probabilityBonusLimit

    def getProbabilityBonusLimitName(self):
        return self.__probabilityBonusName

    def getHistoryName(self):
        return self.__historyName

    def getStatsName(self):
        return self.__statsName

    def getUseStats(self):
        return bool(self.__statsName)

    def getRerollCurrency(self):
        return self.__rerollCurrency

    def getRerollPrices(self):
        return self.__rerollPrices

    def getRerollMaxAttempts(self):
        return self.__rerollMaxAttempts

    def isRerollable(self):
        return self.__rerollMaxAttempts is not None

    def _compare(self, other):
        return cmp(self.getID(), other.getID())

    def getBonuses(self):
        return self.__bonuses

    def __updateByConfig(self, lootBoxConfig):
        self.__isEnabled = lootBoxConfig.get(b'enabled')
        self.__type = lootBoxConfig.get(b'type')
        self.__category = lootBoxConfig.get(b'category')
        self.__bonus = lootBoxConfig.get(b'bonus', {})
        self.__statsName = lootBoxConfig.get(b'statsInfo', b'')
        self.__historyName = lootBoxConfig.get(b'historyName')
        limitsConfig = lootBoxConfig.get(b'limits', {})
        self.__guaranteedFrequencyName, self.__guaranteedFrequency = self.__readFrequencyLimit(limitsConfig)
        self.__probabilityBonusName, self.__probabilityBonusLimit = self.__readProbabilityBonusLimit(limitsConfig)
        self.__rerollCurrency, self.__rerollPrices, self.__rerollMaxAttempts = self.__readRerolls(lootBoxConfig.get(b'reroll'))
        self.__bonuses = lootBoxConfig.get(b'bonus', {})
        return

    @staticmethod
    def __readProbabilityBonusLimit(limitsCfg):
        for probabilityBonusName, limit in iteritems(limitsCfg):
            if b'useBonusProbabilityAfter' in limit:
                return (probabilityBonusName, limit[b'useBonusProbabilityAfter'] + 1)
            if b'guaranteedFrequency' in limit:
                return (probabilityBonusName, limit[b'guaranteedFrequency'])

        return (None, 0)

    @staticmethod
    def __readFrequencyLimit(limitsCfg):
        for limitName, limit in iteritems(limitsCfg):
            if b'guaranteedFrequency' in limit:
                return (limitName, limit[b'guaranteedFrequency'])

        return (None, 0)

    @staticmethod
    def __readRerolls(rerollCfg):
        if rerollCfg is None:
            return (None, None, None)
        else:
            return (
             rerollCfg[b'currency'],
             tuple(rerollCfg[b'prices']),
             rerollCfg[b'maxAttempts'])
