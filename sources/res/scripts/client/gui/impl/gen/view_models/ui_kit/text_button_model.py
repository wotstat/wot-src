from gui.impl.gen import R
from gui.impl.gen.view_models.ui_kit.button_common_model import ButtonCommonModel

class TextButtonModel(ButtonCommonModel):
    __slots__ = ()

    def __init__(self, properties=9, commands=2):
        super(TextButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getLabelAdditional(self):
        return self._getResource(6)

    def setLabelAdditional(self, value):
        self._setResource(6, value)
        return

    def getLabelAdditionalString(self):
        return self._getString(7)

    def setLabelAdditionalString(self, value):
        self._setString(7, value)
        return

    def getImage(self):
        return self._getResource(8)

    def setImage(self, value):
        self._setResource(8, value)
        return

    def _initialize(self):
        super(TextButtonModel, self)._initialize()
        self._addResourceProperty(b'labelAdditional', R.invalid())
        self._addStringProperty(b'labelAdditionalString', b'')
        self._addResourceProperty(b'image', R.invalid())
        return
