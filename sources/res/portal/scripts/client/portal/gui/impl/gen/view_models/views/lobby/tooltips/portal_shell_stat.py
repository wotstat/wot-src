from frameworks.wulf import ViewModel

class PortalShellStat(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(PortalShellStat, self).__init__(properties=properties, commands=commands)
        return

    def getFrom(self):
        return self._getNumber(0)

    def setFrom(self, value):
        self._setNumber(0, value)
        return

    def getTo(self):
        return self._getNumber(1)

    def setTo(self, value):
        self._setNumber(1, value)
        return

    def getName(self):
        return self._getString(2)

    def setName(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(PortalShellStat, self)._initialize()
        self._addNumberProperty(b'from', 0)
        self._addNumberProperty(b'to', 0)
        self._addStringProperty(b'name', b'')
        return
