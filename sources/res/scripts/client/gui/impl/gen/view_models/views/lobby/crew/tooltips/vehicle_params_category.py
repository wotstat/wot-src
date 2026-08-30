from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.tooltips.vehicle_params_item import VehicleParamsItem

class VehicleParamsCategory(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(VehicleParamsCategory, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getItems(self):
        return self._getArray(1)

    def setItems(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getItemsType():
        return VehicleParamsItem

    def _initialize(self):
        super(VehicleParamsCategory, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addArrayProperty(b'items', Array())
        return
