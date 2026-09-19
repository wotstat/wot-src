from frameworks.wulf import Array, ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.widgets.difficulty_item_model import DifficultyItemModel

class DifficultyViewModel(ViewModel):
    __slots__ = (b'onSwichLevel',)

    def __init__(self, properties=2, commands=1):
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

    def _initialize(self):
        super(DifficultyViewModel, self)._initialize()
        self._addArrayProperty(b'difficulties', Array())
        self._addBoolProperty(b'isDisabled', False)
        self.onSwichLevel = self._addCommand(b'onSwichLevel')
        return
