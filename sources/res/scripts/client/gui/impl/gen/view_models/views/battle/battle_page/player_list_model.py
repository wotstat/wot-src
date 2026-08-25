from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.battle_player import BattlePlayer

class PlayerListModel(ViewModel):
    __slots__ = (b'onPlatoonInvite', b'onPlayerCommend')

    def __init__(self, properties=9, commands=2):
        super(PlayerListModel, self).__init__(properties=properties, commands=commands)
        return

    def getIsColorblind(self):
        return self._getBool(0)

    def setIsColorblind(self, value):
        self._setBool(0, value)
        return

    def getIsFogOfWarEnabled(self):
        return self._getBool(1)

    def setIsFogOfWarEnabled(self, value):
        self._setBool(1, value)
        return

    def getIsCommendationEnabled(self):
        return self._getBool(2)

    def setIsCommendationEnabled(self, value):
        self._setBool(2, value)
        return

    def getIsLiveTagsEnabled(self):
        return self._getBool(3)

    def setIsLiveTagsEnabled(self, value):
        self._setBool(3, value)
        return

    def getIsAnonymized(self):
        return self._getBool(4)

    def setIsAnonymized(self, value):
        self._setBool(4, value)
        return

    def getHasClan(self):
        return self._getBool(5)

    def setHasClan(self, value):
        self._setBool(5, value)
        return

    def getPlatoonsEnabled(self):
        return self._getBool(6)

    def setPlatoonsEnabled(self, value):
        self._setBool(6, value)
        return

    def getAllies(self):
        return self._getArray(7)

    def setAllies(self, value):
        self._setArray(7, value)
        return

    @staticmethod
    def getAlliesType():
        return BattlePlayer

    def getEnemies(self):
        return self._getArray(8)

    def setEnemies(self, value):
        self._setArray(8, value)
        return

    @staticmethod
    def getEnemiesType():
        return BattlePlayer

    def _initialize(self):
        super(PlayerListModel, self)._initialize()
        self._addBoolProperty(b'isColorblind', False)
        self._addBoolProperty(b'isFogOfWarEnabled', False)
        self._addBoolProperty(b'isCommendationEnabled', False)
        self._addBoolProperty(b'isLiveTagsEnabled', False)
        self._addBoolProperty(b'isAnonymized', False)
        self._addBoolProperty(b'hasClan', False)
        self._addBoolProperty(b'platoonsEnabled', False)
        self._addArrayProperty(b'allies', Array())
        self._addArrayProperty(b'enemies', Array())
        self.onPlatoonInvite = self._addCommand(b'onPlatoonInvite')
        self.onPlayerCommend = self._addCommand(b'onPlayerCommend')
        return
