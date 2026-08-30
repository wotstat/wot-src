from __future__ import absolute_import
import logging, typing
from future.builtins import range
from battle_pass_common import BATTLE_PASS_OFFER_TOKEN_PREFIX, BATTLE_PASS_TOKEN_3D_STYLE, BattlePassRewardReason, getBattlePassPassEntitlementName, getBattlePassShopEntitlementName, isPostProgressionChapter
from gui.battle_pass.battle_pass_helpers import getOfferTokenByGift, getStyleInfoForChapter, makeChapterMediaName
from gui.impl.gen import R
from gui.impl.pub.notification_commands import EventNotificationCommand, NotificationEvent
from gui.shared.event_dispatcher import showBattlePass
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController
from skeletons.gui.offers import IOffersDataProvider
if typing.TYPE_CHECKING:
    from account_helpers.offers.events_data import OfferEventData
    from typing import Any, Callable, Dict, List, Optional
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def isProgressionComplete(_, battlePass=None):
    if battlePass.getMainChapterIDs():
        isCompleted = all(battlePass.isChapterCompleted(chapter) for chapter in battlePass.getMainChapterIDs())
        isAllChosen = battlePass.getNotChosenRewardCount() == 0
        isAllChaptersBought = battlePass.isAllMainChaptersBought()
        return isCompleted and isAllChosen and isAllChaptersBought
    return False


def separateRewards(rewards):
    styleTokens = []
    chosenStyle = None
    defaultRewards = rewards[:]
    blocksToRemove = []
    for index, rewardBlock in enumerate(defaultRewards):
        if b'tokens' in rewardBlock:
            for tokenID in rewardBlock[b'tokens']:
                if tokenID.startswith(BATTLE_PASS_TOKEN_3D_STYLE):
                    styleTokens.append(tokenID)
                    chapter = int(tokenID.split(b':')[3])
                    intCD, _ = getStyleInfoForChapter(chapter)
                    if intCD is not None:
                        chosenStyle = chapter

        for tokenID in styleTokens:
            rewardBlock.get(b'tokens', {}).pop(tokenID, None)

        if not rewardBlock.get(b'tokens', {}):
            rewardBlock.pop(b'tokens', None)
        if not rewardBlock:
            blocksToRemove.append(index)
        styleTokens = []

    for index in sorted(blocksToRemove, reverse=True):
        defaultRewards.pop(index)

    return (defaultRewards, chosenStyle)


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def packStartEvent(rewards, data, packageRewards, starterPack, eventMethod, battlePass=None):
    if rewards is None or data is None:
        return
    reason = data[b'reason']
    if reason in (BattlePassRewardReason.STYLE_UPGRADE,):
        return
    else:
        if not (b'newLevel' in data and b'chapter' in data):
            return
        isPremiumPurchase = reason in BattlePassRewardReason.PURCHASE_REASONS
        newLevel = data[b'newLevel']
        chapter = data[b'chapter']
        prevLevel = data[b'prevLevel']
        if isPostProgressionChapter(chapter):
            return
        data.update({b'needVideo': (needToShowVideo(chapter, newLevel, battlePass=battlePass))})
        isFinalLevel = battlePass.isFinalLevel(chapter, newLevel)
        isRareLevel = False
        if newLevel is not None:
            for level in range(prevLevel + 1, newLevel + 1):
                if battlePass.isRareLevel(chapter, level):
                    isRareLevel = True
                    break

        if b'entitlements' in rewards:
            rewards[b'entitlements'].pop(getBattlePassPassEntitlementName(battlePass.getSeasonID()), None)
            rewards[b'entitlements'].pop(getBattlePassShopEntitlementName(battlePass.getSeasonID()), None)
            if not rewards[b'entitlements']:
                rewards.pop(b'entitlements')
        if not isPremiumPurchase and not isRareLevel and not isFinalLevel or not rewards:
            return
        return EventNotificationCommand(NotificationEvent(method=eventMethod, rewards=[
         rewards], data=data, packageRewards=packageRewards, starterPack=starterPack))


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def multipleBattlePassPurchasedEventMethod(rewards, data, packageRewards, starterPack, battlePass=None):
    if battlePass.isDisabled():
        return
    else:
        currentChapterID = battlePass.getCurrentChapterID()
        chapterID = currentChapterID if not isPostProgressionChapter(currentChapterID) else None
        showBattlePass(R.aliases.battle_pass.Progression() if chapterID else None, chapterID)
        battlePass.getRewardLogic().startRewardFlow(rewards, data, packageRewards, starterPack)
        return


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def defaultEventMethod(rewards, data, packageRewards, starterPack, battlePass=None):
    battlePass.getRewardLogic().startRewardFlow(rewards, data, packageRewards, starterPack)
    return


def packToken(tokenID):
    return {b'tokens': {tokenID: {b'count': 1, b'expires': {b'after': 1}}}}


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def needToShowVideo(chapterID, level, battlePass=None):
    return R.videos.battle_pass.dyn(makeChapterMediaName(chapterID)).exists() and battlePass.isFinalLevel(chapterID, level) and (battlePass.isExtraChapter(chapterID) or battlePass.isHoliday())


@dependency.replace_none_kwargs(offers=IOffersDataProvider)
def processRewardsToChoose(rewardsToChoose, offers=None):
    rewards = {}
    for token in rewardsToChoose:
        offer = _getOfferByGiftToken(token, offers=offers)
        if offer is not None:
            rewards[token] = not offer.availableTokens

    return rewards


@dependency.replace_none_kwargs(offers=IOffersDataProvider)
def _getOfferByGiftToken(token, offers=None):
    return offers.getOfferByToken(getOfferTokenByGift(token))


@dependency.replace_none_kwargs(offers=IOffersDataProvider)
def _isRewardChoiceToken(token, offers=None):
    return token.startswith(BATTLE_PASS_OFFER_TOKEN_PREFIX) and _getOfferByGiftToken(token, offers=offers) is not None
