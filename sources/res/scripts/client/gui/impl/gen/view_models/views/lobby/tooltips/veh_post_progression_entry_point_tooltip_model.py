from frameworks.wulf import ViewModel
from gui.impl.gen import R

class VehPostProgressionEntryPointTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(VehPostProgressionEntryPointTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getModulesExplored(self):
        return self._getNumber(0)

    def setModulesExplored(self, value):
        self._setNumber(0, value)
        return

    def getModulesTotal(self):
        return self._getNumber(1)

    def setModulesTotal(self, value):
        self._setNumber(1, value)
        return

    def getHeader(self):
        return self._getResource(2)

    def setHeader(self, value):
        self._setResource(2, value)
        return

    def getDescription(self):
        return self._getResource(3)

    def setDescription(self, value):
        self._setResource(3, value)
        return

    def getStatus(self):
        return self._getResource(4)

    def setStatus(self, value):
        self._setResource(4, value)
        return

    def getHasVehiclesToUnlock(self):
        return self._getBool(5)

    def setHasVehiclesToUnlock(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(VehPostProgressionEntryPointTooltipModel, self)._initialize()
        self._addNumberProperty(b'modulesExplored', 0)
        self._addNumberProperty(b'modulesTotal', 0)
        self._addResourceProperty(b'header', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        self._addResourceProperty(b'status', R.invalid())
        self._addBoolProperty(b'hasVehiclesToUnlock', False)
        return
