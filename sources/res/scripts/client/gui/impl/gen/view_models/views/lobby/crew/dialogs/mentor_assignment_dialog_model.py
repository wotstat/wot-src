from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.mentor_assignment_tankman_model import MentorAssignmentTankmanModel

class MentorAssignmentDialogModel(DialogTemplateViewModel):
    __slots__ = (b'onInputChange',)

    def __init__(self, properties=14, commands=3):
        super(MentorAssignmentDialogModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def sourceTankman(self):
        return self._getViewModel(6)

    @staticmethod
    def getSourceTankmanType():
        return MentorAssignmentTankmanModel

    @property
    def targetTankman(self):
        return self._getViewModel(7)

    @staticmethod
    def getTargetTankmanType():
        return MentorAssignmentTankmanModel

    def getNation(self):
        return self._getString(8)

    def setNation(self, value):
        self._setString(8, value)
        return

    def getXpTransfer(self):
        return self._getReal(9)

    def setXpTransfer(self, value):
        self._setReal(9, value)
        return

    def getXpLose(self):
        return self._getReal(10)

    def setXpLose(self, value):
        self._setReal(10, value)
        return

    def getIsConfirmRequire(self):
        return self._getBool(11)

    def setIsConfirmRequire(self, value):
        self._setBool(11, value)
        return

    def getIsSourceMaxXp(self):
        return self._getBool(12)

    def setIsSourceMaxXp(self, value):
        self._setBool(12, value)
        return

    def getIsTargetMaxXp(self):
        return self._getBool(13)

    def setIsTargetMaxXp(self, value):
        self._setBool(13, value)
        return

    def _initialize(self):
        super(MentorAssignmentDialogModel, self)._initialize()
        self._addViewModelProperty(b'sourceTankman', MentorAssignmentTankmanModel())
        self._addViewModelProperty(b'targetTankman', MentorAssignmentTankmanModel())
        self._addStringProperty(b'nation', b'')
        self._addRealProperty(b'xpTransfer', 0.0)
        self._addRealProperty(b'xpLose', 0.0)
        self._addBoolProperty(b'isConfirmRequire', False)
        self._addBoolProperty(b'isSourceMaxXp', False)
        self._addBoolProperty(b'isTargetMaxXp', False)
        self.onInputChange = self._addCommand(b'onInputChange')
        return
