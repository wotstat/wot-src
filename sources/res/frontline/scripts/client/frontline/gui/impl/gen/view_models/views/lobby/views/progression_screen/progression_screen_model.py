from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.progression_screen.tiers_section_model import TiersSectionModel

class ProgressionScreenModel(ViewModel):
    __slots__ = (b'onClaimRewards', b'onClose')

    def __init__(self, properties=9, commands=2):
        super(ProgressionScreenModel, self).__init__(properties=properties, commands=commands)
        return

    def getFrontlineState(self):
        return self._getString(0)

    def setFrontlineState(self, value):
        self._setString(0, value)
        return

    def getCountdownSeconds(self):
        return self._getNumber(1)

    def setCountdownSeconds(self, value):
        self._setNumber(1, value)
        return

    def getLevel(self):
        return self._getNumber(2)

    def setLevel(self, value):
        self._setNumber(2, value)
        return

    def getIsMaxLevel(self):
        return self._getBool(3)

    def setIsMaxLevel(self, value):
        self._setBool(3, value)
        return

    def getCurrentPoints(self):
        return self._getNumber(4)

    def setCurrentPoints(self, value):
        self._setNumber(4, value)
        return

    def getNeededPoints(self):
        return self._getNumber(5)

    def setNeededPoints(self, value):
        self._setNumber(5, value)
        return

    def getAmountRewardsToClaim(self):
        return self._getNumber(6)

    def setAmountRewardsToClaim(self, value):
        self._setNumber(6, value)
        return

    def getAreRewardsJustEarned(self):
        return self._getBool(7)

    def setAreRewardsJustEarned(self, value):
        self._setBool(7, value)
        return

    def getTiersSections(self):
        return self._getArray(8)

    def setTiersSections(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getTiersSectionsType():
        return TiersSectionModel

    def _initialize(self):
        super(ProgressionScreenModel, self)._initialize()
        self._addStringProperty(b'frontlineState', b'')
        self._addNumberProperty(b'countdownSeconds', 0)
        self._addNumberProperty(b'level', 0)
        self._addBoolProperty(b'isMaxLevel', False)
        self._addNumberProperty(b'currentPoints', 0)
        self._addNumberProperty(b'neededPoints', 0)
        self._addNumberProperty(b'amountRewardsToClaim', 0)
        self._addBoolProperty(b'areRewardsJustEarned', False)
        self._addArrayProperty(b'tiersSections', Array())
        self.onClaimRewards = self._addCommand(b'onClaimRewards')
        self.onClose = self._addCommand(b'onClose')
        return
