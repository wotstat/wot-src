import logging, json
from gui.Scaleform.daapi.view.lobby.referral_program.referral_program_helpers import isReferralProgramEnabled
from gui.clientgw.promo_screens.parsers import PromoDataParser
from gui.referral_program import ScoresLimitReachedError
from gui.notify_center import proxy_data
from gui.notify_center.errors import ParseError
from gui.notify_center.notify_center_helpers import parseSize
from gui.notify_center.xml.shared_parsers import ParsersCollection, SectionParser
from helpers import dependency
from skeletons.gui.game_control import IReferralProgramController
_logger = logging.getLogger(__name__)

class _ClanApplicationParser(SectionParser):

    def getTagName(self):
        return b'clan_application_received'

    def parse(self, section, parentSection=None):
        return proxy_data.ClanApplicationItem(section.readInt64(b'account_id'), section.readInt64(b'application_id'), section.readInt(b'active_applications_count'))


class _ClanAppActionParser(SectionParser):

    def parse(self, section, parentSection=None):
        return self._getItemClass()(section.readInt64(b'account_id'), section.readInt64(b'application_id'))

    def _getItemClass(self):
        raise NotImplementedError
        return


class _ClanAppAcceptedActionParser(_ClanAppActionParser):

    def getTagName(self):
        return b'clan_application_accepted_for_members'

    def _getItemClass(self):
        return proxy_data.ClanAppAcceptedActionItem


class _ClanAppDeclinedActionParser(_ClanAppActionParser):

    def getTagName(self):
        return b'clan_application_declined_for_members'

    def _getItemClass(self):
        return proxy_data.ClanAppDeclinedActionItem


class _ClanInviteParser(SectionParser):

    def getTagName(self):
        return b'clan_invite_received'

    def parse(self, section, parentSection=None):
        return proxy_data.ClanInviteItem(section.readInt(b'invite_id'), section.readInt64(b'clan_id'), self._readString(b'clan_name', section), self._readString(b'clan_tag', section), section.readInt(b'active_invites_count'))


class _ClanPersonalAppParser(SectionParser):

    def parse(self, section, parentSection=None):
        return self._createItem(section.readInt64(b'clan_id'), self._readString(b'clan_name', section), self._readString(b'clan_tag', section), section.readInt64(b'application_id'))

    def _createItem(self, cId, cName, cTag, appId):
        raise NotImplementedError
        return


class _ClanAppAcceptedParser(_ClanPersonalAppParser):

    def getTagName(self):
        return b'clan_application_accepted'

    def _createItem(self, cId, cName, cTag, appId):
        return proxy_data.ClanAppAcceptedItem(cId, cName, cTag, appId)


class _ClanAppDeclinedParser(_ClanPersonalAppParser):

    def getTagName(self):
        return b'clan_application_declined'

    def _createItem(self, cId, cName, cTag, appId):
        return proxy_data.ClanAppDeclinedItem(cId, cName, cTag, appId)


class _ClanInviteActionParser(SectionParser):

    def parse(self, section, parentSection=None):
        return self._createItem(section.readInt64(b'account_id'), section.readInt(b'invite_id'))

    def _createItem(self, account_id, invite_id):
        raise NotImplementedError
        return


class _ClanInviteAcceptedParser(_ClanInviteActionParser):

    def getTagName(self):
        return b'clan_invite_accepted'

    def _createItem(self, account_id, invite_id):
        return proxy_data.ClanInviteAcceptedItem(account_id, invite_id)


class _ClanInviteDeclinedParser(_ClanInviteActionParser):

    def getTagName(self):
        return b'clan_invite_declined'

    def _createItem(self, account_id, invite_id):
        return proxy_data.ClanInviteDeclinedItem(account_id, invite_id)


class _ClanInvitesCreatedParser(SectionParser):

    def getTagName(self):
        return b'clan_invites_created'

    def parse(self, section, parentSection=None):
        return proxy_data.ClanInvitesCreatedItem(self.__getItems(b'account_ids', section), self.__getItems(b'invite_ids', section))

    def __getItems(self, sectionName, section):
        s = self._readString(sectionName, section)
        itemsList = s.split(b',')
        return tuple(long(itemsList[i].strip()) for i in xrange(len(itemsList)))


class _ShowPromoParser(SectionParser):

    def getTagName(self):
        return b'show_promo_teaser'

    def parse(self, section, parentSection=None):
        data = dict(section)
        data[b'data'] = dict(section[b'data'])
        return proxy_data.ShowTeaserItem(PromoDataParser.parseXML(section))


