import CGF
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class WTRegenerationSoundComponent(object):
    category = b'White Tiger'
    editorTitle = b'Regeneration Sound Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    impulsEvent = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Sound impulse event', value=b'')
    interruptEvent = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Sound interrupt event', value=b'')
    completeEvent = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Sound complete event', value=b'')


@registerComponent
class WTRegenerationComponent(object):
    category = b'White Tiger'
    editorTitle = b'Regeneration Component'
    domain = CGF.DomainOption.DomainClient
