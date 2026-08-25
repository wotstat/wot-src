from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.common.user_name_model import UserNameModel

class BattleType(Enum):
    SOLO = b'solo'
    RANDOMPLATOON = b'randomPlatoon'
    PLATOON = b'platoon'


class PlayerBattleTypeStatusModel(ViewModel):
    __slots__ = (b'onInviteToPlatoon',)

    def __init__(self, properties=3, commands=1):
        super(PlayerBattleTypeStatusModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def user(self):
        return self._getViewModel(0)

    @staticmethod
    def getUserType():
        return UserNameModel

    def getBattleType(self):
        return BattleType(self._getString(1))

    def setBattleType(self, value):
        self._setString(1, value.value)
        return

    def getIsPlatoonWindowOpen(self):
        return self._getBool(2)

    def setIsPlatoonWindowOpen(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(PlayerBattleTypeStatusModel, self)._initialize()
        self._addViewModelProperty(b'user', UserNameModel())
        self._addStringProperty(b'battleType')
        self._addBoolProperty(b'isPlatoonWindowOpen', False)
        self.onInviteToPlatoon = self._addCommand(b'onInviteToPlatoon')
        return
