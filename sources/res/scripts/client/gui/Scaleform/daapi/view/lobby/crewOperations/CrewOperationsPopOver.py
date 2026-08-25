from __future__ import absolute_import
import BigWorld
from CurrentVehicle import g_currentVehicle
from gui import SystemMessages
from gui.ClientUpdateManager import g_clientUpdateManager
from gui.Scaleform.daapi.view.meta.CrewOperationsPopOverMeta import CrewOperationsPopOverMeta
from gui.Scaleform.locale.CREW_OPERATIONS import CREW_OPERATIONS
from gui.impl.dialogs.dialogs import showRetrainMassiveDialog, showRetrainSingleDialog
from gui.prb_control import prb_getters
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.Vehicle import Vehicle, getLowEfficiencyCrew
from gui.shared.gui_items.items_actions import factory
from gui.shared.gui_items.processors.tankman import TankmanAutoReturn, TankmanReturn
from gui.shared.gui_items.processors.vehicle import VehicleAutoReturnProcessor
from gui.shared.notifications import NotificationPriorityLevel
from gui.shared.utils import decorators
from helpers import dependency
from helpers import i18n
from skeletons.gui.shared import IItemsCache
OPERATION_RETRAIN = b'retrain'
OPERATION_RETURN = b'return'
OPERATION_DROP_IN_BARRACK = b'dropInBarrack'

