from __future__ import absolute_import
import typing
from functools import partial
import AccountCommands
from challenges_common import CHALLENGES_PDATA_KEY
from shared_utils.account_helpers.diff_utils import synchronizeDicts
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, Optional

def _getProxy(callback):
    if callback is not None:
        return (lambda requestID, resultID, errorStr, ext={}: callback(resultID, errorStr, ext))
    else:
        return


class Challenges(object):

    def __init__(self, syncData, commandsProxy):
        self.__cache = {}
        self.__ignore = True
        self.__syncData = syncData
        self.__commandsProxy = commandsProxy
        return

    def onAccountBecomePlayer(self):
        self.__ignore = False
        return

    def onAccountBecomeNonPlayer(self):
        self.__ignore = True
        return

    def getCache(self, callback=None):
        if self.__ignore:
            if callback is not None:
                callback(AccountCommands.RES_NON_PLAYER, None)
            return
        self.__syncData.waitForSync(partial(self.__onGetCacheResponse, callback))
        return

    def synchronize(self, isFullSync, diff):
        if isFullSync and self.__cache:
            self.__cache.clear()
        if CHALLENGES_PDATA_KEY in diff:
            synchronizeDicts(diff[CHALLENGES_PDATA_KEY], self.__cache.setdefault(CHALLENGES_PDATA_KEY, {}))
        return

    def activateChallenge(self, challengeId, callback=None):
        self.__commandsProxy.perform(AccountCommands.CMD_CHALLENGE_ACTIVATE, challengeId, _getProxy(callback))
        return

    def restartChallenge(self, challengeId, isFree, callback=None):
        self.__commandsProxy.perform(AccountCommands.CMD_CHALLENGE_RESTART, challengeId, isFree, _getProxy(callback))
        return

    def surrenderChallenge(self, challengeId, callback=None):
        self.__commandsProxy.perform(AccountCommands.CMD_CHALLENGE_SURRENDER, challengeId, _getProxy(callback))
        return

    def completeActiveQuest(self, callback=None):
        self.__commandsProxy.perform(AccountCommands.CMD_COMPLETE_ACTIVE_CHALLENGE_QUEST, _getProxy(callback))
        return

    def completeActiveChallenge(self, callback=None):
        self.__commandsProxy.perform(AccountCommands.CMD_COMPLETE_ACTIVE_CHALLENGE, _getProxy(callback))
        return

    def failActiveQuest(self, callback=None):
        self.__commandsProxy.perform(AccountCommands.CMD_FAIL_ACTIVE_CHALLENGE_QUEST, _getProxy(callback))
        return

    def setActiveChallengeAttempts(self, amount, callback=None):
        self.__commandsProxy.perform(AccountCommands.CMD_SET_ACTIVE_CHALLENGE_ATTEMPTS, amount, _getProxy(callback))
        return

    def setChallengeCompletions(self, challengeID, amount, callback=None):
        self.__commandsProxy.perform(AccountCommands.CMD_SET_CHALLENGE_COMPLETIONS, challengeID, amount, _getProxy(callback))
        return

    def setChallengeRestartsUsed(self, challengeID, amount, callback=None):
        self.__commandsProxy.perform(AccountCommands.CMD_SET_CHALLENGE_RESTARTS_USED, challengeID, amount, _getProxy(callback))
        return

    def resetChallengeProgress(self, challengeID, callback=None):
        self.__commandsProxy.perform(AccountCommands.CMD_RESET_CHALLENGE_PROGRESS, challengeID, _getProxy(callback))
        return

    def __onGetCacheResponse(self, callback, resultID):
        if resultID < 0:
            if callback is not None:
                callback(resultID, None)
            return
        if callback is not None:
            callback(resultID, self.__cache)
        return
