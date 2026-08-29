import logging
from gui.SystemMessages import SM_TYPE, CURRENCY_TO_SM_TYPE, CURRENCY_TO_SM_TYPE_DISMANTLING
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import formatPrice
from gui.shared.gui_items import GUI_ITEM_TYPE
from gui.shared.gui_items.gui_item_economics import ITEM_PRICE_ZERO, ITEM_PRICE_EMPTY
from gui.shared.gui_items.processors import makeSuccess, makeError
from gui.shared.money import ZERO_MONEY
from gui.shared.notifications import NotificationPriorityLevel
from helpers import dependency
from skeletons.gui.shared import IItemsCache
from skeletons.gui.game_control import IWotPlusController
_logger = logging.getLogger(__name__)

class _ItemProcessorMessage(object):
    _ITEMS_MSG_PREFIXES = {(GUI_ITEM_TYPE.SHELL): b'shell', 
       (GUI_ITEM_TYPE.EQUIPMENT): b'artefact', 
       (GUI_ITEM_TYPE.OPTIONALDEVICE): b'artefact', 
       (GUI_ITEM_TYPE.BATTLE_BOOSTER): b'battleBooster', 
       (GUI_ITEM_TYPE.CREW_BOOKS): b'crewBooks'}
    _ITEMS_MSG_PREFIXES.update({typeID: b'module' for typeID in GUI_ITEM_TYPE.VEHICLE_MODULES})
    __slots__ = (b'_item',)

    def __init__(self, item):
        self._item = item
        return

    def makeErrorMsg(self, reason):
        msgKey = R.strings.system_messages.dyn(self._formMessage()).dyn(reason)
        return makeError(backport.text((msgKey() if msgKey else b''), **self._getMsgCtx()), self._getErrorMsgType())

    def makeSuccessMsg(self):
        msgKey = R.strings.system_messages.dyn(self._formMessage()).success
        return makeSuccess(backport.text((msgKey() if msgKey else b''), **self._getMsgCtx()), self._getSuccessMsgType())

    def _formMessage(self):
        return (b'{itemType}_{opType}').format(itemType=self._ITEMS_MSG_PREFIXES.get(self._item.itemTypeID, b''), opType=self._getOperation())

    def _getErrorMsgType(self):
        return SM_TYPE.Error

    def _getSuccessMsgType(self):
        return SM_TYPE.Information

    def _getMsgCtx(self):
        raise NotImplementedError
        return

    def _getOperation(self):
        raise NotImplementedError
        return


class ItemBuyProcessorMessage(_ItemProcessorMessage):

    def __init__(self, item, itemCount, responsePrice=None):
        self.__count = itemCount
        self.__responsePrice = responsePrice
        super(ItemBuyProcessorMessage, self).__init__(item)
        return

    def _getSuccessMsgType(self):
        return CURRENCY_TO_SM_TYPE.get(self.__getPrice().getCurrency(), SM_TYPE.PurchaseForCredits)

    def _getMsgCtx(self):
        price = self.__getPrice().price if self.__responsePrice is None else self.__responsePrice
        return {b'name': (self._item.userName), 
           b'kind': (self._item.userType), 
           b'count': (backport.getIntegralFormat(int(self.__count))), 
           b'money': (formatPrice(price, ignoreZeros=True))}

    def _getOperation(self):
        return b'buy'

    def __getPrice(self):
        return self._item.getBuyPrice()


class ItemInstallProcessorMessage(_ItemProcessorMessage):

    def _getMsgCtx(self):
        return {b'name': (self._item.userName), 
           b'kind': (self._item.userType)}

    def _getOperation(self):
        return b'apply'


class ItemDestroyProcessorMessage(_ItemProcessorMessage):

    def _getMsgCtx(self):
        return {b'name': (self._item.userName), 
           b'kind': (self._item.userType)}

    def _getOperation(self):
        return b'destroy'


