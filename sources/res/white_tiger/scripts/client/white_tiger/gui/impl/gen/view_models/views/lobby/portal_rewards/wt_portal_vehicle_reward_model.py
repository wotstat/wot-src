from white_tiger.gui.impl.gen.view_models.views.lobby.portal_rewards.wt_portal_rewards_base_model import WtPortalRewardsBaseModel

class WtPortalVehicleRewardModel(WtPortalRewardsBaseModel):
    __slots__ = (b'onIntroVideoPlay', b'onVehicleVideoComplete', b'onVideoInterrupt')

    def __init__(self, properties=9, commands=7):
        super(WtPortalVehicleRewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getIntroVideoName(self):
        return self._getString(4)

    def setIntroVideoName(self, value):
        self._setString(4, value)
        return

    def getVehicleVideoName(self):
        return self._getString(5)

    def setVehicleVideoName(self, value):
        self._setString(5, value)
        return

    def getIsWindowAccessible(self):
        return self._getBool(6)

    def setIsWindowAccessible(self, value):
        self._setBool(6, value)
        return

    def getIsLastVideo(self):
        return self._getBool(7)

    def setIsLastVideo(self, value):
        self._setBool(7, value)
        return

    def getRemainingVideoNumber(self):
        return self._getNumber(8)

    def setRemainingVideoNumber(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(WtPortalVehicleRewardModel, self)._initialize()
        self._addStringProperty(b'introVideoName', b'')
        self._addStringProperty(b'vehicleVideoName', b'')
        self._addBoolProperty(b'isWindowAccessible', True)
        self._addBoolProperty(b'isLastVideo', False)
        self._addNumberProperty(b'remainingVideoNumber', 0)
        self.onIntroVideoPlay = self._addCommand(b'onIntroVideoPlay')
        self.onVehicleVideoComplete = self._addCommand(b'onVehicleVideoComplete')
        self.onVideoInterrupt = self._addCommand(b'onVideoInterrupt')
        return
