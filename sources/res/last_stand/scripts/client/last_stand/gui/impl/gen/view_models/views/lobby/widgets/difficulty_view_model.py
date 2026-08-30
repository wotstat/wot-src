from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel

class DifficultyViewModel(ViewModel):
    __slots__ = (b'onSwitchLevel',)

    def __init__(self, properties=3, commands=1):
        super(DifficultyViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getDifficulties(self):
        return self._getArray(0)

    def setDifficulties(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getDifficultiesType():
        return DifficultyItemModel

    def getIsDisabled(self):
        return self._getBool(1)

    def setIsDisabled(self, value):
        self._setBool(1, value)
        return

    def getIsSearchingPlatoon(self):
        return self._getBool(2)

    def setIsSearchingPlatoon(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(DifficultyViewModel, self)._initialize()
        self._addArrayProperty(b'difficulties', Array())
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'isSearchingPlatoon', False)
        self.onSwitchLevel = self._addCommand(b'onSwitchLevel')
        return
