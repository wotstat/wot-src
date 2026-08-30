import BigWorld
from Event import Event
from white_tiger_common.common_cgf.dome.components import WTDomeComponent as WTDomeComponentCGF

class WTDomeComponent(WTDomeComponentCGF, BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(WTDomeComponent, self).__init__()
        self.onReplicationDone = Event()
        return

    def onDestroy(self):
        self.onReplicationDone.clear()
        BigWorld.DynamicScriptComponent.onDestroy(self)
        return

    def set_affectedTeam(self, old):
        self.onReplicationDone(self)
        return
