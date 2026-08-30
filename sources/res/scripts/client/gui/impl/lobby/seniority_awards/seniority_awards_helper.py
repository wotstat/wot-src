import logging, BigWorld
from frameworks.wulf import ViewFlags
from gui import SystemMessages
from gui.impl import backport
from gui.impl.auxiliary.rewards_helper import getRewardRendererModelPresenter, DEF_COMPENSATION_PRESENTERS
from gui.impl.auxiliary.tooltips.compensation_tooltip import CompensationTooltipContent, VehicleCompensationTooltipContent
from gui.impl.gen import R
from gui.impl.gen.view_models.views.loot_box_compensation_tooltip_model import LootBoxCompensationTooltipModel
from gui.shared import g_eventBus
from gui.shared.events import GameEvent
from gui.shared.notifications import NotificationPriorityLevel
MAX_BOXES_TO_OPEN = 5
ADDITIONAL_AWARDS_COUNT = 6
_logger = logging.getLogger(__name__)

def showRestrictedSysMessage():

    def _showRestrictedSysMessage():
        SystemMessages.pushMessage(text=backport.text(R.strings.lootboxes.restrictedMessage.body()), type=SystemMessages.SM_TYPE.ErrorHeader, priority=NotificationPriorityLevel.HIGH, messageData={b'header': (backport.text(R.strings.lootboxes.restrictedMessage.header()))})
        return

    BigWorld.callback(0.0, _showRestrictedSysMessage)
    return


def getLootboxRendererModelPresenter(reward):
    return getRewardRendererModelPresenter(reward, None, DEF_COMPENSATION_PRESENTERS)


def getRewardTooltipContent(event):
    tContent = R.views.common.tooltip_window.loot_box_compensation_tooltip.LootBoxCompensationTooltipContent()
    if event.contentID == tContent:
        tooltipData = {b'iconBefore': (event.getArgument(b'iconBefore', b'')), b'labelBefore': (event.getArgument(b'labelBefore', b'')), 
           b'iconAfter': (event.getArgument(b'iconAfter', b'')), 
           b'labelAfter': (event.getArgument(b'labelAfter', b'')), 
           b'bonusName': (event.getArgument(b'bonusName', b''))}
        return CompensationTooltipContent(content=tContent, viewFlag=ViewFlags.VIEW, model=LootBoxCompensationTooltipModel, **tooltipData)
    else:
        tContent = R.views.common.tooltip_window.loot_box_compensation_tooltip.LootBoxVehicleCompensationTooltipContent()
        if event.contentID == tContent:
            tooltipData = {b'iconBefore': (event.getArgument(b'iconBefore', b'')), b'labelBefore': (event.getArgument(b'labelBefore', b'')), 
               b'iconAfter': (event.getArgument(b'iconAfter', b'')), 
               b'labelAfter': (event.getArgument(b'labelAfter', b'')), 
               b'bonusName': (event.getArgument(b'bonusName', b'')), 
               b'vehicleName': (event.getArgument(b'vehicleName', b'')), 
               b'vehicleType': (event.getArgument(b'vehicleType', b'')), 
               b'isElite': (event.getArgument(b'isElite', True)), 
               b'vehicleLvl': (event.getArgument(b'vehicleLvl', b''))}
            return VehicleCompensationTooltipContent(**tooltipData)
        return


def _closeLootBoxWindows():
    g_eventBus.handleEvent(GameEvent(GameEvent.CLOSE_LOOT_BOX_WINDOWS))
    return