class ItemDeconstructionProcessorMessage(_ItemProcessorMessage):
    __slots__ = (b'_count',)

    def __init__(self, item, count):
        super(ItemDeconstructionProcessorMessage, self).__init__(item)
        self._count = count
        return

    def _getMsgCtx(self):
        return {b'name': (self._item.userName), 
           b'count': (backport.getIntegralFormat(int(self._count))), 
           b'money': (formatPrice(self._getOpPrice().price))}

    def _getOpPrice(self):
        return self._item.sellPrices.itemPrice * self._count

    def _getSuccessMsgType(self):
        return SM_TYPE.Deconstructing

    def _getOperation(self):
        return b'deconstructing'


class MultItemsDeconstructionProcessorMessage(ItemDeconstructionProcessorMessage):
    __slots__ = (b'__items',)

    def __init__(self, items):
        self.__items = items
        firstItem, count = self.__items[0]
        super(MultItemsDeconstructionProcessorMessage, self).__init__(firstItem, count)
        return

    def _getMsgCtx(self):
        return {b'names': (self.getNames()), 
           b'money': (formatPrice(self._getOpPrice().price))}

    def _getOpPrice(self):
        price = ITEM_PRICE_EMPTY
        for item, count in self.__items:
            price = price + item.sellPrices.itemPrice * count

        return price

    def getNames(self):
        templateKey = R.strings.messenger.serviceChannelMessages.sysMsg.deconstructingMult.itemsTemplate()
        names = []
        for item, count in self.__items:
            itemStr = backport.text(templateKey, name=item.userName, count=count)
            names.append(itemStr)

        return (b',').join(names)

    def _getOperation(self):
        return b'deconstructingMult'


class ItemRemoveProcessorMessage(_ItemProcessorMessage):

    def _getMsgCtx(self):
        return {b'name': (self._item.userName), 
           b'kind': (self._item.userType)}

    def _getOperation(self):
        return b'remove'


class OptDeviceRemoveProcessorMessage(ItemRemoveProcessorMessage):
    __itemsCache = dependency.descriptor(IItemsCache)
    __wotPlusController = dependency.descriptor(IWotPlusController)

    def __init__(self, item, removalPrice=ZERO_MONEY, useDemountKit=False):
        self.__removalPrice = removalPrice
        self.__useDemountKit = useDemountKit
        super(OptDeviceRemoveProcessorMessage, self).__init__(item)
        return

    def makeSuccessMsg(self):
        defaultKey = R.strings.system_messages.dyn(self._formMessage()).success
        if self.__useDemountKit:
            msgKey = R.strings.system_messages.dyn(self._formMessage()).demount_kit_success
        elif self.__wotPlusController.isFreeToDemount(self._item):
            msgKey = R.strings.system_messages.dyn(self._formMessage()).wot_plus_success
        else:
            msgKey = R.strings.system_messages.dyn(self._formMessage()).money_success
        return makeSuccess(backport.text((msgKey() if msgKey else defaultKey), **self._getMsgCtx()), self._getSuccessMsgType())

    def _getSuccessMsgType(self):
        if self.__useDemountKit:
            return SM_TYPE.DismantlingForDemountKit
        if self.__wotPlusController.isFreeToDemount(self._item):
            return SM_TYPE.DismantlingForFreeWotPlus
        return CURRENCY_TO_SM_TYPE_DISMANTLING.get(self.__removalPrice.getCurrency(), SM_TYPE.DismantlingForGold)

    def _getMsgCtx(self):
        return {b'name': (self._item.userName), 
           b'kind': (self._item.userType), 
           b'money': (formatPrice(self.__removalPrice, ignoreZeros=True))}


class OptDeviceRestoreProcessorMessage(object):
    __slots__ = (b'__device', b'__restorePrice', b'__count')

    def __init__(self, device=None, restorePrice=None, count=0):
        self.__device = device
        self.__restorePrice = restorePrice
        self.__count = count
        return

    def makeSuccessMsg(self):
        header = backport.text(R.strings.messenger.serviceChannelMessages.sysMsg.titles.restore())
        body = backport.text(R.strings.system_messages.artefact_restore.success(), name=self.__device.userName, count=self.__count, money=self._formatSpentMoney(self.__restorePrice))
        return makeSuccess(userMsg=body, msgType=SM_TYPE.InformationHeader, msgData={b'header': header}, msgPriority=NotificationPriorityLevel.MEDIUM)

    def makeErrorMsg(self):
        body = backport.text(R.strings.system_messages.artefact_restore.server_error())
        return makeError(userMsg=body, msgPriority=NotificationPriorityLevel.MEDIUM)

    def _formatSpentMoney(self, costs):
        parts = []
        for cur, amount in costs:
            if not amount:
                continue
            nameKey = R.strings.system_messages.artefact_restore.dyn(cur)
            text = backport.text(nameKey())
            formattedAmount = backport.getIntegralFormat(amount)
            parts.append((u'{}{}').format(text, formattedAmount))

        return (u', ').join(parts)


