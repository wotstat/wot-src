from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.battle_royale.battle_results.leaderboard.group_model import GroupModel

class LeaderboardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LeaderboardModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getGroupList(self):
        return self._getArray(1)

    def setGroupList(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getGroupListType():
        return GroupModel

    def _initialize(self):
        super(LeaderboardModel, self)._initialize()
        self._addStringProperty(b'type', b'solo')
        self._addArrayProperty(b'groupList', Array())
        return
