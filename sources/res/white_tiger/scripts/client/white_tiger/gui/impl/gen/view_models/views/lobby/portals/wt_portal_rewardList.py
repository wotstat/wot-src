from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from white_tiger.gui.impl.gen.view_models.views.lobby.portals.wt_portal_bonus_model import WtPortalBonusModel

class slotType(Enum):
    DEFAULT = b'default'
    EPIC = b'epic'


class WtPortalRewardlist(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(WtPortalRewardlist, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getProbability(self):
        return self._getString(1)

    def setProbability(self, value):
        self._setString(1, value)
        return

    def getProbabilityIconPath(self):
        return self._getString(2)

    def setProbabilityIconPath(self, value):
        self._setString(2, value)
        return

    def getIndex(self):
        return self._getNumber(3)

    def setIndex(self, value):
        self._setNumber(3, value)
        return

    def getSlotType(self):
        return slotType(self._getString(4))

    def setSlotType(self, value):
        self._setString(4, value.value)
        return

    def getRewards(self):
        return self._getArray(5)

    def setRewards(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getRewardsType():
        return WtPortalBonusModel

    def _initialize(self):
        super(WtPortalRewardlist, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'probability', b'')
        self._addStringProperty(b'probabilityIconPath', b'')
        self._addNumberProperty(b'index', 0)
        self._addStringProperty(b'slotType')
        self._addArrayProperty(b'rewards', Array())
        return
