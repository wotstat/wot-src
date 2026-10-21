import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class AreaTriggerDamageComponent(object):
    domain = CGF.DomainOption.DomainAll
    category = b'Portal'
    editorTitle = b'Trigger Damage'
    damageState = ComponentProperty(type=CGFMetaTypes.INT, editorName=b'State', value=0)
    damageStates = ComponentProperty(type=CGFMetaTypes.FLOAT_LIST, editorName=b'Damage States', value=(100.0, 100.0))

    def __init__(self):
        self.reactionID = None
        return
