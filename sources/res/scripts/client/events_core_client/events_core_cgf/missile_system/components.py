import CGF
from Math import Vector3
from cgf_script.component_meta_class import registerComponent

@registerComponent
class ClientMissileComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'Events Core'

    def __init__(self, **kwargs):
        self.distanceToTarget = Vector3(0, 0, 0)
        return


@registerComponent
class MissileReplicationDoneComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'Events Core'


@registerComponent
class MissileInputComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'Events Core'
    editorTitle = b'Client Missile Input'


@registerComponent
class FPVModeComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'Events Core'
    editorTitle = b'FPV Mode Comp'


@registerComponent
class ArcadeModeComponent(object):
    domain = CGF.DomainOption.DomainClient
    category = b'Events Core'
    editorTitle = b'Arcade Mode Comp'
