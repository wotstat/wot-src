from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class EventBoardsBattleOverlayMeta(BaseDAAPIComponent):

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setExperienceDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setExperienceData(data)
        return

    def as_setStatisticsDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatisticsData(data)
        return

    def as_setTableHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeaderData(data)
        return

    def as_setTableDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTableData(data)
        return
