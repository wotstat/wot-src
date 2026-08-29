from enum import IntEnum
from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_base_view_model import VehicleParamBaseViewModel
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_indicator_view_model import VehicleParamIndicatorViewModel
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.vehicle_param_view_model import VehicleParamViewModel

class BuffIconType(IntEnum):
    NONE = 0
    INCREASE = 1
    DECREASE = 2
    MIXED = 3


class VehicleParamGroupViewModel(VehicleParamBaseViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(VehicleParamGroupViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def indicator(self):
        return self._getViewModel(5)

    @staticmethod
    def getIndicatorType():
        return VehicleParamIndicatorViewModel

    def getIsOpen(self):
        return self._getBool(6)

    def setIsOpen(self, value):
        self._setBool(6, value)
        return

    def getBuffIconType(self):
        return BuffIconType(self._getNumber(7))

    def setBuffIconType(self, value):
        self._setNumber(7, value.value)
        return

    def getAdditionalValue(self):
        return self._getString(8)

    def setAdditionalValue(self, value):
        self._setString(8, value)
        return

    def getParams(self):
        return self._getArray(9)

    def setParams(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getParamsType():
        return VehicleParamViewModel

    def getExtraParams(self):
        return self._getArray(10)

    def setExtraParams(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getExtraParamsType():
        return VehicleParamViewModel

    def _initialize(self):
        super(VehicleParamGroupViewModel, self)._initialize()
        self._addViewModelProperty(b'indicator', VehicleParamIndicatorViewModel())
        self._addBoolProperty(b'isOpen', False)
        self._addNumberProperty(b'buffIconType')
        self._addStringProperty(b'additionalValue', b'')
        self._addArrayProperty(b'params', Array())
        self._addArrayProperty(b'extraParams', Array())
        return
