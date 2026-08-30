from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.user_missions.hub.tabs.basic_missions.block_status_model import BlockStatusModel

class DailyMissionsSectionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(DailyMissionsSectionModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def dailyMissionsBlockStatus(self):
        return self._getViewModel(0)

    @staticmethod
    def getDailyMissionsBlockStatusType():
        return BlockStatusModel

    @property
    def premiumDailyMissionsBlockStatus(self):
        return self._getViewModel(1)

    @staticmethod
    def getPremiumDailyMissionsBlockStatusType():
        return BlockStatusModel

    @property
    def rewardProgressBlockStatus(self):
        return self._getViewModel(2)

    @staticmethod
    def getRewardProgressBlockStatusType():
        return BlockStatusModel

    def getTargetQuestId(self):
        return self._getString(3)

    def setTargetQuestId(self, value):
        self._setString(3, value)
        return

    def _initialize(self):
        super(DailyMissionsSectionModel, self)._initialize()
        self._addViewModelProperty(b'dailyMissionsBlockStatus', BlockStatusModel())
        self._addViewModelProperty(b'premiumDailyMissionsBlockStatus', BlockStatusModel())
        self._addViewModelProperty(b'rewardProgressBlockStatus', BlockStatusModel())
        self._addStringProperty(b'targetQuestId', b'')
        return
