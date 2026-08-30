from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_view_model import VehicleParamViewModel

class SpecialVehicleParamModel(VehicleParamViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(SpecialVehicleParamModel, self).__init__(properties=properties, commands=commands)
        return

    def getTemplate(self):
        return self._getString(7)

    def setTemplate(self, value):
        self._setString(7, value)
        return

    def getMeasureUnit(self):
        return self._getString(8)

    def setMeasureUnit(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(SpecialVehicleParamModel, self)._initialize()
        self._addStringProperty(b'template', b'')
        self._addStringProperty(b'measureUnit', b'')
        return
