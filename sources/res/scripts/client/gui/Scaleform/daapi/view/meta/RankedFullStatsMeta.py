from gui.Scaleform.daapi.view.battle.shared.tabbed_full_stats import TabbedFullStatsComponent

class RankedFullStatsMeta(TabbedFullStatsComponent):

    def onVoiceChatControlClick(self):
        self._printOverrideError(b'onVoiceChatControlClick')
        return

    def as_setVoiceChatDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatData(data)
        return

    def as_setVoiceChatControlVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatControlVisible(value)
        return

    def as_setVoiceChatControlSelectedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVoiceChatControlSelected(value)
        return
