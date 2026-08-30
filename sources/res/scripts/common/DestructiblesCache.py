import ResMgr, BigWorld, Math, math
from constants import TREE_TAG, CUSTOM_DESTRUCTIBLE_TAGS
import string
from material_kinds import EFFECT_MATERIALS, EFFECT_MATERIAL_INDEXES_BY_NAMES
from constants import IS_CLIENT, IS_CELLAPP, IS_DEVELOPMENT, DESTRUCTIBLE_MATKIND
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR, LOG_WARNING
import items
from soft_exception import SoftException
if IS_CLIENT:
    from helpers import EffectsList
if IS_CLIENT or IS_CELLAPP:
    from BigWorld import packAngleToUint, unpackAngleFromUint
SEARCH_AD_RADIUS = 5.0
RADIUS_FOR_LOCATION_AD = SEARCH_AD_RADIUS - 0.5
DESTRUCTIBLES_CONFIG_FILE = b'scripts/destructibles.xml'
DESTRUCTIBLES_EFFECTS_FILE = b'scripts/destructibles_effects.xml'
SPT_MATKIND_SOLID = 71
DESTR_TYPE_TREE = 0
DESTR_TYPE_FALLING_ATOM = 1
DESTR_TYPE_FRAGILE = 2
DESTR_TYPE_STRUCTURE = 3
DESTR_STATE_NAME_DESTROYED = b'destroyed'
DESTR_STATE_NAME_UNDAMAGED = b'undamaged'
DESTR_STATE_NAME_FALLEN = b'fallen'
STATIC_OBSTACLE_ID = 10000
_INV_CHUNK_RANGE = 0.01
PI = math.pi
FALLING_DESTRUCTIBLES_IGNORE_ANGLE = PI / 4.0
FALLING_DESTRUCTIBLES_IGNORE_SIN = math.sin(FALLING_DESTRUCTIBLES_IGNORE_ANGLE)
GLOBAL_CHUNK_ID = 127 + 127 << 8 | 127 + 127

