from gui.Scaleform.framework.entities.View import View

class BattleRoyaleVehicleInfoMeta(View):

    def onClose(self):
        self._printOverrideError(b'onClose')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
