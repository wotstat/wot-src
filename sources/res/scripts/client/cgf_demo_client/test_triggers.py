import functools, CGF, GameplayDebug, GenericComponents, Triggers
from cgf_demo.demo_category import DEMO_CATEGORY
from cgf_script.component_meta_class import ComponentProperty, CGFMetaTypes, registerComponent
from cgf_script.managers_registrator import onAddedQuery, onProcessQuery
from constants import IS_EDITOR
if IS_EDITOR:
    from cgf_components_common.state_components import HealthComponent
else:
    from HealthComponent import HealthComponent

@registerComponent
class ShowHealthInfoComponent(object):
    category = DEMO_CATEGORY
    domain = CGF.DomainOption.DomainClient | CGF.DomainOption.DomainEditor


@registerComponent
class TestEntranceNotifier(object):
    category = DEMO_CATEGORY
    domain = CGF.DomainOption.DomainClient
    textComponent = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Text component to output', value=GameplayDebug.DebugTextComponent)
    trigger = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'AreaTrigger to subscribe', value=Triggers.AreaTriggerComponent)
    title = ComponentProperty(type=CGFMetaTypes.STRING, editorName=b'Title', value=b'Area')

    def __init__(self):
        super(TestEntranceNotifier, self).__init__()
        self.__log = b''
        self.__messageCount = 0
        return

    def addMessage(self, message):
        if self.__messageCount >= 10:
            self.__log = b''
            self.__messageCount = 0
        self.__messageCount += 1
        self.__log += message
        self.__flushText()
        return

    def __flushText(self):
        text = self.textComponent()
        if text:
            text.setText(self.__log, (0, 0, 0), (1.0, 1.0, 1.0, 1.0))
        return


class EntranceModifierManager(CGF.ComponentManager):

    @onAddedQuery(TestEntranceNotifier)
    def onEntranceAdded(self, entrance):
        trigger = entrance.trigger()
        if trigger:
            trigger.addEnterReaction(functools.partial(self.__onEnter, entrance))
            trigger.addExitReaction(functools.partial(self.__onExit, entrance))
        return

    def __onEnter(self, entrance, who, where):
        transform = who.findComponentByType(GenericComponents.TransformComponent)
        entrance.addMessage((b'\n{0} was entered at {1}').format(entrance.title, transform.worldPosition))
        return

    def __onExit(self, entrance, who, where):
        transform = who.findComponentByType(GenericComponents.TransformComponent)
        entrance.addMessage((b'\n{0} was exited at {1}').format(entrance.title, transform.worldPosition))
        return


class TestHealthMonitoringManager(CGF.ComponentManager):

    @onAddedQuery(CGF.GameObject, ShowHealthInfoComponent, CGF.No(GameplayDebug.DebugTextComponent))
    def onAddedShowHealthInfo(self, go, _):
        go.createComponent(GameplayDebug.DebugTextComponent, b'', (0, 0, 0), (1.0, 1.0, 1.0, 1.0))
        return

    @onProcessQuery(ShowHealthInfoComponent, HealthComponent, GameplayDebug.DebugTextComponent, tickGroup=b'Simulation')
    def showCurrentHealth(self, _, health, debugText):
        debugText.addFrameText(b'Current health: %d, max health: %d' % (health.health, health.maxHealth))
        return

    @onProcessQuery(ShowHealthInfoComponent, GenericComponents.HealthGradationComponent, HealthComponent, GameplayDebug.DebugTextComponent, tickGroup=b'Simulation')
    def showExplosion(self, _, gradation, health, debugText):
        gradations = {(GenericComponents.EHealthGradation.RED_ZONE): b'Red', 
           (GenericComponents.EHealthGradation.YELLOW_ZONE): b'Yellow', 
           (GenericComponents.EHealthGradation.GREEN_ZONE): b'Green'}
        zone = gradation.getHealthZone(health.health, health.maxHealth)
        debugText.addFrameText((b'Gradation: {0}').format(gradations[zone]))
        return
