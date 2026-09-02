from gui.Scaleform.daapi.view.battle.classic.players_panel import PlayersPanel

class WTPlayersPanelMeta(PlayersPanel):

    def as_setIsBossS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsBoss(value)
        return

    def as_setBossBotInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBossBotInfo(data)
        return

    def as_updateBossBotHpS(self, vehID, hpMax, hpCurrent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBossBotHp(vehID, hpMax, hpCurrent)
        return

    def as_setBossBotSpottedS(self, vehID, status):
        if self._isDAAPIInited():
            return self.flashObject.as_setBossBotSpotted(vehID, status)
        return

    def as_clearBossBotCampS(self, campId):
        if self._isDAAPIInited():
            return self.flashObject.as_clearBossBotCamp(campId)
        return

    def as_setAllBossBotCampsOfflineS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_setAllBossBotCampsOffline()
        return

    def as_updateCampInfoStatusS(self, campId):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCampInfoStatus(campId)
        return

    def as_updateGeneratorCaptureTimerS(self, id, timeLeft, progress, numInvaders, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGeneratorCaptureTimer(id, timeLeft, progress, numInvaders, speed)
        return

    def as_setIsDestroyedS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsDestroyed(id, value)
        return

    def as_resetGeneratorCaptureTimerS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_resetGeneratorCaptureTimer(id)
        return

    def as_updateGeneratorDownTimeS(self, id, totalTime, remainingTime, captureTimeText):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGeneratorDownTime(id, totalTime, remainingTime, captureTimeText)
        return
