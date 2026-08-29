from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui_lootboxes.gui.impl.gen.view_models.views.lobby.gui_lootboxes.guaranteed_reward_model import GuaranteedRewardModel

class LootboxViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=18, commands=0):
        super(LootboxViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def guaranteedReward(self):
        return self._getViewModel(0)

    @staticmethod
    def getGuaranteedRewardType():
        return GuaranteedRewardModel

    def getBoxID(self):
        return self._getNumber(1)

    def setBoxID(self, value):
        self._setNumber(1, value)
        return

    def getBoxType(self):
        return self._getString(2)

    def setBoxType(self, value):
        self._setString(2, value)
        return

    def getCategory(self):
        return self._getString(3)

    def setCategory(self, value):
        self._setString(3, value)
        return

    def getCount(self):
        return self._getNumber(4)

    def setCount(self, value):
        self._setNumber(4, value)
        return

    def getTier(self):
        return self._getNumber(5)

    def setTier(self, value):
        self._setNumber(5, value)
        return

    def getIsOpenEnabled(self):
        return self._getBool(6)

    def setIsOpenEnabled(self, value):
        self._setBool(6, value)
        return

    def getAutoOpenTime(self):
        return self._getNumber(7)

    def setAutoOpenTime(self, value):
        self._setNumber(7, value)
        return

    def getManualMaxOpenCount(self):
        return self._getNumber(8)

    def setManualMaxOpenCount(self, value):
        self._setNumber(8, value)
        return

    def getIconName(self):
        return self._getString(9)

    def setIconName(self, value):
        self._setString(9, value)
        return

    def getUserName(self):
        return self._getString(10)

    def setUserName(self, value):
        self._setString(10, value)
        return

    def getDescriptionKey(self):
        return self._getString(11)

    def setDescriptionKey(self, value):
        self._setString(11, value)
        return

    def getVideoRes(self):
        return self._getResource(12)

    def setVideoRes(self, value):
        self._setResource(12, value)
        return

    def getIsInfinite(self):
        return self._getBool(13)

    def setIsInfinite(self, value):
        self._setBool(13, value)
        return

    def getHasUniqueBack(self):
        return self._getBool(14)

    def setHasUniqueBack(self, value):
        self._setBool(14, value)
        return

    def getUnlockKeyIDs(self):
        return self._getArray(15)

    def setUnlockKeyIDs(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getUnlockKeyIDsType():
        return int

    def getBonusGroups(self):
        return self._getArray(16)

    def setBonusGroups(self, value):
        self._setArray(16, value)
        return

    @staticmethod
    def getBonusGroupsType():
        return unicode

    def getProgressionStage(self):
        return self._getNumber(17)

    def setProgressionStage(self, value):
        self._setNumber(17, value)
        return

    def _initialize(self):
        super(LootboxViewModel, self)._initialize()
        self._addViewModelProperty(b'guaranteedReward', GuaranteedRewardModel())
        self._addNumberProperty(b'boxID', 0)
        self._addStringProperty(b'boxType', b'unknown')
        self._addStringProperty(b'category', b'')
        self._addNumberProperty(b'count', 0)
        self._addNumberProperty(b'tier', 0)
        self._addBoolProperty(b'isOpenEnabled', True)
        self._addNumberProperty(b'autoOpenTime', 0)
        self._addNumberProperty(b'manualMaxOpenCount', 0)
        self._addStringProperty(b'iconName', b'unknown')
        self._addStringProperty(b'userName', b'unknown')
        self._addStringProperty(b'descriptionKey', b'unknown')
        self._addResourceProperty(b'videoRes', R.invalid())
        self._addBoolProperty(b'isInfinite', True)
        self._addBoolProperty(b'hasUniqueBack', False)
        self._addArrayProperty(b'unlockKeyIDs', Array())
        self._addArrayProperty(b'bonusGroups', Array())
        self._addNumberProperty(b'progressionStage', 0)
        return
