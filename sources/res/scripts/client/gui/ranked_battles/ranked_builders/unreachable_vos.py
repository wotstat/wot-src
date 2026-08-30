from gui.impl import backport
from gui.impl.gen import R
from gui.shared.formatters import text_styles
from helpers import int2roman
from main_page_vos import getRankedMainSeasonOnHeader

def getUnreachableVO(season, minLevel, maxLevel, isAvailableForBuy, isAvailableForRestore):
    levelsStr = __formatUnreachableLevels(minLevel, maxLevel)
    centerText = R.strings.ranked_battles.rankedBattlesUnreachableView.vehicleUnavailable
    if isAvailableForBuy:
        centerText = R.strings.ranked_battles.rankedBattlesUnreachableView.vehicleAvailableForBuy
    elif isAvailableForRestore:
        centerText = R.strings.ranked_battles.rankedBattlesUnreachableView.vehicleAvailableForRestore
    return {b'bottomRules': (__formatBottomItems()), b'header': (getRankedMainSeasonOnHeader(season, None)), 
       b'centerText': (text_styles.vehicleStatusCriticalText(backport.text(centerText(), levels=levelsStr))), 
       b'bottomText': (text_styles.highTitle(backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.bottomText(), levels=levelsStr))), 
       b'closeBtnLabel': (backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.closeBtnLabel())), 
       b'closeBtnTooltip': b'', 
       b'bgImage': (backport.image(R.images.gui.maps.icons.rankedBattles.bg.main())), 
       b'centerImg': (backport.image(R.images.gui.maps.icons.rankedBattles.XlessView.ranked_battle_locked_sm())), 
       b'centerImgBig': (backport.image(R.images.gui.maps.icons.rankedBattles.XlessView.ranked_battle_locked_big()))}


def __formatBottomItems():
    return [
     {b'tooltip': b'', 
        b'image': (backport.image(R.images.gui.maps.icons.rankedBattles.XlessView.icon_prem())), 
        b'description': (text_styles.main(backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.bottom.premium(), premiumType=backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.bottom.premium.plus()))))},
     {b'tooltip': b'', 
        b'image': (backport.image(R.images.gui.maps.icons.rankedBattles.XlessView.icon_ranks_task_200x100())), 
        b'description': (text_styles.main(backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.bottom.missions())))},
     {b'tooltip': b'', 
        b'image': (backport.image(R.images.gui.maps.icons.rankedBattles.XlessView.icon_reserves())), 
        b'description': (text_styles.main(backport.text(R.strings.ranked_battles.rankedBattlesUnreachableView.bottom.reserves())))}]


def __formatUnreachableLevels(minLevel, maxLevel):
    if minLevel == maxLevel:
        return int2roman(minLevel)
    return (b'{0}-{1}').format(int2roman(minLevel), int2roman(maxLevel))
