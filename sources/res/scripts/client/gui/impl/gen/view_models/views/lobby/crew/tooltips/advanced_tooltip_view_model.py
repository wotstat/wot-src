from frameworks.wulf import ViewModel

class AdvancedTooltipViewModel(ViewModel):
    __slots__ = (b'onError',)

    def __init__(self, properties=3, commands=1):
        super(AdvancedTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getMovie(self):
        return self._getString(0)

    def setMovie(self, value):
        self._setString(0, value)
        return

    def getHeader(self):
        return self._getString(1)

    def setHeader(self, value):
        self._setString(1, value)
        return

    def getDescription(self):
        return self._getString(2)

    def setDescription(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(AdvancedTooltipViewModel, self)._initialize()
        self._addStringProperty(b'movie', b'')
        self._addStringProperty(b'header', b'')
        self._addStringProperty(b'description', b'')
        self.onError = self._addCommand(b'onError')
        return
