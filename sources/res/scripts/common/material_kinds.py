from __future__ import absolute_import
from past.builtins import intern
import ResMgr
from soft_exception import SoftException
_MATERIAL_KINDS_FILE = b'system/data/material_kinds.xml'
_EFFECT_MATERIALS_FILE = b'system/data/effect_materials.xml'
IDS_BY_NAMES = None
NAMES_BY_IDS = None
EFFECT_MATERIALS = None
EFFECT_MATERIAL_INDEXES_BY_NAMES = None
EFFECT_MATERIAL_NAMES_BY_INDEXES = None
EFFECT_MATERIAL_INDEXES_BY_IDS = None
EFFECT_MATERIAL_IDS_BY_NAMES = None
NOT_GROUND_MATERIALS = None
EFFECT_MATERIAL_PROPERTIES = None

def _init():
    global EFFECT_MATERIALS
    global EFFECT_MATERIAL_IDS_BY_NAMES
    global EFFECT_MATERIAL_INDEXES_BY_IDS
    global EFFECT_MATERIAL_INDEXES_BY_NAMES
    global EFFECT_MATERIAL_NAMES_BY_INDEXES
    global EFFECT_MATERIAL_PROPERTIES
    global IDS_BY_NAMES
    global NAMES_BY_IDS
    global NOT_GROUND_MATERIALS
    IDS_BY_NAMES = {}
    NAMES_BY_IDS = {}
    EFFECT_MATERIALS = []
    EFFECT_MATERIAL_INDEXES_BY_NAMES = {}
    EFFECT_MATERIAL_NAMES_BY_INDEXES = {}
    EFFECT_MATERIAL_INDEXES_BY_IDS = {}
    EFFECT_MATERIAL_IDS_BY_NAMES = {b'default': [0]}
    NOT_GROUND_MATERIALS = []
    EFFECT_MATERIAL_PROPERTIES = {}
    xmlPath = _MATERIAL_KINDS_FILE
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _raiseWrongXml(xmlPath, b'can not open or read')
    ids = set()
    for s in section.values():
        id = s.readInt(b'id', -1)
        name = s.readString(b'desc')
        if not name or id in ids or name in IDS_BY_NAMES:
            _raiseWrongXml(xmlPath, b"wrong or non-unique 'id' or 'desc' (%d, '%s')" % (id, name))
        ids.add(id)
        IDS_BY_NAMES[name] = id
        NAMES_BY_IDS[id] = name
        matName = s.readString(b'effect_material')
        if matName:
            matName = intern(matName)
            if matName not in EFFECT_MATERIALS:
                EFFECT_MATERIALS.append(matName)
            if EFFECT_MATERIAL_IDS_BY_NAMES.get(matName) is None:
                EFFECT_MATERIAL_IDS_BY_NAMES[matName] = []
            EFFECT_MATERIAL_IDS_BY_NAMES[matName].append(id)

    for ind, matName in enumerate(EFFECT_MATERIALS):
        EFFECT_MATERIAL_INDEXES_BY_NAMES[matName] = ind
        EFFECT_MATERIAL_NAMES_BY_INDEXES[ind] = matName
        for id in EFFECT_MATERIAL_IDS_BY_NAMES[matName]:
            EFFECT_MATERIAL_INDEXES_BY_IDS[id] = ind

    ResMgr.purge(xmlPath, True)
    xmlPath = _EFFECT_MATERIALS_FILE
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _raiseWrongXml(xmlPath, b'can not open or read')
    for s in section.values():
        name = s.readString(b'name')
        if not name:
            _raiseWrongXml(xmlPath, b"wrong 'name' ('%s')" % name)
        if EFFECT_MATERIAL_PROPERTIES.get(name) is not None:
            _raiseWrongXml(xmlPath, b"name duplication ('%s')" % name)
        EFFECT_MATERIAL_PROPERTIES[name] = {}
        hardnessMap = s.readVector2(b'hardness_map')
        if hardnessMap:
            EFFECT_MATERIAL_PROPERTIES[name][b'hardness_map'] = [
             hardnessMap[0], hardnessMap[1]]
        if s.readBool(b'not_ground_material'):
            NOT_GROUND_MATERIALS.append(name)

    ResMgr.purge(xmlPath, True)
    return


def _raiseWrongXml(fileName, msg):
    raise SoftException(b"error in '" + fileName + b"': " + msg)
    return


def getWaterMatKind():
    return EFFECT_MATERIAL_IDS_BY_NAMES[b'water'][0]


_init()
