from frameworks.wulf import ViewModel

class ProgressiveRewardModel(ViewModel):
    __slots__ = ()
    PROB_MIN = b'prob_min'
    PROB_MED = b'prob_med'
    PROB_MAX = b'prob_max'
    RECEIVED = b'received'

    def __init__(self, properties=4, commands=0):
        super(ProgressiveRewardModel, self).__init__(properties=properties, commands=commands)
        return

    def getMaxSteps(self):
        return self._getNumber(0)

    def setMaxSteps(self, value):
        self._setNumber(0, value)
        return

    def getCurrentStep(self):
        return self._getNumber(1)

    def setCurrentStep(self, value):
        self._setNumber(1, value)
        return

    def getCurrentStepState(self):
        return self._getString(2)

    def setCurrentStepState(self, value):
        self._setString(2, value)
        return

    def getIsEnabled(self):
        return self._getBool(3)

    def setIsEnabled(self, value):
        self._setBool(3, value)
        return

    def _initialize(self):
        super(ProgressiveRewardModel, self)._initialize()
        self._addNumberProperty(b'maxSteps', 0)
        self._addNumberProperty(b'currentStep', 0)
        self._addStringProperty(b'currentStepState', b'')
        self._addBoolProperty(b'isEnabled', False)
        return
