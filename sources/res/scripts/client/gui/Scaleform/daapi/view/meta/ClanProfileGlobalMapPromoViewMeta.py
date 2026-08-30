from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ClanProfileGlobalMapPromoViewMeta(BaseDAAPIComponent):

    def showInfo(self):
        self._printOverrideError(b'showInfo')
        return

    def showMap(self):
        self._printOverrideError(b'showMap')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
