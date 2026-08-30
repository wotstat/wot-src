from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R

class MapsTrainingMinimapPoint(ViewModel):
    __slots__ = ()
    POINT_TYPE_DEFAULT = b'point'
    POINT_TYPE_BASE = b'main'
    POINT_TYPE_ENEMY_BASE = b'enemyBase'

    def __init__(self, properties=8, commands=0):
        super(MapsTrainingMinimapPoint, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getIsLeft(self):
        return self._getBool(1)

    def setIsLeft(self, value):
        self._setBool(1, value)
        return

    def getTextKeys(self):
        return self._getArray(2)

    def setTextKeys(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getTextKeysType():
        return unicode

    def getType(self):
        return self._getString(3)

    def setType(self, value):
        self._setString(3, value)
        return

    def getPositionX(self):
        return self._getNumber(4)

    def setPositionX(self, value):
        self._setNumber(4, value)
        return

    def getPositionY(self):
        return self._getNumber(5)

    def setPositionY(self, value):
        self._setNumber(5, value)
        return

    def getIsShowTooltip(self):
        return self._getBool(6)

    def setIsShowTooltip(self, value):
        self._setBool(6, value)
        return

    def getTooltipImage(self):
        return self._getResource(7)

    def setTooltipImage(self, value):
        self._setResource(7, value)
        return

    def _initialize(self):
        super(MapsTrainingMinimapPoint, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addBoolProperty(b'isLeft', False)
        self._addArrayProperty(b'textKeys', Array())
        self._addStringProperty(b'type', b'')
        self._addNumberProperty(b'positionX', 0)
        self._addNumberProperty(b'positionY', 0)
        self._addBoolProperty(b'isShowTooltip', False)
        self._addResourceProperty(b'tooltipImage', R.invalid())
        return
