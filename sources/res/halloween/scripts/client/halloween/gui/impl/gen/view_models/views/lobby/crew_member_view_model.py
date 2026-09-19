from enum import Enum
from frameworks.wulf import ViewModel

class CrewStates(Enum):
    RECEIVED = b'received'
    INSHOP = b'inShop'
    INBASEREWARD = b'inBaseReward'


class CrewMemberViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=8, commands=0):
        super(CrewMemberViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getVoiceover(self):
        return self._getString(3)

    def setVoiceover(self, value):
        self._setString(3, value)
        return

    def getHasIsShop(self):
        return self._getBool(4)

    def setHasIsShop(self, value):
        self._setBool(4, value)
        return

    def getHasVoiceover(self):
        return self._getBool(5)

    def setHasVoiceover(self, value):
        self._setBool(5, value)
        return

    def getTooltipId(self):
        return self._getString(6)

    def setTooltipId(self, value):
        self._setString(6, value)
        return

    def getState(self):
        return CrewStates(self._getString(7))

    def setState(self, value):
        self._setString(7, value.value)
        return

    def _initialize(self):
        super(CrewMemberViewModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'icon', b'')
        self._addStringProperty(b'voiceover', b'')
        self._addBoolProperty(b'hasIsShop', False)
        self._addBoolProperty(b'hasVoiceover', False)
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'state')
        return
