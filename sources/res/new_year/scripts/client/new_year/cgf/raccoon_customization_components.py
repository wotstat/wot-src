import CGF
from helpers import dependency
from GenericComponents import DynamicModelComponent, AnimatorComponent
from cgf_script.component_meta_class import registerComponent, ComponentProperty, CGFMetaTypes
from cgf_script.managers_registrator import onAddedQuery, onRemovedQuery
from shared_utils import CONST_CONTAINER
from new_year.skeletons.new_year import ITamagotchiDataProvider, INewYearTamagotchiController
from new_year_common.items.components.ny_constants import RaidState
from debug_utils import LOG_ERROR
from Queue import Queue

class RaccoonCommands(CONST_CONTAINER):
    FOOD = b'food'
    ACTIVITY = b'activity'
    FUN = b'fun'
    MOOD = b'mood'
    TRIGGER_COMMANDS = (
     FOOD, ACTIVITY, FUN)
    STATE_COMMANDS = (MOOD,)


class RaccoonHelperTriggers(CONST_CONTAINER):
    STAND_UP = b'stand_up'
    MOOD_UPDATE = b'mood_update'


class RaccoonObjects(CONST_CONTAINER):
    SCISSORS = b'Scissors'
    TOOTHBRUSH = b'ToothBrush'
    MASSAGER = b'Massager'
    FRUITS = b'Fruits'
    RUSKS = b'Rusks'
    CEREALS = b'Cereals'
    CHUMBLEY = b'Chumbley'
    TANK = b'Tank'
    MOON_ROVER = b'MoonRover'
    GIFT = b'Gift'


class StateMachineNodes(CONST_CONTAINER):
    SCISSORS = b'Care_Scissors'
    TOOTHBRUSH = b'Care_Toothbrush'
    MASSAGER = b'Care_Massager'
    FRUITS = b'Food_Fruits'
    RUSKS = b'Food_Rusks'
    CEREALS = b'Food_Cereals'
    CHUMBLEY = b'Play_Chumbley'
    TANK = b'Play_Tank'
    MOON_ROVER = b'Play_MoonRover'
    SAD = b'Idle_Sad'
    NEUTRAL = b'Idle_Neutral'
    HAPPY = b'Idle_Happy'
    SAD_TRANSITION_NODE = b'Sad_Transition_StandUp'
    DYN_OBJECT_FOOD_NODES = (
     FRUITS, RUSKS, CEREALS)
    DYN_OBJECT_TOY_NODES = (CHUMBLEY, TANK, MOON_ROVER)
    ACTION_NODES = (SCISSORS, TOOTHBRUSH, MASSAGER, FRUITS, RUSKS, CEREALS, CHUMBLEY, TANK, MOON_ROVER)
    IDLE_NODES = (SAD, NEUTRAL, HAPPY)
    TRANSITABLE_NODES = IDLE_NODES + (SAD_TRANSITION_NODE,)


class RaccoonMoodStates(CONST_CONTAINER):
    SAD = 0
    NEUTRAL = 1
    HAPPY = 2


NODE_TO_OBJECT = {(StateMachineNodes.FRUITS): (RaccoonObjects.FRUITS), 
   (StateMachineNodes.RUSKS): (RaccoonObjects.RUSKS), 
   (StateMachineNodes.CEREALS): (RaccoonObjects.CEREALS), 
   (StateMachineNodes.CHUMBLEY): (RaccoonObjects.CHUMBLEY), 
   (StateMachineNodes.TANK): (RaccoonObjects.TANK), 
   (StateMachineNodes.MOON_ROVER): (RaccoonObjects.MOON_ROVER)}

class EffectType(CONST_CONTAINER):
    TOY = b'Toy'
    FOOD = b'Food'


@registerComponent
class RaccoonComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = b'NY Raccoon'
    category = b'New Year'
    toyEffect = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Toy effect', value=CGF.GameObject)
    foodEffect = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Food effect', value=CGF.GameObject)


@registerComponent
class RaccoonRaidControllerComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = b'NY Raccoon Raid Controller'
    category = b'New Year'
    defaultRaccoon = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Default raccoon', value=CGF.GameObject)
    raidRaccoon = ComponentProperty(type=CGFMetaTypes.LINK, editorName=b'Raid raccoon', value=CGF.GameObject)


@registerComponent
class RaccoonRaidComponent(object):
    domain = CGF.DomainOption.DomainClient
    editorTitle = b'NY Raccoon Raid'
    category = b'New Year'


