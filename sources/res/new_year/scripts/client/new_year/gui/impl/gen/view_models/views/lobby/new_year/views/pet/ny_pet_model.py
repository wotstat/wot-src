from enum import Enum, IntEnum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.lootboxes.loot_box_entry_point_model import LootBoxEntryPointModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_indicator_model import NyPetIndicatorModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.pet_shop.ny_pet_shop import NyPetShop

class State(Enum):
    UNKNOWN = b''
    SAD = b'sad'
    NORMAL = b'normal'
    FUN = b'fun'
    RAID = b'raid'
    LOOT = b'loot'


class IndicatorType(Enum):
    FOOD = b'food'
    FUN = b'fun'
    ACTIVITY = b'activity'
    RAID = b'raid'


class SingleTipType(IntEnum):
    EMPTY = -1
    FUNOPENED = 2
    ACTIVITYOPENED = 3
    LEADERBOARD = 4
    RAIDAVAILABLE = 5
    RAIDINDICATORLOW = 6


class NyPetModel(ViewModel):
    __slots__ = (b'onLootBoxEntryPointClick', b'onOnboardingFinish', b'onOnboardingRestart', b'onResetWasOverflowed', b'onProgressFillSound', b'onDeleteItemLeaderboardPoint', b'onCloseSingleTip', b'onPetStateAnimationsChange', b'onShopClick', b'onRaid', b'onRaidSpeedup', b'onItemClick')

    def __init__(self, properties=27, commands=12):
        super(NyPetModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def lootBox(self):
        return self._getViewModel(0)

    @staticmethod
    def getLootBoxType():
        return LootBoxEntryPointModel

    @property
    def shop(self):
        return self._getViewModel(1)

    @staticmethod
    def getShopType():
        return NyPetShop

    @property
    def foodIndicator(self):
        return self._getViewModel(2)

    @staticmethod
    def getFoodIndicatorType():
        return NyPetIndicatorModel

    @property
    def funIndicator(self):
        return self._getViewModel(3)

    @staticmethod
    def getFunIndicatorType():
        return NyPetIndicatorModel

    @property
    def activityIndicator(self):
        return self._getViewModel(4)

    @staticmethod
    def getActivityIndicatorType():
        return NyPetIndicatorModel

    def getPetNeeds(self):
        return self._getArray(5)

    def setPetNeeds(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getPetNeedsType():
        return IndicatorType

    def getHasPetAnimations(self):
        return self._getBool(6)

    def setHasPetAnimations(self, value):
        self._setBool(6, value)
        return

    def getWasLeaderboardFinished(self):
        return self._getBool(7)

    def setWasLeaderboardFinished(self, value):
        self._setBool(7, value)
        return

    def getIsOnboarding(self):
        return self._getBool(8)

    def setIsOnboarding(self, value):
        self._setBool(8, value)
        return

    def getIsRestartedOnboarding(self):
        return self._getBool(9)

    def setIsRestartedOnboarding(self, value):
        self._setBool(9, value)
        return

    def getSingleTip(self):
        return SingleTipType(self._getNumber(10))

    def setSingleTip(self, value):
        self._setNumber(10, value.value)
        return

    def getNeedToCloseSingleTip(self):
        return self._getBool(11)

    def setNeedToCloseSingleTip(self, value):
        self._setBool(11, value)
        return

    def getIsSingleTipCloseOnOutside(self):
        return self._getBool(12)

    def setIsSingleTipCloseOnOutside(self, value):
        self._setBool(12, value)
        return

    def getIsPopoverOpened(self):
        return self._getBool(13)

    def setIsPopoverOpened(self, value):
        self._setBool(13, value)
        return

    def getIsGuiLootBoxesVisible(self):
        return self._getBool(14)

    def setIsGuiLootBoxesVisible(self, value):
        self._setBool(14, value)
        return

    def getMaxBonus(self):
        return self._getNumber(15)

    def setMaxBonus(self, value):
        self._setNumber(15, value)
        return

    def getCurBonus(self):
        return self._getNumber(16)

    def setCurBonus(self, value):
        self._setNumber(16, value)
        return

    def getState(self):
        return State(self._getString(17))

    def setState(self, value):
        self._setString(17, value.value)
        return

    def getIsRaidReady(self):
        return self._getBool(18)

    def setIsRaidReady(self, value):
        self._setBool(18, value)
        return

    def getRaidRemainingTime(self):
        return self._getNumber(19)

    def setRaidRemainingTime(self, value):
        self._setNumber(19, value)
        return

    def getCanUseRaidSpeedup(self):
        return self._getBool(20)

    def setCanUseRaidSpeedup(self, value):
        self._setBool(20, value)
        return

    def getIsPetRaidEnabled(self):
        return self._getBool(21)

    def setIsPetRaidEnabled(self, value):
        self._setBool(21, value)
        return

    def getBoostAmount(self):
        return self._getNumber(22)

    def setBoostAmount(self, value):
        self._setNumber(22, value)
        return

    def getMaxBoostLimit(self):
        return self._getNumber(23)

    def setMaxBoostLimit(self, value):
        self._setNumber(23, value)
        return

    def getRaidViewEnabled(self):
        return self._getBool(24)

    def setRaidViewEnabled(self, value):
        self._setBool(24, value)
        return

    def getBoostAccrualTime(self):
        return self._getNumber(25)

    def setBoostAccrualTime(self, value):
        self._setNumber(25, value)
        return

    def getBoostsToAdd(self):
        return self._getNumber(26)

    def setBoostsToAdd(self, value):
        self._setNumber(26, value)
        return

    def _initialize(self):
        super(NyPetModel, self)._initialize()
        self._addViewModelProperty(b'lootBox', LootBoxEntryPointModel())
        self._addViewModelProperty(b'shop', NyPetShop())
        self._addViewModelProperty(b'foodIndicator', NyPetIndicatorModel())
        self._addViewModelProperty(b'funIndicator', NyPetIndicatorModel())
        self._addViewModelProperty(b'activityIndicator', NyPetIndicatorModel())
        self._addArrayProperty(b'petNeeds', Array())
        self._addBoolProperty(b'hasPetAnimations', True)
        self._addBoolProperty(b'wasLeaderboardFinished', False)
        self._addBoolProperty(b'isOnboarding', False)
        self._addBoolProperty(b'isRestartedOnboarding', False)
        self._addNumberProperty(b'singleTip', SingleTipType.EMPTY.value)
        self._addBoolProperty(b'needToCloseSingleTip', False)
        self._addBoolProperty(b'isSingleTipCloseOnOutside', False)
        self._addBoolProperty(b'isPopoverOpened', False)
        self._addBoolProperty(b'isGuiLootBoxesVisible', False)
        self._addNumberProperty(b'maxBonus', 0)
        self._addNumberProperty(b'curBonus', 0)
        self._addStringProperty(b'state')
        self._addBoolProperty(b'isRaidReady', False)
        self._addNumberProperty(b'raidRemainingTime', 0)
        self._addBoolProperty(b'canUseRaidSpeedup', False)
        self._addBoolProperty(b'isPetRaidEnabled', False)
        self._addNumberProperty(b'boostAmount', 0)
        self._addNumberProperty(b'maxBoostLimit', 0)
        self._addBoolProperty(b'raidViewEnabled', False)
        self._addNumberProperty(b'boostAccrualTime', 0)
        self._addNumberProperty(b'boostsToAdd', 0)
        self.onLootBoxEntryPointClick = self._addCommand(b'onLootBoxEntryPointClick')
        self.onOnboardingFinish = self._addCommand(b'onOnboardingFinish')
        self.onOnboardingRestart = self._addCommand(b'onOnboardingRestart')
        self.onResetWasOverflowed = self._addCommand(b'onResetWasOverflowed')
        self.onProgressFillSound = self._addCommand(b'onProgressFillSound')
        self.onDeleteItemLeaderboardPoint = self._addCommand(b'onDeleteItemLeaderboardPoint')
        self.onCloseSingleTip = self._addCommand(b'onCloseSingleTip')
        self.onPetStateAnimationsChange = self._addCommand(b'onPetStateAnimationsChange')
        self.onShopClick = self._addCommand(b'onShopClick')
        self.onRaid = self._addCommand(b'onRaid')
        self.onRaidSpeedup = self._addCommand(b'onRaidSpeedup')
        self.onItemClick = self._addCommand(b'onItemClick')
        return
