from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleMessageListMeta(BaseDAAPIComponent):

    def onRefreshComplete(self):
        self._printOverrideError(b'onRefreshComplete')
        return

    def as_setupListS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setupList(data)
        return

    def as_clearS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_clear()
        return

    def as_refreshS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_refresh()
        return

    def as_showYellowMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showYellowMessage(key, text)
        return

    def as_showRedMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showRedMessage(key, text)
        return

    def as_showPurpleMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showPurpleMessage(key, text)
        return

    def as_showGreenMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showGreenMessage(key, text)
        return

    def as_showGoldMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showGoldMessage(key, text)
        return

    def as_showSelfMessageS(self, key, text):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelfMessage(key, text)
        return
