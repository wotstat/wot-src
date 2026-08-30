from enum import Enum
from frameworks.wulf import ViewModel

class TooltipType(Enum):
    BACKPORT = b'backport'
    NORMAL = b'normal'
    ABSENT = b'absent'


class DialogTemplateGenericTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=1, commands=0):
        super(DialogTemplateGenericTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return TooltipType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(DialogTemplateGenericTooltipViewModel, self)._initialize()
        self._addStringProperty(b'type')
        return
