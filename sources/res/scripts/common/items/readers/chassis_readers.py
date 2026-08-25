from __future__ import absolute_import
import math
from future.utils import lrange
from past.builtins import intern
import ResMgr
from items import _xml
from items.components import chassis_components
from items.components import component_constants
from items.components.chassis_components import SplineTrackPairDesc
from items.readers import shared_readers
from debug_utils import LOG_ERROR
from constants import IS_EDITOR, IS_CLIENT, IS_UE_EDITOR
if IS_UE_EDITOR or IS_CLIENT:
    import Vehicular

def readWheelsAndGroups(xmlCtx, section):
    wheelGroups = []
    wheels = []
    wheelId = 0
    defSyncAngle = section.readFloat(b'wheels/leadingWheelSyncAngle', 60)
    for sname, subsection in _xml.getChildren(xmlCtx, section, b'wheels'):
        if sname == b'group':
            ctx = (
             xmlCtx, b'wheels/group')
            group = chassis_components.WheelGroup(isLeft=_xml.readBool(ctx, subsection, b'isLeft'), template=intern(_xml.readNonEmptyString(ctx, subsection, b'template')), count=_xml.readInt(ctx, subsection, b'count', 1), startIndex=subsection.readInt(b'startIndex', 0), radius=_xml.readPositiveFloat(ctx, subsection, b'radius'))
            wheelGroups.append(group)
        elif sname == b'wheel':
            from items.vehicles import _readHitTester, _readArmor
            ctx = (
             xmlCtx, (b'wheels/wheel[{}]').format(wheelId))
            radiusKey = b'radius' if subsection.has_key(b'radius') else b'geometry/radius'
            index = _xml.readIntOrNone(ctx, subsection, b'index')
            actualIndex = wheelId if index is None else index
            w = chassis_components.Wheel(index=index, isLeft=_xml.readBool(ctx, subsection, b'isLeft'), radius=_xml.readPositiveFloat(ctx, subsection, radiusKey), nodeName=intern(_xml.readNonEmptyString(ctx, subsection, b'name')), isLeading=subsection.readBool(b'isLeading', False), leadingSyncAngle=subsection.readFloat(b'syncAngle', defSyncAngle), hitTesterManager=_readHitTester(ctx, subsection, b'hitTester', optional=True), materials=_readArmor(ctx, subsection, b'armor', optional=True, index=actualIndex), position=subsection.readVector3(b'wheelPos', (0, 0, 0)))
            if IS_EDITOR:
                w.editorData.defSyncAngle = defSyncAngle
            wheels.append(w)
            wheelId += 1

    wheelIndices = [wheel.index for wheel in wheels]
    if sorted(wheelIndices) == lrange(len(wheels)):
        sortedWheels = [
         None] * len(wheels)
        for wheel in wheels:
            sortedWheels[wheel.index] = wheel

        wheels = sortedWheels
    elif wheelIndices == [None] * len(wheels):
        pass
    else:
        LOG_ERROR(b'Invalid wheel index detected', xmlCtx, wheels)
    return (tuple(wheelGroups), tuple(wheels))