class DestructiblesCache():

    def __init__(self):
        if IS_CLIENT:
            sec = ResMgr.openSection(DESTRUCTIBLES_EFFECTS_FILE)
            if not sec:
                raise SoftException(b"Fail to read '%s'" % DESTRUCTIBLES_EFFECTS_FILE)
            self.__effects = _readDestructiblesEffects(sec)
            ResMgr.purge(DESTRUCTIBLES_EFFECTS_FILE, True)
        sec = ResMgr.openSection(DESTRUCTIBLES_CONFIG_FILE)
        if not sec:
            raise SoftException(b"Fail to read '%s'" % DESTRUCTIBLES_CONFIG_FILE)
        self.__defaultLifetimeEffectChance = sec.readFloat(b'defaultLifetimeEffectChance')
        self.__unitVehicleMass = sec.readFloat(b'unitVehicleMass')
        if not IS_CLIENT or IS_DEVELOPMENT:
            self.__maxHpForShootingThrough = sec.readFloat(b'maxHpForShootingThrough')
            self.__projectilePiercingPowerReduction = _readProjectilePiercingPowerReduction(sec[b'projectilePiercingPowerReduction'])
        descs = []
        for fragileSec in sec[b'fragiles'].values():
            desc = self.__readFragile(fragileSec)
            descs.append(desc)

        for fallingSec in sec[b'fallingAtoms'].values():
            desc = self.__readFallingAtom(fallingSec)
            descs.append(desc)

        for treeSec in sec[b'trees'].values():
            desc = self.__readTree(treeSec)
            descs.append(desc)

        for structSec in sec[b'structures'].values():
            desc = self.__readStructure(structSec)
            descs.append(desc)

        self.__descs = descs
        self.__descIDs = dict((desc[b'filename'], i) for i, desc in enumerate(descs))
        ResMgr.purge(DESTRUCTIBLES_CONFIG_FILE, True)
        return

    @property
    def unitVehicleMass(self):
        return self.__unitVehicleMass

    @property
    def maxHpForShootingThrough(self):
        return self.__maxHpForShootingThrough

    @property
    def projectilePiercingPowerReduction(self):
        return self.__projectilePiercingPowerReduction

    def getDescByID(self, descID):
        if descID < len(self.__descs):
            return self.__descs[descID]
        else:
            return

    def getDescIDByFilename(self, filename):
        return self.__descIDs.get(filename)

    def getDescByFilename(self, filename):
        id = self.getDescIDByFilename(filename)
        if id is not None:
            return self.__descs[id]
        else:
            return

    def __readStructure(self, structSec):
        filename = structSec.readString(b'filename')
        ids = []
        idMap = {}
        for moduleSec in structSec[b'modules'].values():
            module = {b'health': (moduleSec.readInt(b'health'))}
            matName = moduleSec.readString(b'matName')
            res = _parseMaterialName(matName, filename)
            if res:
                type, surface, id, depends = res
            else:
                continue
            effectMtrlIdx = EFFECT_MATERIAL_INDEXES_BY_NAMES.get(surface)
            if effectMtrlIdx is not None:
                module[b'effectMtrlIdx'] = effectMtrlIdx
            else:
                LOG_ERROR(b'Wrong effect material in structure %s' % filename)
            if IS_CLIENT:
                _readAndMapEffect(module, moduleSec, b'ramEffect', self.__effects[b'structures'], filename)
                _readAndMapEffect(module, moduleSec, b'hitEffect', self.__effects[b'structures'], filename)
                _readAndMapEffect(module, moduleSec, b'decayEffect', self.__effects[b'structures'], filename)
                module[b'effectHP'] = intern(moduleSec.readString(b'effectHP'))
                module[b'effectScale'] = moduleSec.readFloat(b'effectScale')
            ids.append(id)
            idMap[id] = (module, depends)

        destrMatkindCnt = DESTRUCTIBLE_MATKIND.NORMAL_MAX - DESTRUCTIBLE_MATKIND.NORMAL_MIN
        if len(ids) > destrMatkindCnt:
            LOG_ERROR(b'Number of modules in structure %s exceeds destructibles material kinds range' % filename)
            ids = ids[:destrMatkindCnt]
        ids.sort()
        map = {}
        modules = {}
        matkindNMin = DESTRUCTIBLE_MATKIND.NORMAL_MIN
        matkindDMin = DESTRUCTIBLE_MATKIND.DAMAGED_MIN
        matkindsNormal = []
        for i, id in enumerate(ids):
            module, depends = idMap[id]
            destroyedMat = matkindDMin + i
            module[b'destroyedMat'] = destroyedMat
            normalMat = matkindNMin + i
            matkindsNormal.append(normalMat)
            modules[normalMat] = module
            map[normalMat] = tuple(ids.index(id) + matkindNMin for id in depends)

        destroyDepends = {}
        for root in map.iterkeys():
            rootDepends = set()
            stack = [root]
            while len(stack) > 0:
                cur = stack.pop()
                if cur in rootDepends:
                    continue
                rootDepends.add(cur)
                depends = map.get(cur)
                if depends is None:
                    continue
                stack += depends

            rootDepends.remove(root)
            if len(rootDepends) > 0:
                destroyDepends[root] = rootDepends

        inversedDestroyDepends = {}
        for keyMat, depends in destroyDepends.iteritems():
            for mat in depends:
                inversedDestroyDepends.setdefault(mat, set()).add(keyMat)

        statePresets = {DESTR_STATE_NAME_UNDAMAGED: [], DESTR_STATE_NAME_DESTROYED: matkindsNormal}
        if structSec.has_key(b'states'):
            for stateSec in structSec[b'states'].values():
                name = stateSec.readString(b'name').strip()
                matNames = stateSec.readString(b'destroyedMaterials').split(b' ')
                matKinds = []
                for matName in matNames:
                    res = _parseMaterialName(matName, filename)
                    if res:
                        type, surface, id, depends = res
                    else:
                        continue
                    matKinds.append(ids.index(id) + matkindNMin)

                statePresets[name] = matKinds

        desc = {b'filename': filename, b'type': DESTR_TYPE_STRUCTURE, b'modules': modules, 
           b'destroyDepends': destroyDepends, 
           b'inversedDestroyDepends': inversedDestroyDepends, 
           b'statePresets': statePresets}
        self.__readAchievementTag(structSec, desc)
        return desc

    def __readExplosive(self, fragileSec, desc):
        explosiveSec = fragileSec[b'explosive']
        if explosiveSec:
            effName = explosiveSec.readString(b'effects', b'smallArmorPiercing')
            desc[b'explosive'] = {b'radius': (explosiveSec.readFloat(b'explosionRadius', 0)), 
               b'armorDamage': (explosiveSec.readFloat(b'damage/armor', 0)), 
               b'devicesDamage': (explosiveSec.readFloat(b'damage/devices', 0)), 
               b'effect': (items.vehicles.g_cache.shotEffectsIndexes.get(effName)), 
               b'fireRadius': (explosiveSec.readFloat(b'fireRadius', 0))}
        return

    def __readFragile(self, fragileSec):
        filename = fragileSec.readString(b'filename')
        kineticDamageCorrection = fragileSec.readFloat(b'kineticDamageCorrection', 0.0)
        desc = {b'filename': filename, b'health': (fragileSec.readInt(b'health')), 
           b'kineticDamageCorrection': kineticDamageCorrection, 
           b'type': DESTR_TYPE_FRAGILE}
        self.__readAchievementTag(fragileSec, desc)
        self.__readExplosive(fragileSec, desc)
        matName = fragileSec.readString(b'matName')
        if matName:
            surface = _parseFragileMaterialName(matName, filename)
            effectMtrlIdx = EFFECT_MATERIAL_INDEXES_BY_NAMES.get(surface)
            if effectMtrlIdx is not None:
                desc[b'effectMtrlIdx'] = effectMtrlIdx
        if IS_CLIENT:
            _readAndMapEffect(desc, fragileSec, b'effect', self.__effects[b'fragiles'], filename)
            _readAndMapEffect(desc, fragileSec, b'hitEffect', self.__effects[b'fragiles'], filename, False)
            _readAndMapEffect(desc, fragileSec, b'decayEffect', self.__effects[b'fragiles'], filename)
            desc[b'effectHP'] = fragileSec.readString(b'effectHP')
            desc[b'effectScale'] = fragileSec.readFloat(b'effectScale')
            _readAndMapEffect(desc, fragileSec, b'lifetimeEffect', self.__effects[b'fragiles'], filename)
            if fragileSec.has_key(b'lifetimeEffectChance'):
                desc[b'lifetimeEffectChance'] = fragileSec.readFloat(b'lifetimeEffectChance')
            else:
                desc[b'lifetimeEffectChance'] = self.__defaultLifetimeEffectChance
        return desc

    def __readTree(self, treeSec):
        filename = treeSec.readString(b'filename')
        kineticDamageCorrection = treeSec.readFloat(b'kineticDamageCorrection', 0.0)
        desc = {b'filename': filename, b'health': (treeSec.readInt(b'health')), 
           b'density': (treeSec.readFloat(b'density')), 
           b'kineticDamageCorrection': kineticDamageCorrection, 
           b'type': DESTR_TYPE_TREE, 
           b'achievementTag': TREE_TAG}
        physParams = _readDestructiblePhysicParams(treeSec)
        desc.update(physParams)
        if IS_CLIENT:
            _readAndMapEffect(desc, treeSec, b'fractureEffect', self.__effects[b'trees'], filename)
            _readAndMapEffect(desc, treeSec, b'touchdownEffect', self.__effects[b'trees'], filename)
            _readAndMapEffect(desc, treeSec, b'lifetimeEffect', self.__effects[b'trees'], filename)
            if treeSec.has_key(b'lifetimeEffectChance'):
                desc[b'lifetimeEffectChance'] = treeSec.readFloat(b'lifetimeEffectChance')
            else:
                desc[b'lifetimeEffectChance'] = self.__defaultLifetimeEffectChance
        return desc

    def __readFallingAtom(self, fallingSec):
        filename = fallingSec.readString(b'filename')
        kineticDamageCorrection = fallingSec.readFloat(b'kineticDamageCorrection', 0.0)
        desc = {b'filename': filename, b'health': (fallingSec.readInt(b'health')), 
           b'kineticDamageCorrection': kineticDamageCorrection, 
           b'type': DESTR_TYPE_FALLING_ATOM}
        self.__readAchievementTag(fallingSec, desc)
        physParams = _readDestructiblePhysicParams(fallingSec)
        desc.update(physParams)
        preferredTiltDirections = _readPreferredTiltDirections(fallingSec)
        if preferredTiltDirections:
            desc[b'preferredTiltDirections'] = preferredTiltDirections
        if IS_CLIENT:
            _readAndMapEffect(desc, fallingSec, b'fractureEffect', self.__effects[b'fallingAtoms'], filename)
            _readAndMapEffect(desc, fallingSec, b'touchdownEffect', self.__effects[b'fallingAtoms'], filename)
            _readAndMapEffect(desc, fallingSec, b'touchdownBreakEffect', self.__effects[b'fallingAtoms'], filename, False)
            _readAndMapEffect(desc, fallingSec, b'lifetimeEffect', self.__effects[b'fallingAtoms'], filename)
            if fallingSec.has_key(b'lifetimeEffectChance'):
                desc[b'lifetimeEffectChance'] = fallingSec.readFloat(b'lifetimeEffectChance')
            else:
                desc[b'lifetimeEffectChance'] = self.__defaultLifetimeEffectChance
            desc[b'effectScale'] = fallingSec.readFloat(b'effectScale')
        return desc

    def __readAchievementTag(self, section, desc):
        tag = section.readString(b'achievementTag')
        if tag:
            if tag in CUSTOM_DESTRUCTIBLE_TAGS:
                desc[b'achievementTag'] = tag
            else:
                raise SoftException(b"Wrong achievement tag '%s' in destructible '%s'" % (
                 tag, section.readString(b'filename')))
        return

    def _getEffect(self, effectName, effectCategory, needLogErrors=True):
        if not effectName:
            if needLogErrors:
                LOG_WARNING(b'Failed to read %s name in %s' % (effectName, effectCategory))
            return
        if string.lower(effectName) == b'none':
            return
        else:
            effects = self.__effects[effectCategory]
            effect = effects.get(effectName)
            if effect is None:
                if needLogErrors:
                    LOG_ERROR(b'Destructibles effect %s is not found' % effectName)
                return
            return effect


