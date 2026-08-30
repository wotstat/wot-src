from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class SelectRespawnViewModel(ViewModel):
    __slots__ = (b'onCompleteBtnClick', b'onSelectPoint')

    def __init__(self, properties=12, commands=2):
        super(SelectRespawnViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getHeader(self):
        return self._getResource(0)

    def setHeader(self, value):
        self._setResource(0, value)
        return

    def getDescription(self):
        return self._getResource(1)

    def setDescription(self, value):
        self._setResource(1, value)
        return

    def getLeftTime(self):
        return self._getString(2)

    def setLeftTime(self, value):
        self._setString(2, value)
        return

    def getBtnDescription(self):
        return self._getResource(3)

    def setBtnDescription(self, value):
        self._setResource(3, value)
        return

    def getPoints(self):
        return self._getArray(4)

    def setPoints(self, value):
        self._setArray(4, value)
        return

    def getBackground(self):
        return self._getResource(5)

    def setBackground(self, value):
        self._setResource(5, value)
        return

    def getMinimapBG(self):
        return self._getString(6)

    def setMinimapBG(self, value):
        self._setString(6, value)
        return

    def getMapSize(self):
        return self._getNumber(7)

    def setMapSize(self, value):
        self._setNumber(7, value)
        return

    def getSelectedPointID(self):
        return self._getString(8)

    def setSelectedPointID(self, value):
        self._setString(8, value)
        return

    def getIsTimeRunningOut(self):
        return self._getBool(9)

    def setIsTimeRunningOut(self, value):
        self._setBool(9, value)
        return

    def getIsWaitingPlayers(self):
        return self._getBool(10)

    def setIsWaitingPlayers(self, value):
        self._setBool(10, value)
        return

    def getIsReplay(self):
        return self._getBool(11)

    def setIsReplay(self, value):
        self._setBool(11, value)
        return

    def _initialize(self):
        super(SelectRespawnViewModel, self)._initialize()
        self._addResourceProperty(b'header', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        self._addStringProperty(b'leftTime', b'')
        self._addResourceProperty(b'btnDescription', R.invalid())
        self._addArrayProperty(b'points', Array())
        self._addResourceProperty(b'background', R.invalid())
        self._addStringProperty(b'minimapBG', b'')
        self._addNumberProperty(b'mapSize', 0)
        self._addStringProperty(b'selectedPointID', b'')
        self._addBoolProperty(b'isTimeRunningOut', False)
        self._addBoolProperty(b'isWaitingPlayers', False)
        self._addBoolProperty(b'isReplay', False)
        self.onCompleteBtnClick = self._addCommand(b'onCompleteBtnClick')
        self.onSelectPoint = self._addCommand(b'onSelectPoint')
        return
