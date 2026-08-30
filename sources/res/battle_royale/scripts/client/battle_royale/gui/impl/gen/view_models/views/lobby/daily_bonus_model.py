from battle_royale.gui.impl.gen.view_models.views.lobby.enums import CoinType
from frameworks.wulf import ViewModel

class DailyBonusModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=5, commands=0):
        super(DailyBonusModel, self).__init__(properties=properties, commands=commands)
        return

    def getHasDailyBonus(self):
        return self._getBool(0)

    def setHasDailyBonus(self, value):
        self._setBool(0, value)
        return

    def getDailyBonusFactor(self):
        return self._getNumber(1)

    def setDailyBonusFactor(self, value):
        self._setNumber(1, value)
        return

    def getSoloTopPlaces(self):
        return self._getNumber(2)

    def setSoloTopPlaces(self, value):
        self._setNumber(2, value)
        return

    def getSquadTopPlaces(self):
        return self._getNumber(3)

    def setSquadTopPlaces(self, value):
        self._setNumber(3, value)
        return

    def getCoinType(self):
        return CoinType(self._getString(4))

    def setCoinType(self, value):
        self._setString(4, value.value)
        return

    def _initialize(self):
        super(DailyBonusModel, self)._initialize()
        self._addBoolProperty(b'hasDailyBonus', False)
        self._addNumberProperty(b'dailyBonusFactor', 0)
        self._addNumberProperty(b'soloTopPlaces', 0)
        self._addNumberProperty(b'squadTopPlaces', 0)
        self._addStringProperty(b'coinType')
        return
