from frameworks.wulf import ViewModel
from white_tiger.gui.impl.gen.view_models.views.lobby.wt_progression_model import WtProgressionModel
from white_tiger.gui.impl.gen.view_models.views.lobby.wt_quests_model import WtQuestsModel

class WtProgressionViewModel(ViewModel):
    __slots__ = (b'onClose', b'onIntroVideoClicked', b'onOutroVideoClicked')

    def __init__(self, properties=3, commands=3):
        super(WtProgressionViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def dailyQuests(self):
        return self._getViewModel(0)

    @staticmethod
    def getDailyQuestsType():
        return WtQuestsModel

    @property
    def progression(self):
        return self._getViewModel(1)

    @staticmethod
    def getProgressionType():
        return WtProgressionModel

    def getIsOutroVideoAvailable(self):
        return self._getBool(2)

    def setIsOutroVideoAvailable(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(WtProgressionViewModel, self)._initialize()
        self._addViewModelProperty(b'dailyQuests', WtQuestsModel())
        self._addViewModelProperty(b'progression', WtProgressionModel())
        self._addBoolProperty(b'isOutroVideoAvailable', False)
        self.onClose = self._addCommand(b'onClose')
        self.onIntroVideoClicked = self._addCommand(b'onIntroVideoClicked')
        self.onOutroVideoClicked = self._addCommand(b'onOutroVideoClicked')
        return
