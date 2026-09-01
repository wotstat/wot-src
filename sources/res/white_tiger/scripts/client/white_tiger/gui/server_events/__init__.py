from __future__ import absolute_import

def registerWhiteTigerBattleResultsKeys():
    from gui.server_events.cond_formatters import BATTLE_RESULTS_KEYS
    from personal_missions_constants import CONDITION_ICON
    BATTLE_RESULTS_KEYS.update({b'wtBossVulnerableDamage': (CONDITION_ICON.DAMAGE), 
       b'maxWtPlasmaBonus': (CONDITION_ICON.IMPROVE), 
       b'wtGeneratorsCaptured': (CONDITION_ICON.BASE_CAPTURE), 
       b'wtDeathCount': (CONDITION_ICON.SURVIVE), 
       b'wtMiniBossDestroyed': (CONDITION_ICON.DAMAGE), 
       b'wtKilledByHyperionCount': (CONDITION_ICON.SURVIVE), 
       b'wtBattleVSPriorityBoss': (CONDITION_ICON.DAMAGE)})
    return


def registerWhiteTigerDailyQuestDecorationMap():
    from constants import DailyQuestDecorationMap
    from soft_exception import SoftException
    from white_tiger.gui.white_tiger_gui_constants import WTDailyQuestDecorationMap
    commonKeys = set(DailyQuestDecorationMap) & set(WTDailyQuestDecorationMap)
    if commonKeys:
        raise SoftException((b'DailyQuestDecorationMap already has keys: {}').format(commonKeys))
    DailyQuestDecorationMap.update(WTDailyQuestDecorationMap)
    return
