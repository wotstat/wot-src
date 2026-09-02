from frameworks.wulf import ViewModel

class WtHeaderWidgetViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=2, commands=1):
        super(WtHeaderWidgetViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCurrentProgression(self):
        return self._getNumber(0)

    def setCurrentProgression(self, value):
        self._setNumber(0, value)
        return

    def getTotalProgression(self):
        return self._getNumber(1)

    def setTotalProgression(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(WtHeaderWidgetViewModel, self)._initialize()
        self._addNumberProperty(b'currentProgression', 0)
        self._addNumberProperty(b'totalProgression', 0)
        self.onClick = self._addCommand(b'onClick')
        return