def _parseFragileMaterialName(matName, filename):
    try:
        arr = matName.split(b'_')
        res = filter(str.isalpha, arr[1])
    except:
        LOG_ERROR(b'Fail to parse material name %s in fragile %s' % (matName, filename))
        res = None

    return res


def _parseMaterialName(matName, filename):
    try:
        arr = matName.split(b'_')
        type = intern(arr[0])
        surface = intern(filter(str.isalpha, arr[1]))
        id = int(arr[2])
        depends = map(int, arr[3:])
        res = (type, surface, id, depends)
    except:
        LOG_ERROR(b'Fail to parse material name %s in structure %s' % (matName, filename))
        res = None

    return res


def _readAndMapEffect(cfg, sec, effectKey, effects, destrFilename, needLogErrors=True):
    effectName = sec.readString(effectKey)
    if not effectName:
        if needLogErrors:
            LOG_WARNING(b'Failed to read %s name in %s' % (effectKey, destrFilename))
            return
    if string.lower(effectName) == b'none':
        return
    else:
        effect = effects.get(effectName)
        if effect is None:
            if needLogErrors:
                LOG_ERROR(b'Destructibles effect %s is not found' % effectName)
            return
        cfg[effectKey] = effect
        return


def _readDestructiblesEffects(sec):
    effects = {}
    for groupName, groupSec in sec.items():
        groupEffects = {}
        for effName, effSec in groupSec.items():
            variants = []
            try:
                for varSec in effSec.values():
                    variants.append(_readEffectsTimeLine(varSec))

            except Exception:
                print Exception, groupName, groupSec, effName
                LOG_CURRENT_EXCEPTION()

            groupEffects[effName] = tuple(variants)

        effects[groupName] = groupEffects

    return effects


