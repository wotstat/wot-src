from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class StationaryReloadSequenceParamsComponent(object):
    category = b'Sequence'
    editorTitle = b'Stationary reload sequence params'
    domain = CGF.Domain.All
    sequencePreparingLayer = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Sequence preparing layer', value=b'')
    sequenceFinishingLayer = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Sequence finishing layer', value=b'')
