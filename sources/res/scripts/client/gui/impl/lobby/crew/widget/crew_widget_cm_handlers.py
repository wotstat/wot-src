from gui import SystemMessages
from gui.Scaleform.framework.entities.EventSystemEntity import EventSystemEntity
from gui.Scaleform.framework.managers.context_menu import AbstractContextMenuHandler
from gui.Scaleform.locale.MENU import MENU
from gui.impl.dialogs import dialogs
from gui.shared import event_dispatcher
from gui.shared.gui_items.Vehicle import NO_VEHICLE_ID
from gui.shared.gui_items.processors.tankman import TankmanUnload
from gui.shared.utils import decorators
from helpers import dependency
from skeletons.gui.shared import IItemsCache
CM_RETRAIN_COLOR = 13347959

class CREW(object):
    PERSONAL_FILE = b'personalFile'
    RETRAIN = b'retrain'
    CHANGE_CREW_MEMBER = b'changeCrewMember'
    SEND_TO_BARRACKS = b'sendToToBarracks'
    DISMISS = b'dismiss'
    QUICK_TRAINING = b'quickTraining'
    CHANGE_SPECIALIZATION = b'changeSpecialization'


class CrewContextMenuHandler(AbstractContextMenuHandler, EventSystemEntity):
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, cmProxy, ctx=None):
        super(CrewContextMenuHandler, self).__init__(cmProxy, ctx, {(CREW.PERSONAL_FILE): b'showPersonalFile', 
           (CREW.RETRAIN): b'retrain', 
           (CREW.QUICK_TRAINING): b'showQuickTraining', 
           (CREW.CHANGE_CREW_MEMBER): b'changeCrewMember', 
           (CREW.CHANGE_SPECIALIZATION): b'changeSpecialization', 
           (CREW.SEND_TO_BARRACKS): b'sendToToBarracks', 
           (CREW.DISMISS): b'dismiss'})
        return

    def showPersonalFile(self):
        event_dispatcher.showPersonalCase(int(self._tankmanID), previousViewID=self._previousViewID)
        return

    def showQuickTraining(self):
        event_dispatcher.showQuickTraining(tankmanInvID=int(self._tankmanID), previousViewID=self._previousViewID, vehicleInvID=self._vehicle.invID if self._vehicle else NO_VEHICLE_ID)
        return

    def retrain(self):
        dialogs.showRetrainSingleDialog(self._tankmanID, self._vehicle.intCD, targetSlotIdx=self._slotIdx)
        return

    def changeCrewMember(self):
        event_dispatcher.showChangeCrewMember(self._slotIdx, self._vehicle.invID, self._previousViewID)
        return

    @decorators.adisp_process(b'unloading')
    def sendToToBarracks(self):
        tankman = self.itemsCache.items.getTankman(self._tankmanID)
        result = yield TankmanUnload(self._vehicle.invID, tankman.vehicleSlotIdx).request()
        if result.userMsg:
            SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType)
        return

    def dismiss(self):
        dialogs.showDismissTankmanDialog(int(self._tankmanID))
        return

    def changeSpecialization(self):
        event_dispatcher.showTankChange(tankmanInvID=int(self._tankmanID), slotIDX=self._slotIdx, previousViewID=self._previousViewID)
        return

    def _generateOptions(self, ctx=None):
        isNotLocked = not self._vehicle.isCrewLocked if self._vehicle else True
        isRetrainAvailable = False
        if self._vehicle:
            for _, tman in self._vehicle.crew:
                if tman and tman.invID == self._tankmanID:
                    isRetrainAvailable = not tman.isMaxCurrentVehicleSkillsEfficiency
                    break

        return [
         self._makeItem(CREW.PERSONAL_FILE, MENU.contextmenu(b'crewWidgetPersonalFile')),
         self._makeItem(CREW.RETRAIN, MENU.contextmenu(b'crewWidgetRetrain'), {b'visible': isRetrainAvailable, b'textColor': CM_RETRAIN_COLOR}),
         self._makeItem(CREW.QUICK_TRAINING, MENU.contextmenu(b'crewWidgetQuickTraining')),
         self._makeItem(CREW.CHANGE_CREW_MEMBER, MENU.contextmenu(b'crewWidgetChangeCrewMember'), {b'enabled': (self._vehicle and isNotLocked)}),
         self._makeItem(CREW.CHANGE_SPECIALIZATION, MENU.contextmenu(b'crewWidgetChangeSpecialization'), {b'enabled': isNotLocked}),
         self._makeItem(CREW.SEND_TO_BARRACKS, MENU.contextmenu(b'crewWidgetSendToToBarracks'), {b'enabled': (self._vehicle and isNotLocked)}),
         self._makeItem(CREW.DISMISS, MENU.contextmenu(b'crewWidgetDismiss'), {b'enabled': isNotLocked})]

    def _initFlashValues(self, ctx):
        self._slotIdx = int(ctx.slotIdx)
        self._tankmanID = int(ctx.tankmanID)
        previousViewID = ctx.previousViewID
        self._previousViewID = int(previousViewID) if previousViewID else None
        self._tankman = self.itemsCache.items.getTankman(self._tankmanID)
        self._vehicle = self.itemsCache.items.getVehicle(self._tankman.vehicleInvID) if self._tankman and self._tankman.vehicleInvID > 0 else None
        return

    def _clearFlashValues(self):
        self._slotIdx = None
        self._tankmanID = None
        self._tankman = None
        self._vehicle = None
        self._previousViewID = None
        return
