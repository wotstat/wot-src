from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.lootbox_system.submodels.rewards_categories_model import RewardsCategoriesModel

class StatisticsModel(ViewModel):
    __slots__ = (b'onReset', b'onUpdateResetState')

    def __init__(self, properties=5, commands=2):
        super(StatisticsModel, self).__init__(properties=properties, commands=commands)
        return

    def getEventName(self):
        return self._getString(0)

    def setEventName(self, value):
        self._setString(0, value)
        return

    def getOpenedCount(self):
        return self._getNumber(1)

    def setOpenedCount(self, value):
        self._setNumber(1, value)
        return

    def getIsResetCompleted(self):
        return self._getBool(2)

    def setIsResetCompleted(self, value):
        self._setBool(2, value)
        return

    def getCategories(self):
        return self._getArray(3)

    def setCategories(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getCategoriesType():
        return RewardsCategoriesModel

    def getPluginPath(self):
        return self._getString(4)

    def setPluginPath(self, value):
        self._setString(4, value)
        return

    def _initialize(self):
        super(StatisticsModel, self)._initialize()
        self._addStringProperty(b'eventName', b'')
        self._addNumberProperty(b'openedCount', 0)
        self._addBoolProperty(b'isResetCompleted', False)
        self._addArrayProperty(b'categories', Array())
        self._addStringProperty(b'pluginPath', b'')
        self.onReset = self._addCommand(b'onReset')
        self.onUpdateResetState = self._addCommand(b'onUpdateResetState')
        return
