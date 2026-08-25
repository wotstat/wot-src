from gui.Scaleform.daapi.view.battle.shared.vehicle_mechanics.mechanic_widgets.vehicle_mechanic_widget import VehicleMechanicWidget

class StagedJetBoostersWidgetMeta(VehicleMechanicWidget):

    def as_setCountS(self, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setCount(count)
        return

    def as_setProgressS(self, progress):
        if self._isDAAPIInited():
            return self.flashObject.as_setProgress(progress)
        return

    def as_updateLayoutS(self, x, y):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLayout(x, y)
        return

    def as_setMovementInfoS(self, direction):
        if self._isDAAPIInited():
            return self.flashObject.as_setMovementInfo(direction)
        return