def _readEffectsTimeLine(section):
    effectsTimeLine = EffectsList.effectsFromSection(section)
    return effectsTimeLine


def _readDestructiblePhysicParams(section):
    params = _readFloatArray(section[b'physicParams'], 7)
    cfg = {b'mass': (params[0]), 
       b'height': (params[1]), 
       b'springAngle': (params[2]), 
       b'springStiffnes': (params[3]), 
       b'springResist': (params[4]), 
       b'airResist': (params[5]), 
       b'buryDepth': (params[6])}
    return cfg


def _readPreferredTiltDirections(section):
    angles = _readFloatArray(section[b'preferredTiltDirections']) if section.has_key(b'preferredTiltDirections') else tuple()
    if angles:
        angles = map((lambda a: (a + 180.0) % 360.0 - 180.0), angles)
        angles.append(max(angles) - 360)
        angles.append(min(angles) + 360)
        angles = map(math.radians, angles)
    return angles


def _readProjectilePiercingPowerReduction(section):
    res = []
    defaultVal = section.readVector2(EFFECT_MATERIALS[0])
    for matName in EFFECT_MATERIALS:
        val = section.readVector2(matName) or defaultVal
        try:
            reductionFactor = float(val[0])
            minReduction = float(val[1])
        except:
            raise SoftException(b'Wrong of missing value of %s/%s' % (section.name, matName))

        res.append((reductionFactor, minReduction))

    return tuple(res)


