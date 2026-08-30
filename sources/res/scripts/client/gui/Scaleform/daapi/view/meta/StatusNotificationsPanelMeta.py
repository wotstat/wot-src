from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class StatusNotificationsPanelMeta(BaseDAAPIComponent):

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setDataS(self, items):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(items)
        return

    def as_setVerticalOffsetS(self, offsetY):
        if self._isDAAPIInited():
            return self.flashObject.as_setVerticalOffset(offsetY)
        return

    def as_setSpeedS(self, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_setSpeed(speed)
        return
