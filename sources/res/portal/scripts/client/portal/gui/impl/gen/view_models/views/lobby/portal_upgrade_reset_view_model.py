from frameworks.wulf import ViewModel

class PortalUpgradeResetViewModel(ViewModel):
    __slots__ = (b'onClose', b'onReset')

    def __init__(self, properties=0, commands=2):
        super(PortalUpgradeResetViewModel, self).__init__(properties=properties, commands=commands)
        return

    def _initialize(self):
        super(PortalUpgradeResetViewModel, self)._initialize()
        self.onClose = self._addCommand(b'onClose')
        self.onReset = self._addCommand(b'onReset')
        return