def readGroundNodesAndGroups(xmlCtx, section, cache):
    if section[b'groundNodes'] is None:
        return (component_constants.EMPTY_TUPLE, component_constants.EMPTY_TUPLE, False, None)
    else:
        groundGroups = []
        groundNodes = []
        for sname, subsection in _xml.getChildren(xmlCtx, section, b'groundNodes'):
            if sname == b'group':
                ctx = (
                 xmlCtx, b'groundNodes/group')
                group = chassis_components.GroundNodeGroup(isLeft=_xml.readBool(ctx, subsection, b'isLeft'), minOffset=_xml.readFloat(ctx, subsection, b'minOffset'), maxOffset=_xml.readFloat(ctx, subsection, b'maxOffset'), nodesTemplate=intern(_xml.readNonEmptyString(ctx, subsection, b'template')), affectedWheelsTemplate=_xml.readStringOrNone(ctx, subsection, b'affectedWheelsTemplate'), nodesCount=_xml.readInt(ctx, subsection, b'count', 1), startIndex=subsection.readInt(b'startIndex', 0), collisionSamplesCount=subsection.readInt(b'collisionSamplesCount', 1), hasLiftMode=_xml.readBool(ctx, subsection, b'hasLiftMode', False))
                groundGroups.append(group)
            elif sname == b'node':
                ctx = (
                 xmlCtx, b'groundNodes/node')
                groundNode = chassis_components.GroundNode(nodeName=intern(_xml.readNonEmptyString(ctx, subsection, b'name')), affectedWheelName=_xml.readStringOrEmpty(ctx, subsection, b'affectedWheelName'), isLeft=_xml.readBool(ctx, subsection, b'isLeft'), minOffset=_xml.readFloat(ctx, subsection, b'minOffset'), maxOffset=_xml.readFloat(ctx, subsection, b'maxOffset'), collisionSamplesCount=_xml.readInt(ctx, subsection, b'collisionSamplesCount', 1), hasLiftMode=_xml.readBool(ctx, subsection, b'hasLiftMode', False))
                groundNodes.append(groundNode)

        activePostmortem = _xml.readBool(xmlCtx, section, b'groundNodes/activePostmortem', False)
        lodSettingsSection = section[b'groundNodes/lodSettings']
        if lodSettingsSection is not None:
            lodSettings = shared_readers.readLodSettings(xmlCtx, section[b'groundNodes'], cache)
        else:
            lodSettings = None
        return (tuple(groundGroups), tuple(groundNodes), activePostmortem, lodSettings)


def readTrackNodes(xmlCtx, section):
    if section[b'trackNodes'] is None:
        return component_constants.EMPTY_TUPLE
    else:
        defElasticity = _xml.readFloat(xmlCtx, section, b'trackNodes/elasticity', 1500.0)
        defDamping = _xml.readFloat(xmlCtx, section, b'trackNodes/damping', 1.0)
        defForwardElastK = _xml.readFloat(xmlCtx, section, b'trackNodes/forwardElastK', 1.0)
        defBackwardElastK = _xml.readFloat(xmlCtx, section, b'trackNodes/backwardElastK', 1.0)
        defOffset = _xml.readFloat(xmlCtx, section, b'trackNodes/offset', 0.0)
        trackNodes = []
        xmlCtx = (
         xmlCtx, b'trackNodes')
        for sname, subsection in _xml.getChildren(xmlCtx, section, b'trackNodes'):
            if sname == b'node':
                ctx = (
                 xmlCtx, b'trackNodes/node')
                name = _xml.readStringOrNone(ctx, subsection, b'leftSibling')
                if name is not None:
                    leftNodeName = intern(name)
                else:
                    leftNodeName = None
                name = _xml.readStringOrNone(ctx, subsection, b'rightSibling')
                if name is not None:
                    rightNodeName = intern(name)
                else:
                    rightNodeName = None
                trackNode = chassis_components.TrackNode(name=intern(_xml.readNonEmptyString(ctx, subsection, b'name')), isLeft=_xml.readBool(ctx, subsection, b'isLeft'), initialOffset=_xml.readFloat(ctx, subsection, b'offset', defOffset), leftNodeName=leftNodeName, rightNodeName=rightNodeName, damping=_xml.readFloat(ctx, subsection, b'damping', defDamping), elasticity=_xml.readFloat(ctx, subsection, b'elasticity', defElasticity), forwardElasticityCoeff=_xml.readFloat(ctx, subsection, b'forwardElastK', defForwardElastK), backwardElasticityCoeff=_xml.readFloat(ctx, subsection, b'backwardElastK', defBackwardElastK))
                trackNodes.append(trackNode)

        return tuple(trackNodes)


def readTrackSplineParams(xmlCtx, section):
    trackSplineParams = None
    if IS_EDITOR:
        if not section.has_key(b'trackThickness'):
            return
    if section[b'trackNodes'] is not None:
        ctx = (
         xmlCtx, b'trackNodes')
        trackSplineParams = chassis_components.TrackSplineParams(thickness=_xml.readFloat(ctx, section, b'trackThickness'), maxAmplitude=_xml.readFloat(ctx, section, b'trackNodes/maxAmplitude'), maxOffset=_xml.readFloat(ctx, section, b'trackNodes/maxOffset'), gravity=_xml.readFloat(ctx, section, b'trackNodes/gravity'))
        if IS_EDITOR:
            trackSplineParams.editorData._enable = _xml.readBool(ctx, section, b'trackNodes/enable', True)
            trackSplineParams.editorData.elasticity = _xml.readFloat(ctx, section, b'trackNodes/elasticity', 1500.0)
            trackSplineParams.editorData.linkBones = _xml.readBool(ctx, section, b'trackNodes/linkBones', False)
    elif section[b'splineDesc'] is not None or section[b'physicalTracks'] is not None:
        trackSplineParams = chassis_components.TrackSplineParams(thickness=_xml.readFloat(xmlCtx, section, b'trackThickness'), maxAmplitude=component_constants.ZERO_FLOAT, maxOffset=component_constants.ZERO_FLOAT, gravity=component_constants.ZERO_FLOAT)
    return trackSplineParams


