from __future__ import absolute_import
from adisp import adisp_process
from debug_utils import LOG_DEBUG
from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesViewWithTable import ClanInvitesAbstractDataProvider
from gui.Scaleform.daapi.view.meta.ClanRequestsViewMeta import ClanRequestsViewMeta
from gui.Scaleform.genConsts.CLANS_ALIASES import CLANS_ALIASES
from gui.Scaleform.locale.CLANS import CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.clans import formatters
from gui.clans.clan_helpers import isInClanEnterCooldown
from gui.clans.data_wrapper.utils import formatField, isValueAvailable
from gui.clans.settings import CLAN_INVITE_STATES
from gui.impl import backport
from gui.shared.events import CoolDownEvent
from gui.shared.formatters import text_styles
from gui.shared.view_helpers import CooldownHelper
from gui.wgcg.clan.contexts import AcceptApplicationCtx, DeclineApplicationCtx, CreateInviteCtx, AccountsInfoCtx
from gui.wgcg.settings import WebRequestDataType
from helpers.i18n import makeString as _ms

class ClanRequestsView(ClanRequestsViewMeta):

    def __init__(self):
        super(ClanRequestsView, self).__init__()
        self._cooldown = CooldownHelper([
         WebRequestDataType.CREATE_APPLICATIONS,
         WebRequestDataType.CREATE_INVITES,
         WebRequestDataType.ACCEPT_APPLICATION,
         WebRequestDataType.ACCEPT_INVITE,
         WebRequestDataType.DECLINE_APPLICATION,
         WebRequestDataType.DECLINE_INVITE,
         WebRequestDataType.DECLINE_INVITES,
         WebRequestDataType.CLAN_INVITES,
         WebRequestDataType.CLAN_MEMBERS_RATING], self._onCooldownHandle, CoolDownEvent.WGCG)
        return

    @property
    def actualRequestsPaginator(self):
        return self._getPaginatorByFilterName(CLANS_ALIASES.INVITE_WINDOW_FILTER_ACTUAL)

    @property
    def expiredRequestsPaginator(self):
        return self._getPaginatorByFilterName(CLANS_ALIASES.INVITE_WINDOW_FILTER_EXPIRED)

    @property
    def processedRequestsPaginator(self):
        return self._getPaginatorByFilterName(CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED)

    def acceptRequest(self, dbId):
        applicationID = int(dbId)
        ctx = AcceptApplicationCtx(applicationID)
        self._getCurrentPaginator().accept(applicationID, ctx)
        return

    def declineRequest(self, dbId):
        applicationID = int(dbId)
        ctx = DeclineApplicationCtx(applicationID)
        self._getCurrentPaginator().decline(applicationID, ctx)
        return

    def sendInvite(self, dbId):
        dbId = int(dbId)
        paginator = self._getCurrentPaginator()
        requestWrapper = paginator.getInviteByDbID(dbId)
        ctx = CreateInviteCtx(requestWrapper.getClanDbID(), [requestWrapper.getAccountDbID()])
        self._getCurrentPaginator().resend(dbId, ctx)
        self._enableRefreshBtn(True)
        return

    def onClanAppsCountReceived(self, clanDbID, appsCount):
        super(ClanRequestsView, self).onClanAppsCountReceived(clanDbID, appsCount)
        if self.actualRequestsPaginator.isSynced():
            self._enableRefreshBtn(True)
        return

    def _onAttachedToWindow(self):
        super(ClanRequestsView, self)._onAttachedToWindow()
        self._cooldown.start()
        self.filterBy(self.currentFilterName)
        return

    def _dispose(self):
        self._cooldown.stop()
        self._cooldown.stop()
        self._cooldown = None
        super(ClanRequestsView, self)._dispose()
        return

    def _onCooldownHandle(self, isInCooldown):
        self.dataProvider.allowActions(not isInCooldown)
        return

    def _getViewAlias(self):
        return CLANS_ALIASES.CLAN_PROFILE_REQUESTS_VIEW_ALIAS

    def _showDummyByFilterName(self, filterName):
        if filterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_ACTUAL:
            self._showDummy(CLANS.CLANINVITESWINDOW_DUMMY_NOACTUALREQUESTS_TITLE)
        elif filterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_EXPIRED:
            self._showDummy(CLANS.CLANINVITESWINDOW_DUMMY_NOEXPIREDREQUESTS_TITLE)
        elif filterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED:
            self._showDummy(CLANS.CLANINVITESWINDOW_DUMMY_NOPROCESSEDREQUESTS_TITLE)
        else:
            LOG_DEBUG(b'Unexpected behaviour: no dummy for filter', filterName)
            self._showDummy(CLANS.CLANINVITESWINDOW_DUMMY_NOACTUALREQUESTS_TITLE)
        return

    def _getDefaultFilterName(self):
        return CLANS_ALIASES.INVITE_WINDOW_FILTER_ACTUAL

    def _getDefaultSortFields(self):
        return (
         (
          b'status', False),)

    def _getSecondSortFields(self):
        if self.currentFilterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED or self.currentFilterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_EXPIRED:
            return (b'updatedAt',)
        return (b'createdAt',)

    def _createSearchDP(self):
        return RequestDataProvider(self)

    @adisp_process
    def _onListUpdated(self, selectedID, isFullUpdate, isReqInCoolDown, result):
        yield lambda callback: callback(None)
        status, data = result
        accountsInfo = tuple()
        if status is True and data:
            ctx = AccountsInfoCtx(tuple(item.getAccountDbID() for item in data))
            accountsResponse = yield self.webCtrl.sendRequest(ctx)
            if accountsResponse.isSuccess():
                accountsInfo = ctx.getDataObj(accountsResponse.data)
        self.dataProvider.setAccountsInfo(accountsInfo)
        super(ClanRequestsView, self)._onListUpdated(selectedID, isFullUpdate, isReqInCoolDown, result)
        return

    def _makeFilters(self):
        return [
         {b'alias': (CLANS_ALIASES.INVITE_WINDOW_FILTER_ACTUAL), 
            b'text': (_ms(CLANS.CLANINVITESWINDOW_FILTERS_ACTUAL, value=self.formatInvitesCount(self.actualRequestsPaginator)))},
         {b'alias': (CLANS_ALIASES.INVITE_WINDOW_FILTER_EXPIRED), 
            b'text': (_ms(CLANS.CLANINVITESWINDOW_FILTERS_EXPIRED, value=self.formatInvitesCount(self.expiredRequestsPaginator)))},
         {b'alias': (CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED), 
            b'text': (_ms(CLANS.CLANINVITESWINDOW_FILTERS_PROCESSED, value=self.formatInvitesCount(self.processedRequestsPaginator)))}]

    def _makeHeaders(self):
        return [
         self._packHeaderColumnData(b'userName', CLANS.CLANINVITESWINDOW_TABLE_USERNAME, 225, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_REQUESTS_USERNAME, textAlign=b'left', defaultSortDirection=b'ascending'),
         self._packHeaderColumnData(b'message', b'', 73, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_REQUESTS_MESSAGE, RES_ICONS.MAPS_ICONS_CLANS_INVITESWINDOW_ICON_STATISTICS_CLAN_INVITE_098),
         self._packHeaderColumnData(b'personalRating', b'', 98, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_REQUESTS_PERSONALRATING, RES_ICONS.MAPS_ICONS_STATISTIC_RATING24),
         self._packHeaderColumnData(b'battlesCount', b'', 98, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_REQUESTS_BATTLESCOUNT, RES_ICONS.MAPS_ICONS_STATISTIC_BATTLES24),
         self._packHeaderColumnData(b'wins', b'', 98, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_REQUESTS_WINS, RES_ICONS.MAPS_ICONS_STATISTIC_WINS24),
         self._packHeaderColumnData(b'awgExp', b'', 98, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_REQUESTS_AWGEXP, RES_ICONS.MAPS_ICONS_STATISTIC_AVGEXP24),
         self._packHeaderColumnData(b'status', CLANS.CLANINVITESWINDOW_TABLE_STATUS, 160, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_REQUESTS_STATUS),
         self._packHeaderColumnData(b'actions', CLANS.CLANINVITESWINDOW_TABLE_ACTIONS, 140, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_REQUESTS_ACTIONS, enabled=False)]


