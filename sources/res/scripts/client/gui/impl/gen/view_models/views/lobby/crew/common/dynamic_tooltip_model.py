from frameworks.wulf import ViewModel
from gui.impl.gen import R

class DynamicTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DynamicTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getHeader(self):
        return self._getResource(0)

    def setHeader(self, value):
        self._setResource(0, value)
        return

    def getBody(self):
        return self._getResource(1)

    def setBody(self, value):
        self._setResource(1, value)
        return

    def getContentId(self):
        return self._getNumber(2)

    def setContentId(self, value):
        self._setNumber(2, value)
        return

    def getTargetId(self):
        return self._getNumber(3)

    def setTargetId(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(DynamicTooltipModel, self)._initialize()
        self._addResourceProperty(b'header', R.invalid())
        self._addResourceProperty(b'body', R.invalid())
        self._addNumberProperty(b'contentId', 0)
        self._addNumberProperty(b'targetId', 0)
        return
