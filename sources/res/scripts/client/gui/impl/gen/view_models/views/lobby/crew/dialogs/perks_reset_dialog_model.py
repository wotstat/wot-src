from gui.impl.gen.view_models.views.lobby.crew.dialogs.tankman_skills_change_base_dialog_model import TankmanSkillsChangeBaseDialogModel

class PerksResetDialogModel(TankmanSkillsChangeBaseDialogModel):
    __slots__ = ()

    def __init__(self, properties=11, commands=2):
        super(PerksResetDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(8)

    def setTitle(self, value):
        self._setString(8, value)
        return

    def getResetGracePeriodLeft(self):
        return self._getNumber(9)

    def setResetGracePeriodLeft(self, value):
        self._setNumber(9, value)
        return

    def getHasFreeFirstReset(self):
        return self._getBool(10)

    def setHasFreeFirstReset(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(PerksResetDialogModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addNumberProperty(b'resetGracePeriodLeft', 0)
        self._addBoolProperty(b'hasFreeFirstReset', False)
        return
