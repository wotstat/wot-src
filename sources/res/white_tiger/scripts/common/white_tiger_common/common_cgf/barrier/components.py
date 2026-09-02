import CGF
from cgf_script.component_meta_class import registerComponent, registerReplicableComponent

@registerReplicableComponent
class WTBarrierComponent(object):
    editorTitle = b'WT Barrier'
    category = b'White Tiger'


@registerComponent
class WTBarrierHelperComponent(object):
    editorTitle = b'WT Barrier Helper'
    category = b'White Tiger'
    domain = CGF.DomainOption.DomainAll

    def __init__(self, avatarID):
        self.avatarID = avatarID
        return


@registerComponent
class WTBarrierRotatorComponent(object):
    category = b'White Tiger'
    domain = CGF.DomainOption.DomainServer

    def __init__(self, settingDistance):
        self.settingDistance = settingDistance
        return
