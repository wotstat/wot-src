import CGF
from cgf_script.component_meta_class import registerComponent

@registerComponent
class WTHyperionNotificationComponent(object):
    category = b'White Tiger'
    editorTitle = b'Hyperion Notification'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient

    def __init__(self):
        self.enterReactionID = None
        self.exitReactionID = None
        return
