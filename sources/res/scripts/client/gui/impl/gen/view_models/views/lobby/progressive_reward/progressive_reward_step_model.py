from frameworks.wulf import ViewModel

class ProgressiveRewardStepModel(ViewModel):
    __slots__ = ()
    PR_STATE_NOT_RECEIVED = b'not_received'
    PR_STATE_OPENED = b'opened'
    PR_STATE_PROB_MIN = b'prob_min'
    PR_STATE_PROB_MED = b'prob_med'
    PR_STATE_PROB_MAX = b'prob_max'
    PR_STATE_RECEIVED = b'received'
    PR_TYPE_SMALL = b'small'
    PR_TYPE_BIG = b'big'
    PR_TYPE_SMALL_HIDDEN = b'small_hidden'
    PR_TYPE_BIG_HIDDEN = b'big_hidden'

    def __init__(self, properties=3, commands=0):
        super(ProgressiveRewardStepModel, self).__init__(properties=properties, commands=commands)
        return

    def getStepState(self):
        return self._getString(0)

    def setStepState(self, value):
        self._setString(0, value)
        return

    def getRewardType(self):
        return self._getString(1)

    def setRewardType(self, value):
        self._setString(1, value)
        return

    def getHasPreviousStep(self):
        return self._getBool(2)

    def setHasPreviousStep(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(ProgressiveRewardStepModel, self)._initialize()
        self._addStringProperty(b'stepState', b'not_received')
        self._addStringProperty(b'rewardType', b'small')
        self._addBoolProperty(b'hasPreviousStep', True)
        return
