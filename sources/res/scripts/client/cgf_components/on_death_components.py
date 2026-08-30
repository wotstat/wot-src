from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class ChangeModelOnDeathComponent(object):
    group = b'Death'
    editorTitle = b'Change Model On Death'
    domain = CGF.Domain.ClientEditor
    modelPath = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Model path', annotations={b'path': b'*.model'})
    delay = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'Delay', value=0.0)

    def __init__(self):
        self.initialModel = None
        return


@registerComponent
class SoundOnDeathComponent(object):
    group = b'Death'
    editorTitle = b'Sound On Death'
    domain = CGF.Domain.ClientEditor
    soundPath = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Sound Prefab', annotations={b'path': b'*.prefab'})
    delay = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGF.PropertyType.Bool, editorName=b'Attach to GO', value=True)


@registerComponent
class EffectOnDeathComponent(object):
    group = b'Death'
    editorTitle = b'Effect On Death'
    domain = CGF.Domain.ClientEditor
    effectPath = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Effect Prefab', annotations={b'path': b'*.prefab'})
    delay = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'Delay', value=0.0)
    attachToGO = ComponentProperty(type=CGF.PropertyType.Bool, editorName=b'Attach to GO', value=True)
