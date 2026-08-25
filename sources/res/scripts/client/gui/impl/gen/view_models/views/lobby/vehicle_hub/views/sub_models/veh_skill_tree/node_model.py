from enum import Enum
from frameworks.wulf import Array, ViewModel

class Status(Enum):
    RESEARCHED = b'researched'
    SELECTED = b'selected'
    DEFAULT = b'default'


class Type(Enum):
    MAJOR = b'major'
    SPECIAL = b'special'
    FINAL = b'final'
    COMMON = b'common'
    GHOST = b'ghost'


class NodeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=0):
        super(NodeModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getX(self):
        return self._getNumber(1)

    def setX(self, value):
        self._setNumber(1, value)
        return

    def getY(self):
        return self._getNumber(2)

    def setY(self, value):
        self._setNumber(2, value)
        return

    def getStatus(self):
        return Status(self._getString(3))

    def setStatus(self, value):
        self._setString(3, value.value)
        return

    def getIsHintRequired(self):
        return self._getBool(4)

    def setIsHintRequired(self, value):
        self._setBool(4, value)
        return

    def getType(self):
        return Type(self._getString(5))

    def setType(self, value):
        self._setString(5, value.value)
        return

    def getPrice(self):
        return self._getReal(6)

    def setPrice(self, value):
        self._setReal(6, value)
        return

    def getIconName(self):
        return self._getString(7)

    def setIconName(self, value):
        self._setString(7, value)
        return

    def getLocalizationName(self):
        return self._getString(8)

    def setLocalizationName(self, value):
        self._setString(8, value)
        return

    def getVehicleName(self):
        return self._getString(9)

    def setVehicleName(self, value):
        self._setString(9, value)
        return

    def getCategories(self):
        return self._getArray(10)

    def setCategories(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getCategoriesType():
        return unicode

    def _initialize(self):
        super(NodeModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addNumberProperty(b'x', 0)
        self._addNumberProperty(b'y', 0)
        self._addStringProperty(b'status')
        self._addBoolProperty(b'isHintRequired', False)
        self._addStringProperty(b'type')
        self._addRealProperty(b'price', 0.0)
        self._addStringProperty(b'iconName', b'')
        self._addStringProperty(b'localizationName', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addArrayProperty(b'categories', Array())
        return
