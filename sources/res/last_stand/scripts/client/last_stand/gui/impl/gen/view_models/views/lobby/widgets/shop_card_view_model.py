from frameworks.wulf import ViewModel

class ShopCardViewModel(ViewModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=0, commands=1):
        super(ShopCardViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(ShopCardViewModel, self)._initialize()
        self.onClick = self._addCommand(b'onClick')
        return
