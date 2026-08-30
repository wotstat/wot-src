from frameworks.wulf import ViewModel

class SoundModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(SoundModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsVoiceDisabled(self):
        return self._getBool(0)

    def setIsVoiceDisabled(self, value):
        self._setBool(0, value)
        return

    def getIsMutedByUser(self):
        return self._getBool(1)

    def setIsMutedByUser(self, value):
        self._setBool(1, value)
        return

    def getIsSpeaking(self):
        return self._getBool(2)

    def setIsSpeaking(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(SoundModel, self)._initialize()
        self._addBoolProperty(b'isVoiceDisabled', False)
        self._addBoolProperty(b'isMutedByUser', False)
        self._addBoolProperty(b'isSpeaking', False)
        return
