import CGF, Math
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerReplicableComponent, registerComponent

@registerReplicableComponent
class MissileComponent(object):
    category = b'Events Core'
    editorTitle = b'Missile'
    baseSpeed = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Base Speed', value=5.0)
    targetSpeed = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Target Speed', value=15.0)
    accelerationRate = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Acceleration Rate', value=3.0)
    rotationRate = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Rotation Rate', value=3.0)
    flightTime = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Flight Time', value=10.0)
    explosionPrefabPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Explosion Prefab', value=b'', annotations={b'path': b'*.prefab'})
    destinationDirection = ComponentProperty(type=CGFMetaTypes.VECTOR3, editorName=b'Destination Direction', value=Math.Vector3(0, 1, 0))
    canRotate = ComponentProperty(type=CGFMetaTypes.BOOL, editorName=b'canRotate', value=True)

    def __init__(self):
        super(MissileComponent, self).__init__()
        self.currentDirection = self.destinationDirection
        self.currentSpeed = self.baseSpeed
        self.isBoostEnabled = False
        self.replicableAvatarId = -1
        self.flightFinishTime = 0.0
        return


@registerComponent
class MissileDeploymentComponent(object):
    category = b'Events Core'
    editorTitle = b'Missile Deployment'
    domain = CGF.DomainOption.DomainAll
    deployTime = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Deploy Time', value=4.0)
    deployOffset = ComponentProperty(type=CGFMetaTypes.VECTOR3, editorName=b'Deploy Offset', value=Math.Vector3(0, 10, 0))

    def __init__(self, angle=0):
        self.angle = angle
        self.deployTransformCallback = None
        return


@registerComponent
class MissileDetonationComponent(object):
    category = b'Events Core'
    domain = CGF.DomainOption.DomainServer
