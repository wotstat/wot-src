from enum import Enum
from gui.impl.gen import R
from frameworks.wulf import ViewModel

class NoteThemeEnum(Enum):
    WARNING = b'warning'
    TEXTONLY = b'textOnly'
    CONTENT = b'content'
    AUTORELOADTIME = b'autoReloadTime'


class VehicleParamsNote(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(VehicleParamsNote, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getResource(1)

    def setIcon(self, value):
        self._setResource(1, value)
        return

    def getTheme(self):
        return NoteThemeEnum(self._getString(2))

    def setTheme(self, value):
        self._setString(2, value.value)
        return

    def _initialize(self):
        super(VehicleParamsNote, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addResourceProperty(b'icon', R.invalid())
        self._addStringProperty(b'theme')
        return
