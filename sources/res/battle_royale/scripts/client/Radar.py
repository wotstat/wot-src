import BigWorld

class Radar(BigWorld.DynamicScriptComponent):

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
