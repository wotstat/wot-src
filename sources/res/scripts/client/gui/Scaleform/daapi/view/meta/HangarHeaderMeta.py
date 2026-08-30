from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HangarHeaderMeta(BaseDAAPIComponent):

    def onQuestBtnClick(self, questType, questID):
        self._printOverrideError(b'onQuestBtnClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_addEntryPointS(self, alias):
        if self._isDAAPIInited():
            return self.flashObject.as_addEntryPoint(alias)
        return

    def as_addSecondaryEntryPointS(self, alias, isRight):
        if self._isDAAPIInited():
            return self.flashObject.as_addSecondaryEntryPoint(alias, isRight)
        return
