import typing
from gui.battle_pass.battle_pass_constants import ChapterState
from gui.game_control.wallet import WalletController
from gui.shared.money import Currency
from helpers import dependency
from skeletons.gui.game_control import IBattlePassController
from skeletons.gui.shared.utils.requesters import IStatsRequester
if typing.TYPE_CHECKING:
    from typing import Dict
_BATTLE_PASS_CHAPTER_STATE_NAME = {(ChapterState.NOT_STARTED): b'not_started', 
   (ChapterState.PAUSED): b'paused', 
   (ChapterState.ACTIVE): b'active', 
   (ChapterState.COMPLETED): b'completed'}

def formatBalance(stats):
    actualMoney = stats.actualMoney.toDict()
    balanceData = {Currency.currencyExternalName(currency): actualMoney.get(currency, 0) for currency in Currency.ALL}
    balanceData.update(stats.dynamicCurrencies)
    balanceData[b'free_xp'] = stats.freeXP
    return balanceData


def formatWalletCurrencyStatuses(stats):
    statuses = {Currency.currencyExternalName(currencyCode): WalletController.STATUS.getKeyByValue(statusCode).lower() for currencyCode, statusCode in stats.currencyStatuses.iteritems() if currencyCode in Currency.ALL}
    statuses.update({currencyCode: WalletController.STATUS.getKeyByValue(statusCode).lower() for currencyCode, statusCode in stats.dynamicCurrencyStatuses.iteritems()})
    return statuses


@dependency.replace_none_kwargs(battlePass=IBattlePassController)
def formatBattlePassInfo(battlePass=None):
    return {b'isActive': (not battlePass.isPaused() and battlePass.isVisible()), 
       b'season': {b'num': (battlePass.getSeasonNum()), 
                   b'leftTime': (battlePass.getFinalOfferTime())}, 
       b'chapters': {chapterID: {b'isBought': (battlePass.isBought(chapterID=chapterID)), b'state': (_BATTLE_PASS_CHAPTER_STATE_NAME[battlePass.getChapterState(chapterID)])} for chapterID in battlePass.getMainChapterIDs()}}
