from frameworks.wulf import ViewModel

class SummerSaleIntroPageViewModel(ViewModel):
    __slots__ = (b'onGoToFeature', b'onClose')

    def __init__(self, properties=0, commands=2):
        super(SummerSaleIntroPageViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(SummerSaleIntroPageViewModel, self)._initialize()
        self.onGoToFeature = self._addCommand(b'onGoToFeature')
        self.onClose = self._addCommand(b'onClose')
        return
