import math, ResMgr, Math
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
        radiusKey = b'radius' if subsection.has_key(b'radius') else b'geometry/radius'
        if sname == b'group':
            ctx = (
             xmlCtx, b'wheels/group')
            group = chassis_components.WheelGroup(isLeft=_xml.readBool(ctx, subsection, b'isLeft'), template=intern(_xml.readNonEmptyString(ctx, subsection, b'template')), count=_xml.readInt(ctx, subsection, b'count', 1), startIndex=subsection.readInt(b'startIndex', 0), radius=_xml.readPositiveFloat(ctx, subsection, radiusKey), trackPairIndex=subsection.readInt(b'trackPairIdx', 0))
            wheelGroups.append(group)
        elif sname == b'wheel':
            from items.vehicles import _readHitTester, _readArmor
            ctx = (
             xmlCtx, (b'wheels/wheel[{}]').format(wheelId))
            index = _xml.readIntOrNone(ctx, subsection, b'index')
            actualIndex = wheelId if index is None else index
            w = chassis_components.Wheel(index=index, isLeft=_xml.readBool(ctx, subsection, b'isLeft'), radius=_xml.readPositiveFloat(ctx, subsection, radiusKey), nodeName=intern(_xml.readNonEmptyString(ctx, subsection, b'name')), isLeading=subsection.readBool(b'isLeading', False), leadingSyncAngle=subsection.readFloat(b'syncAngle', defSyncAngle), hitTesterManager=_readHitTester(ctx, subsection, b'hitTester', optional=True), materials=_readArmor(ctx, subsection, b'armor', optional=True, index=actualIndex), position=subsection.readVector3(b'wheelPos', (0, 0, 0)), trackPairIndex=subsection.readInt(b'trackPairIdx', 0))
            if IS_EDITOR:
                w.editorData.defSyncAngle = defSyncAngle
            wheels.append(w)
            wheelId += 1

    wheelIndices = [wheel.index for wheel in wheels]
    if sorted(wheelIndices) == range(len(wheels)):
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


def _createNameListByTemplate(startIndex, template, count):
    if template is None:
        return []
    else:
        return [b'%s%d' % (template, i) for i in range(startIndex, startIndex + count)]


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
                startIndex = subsection.readInt(b'startIndex', 0)
                count = _xml.readInt(ctx, subsection, b'count', 1)
                namesTemplate = intern(_xml.readNonEmptyString(ctx, subsection, b'template'))
                affectedWheelsTemplate = _xml.readStringOrNone(ctx, subsection, b'affectedWheelsTemplate')
                groundNodeNames = _createNameListByTemplate(startIndex, namesTemplate, count)
                affectedWheels = _createNameListByTemplate(startIndex, affectedWheelsTemplate, count)
                for i, name in enumerate(groundNodeNames):
                    groundNode = chassis_components.GroundNode(nodeName=name, affectedWheelName=affectedWheels[i] if i < len(affectedWheels) else b'', isLeft=_xml.readBool(ctx, subsection, b'isLeft'), minOffset=_xml.readFloat(ctx, subsection, b'minOffset'), maxOffset=_xml.readFloat(ctx, subsection, b'maxOffset'), collisionSamplesCount=subsection.readInt(b'collisionSamplesCount', 1), hasLiftMode=_xml.readBool(ctx, subsection, b'hasLiftMode', False), trackPairIdx=subsection.readInt(b'trackPairIdx', 0))
                    groundNodes.append(groundNode)

            elif sname == b'node':
                ctx = (
                 xmlCtx, b'groundNodes/node')
                groundNode = chassis_components.GroundNode(nodeName=intern(_xml.readNonEmptyString(ctx, subsection, b'name')), affectedWheelName=_xml.readStringOrEmpty(ctx, subsection, b'affectedWheelName'), isLeft=_xml.readBool(ctx, subsection, b'isLeft'), minOffset=_xml.readFloat(ctx, subsection, b'minOffset'), maxOffset=_xml.readFloat(ctx, subsection, b'maxOffset'), collisionSamplesCount=subsection.readInt(b'collisionSamplesCount', 1), hasLiftMode=_xml.readBool(ctx, subsection, b'hasLiftMode', False), trackPairIdx=subsection.readInt(b'trackPairIdx', 0))
                groundNodes.append(groundNode)

        activePostmortem = _xml.readBool(xmlCtx, section, b'groundNodes/activePostmortem', False)
        lodSettingsSection = section[b'groundNodes/lodSettings']
        if lodSettingsSection is not None:
            lodSettings = shared_readers.readLodSettings(xmlCtx, section[b'groundNodes'], cache)
        else:
            lodSettings = None
        return (tuple(groundGroups), tuple(groundNodes), activePostmortem, lodSettings)


