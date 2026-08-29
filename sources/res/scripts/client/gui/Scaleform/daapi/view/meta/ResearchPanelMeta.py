from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class ResearchPanelMeta(BaseDAAPIComponent):

    def goToResearch(self):
        self._printOverrideError(b'goToResearch')
        return

    def goToPostProgression(self):
        self._printOverrideError(b'goToPostProgression')
        return

    def addVehToCompare(self):
        self._printOverrideError(b'addVehToCompare')
        return

    def as_updateCurrentVehicleS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCurrentVehicle(data)
        return

    def as_setEarnedXPS(self, earnedXP):
        if self._isDAAPIInited():
            return self.flashObject.as_setEarnedXP(earnedXP)
        return

    def as_setEliteS(self, isElite):
        if self._isDAAPIInited():
            return self.flashObject.as_setElite(isElite)
        return

    def as_setIGRLabelS(self, visible, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIGRLabel(visible, value)
        return

    def as_actionIGRDaysLeftS(self, visible, value):
        if self._isDAAPIInited():
            return self.flashObject.as_actionIGRDaysLeft(visible, value)
        return

    def as_setNavigationEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setNavigationEnabled(value)
        return
