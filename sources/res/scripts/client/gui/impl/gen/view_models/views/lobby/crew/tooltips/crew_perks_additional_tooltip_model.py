from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_extended_model import SkillExtendedModel
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_progression_model import SkillProgressionModel

class CrewPerksAdditionalTooltipModel(SkillExtendedModel):
    __slots__ = ()

    def __init__(self, properties=16, commands=0):
        super(CrewPerksAdditionalTooltipModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def skillProgression(self):
        return self._getViewModel(9)

    @staticmethod
    def getSkillProgressionType():
        return SkillProgressionModel

    def getInfo(self):
        return self._getString(10)

    def setInfo(self, value):
        self._setString(10, value)
        return

    def getSkillType(self):
        return self._getString(11)

    def setSkillType(self, value):
        self._setString(11, value)
        return

    def getAnimationName(self):
        return self._getString(12)

    def setAnimationName(self, value):
        self._setString(12, value)
        return

    def getIsDisabled(self):
        return self._getBool(13)

    def setIsDisabled(self, value):
        self._setBool(13, value)
        return

    def getShowSkillProgression(self):
        return self._getBool(14)

    def setShowSkillProgression(self, value):
        self._setBool(14, value)
        return

    def getPopularityList(self):
        return self._getArray(15)

    def setPopularityList(self, value):
        self._setArray(15, value)
        return

    @staticmethod
    def getPopularityListType():
        return int

    def _initialize(self):
        super(CrewPerksAdditionalTooltipModel, self)._initialize()
        self._addViewModelProperty(b'skillProgression', SkillProgressionModel())
        self._addStringProperty(b'info', b'')
        self._addStringProperty(b'skillType', b'')
        self._addStringProperty(b'animationName', b'')
        self._addBoolProperty(b'isDisabled', False)
        self._addBoolProperty(b'showSkillProgression', False)
        self._addArrayProperty(b'popularityList', Array())
        return
