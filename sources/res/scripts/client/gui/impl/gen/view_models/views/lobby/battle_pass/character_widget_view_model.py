from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.character_model import CharacterModel

class CharacterWidgetViewModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=2, commands=0):
        super(CharacterWidgetViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def free(self):
        return self._getViewModel(0)

    @staticmethod
    def getFreeType():
        return CharacterModel

    @property
    def paid(self):
        return self._getViewModel(1)

    @staticmethod
    def getPaidType():
        return CharacterModel

    def _initialize(self):
        super(CharacterWidgetViewModel, self)._initialize()
        self._addViewModelProperty(b'free', CharacterModel())
        self._addViewModelProperty(b'paid', CharacterModel())
        return
