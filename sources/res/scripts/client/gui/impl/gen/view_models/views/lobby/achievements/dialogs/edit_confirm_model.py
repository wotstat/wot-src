from enum import Enum
from frameworks.wulf import ViewModel

class DialogType(Enum):
    AUTO_SELECT_ENABLED = b'autoSelectEnabled'
    AUTO_SELECT_DISABLED = b'autoSelectDisabled'
    ERROR = b'error'


class EditConfirmModel(ViewModel):
    __slots__ = (b'onAccept', b'onCancel', b'onClose')

    def __init__(self, properties=1, commands=3):
        super(EditConfirmModel, self).__init__(properties=properties, commands=commands)
        return

    def getDialogType(self):
        return DialogType(self._getString(0))

    def setDialogType(self, value):
        self._setString(0, value.value)
        return

    def _initialize(self):
        super(EditConfirmModel, self)._initialize()
        self._addStringProperty(b'dialogType')
        self.onAccept = self._addCommand(b'onAccept')
        self.onCancel = self._addCommand(b'onCancel')
        self.onClose = self._addCommand(b'onClose')
        return
