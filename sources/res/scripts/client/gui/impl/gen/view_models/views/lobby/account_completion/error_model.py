from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_overlay_view_model import BaseOverlayViewModel

class ErrorModel(BaseOverlayViewModel):
    __slots__ = (b'onButtonClicked',)

    def __init__(self, properties=5, commands=3):
        super(ErrorModel, self).__init__(properties=properties, commands=commands)
        return

    def getTimer(self):
        return self._getNumber(2)

    def setTimer(self, value):
        self._setNumber(2, value)
        return

    def getMessage(self):
        return self._getString(3)

    def setMessage(self, value):
        self._setString(3, value)
        return

    def getButtonLabel(self):
        return self._getResource(4)

    def setButtonLabel(self, value):
        self._setResource(4, value)
        return

    def _initialize(self):
        super(ErrorModel, self)._initialize()
        self._addNumberProperty(b'timer', 0)
        self._addStringProperty(b'message', b'')
        self._addResourceProperty(b'buttonLabel', R.invalid())
        self.onButtonClicked = self._addCommand(b'onButtonClicked')
        return
