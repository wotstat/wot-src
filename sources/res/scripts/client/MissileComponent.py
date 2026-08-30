import BigWorld
from Event import Event
from events_core_common.events_core_cgf.missile_system.components import MissileComponent as MissileComponentCGF

class MissileComponent(MissileComponentCGF, BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(MissileComponent, self).__init__()
        self.onAvatarIdReplicated = Event()
        self.onDetonate = Event()
        return

    def set_replicableAvatarId(self, old):
        self.onAvatarIdReplicated(self, self.replicableAvatarId)
        return

    def set_isDetonateProjectile(self, prev):
        self.onDetonate(self)
        return
