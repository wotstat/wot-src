from frameworks.wulf import ViewModel

class PortalQuestWidget(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PortalQuestWidget, self).__init__(properties=properties, commands=commands)
        return

    def getCurrent(self):
        return self._getNumber(0)

    def setCurrent(self, value):
        self._setNumber(0, value)
        return

    def getMax(self):
        return self._getNumber(1)

    def setMax(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(PortalQuestWidget, self)._initialize()
        self._addNumberProperty(b'current', 0)
        self._addNumberProperty(b'max', 10)
        return
