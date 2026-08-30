from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class StanceDanceFightWidgetMeta(VehicleMechanicWidget):

    def as_setProgressS(self, isSwitchingState, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(isSwitchingState, progress)
        return

    def as_energyBoostS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_energyBoost()
        return

    def as_switchTimerS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_switchTimer(value)
        return

    def as_keysVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_keysVisible(value)
        return

    def as_pauseReplayS(self, isPaused):
        if self._isDAAPIInited():
            return self.flashObject.as_pauseReplay(isPaused)
        return
