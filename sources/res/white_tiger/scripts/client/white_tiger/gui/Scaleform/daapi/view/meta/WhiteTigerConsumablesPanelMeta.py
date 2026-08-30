from gui.Scaleform.daapi.view.battle.shared.consumables_panel import ConsumablesPanel

class WhiteTigerConsumablesPanelMeta(ConsumablesPanel):

    def as_setChargeProgressS(self, idx, charge, isVisible):
        if self._isDAAPIInited():
            return self.flashObject.as_setChargeProgress(idx, charge, isVisible)
        return

    def as_setSelectedS(self, idx, isSelected):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelected(idx, isSelected)
        return

    def as_setDebuffViewS(self, idx, isDebuffMode):
        if self._isDAAPIInited():
            return self.flashObject.as_setDebuffView(idx, isDebuffMode)
        return

    def as_setInspiredS(self, isInspired):
        if self._isDAAPIInited():
            return self.flashObject.as_setInspired(isInspired)
        return

    def as_addWhiteTigerEquipmentSlotS(self, idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText, animation, tag, stage):
        if self._isDAAPIInited():
            return self.flashObject.as_addWhiteTigerEquipmentSlot(idx, keyCode, sfKeyCode, quantity, timeRemaining, reloadingTime, iconPath, tooltipText, animation, tag, stage)
        return

    def as_setStageS(self, idx, stage):
        if self._isDAAPIInited():
            return self.flashObject.as_setStage(idx, stage)
        return
