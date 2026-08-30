from gui.Scaleform.daapi.view.lobby.rally.RallyMainWindowWithSearch import RallyMainWindowWithSearch

class FortBattleRoomWindowMeta(RallyMainWindowWithSearch):

    def onBrowseClanBattles(self):
        self._printOverrideError(b'onBrowseClanBattles')
        return

    def onJoinClanBattle(self, rallyId, slotIndex, peripheryId):
        self._printOverrideError(b'onJoinClanBattle')
        return

    def onCreatedBattleRoom(self, battleID, peripheryId):
        self._printOverrideError(b'onCreatedBattleRoom')
        return

    def refresh(self):
        self._printOverrideError(b'refresh')
        return

    def as_setWindowTitleS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setWindowTitle(value)
        return

    def as_setWaitingS(self, visible, message):
        if self._isDAAPIInited():
            return self.flashObject.as_setWaiting(visible, message)
        return

    def as_setInfoS(self, visible, message, buttonLabel):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfo(visible, message, buttonLabel)
        return
