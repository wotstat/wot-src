class BattleRoyaleVehicleStats(object):
    __DAMAGE_DEALT = 0
    __XP = 1
    __SHOTS = 2
    __DIRECT_HITS = 3
    __DAMAGE_RECEIVED = 4
    __SURVIVED_BATTLES = 5
    __FRAGS = 6
    __MAX_XP = 7
    __MAX_DAMAGE_DEALT = 8
    __MAX_FRAGS = 9
    __END_INDEX = 10

    def __init__(self, rawData):
        self.__rawData = rawData
        self.__checkAndInitData()
        return

    def addShots(self, value):
        self.__rawData[b'brstats'][self.__SHOTS] += value
        return

    def addDirectHits(self, value):
        self.__rawData[b'brstats'][self.__DIRECT_HITS] += value
        return

    def addDamageReceived(self, value):
        self.__rawData[b'brstats'][self.__DAMAGE_RECEIVED] += value
        return

    def addSurvivedBattles(self, value):
        self.__rawData[b'brstats'][self.__SURVIVED_BATTLES] += value
        return

    def addXP(self, value):
        self.__rawData[b'brstats'][self.__XP] += value
        if value > self.__rawData[b'brstats'][self.__MAX_XP]:
            self.__rawData[b'brstats'][self.__MAX_XP] = value
        return

    def addDamageDealt(self, value):
        self.__rawData[b'brstats'][self.__DAMAGE_DEALT] += value
        if value > self.__rawData[b'brstats'][self.__MAX_DAMAGE_DEALT]:
            self.__rawData[b'brstats'][self.__MAX_DAMAGE_DEALT] = value
        return

    def addFrags(self, value):
        self.__rawData[b'brstats'][self.__FRAGS] += value
        if value > self.__rawData[b'brstats'][self.__MAX_FRAGS]:
            self.__rawData[b'brstats'][self.__MAX_FRAGS] = value
        return

    def getXP(self):
        return self.__rawData[b'brstats'][self.__XP]

    def getShotsCount(self):
        return self.__rawData[b'brstats'][self.__SHOTS]

    def getHitsCount(self):
        return self.__rawData[b'brstats'][self.__DIRECT_HITS]

    def getDamageReceived(self):
        return self.__rawData[b'brstats'][self.__DAMAGE_RECEIVED]

    def getDamageDealt(self):
        return self.__rawData[b'brstats'][self.__DAMAGE_DEALT]

    def getSurvivedBattlesCount(self):
        return self.__rawData[b'brstats'][self.__SURVIVED_BATTLES]

    def getFragsCount(self):
        return self.__rawData[b'brstats'][self.__FRAGS]

    def getMaxXp(self):
        return self.__rawData[b'brstats'][self.__MAX_XP]

    def getMaxFrags(self):
        return self.__rawData[b'brstats'][self.__MAX_FRAGS]

    def getMaxDamage(self):
        return self.__rawData[b'brstats'][self.__MAX_DAMAGE_DEALT]

    def _getAvgValue(self, allOccurs, effectiveOccurs):
        if allOccurs:
            return float(effectiveOccurs) / allOccurs
        return 0.0

    def getAvgDamageReceived(self):
        return self._getAvgValue(self.getBattlesCount(), self.getDamageReceived())

    def getAvgFrags(self):
        return self._getAvgValue(self.getBattlesCount(), self.getFragsCount())

    def getHitsEfficiency(self):
        return self._getAvgValue(self.getShotsCount(), self.getHitsCount())

    def getFragsEfficiency(self):
        return self._getAvgValue(self.getDeathsCount(), self.getFragsCount())

    def getDamageEfficiency(self):
        return self._getAvgValue(self.getDamageReceived(), self.getDamageDealt())

    def getBattlesCount(self):
        return self.getWinsCount() + self.getLossesCount()

    def getDeathsCount(self):
        return self.getBattlesCount() - self.getSurvivedBattlesCount()

    def getWinsCount(self):
        return self.__rawData[b'brplaces'].get(1, 0)

    def getLossesCount(self):
        return sum([count for place, count in self.__rawData[b'brplaces'].iteritems() if place != 1])

    def getAvgXP(self):
        return self._getAvgValue(self.getBattlesCount(), self.getXP())

    def getAvgDamage(self):
        return self._getAvgValue(self.getBattlesCount(), self.getDamageDealt())

    def getAveragePosition(self):
        return round(self._getAvgValue(self.getBattlesCount(), self.getPositionSum()), 1)

    def getAverageLevel(self):
        return round(self._getAvgValue(self.getBattlesCount(), self.getAchivedLevelSum()), 1)

    def getPositionSum(self):
        return sum([k * v for k, v in self.__rawData[b'brplaces'].iteritems()])

    def getAchivedLevelSum(self):
        return sum([k * v for k, v in self.__rawData[b'brlevels'].iteritems()])

    def incrementPlace(self, place):
        self.__rawData[b'brplaces'][place] = self.__rawData[b'brplaces'].get(place, 0) + 1
        return

    def incrementLevel(self, level):
        self.__rawData[b'brlevels'][level] = self.__rawData[b'brlevels'].get(level, 0) + 1
        return

    @property
    def places(self):
        return self.__rawData[b'brplaces']

    @property
    def levels(self):
        return self.__rawData[b'brlevels']

    @property
    def rawData(self):
        return self.__rawData

    def __checkAndInitData(self):
        if not self.__rawData:
            self.__rawData[b'brstats'] = []
            self.__rawData[b'brplaces'] = {}
            self.__rawData[b'brlevels'] = {}
        lengthStats = len(self.__rawData[b'brstats'])
        if lengthStats < self.__END_INDEX:
            self.__rawData[b'brstats'] += [0] * (self.__END_INDEX - lengthStats)
        return
