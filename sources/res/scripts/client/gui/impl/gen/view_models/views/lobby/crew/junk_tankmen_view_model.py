from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.crew.tankman_model import TankmanModel

class JunkTankmenViewModel(ViewModel):
    __slots__ = (b'onLoadCards', b'onConfirm', b'onClose')

    def __init__(self, properties=3, commands=3):
        super(JunkTankmenViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getItemsAmount(self):
        return self._getNumber(0)

    def setItemsAmount(self, value):
        self._setNumber(0, value)
        return

    def getItemsOffset(self):
        return self._getNumber(1)

    def setItemsOffset(self, value):
        self._setNumber(1, value)
        return

    def getTankmanList(self):
        return self._getArray(2)

    def setTankmanList(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getTankmanListType():
        return TankmanModel

    def _initialize(self):
        super(JunkTankmenViewModel, self)._initialize()
        self._addNumberProperty(b'itemsAmount', 0)
        self._addNumberProperty(b'itemsOffset', 0)
        self._addArrayProperty(b'tankmanList', Array())
        self.onLoadCards = self._addCommand(b'onLoadCards')
        self.onConfirm = self._addCommand(b'onConfirm')
        self.onClose = self._addCommand(b'onClose')
        return
