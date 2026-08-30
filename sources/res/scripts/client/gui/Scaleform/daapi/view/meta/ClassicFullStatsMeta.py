from gui.Scaleform.daapi.view.battle.shared.tabbed_full_stats import TabbedFullStatsComponent

class ClassicFullStatsMeta(TabbedFullStatsComponent):

    def onSelectQuest(self, questID):
        self._printOverrideError(b'onSelectQuest')
        return

    def onPersonalReservesTabViewed(self, visible):
        self._printOverrideError(b'onPersonalReservesTabViewed')
        return

    def as_questProgressPerformS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_questProgressPerform(data)
        return

    def as_updateProgressTrackingS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgressTracking(data)
        return
