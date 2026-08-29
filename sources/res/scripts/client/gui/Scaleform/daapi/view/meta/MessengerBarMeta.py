from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent

class MessengerBarMeta(BaseDAAPIComponent):

    def channelButtonClick(self):
        self._printOverrideError(b'channelButtonClick')
        return

    def referralButtonClick(self):
        self._printOverrideError(b'referralButtonClick')
        return

    def sessionStatsButtonClick(self):
        self._printOverrideError(b'sessionStatsButtonClick')
        return

    def as_setInitDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setInitData(data)
        return

    def as_setVehicleCompareCartButtonVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehicleCompareCartButtonVisible(value)
        return

    def as_setReferralProgramButtonVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReferralProgramButtonVisible(value)
        return

    def as_setReferralButtonEnabledS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReferralButtonEnabled(value)
        return

    def as_setReferralBtnCounterS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReferralBtnCounter(value)
        return

    def as_setReferralBtnLimitIndicationS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setReferralBtnLimitIndication(value)
        return

    def as_openVehicleCompareCartPopoverS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_openVehicleCompareCartPopover(value)
        return

    def as_showAddVehicleCompareAnimS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_showAddVehicleCompareAnim(data)
        return

    def as_setSessionStatsButtonVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSessionStatsButtonVisible(value)
        return

    def as_setSessionStatsButtonEnableS(self, value, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setSessionStatsButtonEnable(value, tooltip)
        return

    def as_setSessionStatsButtonSettingsUpdateS(self, show, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setSessionStatsButtonSettingsUpdate(show, value)
        return

    def as_setChannelButtonVisibleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setChannelButtonVisible(value)
        return
