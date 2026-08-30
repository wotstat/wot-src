from frameworks.wulf import ViewModel

class RewardInfoModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(RewardInfoModel, self).__init__(properties=properties, commands=commands)
        return

    def getVehicleName(self):
        return self._getString(0)

    def setVehicleName(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(RewardInfoModel, self)._initialize()
        self._addStringProperty(b'vehicleName', b'')
        return
