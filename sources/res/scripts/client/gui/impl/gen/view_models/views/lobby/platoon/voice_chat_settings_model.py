from frameworks.wulf import ViewModel

class VoiceChatSettingsModel(ViewModel):
    __slots__ = (b'switchVoiceChat',)

    def __init__(self, properties=1, commands=1):
        super(VoiceChatSettingsModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsVoiceChatEnabled(self):
        return self._getBool(0)

    def setIsVoiceChatEnabled(self, value):
        self._setBool(0, value)
        return

    def _initialize(self):
        super(VoiceChatSettingsModel, self)._initialize()
        self._addBoolProperty(b'isVoiceChatEnabled', False)
        self.switchVoiceChat = self._addCommand(b'switchVoiceChat')
        return
