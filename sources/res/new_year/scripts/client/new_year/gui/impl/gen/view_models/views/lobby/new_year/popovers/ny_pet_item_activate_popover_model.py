from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.pet.ny_indicator_type import NyIndicatorType

class NyPetItemActivatePopoverModel(NyIndicatorType):
    __slots__ = (b'onItemActivate', b'onItemAmountChange')

    def __init__(self, properties=9, commands=2):
        super(NyPetItemActivatePopoverModel, self).__init__(properties=properties, commands=commands)
        return

    def getItemsInInventory(self):
        return self._getNumber(1)

    def setItemsInInventory(self, value):
        self._setNumber(1, value)
        return

    def getLoyaltyPoints(self):
        return self._getNumber(2)

    def setLoyaltyPoints(self, value):
        self._setNumber(2, value)
        return

    def getVitalityPoints(self):
        return self._getNumber(3)

    def setVitalityPoints(self, value):
        self._setNumber(3, value)
        return

    def getPotentialLoyaltyPoints(self):
        return self._getNumber(4)

    def setPotentialLoyaltyPoints(self, value):
        self._setNumber(4, value)
        return

    def getPotentialVitalityPoints(self):
        return self._getNumber(5)

    def setPotentialVitalityPoints(self, value):
        self._setNumber(5, value)
        return

    def getIsOnboarding(self):
        return self._getBool(6)

    def setIsOnboarding(self, value):
        self._setBool(6, value)
        return

    def getWasLeaderboardFinished(self):
        return self._getBool(7)

    def setWasLeaderboardFinished(self, value):
        self._setBool(7, value)
        return

    def getMaxValue(self):
        return self._getNumber(8)

    def setMaxValue(self, value):
        self._setNumber(8, value)
        return

    def _initialize(self):
        super(NyPetItemActivatePopoverModel, self)._initialize()
        self._addNumberProperty(b'itemsInInventory', 0)
        self._addNumberProperty(b'loyaltyPoints', 0)
        self._addNumberProperty(b'vitalityPoints', 0)
        self._addNumberProperty(b'potentialLoyaltyPoints', 0)
        self._addNumberProperty(b'potentialVitalityPoints', 0)
        self._addBoolProperty(b'isOnboarding', False)
        self._addBoolProperty(b'wasLeaderboardFinished', False)
        self._addNumberProperty(b'maxValue', -1)
        self.onItemActivate = self._addCommand(b'onItemActivate')
        self.onItemAmountChange = self._addCommand(b'onItemAmountChange')
        return
