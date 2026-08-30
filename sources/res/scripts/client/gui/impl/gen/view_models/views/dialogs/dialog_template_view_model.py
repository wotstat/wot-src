from frameworks.wulf import Array, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.dialog_focus_view_model import DialogFocusViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_button_view_model import DialogTemplateButtonViewModel
from gui.impl.gen.view_models.views.dialogs.dialog_template_place_holder_view_model import DialogTemplatePlaceHolderViewModel

class DialogTemplateViewModel(ViewModel):
    __slots__ = (b'onButtonClicked', b'onCloseClicked')
    DEFAULT = b'default'
    ESCAPE = b'escape'

    def __init__(self, properties=6, commands=2):
        super(DialogTemplateViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def focus(self):
        return self._getViewModel(0)

    @staticmethod
    def getFocusType():
        return DialogFocusViewModel

    def getButtons(self):
        return self._getArray(1)

    def setButtons(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getButtonsType():
        return DialogTemplateButtonViewModel

    def getPlaceHolders(self):
        return self._getArray(2)

    def setPlaceHolders(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getPlaceHoldersType():
        return DialogTemplatePlaceHolderViewModel

    def getBackground(self):
        return self._getResource(3)

    def setBackground(self, value):
        self._setResource(3, value)
        return

    def getDimmerAlpha(self):
        return self._getReal(4)

    def setDimmerAlpha(self, value):
        self._setReal(4, value)
        return

    def getDisplayFlags(self):
        return self._getArray(5)

    def setDisplayFlags(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getDisplayFlagsType():
        return unicode

    def _initialize(self):
        super(DialogTemplateViewModel, self)._initialize()
        self._addViewModelProperty(b'focus', DialogFocusViewModel())
        self._addArrayProperty(b'buttons', Array())
        self._addArrayProperty(b'placeHolders', Array())
        self._addResourceProperty(b'background', R.invalid())
        self._addRealProperty(b'dimmerAlpha', 0.0)
        self._addArrayProperty(b'displayFlags', Array())
        self.onButtonClicked = self._addCommand(b'onButtonClicked')
        self.onCloseClicked = self._addCommand(b'onCloseClicked')
        return
