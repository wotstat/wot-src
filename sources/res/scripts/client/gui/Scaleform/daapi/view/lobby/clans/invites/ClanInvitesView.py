from __future__ import absolute_import
from gui.Scaleform.genConsts.CLANS_ALIASES import CLANS_ALIASES
from gui.Scaleform.locale.CLANS import CLANS
from gui.Scaleform.locale.RES_ICONS import RES_ICONS
from gui.clans import formatters
from gui.clans.data_wrapper.utils import formatField, isValueAvailable
from gui.Scaleform.daapi.view.lobby.clans.invites.ClanInvitesViewWithTable import ClanInvitesAbstractDataProvider
from gui.Scaleform.daapi.view.meta.ClanInvitesViewMeta import ClanInvitesViewMeta
from gui.clans.settings import CLAN_INVITE_STATES
from gui.impl import backport
from gui.shared.formatters import text_styles
from helpers.i18n import makeString as _ms
from debug_utils import LOG_DEBUG

class ClanInvitesView(ClanInvitesViewMeta):

    @property
    def allInvitesPaginator(self):
        return self._getPaginatorByFilterName(CLANS_ALIASES.INVITE_WINDOW_FILTER_ALL)

    @property
    def actualInvitesPaginator(self):
        return self._getPaginatorByFilterName(CLANS_ALIASES.INVITE_WINDOW_FILTER_ACTUAL)

    @property
    def expiredInvitesPaginator(self):
        return self._getPaginatorByFilterName(CLANS_ALIASES.INVITE_WINDOW_FILTER_EXPIRED)

    @property
    def processedInvitesPaginator(self):
        return self._getPaginatorByFilterName(CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED)

    def onClanInvitesCountReceived(self, clanDbID, invitesCount):
        super(ClanInvitesView, self).onClanInvitesCountReceived(clanDbID, invitesCount)
        if self.actualInvitesPaginator.isSynced():
            self._enableRefreshBtn(True)
        return

    def _onAttachedToWindow(self):
        super(ClanInvitesView, self)._onAttachedToWindow()
        self.filterBy(self.currentFilterName)
        return

    def _createSearchDP(self):
        return InviteDataProvider(self)

    def _getViewAlias(self):
        return CLANS_ALIASES.CLAN_PROFILE_INVITES_VIEW_ALIAS

    def _showDummyByFilterName(self, filterName):
        inviteText = _ms(CLANS.CLANINVITESWINDOW_DUMMY_NOINVITES_TEXT, invite=text_styles.main(CLANS.CLANINVITESWINDOW_DUMMY_NOINVITES_INVITE))
        if filterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_ALL:
            self._showDummy(CLANS.CLANINVITESWINDOW_DUMMY_NOINVITES_TITLE, inviteText)
        if filterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_ACTUAL:
            self._showDummy(CLANS.CLANINVITESWINDOW_DUMMY_NOINVITESACTUAL_TITLE, inviteText)
        elif filterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_EXPIRED:
            self._showDummy(CLANS.CLANINVITESWINDOW_DUMMY_NOINVITESEXPIRED_TITLE, inviteText)
        elif filterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED:
            self._showDummy(CLANS.CLANINVITESWINDOW_DUMMY_NOINVITESPROCESSED_TITLE, inviteText)
        else:
            LOG_DEBUG(b'Unexpected behaviour: no dummy for filter', filterName)
            self._showDummy(CLANS.CLANINVITESWINDOW_DUMMY_NOINVITES_TITLE, inviteText)
        return

    def _getDefaultFilterName(self):
        return CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED

    def _getDefaultSortFields(self):
        if self.currentFilterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_ALL:
            return ((b'personalRating', False),)
        if self.currentFilterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_ACTUAL or self.currentFilterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_EXPIRED:
            return ((b'sent', False),)
        if self.currentFilterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED:
            return ((b'status', False),)
        return ((b'status', False),)

    def _getSecondSortFields(self):
        if self.currentFilterName == CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED:
            return (b'updatedAt',)
        return (b'createdAt',)

    def _makeFilters(self):
        return [
         {b'alias': (CLANS_ALIASES.INVITE_WINDOW_FILTER_ALL), 
            b'text': (_ms(CLANS.CLANINVITESWINDOW_FILTERS_ALL, value=self.formatInvitesCount(self.allInvitesPaginator)))},
         {b'alias': (CLANS_ALIASES.INVITE_WINDOW_FILTER_ACTUAL), 
            b'text': (_ms(CLANS.CLANINVITESWINDOW_FILTERS_ACTUAL, value=self.formatInvitesCount(self.actualInvitesPaginator)))},
         {b'alias': (CLANS_ALIASES.INVITE_WINDOW_FILTER_EXPIRED), 
            b'text': (_ms(CLANS.CLANINVITESWINDOW_FILTERS_EXPIRED, value=self.formatInvitesCount(self.expiredInvitesPaginator)))},
         {b'alias': (CLANS_ALIASES.INVITE_WINDOW_FILTER_PROCESSED), 
            b'text': (_ms(CLANS.CLANINVITESWINDOW_FILTERS_HASANSWER, value=self.formatInvitesCount(self.processedInvitesPaginator)))}]

    def _makeHeaders(self):
        return [
         self._packHeaderColumnData(b'userName', CLANS.CLANINVITESWINDOW_TABLE_USERNAME, 225, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_INVITES_USERNAME, textAlign=b'left', defaultSortDirection=b'ascending'),
         self._packHeaderColumnData(b'message', b'', 73, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_INVITES_MESSAGE, RES_ICONS.MAPS_ICONS_CLANS_INVITESWINDOW_ICON_STATISTICS_CLAN_INVITE_098),
         self._packHeaderColumnData(b'personalRating', b'', 98, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_INVITES_PERSONALRATING, RES_ICONS.MAPS_ICONS_STATISTIC_RATING24),
         self._packHeaderColumnData(b'battlesCount', b'', 98, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_INVITES_BATTLESCOUNT, RES_ICONS.MAPS_ICONS_STATISTIC_BATTLES24),
         self._packHeaderColumnData(b'wins', b'', 98, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_INVITES_WINS, RES_ICONS.MAPS_ICONS_STATISTIC_WINS24),
         self._packHeaderColumnData(b'awgExp', b'', 98, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_INVITES_AWGEXP, RES_ICONS.MAPS_ICONS_STATISTIC_AVGEXP24),
         self._packHeaderColumnData(b'status', CLANS.CLANINVITESWINDOW_TABLE_STATUS, 150, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_INVITES_STATUS),
         self._packHeaderColumnData(b'sent', CLANS.CLANINVITESWINDOW_TABLE_SENT, 150, CLANS.CLANINVITESWINDOW_TOOLTIPS_TABLE_INVITES_SENT)]


