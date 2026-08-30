from enum import Enum
from frameworks.wulf import ViewModel

class LineType(Enum):
    LEFTTORIGHT = b'leftToRight'
    RIGHTTOLEFT = b'rightToLeft'
    TOPTOBOTTOM = b'topToBottom'
    BOTTOMTOTOP = b'bottomToTop'
    LEFTTOBOTTOM = b'leftToBottom'
    BOTTOMTOLEFT = b'bottomToLeft'
    LEFTTOTOP = b'leftToTop'
    TOPTOLEFT = b'topToLeft'
    TOPTORIGHT = b'topToRight'
    RIGHTTOTOP = b'rightToTop'
    RIGHTTOBOTTOM = b'rightToBottom'
    BOTTOMTORIGHT = b'bottomToRight'


class PathModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PathModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getLineType(self):
        return LineType(self._getString(1))

    def setLineType(self, value):
        self._setString(1, value.value)
        return

    def _initialize(self):
        super(PathModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'lineType')
        return
