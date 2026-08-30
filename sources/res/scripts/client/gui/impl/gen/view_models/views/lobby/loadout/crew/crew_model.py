from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.slot_model import SlotModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.tankman_model import TankmanModel

class CrewModel(ViewModel):
    __slots__ = (b'onOpenCrew', b'onOpenBarracks', b'onToggleAcceleratedTraining', b'onToggleIntensiveTraining', b'onDogMoreInfoClick')
    DEFAULT_STATE = b'default'
    DISABLED_STATE = b'disabled'
    ON_TRAINING_STATE = b'on'
    OFF_TRAINING_STATE = b'off'
    DISABLED_TRAINING_STATE = b'disabled'

    def __init__(self, properties=10, commands=5):
        super(CrewModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasDog(self):
        return self._getBool(0)

    def setHasDog(self, value):
        self._setBool(0, value)
        return

    def getCrew(self):
        return self._getArray(1)

    def setCrew(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getCrewType():
        return TankmanModel

    def getSlots(self):
        return self._getArray(2)

    def setSlots(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getSlotsType():
        return SlotModel

    def getState(self):
        return self._getString(3)

    def setState(self, value):
        self._setString(3, value)
        return

    def getBerthsCount(self):
        return self._getNumber(4)

    def setBerthsCount(self, value):
        self._setNumber(4, value)
        return

    def getAcceleratedTraining(self):
        return self._getString(5)

    def setAcceleratedTraining(self, value):
        self._setString(5, value)
        return

    def getIntensiveTraining(self):
        return self._getString(6)

    def setIntensiveTraining(self, value):
        self._setString(6, value)
        return

    def getVehicleNation(self):
        return self._getString(7)

    def setVehicleNation(self, value):
        self._setString(7, value)
        return

    def getVehicleType(self):
        return self._getString(8)

    def setVehicleType(self, value):
        self._setString(8, value)
        return

    def getVehicleName(self):
        return self._getString(9)

    def setVehicleName(self, value):
        self._setString(9, value)
        return

    def _initialize(self):
        super(CrewModel, self)._initialize()
        self._addBoolProperty(b'hasDog', False)
        self._addArrayProperty(b'crew', Array())
        self._addArrayProperty(b'slots', Array())
        self._addStringProperty(b'state', b'default')
        self._addNumberProperty(b'berthsCount', 0)
        self._addStringProperty(b'acceleratedTraining', b'')
        self._addStringProperty(b'intensiveTraining', b'')
        self._addStringProperty(b'vehicleNation', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleName', b'')
        self.onOpenCrew = self._addCommand(b'onOpenCrew')
        self.onOpenBarracks = self._addCommand(b'onOpenBarracks')
        self.onToggleAcceleratedTraining = self._addCommand(b'onToggleAcceleratedTraining')
        self.onToggleIntensiveTraining = self._addCommand(b'onToggleIntensiveTraining')
        self.onDogMoreInfoClick = self._addCommand(b'onDogMoreInfoClick')
        return
