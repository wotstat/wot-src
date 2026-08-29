from frameworks.wulf import ViewModel

class LearningDataModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(LearningDataModel, self).__init__(properties=properties, commands=commands)
        return

    def getCrewXpAmount(self):
        return self._getNumber(0)

    def setCrewXpAmount(self, value):
        self._setNumber(0, value)
        return

    def getPersonalXpAmount(self):
        return self._getNumber(1)

    def setPersonalXpAmount(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(LearningDataModel, self)._initialize()
        self._addNumberProperty(b'crewXpAmount', 0)
        self._addNumberProperty(b'personalXpAmount', 0)
        return
