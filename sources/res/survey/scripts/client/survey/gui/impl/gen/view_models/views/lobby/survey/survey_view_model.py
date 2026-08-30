from frameworks.wulf import ViewModel

class SurveyViewModel(ViewModel):
    __slots__ = (b'onAccept', b'onExit')

    def __init__(self, properties=1, commands=2):
        super(SurveyViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getResult(self):
        return self._getNumber(0)

    def setResult(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(SurveyViewModel, self)._initialize()
        self._addNumberProperty(b'result', 0)
        self.onAccept = self._addCommand(b'onAccept')
        self.onExit = self._addCommand(b'onExit')
        return
