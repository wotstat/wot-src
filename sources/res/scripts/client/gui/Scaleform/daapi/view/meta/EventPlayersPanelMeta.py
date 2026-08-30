from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventPlayersPanelMeta(BaseDAAPIComponent):

    def as_setPlayerPanelInfoS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelInfo(data)
        return

    def as_setPlayerPanelHpS(self, vehID, hpMax, hpCurrent):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelHp(vehID, hpMax, hpCurrent)
        return

    def as_setPlayerDeadS(self, vehID):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerDead(vehID)
        return

    def as_setPlayerResurrectS(self, vehID, isResurrect):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerResurrect(vehID, isResurrect)
        return

    def as_setPlayerPanelCountPointsS(self, vehID, count):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayerPanelCountPoints(vehID, count)
        return
