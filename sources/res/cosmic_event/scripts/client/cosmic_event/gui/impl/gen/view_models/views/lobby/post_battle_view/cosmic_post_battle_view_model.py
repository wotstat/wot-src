from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from cosmic_event.gui.impl.gen.view_models.views.lobby.post_battle_view.cosmic_daily_missions import CosmicDailyMissions
from cosmic_event.gui.impl.gen.view_models.views.lobby.post_battle_view.player_entry import PlayerEntry

class CosmicPostBattleViewModel(ViewModel):
    __slots__ = (b'onClose',)

    def __init__(self, properties=9, commands=1):
        super(CosmicPostBattleViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentPlayerEntry(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentPlayerEntryType():
        return PlayerEntry

    def getBattleOverTimestamp(self):
        return self._getNumber(1)

    def setBattleOverTimestamp(self, value):
        self._setNumber(1, value)
        return

    def getTotalPoints(self):
        return self._getNumber(2)

    def setTotalPoints(self, value):
        self._setNumber(2, value)
        return

    def getLootResearch(self):
        return self._getNumber(3)

    def setLootResearch(self, value):
        self._setNumber(3, value)
        return

    def getKillAmount(self):
        return self._getNumber(4)

    def setKillAmount(self, value):
        self._setNumber(4, value)
        return

    def getKillStreak(self):
        return self._getNumber(5)

    def setKillStreak(self, value):
        self._setNumber(5, value)
        return

    def getPlayersList(self):
        return self._getArray(6)

    def setPlayersList(self, value):
        self._setArray(6, value)
        return

    @staticmethod
    def getPlayersListType():
        return PlayerEntry

    def getDailyQuests(self):
        return self._getArray(7)

    def setDailyQuests(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getDailyQuestsType():
        return CosmicDailyMissions

    def getHasDailyQuests(self):
        return self._getBool(8)

    def setHasDailyQuests(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(CosmicPostBattleViewModel, self)._initialize()
        self._addViewModelProperty(b'currentPlayerEntry', PlayerEntry())
        self._addNumberProperty(b'battleOverTimestamp', 0)
        self._addNumberProperty(b'totalPoints', 0)
        self._addNumberProperty(b'lootResearch', 0)
        self._addNumberProperty(b'killAmount', 0)
        self._addNumberProperty(b'killStreak', 0)
        self._addArrayProperty(b'playersList', Array())
        self._addArrayProperty(b'dailyQuests', Array())
        self._addBoolProperty(b'hasDailyQuests', False)
        self.onClose = self._addCommand(b'onClose')
        return
