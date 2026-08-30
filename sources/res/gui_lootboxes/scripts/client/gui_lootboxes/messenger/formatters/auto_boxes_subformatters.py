import BigWorld, typing
from adisp import adisp_async, adisp_process
from dossiers2.ui.achievements import BADGES_BLOCK
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events.bonuses import getMergedBonusesFromDicts
from gui.shared.gui_items.dossier import getAchievementFactory
from gui.shared.gui_items.loot_box import ALL_LUNAR_NY_LOOT_BOX_TYPES, EventLootBoxes, WTLootBoxes, NewYearLootBoxes
from helpers import dependency, time_utils
from messenger import g_settings
from messenger.formatters.service_channel import LootBoxAchievesFormatter, QuestAchievesFormatter, ServiceChannelFormatter, WaitItemsSyncFormatter
from messenger.formatters.service_channel_helpers import MessageData, getCustomizationItemData, getRewardsForBoxes
from skeletons.gui.game_control import ISummerSaleController
from skeletons.gui.shared import IItemsCache
from shared_utils import first

class IAutoLootBoxSubFormatter(object):

    @classmethod
    def getBoxesOfThisGroup(cls, boxIDs):
        return

    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        return

    @classmethod
    def _isBoxOfRequiredTypes(cls, boxID, boxTypes):
        return


class AutoLootBoxSubFormatter(IAutoLootBoxSubFormatter):
    __itemsCache = dependency.descriptor(IItemsCache)

    @classmethod
    def getBoxesOfThisGroup(cls, boxIDs):
        return set(boxID for boxID in boxIDs if cls._isBoxOfThisGroup(boxID))

    @classmethod
    def _isBoxOfRequiredTypes(cls, boxID, boxTypes):
        box = cls.__itemsCache.items.tokens.getLootBoxByID(boxID)
        return box is not None and box.getType() in boxTypes


class AsyncAutoLootBoxSubFormatter(WaitItemsSyncFormatter, AutoLootBoxSubFormatter):

    def __init__(self):
        super(AsyncAutoLootBoxSubFormatter, self).__init__()
        self._achievesFormatter = LootBoxAchievesFormatter()
        return


class SyncAutoLootBoxSubFormatter(ServiceChannelFormatter, AutoLootBoxSubFormatter):

    def __init__(self):
        super(SyncAutoLootBoxSubFormatter, self).__init__()
        self._achievesFormatter = LootBoxAchievesFormatter()
        return


class EventBoxesFormatter(AsyncAutoLootBoxSubFormatter):
    __itemsCache = dependency.descriptor(IItemsCache)

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        if isSynced:
            openedBoxesIDs = self.getBoxesOfThisGroup(message.data.keys())
            rewards = getRewardsForBoxes(message, openedBoxesIDs)
            fmtBoxes = self.__getFormattedBoxes(message, openedBoxesIDs)
            fmt = self._achievesFormatter.formatQuestAchieves(rewards, asBattleFormatter=False, processTokens=False)
            ctx = {b'boxes': fmtBoxes, b'rewards': (backport.text(self._getTextResPath().rewards(), rewards=fmt))}
            formatted = g_settings.msgTemplates.format(self._getMessageTemplate(), ctx=ctx)
            settings = self._getGuiSettings(message, self._getMessageTemplate())
            callback([MessageData(formatted, settings)])
        else:
            callback([MessageData(None, None)])
        return

    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        return cls._isBoxOfRequiredTypes(boxID, WTLootBoxes.ALL())

    @staticmethod
    def _getMessageTemplate():
        return b'EventLootBoxesAutoOpenMessage'

    @staticmethod
    def _getTextResPath():
        return R.strings.messenger.serviceChannelMessages.lootBoxesAutoOpen.event

    def __getFormattedBoxes(self, message, openedBoxesIDs):
        boxes = []
        for boxID in openedBoxesIDs:
            box = self.__itemsCache.items.tokens.getLootBoxByID(boxID)
            boxes.append(backport.text(self._getTextResPath().counter(), boxName=box.getUserName(), count=message.data[boxID][b'count']))

        return (b', ').join(boxes)


