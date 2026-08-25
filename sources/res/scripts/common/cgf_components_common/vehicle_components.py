from __future__ import absolute_import
import CGF, Triggers
from cgf_script.registration import ComponentProperty, registerComponent

@registerComponent
class VehicleDestroyingComponent(object):
    category = b'Vehicle'
    editorTitle = b'Vehicle Destroying Component'
    domain = CGF.Domain.ServerEditor
    trigger = ComponentProperty(type=CGF.PropertyType.Link, editorName=b'AreaTrigger to subscribe', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.reactionID = None
        return


@registerComponent
class VehicleDamageLoggerComponent(object):
    category = b'Loggers'
    editorTitle = b'Vehicle Damage Logger Component'
    domain = CGF.Domain.ServerEditor

    def __init__(self):
        self.topMostParentName = None
        return
