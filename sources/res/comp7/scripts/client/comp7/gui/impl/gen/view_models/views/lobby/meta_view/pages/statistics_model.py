from comp7.gui.impl.gen.view_models.views.lobby.enums import Rank
from frameworks.wulf import ViewModel

class StatisticsModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=14, commands=0):
        super(StatisticsModel, self).__init__(properties=properties, commands=commands)
        return

    def getMaxAchievedRatingPoints(self):
        return self._getNumber(0)

    def setMaxAchievedRatingPoints(self, value):
        self._setNumber(0, value)
        return

    def getMaxAchievedRank(self):
        return Rank(self._getNumber(1))

    def setMaxAchievedRank(self, value):
        self._setNumber(1, value.value)
        return

    def getSoloBattlesCount(self):
        return self._getNumber(2)

    def setSoloBattlesCount(self, value):
        self._setNumber(2, value)
        return

    def getSuperPlatoonBattlesCount(self):
        return self._getNumber(3)

    def setSuperPlatoonBattlesCount(self, value):
        self._setNumber(3, value)
        return

    def getWinRate(self):
        return self._getReal(4)

    def setWinRate(self, value):
        self._setReal(4, value)
        return

    def getWinsCount(self):
        return self._getNumber(5)

    def setWinsCount(self, value):
        self._setNumber(5, value)
        return

    def getLossCount(self):
        return self._getNumber(6)

    def setLossCount(self, value):
        self._setNumber(6, value)
        return

    def getDrawCount(self):
        return self._getNumber(7)

    def setDrawCount(self, value):
        self._setNumber(7, value)
        return

    def getAverageDamageDealt(self):
        return self._getReal(8)

    def setAverageDamageDealt(self, value):
        self._setReal(8, value)
        return

    def getAveragePrestige(self):
        return self._getReal(9)

    def setAveragePrestige(self, value):
        self._setReal(9, value)
        return

    def getRecordDamageDealt(self):
        return self._getReal(10)

    def setRecordDamageDealt(self, value):
        self._setReal(10, value)
        return

    def getRecordDamageDealtVehicleName(self):
        return self._getString(11)

    def setRecordDamageDealtVehicleName(self, value):
        self._setString(11, value)
        return

    def getRecordPrestige(self):
        return self._getReal(12)

    def setRecordPrestige(self, value):
        self._setReal(12, value)
        return

    def getRecordPrestigeVehicleName(self):
        return self._getString(13)

    def setRecordPrestigeVehicleName(self, value):
        self._setString(13, value)
        return

    def _initialize(self):
        super(StatisticsModel, self)._initialize()
        self._addNumberProperty(b'maxAchievedRatingPoints', 0)
        self._addNumberProperty(b'maxAchievedRank')
        self._addNumberProperty(b'soloBattlesCount', 0)
        self._addNumberProperty(b'superPlatoonBattlesCount', 0)
        self._addRealProperty(b'winRate', 0.0)
        self._addNumberProperty(b'winsCount', 0)
        self._addNumberProperty(b'lossCount', 0)
        self._addNumberProperty(b'drawCount', 0)
        self._addRealProperty(b'averageDamageDealt', 0.0)
        self._addRealProperty(b'averagePrestige', 0.0)
        self._addRealProperty(b'recordDamageDealt', 0.0)
        self._addStringProperty(b'recordDamageDealtVehicleName', b'')
        self._addRealProperty(b'recordPrestige', 0.0)
        self._addStringProperty(b'recordPrestigeVehicleName', b'')
        return
