from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class EffectOnShotComponent(object):
    group = b'Shooting'
    editorTitle = b'Effect On Shot'
    domain = CGF.Domain.ClientEditor
    effectPath = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Effect Prefab', annotations={b'path': b'*.prefab'})


@registerComponent
class SoundOnShotComponent(object):
    group = b'Shooting'
    editorTitle = b'Sound On Shot'
    domain = CGF.Domain.ClientEditor
    soundPath = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Sound Prefab', annotations={b'path': b'*.prefab'})
