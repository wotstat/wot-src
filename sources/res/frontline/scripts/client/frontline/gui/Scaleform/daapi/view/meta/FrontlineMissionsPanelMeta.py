from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class FrontlineMissionsPanelMeta(BaseDAAPIComponent):

    def as_setPrimaryMissionS(self, messageData):
        if self._isDAAPIInited():
            return self.flashObject.as_setPrimaryMission(messageData)
        return

    def as_setNearestHQS(self, index):
        if self._isDAAPIInited():
            return self.flashObject.as_setNearestHQ(index)
        return

    def as_setMissionDescriptionValueS(self, descValue):
        if self._isDAAPIInited():
            return self.flashObject.as_setMissionDescriptionValue(descValue)
        return
