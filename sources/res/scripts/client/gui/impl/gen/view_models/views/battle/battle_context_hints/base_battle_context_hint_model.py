from frameworks.wulf import ViewModel

class BaseBattleContextHintModel(ViewModel):
    __slots__ = (b'onHintClosed',)

    def __init__(self, properties=1, commands=1):
        super(BaseBattleContextHintModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsVisible(self):
        return self._getBool(0)

    def setIsVisible(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(BaseBattleContextHintModel, self)._initialize()
        self._addBoolProperty(b'isVisible', False)
        self.onHintClosed = self._addCommand(b'onHintClosed')
        return
