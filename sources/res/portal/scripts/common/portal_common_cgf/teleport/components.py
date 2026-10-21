import CGF, Triggers
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent, registerReplicableComponent

@registerComponent
class TeleportSystemComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = b'Portal'
    editorTitle = b'Teleport system component'
    teleportTime = ComponentProperty(CGFMetaTypes.FLOAT, editorName=b'Time for teleport process', value=5.0)
    teleportCooldown = ComponentProperty(CGFMetaTypes.FLOAT, editorName=b'Teleport cooldown', value=10.0)
    placementRadius = ComponentProperty(CGFMetaTypes.FLOAT, editorName=b'Placement search radius', value=5.0)
    placementExcludeRadius = ComponentProperty(CGFMetaTypes.FLOAT, editorName=b'Placement exclude radius', value=0.0)


@registerComponent
class TeleportComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = b'Portal'
    editorTitle = b'Teleport component'
    linkGO = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Destination go link', value=CGF.GameObject)


@registerComponent
class TeleportRequestLinkComponent(object):
    domain = CGF.DomainOption.DomainAll
    category = b'Portal'
    editorTitle = b'Teleport request link component'


@registerReplicableComponent
class TeleportReplicableComponent(object):
    category = b'Portal'
    editorTitle = b'Teleport replicable component'


@registerComponent
class TeleportZoneControllerComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = b'Portal'
    editorTitle = b'Teleport zone controller'
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Teleport area trigger', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.enterReactionID = None
        self.exitReactionID = None
        return


@registerComponent
class TeleportEffectComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    category = b'Portal'
    editorTitle = b'Teleport effect component'
