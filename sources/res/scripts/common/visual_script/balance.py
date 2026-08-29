import BigWorld, sys
from block import Meta, Block, InitParam, buildStrKeysValue
from slot_types import SLOT_TYPE, arrayOf
from type import VScriptStruct, VScriptStructField
from visual_script.misc import errorVScript, ASPECT, EDITOR_TYPE
import ResMgr, constants, nations, items.vehicles as iv
_dataSection = None
_gList = None

class VsePaths(object):

    def __enter__(self):
        if constants.IS_VS_EDITOR:
            self.prevArenaPath = constants.ARENA_TYPE_XML_PATH
            self.prevItemDefPath = constants.ITEM_DEFS_PATH
            self.prevTypeXMLType = iv._VEHICLE_TYPE_XML_PATH
            constants.ARENA_TYPE_XML_PATH = b'../../../res/%s/scripts/arena_defs/' % constants.GAME_ROOT_DIR_NAME
            constants.ITEM_DEFS_PATH = b'../../../res/%s/scripts/item_defs/' % constants.GAME_ROOT_DIR_NAME
            iv._VEHICLE_TYPE_XML_PATH = constants.ITEM_DEFS_PATH + b'vehicles/'
        return

    def __exit__(self, exc_type, exc_val, exc_tb):
        if constants.IS_VS_EDITOR:
            constants.ARENA_TYPE_XML_PATH = self.prevArenaPath
            constants.ITEM_DEFS_PATH = self.prevItemDefPath
            iv._VEHICLE_TYPE_XML_PATH = self.prevTypeXMLType
        return


def cache():
    if not iv.g_cache:
        with VsePaths():
            from items import init
            init(False, None)
            from items.vehicles import init
            init(False, None)
    return iv.g_cache


def getVehicleList(naton):
    if not iv.g_list:
        cache()
    return iv.g_list(naton)


def eqDataSection(eqName):
    global _dataSection
    if not _dataSection:
        if constants.IS_CELLAPP or constants.IS_CLIENT:
            xmlPath = constants.ITEM_DEFS_PATH
        else:
            xmlPath = b'../../../res/%s/scripts/item_defs/' % constants.GAME_ROOT_DIR_NAME
        xmlPath += b'vehicles/common/equipments.xml'
        _dataSection = ResMgr.openSection(xmlPath)
    ds = ResMgr.DataSection(eqName)
    ds.copy(_dataSection[eqName])
    return ds


def getArtefact(name):
    return cache().equipments()[cache().equipmentIDs()[name]]


class EquipmentMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 10512127

    @classmethod
    def blockCategory(cls):
        return b'Balance'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/arena'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.SERVER, ASPECT.CLIENT, ASPECT.HANGAR]


class ConfigParamStruct(VScriptStruct):
    name = VScriptStructField(b'name', SLOT_TYPE.STR)
    value = VScriptStructField(b'value', SLOT_TYPE.STR)

    def __repr__(self):
        return (b'ConfigParam(name = {}, value = {})').format(self.name, self.value)


class ReloadClientPlan(Block, EquipmentMeta):

    def __init__(self, *args, **kwargs):
        super(ReloadClientPlan, self).__init__(*args, **kwargs)
        self._inSlot = self._makeEventInputSlot(b'in', self._execute)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        if constants.IS_CELLAPP:

            def reloader(*args):
                for avatar in BigWorld.entities.valuesOfType(b'Avatar', 0):
                    if avatar.isClientConnected:
                        self._writeLog((b'send reload to client {}').format(avatar.id))
                        avatar.ownClient.showDevelopmentInfo(100, b'')

                return

            BigWorld.addTimer(reloader, 1.0)
        self._out.call()
        return


class ResMgrSpy(object):

    def __init__(self, block, params):
        self.spyParams = params
        self.__spyParamsPaths = []
        self.__block = block
        import sys
        sys.settrace(None)
        sys.settrace(self.traceCalls)
        return

    def stop(self):
        import sys
        sys.settrace(None)
        return

    def traceCalls(self, frame, event, arg):
        self.__traceCalls(frame, event)
        return self.traceCalls

    def __traceCalls(self, frame, event):
        if event != b'call':
            return
        co = frame.f_code
        if not co.co_name.startswith(b'read'):
            return
        l = frame.f_locals
        if b'section' not in l or b'subsectionName' not in l:
            return
        attr = self.__path(l[b'section']) + l[b'subsectionName']
        self.spyParams.discard(attr)
        return

    def __path(self, section):
        if section.name == b'script':
            return b''
        parent = section.parentSection()
        if not parent:
            return b''
        return self.__path(parent) + section.name + b'/'


