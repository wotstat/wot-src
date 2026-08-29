from frameworks.wulf import ViewModel
from mt_birthday.gui.impl.gen.view_models.views.lobby.birthday.progression import Progression

class EntryPointTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(EntryPointTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def progression(self):
        return self._getViewModel(0)

    @staticmethod
    def getProgressionType():
        return Progression

    def getCurrencyCount(self):
        return self._getNumber(1)

    def setCurrencyCount(self, value):
        self._setNumber(1, value)
        return

    def getIsPaused(self):
        return self._getBool(2)

    def setIsPaused(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(EntryPointTooltipModel, self)._initialize()
        self._addViewModelProperty(b'progression', Progression())
        self._addNumberProperty(b'currencyCount', 0)
        self._addBoolProperty(b'isPaused', False)
        return
