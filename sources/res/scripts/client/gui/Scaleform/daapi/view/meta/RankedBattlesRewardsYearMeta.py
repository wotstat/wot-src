from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class RankedBattlesRewardsYearMeta(BaseDAAPIComponent):

    def onChooseRewardBtnClick(self):
        self._printOverrideError(b'onChooseRewardBtnClick')
        return

    def as_setDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setData(data)
        return

    def as_setChooseRewardBtnCounterS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChooseRewardBtnCounter(value)
        return
