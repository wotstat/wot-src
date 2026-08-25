from frameworks.wulf import Array, Map, ViewModel
from gui.impl.gen import R
from gui.impl.gen.view_models.views.dialogs.mono_dialog_template_button_model import MonoDialogTemplateButtonModel

class MonoDialogTemplateViewModel(ViewModel):
    __slots__ = (b'onAction',)
    ACTION_ESCAPE = b'escape'
    ACTION_CLOSE = b'close'
    ACTION_SPACE = b'space'
    ACTION_CONFIRM = b'confirm'
    ACTION_CANCEL = b'cancel'
    ACTION_SECONDARY = b'secondary'

    def __init__(self, properties=5, commands=1):
        super(MonoDialogTemplateViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getButtons(self):
        return self._getArray(0)

    def setButtons(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getButtonsType():
        return MonoDialogTemplateButtonModel

    def getContent(self):
        return self._getMap(1)

    def setContent(self, value):
        self._setMap(1, value)
        return

    @staticmethod
    def getContentType():
        return (unicode, unicode)

    def getResources(self):
        return self._getMap(2)

    def setResources(self, value):
        self._setMap(2, value)
        return

    @staticmethod
    def getResourcesType():
        return (unicode, unicode)

    def getBackgroundImage(self):
        return self._getResource(3)

    def setBackgroundImage(self, value):
        self._setResource(3, value)
        return

    def getDimmerAlpha(self):
        return self._getReal(4)

    def setDimmerAlpha(self, value):
        self._setReal(4, value)
        return

    def _initialize(self):
        super(MonoDialogTemplateViewModel, self)._initialize()
        self._addArrayProperty(b'buttons', Array())
        self._addMapProperty(b'content', Map(unicode, unicode))
        self._addMapProperty(b'resources', Map(unicode, unicode))
        self._addResourceProperty(b'backgroundImage', R.invalid())
        self._addRealProperty(b'dimmerAlpha', 0.0)
        self.onAction = self._addCommand(b'onAction')
        return
