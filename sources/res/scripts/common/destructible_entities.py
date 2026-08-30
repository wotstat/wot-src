from __future__ import absolute_import
import ResMgr
from items import _xml
from constants import IS_CLIENT, IS_BASEAPP, IS_BOT, IS_CELLAPP, IS_WEB
from debug_utils import LOG_DEBUG_DEV
from collections import namedtuple, OrderedDict
if IS_CELLAPP or IS_CLIENT or IS_WEB:
    import material_kinds
    from material_kinds import EFFECT_MATERIAL_INDEXES_BY_NAMES
g_destructibleEntitiesCache = None

class DESTRUCTIBLE_ENTITY_TYPES:
    EPIC_HEADQUARTER = 2
    EPIC_HEADQUARTER89 = 3
    EPIC_HEADQUARTERS = (
     EPIC_HEADQUARTER, EPIC_HEADQUARTER89)


class DestructibleEntitiesCache(object):

    def __init__(self):
        self.destructibleEntityTypes = {}
        self.mapActivityLists = {}
        self.destroyEffectLists = {}
        self.materials = {}
        return

    def getDestructibleEntityType(self, typeID):
        return self.destructibleEntityTypes.get(typeID, None)

    def getMapActivityList(self, name):
        return self.mapActivityLists.get(name, None)

    def getDestroyEffectList(self, name):
        return self.destroyEffectLists.get(name, None)

    def addDestructibleEntityType(self, destructibleEntityType):
        self.destructibleEntityTypes[destructibleEntityType.id] = destructibleEntityType
        return


class DestructibleEntityType(object):
    maxNumStateComponents = property((lambda self: max(len(state.components) for state in self.states.values())))

    def __init__(self, id, displayName, health, destroyedNotificationRadius, materials, observationPoints=(), observedPoints=(), directVisionRadius=None, normalRadioDistance=None):
        self.id = id
        self.displayName = displayName
        self.health = health
        self.destroyedNotificationRadius = destroyedNotificationRadius
        self.materials = materials
        self.states = OrderedDict()
        self.observationPoints = observationPoints
        self.observedPoints = observedPoints
        self.directVisionRadius = directVisionRadius
        self.normalRadioDistance = normalRadioDistance
        return

    def addState(self, name, state):
        self.states[name] = state
        return


class DestructibleEntityState(object):

    def __init__(self):
        self.components = OrderedDict()
        if IS_CLIENT:
            self.effect = None
        return

    def addComponent(self, id, stateComponent):
        self.components[id] = stateComponent
        return

    if IS_CLIENT:

        def setClientProperties(self, effect):
            self.effect = effect
            return


class DestructibleEntityStateComponent(object):

    def __init__(self, destructible, physicsModel):
        self.destructible = destructible
        self.physicsModel = physicsModel
        if IS_CLIENT:
            self.guiNode = None
            self.visualModel = None
        return

    if IS_CLIENT:

        def setClientProperties(self, guiNode, visualModel):
            self.guiNode = guiNode
            self.visualModel = visualModel
            return


def init():
    global g_destructibleEntitiesCache
    g_destructibleEntitiesCache = DestructibleEntitiesCache()
    xmlPath = b'scripts/item_defs/destructible_entities.xml'
    section = ResMgr.openSection(xmlPath)
    if section is None:
        _xml.raiseWrongXml(None, xmlPath, b'can not open or read')
    xmlCtx = (None, xmlPath)
    for _, (typeXmlCtx, typeSection) in _xml.getItemsWithContext(xmlCtx, section, b'type'):
        destructibleEntityType = _readType(typeXmlCtx, typeSection)
        if g_destructibleEntitiesCache.getDestructibleEntityType(destructibleEntityType.id) is not None:
            _xml.raiseWrongXml(typeXmlCtx, b'id', b'duplicate id %s' % destructibleEntityType.id)
        g_destructibleEntitiesCache.addDestructibleEntityType(destructibleEntityType)

    if IS_CLIENT:
        _readDestructibleEntitiesEffects(b'scripts/destructible_entity_effects.xml')
    return


def determineDestructibleEntityTypeID(validVehicleLevels, defaultTypeID):
    validVehicleLevelsType3 = {
     8, 9}
    if set(validVehicleLevels) == validVehicleLevelsType3:
        return 3
    else:
        return defaultTypeID

    return


