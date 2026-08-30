import CGF
from cgf_script.component_meta_class import registerComponent, CGFMetaTypes, ComponentProperty

class EventNames(object):
    COSMIC = b'cosmic_event'


@registerComponent
class Event3dEntryPointGoComponent(object):
    editorTitle = b'Event 3D Entry Point Game object'
    category = b'Events'
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    eventName = ComponentProperty(type=CGFMetaTypes.STRING, value=EventNames.COSMIC, editorName=b'Event name', annotations={b'comboBox': {(EventNames.COSMIC): (EventNames.COSMIC)}})
    hoverOn = ComponentProperty(type=CGFMetaTypes.STRING, value=b'', editorName=b'Cursor hover sound')
    hoverOff = ComponentProperty(type=CGFMetaTypes.STRING, value=b'', editorName=b'Cursor hoverOff sound')
    click = ComponentProperty(type=CGFMetaTypes.STRING, value=b'', editorName=b'Click sound')


@registerComponent
class EventClickedComponent(object):
    eventName = ComponentProperty(type=CGFMetaTypes.STRING, value=b'', editorName=b'Event name')
