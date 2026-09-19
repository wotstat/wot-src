from frameworks.wulf import ViewModel
from halloween.gui.impl.gen.view_models.views.lobby.current_enemy_model import CurrentEnemyModel

class BestiaryModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=3, commands=0):
        super(BestiaryModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentEnemy(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentEnemyType():
        return CurrentEnemyModel

    def getHasUnlockedEnemies(self):
        return self._getBool(1)

    def setHasUnlockedEnemies(self, value):
        self._setBool(1, value)
        return

    def getHasNewEnemies(self):
        return self._getBool(2)

    def setHasNewEnemies(self, value):
        self._setBool(2, value)
        return

    def _initialize(self):
        super(BestiaryModel, self)._initialize()
        self._addViewModelProperty(b'currentEnemy', CurrentEnemyModel())
        self._addBoolProperty(b'hasUnlockedEnemies', False)
        self._addBoolProperty(b'hasNewEnemies', False)
        return
