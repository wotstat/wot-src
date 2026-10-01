import CGF
from cgf_script.component_meta_class import registerComponent

@registerComponent
class PortalOutlineGoComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    editorTitle = b'Portal Outline Game object'
    category = b'Portal'
