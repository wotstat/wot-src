from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class BuffNotificationSystemMeta(BaseDAAPIComponent):

    def onFadeOutFinished(self):
        self._printOverrideError(b'onFadeOutFinished')
        return

    def as_showBuffNotificationS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showBuffNotification(data)
        return

    def as_hideBuffNotificationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideBuffNotification()
        return

    def as_cancelFadeOutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_cancelFadeOut()
        return
