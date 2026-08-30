from gui.Scaleform.daapi.view.meta.WrapperViewMeta import WrapperViewMeta

class BadgesPageMeta(WrapperViewMeta):

    def onBackClick(self):
        self._printOverrideError(b'onBackClick')
        return

    def onSelectBadge(self, badgeID):
        self._printOverrideError(b'onSelectBadge')
        return

    def onDeselectBadge(self):
        self._printOverrideError(b'onDeselectBadge')
        return

    def onSelectSuffixBadge(self, badgeID):
        self._printOverrideError(b'onSelectSuffixBadge')
        return

    def onDeselectSuffixBadge(self):
        self._printOverrideError(b'onDeselectSuffixBadge')
        return

    def onDummyButtonPress(self):
        self._printOverrideError(b'onDummyButtonPress')
        return

    def as_setStaticDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStaticData(data)
        return

    def as_setReceivedBadgesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setReceivedBadges(data)
        return

    def as_setNotReceivedBadgesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNotReceivedBadges(data)
        return

    def as_setSelectedBadgeS(self, data, selected):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedBadge(data, selected)
        return

    def as_setBadgeSuffixS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setBadgeSuffix(data)
        return
