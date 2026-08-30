from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank
from frameworks.wulf import Array, ViewModel
from comp7.gui.impl.gen.view_models.views.lobby.progression_division import ProgressionDivision

class ProgressionItemBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(ProgressionItemBaseModel, self).__init__(properties=properties, commands=commands)
        return

    def getRank(self):
        return Rank(self._getNumber(0))

    def setRank(self, value):
        self._setNumber(0, value.value)
        return

    def getFrom(self):
        return self._getNumber(1)

    def setFrom(self, value):
        self._setNumber(1, value)
        return

    def getTo(self):
        return self._getNumber(2)

    def setTo(self, value):
        self._setNumber(2, value)
        return

    def getDivisions(self):
        return self._getArray(3)

    def setDivisions(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getDivisionsType():
        return ProgressionDivision

    def _initialize(self):
        super(ProgressionItemBaseModel, self)._initialize()
        self._addNumberProperty(b'rank')
        self._addNumberProperty(b'from', 0)
        self._addNumberProperty(b'to', 0)
        self._addArrayProperty(b'divisions', Array())
        return
