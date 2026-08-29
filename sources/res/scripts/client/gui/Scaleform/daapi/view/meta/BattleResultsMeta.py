from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class BattleResultsMeta(AbstractWindowView):

    def saveSorting(self, iconType, sortDirection, bonusType):
        self._printOverrideError(b'saveSorting')
        return

    def showEventsWindow(self, questID, eventType):
        self._printOverrideError(b'showEventsWindow')
        return

    def getClanEmblem(self, uid, clanID):
        self._printOverrideError(b'getClanEmblem')
        return

    def onResultsSharingBtnPress(self):
        self._printOverrideError(b'onResultsSharingBtnPress')
        return

    def showUnlockWindow(self, itemId, unlockType):
        self._printOverrideError(b'showUnlockWindow')
        return

    def showProgressiveRewardView(self):
        self._printOverrideError(b'showProgressiveRewardView')
        return

    def onAppliedPremiumBonus(self):
        self._printOverrideError(b'onAppliedPremiumBonus')
        return

    def onShowDetailsPremium(self):
        self._printOverrideError(b'onShowDetailsPremium')
        return

    def showDogTagWindow(self, componentId):
        self._printOverrideError(b'showDogTagWindow')
        return

    def sendGift(self, playerId, stampName):
        self._printOverrideError(b'sendGift')
        return

    def gotoGiftStamps(self):
        self._printOverrideError(b'gotoGiftStamps')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setClanEmblemS(self, uid, iconTag):
        if self._isDAAPIInited():
            return self.flashObject.as_setClanEmblem(uid, iconTag)
        return

    def as_setTeamInfoS(self, uid, iconTag, teamName):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeamInfo(uid, iconTag, teamName)
        return

    def as_setIsInBattleQueueS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsInBattleQueue(value)
        return

    def as_setGiftSystemDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setGiftSystemData(data)
        return
