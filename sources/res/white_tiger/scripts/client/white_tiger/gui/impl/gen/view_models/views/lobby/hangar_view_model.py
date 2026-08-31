from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class WhiteTigerVehicles(Enum):
    NONE = b'none'
    BT110 = b'BT110'
    BT220 = b'BT220'
    RESISTOR = b'RESISTOR'
    THUNDERBOLT = b'THUNDERBOLT'
    FOUDRE = b'FOUDRE'
    POJISTKA = b'POJISTKA'


class HangarViewModel(ViewModel):
    __slots__ = (b'onEscPressed', b'onInfoClicked', b'onViewLoaded', b'onNarrativeClicked')

    def __init__(self, properties=3, commands=4):
        super(HangarViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def router(self):
        return self._getViewModel(0)

    @staticmethod
    def getRouterType():
        return RouterModel

    def getSelectedVehicle(self):
        return WhiteTigerVehicles(self._getString(1))

    def setSelectedVehicle(self, value):
        self._setString(1, value.value)
        return

    def getIsNarrativeAvailable(self):
        return self._getBool(2)

    def setIsNarrativeAvailable(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(HangarViewModel, self)._initialize()
        self._addViewModelProperty(b'router', RouterModel())
        self._addStringProperty(b'selectedVehicle')
        self._addBoolProperty(b'isNarrativeAvailable', False)
        self.onEscPressed = self._addCommand(b'onEscPressed')
        self.onInfoClicked = self._addCommand(b'onInfoClicked')
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        self.onNarrativeClicked = self._addCommand(b'onNarrativeClicked')
        return
