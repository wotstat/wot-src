from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class DamageInfoPanelMeta(BaseDAAPIComponent):

    def as_showS(self, itemList, showFire, hasMultitrack):
        if self._isDAAPIInited():
            return self.flashObject.as_show(itemList, showFire, hasMultitrack)
        return

    def as_hideS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hide()
        return

    def as_updateEngineS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateEngine(stateId, isHit)
        return

    def as_hideEngineS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideEngine()
        return

    def as_updateAmmoBayS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateAmmoBay(stateId, isHit)
        return

    def as_hideAmmoBayS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideAmmoBay()
        return

    def as_updateFuelTankS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFuelTank(stateId, isHit)
        return

    def as_hideFuelTankS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideFuelTank()
        return

    def as_updateRadioS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateRadio(stateId, isHit)
        return

    def as_hideRadioS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideRadio()
        return

    def as_updateLeftTrackS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateLeftTrack(stateId, isHit)
        return

    def as_updateSecondLeftTrackS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSecondLeftTrack(stateId, isHit)
        return

    def as_hideLeftTrackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideLeftTrack()
        return

    def as_hideSecondLeftTrackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSecondLeftTrack()
        return

    def as_updateRightTrackS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateRightTrack(stateId, isHit)
        return

    def as_updateSecondRightTrackS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSecondRightTrack(stateId, isHit)
        return

    def as_hideRightTrackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideRightTrack()
        return

    def as_hideSecondRightTrackS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSecondRightTrack()
        return

    def as_updateGunS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateGun(stateId, isHit)
        return

    def as_hideGunS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideGun()
        return

    def as_updateTurretRotatorS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateTurretRotator(stateId, isHit)
        return

    def as_hideTurretRotatorS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideTurretRotator()
        return

    def as_updateSurveyingDeviceS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSurveyingDevice(stateId, isHit)
        return

    def as_hideSurveyingDeviceS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSurveyingDevice()
        return

    def as_updateWheelS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateWheel(stateId, isHit)
        return

    def as_hideWheelS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideWheel()
        return

    def as_updateCommanderS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateCommander(stateId, isHit)
        return

    def as_hideCommanderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideCommander()
        return

    def as_updateFirstGunnerS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFirstGunner(stateId, isHit)
        return

    def as_updateSecondGunnerS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSecondGunner(stateId, isHit)
        return

    def as_hideFirstGunnerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideFirstGunner()
        return

    def as_hideSecondGunnerS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSecondGunner()
        return

    def as_updateDriverS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateDriver(stateId, isHit)
        return

    def as_hideDriverS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideDriver()
        return

    def as_updateFirstRadiomanS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFirstRadioman(stateId, isHit)
        return

    def as_updateSecondRadiomanS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSecondRadioman(stateId, isHit)
        return

    def as_hideFirstRadiomanS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideFirstRadioman()
        return

    def as_hideSecondRadiomanS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSecondRadioman()
        return

    def as_updateFirstLoaderS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateFirstLoader(stateId, isHit)
        return

    def as_updateSecondLoaderS(self, stateId, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_updateSecondLoader(stateId, isHit)
        return

    def as_hideFirstLoaderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideFirstLoader()
        return

    def as_hideSecondLoaderS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideSecondLoader()
        return

    def as_showFireS(self, isHit):
        if self._isDAAPIInited():
            return self.flashObject.as_showFire(isHit)
        return

    def as_hideFireS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_hideFire()
        return
