from frameworks.wulf import ViewModel

class WellPanelModel(ViewModel):
    __slots__ = (b'onAction',)

    def __init__(self, properties=4, commands=1):
        super(WellPanelModel, self).__init__(properties=properties, commands=commands)
        return

    def getTopRewardsCount(self):
        return self._getNumber(0)

    def setTopRewardsCount(self, value):
        self._setNumber(0, value)
        return

    def getRegularRewardsCount(self):
        return self._getNumber(1)

    def setRegularRewardsCount(self, value):
        self._setNumber(1, value)
        return

    def getVehicleName(self):
        return self._getString(2)

    def setVehicleName(self, value):
        self._setString(2, value)
        return

    def getIsVisible(self):
        return self._getBool(3)

    def setIsVisible(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(WellPanelModel, self)._initialize()
        self._addNumberProperty(b'topRewardsCount', 0)
        self._addNumberProperty(b'regularRewardsCount', 0)
        self._addStringProperty(b'vehicleName', b'')
        self._addBoolProperty(b'isVisible', False)
        self.onAction = self._addCommand(b'onAction')
        return
