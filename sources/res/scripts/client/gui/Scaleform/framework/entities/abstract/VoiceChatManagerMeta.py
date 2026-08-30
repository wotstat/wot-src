from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class VoiceChatManagerMeta(BaseDAAPIComponent):

    def isPlayerSpeaking(self, accountDBID):
        self._printOverrideError(b'isPlayerSpeaking')
        return

    def isVivox(self):
        self._printOverrideError(b'isVivox')
        return

    def isYY(self):
        self._printOverrideError(b'isYY')
        return

    def isVOIPEnabled(self):
        self._printOverrideError(b'isVOIPEnabled')
        return

    def isVOIPAvailable(self):
        self._printOverrideError(b'isVOIPAvailable')
        return

    def as_onPlayerSpeakS(self, accountDBID, isSpeak, isHimseljoinUnitButtonf):
        if self._isDAAPIInited():
            return self.flashObject.as_onPlayerSpeak(accountDBID, isSpeak, isHimseljoinUnitButtonf)
        return
