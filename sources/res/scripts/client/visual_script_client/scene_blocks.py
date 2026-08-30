import BigWorld
from visual_script import ASPECT
from visual_script.block import Block
from visual_script.slot_types import SLOT_TYPE
from visual_script.arena_blocks import ArenaMeta
from material_kinds import EFFECT_MATERIAL_NAMES_BY_INDEXES, EFFECT_MATERIAL_INDEXES_BY_IDS

class GetSpaceId(Block, ArenaMeta):

    def __init__(self, *args, **kwargs):
        super(GetSpaceId, self).__init__(*args, **kwargs)
        self._spaceId = self._makeDataOutputSlot(b'spaceId', SLOT_TYPE.INT, GetSpaceId._execute)
        return

    def _execute(self):
        from Avatar import PlayerAvatar
        player = BigWorld.player()
        spaceID = player.spaceID if isinstance(player, PlayerAvatar) else player.hangarSpace.spaceID
        self._spaceId.setValue(spaceID)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.HANGAR]


class GetSpaceName(Block, ArenaMeta):

    def __init__(self, *args, **kwargs):
        super(GetSpaceName, self).__init__(*args, **kwargs)
        self._spaceName = self._makeDataOutputSlot(b'spaceName', SLOT_TYPE.STR, self._execute)
        return

    def _execute(self):
        from Avatar import PlayerAvatar
        player = BigWorld.player()
        if isinstance(player, PlayerAvatar):
            spaceName = player.arena.arenaType.geometryName
        else:
            spaceName = player.hangarSpace.spacePath.split(b'/')[-1]
        self._spaceName.setValue(spaceName)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.HANGAR]


class GetTerrainMaterialUnderPoint(Block, ArenaMeta):

    def __init__(self, *args, **kwargs):
        super(GetTerrainMaterialUnderPoint, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._spaceID = self._makeDataInputSlot(b'spaceID', SLOT_TYPE.INT)
        self._position = self._makeDataInputSlot(b'position', SLOT_TYPE.VECTOR3)
        self._dropDistance = self._makeDataInputSlot(b'dropDistance', SLOT_TYPE.FLOAT)
        self._out = self._makeEventOutputSlot(b'out')
        self._material = self._makeDataOutputSlot(b'material', SLOT_TYPE.STR, None)
        return

    def _execute(self):
        material = BigWorld.getMatInfoUnderPoint(self._spaceID.getValue(), self._position.getValue(), self._dropDistance.getValue())
        index = EFFECT_MATERIAL_INDEXES_BY_IDS.get(material)
        name = EFFECT_MATERIAL_NAMES_BY_INDEXES.get(index)
        if name is None:
            name = b'undefined'
        self._material.setValue(name)
        self._out.call()
        return


class TerrainIndexToName(Block, ArenaMeta):

    def __init__(self, *args, **kwargs):
        super(TerrainIndexToName, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._index = self._makeDataInputSlot(b'index', SLOT_TYPE.INT)
        self._out = self._makeEventOutputSlot(b'out')
        self._material = self._makeDataOutputSlot(b'material', SLOT_TYPE.STR, None)
        return

    def _execute(self):
        index = EFFECT_MATERIAL_INDEXES_BY_IDS.get(self._index.getValue())
        name = EFFECT_MATERIAL_NAMES_BY_INDEXES.get(index)
        if name is None:
            name = b'undefined'
        self._material.setValue(name)
        self._out.call()
        return
