import logging
from gui_lootboxes.gui.lb_gui_constants import SCH_CLIENT_MSG_TYPE, GLOW
from constants import LOOTBOX_KEY_PREFIX
from gui.server_events.bonuses import getMergedBonusesFromDicts
from gui.shared.money import ZERO_MONEY, Currency, Money
from helpers import dependency
from skeletons.gui.system_messages import ISystemMessages
TOKEN_COMPENSATION_TEMPLATE = b'lb_comp:{}:{}:{}:{}'
TOKEN_COMPENSATION_PREFIX = b'lb_comp:'
_logger = logging.getLogger(__name__)

def preformatCompensationValue(rewards):
    vehiclesList = rewards.get(b'vehicles', [])
    compValue = _getCompensationVehicleValue(vehiclesList)
    for tokenID in rewards.get(b'tokens', {}).keys():
        if tokenID.startswith(TOKEN_COMPENSATION_PREFIX):
            compValue += _getCompensationValueFromToken(tokenID)

    for currency in Currency.ALL:
        if compValue.get(currency, 0) > 0:
            currencyValue = rewards.pop(currency, 0)
            if currency is not None:
                newCurrencyValue = currencyValue - compValue.get(currency, 0)
                if newCurrencyValue:
                    rewards[currency] = max(newCurrencyValue, 0)

    return


def _getCompensationVehicleValue(vehiclesList):
    comp = ZERO_MONEY
    for vehiclesDict in vehiclesList:
        for _, vehicleData in vehiclesDict.iteritems():
            if b'rentCompensation' in vehicleData:
                comp += Money.makeFromMoneyTuple(vehicleData[b'rentCompensation'])
            if b'customCompensation' in vehicleData:
                comp += Money.makeFromMoneyTuple(vehicleData[b'customCompensation'])

    return comp


def _getCompensationValueFromToken(tokenID):
    currency, value, _, _ = parseCompenstaionToken(tokenID)
    return Money.makeFrom(currency, value)


def preformatStyle(rewards):
    customizations = rewards.get(b'customizations', [])
    if customizations:
        rewards[b'customizations'] = [cData for cData in customizations if not cData.get(b'boundToCurrentVehicle', False)]
        if not rewards[b'customizations']:
            rewards.pop(b'customizations')
    return


def preformatKey(rewards, dataUsedKeys, dataFaildKey):
    for token in rewards.get(b'tokens', {}).iterkeys():
        if token.startswith(LOOTBOX_KEY_PREFIX):
            _, keyID = token.split(b':')
            if int(keyID) in dataUsedKeys.keys() or int(keyID) in dataFaildKey.keys():
                rewards[b'tokens'][token][b'count'] += 1

    return


def preformatVehicleItems(rewards):
    items = rewards.get(b'items')
    if not items:
        return
    else:
        vehiclesList = rewards.get(b'vehicles', [])
        for vehiclesDict in vehiclesList:
            for _, vehicleData in vehiclesDict.iteritems():
                for unlockModule in vehicleData.get(b'unlockModules', []):
                    rewards.get(b'items', {}).pop(unlockModule, None)

        return


def preformatMeta(rewards, result):
    meta = rewards.get(b'meta', {})
    if not meta:
        return
    else:
        result.auxData[b'clientData'][b'uniqueOpening'] |= meta.pop(GLOW, None) is not None
        if not meta:
            del rewards[b'meta']
        return


def prepareOpenResult(result):
    if result and result.success and result.auxData:
        bonus = result.auxData.get(b'bonus', [])
        dataUsedKeys = result.auxData.get(b'clientData', {}).get(b'usedKeys', {})
        dataFaildKey = result.auxData.get(b'extData', {}).get(b'failedKeys', {})
        for rewards in bonus:
            preformatCompensationValue(rewards)
            preformatStyle(rewards)
            preformatKey(rewards, dataUsedKeys, dataFaildKey)
            preformatVehicleItems(rewards)
            preformatMeta(rewards, result)

        rewards = getMergedBonusesFromDicts(bonus)
        openedLootBoxesData = result.auxData.get(b'extData', {}).get(b'openedLootBoxes', {})
        message = {b'rewards': rewards, b'failedKeys': dataFaildKey, 
           b'usedKeys': dataUsedKeys, 
           b'openedLootBoxes': openedLootBoxesData}
        systemMessages = dependency.instance(ISystemMessages)
        systemMessages.proto.serviceChannel.pushClientMessage(message, SCH_CLIENT_MSG_TYPE.LB_OPENED)
    return


def parseCompenstaionToken(tokenID):
    try:
        _, currency, value, item, itemID = tokenID.split(b':')
        return (currency, int(value), item, itemID)
    except ValueError as e:
        _logger.error(e)
        return (None, None, None, None)

    return


def calculateCountBonusItems(bonuses):
    count = 0
    for bonus in bonuses:
        count += bonus.getCount()

    return count
