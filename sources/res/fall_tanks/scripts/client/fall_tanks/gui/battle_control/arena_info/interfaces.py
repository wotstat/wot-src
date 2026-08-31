from __future__ import absolute_import
import typing
from gui.battle_control.arena_info.interfaces import IArenaVehiclesController
if typing.TYPE_CHECKING:
    from Event import Event

class IFallTanksVehicleInfo(object):

    @property
    def isFinished(self):
        raise NotImplementedError
        return

    @property
    def isPlayerVehicle(self):
        raise NotImplementedError
        return

    @property
    def isPlayerVehicleInRace(self):
        raise NotImplementedError
        return

    @property
    def checkpoint(self):
        raise NotImplementedError
        return

    @property
    def finishTime(self):
        raise NotImplementedError
        return

    @property
    def frags(self):
        raise NotImplementedError
        return

    @property
    def racePosition(self):
        raise NotImplementedError
        return


class IFallTanksBattleController(IArenaVehiclesController):
    onFallTanksAttachedInfoUpdate = None

    def getFallTanksAttachedVehicleInfo(self):
        raise NotImplementedError
        return

    def getFallTanksPlayerVehicleInfo(self):
        raise NotImplementedError
        return