class _ShowInBrowserParser(SectionParser):

    def getTagName(self):
        return b'show_in_browser'

    def parse(self, section, parentSection=None):
        url = section.readString(b'url')
        if not url:
            _logger.error(b'NotifyCenter show_in_browser item has no URL')
            return
        size = parseSize(section.readString(b'size'))
        title = section.readString(b'title')
        titleKey = section.readString(b'title_key')
        showRefresh = section.readBool(b'show_refresh')
        webClientHandler = section.readString(b'web_client_handler')
        isSolidBorder = section.readBool(b'is_solid_border')
        return proxy_data.ShowInBrowserItem(url, size, title, showRefresh, webClientHandler, titleKey=titleKey, isSolidBorder=isSolidBorder)


class _ProxyDataItemsParser(ParsersCollection):

    def getTagName(self):
        return b'proxy_data'

    def parse(self, section, parentSection=None):
        items = []
        for item in super(_ProxyDataItemsParser, self).parse(section):
            if item is not None:
                items.append(item)

        return proxy_data.ProxyDataHolder(items)


class _ReferralBubbleParser(SectionParser):

    def getTagName(self):
        return b'update_referral_bubble'

    def parse(self, _, parentSection=None):
        return proxy_data.UpdateRefferalBubbleItem()


class _SubscriptionStateParser(SectionParser):

    def getTagName(self):
        return b'update_subscription_state'

    def parse(self, _, parentSection=None):
        return proxy_data.UpdateSubscriptionStateItem()


class _ReferralProgramEnabledChecker(SectionParser):

    def getTagName(self):
        return b'referral_program_enabled'

    def parse(self, section, parentSection=None):
        isCurrentlyEnabled = isReferralProgramEnabled()
        value = section.asBool
        if value != isCurrentlyEnabled:
            raise ParseError((b'Referral Program is {}').format(b'enabled' if isCurrentlyEnabled else b'disabled'))
        return


class _ReferralProgramPointsTypeChecker(SectionParser):

    def getTagName(self):
        return b'is_active_point_type'

    def parse(self, section, parentSection=None):
        return


class _ReferralProgramPGBFullChecker(SectionParser):
    __referralProgramController = dependency.descriptor(IReferralProgramController)

    def getTagName(self):
        return b'referral_program_pgb_full'

    def parse(self, section, parentSection=None):
        isActivePointType = parentSection.readBool(_ReferralProgramPointsTypeChecker().getTagName())
        if isActivePointType:
            return
        isCurrentlyFull = self.__referralProgramController.isScoresLimitReached()
        value = section.asBool
        if value != isCurrentlyFull:
            raise ScoresLimitReachedError((b'Referral Program PGB is {}').format(b'full' if isCurrentlyFull else b'not full'))
        return


class _CheckClientStateParser(ParsersCollection):

    def __init__(self):
        super(_CheckClientStateParser, self).__init__((
         _ReferralProgramEnabledChecker(),
         _ReferralProgramPGBFullChecker(),
         _ReferralProgramPointsTypeChecker()))
        return

    def parse(self, section, parentSection=None):
        for _ in super(_CheckClientStateParser, self).parse(section):
            pass

        return

    def getTagName(self):
        return b'check_client_state'


class _ClanNotificationParser(SectionParser):

    def getTagName(self):
        return b'update_clan_news_counter'

    def parse(self, section, parentSection=None):
        alias = section.readString(b'alias')
        value = section.readInt(b'count', 0)
        isIncrement = section.readBool(b'isIncrement', True)
        if alias:
            return proxy_data.UpdateClanNotificationItem(alias, value, isIncrement)
        _logger.warning(b'NotifyCenter update_clan_news_counter item has no alias')
        return


class _BecomeRecruiterParser(SectionParser):

    def getTagName(self):
        return b'become_recruiter'

    def parse(self, _, parentSection=None):
        return proxy_data.BecomeRecruiterItem()


class _ShowReferralWindowParser(SectionParser):

    def getTagName(self):
        return b'show_referral_window'

    def parse(self, section, parentSection=None):
        relativeUrl = section.readString(b'relative_url')
        if not relativeUrl:
            _logger.warning(b'NotifyCenter show_referral_window item has no relative_url')
        return proxy_data.ShowReferralWindowItem(relativeUrl)


