from visual_script.block import Block, Meta
from visual_script.slot_types import SLOT_TYPE
from visual_script.misc import ASPECT
from visual_script.dependency import dependencyImporter
dependency, sound_constants, aySkeleton, settings, guiShared, accountSettings = dependencyImporter(b'helpers.dependency', b'armory_yard.gui.Scaleform.daapi.view.lobby.hangar.sound_constants', b'armory_yard.gui.game_control.armory_yard_controller', b'Settings', b'gui.shared', b'account_helpers.AccountSettings')

class AYMeta(Meta):

    @classmethod
    def blockColor(cls):
        return 10512127

    @classmethod
    def blockCategory(cls):
        return b'ArmoryYard'

    @classmethod
    def blockIcon(cls):
        return b':vse/blocks/arena'

    @classmethod
    def blockAspects(cls):
        return [ASPECT.HANGAR]


class GetStageSoundEventName(Block, AYMeta):

    def __init__(self, *args, **kwargs):
        super(GetStageSoundEventName, self).__init__(*args, **kwargs)
        self._stageIndex = self._makeDataInputSlot(b'stageIndex', SLOT_TYPE.INT)
        self._soundEventName = self._makeDataOutputSlot(b'soundEventName', SLOT_TYPE.STR, self._execute)
        return

    def _execute(self):
        stageIndex = self._stageIndex.getValue()
        eventName = sound_constants.getStageVoTapeRecorderName(stageIndex)
        self._soundEventName.setValue(eventName)
        return


