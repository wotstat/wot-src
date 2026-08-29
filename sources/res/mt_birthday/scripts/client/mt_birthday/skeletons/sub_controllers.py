import typing
if typing.TYPE_CHECKING:
    from typing import List, Optional, Tuple, Dict, Any
    from gui.server_events.event_items import Quest

class ITanksBirthdayProgressionSubController(object):

    def start(self):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def parseQuests(self):
        raise NotImplementedError
        return

    @property
    def progressionConfig(self):
        raise NotImplementedError
        return

    def __parseEventData(self, eventData):
        raise NotImplementedError
        return

    @staticmethod
    def isBirthdayProgressionQuest(qID):
        raise NotImplementedError
        return

    @staticmethod
    def getProgressionPointsRequiredFromQuest(questData):
        raise NotImplementedError
        return

    def __onEventsDataUpdated(self, diff):
        raise NotImplementedError
        return

    def __onTokensUpdate(self, diff):
        raise NotImplementedError
        return

    def getProgressionTokensCount(self):
        raise NotImplementedError
        return

    def isInfinityLevel(self):
        raise NotImplementedError
        return

    def getCurrentProgressionLevel(self):
        raise NotImplementedError
        return

    def getLevelByPoints(self, points):
        raise NotImplementedError
        return

    def getInfinityLevel(self):
        raise NotImplementedError
        return

    def getSimpleLevels(self):
        raise NotImplementedError
        return


class IGiftSystemSubController(object):

    def start(self):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def isGiftEventActive(self):
        raise NotImplementedError
        return

    def getStampCount(self, stampName):
        raise NotImplementedError
        return

    def getSimpleStampCount(self):
        raise NotImplementedError
        return

    def getSpecialStampCount(self):
        raise NotImplementedError
        return

    def getExpirationTime(self):
        raise NotImplementedError
        return

    def getMagicPercent(self):
        raise NotImplementedError
        return

    def getAllowMultipleSendCount(self):
        raise NotImplementedError
        return

    def getLimitResetTime(self):
        raise NotImplementedError
        return

    def isAlreadyReceivedGift(self, playerID):
        raise NotImplementedError
        return

    def getKeeper(self):
        raise NotImplementedError
        return

    def getGifter(self):
        raise NotImplementedError
        return

    def getStamper(self):
        raise NotImplementedError
        return

    def getMessenger(self):
        raise NotImplementedError
        return

    def sendGifts(self, stampType, receiversIDs, messageIdx, callback=None):
        raise NotImplementedError
        return
