from __future__ import absolute_import
import AccountCommands, random
from BaseAccountExtensionComponent import BaseAccountExtensionComponent
from PlayerEvents import g_playerEvents as events
from constants import IS_DEVELOPMENT
from debug_utils import LOG_DEBUG_DEV
from white_tiger.skeletons.white_tiger_controller import IWhiteTigerController
from helpers import dependency
from items import vehicles
from skeletons.gui.shared import IItemsCache
from gui.prb_control.dispatcher import g_prbLoader
from gui.ClientUpdateManager import g_clientUpdateManager
_HARRIERS = [
 b'usa:A120_M48A5_hound_TLXXL', b'france:F18_Bat_Chatillon25t_hound_TLXXL',
 b'ussr:R97_Object_140_hound_TLXXL', b'czech:Cz04_T50_51_Waf_Hound_3DSt']

class WhiteTigerAccountComponent(BaseAccountExtensionComponent):
    __wtController = dependency.descriptor(IWhiteTigerController)
    __itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self):
        BaseAccountExtensionComponent.__init__(self)
        g_clientUpdateManager.addCallbacks({b'tokens': (self.__onTokensUpdate)})
        events.onAccountBecomeNonPlayer += self.onBecomeNonPlayer
        self.__isFakeQueueSwitchEnabled = False
        return

    def onBecomeNonPlayer(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        events.onAccountBecomeNonPlayer -= self.onBecomeNonPlayer
        return

    def getWhiteTigerController(self):
        return self.__wtController

    def enqueueBattle(self, queueType, vehInvID):
        if not events.isPlayerEntityChanging:
            self.base.doCmdIntArr(AccountCommands.REQUEST_ID_NO_RESPONSE, AccountCommands.CMD_ENQUEUE_IN_BATTLE_QUEUE, (
             queueType, vehInvID))
        return

    def dequeueBattle(self, queueType):
        if not events.isPlayerEntityChanging:
            self.base.doCmdInt(AccountCommands.REQUEST_ID_NO_RESPONSE, AccountCommands.CMD_DEQUEUE_FROM_BATTLE_QUEUE, queueType)
        return

    def enableQueueSwitchSimulator(self):
        if IS_DEVELOPMENT:
            self.__isFakeQueueSwitchEnabled = True
            LOG_DEBUG_DEV(b'Queue simulator enabled')
        return

    def __simulateRequeue(self, vehicleType):
        vehTypeCompDescr = vehicles.VehicleDescr(typeName=vehicleType).type.compactDescr
        data = self.__itemsCache.items.inventory.getItemData(vehTypeCompDescr)
        g_prbLoader.getDispatcher().getEntity().requeue(vehInvID=data.invID)
        return

    def __onTokensUpdate(self, diff):
        if self.__isFakeQueueSwitchEnabled and IS_DEVELOPMENT:
            if b'wtevent:quick_ticket_boss' in diff.keys():
                self.__isFakeQueueSwitchEnabled = False
                self.__simulateRequeue(b'germany:G98_Waffentrager_E100_TLXXL')
                LOG_DEBUG_DEV(b'Try switching to Waffentrager queue - cheat disabled')
            elif b'wtevent:quick_ticket_hunter' in diff.keys():
                self.__isFakeQueueSwitchEnabled = False
                self.__simulateRequeue(random.choice(_HARRIERS))
                LOG_DEBUG_DEV(b'Try switching to random harrier queue - cheat disabled')
            return
        return
