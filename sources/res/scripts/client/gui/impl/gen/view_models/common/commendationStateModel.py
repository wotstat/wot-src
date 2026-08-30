from enum import Enum
from frameworks.wulf import ViewModel

class CommendationStateEnum(Enum):
    UNAVAILABLE = b'unavailable'
    COMMENDFIRST = b'commendFirst'
    COMMENDBACK = b'commendBack'
    OUTGOINGCOMMENDATION = b'outgoingCommendation'
    MUTUALCOMMENDATION = b'mutualCommendation'


class CommendationStateModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CommendationStateModel, self).__init__(properties=properties, commands=commands)
        return

    def getCommendationState(self):
        return CommendationStateEnum(self._getString(0))

    def setCommendationState(self, value):
        self._setString(0, value.value)
        return

    def getIsNewState(self):
        return self._getBool(1)

    def setIsNewState(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(CommendationStateModel, self)._initialize()
        self._addStringProperty(b'commendationState', CommendationStateEnum.UNAVAILABLE.value)
        self._addBoolProperty(b'isNewState', False)
        return
