from enum import Enum
from frameworks.wulf import ViewModel

class Types(Enum):
    IMAGE = b'image'
    TEXT = b'text'


class SlotLabelElementModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SlotLabelElementModel, self).__init__(properties=properties, commands=commands)
        return

    def getContent(self):
        return self._getString(0)

    def setContent(self, value):
        self._setString(0, value)
        return

    def getType(self):
        return Types(self._getString(1))

    def setType(self, value):
        self._setString(1, value.value)
        return

    def getStyleJson(self):
        return self._getString(2)

    def setStyleJson(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(SlotLabelElementModel, self)._initialize()
        self._addStringProperty(b'content', b'')
        self._addStringProperty(b'type')
        self._addStringProperty(b'styleJson', b'')
        return
