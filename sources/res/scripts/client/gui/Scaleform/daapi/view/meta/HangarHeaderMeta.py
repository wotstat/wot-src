from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class HangarHeaderMeta(BaseDAAPIComponent):

    def onQuestBtnClick(self, questType, questID):
        self._printOverrideError(b'onQuestBtnClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setSecondaryEntryPointVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSecondaryEntryPointVisible(value)
        return

    def as_addEntryPointS(self, alias, registerAlias=None):
        if self._isDAAPIInited():
            return self.flashObject.as_addEntryPoint(alias, registerAlias)
        return

    def as_addSecondaryEntryPointS(self, alias, isRight):
        if self._isDAAPIInited():
            return self.flashObject.as_addSecondaryEntryPoint(alias, isRight)
        return

    def as_setCollectiveGoalEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCollectiveGoalEntryPoint(value)
        return

    def as_setUniversalFlagEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setUniversalFlagEntryPoint(value)
        return

    def as_setArmoryYardEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setArmoryYardEntryPoint(value)
        return

    def as_setEarlyAccessEntryPointS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEarlyAccessEntryPoint(value)
        return
