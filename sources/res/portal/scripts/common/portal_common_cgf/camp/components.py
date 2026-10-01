import CGF
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes, registerReplicableComponent

@registerComponent
class CampSystemComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = b'Portal'
    editorTitle = b'Camp system'
    captureSpeed = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Capture speed', value=2.5)
    captureTime = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Capture time', value=100.0)


@registerComponent
class CampComponent(object):
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    category = b'Portal'
    editorTitle = b'Camp'
    name = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Name', value=b'')

    def __init__(self):
        self.enterReactionID = None
        self.exitReactionID = None
        return


@registerReplicableComponent
class CampReplicableComponent(object):
    category = b'Portal'
    editorTitle = b'Camp Replicable'
    canBeCaptured = ComponentProperty(type=CGFMetaTypes.BOOL, value=False)
    isCaptured = ComponentProperty(type=CGFMetaTypes.BOOL, value=False)
    captureProgress = ComponentProperty(type=CGFMetaTypes.FLOAT, value=0.0)
    captureTotal = ComponentProperty(type=CGFMetaTypes.FLOAT, value=0.0)
    captureCurrentSpeed = ComponentProperty(type=CGFMetaTypes.FLOAT, value=0.0)
