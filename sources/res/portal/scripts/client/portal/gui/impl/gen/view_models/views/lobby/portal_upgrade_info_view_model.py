from frameworks.wulf import ViewModel

class PortalUpgradeInfoViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=0, commands=1):
        super(PortalUpgradeInfoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(PortalUpgradeInfoViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        return
