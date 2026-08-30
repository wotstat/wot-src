from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.tankman_skills_group_model import TankmanSkillsGroupModel

class SkillsMatrixModel(ComponentBaseModel):
    __slots__ = (b'onIncrease', b'onReset', b'onSkillClick', b'onSetAnimationInProgress')

    def __init__(self, properties=8, commands=4):
        super(SkillsMatrixModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def mainSkills(self):
        return self._getViewModel(1)

    @staticmethod
    def getMainSkillsType():
        return TankmanSkillsGroupModel

    def getIsResetDisable(self):
        return self._getBool(2)

    def setIsResetDisable(self, value):
        self._setBool(2, value)
        return

    def getHasResetDiscount(self):
        return self._getBool(3)

    def setHasResetDiscount(self, value):
        self._setBool(3, value)
        return

    def getIsResetFree(self):
        return self._getBool(4)

    def setIsResetFree(self, value):
        self._setBool(4, value)
        return

    def getHasIncreaseDiscount(self):
        return self._getBool(5)

    def setHasIncreaseDiscount(self, value):
        self._setBool(5, value)
        return

    def getResetGracePeriodLeft(self):
        return self._getNumber(6)

    def setResetGracePeriodLeft(self, value):
        self._setNumber(6, value)
        return

    def getBonusSkills(self):
        return self._getArray(7)

    def setBonusSkills(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getBonusSkillsType():
        return TankmanSkillsGroupModel

    def _initialize(self):
        super(SkillsMatrixModel, self)._initialize()
        self._addViewModelProperty(b'mainSkills', TankmanSkillsGroupModel())
        self._addBoolProperty(b'isResetDisable', False)
        self._addBoolProperty(b'hasResetDiscount', False)
        self._addBoolProperty(b'isResetFree', False)
        self._addBoolProperty(b'hasIncreaseDiscount', False)
        self._addNumberProperty(b'resetGracePeriodLeft', 0)
        self._addArrayProperty(b'bonusSkills', Array())
        self.onIncrease = self._addCommand(b'onIncrease')
        self.onReset = self._addCommand(b'onReset')
        self.onSkillClick = self._addCommand(b'onSkillClick')
        self.onSetAnimationInProgress = self._addCommand(b'onSetAnimationInProgress')
        return
