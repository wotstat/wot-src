from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.battle_pass.tankman_model import TankmanModel

class TankmenVoiceoverViewModel(ViewModel):
    __slots__ = (b'showShop', b'close')

    def __init__(self, properties=2, commands=2):
        super(TankmenVoiceoverViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getScreenID(self):
        return self._getNumber(0)

    def setScreenID(self, value):
        self._setNumber(0, value)
        return

    def getTankmen(self):
        return self._getArray(1)

    def setTankmen(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getTankmenType():
        return TankmanModel

    def _initialize(self):
        super(TankmenVoiceoverViewModel, self)._initialize()
        self._addNumberProperty(b'screenID', 0)
        self._addArrayProperty(b'tankmen', Array())
        self.showShop = self._addCommand(b'showShop')
        self.close = self._addCommand(b'close')
        return