def readTrackNodes(xmlCtx, section):
    if not section.has_key(b'trackNodes'):
        return component_constants.EMPTY_TUPLE
    trackNodes = []
    xmlCtx = (xmlCtx, b'trackNodes')
    for sname, subsection in _xml.getChildren(xmlCtx, section, b'trackNodes'):
        if sname == b'trackPair':
            ctx = (
             xmlCtx, b'trackNodes/trackPair')
            nodes = readTrackPairTrackNodes(ctx, subsection)
            trackNodes.extend(nodes)

    if not trackNodes:
        trackNodes.extend(readTrackPairTrackNodes((xmlCtx, b'trackNodes'), section[b'trackNodes']))
    return tuple(trackNodes)


def readTrackPairTrackNodes(xmlCtx, section):
    trackNodes = []
    defElasticity = _xml.readFloat(xmlCtx, section, b'elasticity', 1500.0)
    defDamping = _xml.readFloat(xmlCtx, section, b'damping', 2.0)
    defForwardElastK = _xml.readFloat(xmlCtx, section, b'forwardElastK', 1.0)
    defBackwardElastK = _xml.readFloat(xmlCtx, section, b'backwardElastK', 1.0)
    defOffset = _xml.readFloat(xmlCtx, section, b'offset', 0.0)
    for sname, subsection in section.items():
        if sname == b'node':
            name = _xml.readStringOrNone(xmlCtx, subsection, b'leftSibling')
            if name is not None:
                leftNodeName = intern(name)
            else:
                leftNodeName = None
            name = _xml.readStringOrNone(xmlCtx, subsection, b'rightSibling')
            if name is not None:
                rightNodeName = intern(name)
            else:
                rightNodeName = None
            trackNode = chassis_components.TrackNode(name=intern(_xml.readNonEmptyString(xmlCtx, subsection, b'name')), isLeft=_xml.readBool(xmlCtx, subsection, b'isLeft'), initialOffset=_xml.readFloat(xmlCtx, subsection, b'offset', defOffset), leftNodeName=leftNodeName, rightNodeName=rightNodeName, trackPairIndex=subsection.readInt(b'trackPairIdx', 0), damping=_xml.readFloat(xmlCtx, subsection, b'damping', defDamping), elasticity=_xml.readFloat(xmlCtx, subsection, b'elasticity', defElasticity), forwardElasticityCoeff=_xml.readFloat(xmlCtx, subsection, b'forwardElastK', defForwardElastK), backwardElasticityCoeff=_xml.readFloat(xmlCtx, subsection, b'backwardElastK', defBackwardElastK))
            trackNodes.append(trackNode)

    return trackNodes


def readTrackSplineParams(xmlCtx, section):
    if not section.has_key(b'trackNodes'):
        return None
    else:
        trackPairs = {}
        trackThicknessDef = section.readFloat(b'trackThickness', -0.0339)
        for sname, subsection in _xml.getChildren(xmlCtx, section, b'trackNodes'):
            if sname == b'trackPair':
                ctx = (
                 xmlCtx, b'trackNodes/trackPair')
                pairParams = readSplineTrackPairParams(ctx, subsection, trackThicknessDef)
                trackPairs[pairParams.trackPairIdx] = pairParams

        if not trackPairs:
            trackPairs[component_constants.MAIN_TRACK_PAIR_IDX] = readSplineTrackPairParams((xmlCtx, b'trackNodes'), section[b'trackNodes'], trackThicknessDef)
        return trackPairs


def readSplineTrackPairParams(xmlCtx, section, trackThicknessDef):
    if section is not None:
        trackSplineParams = chassis_components.TrackSplineParams(trackPairIdx=section.readInt(b'trackPairIdx', 0), thickness=section.readFloat(b'trackThickness', trackThicknessDef), maxAmplitude=section.readFloat(b'maxAmplitude', 0.01), maxOffset=section.readFloat(b'maxOffset', 0.01), gravity=section.readFloat(b'gravity', -9.8))
        if IS_EDITOR:
            trackSplineParams.editorData._enable = section.readBool(b'enable', True)
            trackSplineParams.editorData.linkBones = section.readBool(b'linkBones', False)
            trackSplineParams.editorData.elasticity = section.readFloat(b'elasticity', 1500.0)
    else:
        trackSplineParams = chassis_components.TrackSplineParams(trackPairIdx=0, thickness=component_constants.ZERO_FLOAT, maxAmplitude=component_constants.ZERO_FLOAT, maxOffset=component_constants.ZERO_FLOAT, gravity=component_constants.ZERO_FLOAT)
        if IS_EDITOR:
            trackSplineParams.editorData._enable = True
            trackSplineParams.editorData.linkBones = False
            trackSplineParams.editorData.elasticity = 1500.0
    return trackSplineParams


