import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerReplicableComponent, registerComponent
_DEFAULT_HEALTH = 300

class DEATH_REASON(object):
    UNKNOWN = 0
    DESTROYED = 1


@registerReplicableComponent
class DeathComponent(object):
    category = b'Common'
    editorTitle = b'Death Component'


@registerReplicableComponent
class HealthComponent(object):
    category = b'Common'
    editorTitle = b'Health Component'
    maxHealth = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'MaxHealth', value=_DEFAULT_HEALTH)
    health = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'CurrentHealth', value=_DEFAULT_HEALTH)


@registerComponent
class RemoveOnDeathComponent(object):
    category = b'Death'
    editorTitle = b'Remove On Death Component'
    domain = CGF.DomainOption.DomainAll
    delay = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Delay', value=0.0)


@registerComponent
class SpawnOnDeathComponent(object):
    category = b'Death'
    editorTitle = b'Spawn On Death Component'
    domain = CGF.DomainOption.DomainAll
    prefabPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Spawn Prefab', annotations={b'path': b'*.prefab'})
    delay = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGFMetaTypes.BOOL, editorName=b'Attach to GO', value=True)


@registerComponent
class StateSwitcherComponent(object):
    category = b'Common'
    editorTitle = b'State Switcher'
    domain = CGF.DomainOption.DomainAll
    normal = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Normal', value=CGF.GameObject)
    damaged = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Damaged', value=CGF.GameObject)
    critical = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Critical', value=CGF.GameObject)

    def __init__(self):
        self.callback = None
        return
