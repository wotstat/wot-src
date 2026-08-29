from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.nation_change.nation_change_tank_setup_model import NationChangeTankSetupModel

class NationChangeTankSlotModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(NationChangeTankSlotModel, self).__init__(properties=properties, commands=commands)
        return

    def getTankImage(self):
        return self._getResource(0)

    def setTankImage(self, value):
        self._setResource(0, value)
        return

    def getVehicleIntCD(self):
        return self._getNumber(1)

    def setVehicleIntCD(self, value):
        self._setNumber(1, value)
        return

    def getTankNation(self):
        return self._getString(2)

    def setTankNation(self, value):
        self._setString(2, value)
        return

    def getNoEquipment(self):
        return self._getBool(3)

    def setNoEquipment(self, value):
        self._setBool(3, value)
        return

    def getNoCrew(self):
        return self._getBool(4)

    def setNoCrew(self, value):
        self._setBool(4, value)
        return

    def getCrewList(self):
        return self._getArray(5)

    def setCrewList(self, value):
        self._setArray(5, value)
        return

    def getSetups(self):
        return self._getArray(6)

    def setSetups(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getSetupsType():
        return NationChangeTankSetupModel

    def _initialize(self):
        super(NationChangeTankSlotModel, self)._initialize()
        self._addResourceProperty(b'tankImage', R.invalid())
        self._addNumberProperty(b'vehicleIntCD', 0)
        self._addStringProperty(b'tankNation', b'')
        self._addBoolProperty(b'noEquipment', True)
        self._addBoolProperty(b'noCrew', True)
        self._addArrayProperty(b'crewList', Array())
        self._addArrayProperty(b'setups', Array())
        return
