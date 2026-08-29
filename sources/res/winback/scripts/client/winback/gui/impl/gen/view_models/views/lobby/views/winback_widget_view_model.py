from enum import Enum
from frameworks.wulf import ViewModel

class WinbackState(Enum):
    IN_PROGRESS = b'inProgress'
    COMPLETE = b'complete'
    DISABLE = b'disable'
    LAST_STAGE = b'lastStage'


class WinbackWidgetViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=4, commands=1):
        super(WinbackWidgetViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return WinbackState(self._getString(0))

    def setState(self, value):
        self._setString(0, value.value)
        return

    def getLevel(self):
        return self._getNumber(1)

    def setLevel(self, value):
        self._setNumber(1, value)
        return

    def getSelectableRewardsCount(self):
        return self._getNumber(2)

    def setSelectableRewardsCount(self, value):
        self._setNumber(2, value)
        return

    def getProgressionName(self):
        return self._getString(3)

    def setProgressionName(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(WinbackWidgetViewModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addNumberProperty(b'level', 0)
        self._addNumberProperty(b'selectableRewardsCount', 0)
        self._addStringProperty(b'progressionName', b'')
        self.onClick = self._addCommand(b'onClick')
        return
