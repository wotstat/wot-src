from frameworks.wulf import Array
from gui.impl.gen.view_models.common.notification_base_model import NotificationBaseModel
from open_bundle.gui.impl.gen.view_models.views.lobby.bonus_model import BonusModel

class SpecialRewardsNotificationModel(NotificationBaseModel):
    __slots__ = (b'onShowReward',)

    def __init__(self, properties=4, commands=1):
        super(SpecialRewardsNotificationModel, self).__init__(properties=properties, commands=commands)
        return

    def getBundleType(self):
        return self._getString(1)

    def setBundleType(self, value):
        self._setString(1, value)
        return

    def getIsButtonDisabled(self):
        return self._getBool(2)

    def setIsButtonDisabled(self, value):
        self._setBool(2, value)
        return

    def getBonuses(self):
        return self._getArray(3)

    def setBonuses(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def _initialize(self):
        super(SpecialRewardsNotificationModel, self)._initialize()
        self._addStringProperty(b'bundleType', b'')
        self._addBoolProperty(b'isButtonDisabled', False)
        self._addArrayProperty(b'bonuses', Array())
        self.onShowReward = self._addCommand(b'onShowReward')
        return
