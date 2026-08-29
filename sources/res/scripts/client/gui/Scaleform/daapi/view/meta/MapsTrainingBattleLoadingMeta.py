from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MapsTrainingBattleLoadingMeta(BaseDAAPIComponent):

    def gotoBattle(self):
        self._printOverrideError(b'gotoBattle')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setDataPageS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDataPage(data)
        return

    def as_updateProgressS(self, percent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateProgress(percent)
        return
