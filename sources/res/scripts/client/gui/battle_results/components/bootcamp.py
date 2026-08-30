from __future__ import absolute_import
import logging
from bootcamp.BootcampConstants import BATTLE_STATS_RESULT_FIELDS, BATTLE_STATS_ICONS
from helpers.i18n import makeString
import BigWorld
from bootcamp.Bootcamp import g_bootcamp
from constants import PREMIUM_ENTITLEMENTS, SPA_ATTRS
from gui import makeHtmlString
from gui.Scaleform.locale.BOOTCAMP import BOOTCAMP
from gui.battle_results.components import base
from gui.battle_results.components.common import makeRegularFinishResultLabel
from gui.battle_results.settings import PLAYER_TEAM_RESULT
from gui.impl import backport
from gui.impl.gen import R
from helpers import dependency
from helpers.bots import preprocessBotName
from shared_utils import first
from skeletons.gui.game_control import IBootcampController
_logger = logging.getLogger(__name__)
_BG_FOLDER_PATH = b'../maps/icons/bootcamp/battle_result/background/'
_BG_IMAGE_FORMATS = {(PLAYER_TEAM_RESULT.WIN): b'bcVictoryBg_{0}.png', 
   (PLAYER_TEAM_RESULT.DEFEAT): b'bcDefeat.png', 
   (PLAYER_TEAM_RESULT.DRAW): b'bcDraw.png'}
_STAT_ICON_PATH = b'../maps/icons/bootcamp/battle_result/{0}.png'
_STAT_ICON_TOOLTIP_PATH = b'../maps/icons/bootcamp/battle_result/tooltip/{0}.png'
_PREMIUM_RESOURCES = {(PREMIUM_ENTITLEMENTS.BASIC): {b'icon': (backport.image(R.images.gui.maps.icons.bootcamp.rewards.bcPremium())), 
                                  b'iconTooltip': (backport.image(R.images.gui.maps.icons.bootcamp.rewards.tooltips.bcPremium())), 
                                  b'label': (backport.text(R.strings.bootcamp.result.award.premium.label())), 
                                  b'description': (backport.text(R.strings.bootcamp.result.award.premium.text()))}, 
   (PREMIUM_ENTITLEMENTS.PLUS): {b'icon': (backport.image(R.images.gui.maps.icons.bootcamp.rewards.bcPremiumPlus())), 
                                 b'iconTooltip': (backport.image(R.images.gui.maps.icons.bootcamp.rewards.tooltips.bcPremiumPlus())), 
                                 b'label': (backport.text(R.strings.bootcamp.result.award.premiumPlus.label())), 
                                 b'description': (backport.text(R.strings.bootcamp.result.award.premiumPlus.text()))}}

def isTechnicalWin(record, reusable):
    teamResult = reusable.getPersonalTeamResult()
    isBattleGoalCompleted = record[b'personal'][b'avatar'][b'vseBattleResults'].get(b'battleGoalCompleted', False)
    return teamResult != PLAYER_TEAM_RESULT.WIN and isBattleGoalCompleted


class BackgroundItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        teamResult = PLAYER_TEAM_RESULT.DRAW if isTechnicalWin(record, reusable) else reusable.getPersonalTeamResult()
        lessonNum = g_bootcamp.getLessonNum() - 1
        value = _BG_FOLDER_PATH + _BG_IMAGE_FORMATS[teamResult].format(lessonNum)
        return value


class RewardsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        teamResult = reusable.getPersonalTeamResult()
        if not isTechnicalWin(result, reusable) and teamResult != PLAYER_TEAM_RESULT.WIN:
            return
        bootcampController = dependency.instance(IBootcampController)
        lessonNum = g_bootcamp.getLessonNum()
        lastLessonNum = g_bootcamp.getContextIntParameter(b'lastLessonNum')
        lessonSpecificExtras = g_bootcamp.getBattleResultsExtra(lessonNum - 1)
        goldPremuimExtras = []
        showPremium = lessonNum == lastLessonNum and bootcampController.needAwarding()
        if showPremium:
            premiumType = g_bootcamp.getPremiumType()
            if premiumType not in _PREMIUM_RESOURCES:
                _logger.error(b'Premium type %s is not supported or it is not in the bonuses', premiumType)
            else:
                goldPremuimExtras.append({b'id': premiumType, 
                   b'label': (_PREMIUM_RESOURCES[premiumType][b'label']), 
                   b'description': (_PREMIUM_RESOURCES[premiumType][b'description']), 
                   b'icon': (_PREMIUM_RESOURCES[premiumType][b'icon']), 
                   b'iconTooltip': (_PREMIUM_RESOURCES[premiumType][b'iconTooltip'])})
                goldPremuimExtras.append({b'id': b'gold', 
                   b'label': (backport.text(R.strings.bootcamp.message.gold.label())), 
                   b'description': (backport.text(R.strings.bootcamp.message.gold.premiumPlus.text())), 
                   b'icon': (backport.image(R.images.gui.maps.icons.bootcamp.rewards.bcGold())), 
                   b'iconTooltip': (backport.image(R.images.gui.maps.icons.bootcamp.rewards.tooltips.bcGold()))})
        self.addNextComponent(base.DirectStatsItem(b'medals', lessonSpecificExtras[b'medals']))
        self.addNextComponent(base.DirectStatsItem(b'ribbons', lessonSpecificExtras[b'ribbons']))
        self.addNextComponent(base.DirectStatsItem(b'unlocks', lessonSpecificExtras[b'unlocks'] + goldPremuimExtras))
        return


