from frameworks.wulf import ViewModel

class WinbackLeaveModePopoverViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=1, commands=1):
        super(WinbackLeaveModePopoverViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBattlesCount(self):
        return self._getNumber(0)

    def setBattlesCount(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(WinbackLeaveModePopoverViewModel, self)._initialize()
        self._addNumberProperty(b'battlesCount', 0)
        self.onClick = self._addCommand(b'onClick')
        return
