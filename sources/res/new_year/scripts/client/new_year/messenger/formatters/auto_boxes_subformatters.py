import BigWorld
from dossiers2.ui.achievements import BADGES_BLOCK
from gui.impl import backport
from gui_lootboxes.messenger.formatters.auto_boxes_subformatters import AsyncAutoLootBoxSubFormatter
from adisp import adisp_async, adisp_process
from gui.impl.gen import R
from gui.server_events.bonuses import getMergedBonusesFromDicts
from gui.shared.gui_items.dossier import getAchievementFactory
from gui.shared.notifications import NotificationGroup
from new_year.gui.shared.ny_machine_helper import getMachineLootboxTokenId
from messenger import g_settings
from messenger.formatters.service_channel import QuestAchievesFormatter
from messenger.formatters.service_channel_helpers import getRewardsForBoxes, MessageData, getCustomizationItemData
from new_year.ny_constants import NewYearLootBoxes, ALL_LUNAR_NY_LOOT_BOX_TYPES

class NYPostEventBoxesFormatter(AsyncAutoLootBoxSubFormatter):
    __MESSAGE_TEMPLATE = b'LootBoxesAutoOpenMessage'
    __REWARDS_TEMPLATE = b'LootBoxRewardsSysMessage'
    __REQUIERED_BOX_TYPES = {
     NewYearLootBoxes.COMMON_OLD, NewYearLootBoxes.PREMIUM_OLD, NewYearLootBoxes.SPECIAL_OLD}

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        if isSynced:
            openedBoxesIDs = self.getBoxesOfThisGroup(message.data.keys())
            callback([
             self.__getMainMessage(message, openedBoxesIDs),
             self.__getRewardsMessage(message, openedBoxesIDs)])
        else:
            callback([MessageData(None, None)])
        return

    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        return cls._isBoxOfRequiredTypes(boxID, cls.__REQUIERED_BOX_TYPES)

    def __getMainMessage(self, message, openedBoxesIDs):
        count = backport.text(R.strings.messenger.serviceChannelMessages.lootBoxesAutoOpen.event.counter(), count=sum(message.data[boxId][b'count'] for boxId in openedBoxesIDs))
        oldStyleCount = {bID: message.data[bID][b'count'] for bID in openedBoxesIDs}
        rewards = getRewardsForBoxes(message, openedBoxesIDs)
        formatted = g_settings.msgTemplates.format(self.__MESSAGE_TEMPLATE, ctx={b'count': count}, data={b'savedData': {b'rewards': rewards, b'boxIDs': oldStyleCount}})
        settings = self._getGuiSettings(message, self.__MESSAGE_TEMPLATE)
        settings.groupID = NotificationGroup.OFFER
        settings.showAt = BigWorld.time()
        return MessageData(formatted, settings)

    def __getRewardsMessage(self, message, openedBoxesIDs):
        allRewards = getRewardsForBoxes(message, openedBoxesIDs)
        fmt = self._achievesFormatter.formatQuestAchieves(allRewards, asBattleFormatter=False, processTokens=False)
        formattedRewards = g_settings.msgTemplates.format(self.__REWARDS_TEMPLATE, ctx={b'text': fmt})
        settingsRewards = self._getGuiSettings(message, self.__REWARDS_TEMPLATE)
        settingsRewards.showAt = BigWorld.time()
        return MessageData(formattedRewards, settingsRewards)


class NYGiftSystemSurpriseFormatter(AsyncAutoLootBoxSubFormatter):
    __MESSAGE_TEMPLATE = b'NYSpecialLootBoxesAutoOpenMessage'
    __REQUIERED_BOX_TYPES = {NewYearLootBoxes.SPECIAL_AUTO}

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        if isSynced:
            openedBoxesIDs = self.getBoxesOfThisGroup(message.data.keys())
            rewards = getRewardsForBoxes(message, openedBoxesIDs)
            fmt = self._achievesFormatter.formatQuestAchieves(rewards, asBattleFormatter=False, processTokens=False)
            formattedData = g_settings.msgTemplates.format(self.__MESSAGE_TEMPLATE, ctx={b'achieves': fmt})
            settings = self._getGuiSettings(message, self.__MESSAGE_TEMPLATE)
            settings.showAt = BigWorld.time()
            callback([MessageData(formattedData, settings)])
        else:
            callback([MessageData(None, None)])
        return

    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        return cls._isBoxOfRequiredTypes(boxID, cls.__REQUIERED_BOX_TYPES)