def readTraces(xmlCtx, section, centerOffset, cache):
    return chassis_components.Traces(lodDist=shared_readers.readLodDist(xmlCtx, section, b'traces/lodDist', cache), bufferPrefs=intern(_xml.readNonEmptyString(xmlCtx, section, b'traces/bufferPrefs')), textureSet=intern(_xml.readNonEmptyString(xmlCtx, section, b'traces/textureSet')), centerOffset=centerOffset, size=_xml.readPositiveVector2(xmlCtx, section, b'traces/size'), activePostmortem=_xml.readBool(xmlCtx, section, b'traces/activePostmortem', False))


def readTrackBasicParams(xmlCtx, section, cache):
    tracksSection = section[b'tracks']
    if tracksSection is None:
        return
    else:
        trackPairs = {}
        for sname, subsection in _xml.getChildren(xmlCtx, section, b'tracks'):
            if sname == b'trackPair':
                ctx = (
                 xmlCtx, b'tracks/trackPair')
                idx = _xml.readInt(ctx, subsection, b'trackPairIdx')
                trackPairs[idx] = chassis_components.TrackPairParams(leftMaterial=intern(_xml.readNonEmptyString(ctx, subsection, b'leftMaterial')), rightMaterial=intern(_xml.readNonEmptyString(ctx, subsection, b'rightMaterial')), textureScale=_xml.readFloat(ctx, subsection, b'textureScale'), tracksDebris=__readDebrisParams(ctx, subsection, cache))

        if len(trackPairs) == 0:
            trackPairs[component_constants.MAIN_TRACK_PAIR_IDX] = chassis_components.TrackPairParams(leftMaterial=intern(_xml.readNonEmptyString(xmlCtx, section, b'tracks/leftMaterial')), rightMaterial=intern(_xml.readNonEmptyString(xmlCtx, section, b'tracks/rightMaterial')), textureScale=_xml.readFloat(xmlCtx, section, b'tracks/textureScale'), tracksDebris=__readDebrisParams(xmlCtx, section[b'tracks'], cache))
        return chassis_components.TrackBasicVisualParams(lodDist=shared_readers.readLodDist(xmlCtx, section, b'tracks/lodDist', cache), trackPairs=trackPairs)


def __readDebrisParams(xmlCtx, section, cache):
    result = [
     None, None]
    for name, (ctx, subSection) in _xml.getItemsWithContext(xmlCtx, section, b'trackDebris'):
        isLeft = _xml.readBool(ctx, subSection, b'isLeft')
        idx = 0 if isLeft else 1
        if result[idx] is not None:
            _xml.raiseWrongXml(ctx, name, b'isLeft is the same')
        destructionEffect = _xml.readStringOrEmpty(ctx, subSection, b'destructionEffect')
        physicalParams = None
        if subSection[b'physicalParams'] is not None:
            physicalParams = Vehicular.PhysicalDestroyedTrackConfig(subSection[b'physicalParams'])
        nodesRemap = {}
        for key, value in subSection.items():
            if key == b'remapNode':
                nodeName = _xml.readString(ctx, value, b'from')
                remapNode = _xml.readString(ctx, value, b'to')
                nodesRemap[nodeName] = remapNode

        result[idx] = chassis_components.TrackDebrisParams(destructionEffect, physicalParams, cache.getVehicleEffect(destructionEffect), nodesRemap)

    if result[0] and result[1]:
        return chassis_components.TrackPairDebris(result[0], result[1])
    else:
        return


