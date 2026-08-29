from gui.impl.gen.view_models.views.lobby.account_completion.common.base_overlay_view_model import BaseOverlayViewModel

class ContactSupportModel(BaseOverlayViewModel):
    __slots__ = (b'onContactClicked',)

    def __init__(self, properties=3, commands=3):
        super(ContactSupportModel, self).__init__(properties=properties, commands=commands)
        return

    def getMessage(self):
        return self._getString(2)

    def setMessage(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(ContactSupportModel, self)._initialize()
        self._addStringProperty(b'message', b'')
        self.onContactClicked = self._addCommand(b'onContactClicked')
        return
