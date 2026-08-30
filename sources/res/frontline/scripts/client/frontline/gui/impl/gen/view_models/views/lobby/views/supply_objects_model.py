from enum import Enum
from frameworks.wulf import ViewModel

class SupplyType(Enum):
    NONE = b'none'
    PILLBOX = b'pillbox'
    MORTAR = b'mortar'
    FLAMER = b'flamer'
    AIRSHIP = b'airship'


class SupplyObjectsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SupplyObjectsModel, self).__init__(properties=properties, commands=commands)
        return

    def getPoint(self):
        return self._getString(0)

    def setPoint(self, value):
        self._setString(0, value)
        return

    def getObject(self):
        return SupplyType(self._getString(1))

    def setObject(self, value):
        self._setString(1, value.value)
        return

    def getObjectId(self):
        return self._getNumber(2)

    def setObjectId(self, value):
        self._setNumber(2, value)
        return

    def getIsHintShow(self):
        return self._getBool(3)

    def setIsHintShow(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(SupplyObjectsModel, self)._initialize()
        self._addStringProperty(b'point', b'')
        self._addStringProperty(b'object')
        self._addNumberProperty(b'objectId', 0)
        self._addBoolProperty(b'isHintShow', True)
        return
