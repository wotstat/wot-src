from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from battle_royale.gui.impl.gen.view_models.views.lobby.views.user_model import UserModel

class TeamModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TeamModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getUsers(self):
        return self._getArray(1)

    def setUsers(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getUsersType():
        return UserModel

    def _initialize(self):
        super(TeamModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addArrayProperty(b'users', Array())
        return
