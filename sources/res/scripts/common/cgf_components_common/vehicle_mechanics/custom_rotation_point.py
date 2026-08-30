from __future__ import absolute_import
import CGF
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class CustomRotationPointComponent(object):
    category = b'Vehicle Mechanics'
    editorTitle = b'Custom Rotation Point Component'
    domain = CGF.Domain.All
    minSpeed = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'Min speed bound (m/s)', value=0)
    minPoints = ComponentProperty(type=CGF.PropertyType.Vector3List, editorName=b'Min points (left, right)', value=[])
    maxSpeed = ComponentProperty(type=CGF.PropertyType.Int, editorName=b'Max speed bound (m/s)', value=0)
    maxPoints = ComponentProperty(type=CGF.PropertyType.Vector3List, editorName=b'Max points (left, right)', value=[])
    changeRailDirection = ComponentProperty(type=CGF.PropertyType.Bool, editorName=b'Change rail direction', value=False)

    def __init__(self):
        self.physicsRef = None
        self.originGimletCOMOffset = None
        self.originRailCOMOffset = None
        return