class CrewOperationsPopOver(CrewOperationsPopOverMeta):
    itemsCache = dependency.descriptor(IItemsCache)
    __slots__ = (b'_ctxData',)

    def __init__(self, ctx):
        super(CrewOperationsPopOver, self).__init__()
        self._ctxData = ctx.get(b'data')
        return

    def _populate(self):
        super(CrewOperationsPopOver, self)._populate()
        g_clientUpdateManager.addCallbacks({b'inventory': (self.onInventoryUpdate)})
        unitMgr = prb_getters.getClientUnitMgr()
        if unitMgr:
            unitMgr.onUnitLeft += self.__unitMgrOnUnitLeft
        self.__update()
        return

    def onWindowClose(self):
        self.destroy()
        return

    def _destroy(self):
        unitMgr = prb_getters.getClientUnitMgr()
        if unitMgr:
            unitMgr.onUnitLeft -= self.__unitMgrOnUnitLeft
        super(CrewOperationsPopOver, self)._destroy()
        return

    def _dispose(self):
        g_clientUpdateManager.removeObjectCallbacks(self)
        super(CrewOperationsPopOver, self)._dispose()
        return

    def invokeOperation(self, operationName):
        if operationName == OPERATION_RETRAIN:
            if self._ctxData:
                crewIds = self._ctxData.get(b'crewIds', [])
                vehicleCD = self._ctxData.get(b'vehicleCD', None)
                if len(crewIds) == 1:
                    slotIdx, tmanIdx = crewIds[0]
                    showRetrainSingleDialog(tmanIdx, vehicleCD, targetSlotIdx=slotIdx)
                else:
                    showRetrainMassiveDialog([tmanID for _, tmanID in crewIds], vehicleCD)
        elif operationName == OPERATION_RETURN:
            self.__processReturnCrew()
        else:
            self.__unloadCrew()
        return

    def onToggleClick(self, operationName):
        self.__autoReturnToggleSwitch()
        return

    @decorators.adisp_process(b'updating')
    def __autoReturnToggleSwitch(self):
        result = yield VehicleAutoReturnProcessor(g_currentVehicle.item, not g_currentVehicle.item.isAutoReturn).request()
        if result.success and g_currentVehicle.item.isAutoReturn:
            result = yield TankmanAutoReturn(g_currentVehicle.item).request()
        if not result.success:
            if result.userMsg:
                SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType, priority=NotificationPriorityLevel.MEDIUM)
        return

    @decorators.adisp_process(b'crewReturning')
    def __processReturnCrew(self):
        result = yield TankmanReturn(g_currentVehicle.item).request()
        if result.userMsg:
            SystemMessages.pushI18nMessage(result.userMsg, type=result.sysMsgType, priority=result.msgPriority)
        return

    def onInventoryUpdate(self, invDiff):
        if GUI_ITEM_TYPE.TANKMAN in invDiff:
            self.__update()
        return

    def __update(self):
        vehicle = g_currentVehicle.item
        dataForUpdate = {b'operationsArray': [
                              self.__getRetrainOperationData(vehicle),
                              self.__getReturnOperationData(vehicle),
                              self.__getDropInBarrackOperationData(vehicle)]}
        self.as_updateS(dataForUpdate)
        return

    def __getRetrainOperationData(self, vehicle):
        crew = vehicle.crew
        if vehicle.isDisabled:
            return self.__getInitCrewOperationObject(OPERATION_RETRAIN, b'locked')
        if self.__isNoCrew(crew):
            return self.__getInitCrewOperationObject(OPERATION_RETRAIN, b'noCrew')
        if self.__isTopCrewForCurrentVehicle(vehicle):
            return self.__getInitCrewOperationObject(OPERATION_RETRAIN, b'alreadyRetrained')
        return self.__getInitCrewOperationObject(OPERATION_RETRAIN)

    def __getReturnOperationData(self, vehicle):
        if vehicle.isInBattle:
            return self.__getInitCrewOperationObject(OPERATION_RETURN, b'vehicleInBattle')
        else:
            crew = vehicle.crew
            lastCrewIDs = vehicle.lastCrew
            if lastCrewIDs is None:
                return self.__getInitCrewOperationObject(OPERATION_RETURN, b'noPrevious')
            freeBerths = self.itemsCache.items.freeTankmenBerthsCount()
            tankmenToBarracksCount = 0
            demobilizedMembersCounter = 0
            isCrewAlreadyInCurrentVehicle = True
            for _, tankman in crew:
                if tankman is not None:
                    tankmenToBarracksCount += 1

            for slotIdx, lastTankmenInvID in enumerate(lastCrewIDs):
                actualLastTankman = self.itemsCache.items.getTankman(lastTankmenInvID)
                if actualLastTankman is None or actualLastTankman.isDismissed:
                    demobilizedMembersCounter += 1
                    continue
                if vehicle.descriptor.type.crewRoles[slotIdx][0] != actualLastTankman.role:
                    continue
                if actualLastTankman.isInTank:
                    lastTankmanVehicle = self.itemsCache.items.getVehicle(actualLastTankman.vehicleInvID)
                    if lastTankmanVehicle:
                        if lastTankmanVehicle.isLocked:
                            return self.__getInitCrewOperationObject(OPERATION_RETURN, None, CREW_OPERATIONS.RETURN_WARNING_MEMBERSINBATTLE_TOOLTIP, True)
                        if lastTankmanVehicle.invID != vehicle.invID:
                            isCrewAlreadyInCurrentVehicle = False
                        else:
                            tankmenToBarracksCount -= 1
                else:
                    isCrewAlreadyInCurrentVehicle = False
                    freeBerths += 1

            if demobilizedMembersCounter > 0 and demobilizedMembersCounter == len(lastCrewIDs):
                return self.__getInitCrewOperationObject(OPERATION_RETURN, b'allDemobilized')
            if isCrewAlreadyInCurrentVehicle:
                warningId = b'lockCrew' if b'lockCrew' in vehicle.descriptor.type.tags else b''
                return self.__getInitCrewOperationObject(OPERATION_RETURN, b'alreadyOnPlaces', warningId=warningId)
            if 0 < demobilizedMembersCounter < len(lastCrewIDs):
                return self.__getInitCrewOperationObject(OPERATION_RETURN, None, CREW_OPERATIONS.RETURN_WARNING_MEMBERDEMOBILIZED_TOOLTIP, True)
            return self.__getInitCrewOperationObject(OPERATION_RETURN)

    def __getDropInBarrackOperationData(self, vehicle):
        crew = vehicle.crew
        if self.__isNoCrew(crew):
            return self.__getInitCrewOperationObject(OPERATION_DROP_IN_BARRACK, b'noCrew')
        else:
            if vehicle.isInBattle:
                return self.__getInitCrewOperationObject(OPERATION_DROP_IN_BARRACK, None, CREW_OPERATIONS.DROPINBARRACK_WARNING_INBATTLE_TOOLTIP)
            if vehicle.isCrewLocked:
                return self.__getInitCrewOperationObject(OPERATION_DROP_IN_BARRACK, None, CREW_OPERATIONS.DROPINBARRACK_WARNING_CREWISLOCKED_TOOLTIP)
            return self.__getInitCrewOperationObject(OPERATION_DROP_IN_BARRACK)

    def __isTopCrewForCurrentVehicle(self, vehicle):
        return not bool(getLowEfficiencyCrew(vehicle))

    def __isNoCrew(self, crew):
        for _, tman in crew:
            if tman is not None:
                return False

        return True

    def __isNotEnoughSpaceInBarrack(self, crew):
        berthsNeeded = len([(role, t) for role, t in crew if t is not None])
        return 0 < berthsNeeded > self.itemsCache.items.freeTankmenBerthsCount()

    def __getInitCrewOperationObject(self, operationId, errorId=None, warningId=b'', operationAvailable=False):
        context = b'#crew_operations:%s'
        cOpId = context % operationId
        iconPathContext = b'../maps/icons/tankmen/crew/%s%s'
        errorText = b''
        btnLabelText = b''
        if errorId:
            errorText = i18n.makeString(cOpId + b'/error/' + errorId)
        else:
            btnLabelText = i18n.makeString(cOpId + b'/button/label')
        warningInfo = None
        if warningId not in (b'', b'lockCrew'):
            warningInfo = {b'operationAvailable': operationAvailable, b'tooltipId': warningId}
        hasToggleBlock = operationId == OPERATION_RETURN
        toggleBlockErrorText = b''
        toggleBlockToggleText = b''
        if hasToggleBlock:
            if errorId == b'noPrevious' or warningId == b'lockCrew':
                toggleBlockErrorText = i18n.makeString(cOpId + b'/error/' + errorId)
            else:
                toggleBlockToggleText = i18n.makeString(cOpId + b'/toggle/label')
        return {b'id': operationId, b'iconPath': (iconPathContext % (operationId, b'.png')), 
           b'title': (i18n.makeString(cOpId + b'/title')), 
           b'description': (i18n.makeString(cOpId + b'/description')), 
           b'error': errorText, 
           b'warning': warningInfo, 
           b'btnLabel': btnLabelText, 
           b'btnNotificationEnabled': False, 
           b'hasToggleBlock': hasToggleBlock, 
           b'toggleBlockDescription': (i18n.makeString(cOpId + b'/toggle/description')), 
           b'toggleBlockError': toggleBlockErrorText, 
           b'toggleBlockToggleLabel': toggleBlockToggleText, 
           b'isToggleSelected': (g_currentVehicle.item.isAutoReturn)}

    def __unitMgrOnUnitLeft(self, _, __):
        self._destroy()
        return

    @staticmethod
    def __unloadCrew():
        doActions = []
        veh = g_currentVehicle.item
        for slotIdx, tmanInvID in veh.crew:
            if tmanInvID is None:
                continue
            doActions.append((
             factory.UNLOAD_TANKMAN,
             veh.invID,
             slotIdx))

        BigWorld.player().doActions(doActions)
        return
