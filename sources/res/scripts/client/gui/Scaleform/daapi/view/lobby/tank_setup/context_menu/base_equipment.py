from __future__ import absolute_import
from CurrentVehicle import g_currentVehicle
from adisp import adisp_async, adisp_process
from gui.Scaleform.daapi.view.lobby.shared.cm_handlers import CMLabel, option
from gui.Scaleform.daapi.view.lobby.tank_setup.context_menu.base import BaseItemContextMenu, BaseSlotContextMenu, TankSetupCMLabel, FIRST_SLOT, SECOND_SLOT, THIRD_SLOT
from gui.impl.gen.view_models.views.lobby.tank_setup.sub_views.base_setup_model import BaseSetupModel
from gui.impl.lobby.tank_setup.tank_setup_helper import NONE_ID
from gui.shared.event_dispatcher import showModuleInfo
from helpers import dependency
from ids_generators import SequenceIDGenerator
from skeletons.gui.lobby_context import ILobbyContext

class BaseEquipmentItemContextMenu(BaseItemContextMenu):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    _sqGen = SequenceIDGenerator()

    @option(_sqGen.nextSequenceID, CMLabel.INFORMATION)
    def showInfo(self):
        self._sendSlotAction(BaseSetupModel.SHOW_INFO_SLOT_ACTION)
        return

    @option(_sqGen.nextSequenceID, CMLabel.UPGRADE)
    def upgrade(self):
        self._upgradeEquipment()
        return

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.SELECT)
    def select(self):
        self._sendSlotAction(BaseSetupModel.SELECT_SLOT_ACTION)
        return

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.PUT_ON_FIRST)
    def putOnFirst(self):
        self._sendPutOnSlotAction(onId=FIRST_SLOT)
        return

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.PUT_ON_SECOND)
    def putOnSecond(self):
        self._sendPutOnSlotAction(onId=SECOND_SLOT)
        return

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.PUT_ON_THIRD)
    def putOnThird(self):
        self._sendPutOnSlotAction(onId=THIRD_SLOT)
        return

    def _getOptionCustomData(self, label):
        optionData = super(BaseEquipmentItemContextMenu, self)._getOptionCustomData(label)
        for slotID, slotLabel in enumerate(TankSetupCMLabel.PUT_ON_LIST):
            if slotLabel == label:
                item = self._itemsCache.items.getItemByCD(self._intCD)
                optionData.enabled = optionData.enabled and item.mayInstall(self._getCopyVehicle(), slotID)[0]
                break

        return optionData

    def _isVisible(self, label):
        if label == CMLabel.UPGRADE:
            return self._getItem().isUpgradable and (self._getItem().isInInventory or self._getItem().isInSetup(self._getVehicle())) and self.__lobbyContext.getServerSettings().isTrophyDevicesEnabled()
        return super(BaseEquipmentItemContextMenu, self)._isVisible(label)

    def _upgradeEquipment(self):
        return


class BaseEquipmentSlotContextMenu(BaseSlotContextMenu):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    _sqGen = SequenceIDGenerator()

    @option(_sqGen.nextSequenceID, CMLabel.INFORMATION)
    def showInfo(self):
        self._sendSlotAction(BaseSetupModel.SHOW_INFO_SLOT_ACTION)
        return

    @option(_sqGen.nextSequenceID, CMLabel.UPGRADE)
    def upgrade(self):
        self._upgradeEquipment()
        return

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.PUT_ON_FIRST)
    def putOnFirst(self):
        self._sendPutOnSlotAction(onId=FIRST_SLOT)
        return

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.PUT_ON_SECOND)
    def putOnSecond(self):
        self._sendPutOnSlotAction(onId=SECOND_SLOT)
        return

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.PUT_ON_THIRD)
    def putOnThird(self):
        self._sendPutOnSlotAction(onId=THIRD_SLOT)
        return

    def _isVisible(self, label):
        if label == CMLabel.UPGRADE:
            return self._getItem().isUpgradable and self.__lobbyContext.getServerSettings().isTrophyDevicesEnabled()
        return super(BaseEquipmentSlotContextMenu, self)._isVisible(label)

    def _upgradeEquipment(self):
        return


class BaseHangarEquipmentSlotContextMenu(BaseSlotContextMenu):
    __lobbyContext = dependency.descriptor(ILobbyContext)
    _sqGen = SequenceIDGenerator()

    @option(_sqGen.nextSequenceID, CMLabel.INFORMATION)
    def showInfo(self):
        self._showInfo()
        return

    @option(_sqGen.nextSequenceID, CMLabel.UPGRADE)
    def upgrade(self):
        self._upgradeEquipment()
        return

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.PUT_ON_FIRST)
    def putOnFirst(self):
        self._putOnAction(onId=FIRST_SLOT)
        return

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.PUT_ON_SECOND)
    def putOnSecond(self):
        self._putOnAction(onId=SECOND_SLOT)
        return

    @option(_sqGen.nextSequenceID, TankSetupCMLabel.PUT_ON_THIRD)
    def putOnThird(self):
        self._putOnAction(onId=THIRD_SLOT)
        return

    def _getVehicle(self):
        return g_currentVehicle.item

    def _showInfo(self):
        showModuleInfo(self._intCD, self._getVehicle().descriptor)
        return

    def _putOnAction(self, onId):
        return

    def _postProcessLayoutAfterSwap(self, layout):
        return

    @adisp_process
    def _makePutOnAction(self, setupName, onId, copyVehicle, layout):
        leftID, rightID = sorted((onId, self._installedSlotId))
        leftItem, rightItem = layout[leftID], layout[rightID]
        layout[leftID], layout[rightID] = layout[rightID], layout[leftID]
        self._postProcessLayoutAfterSwap(layout)
        result = yield self._doPutOnAction(copyVehicle)
        if result:
            self._sendLastSlotAction(setupName, BaseSetupModel.SWAP_SLOTS_ACTION, {b'leftID': leftID, 
               b'rightID': rightID, b'leftIntCD': (leftItem.intCD if leftItem else NONE_ID), 
               b'rightIntCD': (rightItem.intCD if rightItem else NONE_ID)})
        return

    @adisp_async
    def _doPutOnAction(self, vehicle, callback):
        callback(False)
        return

    def _isVisible(self, label):
        if label == CMLabel.UPGRADE:
            return self._getItem().isUpgradable and self.__lobbyContext.getServerSettings().isTrophyDevicesEnabled()
        return super(BaseHangarEquipmentSlotContextMenu, self)._isVisible(label)

    def _upgradeEquipment(self):
        return
