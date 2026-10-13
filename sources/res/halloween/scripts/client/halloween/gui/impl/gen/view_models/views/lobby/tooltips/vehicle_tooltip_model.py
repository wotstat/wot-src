from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.loadout.crew.slot_model import SlotModel

class VehicleTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(VehicleTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)
        return

    def getVehicleType(self):
        return self._getString(1)

    def setVehicleType(self, value):
        self._setString(1, value)
        return

    def getVehicleState(self):
        return self._getString(2)

    def setVehicleState(self, value):
        self._setString(2, value)
        return

    def getUserName(self):
        return self._getString(3)

    def setUserName(self, value):
        self._setString(3, value)
        return

    def getUserDescription(self):
        return self._getString(4)

    def setUserDescription(self, value):
        self._setString(4, value)
        return

    def getIsElite(self):
        return self._getBool(5)

    def setIsElite(self, value):
        self._setBool(5, value)
        return

    def getIsDailyKeyQuestVisible(self):
        return self._getBool(6)

    def setIsDailyKeyQuestVisible(self, value):
        self._setBool(6, value)
        return

    def getIsStatusVisible(self):
        return self._getBool(7)

    def setIsStatusVisible(self, value):
        self._setBool(7, value)
        return

    def getCrewSlots(self):
        return self._getArray(8)

    def setCrewSlots(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getCrewSlotsType():
        return SlotModel

    def _initialize(self):
        super(VehicleTooltipModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'vehicleState', b'')
        self._addStringProperty(b'userName', b'')
        self._addStringProperty(b'userDescription', b'')
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isDailyKeyQuestVisible', False)
        self._addBoolProperty(b'isStatusVisible', False)
        self._addArrayProperty(b'crewSlots', Array())
        return
