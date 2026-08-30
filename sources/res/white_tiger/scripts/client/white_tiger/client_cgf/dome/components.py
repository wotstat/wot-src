import CGF
from cgf_script.component_meta_class import registerComponent, CGFMetaTypes, ComponentProperty

@registerComponent
class WTDomeClientComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'White Tiger'

    def __init__(self):
        self.enterReactionID = 0
        self.exitReactionID = 0
        return


@registerComponent
class WTDomeClientInDomeHoundEffectComponent(object):
    category = b'White Tiger'
    editorTitle = b'In Dome Hound Effect'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    effectPrefab = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Effect prefab path', value=b'')
