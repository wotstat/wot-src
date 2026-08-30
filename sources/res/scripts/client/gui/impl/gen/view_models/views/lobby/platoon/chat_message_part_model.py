from frameworks.wulf import ViewModel

class ChatMessagePartModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(ChatMessagePartModel, self).__init__(properties=properties, commands=commands)
        return

    def getText(self):
        return self._getString(0)

    def setText(self, value):
        self._setString(0, value)
        return

    def getColor(self):
        return self._getString(1)

    def setColor(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(ChatMessagePartModel, self)._initialize()
        self._addStringProperty(b'text', b'')
        self._addStringProperty(b'color', b'')
        return
