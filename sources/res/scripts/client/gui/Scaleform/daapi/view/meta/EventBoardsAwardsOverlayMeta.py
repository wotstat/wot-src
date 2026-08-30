from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventBoardsAwardsOverlayMeta(BaseDAAPIComponent):

    def changeFilter(self, id):
        self._printOverrideError(b'changeFilter')
        return

    def as_setHeaderS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeader(data)
        return

    def as_setVehicleS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicle(data)
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return
