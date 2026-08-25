from last_stand.gui.impl.gen.view_models.views.common.base_team_member_model import BaseTeamMemberModel

class EventStatsTeamMemberModel(BaseTeamMemberModel):
    __slots__ = ()

    def __init__(self, properties=17, commands=0):
        super(EventStatsTeamMemberModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsFriendRequestSent(self):
        return self._getBool(11)

    def setIsFriendRequestSent(self, value):
        self._setBool(11, value)
        return

    def getIsInFriendList(self):
        return self._getBool(12)

    def setIsInFriendList(self, value):
        self._setBool(12, value)
        return

    def getIsPlatoonRequestCanMade(self):
        return self._getBool(13)

    def setIsPlatoonRequestCanMade(self, value):
        self._setBool(13, value)
        return

    def getIsPlatoonRequestInSquad(self):
        return self._getBool(14)

    def setIsPlatoonRequestInSquad(self, value):
        self._setBool(14, value)
        return

    def getIsPlatoonRequestSent(self):
        return self._getBool(15)

    def setIsPlatoonRequestSent(self, value):
        self._setBool(15, value)
        return

    def getIsBlacklisted(self):
        return self._getBool(16)

    def setIsBlacklisted(self, value):
        self._setBool(16, value)
        return

    def _initialize(self):
        super(EventStatsTeamMemberModel, self)._initialize()
        self._addBoolProperty(b'isFriendRequestSent', False)
        self._addBoolProperty(b'isInFriendList', False)
        self._addBoolProperty(b'isPlatoonRequestCanMade', True)
        self._addBoolProperty(b'isPlatoonRequestInSquad', True)
        self._addBoolProperty(b'isPlatoonRequestSent', False)
        self._addBoolProperty(b'isBlacklisted', False)
        return
