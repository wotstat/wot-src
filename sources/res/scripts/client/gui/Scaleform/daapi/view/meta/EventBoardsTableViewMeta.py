from gui.Scaleform.framework.entities.View import View

class EventBoardsTableViewMeta(View):

    def closeView(self):
        self._printOverrideError(b'closeView')
        return

    def setMyPlace(self):
        self._printOverrideError(b'setMyPlace')
        return

    def participateStatusClick(self):
        self._printOverrideError(b'participateStatusClick')
        return

    def playerClick(self, id):
        self._printOverrideError(b'playerClick')
        return

    def showNextAward(self, visible):
        self._printOverrideError(b'showNextAward')
        return

    def as_setHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setHeaderData(data)
        return

    def as_setStatusDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusData(data)
        return

    def as_setTableDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTableData(data)
        return

    def as_setTableHeaderDataS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setTableHeaderData(data)
        return

    def as_setBackgroundS(self, source):
        if self._isDAAPIInited():
            return self.flashObject.as_setBackground(source)
        return

    def as_setScrollPosS(self, value, centered):
        if self._isDAAPIInited():
            return self.flashObject.as_setScrollPos(value, centered)
        return

    def as_setMyPlaceVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setMyPlaceVisible(visible)
        return

    def as_setMyPlaceS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setMyPlace(value)
        return

    def as_setMyPlaceTooltipS(self, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setMyPlaceTooltip(tooltip)
        return

    def as_setStatusVisibleS(self, visible):
        if self._isDAAPIInited():
            return self.flashObject.as_setStatusVisible(visible)
        return

    def as_setWaitingS(self, visible, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaiting(visible, message)
        return

    def as_setMaintenanceS(self, visible, message1, message2, buttonLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setMaintenance(visible, message1, message2, buttonLabel)
        return

    def as_setAwardsStripesS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setAwardsStripes(data)
        return

    def as_setEmptyDataS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setEmptyData(value)
        return
