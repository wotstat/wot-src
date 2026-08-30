import BigWorld, ResMgr, material_kinds
from constants import IS_EDITOR
from debug_utils import LOG_ERROR, LOG_CURRENT_EXCEPTION
g_instance = None

class DecalMap(object):

    def __init__(self, dataSec):
        self.__cfg = dict()
        self.__texMap = dict()
        self.__textureSets = dict()
        if IS_EDITOR:
            self.__chassisEffectGroups = dict()
        self._readCfg(dataSec)
        self.__initGroups(1.0)
        return

    def __initGroups(self, scaleFactor):
        if not BigWorld.isDynamicDecalEnabled():
            return
        try:
            for group in self.__cfg[b'groups'].items():
                BigWorld.addDecalGroup(group[0], group[1][b'lifeTime'] * scaleFactor, group[1][b'trianglesCount'] * scaleFactor)

            for tex in self.__cfg[b'textures'].items():
                index = BigWorld.decalTextureIndex(tex[1])
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

    def _readCfg(self, dataSec):
        if dataSec is None:
            LOG_ERROR(b'Invalid dataSection.')
            return
        else:
            criticalHitDecalAngle = dataSec.readFloat(b'criticalAngle', 30.0)
            BigWorld.setDamageStickerCriticalAngle(criticalHitDecalAngle)
            self.__cfg[b'groups'] = dict()
            groups = self.__cfg[b'groups']
            for group in dataSec[b'groups'].values():
                desc = dict()
                desc[b'lifeTime'] = _readFloat(group, b'lifeTime', 0, 1000, 1)
                desc[b'trianglesCount'] = _readFloat(group, b'trianglesCount', 1000, 100000, 1000)
                groups[group.name] = desc

            self.__cfg[b'textures'] = dict()
            textures = self.__cfg[b'textures']
            for texture in dataSec[b'textures'].values():
                textures[texture.name] = texture.readString(b'texture')

            chassisEffectsSection = ResMgr.openSection(b'scripts/item_defs/vehicles/common/chassis_effects.xml')
            if not chassisEffectsSection or chassisEffectsSection[b'decals'] is None:
                LOG_ERROR(b'Failed to read chassis_effects.xml file')
                return
            dataSec = chassisEffectsSection[b'decals']
            for group in dataSec[b'bufferPrefs'].values():
                desc = dict()
                desc[b'lifeTime'] = _readFloat(group, b'lifeTime', 0, 1000, 1)
                desc[b'trianglesCount'] = _readFloat(group, b'trianglesCount', 1000, 100000, 1000)
                groups[group.name] = desc
                if IS_EDITOR:
                    self.__chassisEffectGroups[group.name] = desc

            for sMatId in dataSec[b'scales'].values():
                scaleU = _readFloat(sMatId, b'scaleU', 1, 2, 1)
                for matKind in material_kinds.EFFECT_MATERIAL_IDS_BY_NAMES[sMatId.name]:
                    BigWorld.addMatkindScaleU(sMatId.name, matKind, scaleU)

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
                        texIndex = BigWorld.traceTextureIndex(texName)
                        self.__texMap[texName] = texIndex
                        textListIndex = _DIF_TEXT
                        if dsTexture.name == b'ANM':
                            textListIndex = _BUMP_TEXT
                        elif dsTexture.name == b'STRAFE_AM':
                            textListIndex = _STRAFE_DIF_TEXT
                        elif dsTexture.name == b'STRAFE_ANM':
                            textListIndex = _STRAFE_BUMP_TEXT
                        tsMaterial[textListIndex] = texIndex

                self.__textureSets[dsTexSet.name] = ts

            return

    def writeCfg(self):
        return


def _readFloat(dataSec, name, minVal, maxVal, defaultVal):
    if dataSec is None:
        return defaultVal
    else:
        value = dataSec.readFloat(name, defaultVal)
        value = min(maxVal, value)
        value = max(minVal, value)
        return value
