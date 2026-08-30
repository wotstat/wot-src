from gui.Scaleform.daapi.view.lobby.exchange.BaseExchangeWindow import BaseExchangeWindow

class ExchangeXpWindowMeta(BaseExchangeWindow):

    def getSubmitButtonEnableState(self, selectedXPCount):
        self._printOverrideError(b'getSubmitButtonEnableState')
        return

    def as_vehiclesDataChangedS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_vehiclesDataChanged(data)
        return

    def as_totalExperienceChangedS(self, totalXP):
        if self._isDAAPIInited():
            return self.flashObject.as_totalExperienceChanged(totalXP)
        return

    def as_setWalletStatusS(self, walletStatus, enableSubmitButton):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus, enableSubmitButton)
        return

    def as_setTargetXPS(self, targetXP):
        if self._isDAAPIInited():
            return self.flashObject.as_setTargetXP(targetXP)
        return
