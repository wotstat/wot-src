from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_compare.compare_step_model import CompareStepModel

class CompareModificationsPanelViewModel(ViewModel):
    __slots__ = (b'onClearModifications', b'onConfigureModifications', b'onClose')

    def __init__(self, properties=2, commands=3):
        super(CompareModificationsPanelViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsEmpty(self):
        return self._getBool(0)

    def setIsEmpty(self, value):
        self._setBool(0, value)
        return

    def getSteps(self):
        return self._getArray(1)

    def setSteps(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getStepsType():
        return CompareStepModel

    def _initialize(self):
        super(CompareModificationsPanelViewModel, self)._initialize()
        self._addBoolProperty(b'isEmpty', True)
        self._addArrayProperty(b'steps', Array())
        self.onClearModifications = self._addCommand(b'onClearModifications')
        self.onConfigureModifications = self._addCommand(b'onConfigureModifications')
        self.onClose = self._addCommand(b'onClose')
        return
