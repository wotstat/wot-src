from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel

class RecruitNewTankmanDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=2):
        super(RecruitNewTankmanDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def getRole(self):
        return self._getString(6)

    def setRole(self, value):
        self._setString(6, value)
        return

    def getVehicleName(self):
        return self._getString(7)

    def setVehicleName(self, value):
        self._setString(7, value)
        return

    def getIsPremium(self):
        return self._getBool(8)

    def setIsPremium(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(RecruitNewTankmanDialogModel, self)._initialize()
        self._addStringProperty(b'role', b'')
        self._addStringProperty(b'vehicleName', b'')
        self._addBoolProperty(b'isPremium', False)
        return
