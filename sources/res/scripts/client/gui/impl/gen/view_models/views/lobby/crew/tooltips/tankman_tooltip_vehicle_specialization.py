from gui.impl.gen.view_models.common.vehicle_info_model import VehicleInfoModel

class TankmanTooltipVehicleSpecialization(VehicleInfoModel):
    __slots__ = ()

    def __init__(self, properties=13, commands=0):
        super(TankmanTooltipVehicleSpecialization, self).__init__(properties=properties, commands=commands)
        return

    def getSpecializationLevel(self):
        return self._getNumber(10)

    def setSpecializationLevel(self, value):
        self._setNumber(10, value)
        return

    def getHasPenalty(self):
        return self._getBool(11)

    def setHasPenalty(self, value):
        self._setBool(11, value)
        return

    def getNation(self):
        return self._getString(12)

    def setNation(self, value):
        self._setString(12, value)
        return

    def _initialize(self):
        super(TankmanTooltipVehicleSpecialization, self)._initialize()
        self._addNumberProperty(b'specializationLevel', 0)
        self._addBoolProperty(b'hasPenalty', False)
        self._addStringProperty(b'nation', b'')
        return
