from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.crew_widget_tankman_skill_model import CrewWidgetTankmanSkillModel

class CrewWidgetTankmanModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=21, commands=0):
        super(CrewWidgetTankmanModel, self).__init__(properties=properties, commands=commands)
        return

    def getTankmanID(self):
        return self._getNumber(0)

    def setTankmanID(self, value):
        self._setNumber(0, value)
        return

    def getFullName(self):
        return self._getString(1)

    def setFullName(self, value):
        self._setString(1, value)
        return

    def getIcon(self):
        return self._getString(2)

    def setIcon(self, value):
        self._setString(2, value)
        return

    def getSpecializationLevel(self):
        return self._getNumber(3)

    def setSpecializationLevel(self, value):
        self._setNumber(3, value)
        return

    def getBaseSpecializationLevel(self):
        return self._getNumber(4)

    def setBaseSpecializationLevel(self, value):
        self._setNumber(4, value)
        return

    def getRoles(self):
        return self._getArray(5)

    def setRoles(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getRolesType():
        return unicode

    def getSkills(self):
        return self._getArray(6)

    def setSkills(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getSkillsType():
        return CrewWidgetTankmanSkillModel

    def getNewSkillsAmount(self):
        return self._getNumber(7)

    def setNewSkillsAmount(self, value):
        self._setNumber(7, value)
        return

    def getPossibleSkillsAmount(self):
        return self._getNumber(8)

    def setPossibleSkillsAmount(self, value):
        self._setNumber(8, value)
        return

    def getLastPossibleSkillLevel(self):
        return self._getReal(9)

    def setLastPossibleSkillLevel(self, value):
        self._setReal(9, value)
        return

    def getHasPossibleProgress(self):
        return self._getBool(10)

    def setHasPossibleProgress(self, value):
        self._setBool(10, value)
        return

    def getLastSkillLevel(self):
        return self._getReal(11)

    def setLastSkillLevel(self, value):
        self._setReal(11, value)
        return

    def getLastRoleLevel(self):
        return self._getReal(12)

    def setLastRoleLevel(self, value):
        self._setReal(12, value)
        return

    def getLastPossibleRoleLevel(self):
        return self._getReal(13)

    def setLastPossibleRoleLevel(self, value):
        self._setReal(13, value)
        return

    def getLastSkillLevelFull(self):
        return self._getReal(14)

    def setLastSkillLevelFull(self, value):
        self._setReal(14, value)
        return

    def getIsLessMastered(self):
        return self._getBool(15)

    def setIsLessMastered(self, value):
        self._setBool(15, value)
        return

    def getIsInSkin(self):
        return self._getBool(16)

    def setIsInSkin(self, value):
        self._setBool(16, value)
        return

    def getIsFemale(self):
        return self._getBool(17)

    def setIsFemale(self, value):
        self._setBool(17, value)
        return

    def getIsUntrained(self):
        return self._getBool(18)

    def setIsUntrained(self, value):
        self._setBool(18, value)
        return

    def getHasWarning(self):
        return self._getBool(19)

    def setHasWarning(self, value):
        self._setBool(19, value)
        return

    def getIsInteractive(self):
        return self._getBool(20)

    def setIsInteractive(self, value):
        self._setBool(20, value)
        return

    def _initialize(self):
        super(CrewWidgetTankmanModel, self)._initialize()
        self._addNumberProperty(b'tankmanID', 0)
        self._addStringProperty(b'fullName', b'')
        self._addStringProperty(b'icon', b'')
        self._addNumberProperty(b'specializationLevel', 0)
        self._addNumberProperty(b'baseSpecializationLevel', 0)
        self._addArrayProperty(b'roles', Array())
        self._addArrayProperty(b'skills', Array())
        self._addNumberProperty(b'newSkillsAmount', 0)
        self._addNumberProperty(b'possibleSkillsAmount', 0)
        self._addRealProperty(b'lastPossibleSkillLevel', -1)
        self._addBoolProperty(b'hasPossibleProgress', False)
        self._addRealProperty(b'lastSkillLevel', 0.0)
        self._addRealProperty(b'lastRoleLevel', 0.0)
        self._addRealProperty(b'lastPossibleRoleLevel', 0.0)
        self._addRealProperty(b'lastSkillLevelFull', 0.0)
        self._addBoolProperty(b'isLessMastered', False)
        self._addBoolProperty(b'isInSkin', False)
        self._addBoolProperty(b'isFemale', False)
        self._addBoolProperty(b'isUntrained', False)
        self._addBoolProperty(b'hasWarning', False)
        self._addBoolProperty(b'isInteractive', False)
        return
