from __future__ import absolute_import
from gui.clans import formatters
from gui.clans.clan_helpers import ClanPersonalInvitesPaginator, ClanListener
from gui.clans.items import ClanCommonData
from gui.clans.data_wrapper.utils import formatField, isValueAvailable
from gui.clans.settings import CLAN_INVITE_STATES
from gui.impl import backport
from gui.wgcg.settings import WebRequestDataType
from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesViewWithTable import ClanInvitesAbstractDataProvider
from gui.Scaleform.daapi.view.meta.ClanPersonalInvitesViewMeta import ClanPersonalInvitesViewMeta
from gui.Scaleform.locale.CLANS import CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.shared.events import CoolDownEvent
from gui.shared.utils.functions import makeTooltip
from gui.shared.formatters import text_styles
from gui.shared.view_helpers import CooldownHelper
from gui.shared.utils import getPlayerDatabaseID
from helpers import dependency
from helpers.i18n import makeString as _ms
from helpers.html import escape
from skeletons.gui.web import IWebController

class ClanPersonalInvitesView(ClanPersonalInvitesViewMeta, ClanListener):

    def __init__(self):
        super(ClanPersonalInvitesView, self).__init__()
        self._paginator = ClanPersonalInvitesPaginator(self.webCtrl, getPlayerDatabaseID(), [CLAN_INVITE_STATES.ACTIVE])
        self._cooldown = CooldownHelper([
         WebRequestDataType.ACCEPT_APPLICATION,
         WebRequestDataType.ACCEPT_INVITE,
         WebRequestDataType.DECLINE_APPLICATION,
         WebRequestDataType.DECLINE_INVITE,
         WebRequestDataType.DECLINE_INVITES,
         WebRequestDataType.CLANS_INFO,
         WebRequestDataType.CLAN_RATINGS,
         WebRequestDataType.ACCOUNT_INVITES], self._onCooldownHandle, CoolDownEvent.WGCG)
        return

    def declineAllSelectedInvites(self):
        self._paginator.declineList(self.dataProvider.getCheckedIDs())
        return

    def acceptInvite(self, dbID):
        self._paginator.accept(int(dbID))
        return

    def declineInvite(self, dbID):
        self._paginator.decline(int(dbID))
        return

    def showMore(self):
        if not self._paginator.isInProgress():
            self.showWaiting(True)
            self._paginator.right()
        return

    def setSelectAllInvitesCheckBoxSelected(self, selected):
        self.dataProvider.setSelectAll(selected)
        self._updateDeclineSelectedGroup()
        return

    def setInviteSelected(self, dbID, selected):
        self.dataProvider.setCheckedID(dbID, selected)
        self._updateDeclineSelectedGroup()
        return

    def onSortChanged(self, dataProvider, sort):
        order = sort[0][1]
        secondSort = tuple((item, order) for item in self._getSecondSortFields())
        if not self._paginator.isInProgress():
            self.showWaiting(True)
            self._paginator.sort(sort + secondSort)
        return

    def onAccountInvitesReceived(self, invites):
        super(ClanPersonalInvitesView, self).onAccountInvitesReceived(invites)
        self._enableRefreshBtn(True)
        return

    def showWaiting(self, show):
        if show:
            self._parentWnd.as_showWaitingS(CLANS.CLANPERSONALINVITESWINDOW_LOADING, {})
        elif not self._paginator.isInProgress():
            self._parentWnd.as_hideWaitingS()
        return

    def refreshTable(self):
        self._enableRefreshBtn(False)
        self.showWaiting(True)
        self._paginator.refresh()
        return

    def _createSearchDP(self):
        return PersonalInvitesDataProvider(self)

    def _onAttachedToWindow(self):
        super(ClanPersonalInvitesView, self)._onAttachedToWindow()
        self.showWaiting(True)
        self.setSelectAllInvitesCheckBoxSelected(False)
        self._updateDeclineSelectedText(0)
        self._cooldown.start()
        self._paginator.onListUpdated += self._onListUpdated
        self._paginator.onListItemsUpdated += self._onListItemsUpdated
        self._paginator.reset()
        return

    def _populate(self):
        super(ClanPersonalInvitesView, self)._populate()
        self.startClanListening()
        return

    def _dispose(self):
        self._paginator.onListUpdated -= self._onListUpdated
        self._paginator.onListItemsUpdated -= self._onListItemsUpdated
        self._cooldown.stop()
        self._cooldown = None
        self.stopClanListening()
        self.webCtrl.clearClanCommonDataCache()
        super(ClanPersonalInvitesView, self)._dispose()
        return

    def _onCooldownHandle(self, isInCooldown):
        self.dataProvider.allowActions(not isInCooldown)
        return

    def _onListUpdated(self, selectedID, isFullUpdate, isReqInCoolDown, result):
        self._updateSortField(self._paginator.getLastSort())
        status, data = result
        if status is True:
            self._enableRefreshBtn(False)
            if not data:
                self._showDummy(CLANS.CLANPERSONALINVITESWINDOW_NOINVITES)
                self.dataProvider.rebuildList(None, False)
            else:
                self.webCtrl.updateClanCommonDataCache([ClanCommonData.fromClanPersonalInviteWrapper(item) for item in data])
                self.dataProvider.rebuildList(data, self._paginator.canMoveRight())
                self.as_hideDummyS()
        else:
            self._enableRefreshBtn(True, toolTip=CLANS.CLANINVITESWINDOW_TOOLTIPS_REFRESHBUTTON_ENABLEDTRYTOREFRESH)
            self._showDummy(CLANS.CLANINVITESWINDOW_DUMMY_SERVERERROR_TITLE, CLANS.CLANINVITESWINDOW_DUMMY_SERVERERROR_TEXT, RES_ICONS.MAPS_ICONS_LIBRARY_ALERTBIGICON, alignCenter=False)
        self._updateDeclineSelectedGroup()
        self.showWaiting(False)
        return

    def _onListItemsUpdated(self, paginator, items):
        self.dataProvider.refreshItems(items)
        self._updateDeclineSelectedGroup()
        if not self._paginator.isInProgress():
            self.showWaiting(False)
        return

    def _updateDeclineSelectedGroup(self):
        hasInvites = self.dataProvider.itemsCount() > 0
        self._updateDeclineSelectedText(self.dataProvider.selectedCount())
        self.as_setSelectAllCheckboxStateS(self.dataProvider.areAllSelected(), hasInvites)
        return

    def _updateDeclineSelectedText(self, count):
        self.as_setDeclineAllSelectedInvitesStateS(_ms(CLANS.CLANPERSONALINVITESWINDOW_DECLINESELECTED, count=count), not (count == 0 or self._paginator.isInProgress()))
        return

    def _getSecondSortFields(self):
        return (b'createdAt',)

    def _makeHeaders(self):
        return [
         self._packHeaderColumnData(b'clanName', CLANS.CLANPERSONALINVITESWINDOW_TABLE_CLANNAME, 233, CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_TABLE_INVITES_CLANNAME, textAlign=b'left', enabled=True, defaultSortDirection=b'ascending'),
         self._packHeaderColumnData(b'message', b'', 73, CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_TABLE_INVITES_MESSAGE, RES_ICONS.MAPS_ICONS_CLANS_INVITESWINDOW_ICON_STATISTICS_CLAN_INVITE_098, enabled=True),
         self._packHeaderColumnData(b'personalRating', b'', 98, CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_TABLE_INVITES_RATING, RES_ICONS.MAPS_ICONS_STATISTIC_RATING24, enabled=True),
         self._packHeaderColumnData(b'battlesCount', b'', 98, CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_TABLE_INVITES_BATTLESCOUNT, RES_ICONS.MAPS_ICONS_STATISTIC_BATTLES24, enabled=True),
         self._packHeaderColumnData(b'wins', b'', 98, CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_TABLE_INVITES_WINS, RES_ICONS.MAPS_ICONS_STATISTIC_WINS24, enabled=True),
         self._packHeaderColumnData(b'awgExp', b'', 98, CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_TABLE_INVITES_AWGEXP, RES_ICONS.MAPS_ICONS_STATISTIC_AVGEXP24, enabled=True),
         self._packHeaderColumnData(b'status', CLANS.CLANPERSONALINVITESWINDOW_TABLE_STATUS, 160, CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_TABLE_INVITES_STATUS, enabled=True),
         self._packHeaderColumnData(b'actions', CLANS.CLANPERSONALINVITESWINDOW_TABLE_ACTIONS, 132, CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_TABLE_REQUESTS_ACTIONS, enabled=False)]

    def _enableRefreshBtn(self, enable, toolTip=None):
        if enable:
            self.as_updateButtonRefreshStateS(True, makeTooltip(body=_ms(toolTip or CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_REFRESHBUTTON_ENABLED)))
        else:
            self.as_updateButtonRefreshStateS(False, makeTooltip(body=_ms(toolTip or CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_REFRESHBUTTON_DISABLED)))
        return


