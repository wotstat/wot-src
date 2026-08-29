from frameworks.wulf import ViewModel

class DailyQuestRerollViewModel(ViewModel):
    __slots__ = (b'onClose', b'onReroll')

    def __init__(self, properties=3, commands=2):
        super(DailyQuestRerollViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAlert(self):
        return self._getBool(0)

    def setIsAlert(self, value):
        self._setBool(0, value)
        return

    def getRerollCooldown(self):
        return self._getNumber(1)

    def setRerollCooldown(self, value):
        self._setNumber(1, value)
        return

    def getIsPremium(self):
        return self._getBool(2)

    def setIsPremium(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(DailyQuestRerollViewModel, self)._initialize()
        self._addBoolProperty(b'isAlert', False)
        self._addNumberProperty(b'rerollCooldown', 0)
        self._addBoolProperty(b'isPremium', False)
        self.onClose = self._addCommand(b'onClose')
        self.onReroll = self._addCommand(b'onReroll')
        return
