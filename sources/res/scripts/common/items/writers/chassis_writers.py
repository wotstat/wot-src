from items import _xml
from . import shared_writers
from items.components import component_constants
from Math import Vector3
import ResMgr

def writeWheelsAndGroups(wheelsConfig, section, materialData, chassisName):
    wheelId = 0
    groupId = 0
    defSyncAngle = section.readFloat(b'wheels/leadingWheelSyncAngle', 60)
    for sname, subsection in _xml.getChildren(None, section, b'wheels'):
        if sname == b'group':
            group = wheelsConfig.groups[groupId]
            radiusKey = b'radius' if subsection.has_key(b'radius') else b'geometry/radius'
            _xml.rewriteString(subsection, b'template', group.template)
            _xml.rewriteInt(subsection, b'count', group.count)
            _xml.rewriteInt(subsection, b'startIndex', group.startIndex)
            _xml.rewriteFloat(subsection, radiusKey, group.radius)
            groupId += 1
        elif sname == b'wheel':
            from items.vehicles import _writeHitTester, _writeArmor
            index = _xml.readIntOrNone(None, subsection, b'index')
            if index is not None:
                wheelId = index
            wheel = wheelsConfig.wheels[wheelId]
            radiusKey = b'radius' if subsection.has_key(b'radius') else b'geometry/radius'
            _xml.rewriteInt(subsection, b'index', wheelId, createNew=False)
            _xml.rewriteFloat(subsection, radiusKey, wheel.radius)
            _xml.rewriteString(subsection, b'name', wheel.nodeName)
            _xml.rewriteBool(subsection, b'isLeading', wheel.isLeading, False)
            _xml.rewriteFloat(subsection, b'syncAngle', wheel.leadingSyncAngle, defSyncAngle)
            _xml.rewriteVector3(subsection, b'wheelPos', wheel.position, Vector3(0, 0, 0))
            _writeHitTester(wheel.hitTesterManager, None, subsection, b'hitTester')
            wheelMatData = materialData.get(b'wheel' + str(wheelId), None)
            wheelMatData = wheelMatData.get(chassisName, None) if wheelMatData is not None else None
            _writeArmor(wheel.materials, subsection, wheelMatData)
            wheelId += 1

    return


def writeTraces(tracesConfig, section, cache):
    tracesSection = section[b'traces']
    if tracesSection is None:
        tracesSection = section.createSection(b'traces')
    else:
        for childSectionName, _ in tracesSection.items():
            tracesSection.deleteSection(childSectionName)

    shared_writers.writeLodDist(tracesConfig.lodDist, tracesSection, b'lodDist', cache)
    _xml.rewriteBool(tracesSection, b'activePostmortem', tracesConfig.activePostmortem)
    for _, tracesParams in tracesConfig.tracesParams.iteritems():
        tracesParamsSection = tracesSection.createSection(b'tracesParams')
        _xml.rewriteInt(tracesParamsSection, b'trackPairIdx', tracesParams.trackPairIdx)
        _xml.rewriteString(tracesParamsSection, b'bufferPrefs', tracesParams.bufferPrefs)
        _xml.rewriteString(tracesParamsSection, b'textureSet', tracesParams.textureSet)
        _xml.rewriteVector2(tracesParamsSection, b'size', tracesParams.size)
        _xml.rewriteVector2(tracesParamsSection, b'offset', tracesParams.offset)
        _xml.rewriteVector2(tracesParamsSection, b'centerOffsetFactor', tracesParams.centerOffsetFactor)

    return


def writeTrackBasicParams(trackBasicParams, section, cache):
    if trackBasicParams is None:
        return
    else:
        tracksSection = section[b'tracks']
        for childSectionName, childSection in tracksSection.items():
            tracksSection.deleteSection(childSectionName)

        shared_writers.writeLodDist(trackBasicParams.lodDist, section, b'tracks/lodDist', cache)
        for idx, trackPair in enumerate(trackBasicParams.trackPairs.values()):
            trackPairSection = tracksSection.createSection(b'trackPair')
            trackPairSection.writeInt(b'trackPairIdx', idx)
            __writeTrackPairParams(trackPair, trackPairSection)

        return


def __writeTrackPairParams(trackPairParams, section):
    _xml.rewriteString(section, b'leftMaterial', trackPairParams.leftMaterial)
    _xml.rewriteString(section, b'rightMaterial', trackPairParams.rightMaterial)
    _xml.rewriteFloat(section, b'textureScale', trackPairParams.textureScale)
    __writeDebris(trackPairParams.tracksDebris, section)
    return


