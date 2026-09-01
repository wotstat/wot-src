from frameworks.wulf import Array
from gui.impl.gen.view_models.common.vehicle_mechanic_model import VehicleMechanicModel
from gui.impl.gen.view_models.views.lobby.tank_setup.common.base_ammunition_slot import BaseAmmunitionSlot

class ShellAmmunitionSlot(BaseAmmunitionSlot):
    __slots__ = ()

    def __init__(self, properties=16, commands=0):
        super(ShellAmmunitionSlot, self).__init__(properties=properties, commands=commands)
        return

    def getCount(self):
        return self._getNumber(13)

    def setCount(self, value):
        self._setNumber(13, value)
        return

    def getIsInfinity(self):
        return self._getBool(14)

    def setIsInfinity(self, value):
        self._setBool(14, value)
        return

    def getMechanics(self):
        return self._getArray(15)

    def setMechanics(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getMechanicsType():
        return VehicleMechanicModel

    def _initialize(self):
        super(ShellAmmunitionSlot, self)._initialize()
        self._addNumberProperty(b'count', 0)
        self._addBoolProperty(b'isInfinity', False)
        self._addArrayProperty(b'mechanics', Array())
        return