def readLeveredSuspension(xmlCtx, section, cache):
    leveredSection = section[b'leveredSuspension']
    if leveredSection is None:
        return
    else:
        levers = []
        for sname, subsection in _xml.getChildren(xmlCtx, section, b'leveredSuspension'):
            if sname != b'lever':
                continue
            ctx = (
             xmlCtx, b'leveredSuspension/lever')
            limits = _xml.readVector2(ctx, subsection, b'limits')
            lever = chassis_components.SuspensionLever(startNodeName=intern(_xml.readNonEmptyString(ctx, subsection, b'startNode')), jointNodeName=intern(_xml.readNonEmptyString(ctx, subsection, b'jointNode')), trackNodeName=intern(_xml.readNonEmptyString(ctx, subsection, b'trackNode')), minAngle=math.radians(limits.x), maxAngle=math.radians(limits.y), collisionSamplesCount=subsection.readInt(b'collisionSamplesCount', 1), hasLiftMode=_xml.readBool(ctx, subsection, b'hasLiftMode', False), affectedWheelName=_xml.readStringOrEmpty(ctx, subsection, b'affectedWheelName'))
            levers.append(lever)

        ctx = (xmlCtx, b'leveredSuspension')
        leveredSuspensionConfig = chassis_components.LeveredSuspensionConfig(levers=levers, interpolationSpeedMul=_xml.readFloat(ctx, leveredSection, b'interpolationSpeedMul', 10.0), lodSettings=shared_readers.readLodSettings(ctx, leveredSection, cache), activePostmortem=_xml.readBool(ctx, leveredSection, b'activePostmortem', False))
        return leveredSuspensionConfig


def readSplineTrackPairDesc(xmlCtx, section, cache):
    splineSegmentModelSets = {b'default': (chassis_components.SplineSegmentModelSet(left=_xml.readNonEmptyString(xmlCtx, section, b'segmentModelLeft'), right=_xml.readNonEmptyString(xmlCtx, section, b'segmentModelRight'), secondLeft=_xml.readStringOrNone(xmlCtx, section, b'segment2ModelLeft') or b'', secondRight=_xml.readStringOrNone(xmlCtx, section, b'segment2ModelRight') or b''))}
    modelSetsSection = section[b'modelSets']
    if modelSetsSection:
        for sname, subSection in modelSetsSection.items():
            splineSegmentModelSets[sname] = chassis_components.SplineSegmentModelSet(left=_xml.readNonEmptyString(xmlCtx, subSection, b'segmentModelLeft'), right=_xml.readNonEmptyString(xmlCtx, subSection, b'segmentModelRight'), secondLeft=_xml.readStringOrNone(xmlCtx, subSection, b'segment2ModelLeft') or b'', secondRight=_xml.readStringOrNone(xmlCtx, subSection, b'segment2ModelRight') or b'')

    length = _xml.readFloat(xmlCtx, section, b'segmentLength')
    offset = _xml.readFloat(xmlCtx, section, b'segmentOffset', 0)
    offset2 = _xml.readFloat(xmlCtx, section, b'segment2Offset', 0)
    trackPairIdx = section.readInt(b'trackPairIdx', 0)
    atlasUTiles = section.readInt(b'atlas/UTiles', 1)
    atlasVTiles = section.readInt(b'atlas/VTiles', 1)
    leftDesc = _xml.readStringOrNone(xmlCtx, section, b'left')
    rightDesc = _xml.readStringOrNone(xmlCtx, section, b'right')
    return SplineTrackPairDesc(trackPairIdx, splineSegmentModelSets, leftDesc, rightDesc, length, offset, offset2, atlasUTiles, atlasVTiles)


def readSplineConfig(xmlCtx, section, cache):
    if not section.has_key(b'splineDesc'):
        return None
    else:
        trackPairs = {}
        for sname, subsection in _xml.getChildren(xmlCtx, section, b'splineDesc'):
            if sname == b'trackPair':
                ctx = (
                 xmlCtx, b'splineDesc/trackPair')
                desc = readSplineTrackPairDesc(ctx, subsection, cache)
                trackPairs[desc.trackPairIdx] = desc

        if not trackPairs:
            trackPairs[component_constants.MAIN_TRACK_PAIR_IDX] = readSplineTrackPairDesc((xmlCtx, b'splineDesc'), section[b'splineDesc'], cache)
        return chassis_components.SplineConfig(trackPairs, shared_readers.readLodDist(xmlCtx, section, b'splineDesc/lodDist', cache))
