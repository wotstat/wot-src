from gui.Scaleform.daapi.view.battle.classic.players_panel import PlayersPanel

class WhiteTigerPlayersPanelMeta(PlayersPanel):

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

    def as_setPlasmaForVehiclesS(self, vehID, plasmaValue):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlasmaForVehicles(vehID, plasmaValue)
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

    def as_setIsDestroyedS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsDestroyed(id)
        return

    def as_resetGeneratorCaptureTimerS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_resetGeneratorCaptureTimer(id)
        return

    def as_lockGeneratorS(self, id, value):
        if self._isDAAPIInited():
            return self.flashObject.as_lockGenerator(id, value)
        return

    def as_updateGeneratorDownTimeS(self, id, captureTimeText):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGeneratorDownTime(id, captureTimeText)
        return

    def as_setColorBlindS(self, isColorBlind):
        if self._isDAAPIInited():
            return self.flashObject.as_setColorBlind(isColorBlind)
        return
