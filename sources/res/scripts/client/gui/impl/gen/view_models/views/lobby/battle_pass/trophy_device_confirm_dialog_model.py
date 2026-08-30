from frameworks.wulf import Array
from frameworks.wulf import ViewModel

class TrophyDeviceConfirmDialogModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TrophyDeviceConfirmDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def getTrophyBasicName(self):
        return self._getString(0)

    def setTrophyBasicName(self, value):
        self._setString(0, value)
        return

    def getTrophyBasicImg(self):
        return self._getString(1)

    def setTrophyBasicImg(self, value):
        self._setString(1, value)
        return

    def getBonuses(self):
        return self._getArray(2)

    def setBonuses(self, value):
        self._setArray(2, value)
        return

    def getCredits(self):
        return self._getString(3)

    def setCredits(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(TrophyDeviceConfirmDialogModel, self)._initialize()
        self._addStringProperty(b'trophyBasicName', b'')
        self._addStringProperty(b'trophyBasicImg', b'')
        self._addArrayProperty(b'bonuses', Array())
        self._addStringProperty(b'credits', b'')
        return
