from account_helpers import AccountSettings
from account_helpers.AccountSettings import STATS_REGULAR_SORTING
from account_helpers.AccountSettings import STATS_SORTIE_SORTING
from account_helpers.AccountSettings import STATS_COMP7_SORTING
from soft_exception import SoftException
from constants import ARENA_BONUS_TYPE
__all__ = (b'STATS_REGULAR_SORTING', b'STATS_SORTIE_SORTING', b'STATS_COMP7_SORTING', b'writeStatsSorting', b'readStatsSorting')
AVAILABLE_STATS_SORTINGS = [
 STATS_REGULAR_SORTING,
 STATS_SORTIE_SORTING,
 STATS_COMP7_SORTING]

def writeStatsSorting(bonusType, iconType, sortDirection):
    key = STATS_REGULAR_SORTING
    if bonusType == ARENA_BONUS_TYPE.COMP7:
        key = STATS_COMP7_SORTING
    value = {b'iconType': iconType, 
       b'sortDirection': sortDirection}
    AccountSettings.setSettings(key, value)
    return


def readStatsSorting(key):
    if key not in AVAILABLE_STATS_SORTINGS:
        raise SoftException((b'Sorting key {} is invalid').format(key))
    settings = AccountSettings.getSettings(key)
    return (
     settings.get(b'iconType'), settings.get(b'sortDirection'))
