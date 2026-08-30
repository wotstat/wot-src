from enum import Enum
from frameworks.wulf import ViewModel

class PollViewType(Enum):
    SURVEY = b'survey'
    APPLICATION_FORM = b'application_form'


class PollViewModel(ViewModel):
    __slots__ = (b'onGoToPoll', b'onWindowClose')

    def __init__(self, properties=5, commands=2):
        super(PollViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def getText(self):
        return self._getString(1)

    def setText(self, value):
        self._setString(1, value)
        return

    def getSubmitButtonLbl(self):
        return self._getString(2)

    def setSubmitButtonLbl(self, value):
        self._setString(2, value)
        return

    def getCancelButtonLbl(self):
        return self._getString(3)

    def setCancelButtonLbl(self, value):
        self._setString(3, value)
        return

    def getViewType(self):
        return PollViewType(self._getString(4))

    def setViewType(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(PollViewModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'text', b'')
        self._addStringProperty(b'submitButtonLbl', b'')
        self._addStringProperty(b'cancelButtonLbl', b'')
        self._addStringProperty(b'viewType')
        self.onGoToPoll = self._addCommand(b'onGoToPoll')
        self.onWindowClose = self._addCommand(b'onWindowClose')
        return
