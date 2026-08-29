import BigWorld
from CurrentVehicle import g_currentVehicle
from gui.techtree.research_items_data import ResearchItemsData
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from tutorial.control.triggers import Trigger, TriggerWithSubscription, TriggerWithValidateVar
from tutorial.logger import LOG_DEBUG
__all__ = (b'TimerTrigger', b'IsCollectibleVehicleTrigger', b'CurrentVehicleChangedTrigger', b'ItemsCacheSyncTrigger', b'ResearchGoToNextVehicleTrigger')

class TimerTrigger(TriggerWithValidateVar):

    def __init__(self, triggerID, validateVarID, setVarID=None, validateUpdateOnly=False):
        super(TimerTrigger, self).__init__(triggerID, validateVarID, setVarID, validateUpdateOnly)
        self.__timerCallback = None
        return

    def run(self):
        self.isRunning = True
        if self.__timerCallback is None:
            self.isSubscribed = True
            self.__timerCallback = BigWorld.callback(self.getVar(), self.__updateTimer)
        self.toggle(isOn=False)
        return

    def clear(self):
        if self.__timerCallback is not None:
            BigWorld.cancelCallback(self.__timerCallback)
            self.__timerCallback = None
        self.isSubscribed = False
        self.isRunning = False
        return

    def __updateTimer(self, *args):
        self.__timerCallback = None
        self.toggle(isOn=True)
        return


class IsCollectibleVehicleTrigger(Trigger):

    def run(self):
        g_currentVehicle.onChanged += self.__onCurrentVehicleChanged
        self.toggle(isOn=self.isOn())
        return

    def isOn(self, *args):
        return g_currentVehicle.isCollectible()

    def clear(self):
        g_currentVehicle.onChanged -= self.__onCurrentVehicleChanged
        return

    def __onCurrentVehicleChanged(self):
        self.toggle(isOn=self.isOn())
        return


class CurrentVehicleChangedTrigger(TriggerWithSubscription):

    def __init__(self, triggerID, validateVarID, setVarID=None, validateUpdateOnly=False, unlockTargetIDs=None):
        super(CurrentVehicleChangedTrigger, self).__init__(triggerID, validateVarID, setVarID, validateUpdateOnly)
        self.__unlockTargetIDs = unlockTargetIDs or []
        return

    def _subscribe(self):
        g_currentVehicle.onChanged += self.__onCurrentVehicleChanged
        return

    def _unsubscribe(self):
        g_currentVehicle.onChanged -= self.__onCurrentVehicleChanged
        return

    def __onCurrentVehicleChanged(self):
        LOG_DEBUG(b'CurrentVehicleChangedTrigger.onChanged', self.getID())
        self._tutorial.invalidateFlags()
        for targetID in self.__unlockTargetIDs:
            LOG_DEBUG(b'CurrentVehicleChangedTrigger.unlockState', self.getID(), targetID)
            self._tutorial.unlockState(targetID)

        LOG_DEBUG(b'CurrentVehicleChangedTrigger.toggle', self.getID())
        self.toggle()
        return


class ItemsCacheSyncTrigger(TriggerWithSubscription):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, triggerID, validateVarID, setVarID=None, validateUpdateOnly=False, unlockTargetIDs=None):
        super(ItemsCacheSyncTrigger, self).__init__(triggerID, validateVarID, setVarID, validateUpdateOnly)
        self.__unlockTargetIDs = unlockTargetIDs or []
        return

    def _subscribe(self):
        self.itemsCache.onSyncCompleted += self.__onItemsCacheSyncCompleted
        return

    def _unsubscribe(self):
        self.itemsCache.onSyncCompleted -= self.__onItemsCacheSyncCompleted
        return

    def __onItemsCacheSyncCompleted(self, *_):
        LOG_DEBUG(b'ItemsCacheSyncTrigger.onSyncCompleted', self.getID())
        self._tutorial.invalidateFlags()
        for targetID in self.__unlockTargetIDs:
            LOG_DEBUG(b'ItemsCacheSyncTrigger.unlockState', self.getID(), targetID)
            self._tutorial.unlockState(targetID)

        LOG_DEBUG(b'ItemsCacheSyncTrigger.toggle', self.getID())
        self.toggle()
        return


class ResearchGoToNextVehicleTrigger(TriggerWithSubscription):

    def __init__(self, triggerID, validateVarID, setVarID=None, validateUpdateOnly=False, unlockTargetIDs=None):
        super(ResearchGoToNextVehicleTrigger, self).__init__(triggerID, validateVarID, setVarID, validateUpdateOnly)
        self.__unlockTargetIDs = unlockTargetIDs or []
        return

    def _subscribe(self):
        LOG_DEBUG(b'ResearchGoToNextVehicleTrigger.subscribe', self.getID())
        ResearchItemsData.onGoToNextVehicle += self.__onGoToNextVehicle
        return

    def _unsubscribe(self):
        LOG_DEBUG(b'ResearchGoToNextVehicleTrigger.unsubscribe', self.getID())
        ResearchItemsData.onGoToNextVehicle -= self.__onGoToNextVehicle
        return

    def run(self):
        self.isRunning = True
        LOG_DEBUG(b'ResearchGoToNextVehicleTrigger.run', self.getID(), self.isSubscribed)
        if not self.isSubscribed:
            self.isSubscribed = True
            self._subscribe()
        self.isRunning = False
        return

    def __onGoToNextVehicle(self, oldRootCD, newRootCD):
        LOG_DEBUG(b'ResearchGoToNextVehicleTrigger.onGoToNextVehicle', self.getID(), oldRootCD, newRootCD)
        self._tutorial.invalidateFlags()
        for targetID in self.__unlockTargetIDs:
            LOG_DEBUG(b'ResearchGoToNextVehicleTrigger.unlockState', self.getID(), targetID)
            self._tutorial.unlockState(targetID)

        LOG_DEBUG(b'ResearchGoToNextVehicleTrigger.toggle', self.getID())
        self.toggle()
        return
