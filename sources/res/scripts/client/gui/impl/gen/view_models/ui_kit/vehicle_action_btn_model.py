from gui.impl.gen import R
from frameworks.wulf import ViewModel

class VehicleActionBtnModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(VehicleActionBtnModel, self).__init__(properties=properties, commands=commands)
        return

    def getImage(self):
        return self._getResource(0)

    def setImage(self, value):
        self._setResource(0, value)
        return

    def getText(self):
        return self._getString(1)

    def setText(self, value):
        self._setString(1, value)
        return

    def getVisible(self):
        return self._getBool(2)

    def setVisible(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(VehicleActionBtnModel, self)._initialize()
        self._addResourceProperty(b'image', R.invalid())
        self._addStringProperty(b'text', b'')
        self._addBoolProperty(b'visible', False)
        return
