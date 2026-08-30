from frameworks.wulf import Array
from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel
from gui.impl.gen.view_models.views.lobby.crew.dialogs.fill_all_perks_dialog_row import FillAllPerksDialogRow

class FillAllPerksDialogModel(DialogTemplateViewModel):
    __slots__ = (b'onChange',)

    def __init__(self, properties=9, commands=3):
        super(FillAllPerksDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def getRows(self):
        return self._getArray(6)

    def setRows(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getRowsType():
        return FillAllPerksDialogRow

    def getAppliedForBarracks(self):
        return self._getBool(7)

    def setAppliedForBarracks(self, value):
        self._setBool(7, value)
        return

    def getAreBarracksEmpty(self):
        return self._getBool(8)

    def setAreBarracksEmpty(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(FillAllPerksDialogModel, self)._initialize()
        self._addArrayProperty(b'rows', Array())
        self._addBoolProperty(b'appliedForBarracks', False)
        self._addBoolProperty(b'areBarracksEmpty', False)
        self.onChange = self._addCommand(b'onChange')
        return
