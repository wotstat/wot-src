from collections import namedtuple
from gui import SystemMessages
from gui.SystemMessages import pushMessagesFromResult
from gui.shared.gui_items.processors.common import GoldToCreditsExchanger, PremiumAccountBuyer
from gui.shared.gui_items.processors.goodies import BoosterBuyer
from gui.shared.gui_items.processors.module import ModuleBuyer
from gui.shared.gui_items.processors.vehicle import VehicleBuyer, showVehicleReceivedResultMessages
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.goodies import IGoodiesCache
from skeletons.gui.shared import IItemsCache
from soft_exception import SoftException
from web.web_client_api import Field, W2CSchema, w2c
from web.web_client_api.common import ShopItemType
_ItemBuySpec = namedtuple(b'ItemBuySpec', (b'type', b'id', b'count'))
_EXCHANGER = {(Currency.GOLD): (lambda value: GoldToCreditsExchanger(value, withConfirm=False))}

def parseItemsSpec(specList):
    specList = specList or tuple()
    fields = {b'type', b'id', b'count'}
    if not all(set(spec).issubset(fields) for spec in specList):
        raise SoftException(b'invalid item buy spec')
    for spec in specList:
        if not ShopItemType.hasValue(spec[b'type']):
            raise SoftException((b'unsupported item type "{}"').format(spec[b'type']))

    return [_ItemBuySpec(spec[b'type'], spec[b'id'], spec[b'count']) for spec in specList]


def itemsSpecValidator(specList):
    try:
        parseItemsSpec(specList)
    except SoftException:
        raise

    return True


def _currencyExchangeValidator(_, data):
    return all(v > 0 and c in _EXCHANGER.iterkeys() for c, v in data.get(b'currencies', {}).iteritems())


class _BuyItemsSchema(W2CSchema):
    items = Field(required=True, type=list, validator=(lambda value, _: itemsSpecValidator(value)))


class _CurrencyExchangeSchema(W2CSchema):
    currencies = Field(required=True, type=dict, validator=_currencyExchangeValidator)


class TradeWebApiMixin(object):
    _goodiesCache = dependency.descriptor(IGoodiesCache)
    _itemsCache = dependency.descriptor(IItemsCache)

    @w2c(_CurrencyExchangeSchema, b'exchange')
    def exchange(self, cmd):
        exchangeResults = {}
        for currencyType, currencyValue in cmd.currencies.iteritems():
            result = yield _EXCHANGER[currencyType](currencyValue).request()
            exchangeResults[currencyType] = {b'success': (result.success), 
               b'message': (result.userMsg)}
            pushMessagesFromResult(result)

        yield exchangeResults
        return

    @w2c(_BuyItemsSchema, b'buy_items')
    def buyItems(self, cmd):
        responses = []
        items = self._itemsCache.items
        for spec in parseItemsSpec(cmd.items):
            if spec.type in (ShopItemType.DEVICE, ShopItemType.EQUIPMENT, ShopItemType.BATTLE_BOOSTER):
                item = items.getItemByCD(spec.id)
                currency = item.buyPrices.itemPrice.price.getCurrency()
                buyer = ModuleBuyer(item, spec.count, currency)
            elif spec.type == ShopItemType.BOOSTER:
                item = self._goodiesCache.getBooster(spec.id)
                currency = item.buyPrices.itemPrice.price.getCurrency()
                buyer = BoosterBuyer(item, spec.count, currency)
            elif spec.type == ShopItemType.VEHICLE:
                item = items.getItemByCD(spec.id)
                buyer = VehicleBuyer(item, buySlot=False, showNotEnoughSlotMsg=False)
            elif spec.type == ShopItemType.PREMIUM:
                daysCount = spec.count
                buyer = PremiumAccountBuyer(daysCount, price=items.shop.getPremiumCostWithDiscount()[daysCount], requireConfirm=False)
            else:
                raise SoftException((b'Invalid item type: "{}".').format(spec.type))
            if buyer:
                response = yield buyer.request()
                responses.append(self.__makeResult(spec.type, spec.id, response))
            else:
                responses.append(None)

        results = []
        for response in responses:
            status = response[b'success']
            if status and status.userMsg:
                if response[b'type'] == ShopItemType.VEHICLE:
                    showVehicleReceivedResultMessages(status)
                else:
                    SystemMessages.pushI18nMessage(status.userMsg, type=status.sysMsgType)
                statusData = status.auxData
                if statusData is None or b'errStr' not in statusData or not statusData[b'errStr']:
                    result = b'success'
                else:
                    result = statusData[b'errStr']
                results.append(self.__makeResult(response[b'type'], response[b'id'], status.success, result))
            else:
                results.append(self.__makeResult(response[b'type'], response[b'id'], False))

        yield results
        return

    @staticmethod
    def __makeResult(itemType, itemId, success, result=b'error'):
        return {b'type': itemType, b'id': itemId, b'success': success, b'result': result}
