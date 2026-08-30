from frameworks.wulf import ViewModel

class BannerTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(BannerTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return self._getString(0)

    def setState(self, value):
        self._setString(0, value)
        return

    def getEventStartDate(self):
        return self._getNumber(1)

    def setEventStartDate(self, value):
        self._setNumber(1, value)
        return

    def getEventEndDate(self):
        return self._getNumber(2)

    def setEventEndDate(self, value):
        self._setNumber(2, value)
        return

    def getRewardsCount(self):
        return self._getNumber(3)

    def setRewardsCount(self, value):
        self._setNumber(3, value)
        return

    def getCurLevel(self):
        return self._getNumber(4)

    def setCurLevel(self, value):
        self._setNumber(4, value)
        return

    def getMaxLevel(self):
        return self._getNumber(5)

    def setMaxLevel(self, value):
        self._setNumber(5, value)
        return

    def getCurPoints(self):
        return self._getNumber(6)

    def setCurPoints(self, value):
        self._setNumber(6, value)
        return

    def getMaxPoints(self):
        return self._getNumber(7)

    def setMaxPoints(self, value):
        self._setNumber(7, value)
        return

    def getVehiclesLevel(self):
        return self._getString(8)

    def setVehiclesLevel(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(BannerTooltipModel, self)._initialize()
        self._addStringProperty(b'state', b'')
        self._addNumberProperty(b'eventStartDate', 0)
        self._addNumberProperty(b'eventEndDate', 0)
        self._addNumberProperty(b'rewardsCount', 0)
        self._addNumberProperty(b'curLevel', 0)
        self._addNumberProperty(b'maxLevel', 0)
        self._addNumberProperty(b'curPoints', 0)
        self._addNumberProperty(b'maxPoints', 0)
        self._addStringProperty(b'vehiclesLevel', b'')
        return
