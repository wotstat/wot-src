import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.ranked_battles.ranked_helpers.web_season_provider import TOP_LEAGUE_ID
from gui.shared.utils.functions import makeTooltip
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.shared.formatters import text_styles, icons

def getFinishSeasonData(efficiencyValue, seasonNumber):
    return {b'typeTitle': (backport.text(R.strings.ranked_battles.seasonComplete.smallTitle())), 
       b'typeIcon': (backport.image(R.images.gui.maps.icons.battleTypes.c_40x40.ranked())), 
       b'seasonTitle': (backport.text(R.strings.ranked_battles.seasonComplete.bigTitle(), season=str(seasonNumber))), 
       b'effectValue': (backport.getIntegralFormat(int(round(efficiencyValue)))), 
       b'effectLabel': (backport.text(R.strings.ranked_battles.seasonComplete.effectLabel())), 
       b'btnLabel': (backport.text(R.strings.ranked_battles.seasonComplete.leadersButton())), 
       b'bgSource': (backport.image(R.images.gui.maps.icons.rankedBattles.bg.main()))}


def getFinishInLeagueData(league, position, seasonNumber, isSprinter):
    header = backport.text(R.strings.ranked_battles.rankedBattleMainView.leaguesView.dyn((b'league{}').format(league))())
    body = backport.text(R.strings.ranked_battles.seasonComplete.tooltip.body(), season=str(seasonNumber))
    sprinterLabel = b''
    if isSprinter:
        if league == TOP_LEAGUE_ID:
            sprinterLabel = backport.text(R.strings.ranked_battles.seasonComplete.sprinterTop())
        else:
            sprinterLabel = backport.text(R.strings.ranked_battles.seasonComplete.sprinterImproved())
        sprinterLabel = text_styles.concatStylesToSingleLine(icons.makeImageTag(backport.image(R.images.gui.maps.icons.rankedBattles.sprinter_icon()), 32, 17, -3), text_styles.highlightText(sprinterLabel))
    return {b'mainImage': (backport.image(R.images.gui.maps.icons.rankedBattles.league.c_300x300.num(league)())), 
       b'state': (RANKEDBATTLES_ALIASES.SEASON_COMPLETE_VIEW_LEAGUE_STATE), 
       b'placeLabel': (backport.text(R.strings.ranked_battles.seasonComplete.placeInRating())), 
       b'placeValue': position, 
       b'placeTooltip': (TOOLTIPS_CONSTANTS.RANKED_BATTLES_POSITION), 
       b'descr': b'', 
       b'sprinterLabel': sprinterLabel, 
       b'tooltip': (makeTooltip(header=header, body=body))}


def getFinishInDivisionsData(division, rankID, seasonNumber):
    divisionID = division.getID()
    divisionName = backport.text(R.strings.ranked_battles.division.dyn(division.getUserID())())
    rankUserID = division.getRankUserName(rankID)
    header = backport.text(R.strings.ranked_battles.seasonComplete.division.tooltip.header(), rank=rankUserID, division=divisionName)
    body = backport.text(R.strings.ranked_battles.seasonComplete.tooltip.body(), season=str(seasonNumber))
    return {b'mainImage': (backport.image(R.images.gui.maps.icons.rankedBattles.ranks.c_190x260.dyn(b'rank%s_%s' % (divisionID, rankUserID))())), 
       b'state': (RANKEDBATTLES_ALIASES.SEASON_COMPLETE_VIEW_DIVISION_STATE), 
       b'placeLabel': (backport.text(R.strings.ranked_battles.seasonComplete.outOfRating())), 
       b'placeValue': b'', 
       b'descr': (backport.text(R.strings.ranked_battles.seasonComplete.bestRank())), 
       b'tooltip': (makeTooltip(header=header, body=body))}


def getAwardsData(awards):
    return {b'ribbonType': b'ribbon2', 
       b'rendererLinkage': b'RibbonAwardAnimUI', 
       b'gap': 20, 
       b'rendererWidth': 80, 
       b'rendererHeight': 80, 
       b'awards': awards}
