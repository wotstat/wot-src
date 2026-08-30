from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MissionsVehicleSelectorMeta(BaseDAAPIComponent):

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_showSelectedVehicleS(self, vehData):
        if self._isDAAPIInited():
            return self.flashObject.as_showSelectedVehicle(vehData)
        return

    def as_hideSelectedVehicleS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSelectedVehicle()
        return

    def as_closeS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_close()
        return
