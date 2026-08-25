from enum import IntEnum
from frameworks.wulf import Array, ViewModel
from story_mode.gui.impl.gen.view_models.views.lobby.mission_model import MissionModel
from story_mode.gui.impl.gen.view_models.views.lobby.parallax_model import ParallaxModel
from story_mode.gui.impl.gen.view_models.views.lobby.selected_mission_model import SelectedMissionModel
from story_mode.gui.impl.gen.view_models.views.lobby.task_model import TaskModel

class TabsEnum(IntEnum):
    NEWBIES = 0
    EVENT = 1


class MissionSelectionViewModel(ViewModel):
    __slots__ = (b'onQuit', b'onMissionSelect', b'onLoaded', b'onChangeTab', b'onSelectedMissionTaskUnlocked', b'onAboutClick', b'onNavigate')

    def __init__(self, properties=8, commands=7):
        super(MissionSelectionViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def selectedMission(self):
        return self._getViewModel(0)

    @staticmethod
    def getSelectedMissionType():
        return SelectedMissionModel

    @property
    def parallax(self):
        return self._getViewModel(1)

    @staticmethod
    def getParallaxType():
        return ParallaxModel

    def getSelectedTab(self):
        return TabsEnum(self._getNumber(2))

    def setSelectedTab(self, value):
        self._setNumber(2, value.value)
        return

    def getIsParallaxEnabled(self):
        return self._getBool(3)

    def setIsParallaxEnabled(self, value):
        self._setBool(3, value)
        return

    def getIsTabsVisible(self):
        return self._getBool(4)

    def setIsTabsVisible(self, value):
        self._setBool(4, value)
        return

    def getMissions(self):
        return self._getArray(5)

    def setMissions(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getMissionsType():
        return MissionModel

    def getTasks(self):
        return self._getArray(6)

    def setTasks(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getTasksType():
        return TaskModel

    def getModeId(self):
        return self._getString(7)

    def setModeId(self, value):
        self._setString(7, value)
        return

    def _initialize(self):
        super(MissionSelectionViewModel, self)._initialize()
        self._addViewModelProperty(b'selectedMission', SelectedMissionModel())
        self._addViewModelProperty(b'parallax', ParallaxModel())
        self._addNumberProperty(b'selectedTab')
        self._addBoolProperty(b'isParallaxEnabled', False)
        self._addBoolProperty(b'isTabsVisible', False)
        self._addArrayProperty(b'missions', Array())
        self._addArrayProperty(b'tasks', Array())
        self._addStringProperty(b'modeId', b'')
        self.onQuit = self._addCommand(b'onQuit')
        self.onMissionSelect = self._addCommand(b'onMissionSelect')
        self.onLoaded = self._addCommand(b'onLoaded')
        self.onChangeTab = self._addCommand(b'onChangeTab')
        self.onSelectedMissionTaskUnlocked = self._addCommand(b'onSelectedMissionTaskUnlocked')
        self.onAboutClick = self._addCommand(b'onAboutClick')
        self.onNavigate = self._addCommand(b'onNavigate')
        return
