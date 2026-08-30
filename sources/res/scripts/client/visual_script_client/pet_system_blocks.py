import typing, skeletons.gui.pet_system
from pet_system_common.pet_constants import AnimationStateName, PetHangarObject, PetStateBehavior, PetStaticTrigger, PetTrigger, StorageStaticTrigger
from visual_script.misc import EDITOR_TYPE
from visual_script.type import VScriptEnum
from visual_script.slot_types import SLOT_TYPE
from visual_script import ASPECT
from visual_script.block import Block, Meta
from visual_script.dependency import dependencyImporter
Event, dependency, game_control, event_dispatcher, lobby_entry, ps_states, state_machine, GenericComponents, guiShared = dependencyImporter(b'Event', b'helpers.dependency', b'skeletons.gui.game_control', b'gui.shared.event_dispatcher', b'gui.Scaleform.lobby_entry', b'gui.impl.lobby.pet_system.states', b'frameworks.state_machine', b'GenericComponents', b'gui.shared')

class PetSystemMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 16776960

    @classmethod
    def blockCategory(cls):
        return b'PetSystem'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/arena'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class OnEventShow(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(OnEventShow, self).__init__(agent)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._fullscreenNeeded = self._makeDataInputSlot(b'fullscreenNeeded', SLOT_TYPE.BOOL)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        if self.__petController.getActiveEvent():
            self.__petController.showEventView(self._fullscreenNeeded.getValue())
            self._out.call()
        return


