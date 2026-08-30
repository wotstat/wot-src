from enum import Enum
from frameworks.wulf import ViewModel

class ButtonType(Enum):
    INFO = b'Info'
    QUESTION = b'Question'
    VIDEO = b'Video'
    DROP_LIST = b'Drop_List'


class NavigationBarInfoButton(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(NavigationBarInfoButton, self).__init__(properties=properties, commands=commands)
        return

    def getLabel(self):
        return self._getString(0)

    def setLabel(self, value):
        self._setString(0, value)
        return

    def getTooltipHeader(self):
        return self._getString(1)

    def setTooltipHeader(self, value):
        self._setString(1, value)
        return

    def getTooltipBody(self):
        return self._getString(2)

    def setTooltipBody(self, value):
        self._setString(2, value)
        return

    def getType(self):
        return ButtonType(self._getString(3))

    def setType(self, value):
        self._setString(3, value.value)
        return

    def _initialize(self):
        super(NavigationBarInfoButton, self)._initialize()
        self._addStringProperty(b'label', b'')
        self._addStringProperty(b'tooltipHeader', b'')
        self._addStringProperty(b'tooltipBody', b'')
        self._addStringProperty(b'type', ButtonType.INFO.value)
        return
