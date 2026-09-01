from frameworks.wulf import Array, ViewModel
from white_tiger.gui.impl.gen.view_models.views.lobby.widgets.progression_level_model import ProgressionLevelModel

class ProgressionContentViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(ProgressionContentViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getStampsCurrent(self):
        return self._getNumber(0)

    def setStampsCurrent(self, value):
        self._setNumber(0, value)
        return

    def getStampsPrevious(self):
        return self._getNumber(1)

    def setStampsPrevious(self, value):
        self._setNumber(1, value)
        return

    def getStampsNeededPerStage(self):
        return self._getNumber(2)

    def setStampsNeededPerStage(self, value):
        self._setNumber(2, value)
        return

    def getCurrentStage(self):
        return self._getNumber(3)

    def setCurrentStage(self, value):
        self._setNumber(3, value)
        return

    def getStages(self):
        return self._getArray(4)

    def setStages(self, value):
        self._setArray(4, value)
        return

    @staticmethod
    def getStagesType():
        return ProgressionLevelModel

    def _initialize(self):
        super(ProgressionContentViewModel, self)._initialize()
        self._addNumberProperty(b'stampsCurrent', 0)
        self._addNumberProperty(b'stampsPrevious', 0)
        self._addNumberProperty(b'stampsNeededPerStage', 0)
        self._addNumberProperty(b'currentStage', 0)
        self._addArrayProperty(b'stages', Array())
        return
