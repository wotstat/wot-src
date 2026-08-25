from gui.Scaleform.daapi.view.battle.classic.page import ClassicPage

class Comp7BaseBattlePageMeta(ClassicPage):

    def showHelp(self):
        self._printOverrideError(b'showHelp')
        return

    def moveSpace(self, x, y, delta):
        self._printOverrideError(b'moveSpace')
        return

    def notifyCursorOver3dScene(self, isOver3dScene):
        self._printOverrideError(b'notifyCursorOver3dScene')
        return

    def notifyCursorDragging(self, isDragging):
        self._printOverrideError(b'notifyCursorDragging')
        return

    def as_updateVehicleStatusS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateVehicleStatus(data)
        return

    def as_onVehicleSelectionConfirmedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onVehicleSelectionConfirmed()
        return

    def as_onBattleStartedS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_onBattleStarted()
        return

    def as_onPrebattleInputStateLockedS(self, isStateLocked):
        if self._isDAAPIInited():
            return self.flashObject.as_onPrebattleInputStateLocked(isStateLocked)
        return
