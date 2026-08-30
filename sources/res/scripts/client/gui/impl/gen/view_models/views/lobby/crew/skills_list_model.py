from frameworks.wulf import Array
from gui.impl.gen.view_models.views.lobby.crew.components.component_base_model import ComponentBaseModel
from gui.impl.gen.view_models.views.lobby.crew.skill_training_model import SkillTrainingModel

class SkillsListModel(ComponentBaseModel):
    __slots__ = (b'onSkillClick', b'onSkillHover', b'onSkillOut', b'onTrain', b'onCancel')

    def __init__(self, properties=4, commands=5):
        super(SkillsListModel, self).__init__(properties=properties, commands=commands)
        return

    def getIrrelevantSkillsList(self):
        return self._getArray(1)

    def setIrrelevantSkillsList(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getIrrelevantSkillsListType():
        return SkillTrainingModel

    def getCommonSkillsList(self):
        return self._getArray(2)

    def setCommonSkillsList(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getCommonSkillsListType():
        return SkillTrainingModel

    def getRegularSkillsList(self):
        return self._getArray(3)

    def setRegularSkillsList(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getRegularSkillsListType():
        return SkillTrainingModel

    def _initialize(self):
        super(SkillsListModel, self)._initialize()
        self._addArrayProperty(b'irrelevantSkillsList', Array())
        self._addArrayProperty(b'commonSkillsList', Array())
        self._addArrayProperty(b'regularSkillsList', Array())
        self.onSkillClick = self._addCommand(b'onSkillClick')
        self.onSkillHover = self._addCommand(b'onSkillHover')
        self.onSkillOut = self._addCommand(b'onSkillOut')
        self.onTrain = self._addCommand(b'onTrain')
        self.onCancel = self._addCommand(b'onCancel')
        return
