import re
from adisp import adisp_async, adisp_process
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.notifications import NotificationPriorityLevel
from gui.shared.system_factory import registerTokenQuestsSubFormatters
from helpers import dependency
from messenger import g_settings
from messenger.formatters.collections_by_type import registerHangarQuestSubFormatters
from messenger.formatters.service_channel import BattlePassQuestAchievesFormatter
from new_year.messenger.formatters.service_channel import NewYearCollectionFormatter
from messenger.formatters.service_channel_helpers import MessageData, getCustomizationItemData, getRewardsForQuests, EOL
from messenger.formatters.token_quest_subformatters import AsyncTokenQuestsSubFormatter
from messenger.m_constants import SCH_CLIENT_MSG_TYPE
from new_year.ny_constants import NY_LEVEL_PREFIX, NY_OLD_COLLECTION_PREFIX, NY_COLLECTION_MEGA_PREFIX, NY_COLLECTION_PREFIXES
from new_year.notification.decorators import NyMessageButtonDecorator
from new_year_common.items.components.ny_constants import MAX_ATMOSPHERE_LVL
from shared_utils import findFirst
from skeletons.gui.server_events import IEventsCache
MAX_LEVEL = b'max'
DEFAULT_LEVEL = b'default'

class NewYearLevelUpRewardFormatter(AsyncTokenQuestsSubFormatter):
    _eventsCache = dependency.descriptor(IEventsCache)

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        if isSynced:
            messages = []
            data = message.data or {}
            questIDs = filter(self._isQuestOfThisGroup, data.get(b'completedQuestIDs', set()))
            levelSettings = self._getGuiSettings(message, b'InformationHeaderSysMessage', priorityLevel=NotificationPriorityLevel.MEDIUM)
            rewardsSettings = self._getGuiSettings(message, self._getTemplateName(), priorityLevel=NotificationPriorityLevel.LOW)
            questsMap = {int(questID.split(b':')[-1]): questID for questID in questIDs}
            for level in sorted(questsMap.keys()):
                header = backport.text(R.strings.ny.notification.levelUp.congrats.dyn(self._getMaxLevel(level)).header())
                text = backport.text(R.strings.ny.notification.levelUp.congrats.dyn(self._getMaxLevel(level)).body(), level=level)
                formatted = g_settings.msgTemplates.format(b'InformationHeaderSysMessage', ctx={b'header': header, b'text': text})
                messages.append(MessageData(formatted, levelSettings))
                fmt = BattlePassQuestAchievesFormatter.formatQuestAchieves(data.get(b'detailedRewards', {}).get(questsMap[level], {}), asBattleFormatter=False, processTokens=True, isBulletsNeed=False)
                if fmt is not None:
                    formatted = g_settings.msgTemplates.format(self._getTemplateName(), ctx={b'text': fmt})
                    messages.append(MessageData(formatted, rewardsSettings))

            callback(messages)
        else:
            callback([MessageData(None, None)])
        return

    def _getTemplateName(self):
        return b'nyLevelUpRewardsReceived'

    @classmethod
    def _deleteColorAndFontAccentuation(cls, text):
        regex = re.compile(b"(color='#.*?'|<b>|</b>)")
        cleanText = re.sub(regex, b'', text)
        return cleanText

    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        return questID.startswith(NY_LEVEL_PREFIX)

    @classmethod
    def _getMaxLevel(cls, level):
        if level != MAX_ATMOSPHERE_LVL:
            return DEFAULT_LEVEL
        return MAX_LEVEL


