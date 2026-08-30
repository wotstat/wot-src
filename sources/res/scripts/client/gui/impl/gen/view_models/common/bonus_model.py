from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.bonus_value_model import BonusValueModel

class BonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(BonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getLocaleName(self):
        return self._getString(0)

    def setLocaleName(self, value):
        self._setString(0, value)
        return

    def getValues(self):
        return self._getArray(1)

    def setValues(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getValuesType():
        return BonusValueModel

    def _initialize(self):
        super(BonusModel, self)._initialize()
        self._addStringProperty(b'localeName', b'')
        self._addArrayProperty(b'values', Array())
        return
