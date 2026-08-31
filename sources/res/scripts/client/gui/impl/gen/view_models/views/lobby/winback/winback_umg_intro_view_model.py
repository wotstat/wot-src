from frameworks.wulf import ViewModel

class WinbackUmgIntroViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=3, commands=1):
        super(WinbackUmgIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasBattlePass(self):
        return self._getBool(0)

    def setHasBattlePass(self, value):
        self._setBool(0, value)
        return

    def getBackgroundPlugin(self):
        return self._getString(1)

    def setBackgroundPlugin(self, value):
        self._setString(1, value)
        return

    def getDailyQuestsPlugin(self):
        return self._getString(2)

    def setDailyQuestsPlugin(self, value):
        self._setString(2, value)
        return

    def _initialize(self):
        super(WinbackUmgIntroViewModel, self)._initialize()
        self._addBoolProperty(b'hasBattlePass', False)
        self._addStringProperty(b'backgroundPlugin', b'')
        self._addStringProperty(b'dailyQuestsPlugin', b'')
        self.onClose = self._addCommand(b'onClose')
        return
