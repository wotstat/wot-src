from __future__ import absolute_import
import typing
from skeletons.gui.game_control import IGameController
if typing.TYPE_CHECKING:
    from typing import Optional, Iterator, List, Dict, Union
    from Event import Event
    from gui.challenges.challenge_item import ChallengeItem
    from challenges_common import ChallengesConfig

class IChallengesController(IGameController):
    onChallengesSettingsChanged = None
    onActiveChallengeChanged = None
    onChallengesClientUpdated = None

    @property
    def systemConfig(self):
        raise NotImplementedError
        return

    @property
    def isEnabled(self):
        raise NotImplementedError
        return

    @property
    def activeChallengeID(self):
        raise NotImplementedError
        return

    def getChallenge(self, challengeId):
        raise NotImplementedError
        return

    def iterChallenges(self):
        raise NotImplementedError
        return

    def availableChallenges(self):
        raise NotImplementedError
        return

    def isChallengeCompleted(self, challenge):
        raise NotImplementedError
        return

    def challengesAvailableForCompletions(self):
        raise NotImplementedError
        return

    def getSortedChallenges(self):
        raise NotImplementedError
        return

    def getNearestChallengeFinishTime(self, challenges):
        raise NotImplementedError
        return

    def getTimeToNearestChallengeEnd(self, challenges=None):
        raise NotImplementedError
        return

    def getTimeToUpdateAvailableChallenges(self):
        raise NotImplementedError
        return

    def getSoonEndingChallenges(self):
        raise NotImplementedError
        return

    def getChallengeProgress(self, challengeID):
        raise NotImplementedError
        return

    def isEnoughMoneyForRestart(self, challenge):
        raise NotImplementedError
        return

    def activateChallenge(self, challengeID):
        raise NotImplementedError
        return

    def restartChallenge(self, challengeID, isFree):
        raise NotImplementedError
        return

    def surrenderChallenge(self, challengeID):
        raise NotImplementedError
        return
