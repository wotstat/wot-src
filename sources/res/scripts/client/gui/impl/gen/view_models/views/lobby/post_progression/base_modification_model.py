from frameworks.wulf import ViewModel
from gui.impl.gen import R

class BaseModificationModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(BaseModificationModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getImageResName(self):
        return self._getString(1)

    def setImageResName(self, value):
        self._setString(1, value)
        return

    def getTitleRes(self):
        return self._getResource(2)

    def setTitleRes(self, value):
        self._setResource(2, value)
        return

    def getTooltipContentId(self):
        return self._getNumber(3)

    def setTooltipContentId(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(BaseModificationModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'imageResName', b'')
        self._addResourceProperty(b'titleRes', R.invalid())
        self._addNumberProperty(b'tooltipContentId', 0)
        return
