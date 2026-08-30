from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_model import CrewSkillModel

class CrewSkillListModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(CrewSkillListModel, self).__init__(properties=properties, commands=commands)
        return

    def getMajorSkills(self):
        return self._getArray(0)

    def setMajorSkills(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getMajorSkillsType():
        return CrewSkillModel

    def getBonusSkills(self):
        return self._getArray(1)

    def setBonusSkills(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getBonusSkillsType():
        return CrewSkillModel

    def getSkillsEfficiency(self):
        return self._getReal(2)

    def setSkillsEfficiency(self, value):
        self._setReal(2, value)
        return

    def _initialize(self):
        super(CrewSkillListModel, self)._initialize()
        self._addArrayProperty(b'majorSkills', Array())
        self._addArrayProperty(b'bonusSkills', Array())
        self._addRealProperty(b'skillsEfficiency', 0.0)
        return
