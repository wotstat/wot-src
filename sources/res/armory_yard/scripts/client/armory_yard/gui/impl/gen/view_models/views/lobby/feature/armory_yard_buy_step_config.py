from frameworks.wulf import ViewModel

class ArmoryYardBuyStepConfig(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ArmoryYardBuyStepConfig, self).__init__(properties=properties, commands=commands)
        return

    def getHasVehicleInReward(self):
        return self._getBool(0)

    def setHasVehicleInReward(self, value):
        self._setBool(0, value)
        return

    def getVehicleRewardTooltipId(self):
        return self._getString(1)

    def setVehicleRewardTooltipId(self, value):
        self._setString(1, value)
        return

    def getVehicleRewardTooltipContentId(self):
        return self._getString(2)

    def setVehicleRewardTooltipContentId(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(ArmoryYardBuyStepConfig, self)._initialize()
        self._addBoolProperty(b'hasVehicleInReward', False)
        self._addStringProperty(b'vehicleRewardTooltipId', b'')
        self._addStringProperty(b'vehicleRewardTooltipContentId', b'')
        return
