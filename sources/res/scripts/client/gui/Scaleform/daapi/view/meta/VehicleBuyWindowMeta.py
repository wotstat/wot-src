from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleBuyWindowMeta(AbstractWindowView):

    def submit(self, data):
        self._printOverrideError(b'submit')
        return

    def stateChange(self, data):
        self._printOverrideError(b'stateChange')
        return

    def selectTab(self, tabIndex):
        self._printOverrideError(b'selectTab')
        return

    def onTradeInClearVehicle(self):
        self._printOverrideError(b'onTradeInClearVehicle')
        return

    def as_setGoldS(self, gold):
        if self._isDAAPIInited():
            return self.flashObject.as_setGold(gold)
        return

    def as_setCreditsS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCredits(value)
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_updateTradeOffVehicleS(self, vehicleBuyTradeOffVo):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTradeOffVehicle(vehicleBuyTradeOffVo)
        return

    def as_setTradeInWarningMessagegeS(self, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setTradeInWarningMessagege(message)
        return

    def as_setStateS(self, academyEnabled, schoolEnabled, freeEnabled, submitEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_setState(academyEnabled, schoolEnabled, freeEnabled, submitEnabled)
        return
