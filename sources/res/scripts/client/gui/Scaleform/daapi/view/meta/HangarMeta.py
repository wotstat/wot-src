from gui.Scaleform.framework.entities.View import View

class HangarMeta(View):

    def onEscape(self):
        self._printOverrideError(b'onEscape')
        return

    def showHelpLayout(self):
        self._printOverrideError(b'showHelpLayout')
        return

    def closeHelpLayout(self):
        self._printOverrideError(b'closeHelpLayout')
        return

    def hideTeaser(self):
        self._printOverrideError(b'hideTeaser')
        return

    def onTeaserClick(self):
        self._printOverrideError(b'onTeaserClick')
        return

    def as_setCarouselEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarouselEnabled(value)
        return

    def as_setupAmmunitionPanelS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setupAmmunitionPanel(data)
        return

    def as_setControlsVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setControlsVisible(value)
        return

    def as_setEventTournamentBannerVisibleS(self, alias, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setEventTournamentBannerVisible(alias, isVisible)
        return

    def as_setPrestigeWidgetVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrestigeWidgetVisible(value)
        return

    def as_setVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(value)
        return

    def as_showHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_showHelpLayout()
        return

    def as_closeHelpLayoutS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_closeHelpLayout()
        return

    def as_show3DSceneTooltipS(self, id, args):
        if self._isDAAPIInited():
            return self.flashObject.as_show3DSceneTooltip(id, args)
        return

    def as_hide3DSceneTooltipS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide3DSceneTooltip()
        return

    def as_setCarouselS(self, linkage, alias):
        if self._isDAAPIInited():
            return self.flashObject.as_setCarousel(linkage, alias)
        return

    def as_showTeaserS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showTeaser(data)
        return

    def as_setTeaserTimerS(self, timeLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setTeaserTimer(timeLabel)
        return

    def as_hideTeaserTimerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideTeaserTimer()
        return

    def as_animateHangarViewsS(self, isShow):
        if self._isDAAPIInited():
            return self.flashObject.as_animateHangarViews(isShow)
        return

    def as_updateCarouselEventEntryStateS(self, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCarouselEventEntryState(isVisible)
        return

    def as_updateHangarComponentsS(self, showComponents=None, hideComponents=None):
        if self._isDAAPIInited():
            return self.flashObject.as_updateHangarComponents(showComponents, hideComponents)
        return
