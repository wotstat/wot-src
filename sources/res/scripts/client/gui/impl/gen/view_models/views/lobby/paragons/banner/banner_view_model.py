from frameworks.wulf import ViewModel

class BannerViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=0, commands=1):
        super(BannerViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(BannerViewModel, self)._initialize()
        self.onClick = self._addCommand(b'onClick')
        return
