from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.battle_result.leader_board.user_battle_info_model import UserBattleInfoModel

class RowModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(RowModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def user(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserType():
        return UserBattleInfoModel

    def getPlace(self):
        return self._getNumber(1)

    def setPlace(self, value):
        self._setNumber(1, value)
        return

    def getIsPersonal(self):
        return self._getBool(2)

    def setIsPersonal(self, value):
        self._setBool(2, value)
        return

    def getIsSquadMode(self):
        return self._getBool(3)

    def setIsSquadMode(self, value):
        self._setBool(3, value)
        return

    def getIsLeaver(self):
        return self._getBool(4)

    def setIsLeaver(self, value):
        self._setBool(4, value)
        return

    def getSquadIndex(self):
        return self._getNumber(5)

    def setSquadIndex(self, value):
        self._setNumber(5, value)
        return

    def _initialize(self):
        super(RowModel, self)._initialize()
        self._addViewModelProperty(b'user', UserBattleInfoModel())
        self._addNumberProperty(b'place', 0)
        self._addBoolProperty(b'isPersonal', False)
        self._addBoolProperty(b'isSquadMode', False)
        self._addBoolProperty(b'isLeaver', False)
        self._addNumberProperty(b'squadIndex', 0)
        return
