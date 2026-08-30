from frameworks.wulf import ViewModel

class DialogTemplateParamViewModel(ViewModel):
    __slots__ = (b'onAction', b'onClose')

    def __init__(self, properties=2, commands=2):
        super(DialogTemplateParamViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return self._getString(0)

    def setType(self, value):
        self._setString(0, value)
        return

    def getParams(self):
        return self._getString(1)

    def setParams(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(DialogTemplateParamViewModel, self)._initialize()
        self._addStringProperty(b'type', b'')
        self._addStringProperty(b'params', b'{}')
        self.onAction = self._addCommand(b'onAction')
        self.onClose = self._addCommand(b'onClose')
        return
