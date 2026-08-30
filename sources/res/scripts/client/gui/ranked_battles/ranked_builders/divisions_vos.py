import typing
from gui.Scaleform.genConsts.RANKEDBATTLES_ALIASES import RANKEDBATTLES_ALIASES
from gui.impl import backport
from gui.impl.gen import R
from gui.ranked_battles import ranked_formatters
from gui.ranked_battles.ranked_builders import shared_vos
from gui.shared.formatters import text_styles
if typing.TYPE_CHECKING:
    from gui.ranked_battles.ranked_models import Division, Rank

def getDivisionVO(division):
    alias = _getAlias()
    divisionVO = shared_vos.getDivisionVO(division)
    divisionVO.update({b'name': (text_styles.middleTitle(divisionVO[b'name'])), 
       b'linkage': alias, 
       b'viewId': alias})
    return divisionVO


def getDivisionStatsVO(divisionEfficiencyPercent, seasonEfficiencyPercent):
    return {b'divisionEfficiency': (shared_vos.getStatVO(ranked_formatters.getFloatPercentStrStat(divisionEfficiencyPercent), b'divisionEfficiency', b'divisionEfficiency', b'divisionEfficiency')), 
       b'seasonEfficiency': (shared_vos.getStatVO(ranked_formatters.getFloatPercentStrStat(seasonEfficiencyPercent), b'seasonEfficiency', b'efficiency', b'seasonEfficiency'))}


def getRankVO(rank):
    steps = []
    achivedStepsCount = rank.getAchievedStepsCount()
    for idx in range(1, rank.getStepsCountToAchieve() + 1):
        if idx <= achivedStepsCount:
            steps.append(RANKEDBATTLES_ALIASES.STEP_RECEIVED_STATE)
        else:
            steps.append(RANKEDBATTLES_ALIASES.STEP_NOT_RECEIVED_STATE)

    shieldVO = None
    shieldStatus = rank.getShieldStatus()
    if shieldStatus is not None and shieldStatus.hp > 0:
        shortcut = R.images.gui.maps.icons.rankedBattles.ranks.shields
        hpShortcut = R.images.gui.maps.icons.rankedBattles.ranks.shields.plate
        shieldKey = (b'c_{}').format(shieldStatus.hp)
        shieldVO = {b'smallImageSrc': (backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_SMALL)())), 
           b'bigImageSrc': (backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_BIG)())), 
           b'hugeImageSrc': (backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_HUGE)())), 
           b'smallPlateSrc': (backport.image(hpShortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_SMALL).dyn(shieldKey)())), 
           b'mediumPlateSrc': (backport.image(hpShortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_MEDIUM).dyn(shieldKey)())), 
           b'bigPlateSrc': (backport.image(hpShortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_BIG).dyn(shieldKey)())), 
           b'hugePlateSrc': (backport.image(hpShortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_HUGE).dyn(shieldKey)()))}
    elif rank.isVisualUnburnable():
        shortcut = R.images.gui.maps.icons.rankedBattles.ranks.unburnable
        shieldVO = {b'smallImageSrc': (backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_SMALL)())), 
           b'bigImageSrc': (backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_BIG)())), 
           b'hugeImageSrc': (backport.image(shortcut.dyn(RANKEDBATTLES_ALIASES.WIDGET_HUGE)()))}
    return {b'stepsData': {b'steps': steps, 
                      b'infoText': b''}, 
       b'rankLabel': (backport.text(R.strings.ranked_battles.rankedBattleMainView.divisions.currentRank()) if rank.isCurrent() else b''), 
       b'smallImageSrc': (rank.getIcon(RANKEDBATTLES_ALIASES.WIDGET_SMALL)), 
       b'bigImageSrc': (rank.getIcon(RANKEDBATTLES_ALIASES.WIDGET_BIG)), 
       b'hugeImageSrc': (rank.getIcon(RANKEDBATTLES_ALIASES.WIDGET_HUGE)), 
       b'isAcquired': (rank.isAcquired()), 
       b'rankID': (str(rank.getID())), 
       b'hasTooltip': True, 
       b'shield': shieldVO}


def _getAlias():
    return RANKEDBATTLES_ALIASES.RANKED_BATTLES_DIVISIONS_PROGRESS_UI
