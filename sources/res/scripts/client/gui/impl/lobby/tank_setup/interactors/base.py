import typing, Event
from gui.impl.lobby.tank_setup.tank_setup_helper import NONE_ID
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from gui.impl.gen.view_models.views.lobby.tank_setup.common.deal_panel_model import AutoRenewalType
if typing.TYPE_CHECKING:
    from gui.shared.gui_items.Vehicle import Vehicle

class InteractingItem(object):
    _itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = (b'__item', b'onItemUpdated', b'onSlotAction', b'onAcceptComplete')

    def __init__(self, item):
        self.__item = item
        self.onItemUpdated = Event.Event()
        self.onSlotAction = Event.Event()
        self.onAcceptComplete = Event.Event()
        return

    def setItem(self, item):
        self.__item = item
        return

    def getItem(self):
        return self.__item

    def clear(self):
        self.__item = None
        self.onItemUpdated.clear()
        self.onSlotAction.clear()
        self.onAcceptComplete.clear()
        return


class BaseAutoRenewal(object):
    __slots__ = (b'_vehicle', b'_value', b'_typeEquip')

    def __init__(self, vehicle):
        self._vehicle = vehicle
        self._value = None
        self._typeEquip = None
        return

    def getValue(self):
        raise NotImplementedError
        return

    def getLocalValue(self):
        if self._value is None:
            return self.getValue()
        else:
            return self._value

    def setLocalTypeEquip(self, typeEquip):
        self._typeEquip = typeEquip
        return

    def getLocalTypeEquip(self):
        return AutoRenewalType.UNDEFINED

    def setLocalValue(self, value):
        self._value = value
        return

    def changeValue(self, callback):
        raise NotImplementedError
        return

    def updateVehicle(self, vehicle):
        self._vehicle = vehicle
        return


class BaseInteractor(object):
    _itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = (b'_item', b'__autoRenewal')

    def __init__(self, item):
        self._item = None
        self.__autoRenewal = None
        self.setItem(item)
        self.__createAutoRenewal()
        return

    def getName(self):
        return

    def getAutoRenewal(self):
        return self.__autoRenewal

    def getVehicleAfterInstall(self):
        currentVehicle = self.getItem()
        vehicle = self._itemsCache.items.getVehicleCopy(currentVehicle)
        return vehicle

    def getItem(self):
        return self._item.getItem()

    def setItem(self, item):
        self._item = item
        if self.__autoRenewal is not None:
            self.__autoRenewal.updateVehicle(self.getItem())
        return

    def getInstalledLayout(self):
        raise NotImplementedError
        return

    def getCurrentLayout(self):
        raise NotImplementedError
        return

    def getSetupLayout(self):
        raise NotImplementedError
        return

    def getPlayerLayout(self):
        return self.getInstalledLayout()

    def hasChanged(self):
        return self.getInstalledLayout() != self.getCurrentLayout()

    def isPlayerLayout(self):
        return self.getPlayerLayout() == self.getCurrentLayout()

    def itemUpdated(self):
        self._item.onItemUpdated(self.getName())
        return

    def onSlotAction(self, actionType, intCD=NONE_ID, slotID=NONE_ID, leftID=NONE_ID, rightID=NONE_ID, leftIntCD=NONE_ID, rightIntCD=NONE_ID):
        self._item.onSlotAction(self.getName(), actionType, intCD, slotID, leftID, rightID, leftIntCD, rightIntCD)
        return

    def onAcceptComplete(self):
        self._item.onAcceptComplete()
        return

    def revert(self):
        return

    def confirm(self, skipDialog=False):
        return

    def clear(self):
        self._item = None
        return

    def updateFrom(self, vehicle, onlyInstalled):
        return

    def getChangedList(self):
        setOfPrevLayout = set(item.intCD for item in self.getInstalledLayout() if item is not None)
        currentItems = []
        for item in self.getCurrentLayout():
            if item and item.intCD not in setOfPrevLayout:
                currentItems.append(item)

        return currentItems

    def showExitConfirmDialog(self):
        return

    def applyAutoRenewal(self, callback):
        autoRenewal = self.getAutoRenewal()
        if autoRenewal is not None:
            autoRenewal.changeValue(callback)
        else:
            callback(None)
        return

    def applyQuit(self, callback, skipApplyAutoRenewal):
        if skipApplyAutoRenewal:
            callback(None)
        else:
            self.applyAutoRenewal(callback)
        return

    def _createAutoRenewal(self):
        return

    def __createAutoRenewal(self):
        self.__autoRenewal = self._createAutoRenewal()
        return
