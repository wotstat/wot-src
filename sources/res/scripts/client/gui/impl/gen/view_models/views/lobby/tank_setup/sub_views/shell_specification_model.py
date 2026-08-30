from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.param_value_model import ParamValueModel

class ShellSpecificationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ShellSpecificationModel, self).__init__(properties=properties, commands=commands)
        return

    def getParamName(self):
        return self._getString(0)

    def setParamName(self, value):
        self._setString(0, value)
        return

    def getMetricValue(self):
        return self._getString(1)

    def setMetricValue(self, value):
        self._setString(1, value)
        return

    def getValues(self):
        return self._getArray(2)

    def setValues(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getValuesType():
        return ParamValueModel

    def _initialize(self):
        super(ShellSpecificationModel, self)._initialize()
        self._addStringProperty(b'paramName', b'')
        self._addStringProperty(b'metricValue', b'')
        self._addArrayProperty(b'values', Array())
        return
