import functools
from battle_pass_common import BattlePassState
from debug_utils import LOG_ERROR_DEV
from gui.Scaleform.daapi.view.lobby.epicBattle.epic_helpers import getFrontLineSkills
from gui.impl import backport
from gui.impl.gen import R
from gui.server_events.awards_formatters import AWARDS_SIZES
from gui.shared.utils.functions import getRelativeUrl
from helpers import dependency
from skeletons.gui.game_control import IEpicBattleMetaGameController, IBattlePassController
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.shared import IItemsCache
from web.web_client_api import w2c, w2capi, W2CSchema, Field
from web.web_client_api.common import ItemPackType

def frontlineDeprecated(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        LOG_ERROR_DEV(b'FrontLineWebApi deprecated due WOTK-36049, move logic to your local api')
        return func(*args, **kwargs)

    return wrapper


class _RewardsSchema(W2CSchema):
    category = Field(type=basestring)


class _SkillSchema(W2CSchema):
    skill_id = Field(required=False, type=int)


@w2capi(name=b'frontline', key=b'action')
class FrontLineWebApi(W2CSchema):
    __epicController = dependency.descriptor(IEpicBattleMetaGameController)
    __battlePassController = dependency.descriptor(IBattlePassController)
    __eventsCache = dependency.descriptor(IEventsCache)
    __itemsCache = dependency.descriptor(IItemsCache)
    _NOT_SUPPORTED_BONUSES = (b'battleToken',)

    @frontlineDeprecated
    @w2c(_RewardsSchema, name=b'get_rewards_data')
    def handleGetRewardsData(self, cmd):
        if hasattr(cmd, b'category') and cmd.category:
            if cmd.category == b'level':
                return self.__getAllLevelAwards()
            if cmd.category == b'vehicles':
                rewardsData = {}
                return rewardsData
            if cmd.category == b'styles':
                rewardsData = {}
                return rewardsData
        return

    @frontlineDeprecated
    @w2c(W2CSchema, name=b'get_all_skills')
    def handleSkillsInfo(self, _):
        return getFrontLineSkills()

    @frontlineDeprecated
    @w2c(W2CSchema, name=b'get_player_skills_status')
    def handleSkillStatus(self, _):
        return {skillID: int(skill.isActivated) for skillID, skill in self.__epicController.getAllSkillsInformation().iteritems()}

    @frontlineDeprecated
    @w2c(W2CSchema, name=b'get_player_skill_points')
    def handleGetSkillPoints(self, _):
        return self.__epicController.getSkillPoints()

    @frontlineDeprecated
    @w2c(W2CSchema, name=b'is_nine_vehicles_level_disabled')
    def handleIsNineVehiclesLevelDisabled(self, _):
        return not self.__epicController.isUnlockVehiclesInBattleEnabled()

    @frontlineDeprecated
    @w2c(_SkillSchema, name=b'increase_player_skill')
    def handleIncreaseSkillLevel(self, cmd):
        if hasattr(cmd, b'skill_id') and cmd.skill_id:
            self.__epicController.increaseSkillLevel(cmd.skill_id)
        return

    @w2c(W2CSchema, name=b'get_player_discount')
    def handleGetPlayerDiscount(self, _):
        return self.__epicController.getStoredEpicDiscount()

    @frontlineDeprecated
    @w2c(W2CSchema, name=b'get_is_battle_pass_completed')
    def handleGetIsBattlePassBought(self, _):
        state = self.__battlePassController.getState()
        return state == BattlePassState.COMPLETED

    @frontlineDeprecated
    @w2c(W2CSchema, name=b'get_metascreen_data')
    def handleGetMetaScreenData(self, _):
        currentLevel, levelProgress = self.__epicController.getPlayerLevelInfo()
        nextLevelExp = self.__epicController.getPointsProgressForLevel(currentLevel)
        data = {b'lvl': currentLevel, 
           b'mode_alias': b'frontline', 
           b'max_lvl': (self.__epicController.getMaxPlayerLevel()), 
           b'exp': levelProgress, 
           b'exp_for_lvl': nextLevelExp, 
           b'rewards_for_lvl': (self.__getLevelAwards(currentLevel + 1)), 
           b'rewards_count': (self.__epicController.getNotChosenRewardCount())}
        return data

    @w2c(W2CSchema, name=b'get_calendar_info')
    def handleGetCalendarInfo(self, _):
        calendarData = dict()
        seasons = (
         self.__epicController.getCurrentSeason(),
         self.__epicController.getNextSeason(),
         self.__epicController.getPreviousSeason())
        for season in seasons:
            if season is not None:
                calendarData[b'season'] = {b'id': (season.getSeasonID()), b'start': (season.getStartDate()), 
                   b'end': (season.getEndDate())}
                calendarData[b'cycles'] = [{b'id': (cycle.ID), b'start': (cycle.startDate), b'end': (cycle.endDate), b'announce_only': (cycle.announceOnly)} for cycle in season.getAllCycles().values()]
                break

        return calendarData

    def __getAllLevelAwards(self):
        awardsData = dict()
        abilityPts = self.__epicController.getAbilityPointsForLevel()
        allLevelData = self.__epicController.getAllLevelRewards()
        for questLvl, rewardData in allLevelData.iteritems():
            bonuses = self.__epicController.replaceOfferByReward(rewardData.getBonuses())
            awardsData[questLvl] = self.__packBonuses(bonuses, questLvl, abilityPts)

        return awardsData

    def __getLevelAwards(self, level):
        allAwards = self.__getAllLevelAwards()
        if level in allAwards:
            return allAwards[level]
        return []

    @classmethod
    def __packBonuses(cls, bonuses, level, abilityPts):
        result = []
        if abilityPts and abilityPts[level - 1]:
            result.append({b'id': 0, 
               b'type': (ItemPackType.CUSTOM_SUPPLY_POINT), 
               b'value': (abilityPts[level - 1]), 
               b'icon': {(AWARDS_SIZES.SMALL): (getRelativeUrl(backport.image(R.images.gui.maps.icons.epicBattles.awards.c_48x48.abilityToken()))), 
                         (AWARDS_SIZES.BIG): (getRelativeUrl(backport.image(R.images.gui.maps.icons.epicBattles.awards.c_80x80.abilityToken())))}})
        for bonus in bonuses:
            if bonus.getName() in cls._NOT_SUPPORTED_BONUSES:
                continue
            bonusList = bonus.getWrappedEpicBonusList()
            for bonusEntry in bonusList:
                bonusEntry[b'icon'] = {size: getRelativeUrl(path) for size, path in bonusEntry[b'icon'].iteritems()}

            result.extend(bonusList)

        return result
