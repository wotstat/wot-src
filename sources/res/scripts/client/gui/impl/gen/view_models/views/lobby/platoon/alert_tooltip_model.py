from frameworks.wulf import ViewModel

class AlertTooltipModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(AlertTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    def getHeader(self):
        return self._getString(0)

    def setHeader(self, value):
        self._setString(0, value)
        return

    def getBody(self):
        return self._getString(1)

    def setBody(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(AlertTooltipModel, self)._initialize()
        self._addStringProperty(b'header', b'')
        self._addStringProperty(b'body', b'')
        return
