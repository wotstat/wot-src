from __future__ import absolute_import
import typing, ResMgr
from constants import SHELL_TYPES_INDICES
from debug_utils import LOG_ERROR
from items import _xml
from items.components import component_constants
EffectDesc = typing.NamedTuple(b'EffectDesc', ((b'prefab', str),))
ShotEffectItemDesc = typing.NamedTuple(b'ShotEffectItemDesc', (
 (
  b'prefab', str),
 (
  b'decal', int),
 (
  b'replaces', frozenset)))
EffectDescMap = typing.Dict[str, EffectDesc]
ShotEffectGroups = typing.Dict[str, ShotEffectItemDesc]
GunEffectDesc = typing.NamedTuple(b'GunEffectDesc', (
 (
  b'idx', int),
 (
  b'explosion', EffectDesc),
 (
  b'groundwave', EffectDesc),
 (
  b'replaces', frozenset)))
GunEffectDescMap = typing.Dict[str, GunEffectDesc]
ShotEffectDesc = typing.NamedTuple(b'ShotEffectDesc', (
 (
  b'idx', int),
 (
  b'defaultHit', ShotEffectItemDesc),
 (
  b'defaultVehicleHit', ShotEffectItemDesc),
 (
  b'defaultSceneHit', ShotEffectItemDesc),
 (
  b'groups', ShotEffectGroups)))
ShotEffects = typing.NamedTuple(b'ShotEffects', (
 (
  b'effects', typing.Sequence[ShotEffectDesc]),
 (
  b'indexes', typing.Dict[str, int])))
DecalDesc = typing.NamedTuple(b'DecalDesc', (
 (
  b'idx', int),
 (
  b'priority', int),
 (
  b'prefab', str)))
Decals = typing.NamedTuple(b'Decals', (
 (
  b'effects', typing.Sequence[DecalDesc]),
 (
  b'indexes', typing.Dict[str, int])))
ShotDefaults = typing.NamedTuple(b'ShotDefaults', (
 (
  b'default', str),
 (
  b'shellTypeEffects', typing.Dict[str, str])))
Defaults = typing.NamedTuple(b'Defaults', (
 (
  b'gun', str),
 (
  b'shot', ShotDefaults)))
_EMPTY_EFFECT = EffectDesc(b'')
_EMPTY_SHOT_EFFECT_ITEM = ShotEffectItemDesc(b'', component_constants.INVALID_EFFECT_INDEX, frozenset())

def readDefaultPrefabEffects(xmlCtx, section, subsectionName):
    section = _xml.getSubsection(xmlCtx, section, subsectionName)
    gunDefault = _xml.readStringOrEmpty(xmlCtx, section, b'gun').strip()
    shotDefault = b''
    shotShellTypeEffects = {}
    shotSection = section[b'shot']
    if shotSection is not None:
        for sectionName, subsection in shotSection.items():
            if sectionName == b'default':
                shotDefault = subsection.asString.strip() or shotDefault
            elif sectionName in SHELL_TYPES_INDICES:
                shotShellTypeEffects[sectionName] = subsection.asString.strip()
            else:
                LOG_ERROR((b'Unrecognized shell type name when reading defaultPrefabEffects: {}').format(sectionName))

    return Defaults(gunDefault, ShotDefaults(shotDefault, shotShellTypeEffects))


def readGunEffects(xmlPath):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    res = {}
    xmlCtx = (
     None, xmlPath)
    idx = 0
    for sname, subsection in section.items():
        ctx = (
         xmlCtx, sname)
        res[sname] = _readGunEffect(ctx, subsection, idx)
        idx += 1

    return res


def readShotEffects(xmlPath, decals):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    effects = []
    indexes = {}
    xmlCtx = (
     None, xmlPath)
    for sname, subsection in section.items():
        ctx = (
         xmlCtx, sname)
        indexes[sname] = len(effects)
        effects.append(_readShotEffect(ctx, subsection, decals, len(effects)))

    return ShotEffects(effects, indexes)


def readDecals(xmlPath):
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    decals = []
    indexes = {}
    xmlCtx = (
     None, xmlPath)
    for sname, subsection in section.items():
        ctx = (
         xmlCtx, sname)
        indexes[sname] = len(decals)
        decals.append(_readDecal(ctx, subsection, len(decals)))

    return Decals(decals, indexes)


def _readEffect(xmlCtx, section):
    prefabPath = _xml.readString(xmlCtx, section, b'prefab')
    return EffectDesc(prefabPath)


def _readGunEffect(xmlCtx, section, idx):
    explosionEffect = _readEffect(xmlCtx, section[b'explosion'])
    groundWaveEffect = _readEffect(xmlCtx, section[b'groundwave']) if section.has_key(b'groundwave') else _EMPTY_EFFECT
    replaces = frozenset(section[b'replaces'].keys()) if section.has_key(b'replaces') else frozenset()
    return GunEffectDesc(idx, explosionEffect, groundWaveEffect, replaces)


def _readShotEffectItem(xmlCtx, section, decals):
    prefabPath = _xml.readString(xmlCtx, section, b'prefab')
    decal = _xml.readStringOrEmpty(xmlCtx, section, b'decal')
    decalId = decals.indexes[decal] if decal else component_constants.INVALID_EFFECT_INDEX
    replaces = frozenset(section[b'replaces'].keys()) if section.has_key(b'replaces') else frozenset()
    return ShotEffectItemDesc(prefabPath, decalId, replaces)


def _readShotEffect(xmlCtx, section, decals, idx):
    res = {}
    defaultHit = _EMPTY_SHOT_EFFECT_ITEM
    defaultVehicleHit = _EMPTY_SHOT_EFFECT_ITEM
    defaultSceneHit = _EMPTY_SHOT_EFFECT_ITEM
    for sname, subsection in section.items():
        xmlCtx = (
         xmlCtx, sname)
        shotEffectItem = _readShotEffectItem(xmlCtx, subsection, decals)
        if sname == b'defaultHit':
            defaultHit = shotEffectItem
        elif sname == b'defaultVehicleHit':
            defaultVehicleHit = shotEffectItem
        elif sname == b'defaultSceneHit':
            defaultSceneHit = shotEffectItem
        else:
            res[sname] = shotEffectItem

    return ShotEffectDesc(idx, defaultHit, defaultVehicleHit, defaultSceneHit, res)


def _readDecal(xmlCtx, section, idx):
    priority = _xml.readNonNegativeInt(xmlCtx, section, b'priority')
    prefabPath = _xml.readString(xmlCtx, section, b'prefab')
    return DecalDesc(idx, priority, prefabPath)
