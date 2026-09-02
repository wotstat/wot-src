from enum import Enum
from frameworks.wulf import ViewModel

class PlayerTypeEnum(Enum):
    HUNTER = b'hunter'
    BOSS = b'boss'


class WhiteTigerLoadingViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(WhiteTigerLoadingViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentProgress(self):
        return self._getNumber(0)

    def setCurrentProgress(self, value):
        self._setNumber(0, value)
        return

    def getPlayerType(self):
        return PlayerTypeEnum(self._getString(1))

    def setPlayerType(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(WhiteTigerLoadingViewModel, self)._initialize()
        self._addNumberProperty(b'currentProgress', 0)
        self._addStringProperty(b'playerType', PlayerTypeEnum.HUNTER.value)
        return