class NewYearCollectionRewardFormatter(AsyncTokenQuestsSubFormatter):
    _eventsCache = dependency.descriptor(IEventsCache)
    _TEMPLATE_NAME = b'newYearCollectionComplete'
    _STR_PATH = R.strings.ny.notification

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        messages = []
        if isSynced:
            data = message.data or {}
            detailedRewards = data.get(b'detailedRewards', {})
            questIDs = filter(self._isQuestOfThisGroup, data.get(b'completedQuestIDs', set()))
            for questID in questIDs:
                rewards = detailedRewards.get(questID, {})
                yearId, _, collectionKey, _ = questID.split(b':')
                year = backport.text(R.strings.ny.systemMessage.dyn(yearId)())
                collectionName = self.__getCollectionName(yearId, collectionKey)
                rows = [
                 backport.text(R.strings.ny.notification.collectionComplete(), setting=collectionName, year=year)]
                self._addFormattedRewards(rewards, rows)
                settings = self._getGuiSettings(message, self._TEMPLATE_NAME, messageSubtype=SCH_CLIENT_MSG_TYPE.NY_EVENT_BUTTON_MESSAGE, decorator=NyMessageButtonDecorator)
                savedData = {b'savedData': {b'completedQuestID': questID, 
                                  b'rewards': rewards}}
                formatted = g_settings.msgTemplates.format(self._TEMPLATE_NAME, ctx={b'text': (EOL.join(rows))}, data=savedData)
                messages.append(MessageData(formatted, settings))

            callback(messages)
        else:
            callback([MessageData(None, None)])
        return

    def _addFormattedRewards(self, data, rows):
        rewards = {}
        for customizationItem in data.get(b'customizations', []):
            custType = customizationItem[b'custType']
            guiItemType, item = getCustomizationItemData(customizationItem[b'id'], custType)
            itemCount = customizationItem[b'value']
            if itemCount > 1:
                count = backport.text(self._STR_PATH.collectionComplete.bonusCount(), count=itemCount)
                item = (b' ').join((item, count))
            rewards.setdefault(guiItemType, []).append(item)

        for guiItemType, items in rewards.iteritems():
            custName = backport.text(self._STR_PATH.collectionComplete.dyn(guiItemType)())
            rows.append((b' ').join((custName, (b', ').join(items))))

        return

    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        return not questID.startswith(NY_COLLECTION_MEGA_PREFIX) and questID.startswith(NY_COLLECTION_PREFIXES)

    @staticmethod
    def __getCollectionName(yearID, collectionID):
        collectionsRoot = R.strings.ny.notification.collectionComplete.name
        compoundKey = (b'_').join((collectionID, yearID))
        rID = collectionsRoot.dyn(compoundKey) or collectionsRoot.dyn(collectionID)
        return backport.text(rID())


class NewYearCollectionMegaRewardFormatter(NewYearCollectionRewardFormatter):
    _eventsCache = dependency.descriptor(IEventsCache)
    _TEMPLATE_NAME = b'newYearCollectionMegaComplete'

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        formatted, settings = (None, None)
        if isSynced:
            data = message.data or {}
            questID = findFirst(self._isQuestOfThisGroup, data.get(b'completedQuestIDs', set()))
            yearId, _, _, _ = questID.split(b':')
            collectionName = backport.text(self._STR_PATH.collectionMegaComplete(), year=backport.text(R.strings.ny.systemMessage.dyn(yearId)()))
            rows = [
             collectionName]
            rewards = data.get(b'detailedRewards', {}).get(questID)
            self._addFormattedRewards(rewards, rows)
            settings = self._getGuiSettings(message, self._TEMPLATE_NAME)
            formatted = g_settings.msgTemplates.format(self._TEMPLATE_NAME, ctx={b'text': (EOL.join(rows))})
        callback([MessageData(formatted, settings)])
        return

    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        return questID.startswith(NY_COLLECTION_MEGA_PREFIX)


class NewYearOldCollectionRewardFormatter(AsyncTokenQuestsSubFormatter):
    _eventsCache = dependency.descriptor(IEventsCache)
    __TEMPLATE_NAME = b'newYearOldCollectionComplete'

    def __init__(self):
        super(NewYearOldCollectionRewardFormatter, self).__init__()
        self._achievesFormatter = NewYearCollectionFormatter()
        return

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        messages = [MessageData(None, None)]
        if isSynced and message.data:
            data = message.data
            completedQuestIDs = self.getQuestOfThisGroup(data.get(b'completedQuestIDs', set()))
            rewards = getRewardsForQuests(message, completedQuestIDs)
            if rewards:
                fmt = self._achievesFormatter.formatAchieves(rewards)
                formatted = g_settings.msgTemplates.format(self.__TEMPLATE_NAME, ctx={b'text': fmt})
                settings = self._getGuiSettings(message, self.__TEMPLATE_NAME)
                messages = [
                 MessageData(formatted, settings)]
        callback(messages)
        return

    @classmethod
    def _isQuestOfThisGroup(cls, questID):
        return questID.startswith(NY_OLD_COLLECTION_PREFIX)


def registerNewYearTokenQuestsSubFormatters():
    registerTokenQuestsSubFormatters((
     NewYearCollectionRewardFormatter(),
     NewYearLevelUpRewardFormatter()))
    registerHangarQuestSubFormatters([
     NewYearCollectionRewardFormatter(),
     NewYearCollectionMegaRewardFormatter(),
     NewYearLevelUpRewardFormatter(),
     NewYearOldCollectionRewardFormatter()])
    return
