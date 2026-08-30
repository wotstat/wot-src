import CGF
from cgf_script.component_meta_class import CGFMetaTypes, ComponentProperty, registerComponent

@registerComponent
class ChangeModelOnDeathComponent(object):
    category = b'Death'
    editorTitle = b'Change Model On Death Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    modelPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Model path', annotations={b'path': b'*.model'})
    delay = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Delay', value=0.0)

    def __init__(self):
        self.initialModel = None
        return


@registerComponent
class SoundOnDeathComponent(object):
    category = b'Death'
    editorTitle = b'Sound On Death Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    soundPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Sound Prefab', annotations={b'path': b'*.prefab'})
    delay = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGFMetaTypes.BOOL, editorName=b'Attach to GO', value=True)


@registerComponent
class EffectOnDeathComponent(object):
    category = b'Death'
    editorTitle = b'Effect On Death Component'
    domain = CGF.DomainOption.DomainEditor | CGF.DomainOption.DomainClient
    effectPath = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Effect Prefab', annotations={b'path': b'*.prefab'})
    delay = ComponentProperty(type=CGFMetaTypes.FLOAT, editorName=b'Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGFMetaTypes.BOOL, editorName=b'Attach to GO', value=True)
