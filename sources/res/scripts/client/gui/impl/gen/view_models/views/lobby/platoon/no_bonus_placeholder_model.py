from frameworks.wulf import ViewModel
from gui.impl.gen import R

class NoBonusPlaceholderModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(NoBonusPlaceholderModel, self).__init__(properties=properties, commands=commands)
        return

    def getText(self):
        return self._getResource(0)

    def setText(self, value):
        self._setResource(0, value)
        return

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def _initialize(self):
        super(NoBonusPlaceholderModel, self)._initialize()
        self._addResourceProperty(b'text', R.invalid())
        self._addResourceProperty(b'icon', R.invalid())
        return
