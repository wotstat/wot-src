from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from white_tiger.gui.impl.gen.view_models.views.lobby.wt_progression_level_model import WtProgressionLevelModel

class WtProgressionModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=6, commands=0):
        super(WtProgressionModel, self).__init__(properties=properties, commands=commands)
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

    def getPreviousStage(self):
        return self._getNumber(4)

    def setPreviousStage(self, value):
        self._setNumber(4, value)
        return

    def getStages(self):
        return self._getArray(5)

    def setStages(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getStagesType():
        return WtProgressionLevelModel

    def _initialize(self):
        super(WtProgressionModel, self)._initialize()
        self._addNumberProperty(b'stampsCurrent', 0)
        self._addNumberProperty(b'stampsPrevious', 0)
        self._addNumberProperty(b'stampsNeededPerStage', 0)
        self._addNumberProperty(b'currentStage', 0)
        self._addNumberProperty(b'previousStage', 0)
        self._addArrayProperty(b'stages', Array())
        return
