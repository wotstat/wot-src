from frameworks.wulf import Array
from gui.impl.gen.view_models.common.missions.bonuses.icon_bonus_model import IconBonusModel
from gui.impl.gen.view_models.views.lobby.notifications.notification_model import NotificationModel

class SessionProgressRewardsNotificationViewModel(NotificationModel):
    __slots__ = (b'goToProgression', b'onShown')

    def __init__(self, properties=5, commands=2):
        super(SessionProgressRewardsNotificationViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStep(self):
        return self._getNumber(1)

    def setStep(self, value):
        self._setNumber(1, value)
        return

    def getShowButton(self):
        return self._getBool(2)

    def setShowButton(self, value):
        self._setBool(2, value)
        return

    def getIsDisabled(self):
        return self._getBool(3)

    def setIsDisabled(self, value):
        self._setBool(3, value)
        return

    def getRewards(self):
        return self._getArray(4)

    def setRewards(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getRewardsType():
        return IconBonusModel

    def _initialize(self):
        super(SessionProgressRewardsNotificationViewModel, self)._initialize()
        self._addNumberProperty(b'step', 1)
        self._addBoolProperty(b'showButton', False)
        self._addBoolProperty(b'isDisabled', False)
        self._addArrayProperty(b'rewards', Array())
        self.goToProgression = self._addCommand(b'goToProgression')
        self.onShown = self._addCommand(b'onShown')
        return