class BaseLayoutProcessorMessage(object):
    __slots__ = ()

    def makeErrorMsg(self, reason):
        layoutKey = R.strings.system_messages.dyn(self._formMessage())
        msgKey = layoutKey.dyn(reason) if layoutKey and reason else None
        return makeError(backport.text((msgKey() if msgKey else R.strings.system_messages.dyn(self._formMessage()).error()), **self._getMsgCtx()), self._getErrorMsgType())

    def makeSuccessMsg(self):
        layoutKey = R.strings.system_messages.dyn(self._formMessage())
        msgKey = layoutKey.dyn(b'success') if layoutKey else None
        return makeSuccess(backport.text((msgKey() if msgKey else b''), **self._getMsgCtx()), self._getSuccessMsgType())

    def _formMessage(self):
        return (b'{layoutType}_{opType}').format(layoutType=self._getLayoutPrefix(), opType=self._getOperation())

    def _getErrorMsgType(self):
        return SM_TYPE.Error

    def _getSuccessMsgType(self):
        return SM_TYPE.Information

    def _getLayoutPrefix(self):
        return b''

    def _getMsgCtx(self):
        return {}

    def _getOperation(self):
        return b''


class LayoutApplyProcessorMessage(BaseLayoutProcessorMessage):
    __slots__ = (b'_vehicle', b'__responsePrice')

    def __init__(self, vehicle, responsePrice=None):
        self._vehicle = vehicle
        self.__responsePrice = responsePrice
        return

    def makeSuccessMsg(self):
        layoutKey = R.strings.system_messages.dyn(self._formMessage())
        msgKey = layoutKey.success_money_spent if layoutKey else None
        return makeSuccess(backport.text((msgKey() if msgKey else b''), **self._getMsgCtx()), self._getSuccessMsgType())

    def _getSuccessMsgType(self):
        return CURRENCY_TO_SM_TYPE.get(self.__getPrice().getCurrency(byWeight=False), SM_TYPE.Information)

    def _getLayoutPrefix(self):
        return b'layout'

    def _getMsgCtx(self):
        price = self.__getPrice().price if self.__responsePrice is None else self.__responsePrice
        return {b'vehName': (self._vehicle.userName), 
           b'money': (formatPrice(price, ignoreZeros=True))}

    def _getOperation(self):
        return b'apply'

    def __getPrice(self):
        return sum([item.getBuyPrice() for item in self._vehicle.shells.layout.getItems() if not item.isInInventory and item not in self._vehicle.shells.installed], ITEM_PRICE_ZERO)


class OptDevicesApplyProcessorMessage(BaseLayoutProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return b'optionalDevices'

    def _getOperation(self):
        return b'apply'


class OptDevicesDemountProcessorMessage(BaseLayoutProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return b'optionalDevices'

    def _getOperation(self):
        return b'remove'


class BattleAbilitiesApplyProcessorMessage(BaseLayoutProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return b'battleAbilities'

    def _getOperation(self):
        return b'apply'


class ShellsApplyProcessorMessage(LayoutApplyProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return b'shells'

    def _getOperation(self):
        return b'apply'


class ConsumablesApplyProcessorMessage(LayoutApplyProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return b'consumables'

    def _getOperation(self):
        return b'apply'


class BattleBoostersApplyProcessorMessage(BaseLayoutProcessorMessage):
    __slots__ = ()

    def _getLayoutPrefix(self):
        return b'battleBoosters'

    def _getOperation(self):
        return b'apply'
