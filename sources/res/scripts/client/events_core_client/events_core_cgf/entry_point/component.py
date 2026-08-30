from enum import Enum
import CGF
from cgf_script.component_meta_class import registerComponent, CGFMetaTypes, ComponentProperty

class EventNames(Enum):
    COSMIC = b'Cosmic'
    HB = b'May'
    PORTAL = b'Portal'
    WT = b'White Tiger'

    @classmethod
    def toDict(cls):
        return {member.value: member.value for member in cls}


@registerComponent
class Event3dEntryPointGoComponent(object):
    editorTitle = b'Event 3D Entry Point Game object'
    category = b'Events Core'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    eventName = ComponentProperty(type=CGFMetaTypes.STRING, value=EventNames.COSMIC, editorName=b'Event name', annotations={b'comboBox': (EventNames.toDict())})


@registerComponent
class EventClickedComponent(object):
    eventName = ComponentProperty(type=CGFMetaTypes.STRING, value=b'', editorName=b'Event name')