class PersonalInvitesDataProvider(ClanInvitesAbstractDataProvider):
    clansCtrl = dependency.descriptor(IWebController)

    def __init__(self, proxy):
        super(PersonalInvitesDataProvider, self).__init__(proxy)
        self._selectedCount = 0
        return

    def selectedCount(self):
        return self._selectedCount

    def areAllSelected(self):
        for item in self.collection:
            if self._isDataRow(item) and not item[b'checked']:
                return False

        return True

    def setSelectAll(self, select):
        self._selectedCount = 0
        for item in self.collection:
            if self._isDataRow(item) and item[b'enabled']:
                item[b'checked'] = select
                self.getExtraData(item[b'dbID'])[b'checked'] = select
                if select:
                    self._selectedCount += 1

        self.refresh()
        return

    def setCheckedID(self, dbID, checked):
        self.getVOByDbID(dbID)[b'checked'] = checked
        self.getExtraData(dbID)[b'checked'] = checked
        self._selectedCount += 1 if checked else -1
        self.refresh()
        return

    def getCheckedIDs(self):
        return [item[b'dbID'] for item in self.collection if self._isDataRow(item) and item[b'checked']]

    def getStatusByDbID(self, dbID):
        return self.getExtraData(dbID)[b'status']

    def buildList(self, cache, showMoreButton=False):
        super(PersonalInvitesDataProvider, self).buildList(cache, showMoreButton)
        self._invalidateSelectedCount()
        return

    def refreshItems(self, items):
        super(PersonalInvitesDataProvider, self).refreshItems(items)
        self._invalidateSelectedCount()
        return

    def invalidateItems(self):
        for item in self.collection:
            if self._isDataRow(item):
                item[b'checked'] = self.getExtraData(item[b'dbID'])[b'checked']
                item[b'actions'] = self.__buildActionsSection(self.getStatusByDbID(item[b'dbID']))

        return

    def _invalidateSelectedCount(self):
        self._selectedCount = 0
        for item in self.collection:
            if self._isDataRow(item) and item[b'checked']:
                self._selectedCount += 1

        return

    def _buildExtraData(self, item, prevExtra):
        checked = False
        if item.getStatus() == CLAN_INVITE_STATES.ACTIVE and prevExtra:
            checked = prevExtra.get(b'checked', False)
        return {b'status': (item.getStatus()), 
           b'checked': checked}

    def _makeVO(self, item, extraData):
        isChecked = extraData[b'checked']
        status = item.getStatus()
        outcome = {b'dbID': (item.getDbID()), 
           b'checked': isChecked, 
           b'clanVO': {b'fullName': (formatField(getter=item.getClanFullName)), 
                       b'clanName': (formatField(getter=item.getClanName)), 
                       b'clanAbbrev': (formatField(getter=item.getClanAbbrev)), 
                       b'dbID': (item.getClanDbID()), 
                       b'isActive': (item.isClanActive())}, 
           b'personalRating': (formatField(getter=item.getPersonalRating, formatter=backport.getIntegralFormat)), 
           b'battlesCount': (formatField(getter=item.getBattlesCount, formatter=backport.getIntegralFormat)), 
           b'wins': (formatField(getter=item.getBattleXpAvg, formatter=(lambda value: backport.getNiceNumberFormat(value) + b'%'))), 
           b'awgExp': (formatField(getter=item.getBattlesPerformanceAvg, formatter=backport.getIntegralFormat)), 
           b'status': {b'text': (self._makeInviteStateString(item)), 
                       b'tooltip': (self._makeTooltip(body=self._makeRequestTooltip(status=item.getStatus(), user=formatField(getter=item.getSenderName), date=formatField(getter=item.getUpdatedAt, formatter=formatters.formatShortDateShortTimeString))))}, 
           b'enabled': (status in (CLAN_INVITE_STATES.ACTIVE, CLAN_INVITE_STATES.ERROR)), 
           b'canShowContextMenu': True, 
           b'messageTooltip': (self._makeTooltip(body=escape(item.getComment()) if isValueAvailable(getter=item.getComment) else str())), 
           b'actions': (self.__buildActionsSection(item.getStatus()))}
        return outcome

    def _makeRequestTooltip(self, status, date, user=None):
        if status == CLAN_INVITE_STATES.ACCEPTED:
            return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_INVITEACCEPTED)), text_styles.main(date), text_styles.main(b''), text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_BYUSER)), text_styles.stats(user))
        if status in (CLAN_INVITE_STATES.DECLINED, CLAN_INVITE_STATES.DECLINED_RESENT):
            return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_INVITEDECLINED)), text_styles.main(date), text_styles.main(b''), text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_BYUSER)), text_styles.stats(user))
        if status in (CLAN_INVITE_STATES.ACTIVE, CLAN_INVITE_STATES.EXPIRED, CLAN_INVITE_STATES.EXPIRED_RESENT):
            return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_INVITESENT)), text_styles.main(date), text_styles.main(b''), text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_SENDER)), text_styles.stats(user))
        return

    def __buildActionsSection(self, inviteStatus):
        acceptButtonEnabled = False
        declineButtonEnabled = False
        acceptButtonVisible = False
        declineButtonVisible = False
        acceptButtonTooltip = None
        clanHasFreeSpaces = True
        clanAcceptJoinRequests = True
        if inviteStatus == CLAN_INVITE_STATES.ACTIVE:
            declineButtonVisible = True
            acceptButtonVisible = True
            declineButtonEnabled = self.isActionsAllowed()
            if not clanAcceptJoinRequests:
                acceptButtonTooltip = CLANS.CLANINVITESWINDOW_HEADER_TOOLTIPS_RECRUITEMENTSTOPPED
            elif not clanHasFreeSpaces:
                acceptButtonTooltip = CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_CANTSENDINVITE_BODY
            else:
                accProfile = self.clansCtrl.getAccountProfile()
                if accProfile.isInClanEnterCooldown():
                    acceptButtonTooltip = _ms(text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANPERSONALINVITESWINDOW_TOOLTIPS_TABLE_CANTACCEPTREQUESTDUETOCD_BODY)), text_styles.main(formatters.formatShortDateShortTimeString(accProfile.getClanCooldownTill()))))
                else:
                    acceptButtonEnabled = self.isActionsAllowed()
        return {b'acceptButtonEnabled': acceptButtonEnabled, 
           b'declineButtonEnabled': declineButtonEnabled, 
           b'acceptButtonVisible': acceptButtonVisible, 
           b'declineButtonVisible': declineButtonVisible, 
           b'acceptButtonTooltip': (self._makeTooltip(body=_ms(acceptButtonTooltip)))}
