from gui.Scaleform.daapi.view.lobby.profile.ProfileTechnique import ProfileTechnique

class ProfileTechniquePageMeta(ProfileTechnique):

    def setIsInHangarSelected(self, value):
        self._printOverrideError(b'setIsInHangarSelected')
        return

    def as_setSelectedVehicleIntCDS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setSelectedVehicleIntCD(index)
        return
