from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_base_view_model import VehicleParamBaseViewModel

class VehicleParamViewModel(VehicleParamBaseViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(VehicleParamViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getString(5)

    def setName(self, value):
        self._setString(5, value)
        return

    def getParentID(self):
        return self._getString(6)

    def setParentID(self, value):
        self._setString(6, value)
        return

    def _initialize(self):
        super(VehicleParamViewModel, self)._initialize()
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'parentID', b'')
        return
