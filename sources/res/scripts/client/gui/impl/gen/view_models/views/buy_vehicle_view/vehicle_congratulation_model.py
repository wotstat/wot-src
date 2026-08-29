from gui.impl.gen import R
from frameworks.wulf import ViewModel

class VehicleCongratulationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=12, commands=0):
        super(VehicleCongratulationModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsElite(self):
        return self._getBool(0)

    def setIsElite(self, value):
        self._setBool(0, value)
        return

    def getIsCollectible(self):
        return self._getBool(1)

    def setIsCollectible(self, value):
        self._setBool(1, value)
        return

    def getVehicleType(self):
        return self._getString(2)

    def setVehicleType(self, value):
        self._setString(2, value)
        return

    def getLvl(self):
        return self._getString(3)

    def setLvl(self, value):
        self._setString(3, value)
        return

    def getVName(self):
        return self._getString(4)

    def setVName(self, value):
        self._setString(4, value)
        return

    def getImage(self):
        return self._getString(5)

    def setImage(self, value):
        self._setString(5, value)
        return

    def getImageAlt(self):
        return self._getString(6)

    def setImageAlt(self, value):
        self._setString(6, value)
        return

    def getBtnLbl(self):
        return self._getResource(7)

    def setBtnLbl(self, value):
        self._setResource(7, value)
        return

    def getBackBtnLbl(self):
        return self._getResource(8)

    def setBackBtnLbl(self, value):
        self._setResource(8, value)
        return

    def getTitle(self):
        return self._getResource(9)

    def setTitle(self, value):
        self._setResource(9, value)
        return

    def getResetAnimTrigger(self):
        return self._getBool(10)

    def setResetAnimTrigger(self, value):
        self._setBool(10, value)
        return

    def getNeedBackBtn(self):
        return self._getBool(11)

    def setNeedBackBtn(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(VehicleCongratulationModel, self)._initialize()
        self._addBoolProperty(b'isElite', False)
        self._addBoolProperty(b'isCollectible', False)
        self._addStringProperty(b'vehicleType', b'')
        self._addStringProperty(b'lvl', b'')
        self._addStringProperty(b'vName', b'')
        self._addStringProperty(b'image', b'')
        self._addStringProperty(b'imageAlt', b'')
        self._addResourceProperty(b'btnLbl', R.invalid())
        self._addResourceProperty(b'backBtnLbl', R.invalid())
        self._addResourceProperty(b'title', R.invalid())
        self._addBoolProperty(b'resetAnimTrigger', False)
        self._addBoolProperty(b'needBackBtn', False)
        return
