from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.personal_reserves.reserves_group_model import ReservesGroupModel

class ReservesActivationViewModel(ViewModel):
    __slots__ = (b'onNavigateToStore', b'onClose', b'onBoosterActivate', b'onNavigateToDepot', b'onCardHover')

    def __init__(self, properties=5, commands=5):
        super(ReservesActivationViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getReserveGroups(self):
        return self._getArray(0)

    def setReserveGroups(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getReserveGroupsType():
        return ReservesGroupModel

    def getGold(self):
        return self._getNumber(1)

    def setGold(self, value):
        self._setNumber(1, value)
        return

    def getCanActivateClanReserves(self):
        return self._getBool(2)

    def setCanActivateClanReserves(self, value):
        self._setBool(2, value)
        return

    def getNextExpirationTime(self):
        return self._getNumber(3)

    def setNextExpirationTime(self, value):
        self._setNumber(3, value)
        return

    def getNextExpirationAmount(self):
        return self._getNumber(4)

    def setNextExpirationAmount(self, value):
        self._setNumber(4, value)
        return

    def _initialize(self):
        super(ReservesActivationViewModel, self)._initialize()
        self._addArrayProperty(b'reserveGroups', Array())
        self._addNumberProperty(b'gold', 0)
        self._addBoolProperty(b'canActivateClanReserves', False)
        self._addNumberProperty(b'nextExpirationTime', 0)
        self._addNumberProperty(b'nextExpirationAmount', 0)
        self.onNavigateToStore = self._addCommand(b'onNavigateToStore')
        self.onClose = self._addCommand(b'onClose')
        self.onBoosterActivate = self._addCommand(b'onBoosterActivate')
        self.onNavigateToDepot = self._addCommand(b'onNavigateToDepot')
        self.onCardHover = self._addCommand(b'onCardHover')
        return
