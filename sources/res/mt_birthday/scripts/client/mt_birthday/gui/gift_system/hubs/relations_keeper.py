import typing
from helpers.time_utils import getTimestampFromISO
from collections import OrderedDict
from gui.gift_system.constants import MAX_CACHED_PLAYERS
from gui.gift_system.hubs.base.relations_keeper import GiftEventBaseKeeper
from gui.gift_system.hubs.base.relations_keeper import IGiftEventKeeper
from gui.gift_system.wrappers import ifMessagesEnabled
from gui.impl.gen import R
if typing.TYPE_CHECKING:
    from typing import List, Optional
WE_SENT_INDEX = 0

class IGiftEventBirthdayKeeper(IGiftEventKeeper):

    def getMagicPercent(self):
        raise NotImplementedError
        return

    def getAllowMultipleSendCount(self):
        raise NotImplementedError
        return

    def getExpireTime(self):
        raise NotImplementedError
        return

    def updateExpireTime(self):
        raise NotImplementedError
        return

    def getExpireDelta(self):
        raise NotImplementedError
        return

    def getPlayersWaitingResponse(self):
        raise NotImplementedError
        return

    def getWaitResponseLimit(self):
        raise NotImplementedError
        return

    def getLastPlayerUpdatedAt(self):
        raise NotImplementedError
        return

    def isAlreadyReceivedGift(self, playerID):
        raise NotImplementedError
        return

    def updateSentGiftState(self, playerID):
        raise NotImplementedError
        return


class WaitingResponsePlayers(object):

    def __init__(self):
        self.__playersWaitingResponse = OrderedDict()
        return

    def clear(self):
        self.__playersWaitingResponse.clear()
        return

    def updateNewSender(self, player):
        if len(self.__playersWaitingResponse) == MAX_CACHED_PLAYERS:
            self.__playersWaitingResponse.popitem()
        newDict = OrderedDict([(player, None)])
        for playerID in self.__playersWaitingResponse:
            newDict[playerID] = None

        self.__playersWaitingResponse = newDict
        return

    def updatePreviousSender(self, player):
        if len(self.__playersWaitingResponse) != MAX_CACHED_PLAYERS:
            self.__playersWaitingResponse[player] = None
        return

    def delFromPlayersWaitingResponse(self, receiverID):
        if receiverID in self.__playersWaitingResponse:
            self.__playersWaitingResponse.pop(receiverID)
        return

    def getPlayersWaitingResponse(self):
        return self.__playersWaitingResponse


class GiftEventBirthdayKeeper(GiftEventBaseKeeper, IGiftEventBirthdayKeeper):
    __slots__ = (b'__magicPercent', b'__allowMultipleSendCount', b'__state', b'__expireTime', b'__expireDelta')

    def __init__(self, *args, **kwargs):
        self.__magicPercent = 0
        self.__allowMultipleSendCount = None
        self.__state = dict()
        self.__expireTime = 0
        self.__expireDelta = 0
        self.__waitResponseLimit = 0
        self.__playersWaitingResponse = WaitingResponsePlayers()
        self.__lastPlayerUpdatedAt = None
        super(GiftEventBirthdayKeeper, self).__init__(*args, **kwargs)
        return

    def getMagicPercent(self):
        return self.__magicPercent

    def getAllowMultipleSendCount(self):
        return self.__allowMultipleSendCount

    def getPlayersWaitingResponse(self):
        return self.__playersWaitingResponse.getPlayersWaitingResponse()

    def getWaitResponseLimit(self):
        return self.__waitResponseLimit

    def getLastPlayerUpdatedAt(self):
        return self.__lastPlayerUpdatedAt

    def getExpireTime(self):
        return self.__expireTime

    def updateExpireTime(self):
        self.__expireTime += self.__expireDelta
        self.__state = dict()
        return

    def getExpireDelta(self):
        return self.__expireDelta

    def __processState(self, state):
        for i in range(0, len(state), 3):
            spaID, weSend, weHaveBeenSent = state[i:i + 3]
            self.__state.update({spaID: [weSend, weHaveBeenSent]})

        return

    def isAlreadyReceivedGift(self, playerID):
        return bool(self.__state.get(playerID, [0, 0])[WE_SENT_INDEX])

    def updateSentGiftState(self, playerID):
        if playerID in self.__state:
            self.__state[playerID][WE_SENT_INDEX] += 1
        else:
            self.__state.update({playerID: [1, 0]})
        return

    def delFromPlayersWaitingResponse(self, receiverID):
        self.__playersWaitingResponse.delFromPlayersWaitingResponse(receiverID)
        return

    def destroy(self):
        self.__magicPercent = None
        self.__allowMultipleSendCount = None
        self.__waitResponseLimit = None
        self.__playersWaitingResponse.clear()
        self.__playersWaitingResponse = None
        self.__lastPlayerUpdatedAt = None
        self.__state = None
        super(GiftEventBirthdayKeeper, self).destroy()
        return

    @ifMessagesEnabled
    def processWebState(self, webState):
        self.__magicPercent = webState.common.get(b'magic_percent', 0)
        self.__allowMultipleSendCount = webState.common.get(b'allow_multiple_send_count', 0)
        self.__waitResponseLimit = webState.common.get(b'get_wait_response_limit', 0)
        self.__processState(webState.state)
        self.__expireTime = webState.expireTime
        self.__expireDelta = webState.expireDelta
        super(GiftEventBirthdayKeeper, self).processWebState(webState)
        return

    def processWaitResponse(self, incomeData):
        lastPlayerUpdatedAt = getTimestampFromISO(incomeData.lastPlayerUpdatedAt) if incomeData.lastPlayerUpdatedAt else 0
        currentLastPlayerUpdatedAt = self.__lastPlayerUpdatedAt
        self.__lastPlayerUpdatedAt = max(lastPlayerUpdatedAt, currentLastPlayerUpdatedAt)
        updateFunction = self.__playersWaitingResponse.updatePreviousSender
        players = incomeData.players
        if currentLastPlayerUpdatedAt is not None and lastPlayerUpdatedAt > currentLastPlayerUpdatedAt:
            updateFunction = self.__playersWaitingResponse.updateNewSender
            players.reverse()
        for player in players:
            if player not in self.__playersWaitingResponse.getPlayersWaitingResponse():
                updateFunction(player)

        return

    @staticmethod
    def getPhraseByID(phraseID):
        return R.strings.player_phrases.player.num(str(phraseID))
