from gui.impl.gen.view_models.views.dialogs.dialog_template_view_model import DialogTemplateViewModel

class PunishmentDialogModel(DialogTemplateViewModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=2):
        super(PunishmentDialogModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(6)

    def setTitle(self, value):
        self._setString(6, value)
        return

    def getText(self):
        return self._getString(7)

    def setText(self, value):
        self._setString(7, value)
        return

    def getInfoText(self):
        return self._getString(8)

    def setInfoText(self, value):
        self._setString(8, value)
        return

    def _initialize(self):
        super(PunishmentDialogModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self._addStringProperty(b'text', b'')
        self._addStringProperty(b'infoText', b'')
        return
