from enum import Enum
from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.key_type_model import KeyTypeModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.lootbox_key_view_model import LootboxKeyViewModel

class Glows(Enum):
    DEFAULT = b'DEFAULT'
    UNIQUE = b'UNIQUE'


class LootboxesRewardsViewModel(ViewModel):
    __slots__ = (b'onClose', b'showVehicleInHangar', b'onRepeatOpen')
    ARG_REWARD_INDEX = b'tooltipId'
    MAX_MAIN_REWARDS = 3
    MAX_VISIBLE_REWARDS = 9

    def __init__(self, properties=17, commands=3):
        super(LootboxesRewardsViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def lootboxKey(self):
        return self._getViewModel(0)

    @staticmethod
    def getLootboxKeyType():
        return LootboxKeyViewModel

    @property
    def keyType(self):
        return self._getViewModel(1)

    @staticmethod
    def getKeyTypeType():
        return KeyTypeModel

    def getIsHiddenCount(self):
        return self._getBool(2)

    def setIsHiddenCount(self, value):
        self._setBool(2, value)
        return

    def getLootboxID(self):
        return self._getNumber(3)

    def setLootboxID(self, value):
        self._setNumber(3, value)
        return

    def getLootBoxName(self):
        return self._getResource(4)

    def setLootBoxName(self, value):
        self._setResource(4, value)
        return

    def getLootBoxIconName(self):
        return self._getString(5)

    def setLootBoxIconName(self, value):
        self._setString(5, value)
        return

    def getLootBoxCount(self):
        return self._getNumber(6)

    def setLootBoxCount(self, value):
        self._setNumber(6, value)
        return

    def getLootBoxOpenCount(self):
        return self._getNumber(7)

    def setLootBoxOpenCount(self, value):
        self._setNumber(7, value)
        return

    def getSenderName(self):
        return self._getString(8)

    def setSenderName(self, value):
        self._setString(8, value)
        return

    def getMoreSendersCount(self):
        return self._getNumber(9)

    def setMoreSendersCount(self, value):
        self._setNumber(9, value)
        return

    def getPhraseRes(self):
        return self._getResource(10)

    def setPhraseRes(self, value):
        self._setResource(10, value)
        return

    def getIsNameLoading(self):
        return self._getBool(11)

    def setIsNameLoading(self, value):
        self._setBool(11, value)
        return

    def getLootBoxMaxOpenCount(self):
        return self._getNumber(12)

    def setLootBoxMaxOpenCount(self, value):
        self._setNumber(12, value)
        return

    def getCountFailKey(self):
        return self._getNumber(13)

    def setCountFailKey(self, value):
        self._setNumber(13, value)
        return

    def getGlowType(self):
        return Glows(self._getString(14))

    def setGlowType(self, value):
        self._setString(14, value.value)
        return

    def getRewards(self):
        return self._getArray(15)

    def setRewards(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def getMainRewards(self):
        return self._getArray(16)

    def setMainRewards(self, value):
        self._setArray(16, value)
        return

    @staticmethod
    def getMainRewardsType():
        return BonusModel

    def _initialize(self):
        super(LootboxesRewardsViewModel, self)._initialize()
        self._addViewModelProperty(b'lootboxKey', LootboxKeyViewModel())
        self._addViewModelProperty(b'keyType', KeyTypeModel())
        self._addBoolProperty(b'isHiddenCount', False)
        self._addNumberProperty(b'lootboxID', 0)
        self._addResourceProperty(b'lootBoxName', R.invalid())
        self._addStringProperty(b'lootBoxIconName', b'')
        self._addNumberProperty(b'lootBoxCount', 0)
        self._addNumberProperty(b'lootBoxOpenCount', 0)
        self._addStringProperty(b'senderName', b'')
        self._addNumberProperty(b'moreSendersCount', 0)
        self._addResourceProperty(b'phraseRes', R.invalid())
        self._addBoolProperty(b'isNameLoading', False)
        self._addNumberProperty(b'lootBoxMaxOpenCount', 0)
        self._addNumberProperty(b'countFailKey', 0)
        self._addStringProperty(b'glowType', Glows.DEFAULT.value)
        self._addArrayProperty(b'rewards', Array())
        self._addArrayProperty(b'mainRewards', Array())
        self.onClose = self._addCommand(b'onClose')
        self.showVehicleInHangar = self._addCommand(b'showVehicleInHangar')
        self.onRepeatOpen = self._addCommand(b'onRepeatOpen')
        return
