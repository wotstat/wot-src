from frameworks.wulf import ViewModel

class InfoPageModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(InfoPageModel, self).__init__(properties=properties, commands=commands)
        return

    def getRerollInterval(self):
        return self._getNumber(0)

    def setRerollInterval(self, value):
        self._setNumber(0, value)
        return

    def getIsWeeklySectionAvailable(self):
        return self._getBool(1)

    def setIsWeeklySectionAvailable(self, value):
        self._setBool(1, value)
        return

    def getStandardBlockPlugin(self):
        return self._getString(2)

    def setStandardBlockPlugin(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(InfoPageModel, self)._initialize()
        self._addNumberProperty(b'rerollInterval', 0)
        self._addBoolProperty(b'isWeeklySectionAvailable', False)
        self._addStringProperty(b'standardBlockPlugin', b'')
        self.onClose = self._addCommand(b'onClose')
        return
