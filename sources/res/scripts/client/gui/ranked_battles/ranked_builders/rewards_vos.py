import typing
from gui.Scaleform.genConsts.RANKEDBATTLES_CONSTS import RANKEDBATTLES_CONSTS
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import icons, text_styles
from gui.shared.utils.functions import makeTooltip
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.ranked_battles.ranked_builders import shared_vos
from gui.ranked_battles.constants import STANDARD_POINTS_COUNT
if typing.TYPE_CHECKING:
    from gui.ranked_battles.ranked_models import Rank, Division
    from gui.ranked_battles.constants import YearAwardsNames

def getSeasonOnTabs(selectedLinkage, isYearRewardEnabled):
    result = [
     __getRanksTab(selectedLinkage == RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_RANKS_UI, True),
     __getLeaguesTab(selectedLinkage == RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_LEAGUES_UI, True)]
    if isYearRewardEnabled:
        result.append(__getYearRewardTab(selectedLinkage == RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_YEAR_UI, True))
    return result


def getSeasonOffTabs(isYearRewardEnabled):
    result = [
     __getRanksTab(False, False),
     __getLeaguesTab(False, False)]
    if isYearRewardEnabled:
        result.append(__getYearRewardTab(True, True))
    return result


def __getRanksTab(selected, enabled):
    return {b'id': (RANKEDBATTLES_CONSTS.RANKED_BATTLES_REWARDS_RANKEDS_ID), 
       b'label': (backport.text(R.strings.ranked_battles.rewardsView.tabs.ranks())), 
       b'linkage': (RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_RANKS_UI), 
       b'viewId': (RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_RANKS_UI), 
       b'selected': selected, 
       b'enabled': enabled}


def __getLeaguesTab(selected, enabled):
    return {b'id': (RANKEDBATTLES_CONSTS.RANKED_BATTLES_REWARDS_LEAGUES_ID), 
       b'label': (backport.text(R.strings.ranked_battles.rewardsView.tabs.leagues())), 
       b'linkage': (RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_LEAGUES_UI), 
       b'viewId': (RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_LEAGUES_UI), 
       b'selected': selected, 
       b'enabled': enabled}


def __getYearRewardTab(selected, enabled):
    return {b'id': (RANKEDBATTLES_CONSTS.RANKED_BATTLES_REWARDS_YEAR_ID), 
       b'label': (backport.text(R.strings.ranked_battles.rewardsView.tabs.year())), 
       b'linkage': (RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_YEAR_UI), 
       b'viewId': (RANKEDBATTLES_ALIASES.RANKED_BATTLES_REWARDS_YEAR_UI), 
       b'selected': selected, 
       b'enabled': enabled}


def getDivisionVO(division):
    divisionVO = shared_vos.getDivisionVO(division)
    divisionVO.update({b'name': (text_styles.promoTitle(divisionVO[b'name']))})
    return divisionVO


def getRankRewardsVO(rank, bonuses, currentRankID):
    if rank.getID() == currentRankID:
        awardState = RANKEDBATTLES_CONSTS.RANKED_REWARDS_RANK_CURRENT
    elif rank.getID() == currentRankID + 1:
        awardState = RANKEDBATTLES_CONSTS.RANKED_REWARDS_RANK_NEXT
    elif rank.getID() < currentRankID:
        awardState = RANKEDBATTLES_CONSTS.RANKED_REWARDS_RANK_RECEIVED
    else:
        awardState = RANKEDBATTLES_CONSTS.RANKED_REWARDS_RANK_LOCKED
    return {b'state': awardState, b'rankID': (rank.getID()), 
       b'levelStr': (rank.getUserName()), 
       b'bonuses': bonuses}


def getLeagueRewardVO(leagueID, styleBonus, styleID, styleName, badgeID, isCurrent):
    descr = backport.text(R.strings.ranked_battles.rewardsView.tabs.leagues.awardDescr.style(), styleName=styleName, badgeName=backport.text(R.strings.badge.dyn((b'badge_{}').format(badgeID))()))
    return {b'leagueID': leagueID, 
       b'title': (backport.text(R.strings.ranked_battles.rewardsView.tabs.leagues.dyn(b'league%s' % leagueID)())), 
       b'description': descr, 
       b'styleID': styleID, 
       b'isSpecial': (styleBonus.isSpecial), 
       b'specialAlias': (styleBonus.specialAlias), 
       b'isCurrent': isCurrent}


def getYearRewardDataVO(points, awards, rewardingComplete, awardType, compensation, exchange):
    if rewardingComplete:
        title = backport.text(R.strings.ranked_battles.rewardsView.tabs.year.title.awarded(), points=points)
    else:
        title = backport.text(R.strings.ranked_battles.rewardsView.tabs.year.title.notAwarded(), points=points)
    tooltipBody = backport.text(R.strings.tooltips.rankedBattleView.rewardsView.tabs.year.scorePoint.body.mainText())
    if exchange > 0:
        exchangePart = backport.text(R.strings.tooltips.rankedBattleView.rewardsView.tabs.year.scorePoint.body.exchangeText(), points=text_styles.stats(str(STANDARD_POINTS_COUNT)), rankedImg=icons.makeImageTag(backport.image(R.images.gui.maps.icons.rankedBattles.ranked_point_16x16()), 16, 16, -3), crystal=text_styles.stats(exchange), crystalImg=icons.crystal())
        tooltipBody = text_styles.concatStylesToMultiLine(tooltipBody, exchangePart)
    compensationText = b''
    if rewardingComplete and compensation > 0 and exchange > 0:
        if awardType is not None:
            compensationText = text_styles.mainBig(backport.text(R.strings.ranked_battles.rewardsView.tabs.year.compensation.extraPoints(), points=text_styles.highlightText(compensation), rankedImg=icons.makeImageTag(backport.image(R.images.gui.maps.icons.rankedBattles.ranked_point_16x16()), 16, 16, -3), crystal=text_styles.highlightText(compensation * exchange), crystalImg=icons.crystal()))
        else:
            compensationText = text_styles.mainBig(backport.text(R.strings.ranked_battles.rewardsView.tabs.year.compensation.notEnough(), crystal=text_styles.highlightText(compensation * exchange), crystalImg=icons.crystal()))
    return {b'title': title, b'titleIcon': (backport.image(R.images.gui.maps.icons.rankedBattles.ranked_point_28x28())), 
       b'titleTooltip': (makeTooltip(header=backport.text(R.strings.tooltips.rankedBattleView.rewardsView.tabs.year.scorePoint.header()), body=tooltipBody)), 
       b'compensation': compensationText, 
       b'points': points, 
       b'rewards': awards}
