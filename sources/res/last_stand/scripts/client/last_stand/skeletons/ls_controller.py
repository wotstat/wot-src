from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from last_stand.gui.game_control.ls_controller import _LSConfig, _VehiclesConfig
    from Event import Event
    from gui.shared.utils.requesters import RequestCriteria

class ILSController(IGameController):
    onSettingsUpdate = None
    onEventDisabled = None

    @property
    def lootBoxesEvent(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def isBattlesEnabled(self):
        raise NotImplementedError
        return

    def isPromoScreenEnabled(self):
        raise NotImplementedError
        return

    def isIntroVideoEnabled(self):
        raise NotImplementedError
        return

    def isInfoPageEnabled(self):
        raise NotImplementedError
        return

    def isMetaInfoEnabled(self):
        raise NotImplementedError
        return

    def isLootBoxEntryPointEnabled(self):
        raise NotImplementedError
        return

    def isParallaxEnabled(self):
        raise NotImplementedError
        return

    def isHangar3dPointVisible(self):
        raise NotImplementedError
        return

    def isHangar3dPointRewardVisible(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def getModeSettings(self):
        raise NotImplementedError
        return

    def getConfig(self):
        raise NotImplementedError
        return

    def selectBattle(self, *args, **kwargs):
        raise NotImplementedError
        return

    def openHangar(self):
        raise NotImplementedError
        return

    def isEventPrb(self):
        raise NotImplementedError
        return

    def selectRandomMode(self):
        raise NotImplementedError
        return

    def getVehiclesConfig(self):
        raise NotImplementedError
        return

    def getSuitableVehicles(self, criteria=None):
        raise NotImplementedError
        return

    def getVehiclesCriteria(self):
        raise NotImplementedError
        return