class RequestDataProvider(ClanInvitesAbstractDataProvider):

    def __init__(self, proxy):
        super(RequestDataProvider, self).__init__(proxy)
        self.__accountsInfo = {}
        return

    def setAccountsInfo(self, acc_info):
        self.__accountsInfo = dict((info.getDbID(), info) for info in acc_info)
        return

    def getStatusByDbID(self, dbID):
        return self.getExtraData(dbID)

    def invalidateItems(self):
        for item in self.collection:
            if self._isDataRow(item):
                item[b'actions'] = self.__buildActionsSection(item[b'userInfo'][b'dbID'], self.getStatusByDbID(item[b'dbID']))

        return

    def _buildExtraData(self, item, prevExtra):
        return item.getStatus()

    def _makeVO(self, item, extraData):
        accountDbId = item.getAccountDbID()
        return {b'dbID': (item.getDbID()), 
           b'userInfo': {b'userName': (item.getAccountName()), 
                         b'dbID': accountDbId}, 
           b'personalRating': (formatField(getter=item.getPersonalRating, formatter=backport.getIntegralFormat)), 
           b'battlesCount': (formatField(getter=item.getBattlesCount, formatter=backport.getIntegralFormat)), 
           b'wins': (formatField(getter=item.getBattlesPerformanceAvg, formatter=(lambda value: backport.getNiceNumberFormat(value) + b'%'))), 
           b'awgExp': (formatField(getter=item.getBattleXpAvg, formatter=backport.getIntegralFormat)), 
           b'status': {b'text': (self._makeInviteStateString(item)), 
                       b'tooltip': (self._makeTooltip(body=self._makeRequestTooltip(status=item.getStatus(), user=formatField(getter=item.getChangerName), date=formatField(getter=item.getUpdatedAt, formatter=formatters.formatShortDateShortTimeString))))}, 
           b'canShowContextMenu': True, 
           b'messageTooltip': (self._makeTooltip(body=item.getComment() if isValueAvailable(getter=item.getComment) else str())), 
           b'actions': (self.__buildActionsSection(accountDbId, item.getStatus()))}

    def _makeRequestTooltip(self, status, date, user=None):
        if status == CLAN_INVITE_STATES.ACCEPTED:
            return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_REQUESTACCEPTED)), text_styles.main(date), text_styles.main(b''), text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_BYUSER)), text_styles.stats(user))
        else:
            if status in (CLAN_INVITE_STATES.DECLINED, CLAN_INVITE_STATES.DECLINED_RESENT):
                return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_REQUESTDECLINED)), text_styles.main(date), text_styles.main(b''), text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_BYUSER)), text_styles.stats(user))
            if status in (CLAN_INVITE_STATES.EXPIRED, CLAN_INVITE_STATES.EXPIRED_RESENT):
                return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_REQUESTEXPIRED)), text_styles.main(date))
            if status == CLAN_INVITE_STATES.ACTIVE:
                return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_REQUEST_REQUESTSENT)), text_styles.main(date))
            return

    def __buildActionsSection(self, accountDbId, inviteStatus):
        acceptButtonEnabled = False
        declineButtonEnabled = False
        inviteButtonEnabled = False
        acceptButtonVisible = False
        declineButtonVisible = False
        inviteButtonVisible = False
        invBtnTooltip = None
        acceptButtonTooltip = None
        clanHasFreeSpaces = self.proxy.clanInfo.hasFreePlaces()
        if self.proxy.currentFilterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_ACTUAL:
            if inviteStatus == CLAN_INVITE_STATES.ACTIVE:
                declineButtonVisible = True
                acceptButtonVisible = True
                declineButtonEnabled = self.isActionsAllowed()
                if not clanHasFreeSpaces:
                    acceptButtonTooltip = self._makeTooltip(body=_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_CANTSENDINVITE_BODY))
                else:
                    accInfo = self.__accountsInfo.get(accountDbId)
                    if accInfo and isInClanEnterCooldown(accInfo.getClanCooldownTill()):
                        acceptButtonTooltip = self._makeTooltip(body=_ms(text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_CANTACCEPTREQUESTDUETOCD_BODY)), text_styles.main(formatters.formatShortDateShortTimeString(accInfo.getClanCooldownTill())))))
                    else:
                        acceptButtonEnabled = self.isActionsAllowed()
        elif self.proxy.currentFilterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_EXPIRED:
            if inviteStatus == CLAN_INVITE_STATES.EXPIRED:
                inviteButtonVisible = True
                if not clanHasFreeSpaces:
                    invBtnTooltip = CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_CANTACCEPTREQUEST_BODY
                else:
                    invBtnTooltip = CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_INVITES_INVITEBUTTON
                    inviteButtonEnabled = self.isActionsAllowed()
        elif self.proxy.currentFilterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED:
            if inviteStatus == CLAN_INVITE_STATES.DECLINED:
                inviteButtonVisible = True
                if not clanHasFreeSpaces:
                    invBtnTooltip = CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_CANTACCEPTREQUEST_BODY
                else:
                    invBtnTooltip = CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_INVITES_INVITEBUTTON
                    inviteButtonEnabled = self.isActionsAllowed()
        return {b'acceptButtonEnabled': acceptButtonEnabled, 
           b'declineButtonEnabled': declineButtonEnabled, 
           b'inviteButtonEnabled': inviteButtonEnabled, 
           b'acceptButtonVisible': acceptButtonVisible, 
           b'declineButtonVisible': declineButtonVisible, 
           b'inviteButtonVisible': inviteButtonVisible, 
           b'inviteButtonText': (_ms(CLANS.CLANINVITESWINDOW_TABLE_INVITEBUTTON)), 
           b'inviteButtonTooltip': (self._makeTooltip(body=_ms(invBtnTooltip))), 
           b'acceptButtonTooltip': acceptButtonTooltip}
