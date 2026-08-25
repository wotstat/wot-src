from account_helpers import AccountSettings
from account_helpers.AccountSettings import NEW_SETTINGS_COUNTER
from account_helpers.settings_core import settings_constants
from helpers import dependency
from skeletons.gui.game_control import IAnonymizerController, IVehiclePostProgressionController, ILimitedUIController, ICommendationsController
from skeletons.gui.lobby_context import ILobbyContext
_NEW_SETTING_COUNTER_VISIBILITY_VALIDATORS = {(settings_constants.GAME.ANONYMIZER): (lambda : dependency.instance(IAnonymizerController).isEnabled), 
   b'showQuestProgress': (lambda : dependency.instance(ILobbyContext).getServerSettings().isPersonalMissionsEnabled()), 
   (settings_constants.GAME.GAMEPLAY_DEV_MAPS): (lambda : dependency.instance(ILobbyContext).getServerSettings().isMapsInDevelopmentEnabled()), 
   (settings_constants.GAME.SWITCH_SETUPS_IN_LOADING): (lambda : dependency.instance(IVehiclePostProgressionController).isSwitchSetupFeatureEnabled()), 
   (settings_constants.GAME.LIMITED_UI_ACTIVE): (lambda : dependency.instance(ILimitedUIController).isUserSettingsMayShow), 
   (settings_constants.BattleCommStorageKeys.ENABLE_COMMENDATIONS_FEEDBACK): (lambda : dependency.instance(ICommendationsController).isCommendationsEnabled), 
   (settings_constants.SOUND.PHYSICS_QUALITY): (lambda : dependency.instance(ILobbyContext).getServerSettings().isPhysicsSoundEnabled())}

def isNewSettingCounterVisible(settingKey):
    return _NEW_SETTING_COUNTER_VISIBILITY_VALIDATORS.get(settingKey, (lambda : True))()


def getCountNewSettings():
    settings = _getSettingsFromStorage()
    count = _countNewSettingsItems(settings, 0)
    return count


def getNewSettings():
    settings = _getSettingsFromStorage()
    result = []
    grouping = set()
    for tabID, tabsSettings in settings.iteritems():
        tabData = _getTabData(result, tabID)
        for subTabID, controlSettings in tabsSettings.iteritems():
            if isinstance(controlSettings, bool):
                controlID = subTabID
                subTabID = None
                _packCounter(tabData, controlSettings, subTabID, controlID)
            else:
                for controlID, state in controlSettings.iteritems():
                    controlID = _tryGrouping(controlID, grouping)
                    if not controlID:
                        continue
                    _packCounter(tabData, state, subTabID, controlID)

    return result


def invalidateSettings(tabName, subTabName, controlIDs):
    settings = _getSettingsFromStorage()
    isChanged = False
    if tabName in settings.keys():
        tabSettings = settings[tabName]
        if subTabName in tabSettings:
            subContainer = tabSettings[subTabName]
        else:
            subContainer = tabSettings
        for controlID in controlIDs:
            if controlID in settings_constants.GROUPS_NOVELTY_SETTINGS:
                for controlName in settings_constants.GROUPS_NOVELTY_SETTINGS[controlID]:
                    if controlName in subContainer and subContainer[controlName]:
                        subContainer[controlName] = False
                        isChanged = True

            elif controlID in subContainer and subContainer[controlID]:
                subContainer[controlID] = False
                isChanged = True

    if isChanged:
        _setSettingsToStorage(settings)
        return True
    return False


def dropCounters():
    newsettings = getNewSettings()
    for setting in newsettings:
        for subtab in setting[b'subTabsData']:
            for counter in subtab[b'counters']:
                invalidateSettings(setting[b'tabId'], subtab[b'subTabId'], [
                 counter[b'componentId']])

    return


def _countNewSettingsItems(dictItem, count):
    for _, v in dictItem.iteritems():
        if isinstance(v, dict):
            count = _countNewSettingsItems(v, count)
        elif isinstance(v, bool) and v:
            count = count + 1

    return count


def _getTabData(formatedData, searchTabID):
    for tabData in formatedData:
        if tabData[b'tabId'] == searchTabID:
            if b'subTabsData' not in tabData:
                tabData[b'subTabsData'] = []
            return tabData

    tabData = {b'tabId': searchTabID, b'subTabsData': []}
    formatedData.append(tabData)
    return tabData


def _packCounter(tabData, state, subTabID, controlID):
    count = b'1' if state else b'0'
    counters = None
    for subTabData in tabData[b'subTabsData']:
        if subTabData[b'subTabId'] == subTabID:
            if b'counters' not in subTabData:
                subTabData[b'counters'] = []
            counters = subTabData[b'counters']
            break

    if counters is None:
        emptySubTabData = {b'subTabId': subTabID, b'counters': []}
        tabData[b'subTabsData'].append(emptySubTabData)
        counters = emptySubTabData[b'counters']
    counters.append({b'componentId': controlID, b'count': count})
    return


def _getSettingsFromStorage():
    return _filterSettings(AccountSettings.getSettings(NEW_SETTINGS_COUNTER))


def _setSettingsToStorage(value):
    AccountSettings.setSettings(NEW_SETTINGS_COUNTER, _filterSettings(value))
    return


def _filterSettings(value):
    return {category: {settingKey: settingValue for settingKey, settingValue in settings.iteritems() if isNewSettingCounterVisible(settingKey)} for category, settings in value.iteritems()}


def _tryGrouping(controlID, grouping):
    for group, controls in settings_constants.GROUPS_NOVELTY_SETTINGS.iteritems():
        if controlID in controls:
            if group not in grouping:
                grouping.add(group)
                return group
            return

    return controlID
