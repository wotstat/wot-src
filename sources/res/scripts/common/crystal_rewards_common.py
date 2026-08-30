from __future__ import absolute_import
from constants import ARENA_BONUS_TYPE_NAMES
from soft_exception import SoftException

def readCrystalRewards(section, logId=b''):
    results = {}
    for bonusTypeName, rewards in section.items():
        bonus_type = ARENA_BONUS_TYPE_NAMES.get(bonusTypeName)
        if not bonus_type:
            raise SoftException(b'%s %s: %s' % (section.name, logId, b'Unknown ARENA_BONUS_TYPE <%s>' % bonusTypeName))
        winner_rewards = rewards.readString(b'winner').strip()
        if not winner_rewards:
            raise SoftException(b'%s %s: %s' % (section.name, logId, b'not found <winner>'))
        loser_rewards = rewards.readString(b'loser').strip()
        if not loser_rewards:
            raise SoftException(b'%s %s: %s' % (section.name, logId, b'not found <loser>'))
        comparator = rewards.readString(b'comparator', b'fareTeamXPPosition')
        results[bonus_type] = {True: {i + 1: int(reward) for i, reward in enumerate(winner_rewards.split(b' '))}, False: {i + 1: int(reward) for i, reward in enumerate(loser_rewards.split(b' '))}, b'comparator': comparator}

    return results
