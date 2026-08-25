from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class ShotColorTransmissionComponent(object):
    editorTitle = b'Gun Shot Effect Component'
    category = b'Animator Triggers'
    domain = CGF.Domain.ClientEditor
    materialParam = ComponentProperty(type=CGF.PropertyType.String, editorName=b'material property', value=b'TintColor')
    startValue = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'start value', value=0.0)
    endValue = ComponentProperty(type=CGF.PropertyType.Float, editorName=b'end value', value=0.5)
