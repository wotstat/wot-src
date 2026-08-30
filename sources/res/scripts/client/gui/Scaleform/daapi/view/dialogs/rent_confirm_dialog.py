from __future__ import absolute_import
import logging
from gui.Scaleform.daapi.view.dialogs import I18nConfirmDialogMeta, DIALOG_BUTTON_ID
from gui.Scaleform.framework import ScopeTemplates
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import formatPrice, text_styles
from gui.shared.money import MONEY_UNDEFINED
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController
from skeletons.gui.shared import IItemsCache
_logger = logging.getLogger(__name__)

class RentConfirmDialogMeta(I18nConfirmDialogMeta):
    epicController = dependency.descriptor(IEpicBattleMetaGameController)
    itemsCache = dependency.descriptor(IItemsCache)

    def __init__(self, intCD, rentType, nums=(0,), price=MONEY_UNDEFINED, seasonType=0, renew=False):
        key = b'rentConfirmationRenew' if renew else b'rentConfirmation'
        super(RentConfirmDialogMeta, self).__init__(key, scope=ScopeTemplates.LOBBY_SUB_SCOPE, focusedID=DIALOG_BUTTON_ID.SUBMIT)
        vehicle = self.itemsCache.items.getItemByCD(intCD)
        event = backport.text(R.strings.dialogs.rentConfirmation.event(), eventName=backport.text(R.strings.arenas.type.epic.name.inQuotes()))
        self._messageCtx = {b'name': (vehicle.shortUserName or b'Vehicle'), 
           b'event': (text_styles.stats(event)), 
           b'price': (formatPrice(price, reverse=True, useIcon=True))}
        return
