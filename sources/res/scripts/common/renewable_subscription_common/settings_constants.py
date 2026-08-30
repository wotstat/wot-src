from __future__ import absolute_import
from enum import Enum
RS_PDATA_KEY = b'renewableSub'
RS_EXPIRATION_TIME = b'expiry'
RS_BADGES = b'badges'
RS_TIER = b'tier'
PRO_BOOST_PDATA_KEY = b'wotPlusProBoost'
IDLE_CREW_XP_PDATA_KEY = b'idleCrewXP'
RS_SR_BACKGROUND = b'serviceRecordBackground'
RS_SR_RIBBON = b'serviceRecordRibbon'
IDLE_CREW_VEH_INV_ID = b'vehInvID'
LAST_XP_UPDATE_TIMESTAMP = b'lastXPUpdate'
PASSIVE_XP_CURRENCY = b'currency'
ISSUED_XP_CACHE = b'xpCache'
PRO_BOOSTED_VEHICLE = b'vehInvID'
PRO_BOOST_ACTIVATION_TIME = b'activationTime'
CLEAR_PRO_BOOST_VEHICLE_ID = None
PASSIVE_XP_ENTITLEMENT = b'subscription_passive_xp'
PASSIVE_XP_SECONDS = b'passive_xp_seconds'
WOTP_REQUESTER_NAME = b'wotPlus'
SUBSCRIPTION_DURATION_LENGTH = 2592000
PRO_THRESHOLD_DAYS = 270
DEFAULT_DEMOUNT_ACTION = 0
WOT_PLUS_DEMOUNT_ACTION = 1

class WotPlusState(Enum):
    INACTIVE = 0
    ACTIVE = 1
    CANCELLED = 2


class OptionalDevicesUsageConst(object):
    REMOVE = b'remove'
    UPDATE = b'update'
    COPY = b'copy'


class WotPlusTier(object):
    NONE = 0
    CORE = 1
    PRO = 2
    ALL = (
     CORE, PRO)
