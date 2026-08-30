from __future__ import absolute_import
import typing
if typing.TYPE_CHECKING:
    from typing import Optional, Dict, Callable, Union
    from Event import Event
    from gui.server_events.event_items import DailyEpicTokenQuest, Quest, DailyQuest, PremiumQuest, WeeklyQuest
    from gui.server_events.personal_missions_cache import PersonalMissionsCache

class IEventsCache(object):
    onSyncStarted = None
    onSyncCompleted = None
    onProgressUpdated = None
    onEventsVisited = None
    onProfileVisited = None
    onPersonalQuestsVisited = None
    onPMSyncCompleted = None

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def start(self):
        raise NotImplementedError
        return

    def stop(self, isDisconnected=False):
        raise NotImplementedError
        return

    def clear(self):
        raise NotImplementedError
        return

    @property
    def isStarted(self):
        raise NotImplementedError
        return

    @property
    def waitForSync(self):
        raise NotImplementedError
        return

    @property
    def prefetcher(self):
        raise NotImplementedError
        return

    @property
    def dailyQuests(self):
        raise NotImplementedError
        return

    @property
    def questsProgress(self):
        raise NotImplementedError
        return

    def getPersonalMissions(self):
        raise NotImplementedError
        return

    def getLockedQuestTypes(self, branch):
        raise NotImplementedError
        return

    def getLockedPersonalMissions(self):
        raise NotImplementedError
        return

    def update(self, diff=None, callback=None):
        raise NotImplementedError
        return

    def getQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getUngroupedBasicQuestByID(self, qID):
        raise NotImplementedError
        return

    def getMotiveQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getPremiumQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getDailyQuests(self, filterFunc=None, includeEpic=False):
        raise NotImplementedError
        return

    def getDailyEpicQuest(self):
        raise NotImplementedError
        return

    def getWeeklyQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getBattleQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getGroups(self, filterFunc=None):
        raise NotImplementedError
        return

    def getHiddenQuests(self, filterFunc=None, makeRelations=True):
        raise NotImplementedError
        return

    def getRankedQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getAllQuests(self, filterFunc=None, includePersonalMissions=False, makeRelations=True):
        raise NotImplementedError
        return

    def getActions(self, filterFunc=None):
        raise NotImplementedError
        return

    def getActionEntities(self):
        raise NotImplementedError
        return

    def getAnnouncedActions(self):
        raise NotImplementedError
        return

    def getEvents(self, filterFunc=None):
        raise NotImplementedError
        return

    def getAllEvents(self, filterFunc=None):
        raise NotImplementedError
        return

    def getCurrentEvents(self):
        raise NotImplementedError
        return

    def getFutureEvents(self):
        raise NotImplementedError
        return

    def getAffectedAction(self, item):
        raise NotImplementedError
        return

    def getItemAction(self, item, isBuying=True, forCredits=False):
        raise NotImplementedError
        return

    def getBoosterAction(self, booster, isBuying=True, forCredits=False):
        raise NotImplementedError
        return

    def getRentAction(self, item, rentPackage):
        raise NotImplementedError
        return

    def getEconomicsAction(self, name):
        raise NotImplementedError
        return

    def isBalancedSquadEnabled(self):
        raise NotImplementedError
        return

    def getBalancedSquadBounds(self, tag=b'default'):
        raise NotImplementedError
        return

    def isSquadXpFactorsEnabled(self):
        raise NotImplementedError
        return

    def getSquadBonusLevelDistance(self):
        raise NotImplementedError
        return

    def getSquadPenaltyLevelDistance(self):
        raise NotImplementedError
        return

    def getSquadZeroBonuses(self):
        raise NotImplementedError
        return

    def getSquadXPFactor(self):
        raise NotImplementedError
        return

    def getQuestsDossierBonuses(self):
        raise NotImplementedError
        return

    def getQuestsByTokenRequirement(self, token):
        raise NotImplementedError
        return

    def getQuestsByTokenBonus(self, token):
        raise NotImplementedError
        return

    def getCompensation(self, tokenID):
        raise NotImplementedError
        return

    def hasQuestDelayedRewards(self, questID):
        raise NotImplementedError
        return

    def getAdvisableQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getActiveQuests(self, filterFunc=None):
        raise NotImplementedError
        return

    def getProgressiveReward(self):
        raise NotImplementedError
        return

    def getLobbyHeaderTabCounter(self):
        raise NotImplementedError
        return
