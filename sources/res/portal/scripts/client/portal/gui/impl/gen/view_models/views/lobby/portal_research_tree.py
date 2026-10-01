from frameworks.wulf import Array
from frameworks.wulf import ViewModel
from portal.gui.impl.gen.view_models.views.lobby.node_stage_model import NodeStageModel

class PortalResearchTree(ViewModel):
    __slots__ = ()

    def __init__(self, properties=4, commands=0):
        super(PortalResearchTree, self).__init__(properties=properties, commands=commands)
        return

    def getStageNumber(self):
        return self._getNumber(0)

    def setStageNumber(self, value):
        self._setNumber(0, value)
        return

    def getIsUnlocked(self):
        return self._getBool(1)

    def setIsUnlocked(self, value):
        self._setBool(1, value)
        return

    def getIsViewed(self):
        return self._getBool(2)

    def setIsViewed(self, value):
        self._setBool(2, value)
        return

    def getStageNodes(self):
        return self._getArray(3)

    def setStageNodes(self, value):
        self._setArray(3, value)
        return

    @staticmethod
    def getStageNodesType():
        return NodeStageModel

    def _initialize(self):
        super(PortalResearchTree, self)._initialize()
        self._addNumberProperty(b'stageNumber', 0)
        self._addBoolProperty(b'isUnlocked', False)
        self._addBoolProperty(b'isViewed', False)
        self._addArrayProperty(b'stageNodes', Array())
        return
