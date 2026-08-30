from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from gui.battle_control.components_states.ammo.constants import AmmoShootPossibility, ActiveAmmoMode, ShellMode

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

    def getAmmoMode(self):
        raise NotImplementedError
        return

    def getShellReloadTimes(self, currShell, shellChangeTime, shells):
        raise NotImplementedError
        return


class IAmmoMode(object):

    def getActiveMode(self):
        raise NotImplementedError
        return

    def getModifiedShells(self):
        raise NotImplementedError
        return

    def getShellMode(self, shellIntCD):
        raise NotImplementedError
        return
