from enum import IntEnum
from frameworks.wulf import ViewModel
from new_year.gui.impl.gen.view_models.common.region_model import RegionModel
from new_year.gui.impl.gen.view_models.views.lobby.new_year.components.video_cover_model import VideoCoverModel

class Tabs(IntEnum):
    DEFAULT = 0
    QUESTS = 1
    LEADERBOARD = 6


class NewYearInfoViewModel(ViewModel):
    __slots__ = (b'onButtonClick',)
    LEVELS = b'levels'
    STYLES = b'styles'
    SMALLBOXES = b'smallBoxes'
    BIGBOXES = b'bigBoxes'
    GUARANTEED_REWARDS = b'guaranteedRewards'
    STREAM_BOX = b'streamBox'
    PET = b'pet'
    SURPRISE_MACHINE = b'surprise_machine'
    QUESTS = b'quests'
    REWARDS = b'rewards'
    LEADERS = b'leaders'
    LEADERS_RULES = b'leaders_rules'

    def __init__(self, properties=15, commands=1):
        super(NewYearInfoViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def videoCover(self):
        return self._getViewModel(0)

    @staticmethod
    def getVideoCoverType():
        return VideoCoverModel

    @property
    def region(self):
        return self._getViewModel(1)

    @staticmethod
    def getRegionType():
        return RegionModel

    def getStartTab(self):
        return Tabs(self._getNumber(2))

    def setStartTab(self, value):
        self._setNumber(2, value.value)
        return

    def getStartDate(self):
        return self._getNumber(3)

    def setStartDate(self, value):
        self._setNumber(3, value)
        return

    def getEndDate(self):
        return self._getNumber(4)

    def setEndDate(self, value):
        self._setNumber(4, value)
        return

    def getMaxBonus(self):
        return self._getReal(5)

    def setMaxBonus(self, value):
        self._setReal(5, value)
        return

    def getUsualMaxBonus(self):
        return self._getReal(6)

    def setUsualMaxBonus(self, value):
        self._setReal(6, value)
        return

    def getQuestsToGetExtraSlot(self):
        return self._getNumber(7)

    def setQuestsToGetExtraSlot(self, value):
        self._setNumber(7, value)
        return

    def getMinMultiplier(self):
        return self._getReal(8)

    def setMinMultiplier(self, value):
        self._setReal(8, value)
        return

    def getMaxMultiplier(self):
        return self._getReal(9)

    def setMaxMultiplier(self, value):
        self._setReal(9, value)
        return

    def getIsLootBoxesBuyEnabled(self):
        return self._getBool(10)

    def setIsLootBoxesBuyEnabled(self, value):
        self._setBool(10, value)
        return

    def getIsLootBoxEnabled(self):
        return self._getBool(11)

    def setIsLootBoxEnabled(self, value):
        self._setBool(11, value)
        return

    def getHasSmallBoxes(self):
        return self._getBool(12)

    def setHasSmallBoxes(self, value):
        self._setBool(12, value)
        return

    def getHasTamagochiUnlock(self):
        return self._getBool(13)

    def setHasTamagochiUnlock(self, value):
        self._setBool(13, value)
        return

    def getIsMachineEnabled(self):
        return self._getBool(14)

    def setIsMachineEnabled(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(NewYearInfoViewModel, self)._initialize()
        self._addViewModelProperty(b'videoCover', VideoCoverModel())
        self._addViewModelProperty(b'region', RegionModel())
        self._addNumberProperty(b'startTab')
        self._addNumberProperty(b'startDate', 0)
        self._addNumberProperty(b'endDate', 0)
        self._addRealProperty(b'maxBonus', 0.0)
        self._addRealProperty(b'usualMaxBonus', 0.0)
        self._addNumberProperty(b'questsToGetExtraSlot', 0)
        self._addRealProperty(b'minMultiplier', 0.0)
        self._addRealProperty(b'maxMultiplier', 0.0)
        self._addBoolProperty(b'isLootBoxesBuyEnabled', False)
        self._addBoolProperty(b'isLootBoxEnabled', False)
        self._addBoolProperty(b'hasSmallBoxes', False)
        self._addBoolProperty(b'hasTamagochiUnlock', False)
        self._addBoolProperty(b'isMachineEnabled', False)
        self.onButtonClick = self._addCommand(b'onButtonClick')
        return
