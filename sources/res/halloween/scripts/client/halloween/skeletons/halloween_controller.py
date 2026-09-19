from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Any
    from halloween_common.configs.halloween_gsw import GSWModel
    from halloween.gui.game_control.halloween_controller import _HalloweenConfig
    from Event import Event

class IHalloweenController(IGameController):
    onSettingsUpdate = None
    onEventDisabled = None

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

    def isOutroVideoEnabled(self):
        raise NotImplementedError
        return

    def isInfoPageEnabled(self):
        raise NotImplementedError
        return

    def isInfoMetaEnabled(self):
        raise NotImplementedError
        return

    def isAvailable(self):
        raise NotImplementedError
        return

    def getModeSettings(self):
        raise NotImplementedError
        return

    def getHWQuestsCache(self):
        raise NotImplementedError
        return

    def getConfig(self):
        raise NotImplementedError
        return

    @staticmethod
    def getGSWConfig():
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

    def selectVehicle(self, invID):
        raise NotImplementedError
        return

    def hasAccessToVehicle(self, vehTypeCD):
        raise NotImplementedError
        return

    @property
    def remainingEventSeconds(self):
        raise NotImplementedError
        return
