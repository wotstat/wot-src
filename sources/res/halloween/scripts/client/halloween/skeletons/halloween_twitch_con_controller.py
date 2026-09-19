from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class IHalloweenTwitchConController(IGameController):
    onLimitsUpdated = None
    onShopLimitsUpdated = None
    onCertificateCountUpdated = None
    onTwitchConSettingsUpdated = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def isPromoScreenEnabled(self):
        raise NotImplementedError
        return

    def getFullCrewSound(self):
        raise NotImplementedError
        return

    def commanders(self):
        raise NotImplementedError
        return

    def getCommanderByID(self, commanderID):
        raise NotImplementedError
        return

    def getCertificateTokenName(self):
        raise NotImplementedError
        return

    def exchangeCommander(self, commandersData, callback):
        raise NotImplementedError
        return

    def getCertificateCount(self):
        raise NotImplementedError
        return

    def getExchangedCountByCommanderID(self, commanderID):
        raise NotImplementedError
        return

    def getBlockCardCountByCommanderID(self, commanderID):
        raise NotImplementedError
        return

    def canExchangeCertificateByCommanderID(self, commanderID):
        raise NotImplementedError
        return

    def getRemainLimits(self, commanderID):
        raise NotImplementedError
        return

    def getRemainShopLimits(self, commanderID):
        raise NotImplementedError
        return
