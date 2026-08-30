from collections import namedtuple
from copy import deepcopy
from wrapped_reflection_framework import reflectedNamedTuple, ReflectionMetaclass
from items.components import component_constants
from items.components import path_builder
from items.components import shared_components
__all__ = (b'Wheel', b'WheelGroup', b'TrackPair', b'TrackNode', b'TrackBasicVisualParams', b'TrackPairParams', b'TrackPairDebris', b'TrackDebrisParams', b'GroundNode', b'GroundNodeGroup', b'Traces', b'LeveredSuspensionConfig', b'SuspensionLever', b'SplineSegmentModelSet')
Wheel = reflectedNamedTuple(b'Wheel', (b'index', b'isLeft', b'radius', b'nodeName', b'isLeading', b'leadingSyncAngle', b'hitTesterManager', b'materials', b'position', b'trackPairIndex'))
Wheel.hitTester = property((lambda self: self.hitTesterManager.activeHitTester))
WheelGroup = reflectedNamedTuple(b'WheelGroup', (b'isLeft', b'template', b'count', b'startIndex', b'radius', b'trackPairIndex'))
WheelsConfig = reflectedNamedTuple(b'WheelsConfig', (b'groups', b'wheels'))
TrackPair = namedtuple(b'TrackPair', (b'hitTesterManager', b'materials', b'healthParams'))
TrackPair.hitTester = property((lambda self: self.hitTesterManager.activeHitTester))
TrackNode = reflectedNamedTuple(b'TrackNode', (b'name', b'isLeft', b'initialOffset', b'leftNodeName', b'rightNodeName', b'damping', b'elasticity', b'forwardElasticityCoeff', b'backwardElasticityCoeff', b'trackPairIndex'))
TrackBasicVisualParams = reflectedNamedTuple(b'TrackBasicVisualParams', (b'lodDist', b'trackPairs'))
TrackPairParams = reflectedNamedTuple(b'TrackPairParams', (b'leftMaterial', b'rightMaterial', b'textureScale', b'tracksDebris'))
TrackPairDebris = reflectedNamedTuple(b'TrackPairDebris', (b'left', b'right'))
TrackDebrisParams = reflectedNamedTuple(b'TrackDebrisParams', (b'destructionEffect', b'physicalParams', b'destructionEffectData', b'nodesRemap'))
TrackSplineParams = reflectedNamedTuple(b'TrackSplineParams', (b'trackPairIdx', b'thickness', b'maxAmplitude', b'maxOffset', b'gravity'))
GroundNodesParams = reflectedNamedTuple(b'GroundNodesParams', (b'groundNodes',))
GroundNode = reflectedNamedTuple(b'GroundNode', (b'nodeName', b'affectedWheelName', b'isLeft', b'minOffset', b'maxOffset', b'collisionSamplesCount', b'hasLiftMode', b'trackPairIdx'))
GroundNodeGroup = namedtuple(b'GroundNodeGroup', (b'isLeft', b'minOffset', b'maxOffset', b'nodesTemplate', b'affectedWheelsTemplate', b'nodesCount', b'startIndex', b'collisionSamplesCount', b'hasLiftMode', b'trackPairIdx'))
TracesConfig = reflectedNamedTuple(b'TracesConfig', (b'tracesParams', b'lodDist', b'activePostmortem'))
Traces = reflectedNamedTuple(b'Traces', (b'bufferPrefs', b'textureSet', b'centerOffset', b'centerOffsetFactor', b'offset', b'size', b'trackPairIdx'))
LeveredSuspensionConfig = reflectedNamedTuple(b'LeveredSuspensionConfig', (b'levers', b'interpolationSpeedMul', b'lodSettings', b'activePostmortem'))
SuspensionLever = reflectedNamedTuple(b'SuspensionLever', (b'startNodeName', b'jointNodeName', b'trackNodeName', b'minAngle', b'maxAngle', b'collisionSamplesCount', b'hasLiftMode', b'affectedWheelName'))
SplineSegmentModelSet = reflectedNamedTuple(b'SplineSegmentModelSet', (b'modelsSetName', b'left', b'right', b'secondLeft', b'secondRight'))

class SplineTrackPairDesc(object):
    __metaclass__ = ReflectionMetaclass
    __slots__ = (b'trackPairIdx', b'segmentModelSets', b'leftDesc', b'rightDesc', b'segmentLength', b'segmentOffset', b'segment2Offset', b'atlasUTiles', b'atlasVTiles', b'castShadows')

    def __init__(self, trackPairIdx, segmentModelSets, leftDesc, rightDesc, segmentLength, segmentOffset, segment2Offset, atlasUTiles, atlasVTiles, castShadows):
        self.trackPairIdx = trackPairIdx
        self.leftDesc = leftDesc
        self.rightDesc = rightDesc
        self.segmentLength = segmentLength
        self.segmentOffset = segmentOffset
        self.segment2Offset = segment2Offset
        self.atlasUTiles = atlasUTiles
        self.atlasVTiles = atlasVTiles
        self.castShadows = castShadows
        self.segmentModelSets = {}
        segmentModelSets = segmentModelSets or {}
        for setName, setPaths in segmentModelSets.iteritems():
            left = tuple(path_builder.makeIndexes(setPaths.left))
            right = tuple(path_builder.makeIndexes(setPaths.right))
            if setPaths.secondLeft:
                secondLeft = tuple(path_builder.makeIndexes(setPaths.secondLeft))
            else:
                secondLeft = None
            if setPaths.secondRight:
                secondRight = tuple(path_builder.makeIndexes(setPaths.secondRight))
            else:
                secondRight = None
            self.segmentModelSets[setName] = SplineSegmentModelSet(setName, left, right, secondLeft, secondRight)

        return

    def segmentModelLeft(self, modelSetName=b''):
        modelSet = self._getModelSet(modelSetName)
        return path_builder.makePath(*modelSet.left)

    def segmentModelRight(self, modelSetName=b''):
        modelSet = self._getModelSet(modelSetName)
        return path_builder.makePath(*modelSet.right)

    def segment2ModelLeft(self, modelSetName=b''):
        modelSet = self._getModelSet(modelSetName)
        if modelSet.secondLeft:
            return path_builder.makePath(*modelSet.secondLeft)
        else:
            return

    def segment2ModelRight(self, modelSetName=b''):
        modelSet = self._getModelSet(modelSetName)
        if modelSet.secondRight:
            return path_builder.makePath(*modelSet.secondRight)
        else:
            return

    def _getModelSet(self, modelSetName):
        modelSet = modelSetName if modelSetName in self.segmentModelSets else b'default'
        return self.segmentModelSets[modelSet]

    def prerequisites(self, modelSet):
        res = (
         self.segmentModelRight(modelSet), self.segmentModelLeft(modelSet), self.segment2ModelRight(modelSet),
         self.segment2ModelLeft(modelSet), self.leftDesc, self.rightDesc)
        return res


SplineConfig = reflectedNamedTuple(b'SplineConfig', (b'trackPairs', b'lodDist'))
