import typing
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from gui.ranked_battles import ranked_formatters
from gui.ranked_battles.ranked_builders import shared_vos
from gui.ranked_battles.ranked_builders.shared_vos import getStatVO

def getEfficiencyVO(currentSeasonEfficiency, currentSeasonEfficiencyDiff):
    resultVO = shared_vos.getEfficiencyVO(currentSeasonEfficiency, currentSeasonEfficiencyDiff)
    resultVO[b'label'] = text_styles.alignText(text_styles.mainBig(backport.text(R.strings.ranked_battles.rankedBattleMainView.stats.seasonEfficiency())), b'center')
    return resultVO


def getLeagueVO(leagueID, isSprinter, isTop, yearLBsize, isYearLBEnabled):
    resShortCut = R.strings.ranked_battles.rankedBattleMainView.leaguesView
    title = backport.text(resShortCut.unavailableTitle())
    desc = backport.text(resShortCut.unavailableDescr())
    topText = b''
    sprinterImg = b''
    if leagueID:
        title = backport.text(resShortCut.dyn((b'league{}').format(leagueID))())
        descRes = resShortCut.topDescr() if isTop else resShortCut.descr()
        desc = backport.text(descRes, count=yearLBsize)
        sprinterImg = backport.image(R.images.gui.maps.icons.rankedBattles.sprinter_icon()) if isSprinter else b''
        topText = backport.text(resShortCut.top(), count=yearLBsize) if isTop and isYearLBEnabled else b''
    if not isYearLBEnabled:
        desc = backport.text(resShortCut.yearLeaderboardDisabled())
    return {b'title': title, 
       b'descr': desc, 
       b'league': leagueID, 
       b'sprinterImg': sprinterImg, 
       b'topText': topText}


def getRatingVO(rating):
    resultVO = shared_vos.getRatingVO(rating)
    resultVO[b'label'] = text_styles.alignText(text_styles.mainBig(backport.text(R.strings.ranked_battles.rankedBattleMainView.stats.rating.title())), b'center')
    return resultVO


def getStatsVO(amountStepsInLeagues, amountBattlesInLeagues, amountSteps, amountBattles):
    return {b'stripesInLeague': (getStatVO(ranked_formatters.getIntegerStrStat(amountStepsInLeagues), b'stripesInLeague', b'stripes', b'stripesInLeague')), 
       b'battlesInLeague': (getStatVO(ranked_formatters.getIntegerStrStat(amountBattlesInLeagues), b'battlesInLeague', b'battles', b'battlesInLeague')), 
       b'stripesTotal': (getStatVO(ranked_formatters.getIntegerStrStat(amountSteps), b'stripesTotal', b'stripesTotal', b'stripesTotal')), 
       b'battlesTotal': (getStatVO(ranked_formatters.getIntegerStrStat(amountBattles), b'battlesTotal', b'battlesTotal', b'battlesTotal'))}
