from __future__ import absolute_import
from battle_results.battle_results_constants import BATTLE_RESULT_ENTRY_TYPE as ENTRY_TYPE
from constants import PlayerSatisfactionRating as Rating
BATTLE_RESULTS = [
 (
  b'avatarPlayerSatisfactionRating', tuple, (int(Rating.NONE), 0.0), None, b'skip', ENTRY_TYPE.ACCOUNT_SELF)]
