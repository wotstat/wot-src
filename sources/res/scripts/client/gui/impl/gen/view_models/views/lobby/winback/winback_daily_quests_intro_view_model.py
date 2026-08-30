from frameworks.wulf import ViewModel

class WinbackDailyQuestsIntroViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=1, commands=1):
        super(WinbackDailyQuestsIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasBattlePass(self):
        return self._getBool(0)

    def setHasBattlePass(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(WinbackDailyQuestsIntroViewModel, self)._initialize()
        self._addBoolProperty(b'hasBattlePass', False)
        self.onClose = self._addCommand(b'onClose')
        return