class IsStageSoundValid(Block, AYMeta):

    def __init__(self, *args, **kwargs):
        super(IsStageSoundValid, self).__init__(*args, **kwargs)
        self._sound = self._makeDataInputSlot(b'sound', SLOT_TYPE.SOUND)
        self._isSoundValid = self._makeDataOutputSlot(b'isSoundValid', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        from gui.impl.gen import R
        sound = self._sound.getValue().name
        if R.sounds.dyn(sound).isValid():
            self._isSoundValid.setValue(True)
            return
        self._isSoundValid.setValue(False)
        return


class GetNextValidSoundStageIndex(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(GetNextValidSoundStageIndex, self).__init__(*args, **kwargs)
        self._inStageIndex = self._makeDataInputSlot(b'inStageIndex', SLOT_TYPE.INT)
        self._outStageIndex = self._makeDataOutputSlot(b'outStageIndex', SLOT_TYPE.INT, self._execute)
        return

    def _execute(self):
        from gui.impl.gen import R
        stageIndex = self._inStageIndex.getValue()
        progress = self.__ayController.getCurrentProgress()
        if progress > self.__ayController.maxNumberOfSteps:
            progress = self.__ayController.maxNumberOfSteps
        for index in range(stageIndex, progress + 1):
            eventName = sound_constants.getStageVoTapeRecorderName(index)
            if R.sounds.dyn(eventName).isValid():
                self._outStageIndex.setValue(index)
                return

        if stageIndex == 0:
            self._outStageIndex.setValue(0)
        else:
            self._outStageIndex.setValue(1)
        return


class GetLastValidSound(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(GetLastValidSound, self).__init__(*args, **kwargs)
        self._inStageIndex = self._makeDataInputSlot(b'inStageIndex', SLOT_TYPE.INT)
        self._outStageIndex = self._makeDataOutputSlot(b'outStageIndex', SLOT_TYPE.INT, self._execute)
        return

    def _execute(self):
        from gui.impl.gen import R
        progress = self.__ayController.getCurrentProgress()
        if progress > self.__ayController.maxNumberOfSteps:
            progress = self.__ayController.maxNumberOfSteps
        for index in range(progress, 0, -1):
            eventName = sound_constants.getStageVoTapeRecorderName(index)
            if R.sounds.dyn(eventName).isValid():
                self._outStageIndex.setValue(index)
                return

        self._outStageIndex.setValue(0)
        return


class NeedToUpdateRecorderLamp(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(NeedToUpdateRecorderLamp, self).__init__(*args, **kwargs)
        self._inlastListenedMessage = self._makeDataInputSlot(b'lastListenedMessage', SLOT_TYPE.INT)
        self._needToUpdate = self._makeDataOutputSlot(b'needToUpdate', SLOT_TYPE.BOOL, self._execute)
        return

    def _execute(self):
        from gui.impl.gen import R
        lastListenedMessage = self._inlastListenedMessage.getValue()
        progress = self.__ayController.getCurrentProgress()
        if progress > self.__ayController.maxNumberOfSteps:
            progress = self.__ayController.maxNumberOfSteps
        for index in range(progress, lastListenedMessage, -1):
            eventName = sound_constants.getStageVoTapeRecorderName(index)
            if R.sounds.dyn(eventName).isValid():
                self._needToUpdate.setValue(True)
                return

        self._needToUpdate.setValue(False)
        return


class GetTotalCountOfStages(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(GetTotalCountOfStages, self).__init__(*args, **kwargs)
        self._totalCount = self._makeDataOutputSlot(b'totalCount', SLOT_TYPE.INT, self._execute)
        return

    def _execute(self):
        self._totalCount.setValue(self.__ayController.maxNumberOfSteps)
        return


class GetCurrentProgress(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(GetCurrentProgress, self).__init__(*args, **kwargs)
        self._progress = self._makeDataOutputSlot(b'progress', SLOT_TYPE.INT, self._execute)
        return

    def _execute(self):
        progress = self.__ayController.getCurrentProgress()
        if progress > self.__ayController.maxNumberOfSteps:
            progress = self.__ayController.maxNumberOfSteps
        self._progress.setValue(progress)
        return


class GetLastListenedMessage(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(GetLastListenedMessage, self).__init__(*args, **kwargs)
        self._index = self._makeDataOutputSlot(b'index', SLOT_TYPE.INT, self._execute)
        return

    def _execute(self):
        currentSeason = self.__ayController.serverSettings.getCurrentSeason()
        if currentSeason is None:
            return
        else:
            self._index.setValue(accountSettings.AccountSettings.getArmoryYard(accountSettings.ArmoryYard.AY_SECTION_LAST_LISTENED_MESSAGE))
            return


class SaveLastListenedMessage(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(SaveLastListenedMessage, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._index = self._makeDataInputSlot(b'index', SLOT_TYPE.INT)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        currentSeason = self.__ayController.serverSettings.getCurrentSeason()
        if currentSeason is None:
            return
        else:
            accountSettings.AccountSettings.setArmoryYard(accountSettings.ArmoryYard.AY_SECTION_LAST_LISTENED_MESSAGE, self._index.getValue())
            self._out.call()
            return


class OnStageMuteSound(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(OnStageMuteSound, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def onStartScript(self):
        guiShared.g_eventBus.addListener(guiShared.events.ArmoryYardEvent.STAGE_MUTE_SOUND, self._execute, guiShared.EVENT_BUS_SCOPE.DEFAULT)
        return

    def onFinishScript(self):
        guiShared.g_eventBus.removeListener(guiShared.events.ArmoryYardEvent.STAGE_MUTE_SOUND, self._execute, guiShared.EVENT_BUS_SCOPE.DEFAULT)
        return

    def _execute(self, event):
        self._out.call()
        return


class OnStageUnmuteSound(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(OnStageUnmuteSound, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def onStartScript(self):
        guiShared.g_eventBus.addListener(guiShared.events.ArmoryYardEvent.STAGE_UNMUTE_SOUND, self._execute, guiShared.EVENT_BUS_SCOPE.DEFAULT)
        return

    def onFinishScript(self):
        guiShared.g_eventBus.removeListener(guiShared.events.ArmoryYardEvent.STAGE_UNMUTE_SOUND, self._execute, guiShared.EVENT_BUS_SCOPE.DEFAULT)
        return

    def _execute(self, event):
        self._out.call()
        return


class OnStageFinish(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(OnStageFinish, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        self._index = self._makeDataOutputSlot(b'index', SLOT_TYPE.INT, None)
        return

    def onStartScript(self):
        guiShared.g_eventBus.addListener(guiShared.events.ArmoryYardEvent.STAGE_FINISHED, self._execute, guiShared.EVENT_BUS_SCOPE.DEFAULT)
        return

    def onFinishScript(self):
        guiShared.g_eventBus.removeListener(guiShared.events.ArmoryYardEvent.STAGE_FINISHED, self._execute, guiShared.EVENT_BUS_SCOPE.DEFAULT)
        return

    def _execute(self, event):
        index = event.ctx[b'index']
        if index > self.__ayController.maxNumberOfSteps:
            index = self.__ayController.maxNumberOfSteps
        self._index.setValue(index)
        self._out.call()
        return


class ActivatePOI(Block, AYMeta):

    def __init__(self, *args, **kwargs):
        super(ActivatePOI, self).__init__(*args, **kwargs)
        self._in = self._makeEventInputSlot(b'in', self._execute)
        self._name = self._makeDataInputSlot(b'name', SLOT_TYPE.STR)
        self._out = self._makeEventOutputSlot(b'out')
        return

    def _execute(self):
        ctx = {}
        ctx[b'name'] = self._name.getValue()
        guiShared.g_eventBus.handleEvent(guiShared.events.ArmoryYardEvent(guiShared.events.ArmoryYardEvent.POI_ACTIVATED, ctx=ctx))
        self._out.call()
        return


class OnStageClick(Block, AYMeta):
    __ayController = dependency.descriptor(aySkeleton.IArmoryYardController)

    def __init__(self, *args, **kwargs):
        super(OnStageClick, self).__init__(*args, **kwargs)
        self._out = self._makeEventOutputSlot(b'out')
        self._index = self._makeDataOutputSlot(b'index', SLOT_TYPE.INT, None)
        return

    def onStartScript(self):
        guiShared.g_eventBus.addListener(guiShared.events.ArmoryYardEvent.STAGE_CLICKED, self._execute, guiShared.EVENT_BUS_SCOPE.DEFAULT)
        return

    def onFinishScript(self):
        guiShared.g_eventBus.removeListener(guiShared.events.ArmoryYardEvent.STAGE_CLICKED, self._execute, guiShared.EVENT_BUS_SCOPE.DEFAULT)
        return

    def _execute(self, event):
        stageIndex = event.ctx[b'stageId']
        self._index.setValue(stageIndex)
        self._out.call()
        return
