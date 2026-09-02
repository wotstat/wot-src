from gui.impl.gen.view_models.views.lobby.comp7.division_info_model import DivisionInfoModel

class LeaderboardNavigationDivisionInfo(DivisionInfoModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(LeaderboardNavigationDivisionInfo, self).__init__(properties=properties, commands=commands)
        return

    def getFirstMemberPosition(self):
        return self._getNumber(6)

    def setFirstMemberPosition(self, value):
        self._setNumber(6, value)
        return

    def getRankId(self):
        return self._getNumber(7)

    def setRankId(self, value):
        self._setNumber(7, value)
        return

    def _initialize(self):
        super(LeaderboardNavigationDivisionInfo, self)._initialize()
        self._addNumberProperty(b'firstMemberPosition', -1)
        self._addNumberProperty(b'rankId', 0)
        return
