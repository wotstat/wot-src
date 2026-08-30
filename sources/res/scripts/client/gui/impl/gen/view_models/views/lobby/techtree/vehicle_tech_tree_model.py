from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from gui.impl.gen.view_models.views.lobby.paragons.paragons_entry_point_view_model import ParagonsEntryPointViewModel
from gui.impl.gen.view_models.views.lobby.techtree.node_relation import NodeRelation
from gui.impl.gen.view_models.views.lobby.techtree.node_tech_tree_model import NodeTechTreeModel
from gui.impl.gen.view_models.views.lobby.techtree.paragons_unlocked_branch import ParagonsUnlockedBranch
from gui.impl.gen.view_models.views.lobby.techtree.tech_tree_buttons import TechTreeButtons
from gui.impl.gen.view_models.views.lobby.techtree.tech_tree_custom_hints_model import TechTreeCustomHintsModel
from gui.impl.gen.view_models.views.lobby.techtree.tech_tree_nation_model import TechTreeNationModel
from gui.impl.gen.view_models.views.lobby.techtree.tech_tree_settings import TechTreeSettings
from gui.impl.gen.view_models.views.lobby.techtree.vehicle_node_data import VehicleNodeData

class VehicleTechTreeModel(ViewModel):
    __slots__ = (b'onNationChange', b'goToCollectionVehicle', b'goToBlueprintView', b'buyVehicle', b'unlockVehicle', b'restoreVehicle', b'addVehicleToCompare', b'goToModulesTechTree', b'onBlueprintModeChanged', b'goToPremiumShop', b'goToNationChangeView', b'goToEarlyAccess', b'onTechTreeButtonPressed', b'onClose', b'onParagonsUnlockedBranchShown', b'onResetBranchShown')
    TECHTREE_VEHICLE_TOOLTIP = b'techtreeVehicleTooltip'
    VEHICLE_COLLECTOR_TOOLTIP = b'vehicleCollectorTooltip'
    BLUEPRINT_FRAGMENT_INFO = b'blueprintFragmentInfo'
    TECHTREE_NATION_TOOLTIP = b'techtreeNationTooltip'

    def __init__(self, properties=23, commands=16):
        super(VehicleTechTreeModel, self).__init__(properties=properties, commands=commands)
        return

    @property
    def hints(self):
        return self._getViewModel(0)

    @staticmethod
    def getHintsType():
        return TechTreeCustomHintsModel

    @property
    def settings(self):
        return self._getViewModel(1)

    @staticmethod
    def getSettingsType():
        return TechTreeSettings

    @property
    def paragonsEntryPoint(self):
        return self._getViewModel(2)

    @staticmethod
    def getParagonsEntryPointType():
        return ParagonsEntryPointViewModel

    def getAvailableNations(self):
        return self._getArray(3)

    def setAvailableNations(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getAvailableNationsType():
        return TechTreeNationModel

    def getSelectedNation(self):
        return self._getString(4)

    def setSelectedNation(self, value):
        self._setString(4, value)
        return

    def getEarlyAccessNation(self):
        return self._getString(5)

    def setEarlyAccessNation(self, value):
        self._setString(5, value)
        return

    def getIsCmpAvailable(self):
        return self._getBool(6)

    def setIsCmpAvailable(self, value):
        self._setBool(6, value)
        return

    def getHasCollectibleVehicles(self):
        return self._getBool(7)

    def setHasCollectibleVehicles(self, value):
        self._setBool(7, value)
        return

    def getIsBlueprintMode(self):
        return self._getBool(8)

    def setIsBlueprintMode(self, value):
        self._setBool(8, value)
        return

    def getIsBlueprintModeEnabled(self):
        return self._getBool(9)

    def setIsBlueprintModeEnabled(self, value):
        self._setBool(9, value)
        return

    def getUniversalBlueprintsCount(self):
        return self._getNumber(10)

    def setUniversalBlueprintsCount(self, value):
        self._setNumber(10, value)
        return

    def getNationBlueprintsCount(self):
        return self._getNumber(11)

    def setNationBlueprintsCount(self, value):
        self._setNumber(11, value)
        return

    def getIsEarlyAccessPaused(self):
        return self._getBool(12)

    def setIsEarlyAccessPaused(self, value):
        self._setBool(12, value)
        return

    def getIsEarlyAccessFirstTimeShown(self):
        return self._getBool(13)

    def setIsEarlyAccessFirstTimeShown(self, value):
        self._setBool(13, value)
        return

    def getIsParagonsResetBranchNeedToShow(self):
        return self._getBool(14)

    def setIsParagonsResetBranchNeedToShow(self, value):
        self._setBool(14, value)
        return

    def getIsParagonsEnabled(self):
        return self._getBool(15)

    def setIsParagonsEnabled(self, value):
        self._setBool(15, value)
        return

    def getEarlyAccessCurrentTokens(self):
        return self._getNumber(16)

    def setEarlyAccessCurrentTokens(self, value):
        self._setNumber(16, value)
        return

    def getClosePremiumPanelTrigger(self):
        return self._getReal(17)

    def setClosePremiumPanelTrigger(self, value):
        self._setReal(17, value)
        return

    def getNodes(self):
        return self._getArray(18)

    def setNodes(self, value):
        self._setArray(18, value)
        return

    @staticmethod
    def getNodesType():
        return NodeTechTreeModel

    def getNodesRelation(self):
        return self._getArray(19)

    def setNodesRelation(self, value):
        self._setArray(19, value)
        return

    @staticmethod
    def getNodesRelationType():
        return NodeRelation

    def getVehiclesData(self):
        return self._getArray(20)

    def setVehiclesData(self, value):
        self._setArray(20, value)
        return

    @staticmethod
    def getVehiclesDataType():
        return VehicleNodeData

    def getParagonsUnlockedBranchesToShow(self):
        return self._getArray(21)

    def setParagonsUnlockedBranchesToShow(self, value):
        self._setArray(21, value)
        return

    @staticmethod
    def getParagonsUnlockedBranchesToShowType():
        return ParagonsUnlockedBranch

    def getTechTreeButtons(self):
        return self._getArray(22)

    def setTechTreeButtons(self, value):
        self._setArray(22, value)
        return

    @staticmethod
    def getTechTreeButtonsType():
        return TechTreeButtons

    def _initialize(self):
        super(VehicleTechTreeModel, self)._initialize()
        self._addViewModelProperty(b'hints', TechTreeCustomHintsModel())
        self._addViewModelProperty(b'settings', TechTreeSettings())
        self._addViewModelProperty(b'paragonsEntryPoint', ParagonsEntryPointViewModel())
        self._addArrayProperty(b'availableNations', Array())
        self._addStringProperty(b'selectedNation', b'')
        self._addStringProperty(b'earlyAccessNation', b'')
        self._addBoolProperty(b'isCmpAvailable', False)
        self._addBoolProperty(b'hasCollectibleVehicles', False)
        self._addBoolProperty(b'isBlueprintMode', False)
        self._addBoolProperty(b'isBlueprintModeEnabled', False)
        self._addNumberProperty(b'universalBlueprintsCount', 0)
        self._addNumberProperty(b'nationBlueprintsCount', 0)
        self._addBoolProperty(b'isEarlyAccessPaused', False)
        self._addBoolProperty(b'isEarlyAccessFirstTimeShown', False)
        self._addBoolProperty(b'isParagonsResetBranchNeedToShow', False)
        self._addBoolProperty(b'isParagonsEnabled', False)
        self._addNumberProperty(b'earlyAccessCurrentTokens', 0)
        self._addRealProperty(b'closePremiumPanelTrigger', 0.0)
        self._addArrayProperty(b'nodes', Array())
        self._addArrayProperty(b'nodesRelation', Array())
        self._addArrayProperty(b'vehiclesData', Array())
        self._addArrayProperty(b'paragonsUnlockedBranchesToShow', Array())
        self._addArrayProperty(b'techTreeButtons', Array())
        self.onNationChange = self._addCommand(b'onNationChange')
        self.goToCollectionVehicle = self._addCommand(b'goToCollectionVehicle')
        self.goToBlueprintView = self._addCommand(b'goToBlueprintView')
        self.buyVehicle = self._addCommand(b'buyVehicle')
        self.unlockVehicle = self._addCommand(b'unlockVehicle')
        self.restoreVehicle = self._addCommand(b'restoreVehicle')
        self.addVehicleToCompare = self._addCommand(b'addVehicleToCompare')
        self.goToModulesTechTree = self._addCommand(b'goToModulesTechTree')
        self.onBlueprintModeChanged = self._addCommand(b'onBlueprintModeChanged')
        self.goToPremiumShop = self._addCommand(b'goToPremiumShop')
        self.goToNationChangeView = self._addCommand(b'goToNationChangeView')
        self.goToEarlyAccess = self._addCommand(b'goToEarlyAccess')
        self.onTechTreeButtonPressed = self._addCommand(b'onTechTreeButtonPressed')
        self.onClose = self._addCommand(b'onClose')
        self.onParagonsUnlockedBranchShown = self._addCommand(b'onParagonsUnlockedBranchShown')
        self.onResetBranchShown = self._addCommand(b'onResetBranchShown')
        return
