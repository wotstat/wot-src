from frameworks.wulf import ViewModel
from gui.impl.gen import R

class BaseFieldModel(ViewModel):
    __slots__ = (b'onChange', b'onLostFocus')

    def __init__(self, properties=4, commands=2):
        super(BaseFieldModel, self).__init__(properties=properties, commands=commands)
        return

    def getName(self):
        return self._getResource(0)

    def setName(self, value):
        self._setResource(0, value)
        return

    def getValue(self):
        return self._getString(1)

    def setValue(self, value):
        self._setString(1, value)
        return

    def getErrorMessage(self):
        return self._getString(2)

    def setErrorMessage(self, value):
        self._setString(2, value)
        return

    def getPlaceholder(self):
        return self._getString(3)

    def setPlaceholder(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(BaseFieldModel, self)._initialize()
        self._addResourceProperty(b'name', R.invalid())
        self._addStringProperty(b'value', b'')
        self._addStringProperty(b'errorMessage', b'')
        self._addStringProperty(b'placeholder', b'')
        self.onChange = self._addCommand(b'onChange')
        self.onLostFocus = self._addCommand(b'onLostFocus')
        return
