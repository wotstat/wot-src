from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class WTBossWidgetMeta(BaseDAAPIComponent):

    def as_setWidgetDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setWidgetData(data)
        return

    def as_updateHpS(self, hpCurrent):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHp(hpCurrent)
        return

    def as_updateKillsS(self, kills):
        if self._isDAAPIInited():
            return self.flashObject.as_updateKills(kills)
        return

    def as_updateGeneratorsS(self, availableCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGenerators(availableCount)
        return

    def as_updateDebuffS(self, totalTime, remainingTime):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDebuff(totalTime, remainingTime)
        return

    def as_updateHyperionChargeS(self, count, maxCount):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHyperionCharge(count, maxCount)
        return

    def as_updateGeneratorsChargingS(self, id, timeLeft, progress, numInvaders, speed):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGeneratorsCharging(id, timeLeft, progress, numInvaders, speed)
        return

    def as_resetGeneratorCaptureTimerS(self, id):
        if self._isDAAPIInited():
            return self.flashObject.as_resetGeneratorCaptureTimer(id)
        return

    def as_setPlasmaBonusS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlasmaBonus(value)
        return