class IntCompDescrDecoder(Block, EquipmentMeta):

    def __init__(self, *args, **kwargs):
        super(IntCompDescrDecoder, self).__init__(*args, **kwargs)
        self._intCDs = self._makeDataInputSlot(b'incCD', arrayOf(SLOT_TYPE.INT))
        return

    def captionText(self):
        return b'IntCD Decoder'

    def __parseCDs(self):
        cache()
        from items import vehicles, ITEM_TYPE_NAMES
        err = b''
        results = []
        for intCD in self._intCDs.getValue():
            try:
                itemTypeID, nationID, vehID = vehicles.parseIntCompactDescr(intCD)
                item = vehicles.getItemByCompactDescr(intCD)
            except Exception as e:
                err += (b'{}: {}\n').format(intCD, e)
                results.append(err)
                continue

            results.append((b'{} {} {}\n').format(intCD, (nations.NAMES[nationID], ITEM_TYPE_NAMES[itemTypeID], vehID), item.name))

        return (results, err)

    def _execute(self):
        return

    def validate(self):
        results, err = self.__parseCDs()
        for res in results:
            self._writeLog(res)

        return err


class EquipmentParams(Block, EquipmentMeta):

    def __init__(self, *args, **kwargs):
        super(EquipmentParams, self).__init__(*args, **kwargs)
        self.eqName, = self._getInitParams()
        self._inSlot = self._makeEventInputSlot(b'in', self._execute)
        self._params = self._makeDataInputSlot(b'Parameters', arrayOf(b'ConfigParamStruct'))
        self._out = self._makeEventOutputSlot(b'out')
        return

    def captionText(self):
        return self.eqName

    @classmethod
    def initParams(cls):
        return [
         InitParam(b'EquipmentName', SLOT_TYPE.STR, buildStrKeysValue(b'large_repairkit_battle_royale', b'regenerationKit', b'arcade_minefield_battle_royale', b'healPoint', b'selfBuff', b'trappoint', b'afterburning_battle_royale', b'repairpoint', b'arcade_bomber_battle_royale', b'spawn_kamikaze', b'arcade_smoke_battle_royale_with_damage', b'berserker', b'fireCircle', b'adaptationHealthRestore', b'corrodingShot', b'clingBrander', b'thunderStrike', b'shotPassion'), EDITOR_TYPE.STR_KEY_SELECTOR)]

    def _execute(self):
        self._writeLog((b'_execute {}').format(self._params.getValue()))
        errString = self._processParams()
        if errString:
            return errorVScript(self, errString)
        else:
            if constants.IS_CELLAPP:
                from items.vehicles import g_cache
                import InfluenceZone
                eqExtra = g_cache.commonConfig[b'extrasDict'].get(self.eqName)
                if eqExtra:
                    eqExtra._readConfig(None, None)
            self._out.call()
            return

    def validate(self):
        return self._processParams()

    def _processParams(self):
        if not self._params.getValue():
            return b''
        else:
            import sys
            self._writeLog((b'_processParams {}').format((self._params.getValue(), sys.executable)))
            spy = None
            try:
                try:
                    equipment = getArtefact(self.eqName)
                    equipmentSection = eqDataSection(self.eqName)
                    section = equipmentSection[b'script']
                    for param in self._params.getValue():
                        if not param.name:
                            continue
                        section.writeString(param.name, param.value)

                    if constants.IS_VS_EDITOR:
                        spy = ResMgrSpy(self, {param.name for param in self._params.getValue()})
                    equipment.init(None, equipmentSection)
                except Exception as e:
                    return (b'error {}').format(e)

            finally:
                if spy:
                    spy.stop()

            if spy and spy.spyParams:
                return (b'Were not read {}').format(spy.spyParams)
            return b''
