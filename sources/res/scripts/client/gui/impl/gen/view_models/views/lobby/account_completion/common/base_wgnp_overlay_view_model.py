from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.account_completion.common.base_overlay_view_model import BaseOverlayViewModel

class BaseWgnpOverlayViewModel(BaseOverlayViewModel):
    __slots__ = (b'onConfirmClicked', b'onWarningTimer')

    def __init__(self, properties=9, commands=4):
        super(BaseWgnpOverlayViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getResource(2)

    def setTitle(self, value):
        self._setResource(2, value)
        return

    def getSubTitle(self):
        return self._getResource(3)

    def setSubTitle(self, value):
        self._setResource(3, value)
        return

    def getWarningText(self):
        return self._getString(4)

    def setWarningText(self, value):
        self._setString(4, value)
        return

    def getWarningCountdown(self):
        return self._getNumber(5)

    def setWarningCountdown(self, value):
        self._setNumber(5, value)
        return

    def getIsTitleOnly(self):
        return self._getBool(6)

    def setIsTitleOnly(self, value):
        self._setBool(6, value)
        return

    def getIsConfirmEnabled(self):
        return self._getBool(7)

    def setIsConfirmEnabled(self, value):
        self._setBool(7, value)
        return

    def getIsConfirmVisible(self):
        return self._getBool(8)

    def setIsConfirmVisible(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(BaseWgnpOverlayViewModel, self)._initialize()
        self._addResourceProperty(b'title', R.invalid())
        self._addResourceProperty(b'subTitle', R.invalid())
        self._addStringProperty(b'warningText', b'')
        self._addNumberProperty(b'warningCountdown', 0)
        self._addBoolProperty(b'isTitleOnly', False)
        self._addBoolProperty(b'isConfirmEnabled', True)
        self._addBoolProperty(b'isConfirmVisible', True)
        self.onConfirmClicked = self._addCommand(b'onConfirmClicked')
        self.onWarningTimer = self._addCommand(b'onWarningTimer')
        return
