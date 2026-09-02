from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel

class EnemyBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(EnemyBaseModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def user(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserType():
        return UserNameModel

    def getTankName(self):
        return self._getString(1)

    def setTankName(self, value):
        self._setString(1, value)
        return

    def getShortTankName(self):
        return self._getString(2)

    def setShortTankName(self, value):
        self._setString(2, value)
        return

    def getTankType(self):
        return self._getString(3)

    def setTankType(self, value):
        self._setString(3, value)
        return

    def getVehicleCD(self):
        return self._getNumber(4)

    def setVehicleCD(self, value):
        self._setNumber(4, value)
        return

    def getVehicleID(self):
        return self._getNumber(5)

    def setVehicleID(self, value):
        self._setNumber(5, value)
        return

    def getVehicleIconName(self):
        return self._getString(6)

    def setVehicleIconName(self, value):
        self._setString(6, value)
        return

    def getVehicleLevel(self):
        return self._getNumber(7)

    def setVehicleLevel(self, value):
        self._setNumber(7, value)
        return

    def getDbID(self):
        return self._getNumber(8)

    def setDbID(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(EnemyBaseModel, self)._initialize()
        self._addViewModelProperty(b'user', UserNameModel())
        self._addStringProperty(b'tankName', b'')
        self._addStringProperty(b'shortTankName', b'')
        self._addStringProperty(b'tankType', b'')
        self._addNumberProperty(b'vehicleCD', 0)
        self._addNumberProperty(b'vehicleID', 0)
        self._addStringProperty(b'vehicleIconName', b'')
        self._addNumberProperty(b'vehicleLevel', 0)
        self._addNumberProperty(b'dbID', 0)
        return
