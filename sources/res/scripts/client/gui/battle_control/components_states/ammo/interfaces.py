from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from gui.battle_control.components_states.ammo.constants import AmmoShootPossibility

class IComponentAmmoState(object):

    def isReloadingBlocked(self):
        raise NotImplementedError
        return

    def canChangeVehicleSetting(self, code):
        raise NotImplementedError
        return

    def canShootValidation(self):
        raise NotImplementedError
        return

    def getShotsAmount(self):
        raise NotImplementedError
        return

    def getShootPossibility(self, currentShells):
        raise NotImplementedError
        return

    def getSpecialReloadMessage(self):
        raise NotImplementedError
        return
