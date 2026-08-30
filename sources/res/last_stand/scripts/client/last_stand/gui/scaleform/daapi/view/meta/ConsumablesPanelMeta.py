from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel

class ConsumablesPanelMeta(ConsumablesPanel):

    def as_addAbilitySlotS(self, idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addAbilitySlot(idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText)
        return

    def as_updateAbilityS(self, idx, stage, count, timeRemaining, maxTime):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAbility(idx, stage, count, timeRemaining, maxTime)
        return

    def as_updateAbilityCostS(self, idx, cost):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAbilityCost(idx, cost)
        return

    def as_addPassiveAbilitySlotS(self, idx, iconPath, state, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_addPassiveAbilitySlot(idx, iconPath, state, tooltipText)
        return

    def as_updatePassiveAbilityS(self, idx, iconPath, state, tooltipText):
        if self._isDAAPIInited():
            return self.flashObject.as_updatePassiveAbility(idx, iconPath, state, tooltipText)
        return

    def as_resetPassiveAbilitiesS(self, slots=None):
        if self._isDAAPIInited():
            return self.flashObject.as_resetPassiveAbilities(slots)
        return

    def as_setPreparedS(self, idx):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrepared(idx)
        return
