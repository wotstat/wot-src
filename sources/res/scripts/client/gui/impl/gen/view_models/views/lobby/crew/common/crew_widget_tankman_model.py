from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_skill_list_model import CrewSkillListModel

class CrewWidgetTankmanModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=20, commands=0):
        super(CrewWidgetTankmanModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def skills(self):
        return self._getViewModel(0)

    @staticmethod
    def getSkillsType():
        return CrewSkillListModel

    @property
    def possibleSkills(self):
        return self._getViewModel(1)

    @staticmethod
    def getPossibleSkillsType():
        return CrewSkillListModel

    def getTankmanID(self):
        return self._getNumber(2)

    def setTankmanID(self, value):
        self._setNumber(2, value)
        return

    def getFullName(self):
        return self._getString(3)

    def setFullName(self, value):
        self._setString(3, value)
        return

    def getIcon(self):
        return self._getString(4)

    def setIcon(self, value):
        self._setString(4, value)
        return

    def getRoles(self):
        return self._getArray(5)

    def setRoles(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getRolesType():
        return unicode

    def getNewSkillsAmount(self):
        return self._getNumber(6)

    def setNewSkillsAmount(self, value):
        self._setNumber(6, value)
        return

    def getPossibleSkillsAmount(self):
        return self._getNumber(7)

    def setPossibleSkillsAmount(self, value):
        self._setNumber(7, value)
        return

    def getLastPossibleSkillLevel(self):
        return self._getReal(8)

    def setLastPossibleSkillLevel(self, value):
        self._setReal(8, value)
        return

    def getHasPossibleProgress(self):
        return self._getBool(9)

    def setHasPossibleProgress(self, value):
        self._setBool(9, value)
        return

    def getLastSkillLevel(self):
        return self._getReal(10)

    def setLastSkillLevel(self, value):
        self._setReal(10, value)
        return

    def getLastSkillLevelFull(self):
        return self._getReal(11)

    def setLastSkillLevelFull(self, value):
        self._setReal(11, value)
        return

    def getIsLessMastered(self):
        return self._getBool(12)

    def setIsLessMastered(self, value):
        self._setBool(12, value)
        return

    def getIsInSkin(self):
        return self._getBool(13)

    def setIsInSkin(self, value):
        self._setBool(13, value)
        return

    def getIsFemale(self):
        return self._getBool(14)

    def setIsFemale(self, value):
        self._setBool(14, value)
        return

    def getHasWarning(self):
        return self._getBool(15)

    def setHasWarning(self, value):
        self._setBool(15, value)
        return

    def getIsInteractive(self):
        return self._getBool(16)

    def setIsInteractive(self, value):
        self._setBool(16, value)
        return

    def getHasPostProgression(self):
        return self._getBool(17)

    def setHasPostProgression(self, value):
        self._setBool(17, value)
        return

    def getSkillsEfficiency(self):
        return self._getReal(18)

    def setSkillsEfficiency(self, value):
        self._setReal(18, value)
        return

    def getPossibleSkillsEfficiency(self):
        return self._getReal(19)

    def setPossibleSkillsEfficiency(self, value):
        self._setReal(19, value)
        return

    def _initialize(self):
        super(CrewWidgetTankmanModel, self)._initialize()
        self._addViewModelProperty(b'skills', CrewSkillListModel())
        self._addViewModelProperty(b'possibleSkills', CrewSkillListModel())
        self._addNumberProperty(b'tankmanID', 0)
        self._addStringProperty(b'fullName', b'')
        self._addStringProperty(b'icon', b'')
        self._addArrayProperty(b'roles', Array())
        self._addNumberProperty(b'newSkillsAmount', 0)
        self._addNumberProperty(b'possibleSkillsAmount', 0)
        self._addRealProperty(b'lastPossibleSkillLevel', -1)
        self._addBoolProperty(b'hasPossibleProgress', False)
        self._addRealProperty(b'lastSkillLevel', 0.0)
        self._addRealProperty(b'lastSkillLevelFull', 0.0)
        self._addBoolProperty(b'isLessMastered', False)
        self._addBoolProperty(b'isInSkin', False)
        self._addBoolProperty(b'isFemale', False)
        self._addBoolProperty(b'hasWarning', False)
        self._addBoolProperty(b'isInteractive', False)
        self._addBoolProperty(b'hasPostProgression', False)
        self._addRealProperty(b'skillsEfficiency', 0.0)
        self._addRealProperty(b'possibleSkillsEfficiency', -1)
        return
