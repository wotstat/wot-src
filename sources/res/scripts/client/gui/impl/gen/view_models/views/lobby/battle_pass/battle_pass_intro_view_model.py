from gui.impl.gen import R
from gui.impl.gen.view_models.views.lobby.common.base_intro_view_model import BaseIntroViewModel

class BattlePassIntroViewModel(BaseIntroViewModel):
    __slots__ = ()

    def __init__(self, properties=10, commands=3):
        super(BattlePassIntroViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getBackground(self):
        return self._getResource(5)

    def setBackground(self, value):
        self._setResource(5, value)
        return

    def getSubTitle(self):
        return self._getResource(6)

    def setSubTitle(self, value):
        self._setResource(6, value)
        return

    def getHasMarathon(self):
        return self._getBool(7)

    def setHasMarathon(self, value):
        self._setBool(7, value)
        return

    def getMarathonChapterStartDate(self):
        return self._getNumber(8)

    def setMarathonChapterStartDate(self, value):
        self._setNumber(8, value)
        return

    def getMarathonChapterEndDate(self):
        return self._getNumber(9)

    def setMarathonChapterEndDate(self, value):
        self._setNumber(9, value)
        return

    def _initialize(self):
        super(BattlePassIntroViewModel, self)._initialize()
        self._addResourceProperty(b'background', R.invalid())
        self._addResourceProperty(b'subTitle', R.invalid())
        self._addBoolProperty(b'hasMarathon', False)
        self._addNumberProperty(b'marathonChapterStartDate', 0)
        self._addNumberProperty(b'marathonChapterEndDate', 0)
        return
