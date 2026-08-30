from frameworks.wulf import ViewModel

class BannerViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=1, commands=1):
        super(BannerViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCloseoutTimeStamp(self):
        return self._getNumber(0)

    def setCloseoutTimeStamp(self, value):
        self._setNumber(0, value)
        return

    def _initialize(self):
        super(BannerViewModel, self)._initialize()
        self._addNumberProperty(b'closeoutTimeStamp', 0)
        self.onClick = self._addCommand(b'onClick')
        return
