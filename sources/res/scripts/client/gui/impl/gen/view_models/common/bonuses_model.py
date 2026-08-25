from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.bonus_model import BonusModel

class BonusesModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BonusesModel, self).__init__(properties=properties, commands=commands)
        return

    def getItems(self):
        return self._getArray(0)

    def setItems(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getItemsType():
        return BonusModel

    def getTitle(self):
        return self._getString(1)

    def setTitle(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(BonusesModel, self)._initialize()
        self._addArrayProperty(b'items', Array())
        self._addStringProperty(b'title', b'')
        return
