from frameworks.wulf import ViewModel
from gui.impl.gen import R

class MissionConditionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(MissionConditionModel, self).__init__(properties=properties, commands=commands)
        return

    def getIcon(self):
        return self._getResource(0)

    def setIcon(self, value):
        self._setResource(0, value)
        return

    def getText(self):
        return self._getString(1)

    def setText(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(MissionConditionModel, self)._initialize()
        self._addResourceProperty(b'icon', R.invalid())
        self._addStringProperty(b'text', b'')
        return