class LunarNYEnvelopeAutoOpenFormatter(AsyncAutoLootBoxSubFormatter):
    __MESSAGE_TEMPLATE = b'LunarBoxesAutoOpenMessage'
    _DECAL_TYPE_NAME = b'projection_decal'

    def __init__(self):
        super(LunarNYEnvelopeAutoOpenFormatter, self).__init__()
        self._achievesFormatter = QuestAchievesFormatter()
        return

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        if isSynced:
            openedBoxesIDs = self.getBoxesOfThisGroup(message.data.keys())
            rewards = getRewardsForBoxes(message, openedBoxesIDs)
            if b'charms' in rewards:
                rewards.pop(b'charms')
            if b'customizationSum' in rewards:
                rewards.pop(b'customizationSum')
            fmt = self.formatAchieves(rewards, self._achievesFormatter)
            formattedRewards = g_settings.msgTemplates.format(self.__MESSAGE_TEMPLATE, ctx={b'rewards': fmt})
            settingsRewards = self._getGuiSettings(message, self.__MESSAGE_TEMPLATE)
            settingsRewards.showAt = BigWorld.time()
            callback([MessageData(formattedRewards, settingsRewards)])
        else:
            callback([MessageData(None, None)])
        return

    @classmethod
    def formatAchieves(cls, rewards, formatter):
        result = []
        items = getMergedBonusesFromDicts((rewards,))
        formatedItems = formatter.formatQuestAchieves(items, False, processCustomizations=False)
        if formatedItems:
            result.append(formatedItems)
        if b'customizations' in rewards:
            customizations = rewards.get(b'customizations')
            decalsStr = cls.__makeDecalsString(customizations)
            if decalsStr:
                result.append(decalsStr)
        achievementsNames = cls.__extractAchievements(items)
        if achievementsNames:
            result.append(cls.__makeAchieve(b'dossiersAccruedInvoiceReceived', dossiers=(b', ').join(achievementsNames)))
        return (b'<br/>').join(result)

    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        return cls._isBoxOfRequiredTypes(boxID, ALL_LUNAR_NY_LOOT_BOX_TYPES)

    @classmethod
    def __makeAchieve(cls, key, **kwargs):
        return g_settings.htmlTemplates.format(key, kwargs)

    @staticmethod
    def __extractAchievements(data):
        result = set()
        for block in data.get(b'dossier', {}).values():
            if isinstance(block, dict):
                for record in block.keys():
                    if record[0] == BADGES_BLOCK:
                        continue
                    factory = getAchievementFactory(record)
                    if factory is not None:
                        a = factory.create()
                        if a is not None:
                            result.add(a.getUserName())

        return result

    @classmethod
    def __makeDecalsString(cls, customizations):
        decals = []
        for customization in customizations:
            custType = customization.get(b'custType', None)
            custValue = customization.get(b'value', 0)
            if custType == cls._DECAL_TYPE_NAME and custValue > 0:
                _, itemUserName = getCustomizationItemData(customization[b'id'], custType)
                decals.append(itemUserName)

        if len(decals) > 1:
            decalsTitle = backport.text(R.strings.messenger.serviceChannelMessages.lunarBoxesAutoOpen.many.projection_decal())
            return decalsTitle + (b' ').join(decals)
        else:
            if decals:
                decalsTitle = backport.text(R.strings.messenger.serviceChannelMessages.lunarBoxesAutoOpen.projection_decal())
                return (b'').join((decalsTitle, decals[0]))
            return b''


class NYPostEventSurpriseMachineFormatter(AsyncAutoLootBoxSubFormatter):
    __MESSAGE_TEMPLATE = b'NYSurpriseMachineRewardsSysMessage'

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        if not isSynced:
            callback([MessageData(None, None)])
            return
        else:
            boxData = message.data.get(getMachineLootboxTokenId(), {})
            ctx = {b'coins': (boxData[b'count']), 
               b'rewards': (self._achievesFormatter.formatQuestAchieves(boxData[b'rewards'], asBattleFormatter=False, processTokens=False))}
            formattedRewards = g_settings.msgTemplates.format(self.__MESSAGE_TEMPLATE, ctx=ctx)
            settingsRewards = self._getGuiSettings(message, self.__MESSAGE_TEMPLATE)
            settingsRewards.showAt = BigWorld.time()
            callback([MessageData(formattedRewards, settingsRewards)])
            return

    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        return boxID == getMachineLootboxTokenId()
