from frameworks.wulf import Array
from halloween.gui.impl.gen.view_models.views.lobby.enemy_model import EnemyModel
from gui.impl.gen.view_models.views.selectable_view_model import SelectableViewModel

class BestiaryViewModel(SelectableViewModel):
    __slots__ = (b'onClose', b'onChangeEnemy', b'onResize')

    def __init__(self, properties=2, commands=5):
        super(BestiaryViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getSelectedIntCD(self):
        return self._getNumber(0)

    def setSelectedIntCD(self, value):
        self._setNumber(0, value)
        return

    def getEnemies(self):
        return self._getArray(1)

    def setEnemies(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getEnemiesType():
        return EnemyModel

    def _initialize(self):
        super(BestiaryViewModel, self)._initialize()
        self._addNumberProperty(b'selectedIntCD', 0)
        self._addArrayProperty(b'enemies', Array())
        self.onClose = self._addCommand(b'onClose')
        self.onChangeEnemy = self._addCommand(b'onChangeEnemy')
        self.onResize = self._addCommand(b'onResize')
        return