def readTraces(xmlCtx, section, centerOffset, cache):
    tracesSection = section[b'traces']
    if tracesSection is None:
        return
    else:
        tracesParams = {}
        for sectName, subsection in tracesSection.items():
            if sectName != b'tracesParams':
                continue
            idx = _xml.readInt(xmlCtx, subsection, b'trackPairIdx')
            tracesParams[idx] = chassis_components.Traces(bufferPrefs=intern(_xml.readNonEmptyString(xmlCtx, subsection, b'bufferPrefs')), textureSet=intern(_xml.readNonEmptyString(xmlCtx, subsection, b'textureSet')), centerOffset=centerOffset, centerOffsetFactor=subsection.readVector2(b'centerOffsetFactor', Math.Vector2(1, 1)), offset=subsection.readVector2(b'offset', Math.Vector2(0, 0)), size=_xml.readPositiveVector2(xmlCtx, subsection, b'size'), trackPairIdx=idx)

        if len(tracesParams) == 0:
            tracesParams[component_constants.MAIN_TRACK_PAIR_IDX] = chassis_components.Traces(bufferPrefs=intern(_xml.readNonEmptyString(xmlCtx, tracesSection, b'bufferPrefs')), textureSet=intern(_xml.readNonEmptyString(xmlCtx, tracesSection, b'textureSet')), centerOffset=centerOffset, centerOffsetFactor=tracesSection.readVector2(b'centerOffsetFactor', Math.Vector2(1, 1)), offset=tracesSection.readVector2(b'offset', Math.Vector2(0, 0)), size=_xml.readPositiveVector2(xmlCtx, tracesSection, b'size'), trackPairIdx=component_constants.MAIN_TRACK_PAIR_IDX)
        tracesConfig = chassis_components.TracesConfig(tracesParams=tracesParams, lodDist=shared_readers.readLodDist(xmlCtx, tracesSection, b'lodDist', cache), activePostmortem=_xml.readBool(xmlCtx, tracesSection, b'activePostmortem', False))
        return tracesConfig


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
    splineSegmentModelSets = {b'default': (chassis_components.SplineSegmentModelSet(modelsSetName=b'default', left=_xml.readNonEmptyString(xmlCtx, section, b'segmentModelLeft'), right=_xml.readNonEmptyString(xmlCtx, section, b'segmentModelRight'), secondLeft=_xml.readStringOrNone(xmlCtx, section, b'segment2ModelLeft') or b'', secondRight=_xml.readStringOrNone(xmlCtx, section, b'segment2ModelRight') or b''))}
    modelSetsSection = section[b'modelSets']
    if modelSetsSection:
        for sname, subSection in modelSetsSection.items():
            splineSegmentModelSets[sname] = chassis_components.SplineSegmentModelSet(modelsSetName=sname, left=_xml.readNonEmptyString(xmlCtx, subSection, b'segmentModelLeft'), right=_xml.readNonEmptyString(xmlCtx, subSection, b'segmentModelRight'), secondLeft=_xml.readStringOrNone(xmlCtx, subSection, b'segment2ModelLeft') or b'', secondRight=_xml.readStringOrNone(xmlCtx, subSection, b'segment2ModelRight') or b'')

    length = _xml.readFloat(xmlCtx, section, b'segmentLength')
    offset = _xml.readFloat(xmlCtx, section, b'segmentOffset', 0)
    offset2 = _xml.readFloat(xmlCtx, section, b'segment2Offset', 0)
    castShadows = _xml.readBool(xmlCtx, section, b'castShadows', True)
    trackPairIdx = section.readInt(b'trackPairIdx', 0)
    atlasUTiles = section.readInt(b'atlas/UTiles', 1)
    atlasVTiles = section.readInt(b'atlas/VTiles', 1)
    leftDesc = _xml.readStringOrNone(xmlCtx, section, b'left')
    rightDesc = _xml.readStringOrNone(xmlCtx, section, b'right')
    return SplineTrackPairDesc(trackPairIdx, splineSegmentModelSets, leftDesc, rightDesc, length, offset, offset2, atlasUTiles, atlasVTiles, castShadows)


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