class InviteDataProvider(ClanInvitesAbstractDataProvider):

    def _makeVO(self, item, extraData):
        return {b'dbID': (item.getDbID()), 
           b'userInfo': {b'userName': (formatField(getter=item.getAccountName)), 
                         b'dbID': (item.getAccountDbID())}, 
           b'personalRating': (formatField(getter=item.getPersonalRating, formatter=backport.getIntegralFormat)), 
           b'battlesCount': (formatField(getter=item.getBattlesCount, formatter=backport.getIntegralFormat)), 
           b'wins': (formatField(getter=item.getBattlesPerformanceAvg, formatter=(lambda value: backport.getNiceNumberFormat(value) + b'%'))), 
           b'awgExp': (formatField(getter=item.getBattleXpAvg, formatter=backport.getIntegralFormat)), 
           b'status': {b'text': (self._makeInviteStateString(item)), 
                       b'tooltip': (self._makeTooltip(body=self._makeRequestTooltip(status=item.getStatus(), user=formatField(getter=item.getSenderName), date=formatField(getter=item.getUpdatedAt, formatter=formatters.formatShortDateShortTimeString))))}, 
           b'canShowContextMenu': True, 
           b'messageTooltip': (self._makeTooltip(body=item.getComment() if isValueAvailable(getter=item.getComment) else str())), 
           b'sent': (formatField(getter=item.getCreatedAt, formatter=formatters.formatShortDateShortTimeString))}

    def _makeRequestTooltip(self, status, date, user=None):
        if status == CLAN_INVITE_STATES.ACCEPTED:
            return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_INVITEACCEPTED)), text_styles.main(date), text_styles.main(b''), text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_BYUSER)), text_styles.stats(user))
        else:
            if status in (CLAN_INVITE_STATES.DECLINED, CLAN_INVITE_STATES.DECLINED_RESENT):
                return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_INVITEDECLINED)), text_styles.main(date), text_styles.main(b''), text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_BYUSER)), text_styles.stats(user))
            if status in (CLAN_INVITE_STATES.ACTIVE, CLAN_INVITE_STATES.EXPIRED, CLAN_INVITE_STATES.EXPIRED_RESENT):
                return text_styles.concatStylesToMultiLine(text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_INVITESENT)), text_styles.main(date), text_styles.main(b''), text_styles.standard(_ms(CLANS.CLANINVITESWINDOW_TOOLTIPS_INVITE_SENDER)), text_styles.stats(user))
            return
