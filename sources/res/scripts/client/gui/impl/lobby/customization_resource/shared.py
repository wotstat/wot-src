from account_helpers.AccountSettings import CUSTOMIZATION_RESOURCE_LIMIT_UPDATED, CUSTOMIZATION_RESOURCE_LAST_CLICK_WEEK, AccountSettings
from gui.Scaleform.daapi.view.lobby.store.browser.shop_helpers import getCustomizationResourceUrl
from gui.impl.lobby.customization.shared import CustomizationTabs
from gui.shared.event_dispatcher import showShop, showHangar
from gui.shared.gui_items import GUI_ITEM_TYPE_NAMES
from helpers import dependency, time_utils
from skeletons.gui.game_control import ICustomizationResourceController

@dependency.replace_none_kwargs(customizationResourceController=ICustomizationResourceController)
def getCustomizationResourceLimitUpdated(customizationResourceController=None):
    isLimitUpdated = AccountSettings.getSettings(CUSTOMIZATION_RESOURCE_LIMIT_UPDATED)
    startTime = customizationResourceController.getStartTime()
    if startTime and not isLimitUpdated:
        currentTime = int(time_utils.getServerUTCTime())
        weeksElapsed = (currentTime - startTime) // time_utils.ONE_WEEK
        lastClickWeek = AccountSettings.getSettings(CUSTOMIZATION_RESOURCE_LAST_CLICK_WEEK)
        if weeksElapsed > lastClickWeek:
            isLimitUpdated = True
            AccountSettings.setSettings(CUSTOMIZATION_RESOURCE_LIMIT_UPDATED, True)
    return isLimitUpdated


@dependency.replace_none_kwargs(customizationResourceController=ICustomizationResourceController)
def setCustomizationResourceLimitFlags(customizationResourceController=None):
    startTime = customizationResourceController.getStartTime()
    if startTime:
        currentTime = int(time_utils.getServerUTCTime())
        weeksElapsed = (currentTime - startTime) // time_utils.ONE_WEEK
        AccountSettings.setSettings(CUSTOMIZATION_RESOURCE_LAST_CLICK_WEEK, weeksElapsed)
    AccountSettings.setSettings(CUSTOMIZATION_RESOURCE_LIMIT_UPDATED, False)
    return


def getTabItemTypeName(tabId):
    itemTypeName = GUI_ITEM_TYPE_NAMES[CustomizationTabs.SLOT_TYPES[tabId]]
    if tabId == CustomizationTabs.STYLED_3D:
        itemTypeName = (b'{}_{}').format(itemTypeName, CustomizationTabs.STYLE_PREFIX[tabId])
    return itemTypeName


@dependency.replace_none_kwargs(customizationResourceController=ICustomizationResourceController)
def closeWindowHandler(view, customizationResourceController=None):
    if not customizationResourceController.isEnabled():
        showHangar()
        view.destroyWindow()
    elif not customizationResourceController.isExchangeEnabled():
        showShop(getCustomizationResourceUrl())
        view.destroyWindow()
    return


def splitByChunks(data, chunkSize):
    for i in xrange(0, len(data), chunkSize):
        yield data[i:i + chunkSize]

    return


def mergeResults(allResults):
    mainResult = {b'success': True, 
       b'items': [], b'reward': {b'currencies': {}}}
    for result in allResults:
        if not result.success or result.auxData is None:
            mainResult[b'success'] = False
            break
        mainResult[b'items'].extend(result.auxData.items)
        reward = result.auxData.reward or {}
        currencies = reward.get(b'currencies', {})
        for currencyName, currencyData in currencies.iteritems():
            count = currencyData.get(b'count', 0)
            if currencyName not in mainResult[b'reward'][b'currencies']:
                mainResult[b'reward'][b'currencies'][currencyName] = {b'count': 0}
            mainResult[b'reward'][b'currencies'][currencyName][b'count'] += count

    return mainResult
