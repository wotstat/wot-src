from frameworks.wulf import ViewModel

class WtBattleLoadingModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(WtBattleLoadingModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsBoss(self):
        return self._getBool(0)

    def setIsBoss(self, value):
        self._setBool(0, value)
        return

    def getVehicleName(self):
        return self._getString(1)

    def setVehicleName(self, value):
        self._setString(1, value)
        return

    def getProgress(self):
        return self._getReal(2)

    def setProgress(self, value):
        self._setReal(2, value)
        return

    def _initialize(self):
        super(WtBattleLoadingModel, self)._initialize()
        self._addBoolProperty(b'isBoss', False)
        self._addStringProperty(b'vehicleName', b'')
        self._addRealProperty(b'progress', 0.0)
        return
