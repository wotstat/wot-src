import CGF, Event
from GenericComponents import VSEComponent
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery

@registerComponent
class TriggerVSEComponent(object):
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor
    eventName = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'event name', value=b'event')

    def __init__(self):
        super(TriggerVSEComponent, self).__init__()
        self.triggerEvent = Event.Event()
        return


class TriggerVSEComponentsManager(CGF.ComponentManager):

    @onAddedQuery(TriggerVSEComponent, VSEComponent)
    def handleComponentAdded(self, triggerVseComponent, vseComponent):
        triggerVseComponent.triggerEvent += vseComponent.context.onTriggerEvent
        return

    @onRemovedQuery(TriggerVSEComponent, VSEComponent)
    def handleComponentRemoved(self, triggerVseComponent, vseComponent):
        triggerVseComponent.triggerEvent -= vseComponent.context.onTriggerEvent
        return
