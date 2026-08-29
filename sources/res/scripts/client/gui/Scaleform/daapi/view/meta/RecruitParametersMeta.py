from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RecruitParametersMeta(BaseDAAPIComponent):

    def onNationChanged(self, nationID):
        self._printOverrideError(b'onNationChanged')
        return

    def onVehicleClassChanged(self, vehClass):
        self._printOverrideError(b'onVehicleClassChanged')
        return

    def onVehicleChanged(self, vehID):
        self._printOverrideError(b'onVehicleChanged')
        return

    def onTankmanRoleChanged(self, roleID):
        self._printOverrideError(b'onTankmanRoleChanged')
        return

    def setPredefinedTankman(self, tmanParams):
        self._printOverrideError(b'setPredefinedTankman')
        return

    def as_setVehicleClassDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleClassData(data)
        return

    def as_setVehicleDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleData(data)
        return

    def as_setTankmanRoleDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTankmanRoleData(data)
        return

    def as_setNationsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setNationsData(data)
        return
