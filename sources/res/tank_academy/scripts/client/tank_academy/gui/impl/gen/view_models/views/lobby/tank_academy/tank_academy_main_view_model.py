from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from tank_academy.gui.impl.gen.view_models.views.lobby.tank_academy.quest_group_model import QuestGroupModel
from tank_academy.gui.impl.gen.view_models.views.lobby.tank_academy.quest_progress_model import QuestProgressModel

class TankAcademyMainViewModel(ViewModel):
    __slots__ = (b'onShowView', b'onSelectDelayedReward', b'onClose', b'onShowInfoPage', b'onShowQuestTutorial', b'onShowQuestVehicle', b'onUseQuestToken', b'onViewVehicles', b'onSeenAnimation')
    BOX_TOOLTIP_ARG_SHOW_COUNT = b'showCount'
    BOX_TOOLTIP_ARG_QUEST_GROUP_INDEX = b'questGroupIndex'
    BOX_TOOLTIP_ARG_QUEST_INDEX = b'questIndex'
    ARG_SHOW_QUEST_TUTORIAL = b'questNumber'
    ARG_SHOW_QUEST_VEHICLE = b'questNumber'
    ARG_USE_QUEST_TOKEN = b'questNumber'
    ARG_QUEST_ID = b'questID'
    ARG_TOKEN_ID = b'tokenID'

    def __init__(self, properties=4, commands=9):
        super(TankAcademyMainViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def questProgress(self):
        return self._getViewModel(0)

    @staticmethod
    def getQuestProgressType():
        return QuestProgressModel

    def getIsRewardsViewOpen(self):
        return self._getBool(1)

    def setIsRewardsViewOpen(self, value):
        self._setBool(1, value)
        return

    def getQuest_groups(self):
        return self._getArray(2)

    def setQuest_groups(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getQuest_groupsType():
        return QuestGroupModel

    def getUnobtainedVehiclesCount(self):
        return self._getNumber(3)

    def setUnobtainedVehiclesCount(self, value):
        self._setNumber(3, value)
        return

    def _initialize(self):
        super(TankAcademyMainViewModel, self)._initialize()
        self._addViewModelProperty(b'questProgress', QuestProgressModel())
        self._addBoolProperty(b'isRewardsViewOpen', False)
        self._addArrayProperty(b'quest_groups', Array())
        self._addNumberProperty(b'unobtainedVehiclesCount', 0)
        self.onShowView = self._addCommand(b'onShowView')
        self.onSelectDelayedReward = self._addCommand(b'onSelectDelayedReward')
        self.onClose = self._addCommand(b'onClose')
        self.onShowInfoPage = self._addCommand(b'onShowInfoPage')
        self.onShowQuestTutorial = self._addCommand(b'onShowQuestTutorial')
        self.onShowQuestVehicle = self._addCommand(b'onShowQuestVehicle')
        self.onUseQuestToken = self._addCommand(b'onUseQuestToken')
        self.onViewVehicles = self._addCommand(b'onViewVehicles')
        self.onSeenAnimation = self._addCommand(b'onSeenAnimation')
        return
