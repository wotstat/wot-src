from __future__ import absolute_import
from wg_async import wg_async, wg_await
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.view.lobby.missions import missions_helper
from gui.Scaleform.daapi.view.lobby.user_missions.missions_group_packers import getGroupPackerByContextID
from gui.Scaleform.daapi.view.meta.MissionDetailsContainerViewMeta import MissionDetailsContainerViewMeta
from gui.Scaleform.genConsts.QUESTS_ALIASES import QUESTS_ALIASES
from gui.server_events.events_helpers import isDailyQuest, isPremium
from gui.server_events.formatters import parseComplexToken
from gui.server_events.events_constants import BATTLE_ROYALE_GROUPS_ID
from gui.shared import events, EVENT_BUS_SCOPE
from helpers import dependency
from skeletons.gui.server_events import IEventsCache
from skeletons.gui.game_control import IBattleRoyaleController

class MissionDetailsContainerView(LobbySubView, MissionDetailsContainerViewMeta):
    eventsCache = dependency.descriptor(IEventsCache)
    __battleRoyaleController = dependency.descriptor(IBattleRoyaleController)
    __showDQInMissionsTab = False

    def __init__(self, ctx=None):
        super(MissionDetailsContainerView, self).__init__(ctx)
        self.__ctx = ctx
        self.__groupPacker = None
        self.__quests = {}
        return

    def closeView(self):
        self.destroy()
        return

    def requestMissionData(self, index):
        missionData = self.__datailedList[index]
        self.as_setMissionDataS(missionData)
        self.onChangePage(missionData[b'eventID'])
        return

    def onTokenBuyClick(self, tokenId, questId):
        self.fireEvent(events.OpenLinkEvent(events.OpenLinkEvent.TOKEN_SHOP, params={b'name': (parseComplexToken(tokenId).webID)}))
        return

    def onChangePage(self, eventID):
        vehicleSelector = self.getComponent(QUESTS_ALIASES.MISSIONS_VEHICLE_SELECTOR_ALIAS)
        if vehicleSelector is None:
            return
        else:
            quest = self.__quests.get(eventID)
            detailedData = missions_helper.getDetailedMissionData(quest)
            criteria, extraConditions, isForBattleRoyale = detailedData.getVehicleRequirementsCriteria()
            vehicleSelector.as_closeS()
            if criteria and not quest.isCompleted():
                vehicleSelector.setCriteria(criteria, extraConditions, isForBattleRoyale)
            else:
                vehicleSelector.as_hideSelectedVehicleS()
            return

    @classmethod
    def setShowDQInMissionsTab(cls, value):
        cls.__showDQInMissionsTab = value
        return

    def _populate(self):
        super(MissionDetailsContainerView, self)._populate()
        self.addListener(events.HideWindowEvent.HIDE_MISSION_DETAILS_VIEW, self.__handleDetailsClose, EVENT_BUS_SCOPE.LOBBY)
        self.eventsCache.onSyncCompleted += self.__setData
        self.eventsCache.onPMSyncCompleted += self.__setData
        self.__setData(needDemand=True)
        return

    def _invalidate(self, ctx=None):
        self.__ctx = ctx
        self.__setData(needDemand=False)
        return

    def _dispose(self):
        self.removeListener(events.HideWindowEvent.HIDE_MISSION_DETAILS_VIEW, self.__handleDetailsClose, EVENT_BUS_SCOPE.LOBBY)
        self.eventsCache.onPMSyncCompleted -= self.__setData
        self.eventsCache.onSyncCompleted -= self.__setData
        self.__quests = None
        if self.__groupPacker is not None:
            self.__groupPacker.clear()
            self.__groupPacker = None
        super(MissionDetailsContainerView, self)._dispose()
        return

    @wg_async
    def __setData(self, needDemand=True, *_):
        if needDemand:
            yield wg_await(self.eventsCache.prefetcher.demand())
        eventID = self.__ctx.get(b'eventID')
        groupID = self.__ctx.get(b'groupID')
        if self.__groupPacker is not None:
            self.__groupPacker.clear()
        self.__groupPacker = getGroupPackerByContextID(groupID, self.eventsCache)
        self.__datailedList = []
        self.__quests = self.__getQuests(groupID)
        if self.__groupPacker is not None:
            for quest in self.__groupPacker.findEvents(self.__quests):
                data = missions_helper.getDetailedMissionData(quest).getInfo()
                self.__datailedList.append(data)

        else:
            quest = self.__quests.get(eventID)
            if quest is not None:
                self.__datailedList.append(missions_helper.getDetailedMissionData(quest).getInfo())
        if not self.__datailedList or self.__isQuestInvalid(eventID):
            self.closeView()
        else:
            pages = [{b'buttonsGroup': b'MissionDetailsPageGroup', b'pageIndex': i, b'label': (b'%i' % (i + 1)), b'tooltip': (mission.get(b'statusTooltipData')), b'status': (mission.get(b'status')), b'selected': (eventID == mission.get(b'eventID'))} for i, mission in enumerate(self.__datailedList)]
            self.as_setInitDataS({b'pages': pages})
        return

    def __handleDetailsClose(self, _):
        self.destroy()
        return

    def __getQuests(self, groupID):

        def missionsFilter(q):
            checkDaily = True if self.__showDQInMissionsTab else not isDailyQuest(q.getID()) and not isPremium(q.getID())
            return checkDaily and q.getFinishTimeLeft()

        if groupID == BATTLE_ROYALE_GROUPS_ID:
            return self.__battleRoyaleController.getQuests()
        return self.eventsCache.getQuests(missionsFilter)

    def __isQuestInvalid(self, eventID):
        return eventID not in self.__quests