def _readFloatArray(sec, count=None):
    arrayStr = sec.readString(b'')
    strArr = arrayStr.split()
    if count is not None and len(strArr) != count:
        raise SoftException(b'Error reading float array from section %s' % sec.name)
    return tuple(map(float, strArr))


def _readIntArray(sec, count):
    arrayStr = sec.readString(b'')
    strArr = arrayStr.split()
    if len(strArr) != count:
        raise SoftException(b'Error reading int array from section %s' % sec.name)
    return tuple(map(int, strArr))


def _readStringArray(sec, count):
    arrayStr = sec.readString(b'')
    strArr = arrayStr.split()
    if len(strArr) != count:
        raise SoftException(b'Error reading int array from section %s' % sec.name)
    return strArr


def scaledDestructibleHealth(scale, refHealth):
    return int(math.ceil(scale * scale * refHealth))


def chunkIDFromChunkPosition(position):
    chunkX = int(round(position.x * 0.01))
    chunkZ = int(round(position.z * 0.01))
    return chunkX + 127 << 8 | chunkZ + 127


def controllerPositionFromChunkID(chunkID):
    x = ((chunkID >> 8) - 127) * 100.0 + 50.0
    z = ((chunkID & 255) - 127) * 100.0 + 50.0
    return Math.Vector3(x, 0, z)


def chunkIndexesFromPosition(position):
    chunkX = int(math.floor(position[0] * _INV_CHUNK_RANGE))
    chunkZ = int(math.floor(position[2] * _INV_CHUNK_RANGE))
    return (chunkX, chunkZ)


def chunkIDFromPosition(position):
    return chunkIDFromChunkIndexes(*chunkIndexesFromPosition(position))


def chunkIDFromChunkIndexes(gridX, gridZ):
    return gridX + 127 << 8 | gridZ + 127


def chunkIndexesFromChunkID(id):
    return (
     (id >> 8) - 127, (id & 255) - 127)


def areaDestructiblesPositionFromChunkID(chunkID):
    gridX, gridZ = chunkIndexesFromChunkID(chunkID)
    pos = controllerPositionFromChunkID(chunkID)
    dx = RADIUS_FOR_LOCATION_AD * math.cos(PI / 10.0 * (gridX + gridZ))
    dz = RADIUS_FOR_LOCATION_AD * math.sin(PI / 10.0 * (gridX + gridZ))
    return Math.Vector3(pos.x + dx, 0, pos.z + dz)


def encodeUint16(value):
    return (
     value >> 8 & 255, value & 255)


def decodeUint16(data):
    return data[0] << 8 | data[1]


def encodeDestructibleModule(destrID, matKind, isShotDamage):
    return encodeUint16(destrID) + ((matKind & 127) << 1 | int(isShotDamage),)


def decodeDestructibleModule(data):
    return (
     decodeUint16(data[:2]), data[2] >> 1, bool(data[2] & 1))


def encodeFragile(destrID, isShotDamage):
    return encodeUint16(destrID) + (int(isShotDamage),)


def decodeFragile(data):
    return (
     decodeUint16(data[:2]), bool(data[2]))


def encodeFallenColumn(destrID, fallYaw, fallSpeed):
    params = packAngleToUint(fallYaw, 6) << 2 | max(0, min(int(fallSpeed), 3))
    return encodeUint16(destrID) + (params,)


def decodeFallenColumn(data):
    destrID = decodeUint16(data[:2])
    params = data[2]
    fallYaw = unpackAngleFromUint(params >> 2, 6)
    fallSpeed = float(params & 3)
    return (destrID, fallYaw, fallSpeed)


def encodeFallenTree(destrID, fallYaw, fallPitchConstr, fallSpeed):
    params = packAngleToUint(fallYaw, 6) << 2 | max(0, min(int(fallSpeed), 3))
    return encodeUint16(destrID) + encodeUint16(packAngleToUint(fallPitchConstr, 16)) + (params,)


def decodeFallenTree(data):
    destrID = decodeUint16(data[:2])
    fallPitchConstr = unpackAngleFromUint(decodeUint16(data[2:4]), 16)
    params = data[4]
    fallYaw = unpackAngleFromUint(params >> 2, 6)
    fallSpeed = float(params & 3)
    return (destrID, fallYaw, fallPitchConstr, fallSpeed)
