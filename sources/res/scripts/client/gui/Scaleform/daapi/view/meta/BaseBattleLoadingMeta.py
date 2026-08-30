from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BaseBattleLoadingMeta(BaseDAAPIComponent):

    def as_setProgressS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(value)
        return

    def as_setMapIconS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setMapIcon(source)
        return

    def as_setEventInfoPanelDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setEventInfoPanelData(data)
        return

    def as_setTipS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTip(value)
        return

    def as_setTipTitleS(self, title):
        if self._isDAAPIInited():
            return self.flashObject.as_setTipTitle(title)
        return

    def as_setVisualTipInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisualTipInfo(data)
        return
