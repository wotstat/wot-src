from enum import Enum
from frameworks.wulf import Array, Map, ViewModel
from gui.impl.gen.view_models.views.lobby.common.router_model import RouterModel

class NationEnum(Enum):
    CHINA = b'china'
    CZECHOSLOVAKIA = b'czech'
    FRANCE = b'france'
    GERMANY = b'germany'
    ITALY = b'italy'
    JAPAN = b'japan'
    POLAND = b'poland'
    SWEDEN = b'sweden'
    UK = b'uk'
    USA = b'usa'
    USSR = b'ussr'


class TechTreeViewModel(ViewModel):
    __slots__ = (b'onOpenAboutVehicle', b'onAddToCompare', b'onOpenCollectableVehicles', b'onOpenPremiumShop')

    def __init__(self, properties=8, commands=4):
        super(TechTreeViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def router(self):
        return self._getViewModel(0)

    @staticmethod
    def getRouterType():
        return RouterModel

    def getFirstHighlightedLevel(self):
        return self._getNumber(1)

    def setFirstHighlightedLevel(self, value):
        self._setNumber(1, value)
        return

    def getShowWelcomeAnimation(self):
        return self._getBool(2)

    def setShowWelcomeAnimation(self, value):
        self._setBool(2, value)
        return

    def getCollectableVehiclesAvailable(self):
        return self._getBool(3)

    def setCollectableVehiclesAvailable(self, value):
        self._setBool(3, value)
        return

    def getSelectedNation(self):
        return NationEnum(self._getString(4))

    def setSelectedNation(self, value):
        self._setString(4, value.value)
        return

    def getAvailableNations(self):
        return self._getArray(5)

    def setAvailableNations(self, value):
        self._setArray(5, value)
        return

    @staticmethod
    def getAvailableNationsType():
        return NationEnum

    def getTechTreeNodes(self):
        return self._getMap(6)

    def setTechTreeNodes(self, value):
        self._setMap(6, value)
        return

    @staticmethod
    def getTechTreeNodesType():
        return (int, unicode)

    def getNodeOverrides(self):
        return self._getMap(7)

    def setNodeOverrides(self, value):
        self._setMap(7, value)
        return

    @staticmethod
    def getNodeOverridesType():
        return (int, unicode)

    def _initialize(self):
        super(TechTreeViewModel, self)._initialize()
        self._addViewModelProperty(b'router', RouterModel())
        self._addNumberProperty(b'firstHighlightedLevel', 10)
        self._addBoolProperty(b'showWelcomeAnimation', False)
        self._addBoolProperty(b'collectableVehiclesAvailable', False)
        self._addStringProperty(b'selectedNation', NationEnum.CZECHOSLOVAKIA.value)
        self._addArrayProperty(b'availableNations', Array())
        self._addMapProperty(b'techTreeNodes', Map(int, unicode))
        self._addMapProperty(b'nodeOverrides', Map(int, unicode))
        self.onOpenAboutVehicle = self._addCommand(b'onOpenAboutVehicle')
        self.onAddToCompare = self._addCommand(b'onAddToCompare')
        self.onOpenCollectableVehicles = self._addCommand(b'onOpenCollectableVehicles')
        self.onOpenPremiumShop = self._addCommand(b'onOpenPremiumShop')
        return
