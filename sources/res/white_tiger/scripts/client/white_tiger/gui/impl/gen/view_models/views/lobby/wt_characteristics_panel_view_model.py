from frameworks.wulf import Array
from gui.impl.gen import R
from frameworks.wulf import ViewModel
from white_tiger.gui.impl.gen.view_models.views.lobby.wt_characteristic_model import WtCharacteristicModel

class WtCharacteristicsPanelViewModel(ViewModel):
    __slots__ = (b'onLeaveClicked',)

    def __init__(self, properties=3, commands=1):
        super(WtCharacteristicsPanelViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSpecialInfo(self):
        return self._getResource(0)

    def setSpecialInfo(self, value):
        self._setResource(0, value)
        return

    def getPros(self):
        return self._getArray(1)

    def setPros(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getProsType():
        return WtCharacteristicModel

    def getCons(self):
        return self._getArray(2)

    def setCons(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getConsType():
        return WtCharacteristicModel

    def _initialize(self):
        super(WtCharacteristicsPanelViewModel, self)._initialize()
        self._addResourceProperty(b'specialInfo', R.invalid())
        self._addArrayProperty(b'pros', Array())
        self._addArrayProperty(b'cons', Array())
        self.onLeaveClicked = self._addCommand(b'onLeaveClicked')
        return
