from frameworks.wulf import ViewModel

class EventInfoViewModel(ViewModel):
    __slots__ = (b'onInfoVideoClicked',)

    def __init__(self, properties=1, commands=1):
        super(EventInfoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getTitle(self):
        return self._getString(0)

    def setTitle(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(EventInfoViewModel, self)._initialize()
        self._addStringProperty(b'title', b'')
        self.onInfoVideoClicked = self._addCommand(b'onInfoVideoClicked')
        return
