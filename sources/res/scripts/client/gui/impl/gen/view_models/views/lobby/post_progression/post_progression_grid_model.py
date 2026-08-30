from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.post_progression.multi_step_model import MultiStepModel
from gui.impl.gen.view_models.views.lobby.post_progression.single_step_model import SingleStepModel

class PostProgressionGridModel(ViewModel):
    __slots__ = (b'onMainStepActionClick', b'onMainStepSelectClick', b'onMultiStepActionClick', b'onMultiStepSelectClick', b'onPrebattleSwitchToggleClick')

    def __init__(self, properties=3, commands=5):
        super(PostProgressionGridModel, self).__init__(properties=properties, commands=commands)
        return

    def getMainSelectedIdx(self):
        return self._getNumber(0)

    def setMainSelectedIdx(self, value):
        self._setNumber(0, value)
        return

    def getMainSteps(self):
        return self._getArray(1)

    def setMainSteps(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getMainStepsType():
        return SingleStepModel

    def getMultiSteps(self):
        return self._getArray(2)

    def setMultiSteps(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getMultiStepsType():
        return MultiStepModel

    def _initialize(self):
        super(PostProgressionGridModel, self)._initialize()
        self._addNumberProperty(b'mainSelectedIdx', -1)
        self._addArrayProperty(b'mainSteps', Array())
        self._addArrayProperty(b'multiSteps', Array())
        self.onMainStepActionClick = self._addCommand(b'onMainStepActionClick')
        self.onMainStepSelectClick = self._addCommand(b'onMainStepSelectClick')
        self.onMultiStepActionClick = self._addCommand(b'onMultiStepActionClick')
        self.onMultiStepSelectClick = self._addCommand(b'onMultiStepSelectClick')
        self.onPrebattleSwitchToggleClick = self._addCommand(b'onPrebattleSwitchToggleClick')
        return
