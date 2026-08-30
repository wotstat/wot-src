import Math
from soft_exception import SoftException
from visual_script.block import Meta, Block, InitParam, buildStrKeysValue
from visual_script.misc import errorVScript, ASPECT, EDITOR_TYPE
from visual_script.slot_types import SLOT_TYPE, arrayOf

class ArenaMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 10512127

    @classmethod
    def blockCategory(cls):
        return b'Arena'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/arena'


class GetUDOByNameBase(Block, ArenaMeta):
    _UDOTypes = []

    def __init__(self, *args, **kwargs):
        super(GetUDOByNameBase, self).__init__(*args, **kwargs)
        self._nameType, self._type, self._exclude = self._getInitParams()
        if self._nameType == b'single name':
            self._name = self._makeDataInputSlot(b'name', SLOT_TYPE.STR)
        elif self._nameType == b'multiple names':
            self._names = self._makeDataInputSlot(b'names', arrayOf(SLOT_TYPE.STR))
        elif self._nameType == b'any names':
            pass
        else:
            errorVScript(self, b'Unsupported name reference')
        self._UDOs = self._makeDataOutputSlot(self._type + b's', arrayOf(self._type), self._getAll)
        self._firstUDO = self._makeDataOutputSlot(b'first' + self._type, self._type, self._getFirst)
        return

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'UDO names', SLOT_TYPE.STR, buildStrKeysValue(b'single name', b'multiple names', b'any names'), EDITOR_TYPE.STR_KEY_SELECTOR),
         InitParam(b'UDO type', SLOT_TYPE.STR, buildStrKeysValue(*cls._UDOTypes), EDITOR_TYPE.STR_KEY_SELECTOR),
         InitParam(b'Exclude Names', SLOT_TYPE.BOOL, False)]

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/rubic'

    def captionText(self):
        if self._nameType == b'any names':
            return b'Get UDO'
        else:
            if self._exclude:
                return b'Get UDO Excluding Name'
            return b'Get UDO By Name'

        return

    def _getAll(self):
        self._UDOs.setValue(self._allValidUDOs())
        return

    def _getFirst(self):
        udos = self._allValidUDOs()
        if udos:
            self._firstUDO.setValue(self._allValidUDOs()[0])
        else:
            raise SoftException(b"GetUDOByName block can't find a referred UDO by it name")
        return

    def _getUDOsOfType(self, typeName):
        raise SoftException(b'Using the base GetUDOByNameBase class directly')
        return

    def _allValidUDOs(self):
        allUDOs = self._getUDOsOfType(self._type)
        if self._nameType == b'single name':
            names = [
             self._name.getValue()]
        elif self._nameType == b'multiple names':
            names = self._names.getValue()
        else:
            if self._nameType == b'any names':
                return allUDOs
            else:
                return []

        if self._exclude:
            return [udo for udo in allUDOs if udo.name not in names]
        return [udo for udo in allUDOs if udo.name in names]


class GetDataFromStorageBase(Block, ArenaMeta):

    def __init__(self, *args, **kwargs):
        super(GetDataFromStorageBase, self).__init__(*args, **kwargs)
        self.componentName, self._valueType = self._getInitParams()
        self.componentSlot = self._makeDataInputSlot(b'componentProperty', SLOT_TYPE.STR)
        self.componentSlot.setDefaultValue(self.componentName)
        if self.componentName == b'globalGoal':
            self._keySlot = self._makeDataInputSlot(b'key', SLOT_TYPE.STR)
        if self._valueType == SLOT_TYPE.STR:
            self._valueSlot = self._makeDataOutputSlot(b'value', SLOT_TYPE.STR, self._exec)
        elif self._valueType == SLOT_TYPE.INT:
            self._valueSlot = self._makeDataOutputSlot(b'value', SLOT_TYPE.INT, self._exec)
        elif self._valueType == SLOT_TYPE.FLOAT:
            self._valueSlot = self._makeDataOutputSlot(b'value', SLOT_TYPE.FLOAT, self._exec)
        return

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'Component property name', SLOT_TYPE.STR, buildStrKeysValue(b'globalGoal'), EDITOR_TYPE.STR_KEY_SELECTOR),
         InitParam(b'Value Types', SLOT_TYPE.STR, buildStrKeysValue(SLOT_TYPE.STR, SLOT_TYPE.FLOAT, SLOT_TYPE.INT), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def _exec(self):
        storage = self.arena.arenaInfo.mapsTrainingStorageComponent
        if self.componentName == b'globalGoal':
            self._valueSlot.setValue(storage.getGlobalGoal(self._keySlot.getValue()))
        return


class GetFlyDirection(Block, ArenaMeta):

    def __init__(self, *args, **kwargs):
        super(GetFlyDirection, self).__init__(*args, **kwargs)
        self._arena = self._makeDataInputSlot(b'arena', SLOT_TYPE.ARENA)
        self._teamID = self._makeDataInputSlot(b'teamID', SLOT_TYPE.INT)
        self._res = self._makeDataOutputSlot(b'flyDirection', SLOT_TYPE.VECTOR3, self._exec)
        return

    @classmethod
    def blockAspects(cls):
        return [ASPECT.CLIENT, ASPECT.SERVER]

    def _exec(self):
        arena = self._arena.getValue()
        teamID = self._teamID.getValue()
        direction = None
        arenaType = arena.arenaType
        reconSettings = getattr(arenaType, b'recon')
        if reconSettings is not None:
            direction = reconSettings.flyDirections.get(teamID)
        if direction is None:
            errorVScript(self, (b'Missing flyDirection for arena [geometryName={}, gameplayName={}]; teamID={}').format(arenaType.geometryName, arenaType.gameplayName, teamID))
            direction = Math.Vector3(1.0, 0.0, 0.0)
        self._res.setValue(direction)
        return
