from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class TweenManagerMeta(BaseDAAPIComponent):

    def createTween(self, tween):
        self._printOverrideError(b'createTween')
        return

    def disposeTween(self, tween):
        self._printOverrideError(b'disposeTween')
        return

    def disposeAll(self):
        self._printOverrideError(b'disposeAll')
        return

    def as_setDataFromXmlS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDataFromXml(data)
        return
