from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.skill_model import SkillModel

class CharacterModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(CharacterModel, self).__init__(properties=properties, commands=commands)
        return

    def getTankman(self):
        return self._getString(0)

    def setTankman(self, value):
        self._setString(0, value)
        return

    def getIcon(self):
        return self._getString(1)

    def setIcon(self, value):
        self._setString(1, value)
        return

    def getSkills(self):
        return self._getArray(2)

    def setSkills(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getSkillsType():
        return SkillModel

    def getTooltipId(self):
        return self._getString(3)

    def setTooltipId(self, value):
        self._setString(3, value)
        return

    def getGroupName(self):
        return self._getString(4)

    def setGroupName(self, value):
        self._setString(4, value)
        return

    def getHasVoice(self):
        return self._getBool(5)

    def setHasVoice(self, value):
        self._setBool(5, value)
        return

    def _initialize(self):
        super(CharacterModel, self)._initialize()
        self._addStringProperty(b'tankman', b'')
        self._addStringProperty(b'icon', b'')
        self._addArrayProperty(b'skills', Array())
        self._addStringProperty(b'tooltipId', b'')
        self._addStringProperty(b'groupName', b'')
        self._addBoolProperty(b'hasVoice', False)
        return
