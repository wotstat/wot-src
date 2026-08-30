from gui.Scaleform.daapi.view.lobby.prb_windows.PrebattleWindow import PrebattleWindow

class BattleSessionWindowMeta(PrebattleWindow):

    def requestToAssignMember(self, accId):
        self._printOverrideError(b'requestToAssignMember')
        return

    def requestToUnassignMember(self, accId):
        self._printOverrideError(b'requestToUnassignMember')
        return

    def canMoveToAssigned(self, accId):
        self._printOverrideError(b'canMoveToAssigned')
        return

    def canMoveToUnassigned(self, accId):
        self._printOverrideError(b'canMoveToUnassigned')
        return

    def setSelectedFilter(self, value):
        self._printOverrideError(b'setSelectedFilter')
        return

    def onCantMoveS(self, accId):
        self._printOverrideError(b'onCantMoveS')
        return

    def as_setStartTimeS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setStartTime(value)
        return

    def as_setTotalPlayersCountS(self, value):
        if self._isDAAPIInited():
            return self.flashObject.as_setTotalPlayersCount(value)
        return

    def as_setInfoS(self, isTurnamentBattle, wins, map, firstTeam, secondTeam, count, description, comment, unitLetter, vehicleLevel, teamIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setInfo(isTurnamentBattle, wins, map, firstTeam, secondTeam, count, description, comment, unitLetter, vehicleLevel, teamIndex)
        return

    def as_setWinnerIfDrawS(self, value=0):
        if self._isDAAPIInited():
            return self.flashObject.as_setWinnerIfDraw(value)
        return

    def as_setNationsLimitsS(self, nations):
        if self._isDAAPIInited():
            return self.flashObject.as_setNationsLimits(nations)
        return

    def as_setClassesLimitsS(self, vehicleLevels, classesLimitsAreIdentical):
        if self._isDAAPIInited():
            return self.flashObject.as_setClassesLimits(vehicleLevels, classesLimitsAreIdentical)
        return

    def as_setCommonLimitsS(self, teamLevel, maxPlayers):
        if self._isDAAPIInited():
            return self.flashObject.as_setCommonLimits(teamLevel, maxPlayers)
        return

    def as_setPlayersCountTextS(self, playersCountText):
        if self._isDAAPIInited():
            return self.flashObject.as_setPlayersCountText(playersCountText)
        return

    def as_setFiltersS(self, data, selectedIndex):
        if self._isDAAPIInited():
            return self.flashObject.as_setFilters(data, selectedIndex)
        return
