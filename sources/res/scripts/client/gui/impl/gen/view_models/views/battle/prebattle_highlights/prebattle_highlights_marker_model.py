from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel

class PrebattleHighlightsMarkerModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(PrebattleHighlightsMarkerModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def userName(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserNameType():
        return UserNameModel

    @property
    def vehicle(self):
        return self._getViewModel(1)

    @staticmethod
    def getVehicleType():
        return VehicleModel

    @property
    def prestigeEmblem(self):
        return self._getViewModel(2)

    @staticmethod
    def getPrestigeEmblemType():
        return PrestigeEmblemModel

    def getPersonal(self):
        return self._getBool(3)

    def setPersonal(self, value):
        self._setBool(3, value)
        return

    def getPosx(self):
        return self._getReal(4)

    def setPosx(self, value):
        self._setReal(4, value)
        return

    def getPosy(self):
        return self._getReal(5)

    def setPosy(self, value):
        self._setReal(5, value)
        return

    def getSquadIndex(self):
        return self._getNumber(6)

    def setSquadIndex(self, value):
        self._setNumber(6, value)
        return

    def getVehId(self):
        return self._getNumber(7)

    def setVehId(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(PrebattleHighlightsMarkerModel, self)._initialize()
        self._addViewModelProperty(b'userName', UserNameModel())
        self._addViewModelProperty(b'vehicle', VehicleModel())
        self._addViewModelProperty(b'prestigeEmblem', PrestigeEmblemModel())
        self._addBoolProperty(b'personal', False)
        self._addRealProperty(b'posx', 0.0)
        self._addRealProperty(b'posy', 0.0)
        self._addNumberProperty(b'squadIndex', 0)
        self._addNumberProperty(b'vehId', 0)
        return
