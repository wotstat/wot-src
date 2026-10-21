import CGF, Triggers
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes

@registerComponent
class BossComponent(object):
    category = b'Portal'
    editorTitle = b'Boss'
    domain = CGF.DomainOption.DomainAll


@registerComponent
class SyncActivationComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = b'Portal'
    editorTitle = b'Sync activation'


@registerComponent
class FrontierObserverComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = b'Portal'
    editorTitle = b'Frontier Observer'
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Trigger', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.enterReactionID = None
        return
