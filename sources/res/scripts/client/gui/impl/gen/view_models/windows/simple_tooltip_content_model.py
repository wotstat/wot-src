from frameworks.wulf import ViewModel

class SimpleTooltipContentModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(SimpleTooltipContentModel, self).__init__(properties=properties, commands=commands)
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

    def getNote(self):
        return self._getString(2)

    def setNote(self, value):
        self._setString(2, value)
        return

    def getAlert(self):
        return self._getString(3)

    def setAlert(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(SimpleTooltipContentModel, self)._initialize()
        self._addStringProperty(b'header', b'')
        self._addStringProperty(b'body', b'')
        self._addStringProperty(b'note', b'')
        self._addStringProperty(b'alert', b'')
        return
