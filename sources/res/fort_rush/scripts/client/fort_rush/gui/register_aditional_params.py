from __future__ import absolute_import

class FortRushConditionIcons(object):
    SCORE_POINTS = b'scorePoints'
    PROGRESSION_POINTS = b'progressionPoints'
    CAPTURES = b'captures'
    ZONE_DAMAGE_DEALT = b'zoneDamageDealt'
    RAMMING = b'ramming'


def registerConditionFormatterIcons():
    from personal_missions_constants import CONDITION_ICON
    from gui.server_events.cond_formatters import BATTLE_RESULTS_KEYS
    BATTLE_RESULTS_KEYS.update({b'fortRush/scorePoints': (FortRushConditionIcons.SCORE_POINTS), 
       b'fortRush/progressionPoints': (FortRushConditionIcons.SCORE_POINTS), 
       b'fortRush/captures': (FortRushConditionIcons.CAPTURES), 
       b'fortRush/neutralizes': (FortRushConditionIcons.CAPTURES), 
       b'fortRush/firstCaptures': (FortRushConditionIcons.CAPTURES), 
       b'fortRush/captorKills': (CONDITION_ICON.KILL_VEHICLES), 
       b'fortRush/zoneDamageDealt': (CONDITION_ICON.DAMAGE), 
       b'fortRush/LTNeutralizes': (FortRushConditionIcons.CAPTURES), 
       b'fortRush/HTDamage': (CONDITION_ICON.DAMAGE), 
       b'fortRush/ATSPGDamage': (CONDITION_ICON.DAMAGE), 
       b'fortRush/ramming': (FortRushConditionIcons.RAMMING), 
       b'fortRush/sameLife/captures': (FortRushConditionIcons.CAPTURES), 
       b'deathCount': (CONDITION_ICON.FOLDER)})
    return
