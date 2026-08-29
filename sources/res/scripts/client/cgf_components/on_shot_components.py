import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent

@registerComponent
class EffectOnShotComponent(object):
    category = b'Shooting'
    editorTitle = b'Effect On Shot Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    effectPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Effect Prefab', annotations={b'path': b'*.prefab'})


@registerComponent
class SoundOnShotComponent(object):
    category = b'Shooting'
    editorTitle = b'Sound On Shot Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    soundPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Sound Prefab', annotations={b'path': b'*.prefab'})
