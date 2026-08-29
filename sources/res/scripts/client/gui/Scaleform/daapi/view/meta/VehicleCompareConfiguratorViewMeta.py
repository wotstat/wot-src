from gui.Scaleform.daapi.view.lobby.vehicle_compare.cmp_configurator_base import VehicleCompareConfiguratorBaseView

class VehicleCompareConfiguratorViewMeta(VehicleCompareConfiguratorBaseView):

    def removeDevice(self, slotType, slotIndex):
        self._printOverrideError(b'removeDevice')
        return

    def selectShell(self, shellId, slotIndex):
        self._printOverrideError(b'selectShell')
        return

    def camoSelected(self, selected):
        self._printOverrideError(b'camoSelected')
        return

    def showModules(self):
        self._printOverrideError(b'showModules')
        return

    def toggleTopModules(self, value):
        self._printOverrideError(b'toggleTopModules')
        return

    def skillSelect(self, skillType, slotIndex, selected):
        self._printOverrideError(b'skillSelect')
        return

    def changeCrewLevel(self, crewLevelId):
        self._printOverrideError(b'changeCrewLevel')
        return

    def as_setDevicesDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setDevicesData(data)
        return

    def as_setAmmoS(self, shells):
        if self._isDAAPIInited():
            return self.flashObject.as_setAmmo(shells)
        return

    def as_setSelectedAmmoIndexS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedAmmoIndex(index)
        return

    def as_setCamoS(self, selected):
        if self._isDAAPIInited():
            return self.flashObject.as_setCamo(selected)
        return

    def as_disableCamoS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_disableCamo()
        return

    def as_setSkillsBlockedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSkillsBlocked(value)
        return

    def as_setCrewAttentionIconVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewAttentionIconVisible(value)
        return

    def as_setSkillsS(self, skills):
        if self._isDAAPIInited():
            return self.flashObject.as_setSkills(skills)
        return

    def as_setTopModulesSelectedS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTopModulesSelected(value)
        return

    def as_setCrewLevelIndexS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setCrewLevelIndex(value)
        return

    def as_setIsPostProgressionEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setIsPostProgressionEnabled(value)
        return
