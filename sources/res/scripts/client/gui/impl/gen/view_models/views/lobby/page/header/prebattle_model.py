from frameworks.wulf import Map, ViewModel
from gui.impl.gen.view_models.views.lobby.common.vehicle_model import VehicleModel

class PrebattleModel(ViewModel):
    __slots__ = (b'onAction',)
    PLAYER_CREATOR = b'playerCreator'
    PLAYER_READY = b'playerReady'
    READINESS_AVAILABLE = b'readinessAvailable'
    ACTION_ENABLED = b'actionEnabled'
    BATTLE_START_ACTION_TYPE = b'battleStartAction'
    BATTLE_READY_ACTION_TYPE = b'readyAction'
    BATTLE_EXIT_ACTION_TYPE = b'battleExitAction'
    BATTLE_STATE_IDLE = b'idle'
    BATTLE_STATE_SEARCHING = b'searchingBattle'
    BATTLE_STATE_READY = b'battleReady'
    E_SPORT = b'E_SPORT'
    TRAINING = b'TRAINING'
    BATTLE_SESSION = b'BATTLE_SESSION'
    RANDOM = b'RANDOM'
    EVENT = b'EVENT'
    STRONGHOLD = b'STRONGHOLD'
    RANKED = b'RANKED'
    EPIC_TRAINING = b'EPIC_TRAINING'
    TOURNAMENT = b'TOURNAMENT'
    EPIC = b'EPIC'
    BATTLE_ROYALE = b'BATTLE_ROYALE'
    MAPBOX = b'MAPBOX'
    MAPS_TRAINING = b'MAPS_TRAINING'
    BATTLE_ROYALE_TOURNAMENT = b'BATTLE_ROYALE_TOURNAMENT'

    def __init__(self, properties=7, commands=1):
        super(PrebattleModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def battleVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getBattleVehicleType():
        return VehicleModel

    def getStates(self):
        return self._getMap(1)

    def setStates(self, value):
        self._setMap(1, value)
        return

    @staticmethod
    def getStatesType():
        return (unicode, bool)

    def getCurrentMode(self):
        return self._getString(2)

    def setCurrentMode(self, value):
        self._setString(2, value)
        return

    def getCurrentModeId(self):
        return self._getString(3)

    def setCurrentModeId(self, value):
        self._setString(3, value)
        return

    def getQueueType(self):
        return self._getString(4)

    def setQueueType(self, value):
        self._setString(4, value)
        return

    def getBattleStatus(self):
        return self._getString(5)

    def setBattleStatus(self, value):
        self._setString(5, value)
        return

    def getBattleButtonAlwaysOn(self):
        return self._getBool(6)

    def setBattleButtonAlwaysOn(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(PrebattleModel, self)._initialize()
        self._addViewModelProperty(b'battleVehicle', VehicleModel())
        self._addMapProperty(b'states', Map(unicode, bool))
        self._addStringProperty(b'currentMode', b'')
        self._addStringProperty(b'currentModeId', b'')
        self._addStringProperty(b'queueType', b'')
        self._addStringProperty(b'battleStatus', b'')
        self._addBoolProperty(b'battleButtonAlwaysOn', False)
        self.onAction = self._addCommand(b'onAction')
        return
