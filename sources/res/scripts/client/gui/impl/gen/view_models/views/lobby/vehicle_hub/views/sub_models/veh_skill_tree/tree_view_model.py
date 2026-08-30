from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.node_model import NodeModel
from gui.impl.gen.view_models.views.lobby.vehicle_hub.views.sub_models.veh_skill_tree.path_model import PathModel

class ResearchAvailability(Enum):
    NOT_IN_INVENTORY = b'notInInventory'
    NOT_ENOUGH_EXP = b'notEnoughExp'
    IN_BATTLE = b'inBattle'
    IN_FORMATION = b'inFormation'
    NEEDS_REPAIR = b'needsRepair'
    AVAILABLE = b'researchAvailable'
    EMERGENCY_MODE_ENABLED = b'emergencyModeEnabled'
    RESEARCH_IN_PROGRESS = b'researchInProgress'


class TreeViewModel(ViewModel):
    __slots__ = (b'onResearch', b'onShowNodeConfigurationWindow', b'onSelectNode', b'onFinalNodeResearchAnimationFinished')

    def __init__(self, properties=9, commands=4):
        super(TreeViewModel, self).__init__(properties=properties, commands=commands)
        return

    def getResearchedPerks(self):
        return self._getArray(0)

    def setResearchedPerks(self, value):
        self._setArray(0, value)
        return

    @staticmethod
    def getResearchedPerksType():
        return int

    def getNodes(self):
        return self._getArray(1)

    def setNodes(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getNodesType():
        return NodeModel

    def getPaths(self):
        return self._getArray(2)

    def setPaths(self, value):
        self._setArray(2, value)
        return

    @staticmethod
    def getPathsType():
        return Array[PathModel]

    def getRootNodeId(self):
        return self._getNumber(3)

    def setRootNodeId(self, value):
        self._setNumber(3, value)
        return

    def getRootNodeUiId(self):
        return self._getNumber(4)

    def setRootNodeUiId(self, value):
        self._setNumber(4, value)
        return

    def getResearchAvailability(self):
        return ResearchAvailability(self._getString(5))

    def setResearchAvailability(self, value):
        self._setString(5, value.value)
        return

    def getLockedTree(self):
        return self._getBool(6)

    def setLockedTree(self, value):
        self._setBool(6, value)
        return

    def getIsProgressionCompleted(self):
        return self._getBool(7)

    def setIsProgressionCompleted(self, value):
        self._setBool(7, value)
        return

    def getIsPrestigeGlareShown(self):
        return self._getBool(8)

    def setIsPrestigeGlareShown(self, value):
        self._setBool(8, value)
        return

    def _initialize(self):
        super(TreeViewModel, self)._initialize()
        self._addArrayProperty(b'researchedPerks', Array())
        self._addArrayProperty(b'nodes', Array())
        self._addArrayProperty(b'paths', Array())
        self._addNumberProperty(b'rootNodeId', 0)
        self._addNumberProperty(b'rootNodeUiId', 0)
        self._addStringProperty(b'researchAvailability')
        self._addBoolProperty(b'lockedTree', False)
        self._addBoolProperty(b'isProgressionCompleted', False)
        self._addBoolProperty(b'isPrestigeGlareShown', False)
        self.onResearch = self._addCommand(b'onResearch')
        self.onShowNodeConfigurationWindow = self._addCommand(b'onShowNodeConfigurationWindow')
        self.onSelectNode = self._addCommand(b'onSelectNode')
        self.onFinalNodeResearchAnimationFinished = self._addCommand(b'onFinalNodeResearchAnimationFinished')
        return
