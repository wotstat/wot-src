from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class ChallengesFailModel(NotificationBaseModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=2, commands=1):
        super(ChallengesFailModel, self).__init__(properties=properties, commands=commands)
        return

    def getChallengeName(self):
        return self._getString(1)

    def setChallengeName(self, value):
        self._setString(1, value)
        return

    def _initialize(self):
        super(ChallengesFailModel, self)._initialize()
        self._addStringProperty(b'challengeName', b'')
        self.onClick = self._addCommand(b'onClick')
        return
