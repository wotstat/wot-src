from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import DialogTemplateButtonViewModel

class CustomSoundButtonModel(DialogTemplateButtonViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(CustomSoundButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getSoundClick(self):
        return self._getString(5)

    def setSoundClick(self, value):
        self._setString(5, value)
        return

    def _initialize(self):
        super(CustomSoundButtonModel, self)._initialize()
        self._addStringProperty(b'soundClick', b'')
        return
