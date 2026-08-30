from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class VehicleSellDialogMeta(AbstractWindowView):

    def setDialogSettings(self, isOpen):
        self._printOverrideError(b'setDialogSettings')
        return

    def sell(self):
        self._printOverrideError(b'sell')
        return

    def setUserInput(self, value):
        self._printOverrideError(b'setUserInput')
        return

    def setCrewDismissal(self, value):
        self._printOverrideError(b'setCrewDismissal')
        return

    def onSelectionChanged(self, itemID, toInventory, currency):
        self._printOverrideError(b'onSelectionChanged')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_visibleControlBlockS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_visibleControlBlock(value)
        return

    def as_enableButtonS(self, value, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_enableButton(value, tooltip)
        return

    def as_setSellEnabledS(self, value, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setSellEnabled(value, message)
        return

    def as_setControlQuestionDataS(self, isGold, value, question):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlQuestionData(isGold, value, question)
        return

    def as_setTotalS(self, common, total):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotal(common, total)
        return

    def as_updateAccountMoneyS(self, currency, value):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAccountMoney(currency, value)
        return
