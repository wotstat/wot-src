from frameworks.wulf import ViewModel

class DailyIntroScreenViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=1, commands=1):
        super(DailyIntroScreenViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsDailyQuestsEnabled(self):
        return self._getBool(0)

    def setIsDailyQuestsEnabled(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(DailyIntroScreenViewModel, self)._initialize()
        self._addBoolProperty(b'isDailyQuestsEnabled', False)
        self.onClose = self._addCommand(b'onClose')
        return
