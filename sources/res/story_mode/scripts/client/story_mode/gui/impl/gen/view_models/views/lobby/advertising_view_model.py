from frameworks.wulf import ViewModel

class AdvertisingViewModel(ViewModel):
    __slots__ = (b'onClose', b'onSubmit')

    def __init__(self, properties=0, commands=2):
        super(AdvertisingViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(AdvertisingViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.onSubmit = self._addCommand(b'onSubmit')
        return
