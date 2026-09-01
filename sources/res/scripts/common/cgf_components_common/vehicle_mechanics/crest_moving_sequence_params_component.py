from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class CrestMovingSequenceParamsComponent(object):
    category = b'Sequence'
    editorTitle = b'Crest moving sequence params'
    domain = CGF.Domain.All
    sequence0PosLayer = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Sequence 0 position layer', value=b'')
    sequence1PosLayer = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Sequence 1 position layer', value=b'')
    sequence2PosLayer = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Sequence 2 position layer', value=b'')
    sequence3PosLayer = ComponentProperty(type=CGF.PropertyType.String, editorName=b'Sequence 3 position layer', value=b'')
