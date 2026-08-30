from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BattleRoyaleHangarWidgetMeta(BaseDAAPIComponent):

    def onClick(self):
        self._printOverrideError(b'onClick')
        return

    def onChangeServerClick(self):
        self._printOverrideError(b'onChangeServerClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
