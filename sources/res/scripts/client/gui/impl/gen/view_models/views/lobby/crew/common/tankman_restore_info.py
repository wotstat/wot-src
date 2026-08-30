from frameworks.wulf import ViewModel

class TankmanRestoreInfo(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TankmanRestoreInfo, self).__init__(properties=properties, commands=commands)
        return

    def getFreePeriod(self):
        return self._getNumber(0)

    def setFreePeriod(self, value):
        self._setNumber(0, value)
        return

    def getPaidPeriod(self):
        return self._getNumber(1)

    def setPaidPeriod(self, value):
        self._setNumber(1, value)
        return

    def getRecoverPrice(self):
        return self._getNumber(2)

    def setRecoverPrice(self, value):
        self._setNumber(2, value)
        return

    def getMembersBuffer(self):
        return self._getNumber(3)

    def setMembersBuffer(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(TankmanRestoreInfo, self)._initialize()
        self._addNumberProperty(b'freePeriod', 0)
        self._addNumberProperty(b'paidPeriod', 0)
        self._addNumberProperty(b'recoverPrice', 0)
        self._addNumberProperty(b'membersBuffer', 0)
        return
