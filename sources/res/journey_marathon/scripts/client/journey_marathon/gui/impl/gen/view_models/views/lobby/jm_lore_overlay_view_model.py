from frameworks.wulf import ViewModel

class JmLoreOverlayViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=1, commands=1):
        super(JmLoreOverlayViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getNodeId(self):
        return self._getString(0)

    def setNodeId(self, value):
        self._setString(0, value)
        return

    def _initialize(self):
        super(JmLoreOverlayViewModel, self)._initialize()
        self._addStringProperty(b'nodeId', b'')
        self.onClose = self._addCommand(b'onClose')
        return
