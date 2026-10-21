from enum import Enum
from frameworks.wulf import ViewModel

class NodeStatus(Enum):
    LOCKED = b'locked'
    AVAILABLE = b'available'
    NOT_ENOUGH_POINTS = b'notEnoughPoints'
    LEARNED = b'learned'
    NEED_TO_LEARN = b'needToLearn'
    SKIPPED = b'skipped'


class ItemType(Enum):
    GUN = b'vehicleGun'
    ENGINE = b'vehicleEngine'
    TURRET = b'vehicleTurret'
    HULL = b'vehicleChassis'
    DAMAGEBONUS = b'damageBonus'
    KDBONUS = b'kdBonus'
    SMALLMOBILITYBONUS = b'smallMobilityBonus'
    SMALLKDBONUS = b'smallKDBonus'
    NONE = b'none'


class ItemModifier(Enum):
    DAMAGEGUN = b'damageGun'
    QUICKFIREGUN = b'quickfireGun'
    DRUMGUN = b'drumGun'
    DUALGUN = b'dualGun'
    MAGAZINERELOADINGGUN = b'magazineReloadingGun'
    FASTHULL = b'fastHull'
    HPHULL = b'hpHull'
    ARMOREDHULL = b'armoredHull'
    FASTTURRET = b'fastTurret'
    HPTURRET = b'hpTurret'
    FASTENGINE = b'fastEngine'
    POWERENGINE = b'powerEngine'
    NONE = b'none'


class NodeType(Enum):
    MODULE = b'module'
    VEHICLEMODIFIER = b'vehicleModifier'
    ABILITY = b'ability'


class NodeStageModel(ViewModel):
    __slots__ = ()

    def __init__(self, properties=7, commands=0):
        super(NodeStageModel, self).__init__(properties=properties, commands=commands)
        return

    def getId(self):
        return self._getNumber(0)

    def setId(self, value):
        self._setNumber(0, value)
        return

    def getName(self):
        return self._getString(1)

    def setName(self, value):
        self._setString(1, value)
        return

    def getPointsToOpen(self):
        return self._getNumber(2)

    def setPointsToOpen(self, value):
        self._setNumber(2, value)
        return

    def getItemType(self):
        return ItemType(self._getString(3))

    def setItemType(self, value):
        self._setString(3, value.value)
        return

    def getItemModifier(self):
        return ItemModifier(self._getString(4))

    def setItemModifier(self, value):
        self._setString(4, value.value)
        return

    def getNodeType(self):
        return NodeType(self._getString(5))

    def setNodeType(self, value):
        self._setString(5, value.value)
        return

    def getNodeStatus(self):
        return NodeStatus(self._getString(6))

    def setNodeStatus(self, value):
        self._setString(6, value.value)
        return

    def _initialize(self):
        super(NodeStageModel, self)._initialize()
        self._addNumberProperty(b'id', 0)
        self._addStringProperty(b'name', b'')
        self._addNumberProperty(b'pointsToOpen', 0)
        self._addStringProperty(b'itemType')
        self._addStringProperty(b'itemModifier')
        self._addStringProperty(b'nodeType')
        self._addStringProperty(b'nodeStatus')
        return
