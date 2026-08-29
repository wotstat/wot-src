from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class SecondaryEntryPointMeta(BaseDAAPIComponent):

    def onClick(self):
        self._printOverrideError(b'onClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setCountS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setCount(count)
        return
