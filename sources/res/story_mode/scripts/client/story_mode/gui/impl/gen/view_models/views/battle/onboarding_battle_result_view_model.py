from gui.impl.gen import R
from frameworks.wulf import ViewModel

class OnboardingBattleResultViewModel(ViewModel):
    __slots__ = (b'onContinue', b'onLoaded')

    def __init__(self, properties=2, commands=2):
        super(OnboardingBattleResultViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getCauseText(self):
        return self._getResource(0)

    def setCauseText(self, value):
        self._setResource(0, value)
        return

    def getMissionId(self):
        return self._getNumber(1)

    def setMissionId(self, value):
        self._setNumber(1, value)
        return

    def _initialize(self):
        super(OnboardingBattleResultViewModel, self)._initialize()
        self._addResourceProperty(b'causeText', R.invalid())
        self._addNumberProperty(b'missionId', 0)
        self.onContinue = self._addCommand(b'onContinue')
        self.onLoaded = self._addCommand(b'onLoaded')
        return
