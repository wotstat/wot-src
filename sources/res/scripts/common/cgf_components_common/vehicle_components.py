import CGF, Triggers
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent

@registerComponent
class VehicleDestroyingComponent(object):
    category = b'Vehicle'
    editorTitle = b'Vehicle Destroying Component'
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'AreaTrigger to subscribe', value=Triggers.AreaTriggerComponent)

    def __init__(self):
        self.reactionID = None
        return


@registerComponent
class VehicleDamageLoggerComponent(object):
    category = b'Loggers'
    editorTitle = b'Vehicle Damage Logger Component'
    domain = CGF.DomainOption.DomainServer | CGF.DomainOption.DomainEditor

    def __init__(self):
        self.topMostParentName = None
        return
