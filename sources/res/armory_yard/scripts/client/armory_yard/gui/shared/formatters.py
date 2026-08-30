import typing
from copy import deepcopy
from armory_yard.gui.shared.bonus_packers import packBonuses, getArmoryYardBonusPacker
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.money import Currency
from gui.shared.formatters.currency import getBWFormatter
from gui.shared.notifications import NotificationPriorityLevel
from messenger.formatters.service_channel_helpers import MessageData
from messenger import g_settings
from helpers import dependency
from messenger.formatters.service_channel import IQuestAchievesSubformatter, ServiceChannelFormatter, QuestAchievesFormatter
from skeletons.gui.game_control import IArmoryYardController
from armory_yard_constants import ARMORY_YARD_SYS_MSG_PROGRESSION, getProgressionToken
CURRENCIES_FORMATTERS = {(Currency.GOLD): b"<font color='#FFC363'>{}</font>", 
   (Currency.AYCOIN): b"<font color='#E9E2BF'>{}</font>", 
   (Currency.CRYSTAL): b"<font color='#C9C9B6'>{}</font>"}
ITEMS_FORMATTER = b"<font color='#CED9D9'>{}</font>"
_ITEMS_WITHOUT_PIECES = frozenset({b'freeXP', b'credits', b'premium_universal', b'crystal'})
_BULLET = u' \u2022 '

def formatSpentCurrencies(currencies):
    included = [backport.text(R.strings.armory_shop.notifications.description.dyn(currencyName)(), value=CURRENCIES_FORMATTERS[currencyName].format(getBWFormatter(currencyName)(currencyAmount))) for currencyName, currencyAmount in currencies if currencyAmount]
    return (b'\n').join(included)


def formatPurchaseItems(items, packer=None, skipCount=False, isBundle=False, isVehicle=False):
    formattedItems = []
    prefix = _BULLET if not isVehicle and (isBundle or len(items) > 2) else b''
    for bonus in packBonuses(items, packer):
        count = bonus.getValue() or 1
        if skipCount:
            backportText = R.strings.armory_shop.notifications.purchaseContent.withoutCount()
        elif bonus.getName() in _ITEMS_WITHOUT_PIECES:
            backportText = R.strings.armory_shop.notifications.purchaseContent.withoutPieces()
            count = ITEMS_FORMATTER.format(getBWFormatter(bonus.getName())(count))
        else:
            backportText = R.strings.armory_shop.notifications.purchaseContent()
        label = bonus.getLabel()
        formattedItems.append(prefix + backport.text(backportText, product=ITEMS_FORMATTER.format(label) if skipCount else label, count=count))

    if isVehicle:
        header = backport.text(R.strings.armory_shop.notifications.vehicle())
        return _BULLET + header + (b', ').join(formattedItems)
    return (b'\n').join(formattedItems)


def formatBundlePurchase(productId, items):
    items = deepcopy(items)
    _cutCompensation(items)
    vehicles = items.pop(b'vehicles')
    return backport.text(R.strings.armory_shop.notifications.bundleContent(), vehicles=formatPurchaseItems({b'vehicles': vehicles}, skipCount=True, isBundle=True, isVehicle=True), items=formatPurchaseItems(items, getArmoryYardBonusPacker()), isBundle=True)


def _cutCompensation(rewards):
    if b'vehicles' in rewards:
        creditCompensation = 0
        goldCompensation = 0
        for _, vehParams in rewards[b'vehicles'][0].iteritems():
            credit, gold = vehParams.get(b'customCompensation', (0, 0))
            creditCompensation += credit
            goldCompensation += gold

        if creditCompensation:
            rewards[b'credits'] = rewards[b'credits'] - creditCompensation
            if rewards[b'credits'] <= 0:
                del rewards[b'credits']
        if goldCompensation:
            rewards[b'gold'] = rewards[b'gold'] - goldCompensation
            if rewards[b'gold'] <= 0:
                del rewards[b'gold']
    return


class AYProgressionQuestAchievesSubFormatter(IQuestAchievesSubformatter):
    __armoryYardCtrl = dependency.descriptor(IArmoryYardController)

    @classmethod
    def format(cls, data, asBattleFormatter, result, processCustomizations=True, processTokens=True):
        if not asBattleFormatter:
            return
        else:
            tokens = data.get(b'detailedRewards', {}).get(ARMORY_YARD_SYS_MSG_PROGRESSION, {}).get(b'tokens', {})
            seasonID = cls.__armoryYardCtrl.currentSeasonID
            if not tokens or seasonID is None:
                return
            itemsNames = []
            tokenData = tokens.get(getProgressionToken(seasonID))
            if tokenData:
                count = tokenData.get(b'count', 0)
                if count > 0:
                    itemsNames.append(backport.text(R.strings.messenger.serviceChannelMessages.battleResults.quests.items.name(), name=backport.text(R.strings.quests.bonusName.armory_progression_coin()), count=count))
            if itemsNames:
                result.append(cls._makeQuestsAchieve(b'battleQuestsItems', names=(b', ').join(itemsNames)))
            return

    @classmethod
    def _makeQuestsAchieve(cls, key, **kwargs):
        return g_settings.htmlTemplates.format(key, kwargs)


class AYCancelingRerollFormatter(ServiceChannelFormatter):

    def format(self, message, *args):
        if message is None:
            return []
        else:
            currency = message.data.get(b'code', None)
            price = message.data.get(b'amount')
            msgR = R.strings.armory_yard.notifications
            msgType, refundText = {(Currency.CRYSTAL): (
                                  b'ArmoryYardRerollTransactionForCrystalSysMessage', msgR.refund.priceCrystal), 
               (Currency.GOLD): (
                               b'ArmoryYardRerollTransactionForGoldSysMessage', msgR.refund.priceGold)}.get(currency, (b'ArmoryYardRerollTransactionForFreeRerollSysMessage', msgR.refund.freeReroll))
            text = backport.text(msgR.task.cancelReplacement())
            header = backport.text(msgR.title())
            paymentText = backport.text(refundText())
            formatter = g_settings.msgTemplates.format(msgType, {b'header': header, b'text': text, 
               b'paymentText': paymentText, 
               b'price': price})
            return [
             MessageData(formatter, self._getGuiSettings(message, msgType, priorityLevel=NotificationPriorityLevel.MEDIUM))]


class AYDeferredRewardCollectingFormatter(ServiceChannelFormatter):
    _MSG_TEMPLATE = b'ArmoryYardReceivingAwardsSysMessage'

    def format(self, message, *args):
        if message is None:
            return []
        else:
            msgR = R.strings.armory_yard.notifications
            text = backport.text(msgR.ReceivedRewards())
            rewards = QuestAchievesFormatter.formatQuestAchieves(message.data or {}, False)
            formatter = g_settings.msgTemplates.format(self._MSG_TEMPLATE, {b'text': text, b'rewards': rewards})
            return [
             MessageData(formatter, self._getGuiSettings(message, self._MSG_TEMPLATE, priorityLevel=NotificationPriorityLevel.MEDIUM))]
