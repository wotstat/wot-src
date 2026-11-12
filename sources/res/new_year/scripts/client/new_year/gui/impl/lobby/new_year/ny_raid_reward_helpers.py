import logging
from constants import LOOTBOX_KEY_PREFIX
from gui.shared.money import ZERO_MONEY, Currency, Money
from new_year_common.items.components.ny_constants import TOKEN_MANDARIN
_TOKEN_COMPENSATION_PREFIX = b'lb_comp:'
_CURRENCY_TOKENS = (TOKEN_MANDARIN,)
_logger = logging.getLogger(__name__)

def prepareRaidRewardResult(result):
    if result and result.success and result.auxData:
        bonus = result.auxData.get(b'bonus', [])
        dataUsedKeys = result.auxData.get(b'clientData', {}).get(b'usedKeys', {})
        dataFailedKeys = result.auxData.get(b'extData', {}).get(b'failedKeys', {})
        for rewards in bonus:
            preformatCompensationValue(rewards)
            preformatStyle(rewards)
            preformatKey(rewards, dataUsedKeys, dataFailedKeys)
            preformatVehicleItems(rewards)
            preformatMeta(rewards, result)

    return


def preformatCompensationValue(rewards):
    compValue = ZERO_MONEY
    for vehiclesDict in _getVehiclesList(rewards):
        for vehicleData in vehiclesDict.itervalues():
            for compensation in (b'rentCompensation', b'customCompensation'):
                if compensation in vehicleData:
                    compValue += Money.makeFromMoneyTuple(vehicleData[compensation])

    tokens = rewards.get(b'tokens', {})
    popTokens = set()
    for tokenName, info in tokens.iteritems():
        if tokenName.startswith(_TOKEN_COMPENSATION_PREFIX):
            currency, amount = _parseCompensationToken(tokenName)
            compValue += Money.makeFrom(currency, amount)
            if currency in _CURRENCY_TOKENS:
                tokens[currency][b'count'] -= amount * info[b'count']
                if tokens[currency][b'count'] == 0:
                    popTokens.add(currency)

    for tokenName in popTokens:
        tokens.pop(tokenName)

    for currency in Currency.ALL:
        if compValue.get(currency, 0) > 0:
            currencyValue = rewards.pop(currency, 0)
            newCurrencyValue = currencyValue - compValue.get(currency, 0)
            if newCurrencyValue:
                rewards[currency] = max(newCurrencyValue, 0)

    return


def preformatStyle(rewards):
    customizations = rewards.get(b'customizations', [])
    if customizations:
        rewards[b'customizations'] = [cData for cData in customizations if not cData.get(b'boundToCurrentVehicle', False)]
        if not rewards[b'customizations']:
            rewards.pop(b'customizations')
    return


def preformatKey(rewards, dataUsedKeys, dataFailedKeys):
    for token in rewards.get(b'tokens', {}).iterkeys():
        if token.startswith(LOOTBOX_KEY_PREFIX):
            _, keyID = token.split(b':')
            if int(keyID) in dataUsedKeys or int(keyID) in dataFailedKeys:
                rewards[b'tokens'][token][b'count'] += 1

    return


def preformatVehicleItems(rewards):
    items = rewards.get(b'items')
    if not items:
        return
    else:
        for vehiclesDict in _getVehiclesList(rewards):
            for vehicleData in vehiclesDict.itervalues():
                for unlockModule in vehicleData.get(b'unlockModules', []):
                    items.pop(unlockModule, None)

        return


def preformatMeta(rewards, result):
    meta = rewards.get(b'meta', {})
    if not meta:
        return
    else:
        clientData = result.auxData.setdefault(b'clientData', {})
        clientData[b'uniqueOpening'] = clientData.get(b'uniqueOpening', False) | (meta.pop(b'glow', None) is not None)
        if not meta:
            del rewards[b'meta']
        return


def _getVehiclesList(rewards):
    vehiclesList = rewards.get(b'vehicles', [])
    if isinstance(vehiclesList, dict):
        return [vehiclesList]
    return vehiclesList


def _parseCompensationToken(tokenID):
    try:
        _, currency, value, _, _ = tokenID.split(b':')
        return (currency, int(value))
    except ValueError as error:
        _logger.error(error)
        return (None, None)

    return
