from __future__ import absolute_import
import CGF
from cgf_script.registration import registerComponent

@registerComponent
class RespawnBlockComponent(object):
    category = b'Respawns'
    editorTitle = b'RespawnBlockComponent'
    domain = CGF.Domain.All

    def __init__(self, initBlock):
        super(RespawnBlockComponent, self).__init__()
        self.blockers = set()
        self.blockers.add(initBlock)
        return


@registerComponent
class PerformRespawnComponent(object):
    category = b'Respawns'
    editorTitle = b'PerformRespawnComponent'
    domain = CGF.Domain.All
