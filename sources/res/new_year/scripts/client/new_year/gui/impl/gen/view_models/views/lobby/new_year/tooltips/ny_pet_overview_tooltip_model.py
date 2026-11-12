from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_pet_indicator_model import NyPetIndicatorModel

class RaidStatus(Enum):
    NONE = b'none'
    READY = b'ready'
    ACTIVE = b'active'
    LOOT = b'loot'


class NyPetOverviewTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(NyPetOverviewTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentBonus(self):
        return self._getNumber(0)

    def setCurrentBonus(self, value):
        self._setNumber(0, value)
        return

    def getMinBonus(self):
        return self._getNumber(1)

    def setMinBonus(self, value):
        self._setNumber(1, value)
        return

    def getMaxBonus(self):
        return self._getNumber(2)

    def setMaxBonus(self, value):
        self._setNumber(2, value)
        return

    def getIsLeaderboard(self):
        return self._getBool(3)

    def setIsLeaderboard(self, value):
        self._setBool(3, value)
        return

    def getIndicators(self):
        return self._getArray(4)

    def setIndicators(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getIndicatorsType():
        return NyPetIndicatorModel

    def getRaidStatus(self):
        return RaidStatus(self._getString(5))

    def setRaidStatus(self, value):
        self._setString(5, value.value)
        return

    def getRaidTimeLeft(self):
        return self._getNumber(6)

    def setRaidTimeLeft(self, value):
        self._setNumber(6, value)
        return

    def getShowRaidInvite(self):
        return self._getBool(7)

    def setShowRaidInvite(self, value):
        self._setBool(7, value)
        return

    def _initialize(self):
        super(NyPetOverviewTooltipModel, self)._initialize()
        self._addNumberProperty(b'currentBonus', 0)
        self._addNumberProperty(b'minBonus', 0)
        self._addNumberProperty(b'maxBonus', 0)
        self._addBoolProperty(b'isLeaderboard', True)
        self._addArrayProperty(b'indicators', Array())
        self._addStringProperty(b'raidStatus', RaidStatus.NONE.value)
        self._addNumberProperty(b'raidTimeLeft', 0)
        self._addBoolProperty(b'showRaidInvite', False)
        return
