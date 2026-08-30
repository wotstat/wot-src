import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent

@registerComponent
class GunShotEffectComponent(object):
    editorTitle = b'Gun Shot Effect Component'
    category = b'Animator Triggers'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    materialParam = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'material property', value=b'TintlColor')
    startValue = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'start value', value=0.0)
    endValue = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'end value', value=0.5)