def __writeDebris(tracksDebris, section):
    if tracksDebris is None:
        return
    else:
        for sname, subsection in section.items():
            if sname == b'trackDebris':
                section.deleteSection(sname)

        leftDebrisSection = section.createSection(b'trackDebris')
        leftDebrisSection.writeBool(b'isLeft', True)
        leftDebris = tracksDebris.left
        if leftDebris is not None:
            _xml.rewriteString(leftDebrisSection, b'destructionEffect', leftDebris.destructionEffect)
            for key, value in leftDebris.nodesRemap.items():
                remapNodeSection = leftDebrisSection.createSection(b'remapNode')
                remapNodeSection.writeString(b'from', key)
                remapNodeSection.writeString(b'to', value)

            if leftDebris.physicalParams is not None:
                physicalParamsSection = leftDebrisSection.createSection(b'physicalParams')
                leftDebris.physicalParams.save(physicalParamsSection)
        rightDebrisSection = section.createSection(b'trackDebris')
        rightDebrisSection.writeBool(b'isLeft', False)
        rightDebris = tracksDebris.right
        if rightDebris is not None:
            _xml.rewriteString(rightDebrisSection, b'destructionEffect', rightDebris.destructionEffect)
            if rightDebris.nodesRemap is not None:
                for key, value in rightDebris.nodesRemap.items():
                    remapNodeSection = rightDebrisSection.createSection(b'remapNode')
                    remapNodeSection.writeString(b'from', key)
                    remapNodeSection.writeString(b'to', value)

            if rightDebris.physicalParams is not None:
                physicalParamsSection = rightDebrisSection.createSection(b'physicalParams')
                rightDebris.physicalParams.save(physicalParamsSection)
        return


def writeTrackNodesAndSplineParams(nodes, trackSplineParams, section):
    if trackSplineParams is None:
        return
    else:
        if len(nodes) == 0:
            if section.has_key(b'trackNodes'):
                section.deleteSection(b'trackNodes')
            return
        if section.has_key(b'trackThickness'):
            section.deleteSection(b'trackThickness')
        trackNodesSection = section[b'trackNodes'] if section.has_key(b'trackNodes') else section.createSection(b'trackNodes')
        for childSectionName, _ in trackNodesSection.items():
            trackNodesSection.deleteSection(childSectionName)

        def writeSplineParams(params, curSection):
            _xml.rewriteFloat(curSection, b'trackPairIdx', params.trackPairIdx)
            _xml.rewriteFloat(curSection, b'trackThickness', params.thickness)
            _xml.rewriteFloat(curSection, b'maxAmplitude', params.maxAmplitude)
            _xml.rewriteFloat(curSection, b'maxOffset', params.maxOffset)
            _xml.rewriteFloat(curSection, b'gravity', params.gravity)
            _xml.rewriteFloat(curSection, b'damping', params.editorData.damping)
            _xml.rewriteBool(curSection, b'enable', params.editorData._enable)
            _xml.rewriteBool(curSection, b'linkBones', params.editorData.linkBones)
            _xml.rewriteFloat(curSection, b'elasticity', params.editorData.elasticity)
            return

        def writeTrackNode(curNode, curSection):
            _xml.rewriteBool(curSection, b'isLeft', curNode.isLeft)
            _xml.rewriteString(curSection, b'name', curNode.name)
            _xml.rewriteFloat(curSection, b'forwardElastK', curNode.forwardElasticityCoeff, 1.0)
            _xml.rewriteFloat(curSection, b'backwardElastK', curNode.backwardElasticityCoeff, 1.0)
            _xml.rewriteFloat(curSection, b'offset', curNode.initialOffset, 0.0)
            _xml.rewriteFloat(curSection, b'trackPairIdx', curNode.trackPairIndex)
            if curNode.leftNodeName:
                _xml.rewriteString(curSection, b'leftSibling', curNode.leftNodeName)
            if curNode.rightNodeName:
                _xml.rewriteString(curSection, b'rightSibling', curNode.rightNodeName)
            return

        for _, params in trackSplineParams.iteritems():
            pairSection = trackNodesSection.createSection(b'trackPair')
            writeSplineParams(params, pairSection)
            for node in nodes:
                if node.trackPairIndex != params.trackPairIdx:
                    continue
                for childSectionName, childSection in pairSection.items():
                    if childSectionName == b'node' and node.name == childSection.readString(b'name'):
                        sectionToSave = childSection
                        break
                else:
                    sectionToSave = pairSection.createSection(b'node')

                writeTrackNode(node, sectionToSave)

        return


