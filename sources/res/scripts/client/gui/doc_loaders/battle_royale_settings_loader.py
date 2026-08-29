import logging
from collections import namedtuple
import typing
from ResMgr import DataSection
import resource_helper
from battle_royale.gui.constants import ParamTypes
from gui.impl import backport
from gui.impl.gen import R
from soft_exception import SoftException
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.vehicle_modules import VehicleModule
_BATTLE_ROYALE_CONFIG_XML_PATH = b'gui/battle_royale_settings.xml'
_BATTLE_ROYALE_SETTINGS = None
_logger = logging.getLogger(__name__)
ModuleData = namedtuple(b'ModuleData', (b'titleText', b'icon', b'deltaParams', b'priorityParams', b'params', b'constParams'))
VehicleProperties = namedtuple(b'VehicleParameters', (b'strengths', b'weaknesses'))
_PriorityParameter = namedtuple(b'PriorityParameter', (b'name', b'type'))
_BRSettings = namedtuple(b'_BRSettings', (b'radar', b'spawn', b'techTree', b'vehicleProperties', b'upgradeAttentionTime', b'sounds'))
_SpawnSettings = namedtuple(b'_SpawnSettings', (b'selectEndingSoonTime',))
_SoundsSettings = namedtuple(b'_SoundsSettings', (b'finalEnemiesCount', b'middleAverageLevel'))
_TechTreeSettings = namedtuple(b'_TechTreeSettings', (b'modules', b'vehicleParams'))
_MarkerLifetimeSettings = namedtuple(b'_MarkerLifetimeSettings', (b'fadeIn', b'fadeOut', b'lifeTime'))
_RadarSettings = namedtuple(b'_RadarSettings', (b'marker',))
_AirdropSettings = namedtuple(b'_AirdropSettings', (b'marker',))

def _getModuleText(txtPath):
    treeTxt = R.strings.battle_royale.techtree.dyn(txtPath, None)
    if treeTxt is None:
        _logger.warning(b'Could not find text for %s', txtPath)
        return b''
    else:
        return backport.text(treeTxt())


def _readBattleRoyaleSettings():
    _, section = resource_helper.getRoot(_BATTLE_ROYALE_CONFIG_XML_PATH)
    result = _BRSettings(_readRadarSettings(section[b'radar']), _readSpawnSettings(section[b'spawn']), _readTechTreeSettings(section[b'techTree']), _readVehicleProperties(section[b'vehicleProperties']), section[b'upgradeAttentionTime'].asFloat, _readSoundSettings(section[b'sounds']))
    resource_helper.purgeResource(_BATTLE_ROYALE_CONFIG_XML_PATH)
    return result


def _readRadarSettings(section):
    return _RadarSettings(_readMarkerSettings(section))


def _readMarkerSettings(section):
    airdropSection = section[b'marker']
    return _MarkerLifetimeSettings(airdropSection[b'fadeIn'].asFloat, airdropSection[b'fadeOut'].asFloat, airdropSection[b'lifeTime'].asFloat)


def _readSpawnSettings(section):
    return _SpawnSettings(section[b'selectEndingSoonTime'].asFloat)


def _readSoundSettings(section):
    phases = section[b'battlePhases']
    return _SoundsSettings(phases[b'final'][b'enemiesCount'].asFloat, phases[b'middle'][b'averageLevel'].asFloat)


def _readVehicleProperties(section):
    allProperties = frozenset([subsection.asString for subsection in section[b'properties'].values()])
    vehicleProperties = {}
    for nation, properties in section[b'vehicles'].items():
        vehicleProperties[nation] = VehicleProperties(strengths=_parseProperties(properties[b'strengths'], allProperties), weaknesses=_parseProperties(properties[b'weaknesses'], allProperties))

    return vehicleProperties


def _parseProperties(section, allProperties):
    properties = section.asString.split(b' ')
    for vehProperty in properties:
        if vehProperty not in allProperties:
            raise SoftException(b'There is incorrect vehicle property "%s" in the battle royale settings' % vehProperty)

    return properties


def _readModuleParams(section, priorityParams, paramTypes):
    params = []
    for innerBlock in section.values():
        paramName = innerBlock.asString
        params.append(paramName)
        for attributeValue in innerBlock.values():
            if attributeValue.asString == b'1':
                priorityParams.append(_PriorityParameter(paramName, paramTypes))

    return params


def _readConstModuleParams(section, priorityParams):
    params = {}
    for innerBlock in section.values():
        isPriority = False
        innerTag = b''
        for innerTag, value in innerBlock.items():
            param = value.asString
            if innerTag != b'priority':
                params[innerTag] = param
            elif param == b'1':
                isPriority = True

        if isPriority:
            priorityParams.append(_PriorityParameter(innerTag, ParamTypes.CONST))

    return params


def _readTechTreeSettings(section):
    result = {}
    for _, modules in section[b'modules'].items():
        for m in modules.values():
            mId = m[b'id'].asString
            mTitleText = m[b'titleText'].asString
            mIcon = m[b'icon'].asString
            priorityParams = []
            deltaParameters = _readModuleParams(m[b'deltaParameters'], priorityParams, ParamTypes.DELTA) if m[b'deltaParameters'] is not None else tuple()
            params = tuple(_readModuleParams(m[b'parameters'], priorityParams, ParamTypes.SIMPLE)) if m[b'parameters'] is not None else tuple()
            constParams = _readConstModuleParams(m[b'constantParams'], priorityParams) if m[b'constantParams'] is not None else {}
            result[mId] = ModuleData(titleText=_getModuleText(mTitleText), icon=mIcon, deltaParams=deltaParameters, priorityParams=priorityParams, params=params, constParams=constParams)

    return _TechTreeSettings(result, [subsection.asString for subsection in section[b'vehicleParams'].values()])


def getTreeModuleSettings(vModule):
    descriptorId = vModule.name
    data = getBattleRoyaleSettings().techTree.modules.get(descriptorId)
    if not data:
        _logger.warning(b'Data for module "%s" has not been found', descriptorId)
        return None
    else:
        return data


def getTreeVehicleParams():
    data = getBattleRoyaleSettings().techTree.vehicleParams
    if not data:
        return None
    else:
        return data


def getTreeModuleHeader(vModule):
    mData = getTreeModuleSettings(vModule)
    if mData is not None:
        return mData.titleText
    else:
        return b''


def getTreeModuleIcon(vModule):
    data = getTreeModuleSettings(vModule)
    if data is not None:
        return data.icon
    else:
        return b''


def getVehicleProperties(nationName):
    data = getBattleRoyaleSettings().vehicleProperties.get(nationName)
    if data is None:
        _logger.error(b'There is not vehicle properties for the nation=%s', nationName)
        return VehicleProperties(strengths=(), weaknesses=())
    else:
        return data


def getBattleRoyaleSettings():
    global _BATTLE_ROYALE_SETTINGS
    if _BATTLE_ROYALE_SETTINGS is None:
        _BATTLE_ROYALE_SETTINGS = _readBattleRoyaleSettings()
    return _BATTLE_ROYALE_SETTINGS


def reloadBattleRoyaleSettings():
    global _BATTLE_ROYALE_SETTINGS
    if _BATTLE_ROYALE_SETTINGS:
        _BATTLE_ROYALE_SETTINGS = _readBattleRoyaleSettings()
    return
