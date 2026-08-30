import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class MaterialComponent(object):
    category = b'Material'
    editorTitle = b'Material'
    domain = CGF.DomainOption.DomainAll
    kind = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Kind', value=b'', annotations={b'comboBox': {b'ground': b'ground', b'stone': b'stone', 
                     b'wood': b'wood', 
                     b'metal': b'metal', 
                     b'snow': b'snow', 
                     b'sand': b'sand', 
                     b'water': b'water', 
                     b'dirt': b'dirt', 
                     b'oil': b'oil'}})
