from enum import Enum
from frameworks.wulf import ViewModel
from gui.impl.gen import R

class ButtonType(Enum):
    PRIMARY = b'primary'
    SECONDARY = b'secondary'
    CUSTOM = b'custom'


class MonoDialogTemplateButtonModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(MonoDialogTemplateButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getAction(self):
        return self._getString(0)

    def setAction(self, value):
        self._setString(0, value)
        return

    def getLabel(self):
        return self._getResource(1)

    def setLabel(self, value):
        self._setResource(1, value)
        return

    def getSoundTarget(self):
        return self._getString(2)

    def setSoundTarget(self, value):
        self._setString(2, value)
        return

    def getIsDisabled(self):
        return self._getBool(3)

    def setIsDisabled(self, value):
        self._setBool(3, value)
        return

    def getType(self):
        return ButtonType(self._getString(4))

    def setType(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(MonoDialogTemplateButtonModel, self)._initialize()
        self._addStringProperty(b'action', b'')
        self._addResourceProperty(b'label', R.invalid())
        self._addStringProperty(b'soundTarget', b'')
        self._addBoolProperty(b'isDisabled', False)
        self._addStringProperty(b'type')
        return