class RaccoonManager(CGF.ComponentManager):
    __slots__ = (b'__model', b'__animator', b'__moodState', b'__moodNeedUpdate', b'__activeFoodObject', b'__activeToyObject', b'__toyEffect', b'__foodEffect', b'__inAnimation', b'__commandQueue', b'__inView', b'__raidAnimationDuration', b'__raidCtrl', b'__skipRaidAnimation', b'__raidExitAtEnd')
    __dataProvider = dependency.descriptor(ITamagotchiDataProvider)
    __tamagotchiCtrl = dependency.descriptor(INewYearTamagotchiController)

    def __init__(self, *args):
        super(RaccoonManager, self).__init__(*args)
        self.__model = None
        self.__animator = None
        self.__raidCtrl = None
        self.__moodState = RaccoonMoodStates.NEUTRAL
        self.__moodNeedUpdate = False
        self.__activeFoodObject = None
        self.__activeToyObject = None
        self.__toyEffect = None
        self.__foodEffect = None
        self.__inAnimation = False
        self.__inView = False
        self.__skipRaidAnimation = False
        self.__raidExitAtEnd = False
        self.__raidAnimationDuration = 0.0
        self.__commandQueue = Queue()
        return

    @property
    def isActive(self):
        return self.__model is not None and self.__animator is not None

    @property
    def raidAnimationDuration(self):
        return self.__raidAnimationDuration

    def isRaidVisualActive(self):
        if not self.__raidCtrl:
            return False
        else:
            raidRaccoon = self.__raidCtrl.raidRaccoon
            return raidRaccoon is not None and raidRaccoon.isValid() and raidRaccoon.isActive()

    def isRaidExitAtEnd(self):
        return self.__raidExitAtEnd

    def activate(self):
        self.__dataProvider.onViewVisibilityChanged += self.__onViewVisibilityChanged
        self.__tamagotchiCtrl.onRaidDataUpdated += self.__onRaidDataUpdated
        return

    def deactivate(self):
        self.__dataProvider.onViewVisibilityChanged -= self.__onViewVisibilityChanged
        self.__tamagotchiCtrl.onRaidDataUpdated -= self.__onRaidDataUpdated
        self.__reset()
        return

    @onAddedQuery(RaccoonComponent, DynamicModelComponent, AnimatorComponent)
    def onAddedRaccoon(self, raccoon, model, animator):
        self.__model = model
        self.__animator = animator
        self.__animator.setIntParam(RaccoonCommands.MOOD, self.__moodState)
        self.__animator.setOnStateNodeChanged(self.__onAnimatorNodeChanged)
        self.__toyEffect = raccoon.toyEffect
        self.__foodEffect = raccoon.foodEffect
        if self.__tamagotchiCtrl.getRaidState() == RaidState.FINISHED:
            self.__model.setPartVisibleByName(RaccoonObjects.GIFT, True)
        else:
            self.__model.setPartVisibleByName(RaccoonObjects.GIFT, False)
        return

    @onRemovedQuery(RaccoonComponent)
    def onRemovedRaccoon(self, _):
        self.__reset()
        return

    @onAddedQuery(RaccoonRaidControllerComponent)
    def onAddedRaccoonRaidController(self, ctrlComponent):
        self.__raidCtrl = ctrlComponent
        if self.__dataProvider.isRaidActive():
            self.__raidCtrl.defaultRaccoon.deactivate()
            self.__raidCtrl.raidRaccoon.activate()
            self.__skipRaidAnimation = True
        else:
            self.__raidCtrl.defaultRaccoon.activate()
            self.__raidCtrl.raidRaccoon.deactivate()
        return

    @onRemovedQuery(RaccoonRaidControllerComponent)
    def onRemovedRaccoonRaidController(self, ctrlComponent):
        self.__raidCtrl = None
        return

    @onAddedQuery(RaccoonRaidComponent, AnimatorComponent)
    def onAddedRaccoonRaidComponent(self, raidComponent, animator):
        self.__raidAnimationDuration = animator.getDuration()
        if self.__skipRaidAnimation:
            animator.stop()
            animator.start(animator.getDuration())
            self.__raidExitAtEnd = True
            self.__skipRaidAnimation = False
        return

    def clearQueue(self):
        with self.__commandQueue.mutex:
            self.__commandQueue.queue.clear()
        return

    def addCommand(self, command, optionalValue=None):
        if not self.isActive:
            return
        else:
            self.__commandQueue.put((command, optionalValue))
            self.__onAnimatorNodeChanged(None)
            return

    def setMoodState(self, moodState):
        if not self.isActive:
            return
        else:
            self.__moodNeedUpdate = self.__moodNeedUpdate or moodState != self.__moodState
            self.__moodState = moodState
            self.__onAnimatorNodeChanged(None)
            return

    def doRaidAction(self):
        if not self.__raidCtrl:
            return
        self.__hideActiveObjects()
        self.__raidExitAtEnd = False
        self.__raidCtrl.defaultRaccoon.deactivate()
        self.__raidCtrl.raidRaccoon.activate()
        return

    def releaseRaidAction(self):
        if not self.__raidCtrl:
            return
        self.__raidExitAtEnd = False
        self.__raidCtrl.raidRaccoon.deactivate()
        self.__raidCtrl.defaultRaccoon.activate()
        return

    def __onViewVisibilityChanged(self, enabled):
        self.__inView = enabled
        if not self.__inView and self.__raidCtrl.defaultRaccoon.isActive:
            self.__hideActiveObjects()
            self.__raidCtrl.defaultRaccoon.deactivate()
            self.__raidCtrl.defaultRaccoon.activate()
        return

    def __hideActiveObjects(self):
        if not self.__model:
            return
        if self.__activeToyObject:
            self.__model.setPartVisibleByName(self.__activeToyObject, False)
        if self.__activeFoodObject:
            self.__model.setPartVisibleByName(self.__activeFoodObject, False)
        return

    def __onRaidDataUpdated(self):
        if not self.__model:
            return
        if self.__tamagotchiCtrl.getRaidState() == RaidState.FINISHED:
            self.__model.setPartVisibleByName(RaccoonObjects.GIFT, True)
        else:
            self.__model.setPartVisibleByName(RaccoonObjects.GIFT, False)
        return

    def __reset(self):
        self.__resetGoCache()
        self.clearQueue()
        self.__activeToyObject = None
        self.__activeFoodObject = None
        self.__commandQueue = Queue()
        return

    def __resetGoCache(self):
        self.__model = None
        self.__animator = None
        self.__toyEffect = None
        self.__foodEffect = None
        return

    def __updateMoodState(self):
        self.__moodNeedUpdate = False
        self.__executeCommand(RaccoonCommands.MOOD, self.__moodState)
        currentNode = self.__animator.getStateNodeName()
        if currentNode in StateMachineNodes.TRANSITABLE_NODES:
            self.__executeCommand(RaccoonHelperTriggers.MOOD_UPDATE)
        return

    def __executeCommand(self, command, optValue=None):
        if command in RaccoonCommands.TRIGGER_COMMANDS or command in RaccoonHelperTriggers.ALL():
            self.__animator.setTrigger(command)
            self.__inAnimation = True
        if command in RaccoonCommands.STATE_COMMANDS and optValue is not None:
            self.__animator.setIntParam(command, optValue)
        return

    def __update(self):
        currentNode = self.__animator.getStateNodeName()
        if currentNode == StateMachineNodes.SAD and (not self.__commandQueue.empty() or self.__moodNeedUpdate):
            self.__executeCommand(RaccoonHelperTriggers.STAND_UP)
            return
        if currentNode not in StateMachineNodes.TRANSITABLE_NODES:
            return
        if self.__commandQueue.empty():
            self.__updateMoodState()
            self.__inAnimation = False
            return
        self.__executeCommand(*self.__commandQueue.get())
        return

    def __onAnimatorNodeChanged(self, _):
        currentNode = self.__animator.getStateNodeName()
        if currentNode in StateMachineNodes.TRANSITABLE_NODES:
            self.__update()
            return
        if currentNode in StateMachineNodes.ACTION_NODES:
            self.__updateMoodState()
        if currentNode in StateMachineNodes.DYN_OBJECT_TOY_NODES:
            self.__activeToyObject = self.__updateDynObject(currentNode, self.__activeToyObject, self.__toyEffect)
        if currentNode in StateMachineNodes.DYN_OBJECT_FOOD_NODES:
            self.__activeFoodObject = self.__updateDynObject(currentNode, self.__activeFoodObject, self.__foodEffect)
        return

    def __updateDynObject(self, currentNode, activeObject, effectGO):
        objectToActivate = NODE_TO_OBJECT[currentNode]
        if objectToActivate != activeObject:
            if activeObject:
                self.__model.setPartVisibleByName(activeObject, False)
            if effectGO and effectGO.isValid():
                if effectGO.isActive():
                    effectGO.deactivate()
                effectGO.activate()
            else:
                LOG_ERROR((b'RaccoonManager: effect GO is empty or invalid for object {}').format(objectToActivate))
            self.__model.setPartVisibleByName(objectToActivate, True)
        return objectToActivate
