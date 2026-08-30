from frameworks.wulf import ViewModel

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

    def getValue(self):
        return self._getString(1)

    def setValue(self, value):
        self._setString(1, value)
        return

    def getMetricValue(self):
        return self._getString(2)

    def setMetricValue(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(ShellSpecificationModel, self)._initialize()
        self._addStringProperty(b'paramName', b'')
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'metricValue', b'')
        return
