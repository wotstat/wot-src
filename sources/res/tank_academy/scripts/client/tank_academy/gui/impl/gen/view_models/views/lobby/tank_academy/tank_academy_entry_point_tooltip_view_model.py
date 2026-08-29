from frameworks.wulf import ViewModel
from tank_academy.gui.impl.gen.view_models.views.lobby.tank_academy.quest_progress_model import QuestProgressModel
from tank_academy.gui.impl.gen.view_models.views.lobby.tank_academy.quest_view_model import QuestViewModel

class TankAcademyEntryPointTooltipViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(TankAcademyEntryPointTooltipViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def questProgress(self):
        return self._getViewModel(0)

    @staticmethod
    def getQuestProgressType():
        return QuestProgressModel

    @property
    def quest(self):
        return self._getViewModel(1)

    @staticmethod
    def getQuestType():
        return QuestViewModel

    def getEndDate(self):
        return self._getNumber(2)

    def setEndDate(self, value):
        self._setNumber(2, value)
        return

    def getHasToken(self):
        return self._getBool(3)

    def setHasToken(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(TankAcademyEntryPointTooltipViewModel, self)._initialize()
        self._addViewModelProperty(b'questProgress', QuestProgressModel())
        self._addViewModelProperty(b'quest', QuestViewModel())
        self._addNumberProperty(b'endDate', 0)
        self._addBoolProperty(b'hasToken', False)
        return