def _readType(xmlCtx, section):
    id = section.readInt(b'id', -1)
    displayName = section.readString(b'display_name')
    health = section.readFloat(b'health', 100)
    destroyedNotificationRadius = section.readFloat(b'destroyedNotificationRadius', 0)
    materials = _readMaterials(*_xml.getSubSectionWithContext(xmlCtx, section, b'materials'))
    observationPoints = _readPointList(*_xml.getSubSectionWithContext(xmlCtx, section, b'observationPoints'))
    observedPoints = _readPointList(*_xml.getSubSectionWithContext(xmlCtx, section, b'observedPoints'))
    directVisionRadius = section.readFloat(b'directVisionRadius', 0)
    normalRadioDistance = section.readFloat(b'normalRadioDistance', 0)
    destructibleEntityType = DestructibleEntityType(id, displayName, health, destroyedNotificationRadius, materials, observationPoints=observationPoints, observedPoints=observedPoints, directVisionRadius=directVisionRadius, normalRadioDistance=normalRadioDistance)
    for _, (stateXmlCtx, stateSection) in _xml.getChildrenWithContext(xmlCtx, section, b'states'):
        destructibleEntityType.addState(*_readState(stateXmlCtx, stateSection))

    return destructibleEntityType


def _readPointList(xmlCtx, section):
    result = []
    for _, ((_, _), point) in _xml.getItemsWithContext(xmlCtx, section, b'point'):
        result.append(point.asVector3)

    return result


def _readState(xmlCtx, section):
    state = DestructibleEntityState()
    for _, (stateCompXmlCtx, stateCompSection) in _xml.getChildrenWithContext(xmlCtx, section, b'components'):
        state.addComponent(*_readStateComponent(stateCompXmlCtx, stateCompSection))

    if IS_CLIENT:
        effect = section.readString(b'effect', b'')
        if effect == b'':
            effect = None
        state.setClientProperties(effect)
    return (_xml.readString(xmlCtx, section, b'name'), state)


def _readStateComponent(xmlCtx, section):
    destructible = _xml.readBool(xmlCtx, section, b'destructible')
    physicsModel = _xml.readString(xmlCtx, section, b'physics_model')
    component = DestructibleEntityStateComponent(destructible, physicsModel)
    if IS_CLIENT:
        visualModel = _xml.readString(xmlCtx, section, b'visual_model')
        guiNodeName = section.readString(b'gui_node', b'')
        if guiNodeName == b'':
            guiNodeName = None
        component.setClientProperties(guiNodeName, visualModel)
    return (_xml.readString(xmlCtx, section, b'id'), component)


def _readDestructibleEntitiesEffects(filename):
    section = ResMgr.openSection(filename)
    if section is None:
        _xml.raiseWrongXml(None, filename, b'can not open or read')
    mapActivitySection = section[b'map_activities']
    for s in mapActivitySection.values():
        name = s.readString(b'name')
        LOG_DEBUG_DEV(b'name ', name)
        activitySec = s[b'activities']
        activities = activitySec.readStrings(b'activity')
        LOG_DEBUG_DEV(b'activities ', activities)
        g_destructibleEntitiesCache.mapActivityLists[name] = activities

    destructionEffectsSection = section[b'destruction_effects']
    for s in destructionEffectsSection.values():
        name = s.readString(b'name')
        g_destructibleEntitiesCache.destroyEffectLists[name] = s

    return


DestructibleMaterialInfo = namedtuple(b'DestructibleMaterialInfo', (b'kind', b'armor', b'effectMaterialIdx', b'extra', b'vehicleDamageFactor', b'useHitAngle', b'mayRicochet', b'collideOnceOnly', b'checkCaliberForRicochet', b'checkCaliberForHitAngleNorm'))

def _readMaterials(parentXmlCtx, section):
    materials = {}
    if IS_BASEAPP or IS_BOT:
        return materials
    for matName, (xmlCtx, matSection) in _xml.getItemsWithContext(parentXmlCtx, section):
        matKind = material_kinds.IDS_BY_NAMES.get(matName)
        if matKind is None:
            _xml.raiseWrongXml(xmlCtx, matName, b'material kind name is unknown')
        if matKind in materials:
            _xml.raiseWrongXml(xmlCtx, matName, b'duplicate material kind')
        effectMaterialName = _xml.readString(xmlCtx, matSection, b'effectMaterial')
        effectMaterialIdx = EFFECT_MATERIAL_INDEXES_BY_NAMES.get(effectMaterialName)
        if effectMaterialIdx is None:
            _xml.raiseWrongXml(xmlCtx, matName, b'Unknown effect material %s' % effectMaterialName)
        materials[matKind] = DestructibleMaterialInfo(kind=matKind, armor=_xml.readInt(xmlCtx, matSection, b'armor'), extra=None, vehicleDamageFactor=_xml.readFraction(xmlCtx, matSection, b'vehicleDamageFactor'), useHitAngle=_xml.readBool(xmlCtx, matSection, b'useHitAngle'), mayRicochet=_xml.readBool(xmlCtx, matSection, b'mayRicochet'), collideOnceOnly=True, checkCaliberForRicochet=_xml.readBool(xmlCtx, matSection, b'checkCaliberForRicochet'), checkCaliberForHitAngleNorm=_xml.readBool(xmlCtx, matSection, b'checkCaliberForHitAngleNorm'), effectMaterialIdx=effectMaterialIdx)

    return materials
