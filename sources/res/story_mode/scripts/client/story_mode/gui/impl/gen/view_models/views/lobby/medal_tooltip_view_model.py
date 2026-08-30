from frameworks.wulf import ViewModel
from gui.impl.gen import R

class MedalTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(MedalTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getResource(0)

    def setName(self, value):
        self._setResource(0, value)
        return

    def getImage(self):
        return self._getResource(1)

    def setImage(self, value):
        self._setResource(1, value)
        return

    def getConditions(self):
        return self._getResource(2)

    def setConditions(self, value):
        self._setResource(2, value)
        return

    def getDescription(self):
        return self._getResource(3)

    def setDescription(self, value):
        self._setResource(3, value)
        return

    def _initialize(self):
        super(MedalTooltipViewModel, self)._initialize()
        self._addResourceProperty(b'name', R.invalid())
        self._addResourceProperty(b'image', R.invalid())
        self._addResourceProperty(b'conditions', R.invalid())
        self._addResourceProperty(b'description', R.invalid())
        return
