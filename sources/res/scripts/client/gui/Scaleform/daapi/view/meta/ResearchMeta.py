from gui.Scaleform.daapi.view.lobby.techtree.research_view import ResearchView

class ResearchMeta(ResearchView):

    def requestResearchData(self):
        self._printOverrideError(b'requestResearchData')
        return

    def request4Unlock(self, itemCD, topLevel):
        self._printOverrideError(b'request4Unlock')
        return

    def request4Rent(self, itemCD):
        self._printOverrideError(b'request4Rent')
        return

    def goToNextVehicle(self, vehCD):
        self._printOverrideError(b'goToNextVehicle')
        return

    def exitFromResearch(self):
        self._printOverrideError(b'exitFromResearch')
        return

    def goToVehicleView(self, itemCD):
        self._printOverrideError(b'goToVehicleView')
        return

    def compareVehicle(self, itemCD):
        self._printOverrideError(b'compareVehicle')
        return

    def onModuleHover(self, id):
        self._printOverrideError(b'onModuleHover')
        return

    def goToPostProgression(self, itemCD):
        self._printOverrideError(b'goToPostProgression')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setRootDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRootData(data)
        return

    def as_setResearchItemsS(self, nation, raw):
        if self._isDAAPIInited():
            return self.flashObject.as_setResearchItems(nation, raw)
        return

    def as_setFreeXPS(self, freeXP):
        if self._isDAAPIInited():
            return self.flashObject.as_setFreeXP(freeXP)
        return

    def as_setInstalledItemsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInstalledItems(data)
        return

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)
        return

    def as_setXpInfoLinkageS(self, linkage):
        if self._isDAAPIInited():
            return self.flashObject.as_setXpInfoLinkage(linkage)
        return

    def as_setPostProgressionDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPostProgressionData(data)
        return

    def as_showPostProgressionUnlockAnimationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showPostProgressionUnlockAnimation()
        return
