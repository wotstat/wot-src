from enum import Enum
from frameworks.wulf import Array, ViewModel
from frontline.gui.impl.gen.view_models.views.lobby.views.skill_base_model import SkillBaseModel

class SkillCategoryType(Enum):
    FIRESUPPORT = b'firesupport'
    RECONNAISSANCE = b'reconnaissance'
    TACTICS = b'tactics'


class SkillCategoryBaseModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(SkillCategoryBaseModel, self).__init__(properties=properties, commands=commands)
        return

    def getType(self):
        return SkillCategoryType(self._getString(0))

    def setType(self, value):
        self._setString(0, value.value)
        return

    def getSkills(self):
        return self._getArray(1)

    def setSkills(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getSkillsType():
        return SkillBaseModel

    def _initialize(self):
        super(SkillCategoryBaseModel, self)._initialize()
        self._addStringProperty(b'type')
        self._addArrayProperty(b'skills', Array())
        return
