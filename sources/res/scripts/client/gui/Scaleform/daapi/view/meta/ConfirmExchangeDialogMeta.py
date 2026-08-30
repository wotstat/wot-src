from gui.Scaleform.framework.entities.abstract.AbstractWindowView import AbstractWindowView

class ConfirmExchangeDialogMeta(AbstractWindowView):

    def exchange(self, goldValue):
        self._printOverrideError(b'exchange')
        return

    def onSelectedAmountChanged(self, goldValue, needItemsValue):
        self._printOverrideError(b'onSelectedAmountChanged')
        return

    def openDiscountInfoPage(self):
        self._printOverrideError(b'openDiscountInfoPage')
        return

    def as_updateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_update(data)
        return

    def as_setExchangeValuesS(self, goldValue, needItemsValue, discountsAmountApplied):
        if self._isDAAPIInited():
            return self.flashObject.as_setExchangeValues(goldValue, needItemsValue, discountsAmountApplied)
        return
