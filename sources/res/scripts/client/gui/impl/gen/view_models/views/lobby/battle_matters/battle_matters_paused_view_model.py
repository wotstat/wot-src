from frameworks.wulf import ViewModel

class BattleMattersPausedViewModel(ViewModel):
    __slots__ = (b'gotoHangar',)

    def __init__(self, properties=0, commands=1):
        super(BattleMattersPausedViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(BattleMattersPausedViewModel, self)._initialize()
        self.gotoHangar = self._addCommand(b'gotoHangar')
        return
