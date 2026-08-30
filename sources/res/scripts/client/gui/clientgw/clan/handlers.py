from functools import partial
from gui.clans import items
from gui.clientgw.base.handlers import RequestHandlers
from gui.clientgw.clan.contexts import GetFrontsCtx, ClanRatingsCtx, AccountClanRatingsCtx
from gui.clientgw.settings import WebRequestDataType

class ClanRequestHandlers(RequestHandlers):

    def __init__(self, requester, clientgwController):
        super(ClanRequestHandlers, self).__init__(requester)
        self.__clientgwController = clientgwController
        return

    def get(self):
        handlers = {(WebRequestDataType.CLAN_INFO): (self.__getClanInfo), 
           (WebRequestDataType.CLAN_RATINGS): (self.__getClanRatings), 
           (WebRequestDataType.CLAN_GLOBAL_MAP_STATS): (self.__getClanGlobalMapStats), 
           (WebRequestDataType.CLAN_ACCOUNTS): (self.__getClanAccounts), 
           (WebRequestDataType.STRONGHOLD_INFO): (self.__getStrongholdInfo), 
           (WebRequestDataType.ACCOUNT_APPLICATIONS_COUNT): (self.__accountApplications), 
           (WebRequestDataType.CLAN_INVITATIONS_COUNT): (self.__getClanInvitations), 
           (WebRequestDataType.CLAN_MEMBERS): (self.__getClanMembers), 
           (WebRequestDataType.CLAN_MEMBERS_RATING): (self.__getClanMembersRating), 
           (WebRequestDataType.CLAN_PROVINCES): (self.__getProvinces), 
           (WebRequestDataType.SEARCH_CLANS): (self.__searchClans), 
           (WebRequestDataType.GET_RECOMMENDED_CLANS): (self.__getRecommendedClans), 
           (WebRequestDataType.CLAN_APPLICATIONS): (self.__getClanApplications), 
           (WebRequestDataType.CLAN_INVITES): (self.__getClanInvites), 
           (WebRequestDataType.ACCOUNT_INVITES): (self.__getAccountInvites), 
           (WebRequestDataType.ACCEPT_APPLICATION): (self.__acceptApplication), 
           (WebRequestDataType.ACCEPT_INVITE): (self.__acceptInvite), 
           (WebRequestDataType.CREATE_APPLICATIONS): (self.__createApplications), 
           (WebRequestDataType.CREATE_INVITES): (self.__createInvites), 
           (WebRequestDataType.DECLINE_APPLICATION): (self.__declineApplication), 
           (WebRequestDataType.DECLINE_INVITE): (self.__declineInvite), 
           (WebRequestDataType.DECLINE_INVITES): (self.__declineInvites), 
           (WebRequestDataType.GET_ACCOUNT_APPLICATIONS): (self.__getAccountApplications), 
           (WebRequestDataType.CLANS_INFO): (self.__getClansInfo), 
           (WebRequestDataType.CLAN_FAVOURITE_ATTRS): (self.__getClanFavoriteAttributes), 
           (WebRequestDataType.STRONGHOLD_EVENT_SETTINGS): (self.__getStrongholdEventSettings), 
           (WebRequestDataType.STRONGHOLD_EVENT_CLAN_INFO): (self.__getStrongholdEventClanInfo)}
        return handlers

    def __getClanInfo(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'get_clans_info'), (ctx.getClanID(),), fields=ctx.getFields())

    def __getClansInfo(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'get_clans_info'), ctx.getClanIDs(), fields=ctx.getFields())

    def __getClanRatings(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, (b'ratings', b'get_clans_ratings'), ctx.getClanIDs())

    def __getClanGlobalMapStats(self, ctx, callback=None):
        return self.__doClanRequest(ctx, callback, (b'global_map', b'get_statistics'))

    def __getProvinces(self, ctx, callback=None):

        def __onProvincesReceived(response):
            if response.isSuccess() and response.data:
                frontsCtx = GetFrontsCtx([v[b'front_name'] for v in response.data])

                def __onFrontsReceived(frontsResponse):
                    if frontsResponse.isSuccess():
                        fronts = frontsCtx.getDataObj(frontsResponse.data)
                    else:
                        fronts = {}
                    for province in response.data:
                        province[b'frontInfo'] = fronts.get(province[b'front_name'], frontsCtx.getDefDataObj())

                    callback(response)
                    return

                self.__getGMFronts(frontsCtx, __onFrontsReceived)
            else:
                callback(response)
            return

        return self.__doClanRequest(ctx, __onProvincesReceived, (b'global_map', b'get_provinces'))

    def __getGMFronts(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, (b'global_map', b'get_fronts_info'), ctx.getProvincesIDs())

    def __getClanAccounts(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'get_accounts_clans'), ctx.getAccountsIDs())

    def __getClanMembers(self, ctx, callback=None):

        def _onMembersReceived(membersResponse):
            if membersResponse.isSuccess():
                ctx = AccountClanRatingsCtx([v[b'account_id'] for v in membersResponse.data])

                def _onRatingsReceived(ratingsResponse):
                    if ratingsResponse.isSuccess():
                        ratings = ctx.getDataObj(ratingsResponse.data)
                    else:
                        ratings = {}
                    for m in membersResponse.data:
                        m[b'ratings'] = ratings.get(m[b'account_id'], items.AccountClanRatingsData(account_id=m[b'account_id']))

                    callback(membersResponse)
                    return

                self.__getClanMembersRating(ctx, _onRatingsReceived)
            else:
                callback(membersResponse)
            return

        return self.__doClanRequest(ctx, _onMembersReceived, (b'clans', b'get_clan_members'))

    def __getClanMembersRating(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, (b'exporter', b'get_accounts_info'), ctx.getAccountsIDs())

    def __getStrongholdInfo(self, ctx, callback=None):
        return self.__doClanRequest(ctx, callback, (b'strongholds', b'get_info'))

    def __getStrongholdEventSettings(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, (b'wgsh', b'get_event_settings'))

    def __getStrongholdEventClanInfo(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, (b'wgsh', b'get_event_clan_info'))

    def __accountApplications(self, ctx, callback):
        return self.__doTotalRequest(ctx, callback, (b'clans', b'get_account_applications_count_since'))

    def __getClanInvitations(self, ctx, callback):
        return self.__doTotalRequest(ctx, callback, (b'clans', b'get_clan_invites_count_since'))

    def __searchClans(self, ctx, callback):
        limits = self.__clientgwController.getLimits()
        isValid, reason = limits.canSearchClans(ctx.getSearchCriteria())
        if not isValid:
            return self.__doFail(ctx, reason, callback)
        return self._requester.doRequestEx(ctx, partial(self._onClansReceived, callback=callback), (b'clans', b'search_clans'), search=ctx.getSearchCriteria(), get_total_count=ctx.isGetTotalCount(), fields=ctx.getFields(), offset=ctx.getOffset(), limit=ctx.getLimit())

    def __getRecommendedClans(self, ctx, callback):
        return self._requester.doRequestEx(ctx, partial(self._onClansReceived, callback=callback), (b'clans', b'get_recommended_clans'), get_total_count=ctx.isGetTotalCount(), fields=ctx.getFields(), offset=ctx.getOffset(), limit=ctx.getLimit())

    def __getClanApplications(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'get_clan_applications'), clan_id=ctx.getClanDbID(), fields=ctx.getFields(), statuses=ctx.getStatuses(), offset=ctx.getOffset(), limit=ctx.getLimit(), get_total_count=ctx.isGetTotalCount())

    def __getClanInvites(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'get_clan_invites'), clan_id=ctx.getClanDbID(), fields=ctx.getFields(), statuses=ctx.getStatuses(), offset=ctx.getOffset(), limit=ctx.getLimit(), get_total_count=ctx.isGetTotalCount())

    def __getAccountInvites(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'get_account_invites'), fields=ctx.getFields(), statuses=ctx.getStatuses(), offset=ctx.getOffset(), limit=ctx.getLimit(), get_total_count=ctx.isGetTotalCount())

    def __getAccountApplications(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'get_account_applications'), fields=ctx.getFields(), statuses=ctx.getStatuses(), offset=ctx.getOffset(), limit=ctx.getLimit(), get_total_count=ctx.isGetTotalCount())

    def __doTotalRequest(self, ctx, callback, methodName):
        return self._requester.doRequestEx(ctx, callback, methodName, ctx.getID())

    def __doClanRequest(self, ctx, callback, methodName):
        return self._requester.doRequestEx(ctx, callback, methodName, ctx.getClanID())

    def __acceptApplication(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'accept_application'), application_id=ctx.getApplicationDbID())

    def __acceptInvite(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'accept_invite'), invite_id=ctx.getInviteDbID())

    def __createApplications(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'create_applications'), clan_ids=ctx.getClanDbIDs(), comment=ctx.getComment())

    def __createInvites(self, ctx, callback):
        limits = self.__clientgwController.getLimits()
        isValid, reason = limits.canSendInvite(self.__clientgwController.getClanDossier(ctx.getClanDbID()))
        if not isValid:
            return self.__doFail(ctx, reason, callback)
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'create_invites'), clan_id=ctx.getClanDbID(), account_ids=ctx.getAccountDbIDs(), comment=ctx.getComment())

    def __declineApplication(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'decline_application'), application_id=ctx.getApplicationDbID())

    def __declineInvite(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'decline_invite'), invite_id=ctx.getInviteDbID())

    def __declineInvites(self, ctx, callback):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'bulk_decline_invites'), invite_ids=ctx.getInviteDbIDs())

    def __getClanFavoriteAttributes(self, ctx, callback=None):
        return self._requester.doRequestEx(ctx, callback, (b'clans', b'get_clan_favorite_attributes'), ctx.getClanID())

    def _onClansReceived(self, clansResponse, callback):
        if clansResponse.isSuccess() and clansResponse.data and clansResponse.data[b'items']:
            dataRef = clansResponse.data[b'items']
            clanIDs = [item[b'clan_id'] for item in dataRef]
            clanRatingsCtx = ClanRatingsCtx(clanIDs)

            def _onRatingsReceived(ratingsResponse):
                if ratingsResponse.isSuccess():
                    ratings = clanRatingsCtx.getDataObj(ratingsResponse.data)
                    ratings = dict((item.getClanDbID(), item) for item in ratings)
                    for clan in dataRef:
                        clan[b'clan_ratings_data'] = ratings.get(clan[b'clan_id'], items.ClanRatingsData())

                else:
                    for clan in dataRef:
                        clan[b'clan_ratings_data'] = items.ClanRatingsData()

                callback(clansResponse)
                return

            self.__getClanRatings(clanRatingsCtx, _onRatingsReceived)
        else:
            callback(clansResponse)
        return

    def __doFail(self, ctx, reason, callback):
        self._requester._stopProcessing(ctx, reason, callback)
        return
