from __future__ import absolute_import
import CGF, Triggers
from GenericComponents import Sequence
from cgf_script.registration import ComponentProperty

class FortRushCapturePointComponentDescr(object):
    category = b'CapturePoint'
    domain = CGF.Domain.All
    editorTitle = b'Capture Point Component'
    trigger = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'AreaTrigger', value=Triggers.AreaTriggerComponent)
    sequence = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'SequenceComponent', value=Sequence)
    capturablePointName = ComponentProperty(type=CGF.PropertyType.String, editorName=b'capturablePointName')
