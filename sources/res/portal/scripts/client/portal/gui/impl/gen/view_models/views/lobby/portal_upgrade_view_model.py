from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.portal_research_tree import PortalResearchTree
from portal.gui.impl.gen.view_models.views.lobby.portal_ttx_item_model import PortalTtxItemModel
from portal.gui.impl.gen.view_models.views.lobby.portal_upgrade_vehicle_item_model import PortalUpgradeVehicleItemModel

class PortalUpgradeViewModel(ViewModel):
    __slots__ = (b'onClose', b'onAboutImprovements', b'onReset', b'onNodeSelect', b'onNodeReset', b'onMoveSpace', b'onStartMoving', b'onNodeUpgrade', b'onNextVehicleClick', b'onPrevVehicleClick', b'onStageHovered')

    def __init__(self, properties=7, commands=11):
        super(PortalUpgradeViewModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def currentVehicle(self):
        return self._getViewModel(0)

    @staticmethod
    def getCurrentVehicleType():
        return PortalUpgradeVehicleItemModel

    def getTtx(self):
        return self._getArray(1)

    def setTtx(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getTtxType():
        return PortalTtxItemModel

    def getResearchTree(self):
        return self._getArray(2)

    def setResearchTree(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getResearchTreeType():
        return PortalResearchTree

    def getIncompatibleModules(self):
        return self._getArray(3)

    def setIncompatibleModules(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getIncompatibleModulesType():
        return unicode

    def getUpgradeAvailable(self):
        return self._getBool(4)

    def setUpgradeAvailable(self, value):
        self._setBool(4, value)
        return

    def getIsFirstEnter(self):
        return self._getBool(5)

    def setIsFirstEnter(self, value):
        self._setBool(5, value)
        return

    def getIsMaxLevelAchieved(self):
        return self._getBool(6)

    def setIsMaxLevelAchieved(self, value):
        self._setBool(6, value)
        return

    def _initialize(self):
        super(PortalUpgradeViewModel, self)._initialize()
        self._addViewModelProperty(b'currentVehicle', PortalUpgradeVehicleItemModel())
        self._addArrayProperty(b'ttx', Array())
        self._addArrayProperty(b'researchTree', Array())
        self._addArrayProperty(b'incompatibleModules', Array())
        self._addBoolProperty(b'upgradeAvailable', False)
        self._addBoolProperty(b'isFirstEnter', False)
        self._addBoolProperty(b'isMaxLevelAchieved', False)
        self.onClose = self._addCommand(b'onClose')
        self.onAboutImprovements = self._addCommand(b'onAboutImprovements')
        self.onReset = self._addCommand(b'onReset')
        self.onNodeSelect = self._addCommand(b'onNodeSelect')
        self.onNodeReset = self._addCommand(b'onNodeReset')
        self.onMoveSpace = self._addCommand(b'onMoveSpace')
        self.onStartMoving = self._addCommand(b'onStartMoving')
        self.onNodeUpgrade = self._addCommand(b'onNodeUpgrade')
        self.onNextVehicleClick = self._addCommand(b'onNextVehicleClick')
        self.onPrevVehicleClick = self._addCommand(b'onPrevVehicleClick')
        self.onStageHovered = self._addCommand(b'onStageHovered')
        return
