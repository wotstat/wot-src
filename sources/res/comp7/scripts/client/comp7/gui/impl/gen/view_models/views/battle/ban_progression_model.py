from comp7.gui.impl.gen.view_models.views.battle.enums import BanState
from frameworks.wulf import ViewModel

class BanProgressionModel(ViewModel):
    __slots__ = (b'pollServerTime',)

    def __init__(self, properties=4, commands=1):
        super(BanProgressionModel, self).__init__(properties=properties, commands=commands)
        return

    def getBanState(self):
        return BanState(self._getString(0))

    def setBanState(self, value):
        self._setString(0, value.value)
        return

    def getStartTimestamp(self):
        return self._getNumber(1)

    def setStartTimestamp(self, value):
        self._setNumber(1, value)
        return

    def getEndTimestamp(self):
        return self._getNumber(2)

    def setEndTimestamp(self, value):
        self._setNumber(2, value)
        return

    def getServerTimestamp(self):
        return self._getNumber(3)

    def setServerTimestamp(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(BanProgressionModel, self)._initialize()
        self._addStringProperty(b'banState')
        self._addNumberProperty(b'startTimestamp', 0)
        self._addNumberProperty(b'endTimestamp', 0)
        self._addNumberProperty(b'serverTimestamp', 0)
        self.pollServerTime = self._addCommand(b'pollServerTime')
        return
