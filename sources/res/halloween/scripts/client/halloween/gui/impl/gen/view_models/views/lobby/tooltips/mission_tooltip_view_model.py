from enum import Enum
from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class ArtefactStates(Enum):
    NONE = b'none'
    INPROGRESS = b'inProgress'
    RECEIVE = b'receive'
    OPEN = b'open'


class MissionTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(MissionTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsHangar(self):
        return self._getBool(0)

    def setIsHangar(self, value):
        self._setBool(0, value)
        return

    def getId(self):
        return self._getString(1)

    def setId(self, value):
        self._setString(1, value)
        return

    def getIndex(self):
        return self._getNumber(2)

    def setIndex(self, value):
        self._setNumber(2, value)
        return

    def getName(self):
        return self._getString(3)

    def setName(self, value):
        self._setString(3, value)
        return

    def getDescription(self):
        return self._getString(4)

    def setDescription(self, value):
        self._setString(4, value)
        return

    def getRegularArtefactCount(self):
        return self._getNumber(5)

    def setRegularArtefactCount(self, value):
        self._setNumber(5, value)
        return

    def getSkipPrice(self):
        return self._getNumber(6)

    def setSkipPrice(self, value):
        self._setNumber(6, value)
        return

    def getDecodePrice(self):
        return self._getNumber(7)

    def setDecodePrice(self, value):
        self._setNumber(7, value)
        return

    def getRewards(self):
        return self._getArray(8)

    def setRewards(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def getEndDate(self):
        return self._getNumber(9)

    def setEndDate(self, value):
        self._setNumber(9, value)
        return

    def getState(self):
        return ArtefactStates(self._getString(10))

    def setState(self, value):
        self._setString(10, value.value)
        return

    def getIsKingReward(self):
        return self._getBool(11)

    def setIsKingReward(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(MissionTooltipViewModel, self)._initialize()
        self._addBoolProperty(b'isHangar', False)
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'index', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'description', b'')
        self._addNumberProperty(b'regularArtefactCount', 0)
        self._addNumberProperty(b'skipPrice', 0)
        self._addNumberProperty(b'decodePrice', 0)
        self._addArrayProperty(b'rewards', Array())
        self._addNumberProperty(b'endDate', 0)
        self._addStringProperty(b'state')
        self._addBoolProperty(b'isKingReward', False)
        return
