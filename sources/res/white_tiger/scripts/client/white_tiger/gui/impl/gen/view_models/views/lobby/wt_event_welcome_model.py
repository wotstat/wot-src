from frameworks.wulf import ViewModel

class WtEventWelcomeModel(ViewModel):
    __slots__ = (b'onClose', b'onVideo')

    def __init__(self, properties=1, commands=2):
        super(WtEventWelcomeModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsVideoOpened(self):
        return self._getBool(0)

    def setIsVideoOpened(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(WtEventWelcomeModel, self)._initialize()
        self._addBoolProperty(b'isVideoOpened', False)
        self.onClose = self._addCommand(b'onClose')
        self.onVideo = self._addCommand(b'onVideo')
        return
