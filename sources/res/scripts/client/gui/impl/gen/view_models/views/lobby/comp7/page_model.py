from enum import IntEnum
from frameworks.wulf import ViewModel

class Types(IntEnum):
    PAGE = 0
    MAPS = 1
    SEASONVEHICLES = 2


class PageModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(PageModel, self).__init__(properties=properties, commands=commands)
        return

    def getPageType(self):
        return Types(self._getNumber(0))

    def setPageType(self, value):
        self._setNumber(0, value.value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(PageModel, self)._initialize()
        self._addNumberProperty(b'pageType')
        self._addStringProperty(b'name', b'')
        return
