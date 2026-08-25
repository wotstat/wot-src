from gui.battle_results.components import base
from gui.battle_results.templates.cybersport import CYBER_SPORT_BLOCK
from gui.battle_results.templates.fortification import STRONGHOLD_BATTLE_COMMON_STATS_BLOCK
from gui.battle_results.templates.fortification import STRONGHOLD_PERSONAL_STATS_BLOCK
from gui.battle_results.templates.fortification import STRONGHOLD_TEAMS_STATS_BLOCK
from gui.battle_results.templates.regular import MULTI_TEAM_TABS_BLOCK
from gui.battle_results.templates.regular import PROGRESSIVE_REWARD_VO
from gui.battle_results.templates.regular import PRESTIGE_PROGRESS_VO
from gui.battle_results.templates.regular import REGULAR_TABS_BLOCK
from gui.battle_results.templates.regular import VEHICLE_PROGRESS_STATS_BLOCK
from gui.battle_results.templates.regular import BATTLE_PASS_PROGRESS_STATS_BLOCK
from gui.battle_results.templates.regular import QUESTS_PROGRESS_STATS_BLOCK
from gui.battle_results.templates.regular import DOG_TAGS_PROGRESS_STATS_BLOCK
from gui.battle_results.templates.regular import REGULAR_COMMON_STATS_BLOCK
from gui.battle_results.templates.regular import REGULAR_PERSONAL_STATS_BLOCK
from gui.battle_results.templates.regular import REGULAR_TEAMS_STATS_BLOCK
from gui.battle_results.templates.regular import REGULAR_TEXT_STATS_BLOCK
from gui.battle_results.templates.regular import CLAN_TEXT_STATS_BLOCK
from gui.battle_results.templates.regular import COMMENDATIONS_RECEIVED_VO
from gui.battle_results.templates.ranked_battles import RANKED_COMMON_STATS_BLOCK
from gui.battle_results.templates.ranked_battles import RANKED_TEAMS_STATS_BLOCK
from gui.battle_results.templates.ranked_battles import RANKED_RESULTS_BLOCK
from gui.battle_results.templates.ranked_battles import RANKED_PERSONAL_STATS_BLOCK
from gui.battle_results.templates.ranked_battles import RANKED_RESULTS_STATUS_BLOCK
from gui.battle_results.templates.ranked_battles import RANKED_RESULTS_TEAMS_STATS_BLOCK
from gui.battle_results.templates.ranked_battles import RANKED_ENABLE_ANIMATION_BLOCK
from gui.battle_results.templates.ranked_battles import RANKED_SHOW_WIDGET_BLOCK
from gui.battle_results.templates.ranked_battles import RANKED_RESULTS_STATE_BLOCK
from gui.battle_results.templates.epic import EPIC_TABS_BLOCK
from gui.battle_results.templates.epic import EPIC_COMMON_STATS_BLOCK
from gui.battle_results.templates.epic import EPIC_PERSONAL_STATS_BLOCK
from gui.battle_results.templates.epic import EPIC_TEAMS_STATS_BLOCK
from gui.battle_results.templates.maps_training import MAPS_TRAINING_RESULTS_BLOCK
from gui.impl import backport
from gui.impl.gen import R
__all__ = (b'TOTAL_VO_META', b'MULTI_TEAM_TABS_BLOCK', b'REGULAR_TABS_BLOCK', b'VEHICLE_PROGRESS_STATS_BLOCK', b'BATTLE_PASS_PROGRESS_STATS_BLOCK', b'QUESTS_PROGRESS_STATS_BLOCK', b'DOG_TAGS_PROGRESS_STATS_BLOCK', b'REGULAR_COMMON_STATS_BLOCK', b'REGULAR_PERSONAL_STATS_BLOCK', b'REGULAR_TEAMS_STATS_BLOCK', b'REGULAR_TEXT_STATS_BLOCK', b'CLAN_TEXT_STATS_BLOCK', b'STRONGHOLD_BATTLE_COMMON_STATS_BLOCK', b'STRONGHOLD_PERSONAL_STATS_BLOCK', b'STRONGHOLD_TEAMS_STATS_BLOCK', b'CYBER_SPORT_BLOCK', b'RANKED_COMMON_STATS_BLOCK', b'RANKED_TEAMS_STATS_BLOCK', b'RANKED_RESULTS_BLOCK', b'RANKED_PERSONAL_STATS_BLOCK', b'RANKED_RESULTS_STATUS_BLOCK', b'RANKED_ENABLE_ANIMATION_BLOCK', b'EPIC_COMMON_STATS_BLOCK', b'EPIC_TABS_BLOCK', b'EPIC_PERSONAL_STATS_BLOCK', b'EPIC_TEAMS_STATS_BLOCK', b'RANKED_SHOW_WIDGET_BLOCK', b'PROGRESSIVE_REWARD_VO', b'RANKED_RESULTS_STATE_BLOCK', b'MAPS_TRAINING_RESULTS_BLOCK')
TOTAL_VO_META = base.DictMeta({b'personal': {}, b'common': {}, b'team1': [], b'team2': [], b'textData': {}, b'battlePass': None, 
   b'quests': None, 
   b'unlocks': [], b'tabInfo': [], b'cyberSport': None, 
   b'isFreeForAll': False, 
   b'closingTeamMemberStatsEnabled': True, 
   b'selectedTeamMemberId': (-1), 
   b'receivedCommendations': (-1), 
   b'progressiveReward': None, 
   b'dog_tags': {}, b'prestige': None, 
   b'efficiencyTitle': (backport.text(R.strings.battle_results.common.battleEfficiencyWithoutOreders.title()))})
