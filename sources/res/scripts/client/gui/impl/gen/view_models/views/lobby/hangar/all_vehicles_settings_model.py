from frameworks.wulf import ViewModel

class AllVehiclesSettingsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(AllVehiclesSettingsModel, self).__init__(properties=properties, commands=commands)
        return

    def getCrewEnabled(self):
        return self._getBool(0)

    def setCrewEnabled(self, value):
        self._setBool(0, value)
        return

    def getTtcEnabled(self):
        return self._getBool(1)

    def setTtcEnabled(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(AllVehiclesSettingsModel, self)._initialize()
        self._addBoolProperty(b'crewEnabled', False)
        self._addBoolProperty(b'ttcEnabled', False)
        return
