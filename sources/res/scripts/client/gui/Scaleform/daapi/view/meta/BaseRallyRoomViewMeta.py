from gui.Scaleform.daapi.view.lobby.rally.BaseRallyView import BaseRallyView

class BaseRallyRoomViewMeta(BaseRallyView):

    def assignSlotRequest(self, slotIndex, playerId):
        self._printOverrideError(b'assignSlotRequest')
        return

    def leaveSlotRequest(self, playerId):
        self._printOverrideError(b'leaveSlotRequest')
        return

    def onSlotsHighlihgtingNeed(self, databaseID):
        self._printOverrideError(b'onSlotsHighlihgtingNeed')
        return

    def chooseVehicleRequest(self):
        self._printOverrideError(b'chooseVehicleRequest')
        return

    def inviteFriendRequest(self):
        self._printOverrideError(b'inviteFriendRequest')
        return

    def toggleReadyStateRequest(self):
        self._printOverrideError(b'toggleReadyStateRequest')
        return

    def ignoreUserRequest(self, slotIndex):
        self._printOverrideError(b'ignoreUserRequest')
        return

    def editDescriptionRequest(self, description):
        self._printOverrideError(b'editDescriptionRequest')
        return

    def showFAQWindow(self):
        self._printOverrideError(b'showFAQWindow')
        return

    def as_updateRallyS(self, rally):
        if self._isDAAPIInited():
            return self.flashObject.as_updateRally(rally)
        return

    def as_setMembersS(self, hasRestrictions, slots):
        if self._isDAAPIInited():
            return self.flashObject.as_setMembers(hasRestrictions, slots)
        return

    def as_setMemberStatusS(self, slotIndex, status):
        if self._isDAAPIInited():
            return self.flashObject.as_setMemberStatus(slotIndex, status)
        return

    def as_setMemberOfflineS(self, slotIndex, isOffline):
        if self._isDAAPIInited():
            return self.flashObject.as_setMemberOffline(slotIndex, isOffline)
        return

    def as_setMemberVehicleS(self, slotIdx, slotCost, veh):
        if self._isDAAPIInited():
            return self.flashObject.as_setMemberVehicle(slotIdx, slotCost, veh)
        return

    def as_setActionButtonStateS(self, data):
        if self._isDAAPIInited():
            return self.flashObject.as_setActionButtonState(data)
        return

    def as_setCommentS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setComment(value)
        return

    def as_getCandidatesDPS(self):
        if self._isDAAPIInited():
            return self.flashObject.as_getCandidatesDP()
        return

    def as_highlightSlotsS(self, slotsIdx):
        if self._isDAAPIInited():
            return self.flashObject.as_highlightSlots(slotsIdx)
        return

    def as_setVehiclesTitleS(self, value, tooltip):
        if self._isDAAPIInited():
            return self.flashObject.as_setVehiclesTitle(value, tooltip)
        return
