from enum import Enum
from frameworks.wulf import ViewModel

class ScoringTypeEnum(Enum):
    SCAN = b'scan'
    RESEARCH = b'research'
    KILL = b'kill'
    PICKUP = b'pickup'
    RAM = b'ram'
    SHOT = b'shot'
    ABILITYHIT = b'abilityHit'
    ASSIST = b'assist'
    FIRSTBLOOD = b'firstBlood'
    KILLSTREAK = b'killStreak'
    LOOTRESEARCHING = b'lootResearching'
    LOOTRESEARCHINGDONE = b'lootResearchingDone'
    LOOTRESEARCHABLEPICKUP = b'lootResearchablePickUp'


class ScoringModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ScoringModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return ScoringTypeEnum(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getMarsPoints(self):
        return self._getNumber(1)

    def setMarsPoints(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(ScoringModel, self)._initialize()
        self._addStringProperty(b'type', ScoringTypeEnum.SCAN.value)
        self._addNumberProperty(b'marsPoints', 0)
        return
