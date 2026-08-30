from frameworks.wulf import ViewModel

class PersonalMissionsQuestResetViewModel(ViewModel):
    __slots__ = (b'onConfirm', b'onClose')

    def __init__(self, properties=1, commands=2):
        super(PersonalMissionsQuestResetViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getQuestName(self):
        return self._getString(0)

    def setQuestName(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(PersonalMissionsQuestResetViewModel, self)._initialize()
        self._addStringProperty(b'questName', b'')
        self.onConfirm = self._addCommand(b'onConfirm')
        self.onClose = self._addCommand(b'onClose')
        return
