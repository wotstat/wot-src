from functools import partial
from collections import namedtuple
import BigWorld
from adisp import adisp_process
from gui.Scaleform.framework.managers.loaders import SFViewLoadParams
from gui.impl import backport
from helpers import dependency
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from helpers.i18n import makeString as _ms
from helpers.time_utils import ONE_MINUTE
from skeletons.connection_mgr import IConnectionManager
from skeletons.gui.event_boards_controllers import IEventBoardController
from skeletons.gui.shared import IItemsCache
from gui.shared.utils.functions import makeTooltip
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_maintenance import EventBoardsMaintenance
from gui.shared import events, g_eventBus, EVENT_BUS_SCOPE
from gui.shared.formatters import text_styles, icons
from gui.Scaleform.daapi import LobbySubView
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_award_group import EventBoardsAwardGroup
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_pagination import EventBoardsPagination
from gui.Scaleform.daapi.view.lobby.event_boards.event_boards_vos import makeTableViewHeaderVO, makeEventBoardsTableDataVO, makeEventBoardsTableViewStatusVO, makeTableHeaderVO, makeTableViewBackgroundVO, makeCantJoinReasonTextVO, makeAwardGroupDataTooltipVO, makeParameterTooltipVO
from gui.Scaleform.daapi.view.lobby.event_boards.formaters import getStatusTitleStyle, getStatusCountStyle, formatUpdateTime, formatErrorTextWithIcon, getFullName
from gui.Scaleform.locale.TOOLTIPS import TOOLTIPS
from gui.Scaleform.locale.EVENT_BOARDS import EVENT_BOARDS
from gui.Scaleform.genConsts.EVENTBOARDS_ALIASES import EVENTBOARDS_ALIASES
from gui.Scaleform.daapi.view.meta.EventBoardsTableViewMeta import EventBoardsTableViewMeta
from gui.event_boards.event_boards_items import EVENT_STATE as _es, EventSettings, LeaderBoard, PLAYER_STATE_REASON as _psr
MyInfo = namedtuple(b'MyInfo', (b'fullData', b'pageNumber', b'rank', b'battlesCount'))
LeaderboardData = namedtuple(b'LeaderboardData', (b'excelItems', b'pageNumber'))

