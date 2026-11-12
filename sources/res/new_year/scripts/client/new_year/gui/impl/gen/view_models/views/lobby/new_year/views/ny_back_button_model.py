from frameworks.wulf import ViewModel

class NyBackButtonModel(ViewModel):
    __slots__ = (b'onBack',)

    def __init__(self, properties=3, commands=1):
        super(NyBackButtonModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsVisible(self):
        return self._getBool(0)

    def setIsVisible(self, value):
        self._setBool(0, value)
        return

    def getCaption(self):
        return self._getString(1)

    def setCaption(self, value):
        self._setString(1, value)
        return

    def getGoTo(self):
        return self._getString(2)

    def setGoTo(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(NyBackButtonModel, self)._initialize()
        self._addBoolProperty(b'isVisible', False)
        self._addStringProperty(b'caption', b'')
        self._addStringProperty(b'goTo', b'')
        self.onBack = self._addCommand(b'onBack')
        return
