from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class QuestProgressTopViewMeta(BaseDAAPIComponent):

    def onPlaySound(self, soundType):
        self._printOverrideError(b'onPlaySound')
        return

    def as_setVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(isVisible)
        return

    def as_setFlagVisibleS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setFlagVisible(isVisible)
        return

    def as_showContentAnimationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showContentAnimation()
        return
