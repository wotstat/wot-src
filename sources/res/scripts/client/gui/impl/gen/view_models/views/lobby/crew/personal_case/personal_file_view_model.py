from enum import Enum
from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.tankman_skill_model import TankmanSkillModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.tankman_skills_group_model import TankmanSkillsGroupModel

class SkillsState(Enum):
    LEARNAVAILABLE = b'available'
    TRAINING = b'training'
    ACHIEVE = b'achieve'
    ZEROSKILLS = b'zeroSkills'
    ALLSKILLS = b'allSkills'


class PersonalFileViewModel(ViewModel):
    __slots__ = (b'onIncrease', b'onReset', b'onHoverSkill', b'onLeaveSkill', b'onClickSkill')

    def __init__(self, properties=11, commands=5):
        super(PersonalFileViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSkillsState(self):
        return SkillsState(self._getString(0))

    def setSkillsState(self, value):
        self._setString(0, value.value)
        return

    def getSelectAvailableSkillsCount(self):
        return self._getNumber(1)

    def setSelectAvailableSkillsCount(self, value):
        self._setNumber(1, value)
        return

    def getIsFemale(self):
        return self._getBool(2)

    def setIsFemale(self, value):
        self._setBool(2, value)
        return

    def getIsTankmanWithDescription(self):
        return self._getBool(3)

    def setIsTankmanWithDescription(self, value):
        self._setBool(3, value)
        return

    def getIsResetDisable(self):
        return self._getBool(4)

    def setIsResetDisable(self, value):
        self._setBool(4, value)
        return

    def getHasIncreaseDiscount(self):
        return self._getBool(5)

    def setHasIncreaseDiscount(self, value):
        self._setBool(5, value)
        return

    def getHasDropSkillDiscount(self):
        return self._getBool(6)

    def setHasDropSkillDiscount(self, value):
        self._setBool(6, value)
        return

    def getIsTankmanInVehicle(self):
        return self._getBool(7)

    def setIsTankmanInVehicle(self, value):
        self._setBool(7, value)
        return

    def getRelevantGroupedSkills(self):
        return self._getArray(8)

    def setRelevantGroupedSkills(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getRelevantGroupedSkillsType():
        return TankmanSkillsGroupModel

    def getIrrelevantGroupedSkills(self):
        return self._getArray(9)

    def setIrrelevantGroupedSkills(self, value):
        self._setArray(9, value)
        return

    @staticmethod
    def getIrrelevantGroupedSkillsType():
        return TankmanSkillsGroupModel

    def getCommonSkills(self):
        return self._getArray(10)

    def setCommonSkills(self, value):
        self._setArray(10, value)
        return

    @staticmethod
    def getCommonSkillsType():
        return TankmanSkillModel

    def _initialize(self):
        super(PersonalFileViewModel, self)._initialize()
        self._addStringProperty(b'skillsState')
        self._addNumberProperty(b'selectAvailableSkillsCount', 0)
        self._addBoolProperty(b'isFemale', False)
        self._addBoolProperty(b'isTankmanWithDescription', False)
        self._addBoolProperty(b'isResetDisable', False)
        self._addBoolProperty(b'hasIncreaseDiscount', False)
        self._addBoolProperty(b'hasDropSkillDiscount', False)
        self._addBoolProperty(b'isTankmanInVehicle', False)
        self._addArrayProperty(b'relevantGroupedSkills', Array())
        self._addArrayProperty(b'irrelevantGroupedSkills', Array())
        self._addArrayProperty(b'commonSkills', Array())
        self.onIncrease = self._addCommand(b'onIncrease')
        self.onReset = self._addCommand(b'onReset')
        self.onHoverSkill = self._addCommand(b'onHoverSkill')
        self.onLeaveSkill = self._addCommand(b'onLeaveSkill')
        self.onClickSkill = self._addCommand(b'onClickSkill')
        return
