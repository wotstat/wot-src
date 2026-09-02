from gui.Scaleform.daapi.view.battle.shared.crosshair.container import CrosshairPanelContainer

class WTCrosshairPanelContainerMeta(CrosshairPanelContainer):

    def as_showPlasmaIndicatorS(self, plasmaValue, oldPlasmaValue, plasmaMultiplicatorText):
        if self._isDAAPIInited():
            return self.flashObject.as_showPlasmaIndicator(plasmaValue, oldPlasmaValue, plasmaMultiplicatorText)
        return

    def as_setPlasmaSavedS(self, plasmaValue):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlasmaSaved(plasmaValue)
        return

    def as_showExplosiveShotIndicatorS(self, isActive):
        if self._isDAAPIInited():
            return self.flashObject.as_showExplosiveShotIndicator(isActive)
        return

    def as_showBarrierS(self, isVisible, bindKey):
        if self._isDAAPIInited():
            return self.flashObject.as_showBarrier(isVisible, bindKey)
        return

    def as_showIncreaseDamageS(self, useAnim=True):
        if self._isDAAPIInited():
            return self.flashObject.as_showIncreaseDamage(useAnim)
        return

    def as_hideIncreaseDamageS(self, useAnim=True):
        if self._isDAAPIInited():
            return self.flashObject.as_hideIncreaseDamage(useAnim)
        return

    def as_updateIncreaseDamageS(self, progress, isFail=False, useAnim=True):
        if self._isDAAPIInited():
            return self.flashObject.as_updateIncreaseDamage(progress, isFail, useAnim)
        return

    def as_showReloadBoostS(self, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_showReloadBoost(useAnim)
        return

    def as_hideReloadBoostS(self, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_hideReloadBoost(useAnim)
        return

    def as_updateReloadBoostS(self, progress, isFail=False, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_updateReloadBoost(progress, isFail, useAnim)
        return

    def as_showS(self, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_show(useAnim)
        return

    def as_hideS(self, useAnim=False):
        if self._isDAAPIInited():
            return self.flashObject.as_hide(useAnim)
        return