class EventBoardsTableView(LobbySubView, EventBoardsTableViewMeta):
    eventsController = dependency.descriptor(IEventBoardController)
    itemsCache = dependency.descriptor(IItemsCache)
    MIN_CATEGORY = 1
    MAX_CATEGORY = 5
    TOP_POSITION_RANK = -1
    MY_RANK = -2
    MAX_AWARD_GROUPS = 4

    def __init__(self, ctx):
        super(EventBoardsTableView, self).__init__()
        self.__pagination = None
        self.__awardGroup = None
        self.__maintenance = None
        self.__eventID = ctx[b'eventID']
        self.__leaderboardID = ctx[b'leaderboardID']
        self.__maintenanceVisible = False
        self.__cleanUp()
        return

    def getEventID(self):
        return self.__eventID

    def changeLeaderboard(self, leaderboardID):
        self.__cleanUp()
        self.__leaderboardID = leaderboardID
        self.__fetchEventData()
        return

    def closeView(self):
        self.destroy()
        return

    @property
    def eventData(self):
        return self.__eventData

    @property
    def leaderboardID(self):
        return self.__leaderboardID

    def onStepPage(self, direction):
        self.__fetchMyLeaderboardInfo(partial(self.__fetchLeaderboardPageData, self.__leaderboardData.pageNumber + direction, self.TOP_POSITION_RANK))
        return

    def onShowRewardCategory(self, categoryID):
        categoryPage = self.__rewardCategories[categoryID][b'page_number']
        if self.__leaderboardData.pageNumber != categoryPage:
            self.__fetchMyLeaderboardInfo(partial(self.__fetchLeaderboardPageData, categoryPage, self.__rewardCategories[categoryID][b'rank_min']))
        else:
            self.__scrollToRank(self.__rewardCategories[categoryID][b'rank_min'])
        return

    def onRefresh(self):
        self.__fetchEventData()
        return

    def setMyPlace(self):
        self.__fetchMyLeaderboardInfo(self.__moveToMyPlace)
        return

    def showNextAward(self, visible):
        stripes = self.__stripes
        if stripes and stripes[b'tableDP']:
            groupID = stripes[b'tableDP'][1 if visible else 0][b'id']
            self.__awardGroup.setActiveRewardGroup(groupID)
        return

    def playerClick(self, playerID):
        for item in self.__leaderboardData.excelItems:
            if item.getSpaId() == playerID:
                g_eventBus.handleEvent(events.LoadViewEvent(SFViewLoadParams(EVENTBOARDS_ALIASES.EVENTBOARDS_DETAILS_BATTLE_VIEW), ctx={b'eventID': (self.__eventID), 
                   b'leaderboard': (self.__leaderboard), 
                   b'excelItem': item}), scope=EVENT_BUS_SCOPE.LOBBY)
                break

        return

    @adisp_process
    def participateStatusClick(self):
        self.__setWaiting(True)
        yield self.eventsController.joinEvent(self.__eventID)
        yield self.eventsController.getEvents()
        self.__setWaiting(False)
        self.__setPlayerData()
        self.__updateStatus()
        return

    def _populate(self):
        super(EventBoardsTableView, self)._populate()
        self.app.loaderManager.onViewLoaded += self.__onViewLoaded
        self.__fetchEventData()
        return

    def _dispose(self):
        pagination = self.__pagination
        if pagination:
            pagination.onStepPage -= self.onStepPage
        if self.__awardGroup:
            self.__awardGroup.onShowRewardCategory -= self.onShowRewardCategory
        if self.__maintenance:
            self.__maintenance.onRefresh -= self.onRefresh
        self.app.loaderManager.onViewLoaded -= self.__onViewLoaded
        super(EventBoardsTableView, self)._dispose()
        return

    def _onRegisterFlashComponent(self, viewPy, alias):
        super(EventBoardsTableView, self)._onRegisterFlashComponent(viewPy, alias)
        if isinstance(viewPy, EventBoardsPagination):
            self.__pagination = viewPy
            viewPy.onStepPage += self.onStepPage
        if isinstance(viewPy, EventBoardsAwardGroup):
            self.__awardGroup = viewPy
            viewPy.onShowRewardCategory += self.onShowRewardCategory
        if isinstance(viewPy, EventBoardsMaintenance):
            self.__maintenance = viewPy
            viewPy.onRefresh += self.onRefresh
        return

    def __cleanUp(self):
        self.__eventData = None
        self.__myInfo = None
        self.__leaderboard = None
        self.__leaderboardData = None
        self.__rewardCategories = None
        self.__stripes = None
        self.__playerState = None
        self.__top = None
        return

    def __setMaintenance(self, visible):
        if self.__maintenanceVisible != visible:
            self.__maintenanceVisible = visible
            headerText = icons.makeImageTag(RES_ICONS.MAPS_ICONS_LIBRARY_ALERTICON) + _ms(EVENT_BOARDS.MAINTENANCE_TITLE)
            bodyText = _ms(EVENT_BOARDS.MAINTENANCE_BODY)
            buttonText = _ms(EVENT_BOARDS.MAINTENANCE_UPDATE)
            self.as_setMaintenanceS(visible, headerText, bodyText, buttonText)
        return

    def __setWaiting(self, visible):
        self.as_setWaitingS(visible, _ms(b'#waiting:loadContent'))
        return

    def __updateStatus(self):
        event = self.__eventData
        playerState = self.__playerState
        myInfo = self.__myInfo
        state = playerState.getPlayerState() if playerState else None
        canJoin = playerState.getCanJoin() if playerState else True
        stateReasons = playerState.getPlayerStateReasons() if playerState else []
        joined = state is _es.JOINED
        cardinality = event.getCardinality()
        battleCount = myInfo.battlesCount if myInfo else 0
        notFull = cardinality is not None and battleCount < cardinality
        outOfScore = not myInfo.fullData.getIsInsideViewsize() if myInfo else False
        visible = True
        title = b''
        tooltip = None
        showPoints = False
        titleTooltip = None
        buttonVisible = False
        buttonEnabled = False
        buttonLabel = TOOLTIPS.ELEN_BUTTON_REGISTRATION_STARTED_HEADER
        buttonTooltip = makeTooltip(buttonLabel, TOOLTIPS.ELEN_BUTTON_REGISTRATION_STARTED_BODY)
        method = event.getMethod()
        if event.isFinished():
            if not joined:
                title = getStatusTitleStyle(_ms(EVENT_BOARDS.EXCEL_PARTICIPATE_NOTPARTICIPATED))
            elif notFull:
                title = getStatusTitleStyle(_ms(EVENT_BOARDS.EXCEL_PARTICIPATE_NOTPARTICIPATED))
            elif outOfScore:
                showPoints = True
                title = getStatusTitleStyle(_ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_OUTOFRATING))
            else:
                visible = False
        elif joined:
            if notFull:
                showPoints = True
                count = getStatusCountStyle(str(cardinality - battleCount))
                title = getStatusTitleStyle(_ms(EVENT_BOARDS.EXCEL_HEADER_REASON_BATTLESLEFT, number=count))
            elif outOfScore:
                showPoints = True
                title = getStatusTitleStyle(_ms(EVENT_BOARDS.STATUS_CANTJOIN_REASON_OUTOFRATING))
            else:
                visible = False
        elif event.isRegistrationFinished():
            title = formatErrorTextWithIcon(EVENT_BOARDS.STATUS_CANTJOIN_REASON_ENDREGISTRATION)
            tooltip = makeTooltip(EVENT_BOARDS.STATUS_CANTJOIN_REASON_ENDREGISTRATION, EVENT_BOARDS.STATUS_CANTJOIN_REASON_ENDREGISTRATION_TOOLTIP)
        elif canJoin:
            buttonVisible = _psr.SPECIALACCOUNT not in stateReasons
            buttonEnabled = True
        else:
            title, tooltip, buttonVisible = makeCantJoinReasonTextVO(event, self.__playerData)
        if joined and outOfScore and notFull and not event.isFinished():
            amount = myInfo.fullData.getLastInLeaderboardValue()
            parameter = event.getObjectiveParameter()
            titleTooltip = makeParameterTooltipVO(method, amount, parameter)
        playerName = getattr(BigWorld.player(), b'name', b'')
        playerName = getFullName(playerName, myInfo.fullData.getClanTag(), myInfo.fullData.getClanColor())
        myPosition = self.__myInfo.rank
        self.as_setStatusVisibleS(visible)
        self.as_setMyPlaceVisibleS(not visible and myPosition is not None)
        if visible:
            p1 = myInfo.fullData.getP1()
            p2 = myInfo.fullData.getP2()
            p3 = myInfo.fullData.getP3()
            self.as_setStatusDataS(makeEventBoardsTableViewStatusVO(title, tooltip, playerName, p1, p2, p3, showPoints, buttonLabel, buttonTooltip, buttonVisible, buttonEnabled, titleTooltip, method))
        return

    def __calculateRewardCategories(self, rewardGroups, leaderboardViewSize):
        rewardCategories = {}
        last = 0
        for group in rewardGroups:
            rankMin, rankMax = group.getRankMinMax()
            number = group.getRewardCategoryNumber()
            if number not in rewardCategories:
                rewardCategories[number] = {b'rank_min': leaderboardViewSize, b'rank_max': 0, b'rewards': []}
            category = rewardCategories[number]
            category[b'rank_min'] = min(rankMin, category[b'rank_min'])
            category[b'rank_max'] = max(rankMax, category[b'rank_max'])
            category[b'rewards'].append(group.getRewards())
            last = max(last, rankMax)

        if last < leaderboardViewSize:
            rewardCategories[self.MAX_CATEGORY] = {b'rank_min': (last + 1), b'rank_max': leaderboardViewSize, 
               b'rewards': []}
        return rewardCategories

    def __updateRewardCategoriesPlayers(self, rewardCategories, rewards, excelItems):
        last = 0
        categoryPages = {reward.getRewardCategoryNumber(): reward.getPageNumber() for reward in rewards}
        for number in range(self.MIN_CATEGORY, self.MAX_CATEGORY + 1):
            if number not in rewardCategories:
                continue
            category = rewardCategories[number]
            category[b'page_number'] = categoryPages.get(number)
            players = category[b'players'] = []
            for item in excelItems[last:]:
                if category[b'rank_min'] <= item.getRank() <= category[b'rank_max']:
                    players.append(item)
                    last += 1
                elif item.getRank() > category[b'rank_max']:
                    break

        return

    def __setPlayerData(self):
        self.__playerData = self.eventsController.getPlayerEventsData()
        self.__playerState = self.__playerData.getPlayerStateByEventId(self.__eventID)
        return

    def __fetchEventData(self):
        eventData = self.eventsController.getEventsSettingsData().getEvent(self.__eventID)
        rewardByRank = eventData.getRewardsByRank().getRewardByRank(self.__leaderboardID) if eventData else None
        if eventData is None or rewardByRank is None:
            self.__setMaintenance(True)
        else:
            self.__setMaintenance(False)
            self.__eventData = eventData
            self.__rewardCategories = self.__calculateRewardCategories(rewardByRank.getRewardGroups(), eventData.getLeaderboardViewSize())
            eType = eventData.getType()
            leaderboardValue = eventData.getLeaderboard(self.__leaderboardID)
            objectiveParameter = eventData.getObjectiveParameter()
            self.__method = eventData.getMethod()
            self.as_setMyPlaceVisibleS(False)
            self.__updateHeader()
            self.as_setBackgroundS(makeTableViewBackgroundVO(eType, leaderboardValue))
            self.as_setTableHeaderDataS(makeTableHeaderVO(self.__method, objectiveParameter, eType))
            self.__setPlayerData()
            myEventsTop = self.eventsController.getMyEventsTopData()
            self.__top = myEventsTop.getMyLeaderboardEventTop(self.__eventID, self.__leaderboardID)
            self.__fetchMyLeaderboardInfo(self.__moveToMyPlace)
        return

    @adisp_process
    def __fetchLeaderboardPageData(self, page, rank):
        self.__setWaiting(True)
        leaderboard = yield self.eventsController.getLeaderboard(self.__eventID, self.__leaderboardID, page)
        self.__setWaiting(False)
        if leaderboard is None:
            self.__setMaintenance(True)
        else:
            self.__setMaintenance(False)
            excelItems = leaderboard.getExcelItems()
            pageNumber = leaderboard.getPageNumber()
            pagesAmount = leaderboard.getPagesAmount()
            rewards = leaderboard.getRewards()
            self.__leaderboard = leaderboard
            self.__leaderboardData = LeaderboardData(excelItems, pageNumber)
            self.__updateRewardCategoriesPlayers(self.__rewardCategories, rewards, excelItems)
            self.__pagination.updatePage(pageNumber, pagesAmount)
            self.__updateHeader()
            if excelItems:
                self.__updatePage()
                self.__scrollToRank(rank)
                enabledAncors = []
                for categoryIdx in range(self.MIN_CATEGORY, self.MAX_CATEGORY + 1):
                    if categoryIdx in self.__rewardCategories:
                        enable = self.__rewardCategories[categoryIdx].get(b'page_number') is not None
                        self.__awardGroup.as_setEnabledS(categoryIdx - 1, enable)
                    else:
                        enable = False
                    enabledAncors.append(enable)

                group = []
                for idx in range(self.MAX_AWARD_GROUPS + 1):
                    group.append(enabledAncors[idx])

                self.__awardGroup.as_setDataS(group)
                self.__awardGroup.as_setTooltipsS(makeAwardGroupDataTooltipVO(self.__rewardCategories, enabledAncors))
                self.as_setMyPlaceTooltipS(makeTooltip(TOOLTIPS.ELEN_ANCOR_MYPOSITION_HEADER, TOOLTIPS.ELEN_ANCOR_MYPOSITION_BODY))
            else:
                self.as_setEmptyDataS(_ms(EVENT_BOARDS.EXCEL_NODATA))
        return

    @adisp_process
    def __fetchMyLeaderboardInfo(self, onSuccess):
        self.__setWaiting(True)
        myInfo = yield self.eventsController.getMyLeaderboardInfo(self.__eventID, self.__leaderboardID)
        self.__setWaiting(False)
        if myInfo is None:
            self.__setMaintenance(True)
        else:
            self.__setMaintenance(False)
            pageNumber = myInfo.getPageNumber()
            rank = myInfo.getRank()
            battlesCount = myInfo.getBattlesCount()
            self.__myInfo = MyInfo(myInfo, pageNumber, rank, battlesCount)
            self.__updateStatus()
            onSuccess()
        return

    def __moveToMyPlace(self):
        pageNumber = self.__myInfo.pageNumber
        rank = self.__myInfo.rank
        if pageNumber and rank and rank <= self.__eventData.getLeaderboardViewSize():
            self.__fetchLeaderboardPageData(pageNumber, self.MY_RANK)
        else:
            self.__fetchLeaderboardPageData(1, self.TOP_POSITION_RANK)
        return

    def __onViewLoaded(self, view, *args, **kwargs):
        if view.alias in (EVENTBOARDS_ALIASES.RESULT_FILTER_POPOVER_ALIAS,
         EVENTBOARDS_ALIASES.RESULT_FILTER_POPOVER_VEHICLES_ALIAS):
            if view.caller == b'excel':
                view.setData(self.__eventData, self.changeLeaderboard, self.__leaderboardID)
        return

    def __updateHeader(self):
        event = self.__eventData
        name = event.getName()
        eType = event.getType()
        leaderboard = self.__leaderboard
        leaderboardValue = event.getLeaderboard(self.__leaderboardID)
        if event.isFinished():
            date = backport.getLongDateFormat(event.getEndDateTs())
            status = text_styles.main(_ms(EVENT_BOARDS.TIME_EVENTFINISHED, date=date))
            statusTooltip = None
        elif leaderboard:
            recalculationTS = leaderboard.getLastLeaderboardRecalculationTS()
            recalculationInterval = leaderboard.getRecalculationInterval()
            interval = int(recalculationInterval / ONE_MINUTE)
            status = text_styles.main(formatUpdateTime(recalculationTS))
            statusTooltip = _ms(TOOLTIPS.SUMMARY_STATUS_TOOLTIP, interval=interval)
        else:
            status = None
            statusTooltip = None
        self.as_setHeaderDataS(makeTableViewHeaderVO(eType, leaderboardValue, name, status, statusTooltip))
        return

    def __updatePage(self):
        data, stripes = makeEventBoardsTableDataVO(self.__rewardCategories, self.__method)
        self.__stripes = stripes
        self.as_setTableDataS(data)
        self.as_setAwardsStripesS(stripes)
        if self.__myInfo.rank is not None:
            myPosition = self.__getMyPosition()
            if myPosition is not None:
                self.as_setMyPlaceS(myPosition)
        return

    def __scrollToRank(self, rank):
        if rank == self.TOP_POSITION_RANK:
            self.as_setScrollPosS(0, False)
            categoryNumber = self.__getCategoryByRank(self.__leaderboardData.excelItems[0].getRank())
        elif rank == self.MY_RANK:
            self.as_setScrollPosS(self.__getMyPosition(), True)
            categoryNumber = self.__getCategoryByRank(self.__myInfo.rank)
        else:
            self.as_setScrollPosS(self.__getPositionByRank(rank), False)
            categoryNumber = self.__getCategoryByRank(rank)
        if self.MIN_CATEGORY < categoryNumber <= self.MAX_CATEGORY - 1:
            self.__awardGroup.setActiveRewardGroup(categoryNumber)
        return

    @dependency.replace_none_kwargs(connectionMgr=IConnectionManager)
    def __getMyPosition(self, connectionMgr=None):
        if connectionMgr is not None:
            mySpaID = connectionMgr.databaseID
            for idx, item in enumerate(self.__leaderboardData.excelItems):
                if item.getSpaId() == mySpaID:
                    startCategoryNumber = self.__getCategoryByRank(self.__leaderboardData.excelItems[0].getRank())
                    currentCategoryNumber = self.__getCategoryByRank(item.getRank())
                    if startCategoryNumber and currentCategoryNumber:
                        return idx + 1 + (currentCategoryNumber - startCategoryNumber)
                    break

        return

    def __getPositionByRank(self, rank):
        for idx, item in enumerate(self.__leaderboardData.excelItems):
            if item.getRank() >= rank:
                startCategoryNumber = self.__getCategoryByRank(self.__leaderboardData.excelItems[0].getRank())
                currentCategoryNumber = self.__getCategoryByRank(rank)
                if startCategoryNumber and currentCategoryNumber:
                    return idx + 1 + (currentCategoryNumber - startCategoryNumber)
                break

        return

    def __getCategoryByRank(self, rank):
        for number, category in self.__rewardCategories.iteritems():
            if category[b'rank_min'] <= rank <= category[b'rank_max']:
                return number

        return 0
