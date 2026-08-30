from enum import Enum
from frameworks.wulf import Array, ViewModel
from gui.impl.gen.view_models.common.missions.bonuses.bonus_model import BonusModel

class NodeType(Enum):
    START = b'start'
    SMALL = b'small'
    MEDIUM = b'medium'
    LARGE = b'large'
    LOCKED = b'locked'


class JmNodeModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=15, commands=0):
        super(JmNodeModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getString(0)

    def setId(self, value):
        self._setString(0, value)
        return

    def getNextNodeIds(self):
        return self._getArray(1)

    def setNextNodeIds(self, value):
        self._setArray(1, value)
        return

    @staticmethod
    def getNextNodeIdsType():
        return unicode

    def getNodeType(self):
        return NodeType(self._getString(2))

    def setNodeType(self, value):
        self._setString(2, value.value)
        return

    def getIsExplored(self):
        return self._getBool(3)

    def setIsExplored(self, value):
        self._setBool(3, value)
        return

    def getPosX(self):
        return self._getNumber(4)

    def setPosX(self, value):
        self._setNumber(4, value)
        return

    def getPosY(self):
        return self._getNumber(5)

    def setPosY(self, value):
        self._setNumber(5, value)
        return

    def getHasLore(self):
        return self._getBool(6)

    def setHasLore(self, value):
        self._setBool(6, value)
        return

    def getLoreX(self):
        return self._getNumber(7)

    def setLoreX(self, value):
        self._setNumber(7, value)
        return

    def getLoreY(self):
        return self._getNumber(8)

    def setLoreY(self, value):
        self._setNumber(8, value)
        return

    def getLoreVisited(self):
        return self._getBool(9)

    def setLoreVisited(self, value):
        self._setBool(9, value)
        return

    def getPrice(self):
        return self._getNumber(10)

    def setPrice(self, value):
        self._setNumber(10, value)
        return

    def getBonuses(self):
        return self._getArray(11)

    def setBonuses(self, value):
        self._setArray(11, value)
        return

    @staticmethod
    def getBonusesType():
        return BonusModel

    def getPathFromCurrentNode(self):
        return self._getArray(12)

    def setPathFromCurrentNode(self, value):
        self._setArray(12, value)
        return

    @staticmethod
    def getPathFromCurrentNodeType():
        return unicode

    def getCanAfford(self):
        return self._getBool(13)

    def setCanAfford(self, value):
        self._setBool(13, value)
        return

    def getHasFullscreenReward(self):
        return self._getBool(14)

    def setHasFullscreenReward(self, value):
        self._setBool(14, value)
        return

    def _initialize(self):
        super(JmNodeModel, self)._initialize()
        self._addStringProperty(b'id', b'')
        self._addArrayProperty(b'nextNodeIds', Array())
        self._addStringProperty(b'nodeType')
        self._addBoolProperty(b'isExplored', False)
        self._addNumberProperty(b'posX', 0)
        self._addNumberProperty(b'posY', 0)
        self._addBoolProperty(b'hasLore', False)
        self._addNumberProperty(b'loreX', 0)
        self._addNumberProperty(b'loreY', 0)
        self._addBoolProperty(b'loreVisited', False)
        self._addNumberProperty(b'price', 0)
        self._addArrayProperty(b'bonuses', Array())
        self._addArrayProperty(b'pathFromCurrentNode', Array())
        self._addBoolProperty(b'canAfford', False)
        self._addBoolProperty(b'hasFullscreenReward', False)
        return
