from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.common.skill.skill_simple_model import SkillSimpleModel

class CompareSkillsPanelViewModel(ViewModel):
    __slots__ = (b'onClick', b'onReset')

    def __init__(self, properties=1, commands=2):
        super(CompareSkillsPanelViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSkills(self):
        return self._getArray(0)

    def setSkills(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getSkillsType():
        return SkillSimpleModel

    def _initialize(self):
        super(CompareSkillsPanelViewModel, self)._initialize()
        self._addArrayProperty(b'skills', Array())
        self.onClick = self._addCommand(b'onClick')
        self.onReset = self._addCommand(b'onReset')
        return
