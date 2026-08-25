from __future__ import absolute_import
import BigWorld
from debug_utils import LOG_DEBUG_DEV
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

class TeamInfo(BigWorld.Entity):
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onCombatEquipmentUsed(self, vehicleID, equipmentID):
        self.__sessionProvider.shared.equipments.onCombatEquipmentUsed(vehicleID, equipmentID)
        return

    def onEnterWorld(self, prereqs):
        LOG_DEBUG_DEV((b'[TeamInfo] onEnterWorld: team = {}').format(self.teamID))
        BigWorld.player().arena.registerTeamInfo(self)
        return

    def onLeaveWorld(self):
        LOG_DEBUG_DEV((b'[TeamInfo] onLeaveWorld: team = {}').format(self.teamID))
        BigWorld.player().arena.unregisterTeamInfo(self)
        return

    def onDynamicComponentCreated(self, component):
        LOG_DEBUG_DEV(b'Component created', component)
        return

    def showHittingArea(self, equipmentID, hittingPoint, hittingDirection, hittingTime):
        BigWorld.player().showHittingArea(equipmentID, hittingPoint, hittingDirection, hittingTime)
        return
