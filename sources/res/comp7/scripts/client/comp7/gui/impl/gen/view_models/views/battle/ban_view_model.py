from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.battle.ban_progression_model import BanProgressionModel
from comp7.gui.impl.gen.view_models.views.battle.comp7_vehicle_model import Comp7VehicleModel
from comp7.gui.impl.gen.view_models.views.battle.player_model import PlayerModel

class BanViewModel(ViewModel):
    __slots__ = (b'onClose', b'onConfirm', b'onSelect')

    def __init__(self, properties=7, commands=3):
        super(BanViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def banProgression(self):
        return self._getViewModel(0)

    @staticmethod
    def getBanProgressionType():
        return BanProgressionModel

    def getOwnId(self):
        return self._getNumber(1)

    def setOwnId(self, value):
        self._setNumber(1, value)
        return

    def getPlayers(self):
        return self._getArray(2)

    def setPlayers(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getPlayersType():
        return PlayerModel

    def getVehicles(self):
        return self._getArray(3)

    def setVehicles(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getVehiclesType():
        return Comp7VehicleModel

    def getNationsOrder(self):
        return self._getArray(4)

    def setNationsOrder(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getNationsOrderType():
        return unicode

    def getIsSelectionAvailable(self):
        return self._getBool(5)

    def setIsSelectionAvailable(self, value):
        self._setBool(5, value)
        return

    def getSelectedVehicleCD(self):
        return self._getNumber(6)

    def setSelectedVehicleCD(self, value):
        self._setNumber(6, value)
        return

    def _initialize(self):
        super(BanViewModel, self)._initialize()
        self._addViewModelProperty(b'banProgression', BanProgressionModel())
        self._addNumberProperty(b'ownId', 0)
        self._addArrayProperty(b'players', Array())
        self._addArrayProperty(b'vehicles', Array())
        self._addArrayProperty(b'nationsOrder', Array())
        self._addBoolProperty(b'isSelectionAvailable', True)
        self._addNumberProperty(b'selectedVehicleCD', -1)
        self.onClose = self._addCommand(b'onClose')
        self.onConfirm = self._addCommand(b'onConfirm')
        self.onSelect = self._addCommand(b'onSelect')
        return
