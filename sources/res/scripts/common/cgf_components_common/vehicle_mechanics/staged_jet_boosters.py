from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty

class StagedJetBoostersControllerDescriptor(object):
    category = b'Vehicle Mechanics'
    editorTitle = b'Staged Jet Boosters Controller'
    domain = CGF.Domain.All
    left = ComponentProperty(CGF.PropertyType.Link, editorName=b'Left Rocket', value=CGF.GameObject)
    right = ComponentProperty(CGF.PropertyType.Link, editorName=b'Right Rocket', value=CGF.GameObject)
    stateController = ComponentProperty(CGF.PropertyType.Link, editorName=b'State Controller', value=CGF.GameObject)
