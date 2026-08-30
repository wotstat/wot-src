from frameworks.wulf import Array, ViewModel

class BattlePassIntroViewModel(ViewModel):
    __slots__ = (b'onViewLoaded',)

    def __init__(self, properties=1, commands=1):
        super(BattlePassIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSlides(self):
        return self._getArray(0)

    def setSlides(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getSlidesType():
        return unicode

    def _initialize(self):
        super(BattlePassIntroViewModel, self)._initialize()
        self._addArrayProperty(b'slides', Array())
        self.onViewLoaded = self._addCommand(b'onViewLoaded')
        return
