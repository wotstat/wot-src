from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.tooltips.parameters_values import ParametersValues

class ModulesParameters(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ModulesParameters, self).__init__(properties=properties, commands=commands)
        return

    def getValues(self):
        return self._getArray(0)

    def setValues(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getValuesType():
        return ParametersValues

    def getDescription(self):
        return self._getString(1)

    def setDescription(self, value):
        self._setString(1, value)
        return

    def getUnitOfMeasurement(self):
        return self._getString(2)

    def setUnitOfMeasurement(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(ModulesParameters, self)._initialize()
        self._addArrayProperty(b'values', Array())
        self._addStringProperty(b'description', b'')
        self._addStringProperty(b'unitOfMeasurement', b'')
        return
