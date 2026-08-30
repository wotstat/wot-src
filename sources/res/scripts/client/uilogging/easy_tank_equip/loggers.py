import json
from typing import TYPE_CHECKING
from gui.impl.gen.view_models.views.lobby.easy_tank_equip.common.proposal_model import ProposalType
from uilogging.base.logger import MetricsLogger
from uilogging.easy_tank_equip.constants import FEATURE, EasyTankEquipLogActions, EasyTankEquipLogItems, EasyTankEquipSwapInitiators
if TYPE_CHECKING:
    from typing import List
LOGGING_ITEMS_MAP = {(ProposalType.CREW): (EasyTankEquipLogItems.CREW), (ProposalType.OPT_DEVICES): (EasyTankEquipLogItems.OPT_DEVICES), 
   (ProposalType.SHELLS): (EasyTankEquipLogItems.SHELLS), 
   (ProposalType.CONSUMABLES): (EasyTankEquipLogItems.CONSUMABLES), 
   (ProposalType.STYLES): (EasyTankEquipLogItems.STYLES)}

class EasyTankEquipLogger(MetricsLogger):
    STATUS_KEY = b'status'
    PRESET_NUMBER_KEY = b'preset_number'
    IDS_KEY = b'ids'

    def __init__(self):
        super(EasyTankEquipLogger, self).__init__(FEATURE)
        return

    def createCardInfo(self, status, presetNumber, ids):
        return {(self.STATUS_KEY): status, 
           (self.PRESET_NUMBER_KEY): presetNumber, 
           (self.IDS_KEY): ids}

    def onViewOpen(self, info):
        self.log(action=EasyTankEquipLogActions.OPEN, item=EasyTankEquipLogItems.MAIN_VIEW, info=json.dumps(info))
        return

    def onViewClose(self, isApplyBtnClicked, info):
        if isApplyBtnClicked:
            self.log(action=EasyTankEquipLogActions.CLICK, item=EasyTankEquipLogItems.APPLY_BUTTON, parentScreen=EasyTankEquipLogItems.MAIN_VIEW, info=json.dumps(info))
        else:
            self.log(action=EasyTankEquipLogActions.CLOSE, item=EasyTankEquipLogItems.MAIN_VIEW, info=json.dumps(info))
        return

    def onCancel(self):
        self.log(action=EasyTankEquipLogActions.CLICK, item=EasyTankEquipLogItems.CANCEL_BUTTON, parentScreen=EasyTankEquipLogItems.MAIN_VIEW)
        return

    def onSwitchPreset(self, proposalType, fromPresetNumber, toPresetNumber):
        self.log(action=EasyTankEquipLogActions.SWITCH_PRESET, item=LOGGING_ITEMS_MAP[proposalType], parentScreen=EasyTankEquipLogItems.MAIN_VIEW, info=(b'{}:{}').format(fromPresetNumber, toPresetNumber))
        return

    def onSwapSlots(self, proposalType, isDndUsed, firstSlotNumber, secondSlotNumber):
        initiator = EasyTankEquipSwapInitiators.DRAG_AND_DROP if isDndUsed else EasyTankEquipSwapInitiators.SWAP_BUTTON
        self.log(action=EasyTankEquipLogActions.SWAP_SLOTS, item=LOGGING_ITEMS_MAP[proposalType], parentScreen=EasyTankEquipLogItems.MAIN_VIEW, info=(b'{}:{}:{}').format(initiator, firstSlotNumber, secondSlotNumber))
        return
