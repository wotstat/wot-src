from enum import Enum
from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.common.bonus_item_view_model import BonusItemViewModel

class ArtefactStates(Enum):
    NONE = b'none'
    INPROGRESS = b'inProgress'
    RECEIVE = b'receive'
    OPEN = b'open'


class RewardPathItemViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RewardPathItemViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIndex(self):
        return self._getNumber(1)

    def setIndex(self, value):
        self._setNumber(1, value)
        return

    def getIsClaimVisible(self):
        return self._getBool(2)

    def setIsClaimVisible(self, value):
        self._setBool(2, value)
        return

    def getRewards(self):
        return self._getArray(3)

    def setRewards(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusItemViewModel

    def getState(self):
        return ArtefactStates(self._getString(4))

    def setState(self, value):
        self._setString(4, value.value)
        return

    def getTypes(self):
        return self._getArray(5)

    def setTypes(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getTypesType():
        return unicode

    def _initialize(self):
        super(RewardPathItemViewModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addNumberProperty(b'index', 0)
        self._addBoolProperty(b'isClaimVisible', False)
        self._addArrayProperty(b'rewards', Array())
        self._addStringProperty(b'state')
        self._addArrayProperty(b'types', Array())
        return