class EventLootBoxesFormatter(EventBoxesFormatter):

    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        return cls._isBoxOfRequiredTypes(boxID, EventLootBoxes.ALL())

    @staticmethod
    def _getMessageTemplate():
        return b'EventLootBoxesAutoOpenMessage'

    @staticmethod
    def _getTextResPath():
        return R.strings.lootboxes.notification.lootBoxesAutoOpen


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
            openedBoxesIDs = self.getBoxesOfThisGroup(message.data.keys())
            count = sum(message.data.get(boxId, {}).get(b'count', 0) for boxId in openedBoxesIDs)
            rewards = getRewardsForBoxes(message, openedBoxesIDs)
            ctx = {b'coins': (backport.text(R.strings.lb_messenger.serviceChannelMessages.nyMachine.autoopen.machineCoin(), coins=count)), 
               b'rewards': (self._achievesFormatter.formatQuestAchieves(rewards, asBattleFormatter=False, processTokens=False))}
            formattedRewards = g_settings.msgTemplates.format(self.__MESSAGE_TEMPLATE, ctx=ctx)
            settingsRewards = self._getGuiSettings(message, self.__MESSAGE_TEMPLATE)
            settingsRewards.showAt = BigWorld.time()
            callback([MessageData(formattedRewards, settingsRewards)])
            return

    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        return cls._isBoxOfRequiredTypes(boxID, (NewYearLootBoxes.SURPRISE_COIN,))


class ImmediatelyOpenLootBoxFormatter(AsyncAutoLootBoxSubFormatter):
    DEFAULT_HEADER = R.strings.lb_messenger.serviceChannelMessages.immediatelyOpen.header.default
    __MESSAGE_TEMPLATE = b'ImmediatelyOpenLootBoxSysMessage'
    __immediatelyOpenBoxType = set()
    __summerSaleController = dependency.descriptor(ISummerSaleController)
    __itemsCache = dependency.descriptor(IItemsCache)

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isSynced = yield self._waitForSyncItems()
        if not isSynced:
            callback([MessageData(None, None)])
            return
        else:
            openedBoxesIDs = self.getBoxesOfThisGroup(message.data.keys())
            rewards = getRewardsForBoxes(message, openedBoxesIDs)
            ctx = {b'rewards': (self._achievesFormatter.formatQuestAchieves(rewards, asBattleFormatter=False, processTokens=False)), 
               b'date': (backport.getDateTimeFormat(time_utils.getServerRegionalTime())), 
               b'header': (self.__formHeader(first(openedBoxesIDs)))}
            formattedRewards = g_settings.msgTemplates.format(self.__MESSAGE_TEMPLATE, ctx=ctx)
            settingsRewards = self._getGuiSettings(message, self.__MESSAGE_TEMPLATE)
            settingsRewards.showAt = BigWorld.time()
            callback([MessageData(formattedRewards, settingsRewards)])
            return

    @classmethod
    def _isBoxOfThisGroup(cls, boxID):
        return cls._isBoxOfRequiredTypes(boxID, cls.__getLootBoxType())

    @classmethod
    def __getLootBoxType(cls):
        cls.__immediatelyOpenBoxType.update(lb.getType() for lb in cls.__itemsCache.items.tokens.getLootBoxes().values() if lb.isImmediatelyOpen)
        return cls.__immediatelyOpenBoxType

    def __formHeader(self, boxID):
        lootbox = self.__itemsCache.items.tokens.getLootBoxByID(boxID)
        headerStr = backport.text(R.strings.lb_messenger.serviceChannelMessages.immediatelyOpen.header.dyn(lootbox.getUserNameKey(), self.DEFAULT_HEADER)())
        return headerStr
