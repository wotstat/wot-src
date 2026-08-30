from functools import partial
import typing, BigWorld, ResMgr, material_kinds, persistent_data_cache as pdc
from constants import IS_EDITOR
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION

class DecalMap(object):

    def __init__(self, config):
        self.__texMap = {}
        self.__textureSets = {}
        if IS_EDITOR:
            self.__chassisEffectGroups = config.get(b'chassisEffectsGroups', {})
        self._init(config)
        return

    def _init(self, config):
        BigWorld.setDamageStickerCriticalAngle(config[b'criticalHitDecalAngle'])
        for sMatName, scale in config[b'scales']:
            for matKind in material_kinds.EFFECT_MATERIAL_IDS_BY_NAMES[sMatName]:
                BigWorld.wg_addMatkindScaleU(sMatName, matKind, scale)

        for texName in config[b'traceTextures']:
            self.__texMap[texName] = BigWorld.wg_traceTextureIndex(texName)

        for tsName, tset in config[b'textureSets'].iteritems():
            self.__textureSets[tsName] = {}
            for mName, material in tset.iteritems():
                self.__textureSets[tsName][mName] = [self.__texMap[texName] if texName is not None else None for texName in material]

        self._initGroups(config)
        return

    def _initGroups(self, config, scaleFactor=1.0):
        if not BigWorld.isDynamicDecalEnabled():
            return
        try:
            for group in config[b'groups'].items():
                BigWorld.wg_addDecalGroup(group[0], group[1][b'lifeTime'] * scaleFactor, group[1][b'trianglesCount'] * scaleFactor)

            for tex in config[b'textures'].items():
                index = BigWorld.wg_decalTextureIndex(tex[1])
                if index == -1:
                    LOG_ERROR(b"texture '%s' is not exist or to more textures added to the texture atlas.Max textures count is 16." % tex[1])
                else:
                    self.__texMap[tex[0]] = index

        except Exception:
            LOG_CURRENT_EXCEPTION()

        return

    def getIndex(self, name):
        if not self.__texMap.has_key(name):
            if name != b'':
                LOG_ERROR(b"Invalid texture name '%s'" % name, stack=True)
            return -1
        return self.__texMap[name]

    def getTextureSet(self, name):
        if not self.__textureSets.has_key(name):
            LOG_ERROR(b"Invalid texture set name '%s'" % name, stack=True)
            return dict()
        return self.__textureSets[name]

    if IS_EDITOR:

        @property
        def textureSets(self):
            return self.__textureSets

        @property
        def chassisEffectGroups(self):
            return self.__chassisEffectGroups


def _readFloat(dataSec, name, minVal, maxVal, defaultVal):
    if dataSec is None:
        return defaultVal
    else:
        value = dataSec.readFloat(name, defaultVal)
        value = min(maxVal, value)
        value = max(minVal, value)
        return value


def _readCfg(dataSec):
    if dataSec is None:
        LOG_ERROR(b'Invalid dataSection.')
        return {}
    else:
        config = {b'criticalHitDecalAngle': (dataSec.readFloat(b'criticalAngle', 30.0)), b'groups': {group.name: {b'lifeTime': (_readFloat(group, b'lifeTime', 0, 1000, 1)), b'trianglesCount': (_readFloat(group, b'trianglesCount', 1000, 100000, 1000))} for group in dataSec[b'groups'].values()}, 
           b'chassisEffectsGroups': {}, b'textures': {texture.name: texture.readString(b'texture') for texture in dataSec[b'textures'].values()}, b'scales': [], b'traceTextures': (set()), 
           b'textureSets': {}}
        chassisEffectsSection = ResMgr.openSection(b'scripts/item_defs/vehicles/common/chassis_effects.xml')
        if not chassisEffectsSection or chassisEffectsSection[b'decals'] is None:
            LOG_ERROR(b'Failed to read chassis_effects.xml file')
            return config
        dataSec = chassisEffectsSection[b'decals']
        for group in dataSec[b'bufferPrefs'].values():
            desc = {b'lifeTime': (_readFloat(group, b'lifeTime', 0, 1000, 1)), b'trianglesCount': (_readFloat(group, b'trianglesCount', 1000, 100000, 1000))}
            config[b'groups'][group.name] = desc
            config[b'chassisEffectsGroups'][group.name] = desc

        for sMatId in dataSec[b'scales'].values():
            config[b'scales'].append((sMatId.name, _readFloat(sMatId, b'scaleU', 1, 2, 1)))

        for dsTexSet in dataSec[b'textureSets'].values():
            ts = {}
            _DIF_TEXT = 0
            _BUMP_TEXT = 1
            _STRAFE_DIF_TEXT = 2
            _STRAFE_BUMP_TEXT = 3
            for dsMaterial in dsTexSet.values():
                tsMaterial = [None, None, None, None]
                ts[dsMaterial.name] = tsMaterial
                for dsTexture in dsMaterial.values():
                    texName = dsMaterial.readString(dsTexture.name)
                    config[b'traceTextures'].add(texName)
                    textListIndex = _DIF_TEXT
                    if dsTexture.name == b'ANM':
                        textListIndex = _BUMP_TEXT
                    elif dsTexture.name == b'STRAFE_AM':
                        textListIndex = _STRAFE_DIF_TEXT
                    elif dsTexture.name == b'STRAFE_ANM':
                        textListIndex = _STRAFE_BUMP_TEXT
                    tsMaterial[textListIndex] = texName

            config[b'textureSets'][dsTexSet.name] = ts

        return config


g_instance = None

def init(section):
    global g_instance
    config = pdc.load(b'decal_map_config', partial(_readCfg, section))
    g_instance = DecalMap(config)
    return
