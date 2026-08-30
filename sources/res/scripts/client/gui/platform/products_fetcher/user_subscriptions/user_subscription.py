import logging
from enum import Enum
from typing import Dict
from gui.impl.gen.view_models.views.lobby.page.header.wot_plus_subscription_model import WotPlusPeriodicityEnum
from helpers.time_utils import getTimestampFromISO

class SubscriptionStatus(Enum):
    NEW = b'NEW'
    WAITING_FOR_PURCHASE = b'WAITING_FOR_PURCHASE'
    ACTIVE = b'ACTIVE'
    INACTIVE = b'INACTIVE'
    GDPR_SUSPENDED = b'GDPR_SUSPENDED'
    NEXT_PAYMENT_UNAVAILABLE = b'NEXT_PAYMENT_UNAVAILABLE'


SUBSCRIPTION_CANCEL_STATUSES = [
 SubscriptionStatus.INACTIVE,
 SubscriptionStatus.GDPR_SUSPENDED,
 SubscriptionStatus.NEXT_PAYMENT_UNAVAILABLE]
BILLING_PERIOD_DAYS_MAP = {180: (WotPlusPeriodicityEnum.P6MONTHS), 
   360: (WotPlusPeriodicityEnum.P12MONTHS)}
_logger = logging.getLogger(__name__)

class SubscriptionRequestPlatform(Enum):
    WG_PLATFORM = b'wg_platform'
    STEAM = b'steam'
    UNKNOWN = b'unknown'


class UserSubscription(object):
    __slots__ = (b'subscriptionId', b'productCode', b'status', b'nextBillingTime', b'platform', b'billingPeriod')

    def __init__(self, subscriptionData):
        self.subscriptionId = None
        self.productCode = None
        self.status = None
        self.nextBillingTime = None
        self.platform = SubscriptionRequestPlatform.UNKNOWN
        self.billingPeriod = None
        self.loadFromData(subscriptionData)
        return

    def loadFromData(self, subscriptionData):
        self.subscriptionId = subscriptionData.get(b'subscription_id')
        self.productCode = subscriptionData.get(b'product_code')
        self.status = SubscriptionStatus(subscriptionData.get(b'status'))
        try:
            rawDays = int(subscriptionData.get(b'billing_period', {}).get(b'value'))
            self.billingPeriod = BILLING_PERIOD_DAYS_MAP.get(rawDays)
        except (ValueError, TypeError):
            _logger.warning(b'Unknown billing period in subscription: %s', subscriptionData.get(b'billing_period'))

        try:
            self.nextBillingTime = int(getTimestampFromISO(subscriptionData.get(b'next_billing_time')))
        except (ValueError, TypeError):
            _logger.warning(b'Unknown billing time in subscription: %s', subscriptionData.get(b'next_billing_time'))

        try:
            self.platform = SubscriptionRequestPlatform(subscriptionData.get(b'platform'))
        except ValueError:
            _logger.warning(b'Unknown subscription type in subscription: %s', subscriptionData.get(b'platform'))

        return

    def __str__(self):
        return (b'subscriptionId: {}, productCode: {}, status: {}, nextBillingTime: {}, billingPeriod: {}, platform: {}').format(self.subscriptionId, self.productCode, self.status, self.nextBillingTime, self.billingPeriod, self.platform)
