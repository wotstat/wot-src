from __future__ import absolute_import
from future.utils import viewitems
import ResMgr
from Math import Vector3
from items import _xml
from items.writers import shared_writers

def writeWheelsAndGroups(wheelsConfig, section, materialData, chassisName):
    wheelId = 0
    groupId = 0
    defSyncAngle = section.readFloat(b'wheels/leadingWheelSyncAngle', 60)
    for sname, subsection in _xml.getChildren(None, section, b'wheels'):
        if sname == b'group':
            group = wheelsConfig.groups[groupId]
            _xml.rewriteString(subsection, b'template', group.template)
            _xml.rewriteInt(subsection, b'count', group.count)
            _xml.rewriteInt(subsection, b'startIndex', group.startIndex)
            _xml.rewriteFloat(subsection, b'radius', group.radius)
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


def writeTraces(traces, section, cache):
    shared_writers.writeLodDist(traces.lodDist, section, b'traces/lodDist', cache)
    _xml.rewriteString(section, b'traces/bufferPrefs', traces.bufferPrefs)
    _xml.rewriteString(section, b'traces/textureSet', traces.textureSet)
    _xml.rewriteVector2(section, b'traces/size', traces.size)
    _xml.rewriteBool(section, b'traces/activePostmortem', traces.activePostmortem, defaultValue=False)
    return


def writeTrackBasicParams(trackBasicParams, section, cache):
    if trackBasicParams is None:
        return
    else:
        tracksSection = section[b'tracks']
        for childSectionName in tracksSection.keys():
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
        for sname in section.keys():
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


def writeTrackSplineParams(trackSplineParams, section):
    if trackSplineParams is None:
        return
    else:
        if not section.has_key(b'trackNodes'):
            section.createSection(b'trackNodes')
        _xml.rewriteFloat(section, b'trackThickness', trackSplineParams.thickness)
        _xml.rewriteBool(section, b'trackNodes/enable', trackSplineParams.editorData._enable)
        _xml.rewriteBool(section, b'trackNodes/linkBones', trackSplineParams.editorData.linkBones)
        _xml.rewriteFloat(section, b'trackNodes/maxAmplitude', trackSplineParams.maxAmplitude)
        _xml.rewriteFloat(section, b'trackNodes/maxOffset', trackSplineParams.maxOffset)
        _xml.rewriteFloat(section, b'trackNodes/gravity', trackSplineParams.gravity)
        _xml.rewriteFloat(section, b'trackNodes/elasticity', trackSplineParams.editorData.elasticity)
        _xml.rewriteFloat(section, b'trackNodes/damping', trackSplineParams.editorData.damping)
        return


def writeTrackNodes(nodes, section):
    defForwardElastK = section.readFloat(b'trackNodes/forwardElastK', 1.0)
    defBackwardElastK = section.readFloat(b'trackNodes/backwardElastK', 1.0)
    defOffset = section.readFloat(b'trackNodes/offset', 0.0)

    def writeTrackNode(curNode, curSection):
        _xml.rewriteBool(curSection, b'isLeft', curNode.isLeft)
        _xml.rewriteString(curSection, b'name', curNode.name)
        _xml.rewriteFloat(curSection, b'forwardElastK', curNode.forwardElasticityCoeff, defForwardElastK)
        _xml.rewriteFloat(curSection, b'backwardElastK', curNode.backwardElasticityCoeff, defBackwardElastK)
        _xml.rewriteFloat(curSection, b'offset', curNode.initialOffset, defOffset)
        if curNode.leftNodeName:
            _xml.rewriteString(curSection, b'leftSibling', curNode.leftNodeName)
        if curNode.rightNodeName:
            _xml.rewriteString(curSection, b'rightSibling', curNode.rightNodeName)
        return

    if len(nodes) == 0:
        if section.has_key(b'trackNodes'):
            section.deleteSection(b'trackNodes')
        return
    sectionParent = section[b'trackNodes'] if section.has_key(b'trackNodes') else section.createSection(b'trackNodes')
    sectionToSave = None
    for node in nodes:
        for childSectionName, childSection in sectionParent.items():
            if childSectionName == b'node' and node.name == childSection.readString(b'name'):
                sectionToSave = childSection
                break
        else:
            sectionToSave = sectionParent.createSection(b'node')

        writeTrackNode(node, sectionToSave)

    return


def writeGroundNodes(groups, section):

    def writeGroundNode(curGroup, curSection):
        _xml.rewriteString(curSection, b'template', curGroup.nodesTemplate)
        _xml.rewriteInt(curSection, b'startIndex', curGroup.startIndex)
        _xml.rewriteInt(curSection, b'count', curGroup.nodesCount)
        _xml.rewriteBool(curSection, b'isLeft', curGroup.isLeft)
        _xml.rewriteFloat(curSection, b'minOffset', curGroup.minOffset)
        _xml.rewriteFloat(curSection, b'maxOffset', curGroup.maxOffset)
        _xml.rewriteString(curSection, b'affectedWheelsTemplate', curGroup.affectedWheelsTemplate)
        return

    if len(groups) == 0:
        return
    sectionParent = section[b'groundNodes'] if section.has_key(b'groundNodes') else section.createSection(b'groundNodes')
    for childSectionName, childSection in sectionParent.items():
        if childSectionName == b'group':
            sectionParent.deleteSection(childSection)

    for node in groups:
        sectionToSave = sectionParent.createSection(b'group')
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
            return

        def writeModelSets(item, section):
            if len(item.segmentModelSets) < 2:
                return
            modelSetsSection = section.createSection(b'modelSets')
            for modelSetName, modelSet in viewitems(item.segmentModelSets):
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
    for n, e in viewitems(cache._customEffects[b'slip']):
        if e is effect:
            return _xml.rewriteString(section, subsectionName, n)

    return False
