from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleEndWarningPanelMeta(BaseDAAPIComponent):

    def as_setTotalTimeS(self, minutes, seconds):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalTime(minutes, seconds)
        return

    def as_setTextInfoS(self, text):
        if self._isDAAPIInited():
            return self.flashObject.as_setTextInfo(text)
        return

    def as_setStateS(self, isShow):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(isShow)
        return
