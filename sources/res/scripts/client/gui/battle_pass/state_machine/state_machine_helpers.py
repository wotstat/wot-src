import logging, typing
from battle_pass_common import BATTLE_PASS_OFFER_TOKEN_PREFIX, BATTLE_PASS_TOKEN_3D_STYLE, BattlePassConsts, BattlePassRewardReason, BattlePassState, getBattlePassPassEntitlementName, BATTLE_PASS_SHOP_ENTITLEMENT_PASS
from gui.battle_pass.battle_pass_helpers import getOfferTokenByGift, getStyleInfoForChapter
from gui.impl.gen import R
from gui.impl.pub.notification_commands import EventNotificationCommand, NotificationEvent
from gui.server_events.events_dispatcher import showMissionsBattlePass
from helpers import dependency
from items.vehicles import makeVehicleTypeCompDescrByName
from skeletons.gui.game_control import IBattlePassController
from skeletons.gui.offers import IOffersDataProvider
from skeletons.gui.lobby_context import ILobbyContext
if typing.TYPE_CHECKING:
    from account_helpers.offers.events_data import OfferEventData
    from typing import Any, Callable, Dict, List, Optional
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def isProgressionComplete(_, battlePass=None):
    isCompleteState = battlePass.getState() == BattlePassState.COMPLETED
    isAllChosen = battlePass.getNotChosenRewardCount() == 0
    isAllChaptersBought = all(battlePass.isBought(chapterID=chapter) for chapter, _ in enumerate(battlePass.getChapterConfig(), BattlePassConsts.MINIMAL_CHAPTER_NUMBER))
    isResoureCompleted = battlePass.isResourceCompleted()
    return isCompleteState and isAllChosen and isAllChaptersBought and isResoureCompleted


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def getChapterForStyleId(style, battlePass=None):
    config = battlePass.getStylesConfig()
    for chapterId, styleId in config.iteritems():
        if styleId == style:
            return chapterId

    return


@dependency.replace_none_kwargs(lobbyContext=ILobbyContext)
def getChapterForVehicleCD(vehicleCD, lobbyContext=None):
    config = lobbyContext.getServerSettings().getBattlePassConfig()
    for chapterId, chapterInfo in config.chapters.iteritems():
        vehicleName = chapterInfo.get(b'vehicle')
        if vehicleName:
            rewardVehicleCD = makeVehicleTypeCompDescrByName(vehicleName)
            if vehicleCD == rewardVehicleCD:
                return chapterId

    return


def separateRewards(rewards):
    styleTokens = []
    chosenStyleChapterID = None
    chosenVehicleChapterID = None
    defaultRewards = rewards[:]
    blocksToRemove = []
    for index, rewardBlock in enumerate(defaultRewards):
        if b'tokens' in rewardBlock:
            for tokenID in rewardBlock[b'tokens'].iterkeys():
                if tokenID.startswith(BATTLE_PASS_TOKEN_3D_STYLE):
                    styleTokens.append(tokenID)
                    chapter = int(tokenID.split(b':')[3])
                    intCD, _ = getStyleInfoForChapter(chapter)
                    if intCD is not None:
                        chosenStyleChapterID = chapter

        for tokenID in styleTokens:
            rewardBlock.get(b'tokens', {}).pop(tokenID, None)

        if not rewardBlock.get(b'tokens', {}):
            rewardBlock.pop(b'tokens', None)
        if b'customizations' in rewardBlock:
            for custItem in rewardBlock[b'customizations']:
                if custItem[b'custType'] == b'style':
                    chapterId = getChapterForStyleId(custItem[b'id'])
                    if chapterId is not None:
                        chosenStyleChapterID = chapterId

        if b'vehicles' in rewardBlock:
            for vehicleItem in rewardBlock[b'vehicles']:
                for vehicleCD in vehicleItem:
                    chapterId = getChapterForVehicleCD(vehicleCD)
                    if chapterId is not None:
                        chosenVehicleChapterID = chapterId

        if not rewardBlock:
            blocksToRemove.append(index)
        styleTokens = []

    for index in sorted(blocksToRemove, reverse=True):
        defaultRewards.pop(index)

    return (defaultRewards, chosenStyleChapterID, chosenVehicleChapterID)


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def packStartEvent(rewards, data, packageRewards, eventMethod, battlePass=None):
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
        isFinalLevel = battlePass.isFinalLevel(chapter, newLevel)
        isRareLevel = False
        if newLevel is not None:
            for level in xrange(prevLevel + 1, newLevel + 1):
                if battlePass.isRareLevel(chapter, level):
                    isRareLevel = True
                    break

        if b'entitlements' in rewards:
            rewards[b'entitlements'].pop(getBattlePassPassEntitlementName(battlePass.getSeasonID()), None)
            rewards[b'entitlements'].pop(BATTLE_PASS_SHOP_ENTITLEMENT_PASS, None)
            if not rewards[b'entitlements']:
                rewards.pop(b'entitlements')
        if not isPremiumPurchase and not isRareLevel and not isFinalLevel or not rewards:
            return
        return EventNotificationCommand(NotificationEvent(method=eventMethod, rewards=[rewards], data=data, packageRewards=packageRewards))


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def multipleBattlePassPurchasedEventMethod(rewards, data, packageRewards, battlePass=None):
    if battlePass.isDisabled():
        return
    else:
        chapterID = battlePass.getCurrentChapterID()
        showMissionsBattlePass(R.views.lobby.battle_pass.BattlePassProgressionsView() if chapterID else None, chapterID)
        battlePass.getRewardLogic().startRewardFlow(rewards, data, packageRewards)
        return


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def defaultEventMethod(rewards, data, packageRewards, battlePass=None):
    battlePass.getRewardLogic().startRewardFlow(rewards, data, packageRewards)
    return


def packToken(tokenID):
    return {b'tokens': {tokenID: {b'count': 1, b'expires': {b'after': 1}}}}


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
