from adisp import adisp_async, adisp_process
from constants import SCENARIO_RESULT
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.gui_items import getItemTypeID
from gui.shared.gui_items.Vehicle import getUserName
from helpers import time_utils, dependency
from items import vehicles as vehicles_core
from messenger import g_settings
from messenger.formatters import TimeFormatter
from messenger.formatters.service_channel import BattleResultsFormatter, ServiceChannelFormatter
from messenger.formatters.service_channel_helpers import MessageData
from skeletons.gui.shared import IItemsCache
from story_mode_common.story_mode_constants import MissionId
from story_mode.gui.shared.utils import getRewardList, getTasksCount
from story_mode.skeletons.story_mode_controller import IStoryModeController
from skeletons.gui.customization import ICustomizationService
from skeletons.gui.battle_results import IBattleResultsService
from skeletons.gui.game_control import IBattlePassController

class StoryModeResultsFormatter(BattleResultsFormatter):
    _storyModeCtrl = dependency.descriptor(IStoryModeController)
    _battleResultsService = dependency.descriptor(IBattleResultsService)
    _customizationService = dependency.descriptor(ICustomizationService)
    _battlePass = dependency.descriptor(IBattlePassController)
    _itemsCache = dependency.descriptor(IItemsCache)

    @adisp_async
    @adisp_process
    def format(self, message, callback):
        isForceOnboarding = message.data.get(b'isForceOnboarding', False)
        if isForceOnboarding:
            callback([])
        else:
            messages = yield super(StoryModeResultsFormatter, self).format(message)
            callback(messages)
        return

    def _prepareFormatData(self, message):
        missionId = message.data.get(b'missionId', MissionId.ONE)
        isOnboarding = self._storyModeCtrl.missions.isOnboarding(missionId)
        if isOnboarding:
            self._battleResultKeys = {(SCENARIO_RESULT.LOSE): b'storyModeOnboardingBattleDefeatResult', (SCENARIO_RESULT.PARTIAL): b'storyModeOnboardingBattleDefeatResult', 
               (SCENARIO_RESULT.WIN): b'storyModeOnboardingBattleVictoryResult'}
        else:
            self._battleResultKeys = {(SCENARIO_RESULT.LOSE): b'storyModeRegularBattleDefeatResult', (SCENARIO_RESULT.PARTIAL): b'storyModeRegularBattleDefeatResult', 
               (SCENARIO_RESULT.WIN): b'storyModeRegularBattleVictoryResult'}
        templateName, ctx = super(StoryModeResultsFormatter, self)._prepareFormatData(message)
        ctx[b'scenarioName'] = backport.text(R.strings.sm_battle.prebattle.mission.title.num(missionId)())
        if isOnboarding:
            return (templateName, ctx)
        ctx[b'missionsStr'] = b''
        ctx[b'xpStr'] = b''
        ctx[b'bpPointsStr'] = b''
        ctx[b'crystalStr'] = b''
        ctx[b'creditsStr'] = b''
        ctx[b'rewardsStr'] = b''
        ctx[b'equipCoinStr'] = b''
        progressionInfo = message.data.get(b'progressionInfo', {})
        rewardList = getRewardList(progressionInfo, self._battlePass.isActive())
        completedTasksCount, tasksToCompleteCount = getTasksCount(progressionInfo)
        if tasksToCompleteCount:
            ctx[b'missionsStr'] = g_settings.htmlTemplates.format(b'missionCompleted', {b'completedTasksCount': completedTasksCount, b'tasksToCompleteCount': tasksToCompleteCount})
        freeXP = 0
        credits = 0
        bpPoints = 0
        crystal = 0
        customizations = []
        premium = 0
        items = {}
        vehicles = []
        slots = 0
        equipCoin = 0
        for reward in rewardList:
            credits += reward.get(b'credits', 0)
            freeXP += reward.get(b'freeXP', 0)
            bpPoints += sum(points for points in reward.get(b'battlePassPoints', {}).get(b'vehicles', {}).itervalues())
            crystal += reward.get(b'crystal', 0)
            customizations += reward.get(b'customizations', [])
            premium += reward.get(b'premium_plus', 0)
            slots += reward.get(b'slots', 0)
            equipCoin += reward.get(b'equipCoin', 0)
            if b'items' in reward:
                for itemKey, amount in reward[b'items'].iteritems():
                    items[itemKey] = items.get(itemKey, 0) + amount

            vehicles += reward.get(b'vehicles', [])

        if freeXP:
            ctx[b'xpStr'] = g_settings.htmlTemplates.format(b'xpEarned', {b'freeXP': freeXP})
        if bpPoints:
            ctx[b'bpPointsStr'] = g_settings.htmlTemplates.format(b'bpPointsEarned', {b'bpPoints': bpPoints})
        if crystal:
            ctx[b'crystalStr'] = g_settings.htmlTemplates.format(b'crystalEarned', {b'crystal': crystal})
        if equipCoin:
            ctx[b'equipCoinStr'] = g_settings.htmlTemplates.format(b'equipCoinEarned', {b'equipCoin': equipCoin})
        if credits:
            ctx[b'creditsStr'] = g_settings.htmlTemplates.format(b'creditEarned', {b'credits': credits})
        haveRewardsStr = bool(premium or vehicles or items or customizations)
        if haveRewardsStr:
            rewardsStr = g_settings.htmlTemplates.format(b'rewardsStr', {b'rewardsStr': (backport.text(R.strings.sm_messenger.result.reward()) + b'<br/>')})
            if premium:
                rewardsStr += g_settings.htmlTemplates.format(b'premiumEarned', {b'premium_plus': premium})
            commaItems = []
            if vehicles:
                commaItems += [getUserName(vehicles_core.getVehicleType(vehicle)) for vehicle in vehicles]
            if slots:
                commaItems.append(backport.text(R.strings.sm_messenger.result.slots()) + b'&nbsp;(x' + str(slots) + b')')
            if items:
                for itemKey in sorted(items.iterkeys(), reverse=True):
                    item = self._itemsCache.items.getItemByCD(itemKey)
                    commaItems.append(item.userName + b'&nbsp;(x' + str(items[itemKey]) + b')')

            if customizations:
                for customization in customizations:
                    itemTypeID = getItemTypeID(customization[b'custType'])
                    if itemTypeID:
                        style = self._customizationService.getItemByID(itemTypeID, customization[b'id'])
                        commaItems.append(style.userName + b'&nbsp;(x' + str(customization[b'value']) + b')')

            if commaItems:
                if premium:
                    rewardsStr += b'<br/>'
                rewardsStr += g_settings.htmlTemplates.format(b'commaItems', {b'items': ((b', ').join(commaItems))})
            ctx[b'rewardsStr'] = rewardsStr
        return (templateName, ctx)


class StoryModeAwardFormatter(ServiceChannelFormatter):
    __TEMPLATE = b'storyModeAwardMessage'

    def format(self, message, *args):
        medal = message.data.get(b'medalName')
        badge = message.data.get(b'badgeId')
        medalAward = backport.text(R.strings.sm_messenger.medal.medalName(), medal_name=backport.text(R.strings.achievements.dyn(medal)())) if medal else None
        badgeAward = backport.text(R.strings.sm_messenger.medal.badgeName(), badge_name=backport.text(R.strings.badge.dyn(b'badge_' + str(badge))())) if badge else None
        if medalAward and badgeAward:
            award = backport.text(R.strings.sm_messenger.medal.badgeAndMedal(), medal=medalAward, badge=badgeAward)
        elif medalAward:
            award = medalAward
        else:
            award = badgeAward
        formatted = g_settings.msgTemplates.format(self.__TEMPLATE, {b'at': (TimeFormatter.getLongDatetimeFormat(time_utils.makeLocalServerTime(message.sentTime))), 
           b'award': award})
        return [
         MessageData(formatted, self._getGuiSettings(message, self.__TEMPLATE))]
