from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.comp7.skill_stats_model import SkillStatsModel

class SkillModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SkillModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def skillsStats(self):
        return self._getViewModel(0)

    @staticmethod
    def getSkillsStatsType():
        return SkillStatsModel

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getIntCD(self):
        return self._getNumber(2)

    def setIntCD(self, value):
        self._setNumber(2, value)
        return

    def getStartLevel(self):
        return self._getNumber(3)

    def setStartLevel(self, value):
        self._setNumber(3, value)
        return

    def getIsEquipped(self):
        return self._getBool(4)

    def setIsEquipped(self, value):
        self._setBool(4, value)
        return

    def _initialize(self):
        super(SkillModel, self)._initialize()
        self._addViewModelProperty(b'skillsStats', SkillStatsModel())
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'intCD', 0)
        self._addNumberProperty(b'startLevel', 0)
        self._addBoolProperty(b'isEquipped', False)
        return
