from __future__ import absolute_import
import BigWorld, CGF
from Math import Vector3
import BattleReplay
from helpers import dependency
from skeletons.dynamic_objects_cache import IBattleDynamicObjectsCache
from skeletons.gui.battle_session import IBattleSessionProvider

class Radar(BigWorld.DynamicScriptComponent):
    __dynObjectsCache = dependency.descriptor(IBattleDynamicObjectsCache)
    __sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def onEnterWorld(self, *args):
        return

    def onLeaveWorld(self, *args):
        return

    def set_radarReadinessTime(self, _=None):
        radarCtrl = self.entity.guiSessionProvider.dynamic.radar
        if radarCtrl:
            radarCtrl.updateRadarReadinessTime(self.radarReadinessTime)
        return

    def set_radarReady(self, prev=None):
        radarCtrl = self.entity.guiSessionProvider.dynamic.radar
        if radarCtrl:
            radarCtrl.updateRadarReadiness(self.radarReady)
        return

    def refreshRadar(self):
        self.set_radarReadinessTime()
        self.set_radarReady()
        return

    def activatePatrickEffect(self):
        if BattleReplay.g_replayCtrl.isPlaying and BattleReplay.g_replayCtrl.isTimeWarpInProgress:
            return
        self.__playEffect()
        return

    def __playEffect(self):
        prefabPath = self.__dynObjectsCache.getConfig(self.__sessionProvider.arenaVisitor.getArenaGuiType()).getStPatrickLootEffect().prefabs[0]
        CGF.loadGameObjectIntoHierarchy(prefabPath, self.entity.entityGameObject, Vector3(0))
        return