class HasUnlocksFlag(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        teamResult = reusable.getPersonalTeamResult()
        if teamResult != PLAYER_TEAM_RESULT.WIN:
            return False
        bootcampController = dependency.instance(IBootcampController)
        lessonNum = g_bootcamp.getLessonNum()
        lastLessonNum = g_bootcamp.getContextIntParameter(b'lastLessonNum')
        lessonSpecificExtras = g_bootcamp.getBattleResultsExtra(lessonNum - 1)
        showPremium = lessonNum == lastLessonNum and bootcampController.needAwarding()
        val = bool(lessonSpecificExtras[b'unlocks']) or showPremium
        return val


class StatsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        info = reusable.getPersonalVehiclesInfo(result[b'personal'])
        teamResult = reusable.getPersonalTeamResult()
        if teamResult == PLAYER_TEAM_RESULT.WIN or isTechnicalWin(result, reusable):
            battleStats = g_bootcamp.getBattleStatsLessonWin()
        else:
            battleStats = g_bootcamp.getBattleStatsLessonDefeat()
        for statType in battleStats:
            statFieldName = BATTLE_STATS_RESULT_FIELDS[statType]
            statVal = info.__getattribute__(statFieldName)
            statVal = backport.getIntegralFormat(statVal)
            self.addNextComponent(base.DirectStatsItem(b'', {b'id': statType, 
               b'label': (makeString(BOOTCAMP.battle_result(statType))), 
               b'description': (makeString(BOOTCAMP.battle_result_description(statType))), 
               b'value': statVal, 
               b'icon': (_STAT_ICON_PATH.format(BATTLE_STATS_ICONS[statType])), 
               b'iconTooltip': (_STAT_ICON_TOOLTIP_PATH.format(BATTLE_STATS_ICONS[statType]))}))

        return


class ResultTypeStrItem(base.StatsItem):
    __slots__ = ()
    COMPLETE = b'complete'

    def _convert(self, record, reusable):
        teamResult = self.COMPLETE if isTechnicalWin(record, reusable) else reusable.getPersonalTeamResult()
        return backport.text(R.strings.bootcamp.resultlabel.dyn(teamResult)())


class FinishReasonStrItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        if isTechnicalWin(record, reusable):
            lessonNum = g_bootcamp.getLessonNum()
            return backport.text(R.strings.bootcamp.completionWithoutVictory.num(lessonNum)())
        teamResult = reusable.getPersonalTeamResult()
        val = makeRegularFinishResultLabel(reusable.common.finishReason, teamResult)
        return val


class FinishReasonItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        if isTechnicalWin(record, reusable):
            return PLAYER_TEAM_RESULT.WIN
        return reusable.getPersonalTeamResult()


class ShowRewardsFlag(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        credit = reusable.personal.getBaseCreditsRecords().getRecord(b'credits')
        xp = reusable.personal.getBaseXPRecords().getRecord(b'xp')
        return credit != 0 or xp != 0


class PlayerResultItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        playerName = record[b'players'].values()[0][b'name']
        itemId, item = first(reusable.personal.getVehicleItemsIterator())
        killerID = record[b'personal'][itemId][b'killerID']
        ctx = {b'player': playerName, 
           b'vehicle': (item.userName)}
        if killerID == 0:
            return makeHtmlString(b'html_templates:bootcamp/player_status', b'alive', ctx=ctx)
        if killerID not in record[b'common'][b'bots']:
            return makeHtmlString(b'html_templates:bootcamp/player_status', b'dead', ctx=ctx)
        killerName = record[b'common'][b'bots'][killerID][1]
        ctx[b'killer'] = preprocessBotName(killerName, reusable.common.arenaBonusType)
        return makeHtmlString(b'html_templates:bootcamp/player_status', b'killed', ctx=ctx)


class VideoButtonsItem(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        player = BigWorld.player()
        teamResult = reusable.getPersonalTeamResult()
        buttons = g_bootcamp.getInterludeVideoButtons()
        if player.spaFlags.getFlag(SPA_ATTRS.BOOTCAMP_VIDEO_DISABLED) or teamResult != PLAYER_TEAM_RESULT.WIN and not isTechnicalWin(record, reusable) or not buttons:
            return None
        return buttons


class CreditsBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        intVal = reusable.personal.getBaseCreditsRecords().getRecord(b'credits')
        strVal = backport.getGoldFormat(intVal)
        self.addNextComponent(base.DirectStatsItem(b'value', intVal))
        self.addNextComponent(base.DirectStatsItem(b'str', strVal))
        return


class XPBlock(base.StatsBlock):
    __slots__ = ()

    def setRecord(self, result, reusable):
        intVal = reusable.personal.getBaseXPRecords().getRecord(b'xp')
        strVal = backport.getIntegralFormat(intVal)
        self.addNextComponent(base.DirectStatsItem(b'value', intVal))
        self.addNextComponent(base.DirectStatsItem(b'str', strVal))
        return


class AlternativeLayoutFlag(base.StatsItem):
    __slots__ = ()

    def _convert(self, record, reusable):
        return isTechnicalWin(record, reusable)
