from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel

class ChallengesStartModel(NotificationBaseModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=2, commands=1):
        super(ChallengesStartModel, self).__init__(properties=properties, commands=commands)
        return

    def getFirst(self):
        return self._getBool(1)

    def setFirst(self, value):
        self._setBool(1, value)
        return

    def _initialize(self):
        super(ChallengesStartModel, self)._initialize()
        self._addBoolProperty(b'first', False)
        self.onClick = self._addCommand(b'onClick')
        return
