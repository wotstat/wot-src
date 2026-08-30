from enum import Enum
from gui.impl.gen.view_models.views.lobby.crew.common.button_model import ButtonModel

class ToggleState(Enum):
    ON = b'on'
    OFF = b'off'
    DISABLED = b'disabled'
    HIDDEN = b'hidden'


class ToggleButtonModel(ButtonModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(ToggleButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return ToggleState(self._getString(1))

    def setState(self, value):
        self._setString(1, value.value)
        return

    def getIsDisabled(self):
        return self._getBool(2)

    def setIsDisabled(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(ToggleButtonModel, self)._initialize()
        self._addStringProperty(b'state')
        self._addBoolProperty(b'isDisabled', False)
        return
