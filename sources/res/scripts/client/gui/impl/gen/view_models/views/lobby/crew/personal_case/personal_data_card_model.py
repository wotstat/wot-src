from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R

class DataCardState(Enum):
    DEFAULT = b'default'
    SELECTED = b'selected'
    DISABLED = b'disabled'


class DataCardType(Enum):
    DOCUMENT = b'document'
    SKIN = b'skin'


class DataCardFilter(Enum):
    DOCUMENT = b'document'
    SUITABLESKIN = b'suitableSkin'


class PersonalDataCardModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=0):
        super(PersonalDataCardModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getNation(self):
        return self._getString(2)

    def setNation(self, value):
        self._setString(2, value)
        return

    def getIcon(self):
        return self._getResource(3)

    def setIcon(self, value):
        self._setResource(3, value)
        return

    def getInventoryCount(self):
        return self._getNumber(4)

    def setInventoryCount(self, value):
        self._setNumber(4, value)
        return

    def getNewAmount(self):
        return self._getNumber(5)

    def setNewAmount(self, value):
        self._setNumber(5, value)
        return

    def getRestrictions(self):
        return self._getArray(6)

    def setRestrictions(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRestrictionsType():
        return unicode

    def getCardState(self):
        return DataCardState(self._getString(7))

    def setCardState(self, value):
        self._setString(7, value.value)
        return

    def getCardType(self):
        return DataCardType(self._getString(8))

    def setCardType(self, value):
        self._setString(8, value.value)
        return

    def _initialize(self):
        super(PersonalDataCardModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'name', b'')
        self._addStringProperty(b'nation', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addNumberProperty(b'inventoryCount', 0)
        self._addNumberProperty(b'newAmount', 0)
        self._addArrayProperty(b'restrictions', Array())
        self._addStringProperty(b'cardState')
        self._addStringProperty(b'cardType')
        return
