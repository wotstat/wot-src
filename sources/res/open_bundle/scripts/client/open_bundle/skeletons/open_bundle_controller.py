from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Dict, List
    from gui.server_events.bonuses import SimpleBonus
    from open_bundle.helpers.server_settings import BundlesConfig, BundleConfig

class IOpenBundleController(IGameController):
    onSettingsChanged = None
    onStatusChanged = None

    @property
    def config(self):
        raise NotImplementedError
        return

    @property
    def bundleIDs(self):
        raise NotImplementedError
        return

    def isEnabled(self, bundleID):
        raise NotImplementedError
        return

    def getBundle(self, bundleID):
        raise NotImplementedError
        return

    def isBundleActive(self, bundleID):
        raise NotImplementedError
        return

    def isAllBundleCellsReceived(self, bundleID):
        raise NotImplementedError
        return

    def getBundleTimeLeft(self, bundleID):
        raise NotImplementedError
        return

    def isRareCell(self, bundleID, cellName):
        raise NotImplementedError
        return

    def isUnicNotificationCell(self, bundleID, cellName):
        raise NotImplementedError
        return

    def getCellBonusInfo(self, bundleID, cellName):
        raise NotImplementedError
        return

    def getReceivedCells(self, bundleID):
        raise NotImplementedError
        return

    def getBonusPriority(self, bonus):
        raise NotImplementedError
        return

    def isBonusVisible(self, bonus):
        raise NotImplementedError
        return

    def isRandomPrb(self):
        raise NotImplementedError
        return

    def selectRandomBattle(self, callback):
        raise NotImplementedError
        return
