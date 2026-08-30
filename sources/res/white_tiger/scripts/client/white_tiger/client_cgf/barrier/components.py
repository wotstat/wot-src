import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class WTBarrierEffectComponent(object):
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    category = b'White Tiger'
    editorTitle = b'WT Effect On Shot Component'
    effectPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Effect Prefab', annotations={b'path': b'*.prefab'})


@registerComponent
class WTBarrierClientComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'White Tiger'

    def __init__(self):
        self.isVisible = False
        return


@registerComponent
class WTBarrierDynamicComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'White Tiger'


@registerComponent
class WTBarrierStaticComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'White Tiger'