class _PaymentMethodChangeParser(SectionParser):
    _OPERATION_NAME = b''

    def getTagName(self):
        raise NotImplementedError
        return

    def parse(self, section, parentSection=None):
        method = section.readString(b'method')
        if not method:
            _logger.error(b'NotifyCenter %s item has no method', self.getTagName())
        cdnUrl = section.readString(b'imageUrl')
        if not cdnUrl:
            _logger.warning(b'NotifyCenter %s item has no imageUrl', self.getTagName())
        return proxy_data.PaymentMethodChangeItem(self._OPERATION_NAME, method, cdnUrl)


class _PaymentMethodLinkParser(_PaymentMethodChangeParser):
    _OPERATION_NAME = b'link'

    def getTagName(self):
        return b'payment_method_link'


class _PaymentMethodUnlinkParser(_PaymentMethodChangeParser):
    _OPERATION_NAME = b'unlink'

    def getTagName(self):
        return b'payment_method_unlink'


class _MapboxSurveyAvailableParser(SectionParser):

    def getTagName(self):
        return b'mapbox_survey_available'

    def parse(self, section, parentSection=None):
        return proxy_data.ShowMapboxSurveyAvailableMessage(section.readString(b'geometry_name'))


class _MapboxEventStartedParser(SectionParser):

    def getTagName(self):
        return b'mapbox_event_started'

    def parse(self, _, parentSection=None):
        return proxy_data.ShowMapboxEventStartedMessage()


class _MapboxEventEndedParser(SectionParser):

    def getTagName(self):
        return b'mapbox_event_ended'

    def parse(self, _, parentSection=None):
        return proxy_data.ShowMapboxEventEndedMessage()


class _MapboxRewardReceivedParser(SectionParser):

    def getTagName(self):
        return b'mapbox_reward_received'

    def parse(self, section, parentSection=None):
        return proxy_data.ShowMapboxRewardReceivedMessage({b'rewards': (json.loads(section[b'rewards'].asString)), 
           b'battles': (section[b'battles'].asInt), 
           b'isFinal': (section.readBool(b'is_last_reward'))})


class _IntegratedAuctionRateErrorParser(SectionParser):

    def getTagName(self):
        return b'auction_rate_error'

    def parse(self, _, parentSection=None):
        return proxy_data.ShowAuctionRateErrorMessage()


class _IntegratedAuctionBelowCompetitiveRateParser(SectionParser):

    def getTagName(self):
        return b'auction_below_competitive_rate'

    def parse(self, _, parentSection=None):
        return proxy_data.ShowAuctionBelowCompetitiveRateMessage()


class _IntegratedAuctionLostRateParser(SectionParser):

    def getTagName(self):
        return b'auction_lost_rate'

    def parse(self, section, parentSection=None):
        messageData = json.loads(section[b'data'].asString)
        messageData.setdefault(b'result', b'lost')
        return proxy_data.ShowAuctionResultMessage(messageData=messageData)


class _IntegratedAuctionResultParser(SectionParser):

    def getTagName(self):
        return b'auction_result'

    def parse(self, section, parentSection=None):
        messageData = json.loads(section[b'data'].asString)
        return proxy_data.ShowAuctionResultMessage(messageData=messageData)


class ProxyDataItemParser_v2(_ProxyDataItemsParser):

    def __init__(self):
        super(ProxyDataItemParser_v2, self).__init__((
         _CheckClientStateParser(),
         _ClanApplicationParser(),
         _ClanAppAcceptedActionParser(),
         _ClanAppDeclinedActionParser(),
         _ClanInviteParser(),
         _ClanAppDeclinedParser(),
         _ClanAppAcceptedParser(),
         _ClanInvitesCreatedParser(),
         _ClanInviteDeclinedParser(),
         _ClanInviteAcceptedParser(),
         _ShowInBrowserParser(),
         _ShowPromoParser(),
         _ReferralBubbleParser(),
         _BecomeRecruiterParser(),
         _ShowReferralWindowParser(),
         _ClanNotificationParser(),
         _PaymentMethodLinkParser(),
         _PaymentMethodUnlinkParser(),
         _MapboxSurveyAvailableParser(),
         _MapboxEventStartedParser(),
         _MapboxEventEndedParser(),
         _MapboxRewardReceivedParser(),
         _IntegratedAuctionRateErrorParser(),
         _IntegratedAuctionBelowCompetitiveRateParser(),
         _IntegratedAuctionResultParser(),
         _IntegratedAuctionLostRateParser(),
         _SubscriptionStateParser()))
        return
