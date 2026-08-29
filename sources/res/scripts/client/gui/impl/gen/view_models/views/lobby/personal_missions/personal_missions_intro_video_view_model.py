from frameworks.wulf import ViewModel

class PersonalMissionsIntroVideoViewModel(ViewModel):
    __slots__ = (b'onClose', b'onError', b'onVideoStarted')

    def __init__(self, properties=1, commands=3):
        super(PersonalMissionsIntroVideoViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsWindowAccessible(self):
        return self._getBool(0)

    def setIsWindowAccessible(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(PersonalMissionsIntroVideoViewModel, self)._initialize()
        self._addBoolProperty(b'isWindowAccessible', True)
        self.onClose = self._addCommand(b'onClose')
        self.onError = self._addCommand(b'onError')
        self.onVideoStarted = self._addCommand(b'onVideoStarted')
        return
