from enum import Enum
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_simple_model import SkillSimpleModel

class SkillState(Enum):
    DEFAULT = b'default'
    SELECTED = b'selected'
    DISABLED = b'disabled'


class SkillType(Enum):
    MAJOR = b'major'
    COMMON = b'common'
    BONUS = b'bonus'


class SkillSelectItemModel(SkillSimpleModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(SkillSelectItemModel, self).__init__(properties=properties, commands=commands)
        return

    def getState(self):
        return SkillState(self._getString(4))

    def setState(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(SkillSelectItemModel, self)._initialize()
        self._addStringProperty(b'state')
        return
