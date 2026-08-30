from frameworks.wulf import Array
from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel
from gui.impl.gen.view_models.views.lobby.challenges.bonus_model import BonusModel

class ChallengesMissionCompletedModel(NotificationBaseModel):
    __slots__ = (b'onClick',)

    def __init__(self, properties=3, commands=1):
        super(ChallengesMissionCompletedModel, self).__init__(properties=properties, commands=commands)
        return

    def getMissionID(self):
        return self._getString(1)

    def setMissionID(self, value):
        self._setString(1, value)
        return

    def getRewards(self):
        return self._getArray(2)

    def setRewards(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getRewardsType():
        return BonusModel

    def _initialize(self):
        super(ChallengesMissionCompletedModel, self)._initialize()
        self._addStringProperty(b'missionID', b'')
        self._addArrayProperty(b'rewards', Array())
        self.onClick = self._addCommand(b'onClick')
        return
