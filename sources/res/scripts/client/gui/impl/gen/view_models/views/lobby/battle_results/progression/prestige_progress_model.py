from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.prestige.prestige_emblem_model import PrestigeEmblemModel

class PrestigeProgressModel(ViewModel):
    __slots__ = (b'onNavigate',)
    PATH = b'coui://gui/gameface/_dist/production/mono/plugins/post_battle/elite_system/elite_system.js'

    def __init__(self, properties=11, commands=1):
        super(PrestigeProgressModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentPrestigeEmblemModel(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentPrestigeEmblemModelType():
        return PrestigeEmblemModel

    @property
    def oldPrestigeEmblemModel(self):
        return self._getViewModel(1)

    @staticmethod
    def getOldPrestigeEmblemModelType():
        return PrestigeEmblemModel

    def getVehCD(self):
        return self._getNumber(2)

    def setVehCD(self, value):
        self._setNumber(2, value)
        return

    def getOldLvl(self):
        return self._getNumber(3)

    def setOldLvl(self, value):
        self._setNumber(3, value)
        return

    def getNewLvl(self):
        return self._getNumber(4)

    def setNewLvl(self, value):
        self._setNumber(4, value)
        return

    def getCurrentXP(self):
        return self._getNumber(5)

    def setCurrentXP(self, value):
        self._setNumber(5, value)
        return

    def getCurrentNextLevelXP(self):
        return self._getNumber(6)

    def setCurrentNextLevelXP(self, value):
        self._setNumber(6, value)
        return

    def getOldXP(self):
        return self._getNumber(7)

    def setOldXP(self, value):
        self._setNumber(7, value)
        return

    def getOldNextLvlXP(self):
        return self._getNumber(8)

    def setOldNextLvlXP(self, value):
        self._setNumber(8, value)
        return

    def getGainedXP(self):
        return self._getNumber(9)

    def setGainedXP(self, value):
        self._setNumber(9, value)
        return

    def getIsNavigationEnabled(self):
        return self._getBool(10)

    def setIsNavigationEnabled(self, value):
        self._setBool(10, value)
        return

    def _initialize(self):
        super(PrestigeProgressModel, self)._initialize()
        self._addViewModelProperty(b'currentPrestigeEmblemModel', PrestigeEmblemModel())
        self._addViewModelProperty(b'oldPrestigeEmblemModel', PrestigeEmblemModel())
        self._addNumberProperty(b'vehCD', 0)
        self._addNumberProperty(b'oldLvl', 0)
        self._addNumberProperty(b'newLvl', 0)
        self._addNumberProperty(b'currentXP', 0)
        self._addNumberProperty(b'currentNextLevelXP', 0)
        self._addNumberProperty(b'oldXP', 0)
        self._addNumberProperty(b'oldNextLvlXP', 0)
        self._addNumberProperty(b'gainedXP', 0)
        self._addBoolProperty(b'isNavigationEnabled', False)
        self.onNavigate = self._addCommand(b'onNavigate')
        return
