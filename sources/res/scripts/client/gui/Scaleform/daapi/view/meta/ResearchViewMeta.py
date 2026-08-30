from gui.Scaleform.framework.entities.View import View

class ResearchViewMeta(View):

    def request4Buy(self, itemCD):
        self._printOverrideError(b'request4Buy')
        return

    def request4Info(self, itemCD, rootCD):
        self._printOverrideError(b'request4Info')
        return

    def request4Restore(self, itemCD):
        self._printOverrideError(b'request4Restore')
        return

    def showSystemMessage(self, typeString, message):
        self._printOverrideError(b'showSystemMessage')
        return

    def goToBlueprintView(self, itemCD):
        self._printOverrideError(b'goToBlueprintView')
        return

    def goToNationChangeView(self, itemCD):
        self._printOverrideError(b'goToNationChangeView')
        return

    def goToVehicleCollection(self, nation):
        self._printOverrideError(b'goToVehicleCollection')
        return

    def goToEarlyAccessQuestsView(self):
        self._printOverrideError(b'goToEarlyAccessQuestsView')
        return

    def goToEarlyAccessBuyView(self, itemCD):
        self._printOverrideError(b'goToEarlyAccessBuyView')
        return

    def as_setNodesStatesS(self, primary, data, isRequiredInvalidation=False):
        if self._isDAAPIInited():
            return self.flashObject.as_setNodesStates(primary, data, isRequiredInvalidation)
        return

    def as_setNext2UnlockS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNext2Unlock(data)
        return

    def as_setVehicleTypeXPS(self, xps):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleTypeXP(xps)
        return

    def as_setInventoryItemsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInventoryItems(data)
        return

    def as_setNodeVehCompareDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNodeVehCompareData(data)
        return
