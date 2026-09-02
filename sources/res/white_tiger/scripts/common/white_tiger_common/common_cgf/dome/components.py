import typing, CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent, registerReplicableComponent
if typing.TYPE_CHECKING:
    from typing import Optional, Dict
    from white_tiger_common.wt_constants import WT_TEAMS

@registerReplicableComponent
class WTDomeComponent(object):
    editorTitle = b'WT Dome'
    category = b'White Tiger'
    duration = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Dome duration', value=20.0)


@registerComponent
class WTDomeAreaComponent(object):
    editorTitle = b'WT Dome Area'
    category = b'White Tiger'
    domain = CGF.DomainOption.DomainAll

    def __init__(self):
        self.enterReactionID = 0
        self.exitReactionID = 0
        self.factors = None
        self.affectedTeam = None
        return
