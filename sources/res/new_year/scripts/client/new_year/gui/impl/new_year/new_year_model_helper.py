import typing
from new_year_common.items.components.ny_constants import CurrentNYConstants, TOKEN_LOOTBOX_FRAGMENT
from new_year.gui.impl.new_year.new_year_bonus_packer import packBonusModelAndTooltipData, getNewYearBonusPacker
from new_year.gui.impl.new_year.new_year_helper import nyWeeklyLeaderboardGFSortOrder
from constants import DOSSIER_TYPE
from gui.server_events.bonuses import getNonQuestBonuses
if typing.TYPE_CHECKING:
    from new_year.gui.impl.gen.view_models.views.lobby.new_year.views.leaderboard.ny_leaderboard_reward_model import NyLeaderboardRewardModel
_BONUS_SWAP = {b'dogTagComponents': b'nyStaticDogTag'}

def packNyLeaderboardRewards(rewards, model, tooltips, ctx=None, preserveBadgeDuplicates=False):
    if not rewards:
        return
    else:
        model.clearItems()
        playerBadges = rewards.pop(b'playerBadges', None) if preserveBadgeDuplicates else None
        _preprocessRewards(rewards)
        updaterKeys, updater = ctx if ctx else (tuple(), (lambda : 0))
        bonusContext = {}
        topEndPos = updater()
        if CurrentNYConstants.NY_STATIC_DOGTAG in updaterKeys:
            bonusContext[CurrentNYConstants.NY_STATIC_DOGTAG] = {b'topEndPos': topEndPos}
        if TOKEN_LOOTBOX_FRAGMENT in updaterKeys:
            bonusContext[TOKEN_LOOTBOX_FRAGMENT] = {b'topEndPos': topEndPos}
        bonuses = []
        if playerBadges:
            bonuses.extend(_collectPlayerBadgeBonuses(playerBadges))
        for key, value in rewards.iteritems():
            ctx = bonusContext.get(key)
            bonuses.extend(getNonQuestBonuses(key, value, ctx=ctx))

        bonuses.sort(key=nyWeeklyLeaderboardGFSortOrder)
        packBonusModelAndTooltipData(bonuses, model, getNewYearBonusPacker(), tooltips)
        return


def _preprocessRewards(rewards):
    _preprocessStyle(rewards)
    for key, val in _BONUS_SWAP.iteritems():
        if key in rewards:
            rewards[val] = rewards.pop(key)

    remapBadges = {}
    for key, val in rewards.iteritems():
        if key == b'playerBadges':
            for badgeRecord in val:
                remapBadges[(b'playerBadges', badgeRecord.get(b'id'))] = {b'unique': (badgeRecord.get(b'unique')), 
                   b'value': (badgeRecord.get(b'count'))}

    dossier = rewards.setdefault(b'dossier', {})
    accountDossier = dossier.setdefault(DOSSIER_TYPE.ACCOUNT, {})
    accountDossier.update(remapBadges)
    _remapStrKeysToInt(b'vehicles', rewards)
    return


def _preprocessStyle(rewards):
    customizations = rewards.get(b'customizations', [])
    if customizations:
        rewards[b'customizations'] = [cData for cData in customizations if not cData.get(b'boundToCurrentVehicle', False)]
        if not rewards[b'customizations']:
            rewards.pop(b'customizations')
    return


def _collectPlayerBadgeBonuses(playerBadges):
    bonuses = []
    for badgeRecord in playerBadges:
        badgeId = badgeRecord.get(b'id')
        if badgeId is None:
            continue
        rewards = {b'playerBadges': [badgeRecord]}
        _preprocessRewards(rewards)
        bonuses.extend(getNonQuestBonuses(b'dossier', rewards.get(b'dossier', {})))

    return bonuses


def _remapStrKeysToInt(rewardKey, rewards):
    rewards = rewards.get(rewardKey)
    if not isinstance(rewards, dict):
        return
    for key in rewards.keys():
        if not isinstance(key, int):
            value = rewards.pop(key)
            rewards[int(key)] = value

    return
