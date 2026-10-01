import CGF, Math
from Event import Event
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerReplicableComponent, registerComponent
from debug_utils import LOG_DEBUG

@registerComponent
class PortalGuidedMissileComponent(object):
    domain = CGF.DomainOption.DomainAll
    category = b'Portal'
    editorTitle = b'Guided Missile'
    direction = ComponentProperty(type=CGFMetaTypes.VECTOR3, editorName=b'Direction', value=Math.Vector3(1, 0, 0))
    avatarId = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'Avatar Id', value=-1)
    currentSpeed = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Current Speed', value=5.0)
    baseSpeed = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Base Speed', value=5.0)
    targetSpeed = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Target Speed', value=15.0)
    accelerationRate = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Acceleration Rate', value=3.0)
    rotationRate = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'rotation Rate', value=3.0)
    explosionRadius = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Explosion Radius ', value=100.0)
    armorDamage = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Armor Damage ', value=100.0)
    deviceDamage = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Device Damage ', value=100.0)
    equipmentID = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'Equipment Id', value=-1)
    shellID = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'Shell Id', value=-1)
    explosionPrefabPath = ComponentProperty(type=CGFMetaTypes.STRING, value=b'', editorName=b'Explosion Prefab Path', annotations={b'path': b'*.prefab'})
    flightTime = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Flight Time', value=10.0)
    deployTime = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Deploy Time', value=5.0)


@registerReplicableComponent
class GuidedMissileReplicableComponent(object):
    category = b'Portal'
    editorTitle = b'Guided Missile Replicable Component'
    replicableAvatarId = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'IntValue', value=-1)
    isDeploying = ComponentProperty(type=CGFMetaTypes.BOOL, editorName=b'BoolValue', value=True)

    def __init__(self):
        self.onReplicatedAvatarId = Event()
        self.onDeployFinished = Event()
        self.onDetonate = Event()
        return

    def set_replicableAvatarId(self, old):
        LOG_DEBUG(b'GuidedMissileReplicableComponent::set_replicableAvatarId')
        self.onReplicatedAvatarId(self, self.replicableAvatarId)
        return

    def set_isDeploying(self, old):
        LOG_DEBUG(b'GuidedMissileReplicableComponent::set_isDeploying')
        self.onDeployFinished(self, self.replicableAvatarId)
        return

    def set_isDetonateProjectile(self, prev):
        LOG_DEBUG(b'GuidedMissileReplicableComponent: detonate projectile')
        self.onDetonate(self)
        return
