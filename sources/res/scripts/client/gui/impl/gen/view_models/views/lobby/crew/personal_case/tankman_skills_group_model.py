from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.crew.personal_case.tankman_skill_model import TankmanSkillModel

class TankmanSkillsGroupModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(TankmanSkillsGroupModel, self).__init__(properties=properties, commands=commands)
        return

    def getRole(self):
        return self._getString(0)

    def setRole(self, value):
        self._setString(0, value)
        return

    def getSkills(self):
        return self._getArray(1)

    def setSkills(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSkillsType():
        return TankmanSkillModel

    def _initialize(self):
        super(TankmanSkillsGroupModel, self)._initialize()
        self._addStringProperty(b'role', b'')
        self._addArrayProperty(b'skills', Array())
        return