def writeGroundNodes(nodes, section):
    if len(nodes) == 0:
        return
    sectionParent = section[b'groundNodes'] if section.has_key(b'groundNodes') else section.createSection(b'groundNodes')
    for _, childSection in sectionParent.items():
        sectionParent.deleteSection(childSection)

    def writeGroundNode(curNode, curSection):
        _xml.rewriteString(curSection, b'name', curNode.nodeName)
        _xml.rewriteString(curSection, b'affectedWheelName', curNode.affectedWheelName, b'')
        _xml.rewriteInt(curSection, b'collisionSamplesCount', curNode.collisionSamplesCount)
        _xml.rewriteBool(curSection, b'isLeft', curNode.isLeft)
        _xml.rewriteFloat(curSection, b'minOffset', curNode.minOffset)
        _xml.rewriteFloat(curSection, b'maxOffset', curNode.maxOffset)
        _xml.rewriteInt(curSection, b'trackPairIdx', curNode.trackPairIdx)
        return

    for node in nodes:
        sectionToSave = sectionParent.createSection(b'node')
        writeGroundNode(node, sectionToSave)

    return


def writeSplineDesc(splineDesc, section, cache):
    if splineDesc is None:
        return
    else:

        def writeTrackPairParams(item, section):
            segment2ModelLeft = item.segment2ModelLeft()
            segment2ModelRight = item.segment2ModelRight()
            _xml.rewriteInt(section, b'trackPairIdx', item.trackPairIdx)
            _xml.rewriteString(section, b'segmentModelLeft', item.segmentModelLeft())
            _xml.rewriteString(section, b'segmentModelRight', item.segmentModelRight())
            if segment2ModelLeft is not None:
                _xml.rewriteString(section, b'segment2ModelLeft', segment2ModelLeft)
            if segment2ModelRight is not None:
                _xml.rewriteString(section, b'segment2ModelRight', segment2ModelRight)
            _xml.rewriteString(section, b'left', item.leftDesc)
            _xml.rewriteString(section, b'right', item.rightDesc)
            _xml.rewriteFloat(section, b'segmentLength', item.segmentLength)
            _xml.rewriteFloat(section, b'segmentOffset', item.segmentOffset)
            if item.segment2Offset != 0.0:
                _xml.rewriteFloat(section, b'segment2Offset', item.segment2Offset)
            _xml.rewriteInt(section, b'atlas/UTiles', item.atlasUTiles)
            _xml.rewriteInt(section, b'atlas/VTiles', item.atlasVTiles)
            _xml.deleteAndCleanup(section, b'castShadows') if item.castShadows else _xml.rewriteBool(section, b'castShadows', False)
            return

        def writeModelSets(item, section):
            if len(item.segmentModelSets) < 2:
                return
            modelSetsSection = section.createSection(b'modelSets')
            for modelSetName, modelSet in item.segmentModelSets.iteritems():
                if modelSetName == b'default':
                    continue
                currentModelSetSection = modelSetsSection.createSection(modelSetName)
                _xml.rewriteString(currentModelSetSection, b'segmentModelLeft', modelSet.editorLeft)
                _xml.rewriteString(currentModelSetSection, b'segmentModelRight', modelSet.editorRight)
                _xml.rewriteString(currentModelSetSection, b'segment2ModelLeft', modelSet.editorSecondLeft, b'')
                _xml.rewriteString(currentModelSetSection, b'segment2ModelRight', modelSet.editorSecondRight, b'')

            return

        if section.has_key(b'splineDesc'):
            section.deleteSection(b'splineDesc')
        newSplineDescSection = section.insertSection(b'splineDesc', section.getFirstIndex(b'physicalTracks'))
        for trackPair in splineDesc.trackPairs.values():
            pairSection = newSplineDescSection.createSection(b'trackPair')
            writeTrackPairParams(trackPair, pairSection)
            writeModelSets(trackPair, pairSection)

        shared_writers.writeLodDist(splineDesc.lodDist, newSplineDescSection, b'lodDist', cache)
        return


def writeMudEffect(effect, cache, section, subsectionName):
    for n, e in cache._customEffects[b'slip'].iteritems():
        if e is effect:
            return _xml.rewriteString(section, subsectionName, n)

    return False
