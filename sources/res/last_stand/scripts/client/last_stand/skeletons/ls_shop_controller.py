from __future__ import absolute_import
from skeletons.gui.game_control import IGameController

class ILSShopController(IGameController):
    onShopSettingsUpdated = None
    onBundlesUpdated = None

    def isEnabled(self):
        raise NotImplementedError
        return

    def keyBundles(self):
        raise NotImplementedError
        return

    def getBundleByID(self, bundleID):
        raise NotImplementedError
        return

    def getProgressPointsInBundle(self, bundleID):
        raise NotImplementedError
        return

    def purchaseBundle(self, bundleID, int):
        raise NotImplementedError
        return

    def getPurchaseCount(self, bundleID):
        raise NotImplementedError
        return

    def checkIsEnoughBundles(self):
        raise NotImplementedError
        return
