import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class WTMissileFlyEffectComponent(object):
    category = b'White Tiger'
    editorTitle = b'Missile Fly Effect'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    effectPrefab = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Effect prefab path', value=b'')