class OnFirstClickSend(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(OnFirstClickSend, self).__init__(agent)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        self.__petController.sendFirstClick()
        self._out.call()
        return


class OnPetStorageOpen(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(OnPetStorageOpen, self).__init__(agent)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        if self.__petController.getStateBehavior() == PetStateBehavior.HIDDEN and self.__petController.getActiveEvent():
            self.__petController.showEventView()
        else:
            event_dispatcher.showPetStorageView()
        self._out.call()
        return


class IsInPetStorageView(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(IsInPetStorageView, self).__init__(agent)
        self._state = self._makeDataOutputSlot(b'inState', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        self._state.setValue(self.__petController.isInStorage)
        return


class IsInPetFullscreenEventView(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(IsInPetFullscreenEventView, self).__init__(agent)
        self._state = self._makeDataOutputSlot(b'inState', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        self._state.setValue(self.__petController.isInEventFulscreen)
        return


class PetTriggerEnum(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return b'PetTriggerT'

    @classmethod
    def vs_enum(cls):
        return PetTrigger

    @classmethod
    def nameToIndex(cls, value):
        return cls.vs_enum().ALL.index(value)

    @classmethod
    def _vs_collectEnumEntries(cls):
        entriesData = {}
        for index, name in enumerate(cls.vs_enum().ALL):
            entriesData[name] = index

        return entriesData

    @classmethod
    def vs_aspects(cls):
        return [ASPECT.HANGAR]


class StorageStaticTriggerEnum(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return b'StorageStaticTriggerT'

    @classmethod
    def vs_enum(cls):
        return StorageStaticTrigger

    @classmethod
    def vs_aspects(cls):
        return [ASPECT.HANGAR]


class PetStaticTriggerEnum(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return b'PetStaticTriggerT'

    @classmethod
    def vs_enum(cls):
        return PetStaticTrigger

    @classmethod
    def vs_aspects(cls):
        return [ASPECT.HANGAR]


class AnimationStateNameEnum(VScriptEnum):

    @classmethod
    def vs_name(cls):
        return b'AnimationStateNameT'

    @classmethod
    def vs_enum(cls):
        return AnimationStateName

    @classmethod
    def nameToIndex(cls, value):
        return cls.vs_enum().ALL.index(value)

    @classmethod
    def _vs_collectEnumEntries(cls):
        entriesData = {}
        for index, name in enumerate(cls.vs_enum().ALL):
            entriesData[name] = index

        return entriesData

    @classmethod
    def vs_aspects(cls):
        return [ASPECT.HANGAR]


class GetPetState(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(GetPetState, self).__init__(agent)
        self._state = self._makeDataOutputSlot(b'state', AnimationStateNameEnum.slotType(), self._execute)
        return

    def _execute(self):
        self._state.setValue(AnimationStateNameEnum.nameToIndex(self.__petController.petProxy.petPrefabState))
        return


class OnStateChanged(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(OnStateChanged, self).__init__(agent)
        self._out = self._makeEventOutputSlot(b'out')
        self._state = self._makeDataOutputSlot(b'state', AnimationStateNameEnum.slotType(), None)
        return

    def onStartScript(self):
        self.__petController.petProxy.onUpdatePetPrefabState += self._onUpdatePetState
        return

    def onFinishScript(self):
        self.__petController.petProxy.onUpdatePetPrefabState -= self._onUpdatePetState
        return

    def _onUpdatePetState(self, state):
        self._state.setValue(AnimationStateNameEnum.nameToIndex(state))
        self._out.call()
        return


class OnPetAnimationTriggered(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(OnPetAnimationTriggered, self).__init__(agent)
        self._out = self._makeEventOutputSlot(b'out')
        self._trigger = self._makeDataOutputSlot(b'trigger', PetTriggerEnum.slotType(), None)
        return

    def onStartScript(self):
        self.__petController.petProxy.onTrigger += self._onTrigger
        return

    def onFinishScript(self):
        self.__petController.petProxy.onTrigger -= self._onTrigger
        return

    def _onTrigger(self, trigger):
        self._trigger.setValue(PetTriggerEnum.nameToIndex(trigger))
        self._out.call()
        return


class GetStorageStaticTrigger(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(GetStorageStaticTrigger, self).__init__(agent)
        self._staticTrigger = self._makeDataOutputSlot(b'staticTrigger', StorageStaticTriggerEnum.slotType(), self._execute)
        return

    def _execute(self):
        self._staticTrigger.setValue(self.__petController.storageProxy.storageStaticTrigger)
        return


class OnStorageStaticTriggerChanged(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(OnStorageStaticTriggerChanged, self).__init__(agent)
        self._out = self._makeEventOutputSlot(b'out')
        self._staticTrigger = self._makeDataOutputSlot(b'staticTrigger', StorageStaticTriggerEnum.slotType(), None)
        return

    def onStartScript(self):
        self.__petController.storageProxy.onUpdateStorageStaticTrigger += self._onUpdateStorageStaticTrigger
        return

    def onFinishScript(self):
        self.__petController.storageProxy.onUpdateStorageStaticTrigger -= self._onUpdateStorageStaticTrigger
        return

    def _onUpdateStorageStaticTrigger(self, staticTrigger):
        self._staticTrigger.setValue(staticTrigger)
        self._out.call()
        return


class GetPetStaticTrigger(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(GetPetStaticTrigger, self).__init__(agent)
        self._staticTrigger = self._makeDataOutputSlot(b'staticTrigger', PetStaticTriggerEnum.slotType(), self._execute)
        return

    def _execute(self):
        self._staticTrigger.setValue(self.__petController.petProxy.petStaticTrigger)
        return


class OnPetStaticTriggerChanged(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(OnPetStaticTriggerChanged, self).__init__(agent)
        self._out = self._makeEventOutputSlot(b'out')
        self._staticTrigger = self._makeDataOutputSlot(b'staticTrigger', PetStaticTriggerEnum.slotType(), None)
        return

    def onStartScript(self):
        self.__petController.petProxy.onUpdatePetStaticTrigger += self._onUpdatePetStaticTrigger
        return

    def onFinishScript(self):
        self.__petController.petProxy.onUpdatePetStaticTrigger -= self._onUpdatePetStaticTrigger
        return

    def _onUpdatePetStaticTrigger(self, staticTrigger):
        self._staticTrigger.setValue(staticTrigger)
        self._out.call()
        return


class GetSynergy(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(GetSynergy, self).__init__(agent)
        self._synergy = self._makeDataOutputSlot(b'synergy', SLOT_TYPE.INT, self._execute)
        return

    def _execute(self):
        self._synergy.setValue(self.__petController.petProxy.petSynergyLevel)
        return


class GetIsFirstClickAvailable(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(GetIsFirstClickAvailable, self).__init__(agent)
        self._isAvailable = self._makeDataOutputSlot(b'isAvailable', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        self._isAvailable.setValue(self.__petController.isFirstClickEnable())
        return


class OnSynergyChanged(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(OnSynergyChanged, self).__init__(agent)
        self._out = self._makeEventOutputSlot(b'out')
        self._synergy = self._makeDataOutputSlot(b'synergy', SLOT_TYPE.INT, None)
        return

    def onStartScript(self):
        self.__petController.petProxy.onUpdatePetSynergy += self._onUpdatePetSynergy
        return

    def onFinishScript(self):
        self.__petController.petProxy.onUpdatePetSynergy -= self._onUpdatePetSynergy
        return

    def _onUpdatePetSynergy(self, synergy):
        self._synergy.setValue(synergy)
        self._out.call()
        return


class OnPetObjectHover(Block, PetSystemMeta):

    def __init__(self, agent):
        super(OnPetObjectHover, self).__init__(agent)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._out = self._makeEventOutputSlot(b'out')
        self._isHoverIn = self._makeDataInputSlot(b'isHoverIn', SLOT_TYPE.BOOL)
        self._objectName = self._makeDataInputSlot(b'objectName', SLOT_TYPE.STR, EDITOR_TYPE.ENUM_SELECTOR)
        self._objectName.setEditorData(list(PetHangarObject.ALL))
        return

    def _execute(self):
        if self._isHoverIn.getValue():
            eventType = guiShared.events.PetObjectHoverEvent.HOVER_IN
        else:
            eventType = guiShared.events.PetObjectHoverEvent.HOVER_OUT
        guiShared.g_eventBus.handleEvent(guiShared.events.PetObjectHoverEvent(eventType=eventType, ctx={b'objectName': (self._objectName.getValue())}), scope=guiShared.EVENT_BUS_SCOPE.DEFAULT)
        self._out.call()
        return


class OnPetCanInteractInHangarStateChanged(Block, PetSystemMeta):
    __petController = dependency.descriptor(skeletons.gui.pet_system.IPetSystemController)

    def __init__(self, agent):
        super(OnPetCanInteractInHangarStateChanged, self).__init__(agent)
        self._out = self._makeEventOutputSlot(b'out')
        self._canInteract = self._makeDataOutputSlot(b'canInteract', SLOT_TYPE.BOOL, None)
        return

    def onStartScript(self):
        self.__petController.onUpdateCanInteractInHangar += self._onUpdateCanInteractInHangar
        self._execute()
        return

    def onFinishScript(self):
        self.__petController.onUpdateCanInteractInHangar -= self._onUpdateCanInteractInHangar
        return

    def _execute(self):
        self._canInteract.setValue(self.__petController.canInteractInHangar)
        self._out.call()
        return

    def _onUpdateCanInteractInHangar(self, canInteract):
        self._canInteract.setValue(canInteract)
        self._out.call()
        return
