import CGF
from cgf_script.component_meta_class import registerComponent, CGFMetaTypes, ComponentProperty

@registerComponent
class SuperBossFightEffectComponent(object):
    category = b'Portal'
    editorTitle = b'Super Boss Fight Effect'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor


@registerComponent
class SpawnSound3DOnRemove(object):
    category = b'Portal'
    editorTitle = b'Spawn Sound3D On Remove'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    prefabPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'prefab', annotations={b'path': b'*.prefab'})


@registerComponent
class BossHPMarkerComponent(object):
    category = b'Portal'
    editorTitle = b'Boss HP Marker'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
