from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.panels_common import VehicleMechanicsPanel

class WidgetsPanelMeta(VehicleMechanicsPanel):

    def as_addWidgetS(self, widgetType):
        if self._isDAAPIInited():
            return self.flashObject.as_addWidget(widgetType)
        return

    def as_updateLayoutS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLayout(x, y)
        return

    def as_updateCrosshairTypeS(self, crosshairType):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCrosshairType(crosshairType)
        return

    def as_setVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setVisible(visible)
        return

    def as_isPlayerS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isPlayer(value)
        return

    def as_isReplayS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_isReplay(value)
        return
