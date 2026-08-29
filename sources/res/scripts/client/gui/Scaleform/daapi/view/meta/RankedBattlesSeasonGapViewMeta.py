from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesSeasonGapViewMeta(BaseDAAPIComponent):

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setEfficiencyDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setEfficiencyData(data)
        return

    def as_setRatingDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setRatingData(data)
        return
