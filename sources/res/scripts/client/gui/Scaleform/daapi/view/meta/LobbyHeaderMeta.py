from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class LobbyHeaderMeta(BaseDAAPIComponent):

    def menuItemClick(self, alias):
        self._printOverrideError(b'menuItemClick')
        return

    def showLobbyMenu(self):
        self._printOverrideError(b'showLobbyMenu')
        return

    def showDashboard(self):
        self._printOverrideError(b'showDashboard')
        return

    def showExchangeWindow(self):
        self._printOverrideError(b'showExchangeWindow')
        return

    def showExchangeXPWindow(self):
        self._printOverrideError(b'showExchangeXPWindow')
        return

    def showWotPlusView(self):
        self._printOverrideError(b'showWotPlusView')
        return

    def showPremiumView(self):
        self._printOverrideError(b'showPremiumView')
        return

    def onPremShopClick(self):
        self._printOverrideError(b'onPremShopClick')
        return

    def onReservesClick(self):
        self._printOverrideError(b'onReservesClick')
        return

    def onCrystalClick(self):
        self._printOverrideError(b'onCrystalClick')
        return

    def onPayment(self):
        self._printOverrideError(b'onPayment')
        return

    def movePlatoonPopover(self, popoverCenterX):
        self._printOverrideError(b'movePlatoonPopover')
        return

    def showSquad(self, popoverCenterX):
        self._printOverrideError(b'showSquad')
        return

    def openFullscreenBattleSelector(self):
        self._printOverrideError(b'openFullscreenBattleSelector')
        return

    def closeFullscreenBattleSelector(self):
        self._printOverrideError(b'closeFullscreenBattleSelector')
        return

    def fightClick(self, mapID, actionName):
        self._printOverrideError(b'fightClick')
        return

    def as_setScreenS(self, alias):
        if self._isDAAPIInited():
            return self.flashObject.as_setScreen(alias)
        return

    def as_updateWalletBtnS(self, btnID, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateWalletBtn(btnID, data)
        return

    def as_doDisableNavigationS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_doDisableNavigation()
        return

    def as_doDisableHeaderButtonS(self, btnId, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_doDisableHeaderButton(btnId, isEnabled)
        return

    def as_doSoftDisableHeaderButtonS(self, btnId, isSoftDisable):
        if self._isDAAPIInited():
            return self.flashObject.as_doSoftDisableHeaderButton(btnId, isSoftDisable)
        return

    def as_doDeselectHeaderButtonS(self, alias):
        if self._isDAAPIInited():
            return self.flashObject.as_doDeselectHeaderButton(alias)
        return

    def as_setGoldFishEnabledS(self, isEnabled, playAnimation, tooltip, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setGoldFishEnabled(isEnabled, playAnimation, tooltip, tooltipType)
        return

    def as_updateSquadS(self, isInSquad, tooltip, tooltipType, isEvent, icon, hasPopover, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSquad(isInSquad, tooltip, tooltipType, isEvent, icon, hasPopover, data)
        return

    def as_nameResponseS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_nameResponse(data)
        return

    def as_setBadgeS(self, data, selected):
        if self._isDAAPIInited():
            return self.flashObject.as_setBadge(data, selected)
        return

    def as_setWotPlusDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setWotPlusData(data)
        return

    def as_setPremiumParamsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPremiumParams(data)
        return

    def as_setPremShopDataS(self, iconSrc, premShopText, tooltip, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setPremShopData(iconSrc, premShopText, tooltip, tooltipType)
        return

    def as_updateBattleTypeS(self, battleTypeName, battleTypeIcon, isEnabled, tooltip, tooltipType, battleTypeID, eventBgEnabled, eventAnimEnabled, showLegacySelector, hasNew):
        if self._isDAAPIInited():
            return self.flashObject.as_updateBattleType(battleTypeName, battleTypeIcon, isEnabled, tooltip, tooltipType, battleTypeID, eventBgEnabled, eventAnimEnabled, showLegacySelector, hasNew)
        return

    def as_setServerS(self, name, tooltip, tooltipType):
        if self._isDAAPIInited():
            return self.flashObject.as_setServer(name, tooltip, tooltipType)
        return

    def as_updatePingStatusS(self, pingStatus, isColorBlind):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePingStatus(pingStatus, isColorBlind)
        return

    def as_updateAnonymizedStateS(self, isAnonymized):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAnonymizedState(isAnonymized)
        return

    def as_updateUiEffectsStateS(self, isEnabled):
        if self._isDAAPIInited():
            return self.flashObject.as_updateUiEffectsState(isEnabled)
        return

    def as_setWalletStatusS(self, walletStatus):
        if self._isDAAPIInited():
            return self.flashObject.as_setWalletStatus(walletStatus)
        return

    def as_disableFightButtonS(self, isDisabled):
        if self._isDAAPIInited():
            return self.flashObject.as_disableFightButton(isDisabled)
        return

    def as_setFightButtonS(self, label):
        if self._isDAAPIInited():
            return self.flashObject.as_setFightButton(label)
        return

    def as_setCoolDownForReadyS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCoolDownForReady(value)
        return

    def as_showBubbleTooltipS(self, message, duration):
        if self._isDAAPIInited():
            return self.flashObject.as_showBubbleTooltip(message, duration)
        return

    def as_setFightBtnTooltipS(self, tooltip, isSpecial):
        if self._isDAAPIInited():
            return self.flashObject.as_setFightBtnTooltip(tooltip, isSpecial)
        return

    def as_updateOnlineCounterS(self, clusterStats, tooltip, isAvailable):
        if self._isDAAPIInited():
            return self.flashObject.as_updateOnlineCounter(clusterStats, tooltip, isAvailable)
        return

    def as_initOnlineCounterS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_initOnlineCounter(visible)
        return

    def as_setServerNameS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setServerName(value)
        return

    def as_setHangarMenuDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHangarMenuData(data)
        return

    def as_setButtonCounterS(self, btnAlias, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonCounter(btnAlias, value)
        return

    def as_removeButtonCounterS(self, btnAlias):
        if self._isDAAPIInited():
            return self.flashObject.as_removeButtonCounter(btnAlias)
        return

    def as_setHeaderButtonsS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderButtons(data)
        return

    def as_hideMenuS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_hideMenu(value)
        return

    def as_toggleVisibilityMenuS(self, state):
        if self._isDAAPIInited():
            return self.flashObject.as_toggleVisibilityMenu(state)
        return

    def as_setIsPlatoonDropdownShowingS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsPlatoonDropdownShowing(visible)
        return

    def as_setIsFullscreenBattleSelectorShowingS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsFullscreenBattleSelectorShowing(visible)
        return

    def as_setButtonHighlightS(self, btnAlias, highlightImage):
        if self._isDAAPIInited():
            return self.flashObject.as_setButtonHighlight(btnAlias, highlightImage)
        return
