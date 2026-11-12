from account_helpers import AccountSettings
from account_helpers.AccountSettings import CUSTOMIZATION_RESOURCE_EXCHANGE_PENDING
from gui import SystemMessages
from gui.impl import backport
from gui.impl.gen import R
from gui.impl.lobby.customization.shared import CustomizationTabs
from gui.shared.notifications import NotificationPriorityLevel
_CATEGORY_RESOURCES = (
 (
  CustomizationTabs.PAINTS, b'paints'),
 (
  CustomizationTabs.INSCRIPTIONS, b'inscriptions'),
 (
  CustomizationTabs.EMBLEMS, b'emblems'),
 (
  CustomizationTabs.CAMOUFLAGES, b'camouflages'),
 (
  CustomizationTabs.PROJECTION_DECALS, b'projectionDecals'),
 (
  CustomizationTabs.MODIFICATIONS, b'modifications'),
 (
  CustomizationTabs.STYLED_2D, b'styles2D'),
 (
  CustomizationTabs.STYLED_3D, b'styles3D'))

def markExchangePending():
    AccountSettings.setSettings(CUSTOMIZATION_RESOURCE_EXCHANGE_PENDING, True)
    return


def clearExchangePending():
    AccountSettings.setSettings(CUSTOMIZATION_RESOURCE_EXCHANGE_PENDING, False)
    return


def isExchangePending():
    return AccountSettings.getSettings(CUSTOMIZATION_RESOURCE_EXCHANGE_PENDING)


def formatExchangedItems(categoryCounts):
    texts = R.strings.system_messages.customizationResource
    result = []
    for tabId, resourceKey in _CATEGORY_RESOURCES:
        count = int(categoryCounts.get(tabId, 0))
        if count <= 0:
            continue
        result.append(backport.text(texts.exchange.categoryItem(), name=backport.text(texts.categories.dyn(resourceKey)()), count=count))

    return (b', ').join(result)


def getCategoryCounts(items, categoryMap):
    result = {}
    for itemCD, _, count in items:
        category = categoryMap.get(itemCD)
        if category is not None:
            result[category] = result.get(category, 0) + count

    return result


def pushExchangeSuccess(categoryCounts, reward):
    texts = R.strings.system_messages.customizationResource.exchange.success
    SystemMessages.pushMessage(text=backport.text(texts.body(), items=formatExchangedItems(categoryCounts), reward=reward), type=SystemMessages.SM_TYPE.CustomizationResource, priority=NotificationPriorityLevel.LOW, messageData={b'header': (backport.text(texts.title()))})
    return


def pushExchangeError():
    texts = R.strings.system_messages.customizationResource.exchange.error
    SystemMessages.pushMessage(text=backport.text(texts.body()), type=SystemMessages.SM_TYPE.ErrorHeader, priority=NotificationPriorityLevel.HIGH, messageData={b'header': (backport.text(texts.title()))})
    return
