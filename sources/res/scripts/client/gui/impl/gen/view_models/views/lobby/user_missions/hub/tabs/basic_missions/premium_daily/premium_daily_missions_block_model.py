from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.premium_daily.premium_daily_mission_model import PremiumDailyMissionModel

class PremiumDailyMissionsBlockModel(ViewModel):
    __slots__ = (b'onPurchasePremium',)

    def __init__(self, properties=2, commands=1):
        super(PremiumDailyMissionsBlockModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsAvailable(self):
        return self._getBool(0)

    def setIsAvailable(self, value):
        self._setBool(0, value)
        return

    def getMissionsList(self):
        return self._getArray(1)

    def setMissionsList(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getMissionsListType():
        return PremiumDailyMissionModel

    def _initialize(self):
        super(PremiumDailyMissionsBlockModel, self)._initialize()
        self._addBoolProperty(b'isAvailable', False)
        self._addArrayProperty(b'missionsList', Array())
        self.onPurchasePremium = self._addCommand(b'onPurchasePremium')
        return
