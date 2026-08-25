from frameworks.wulf import Array, ViewModel
from last_stand.gui.impl.gen.view_models.views.lobby.difficulty_dropdown_item_model import DifficultyDropdownItemModel

class EventDifficultyModel(ViewModel):
    __slots__ = (b'onChange',)

    def __init__(self, properties=3, commands=1):
        super(EventDifficultyModel, self).__init__(properties=properties, commands=commands)
        return

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getItemsType():
        return DifficultyDropdownItemModel

    def getSelected(self):
        return self._getArray(1)

    def setSelected(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSelectedType():
        return unicode

    def getLevel(self):
        return self._getNumber(2)

    def setLevel(self, value):
        self._setNumber(2, value)
        return

    def _initialize(self):
        super(EventDifficultyModel, self)._initialize()
        self._addArrayProperty(b'items', Array())
        self._addArrayProperty(b'selected', Array())
        self._addNumberProperty(b'level', 0)
        self.onChange = self._addCommand(b'onChange')
        return
