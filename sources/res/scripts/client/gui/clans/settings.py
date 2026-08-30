import re
from collections import namedtuple
from constants import CLAN_MEMBER_FLAGS
from shared_utils import CONST_CONTAINER
DEFAULT_COOLDOWN = 1.0
REQUEST_TIMEOUT = 60.0
SEND_INVITES_COOLDOWN = 5.0
ACCEPT_INVITES_COOLDOWN = 2.0
DECLINE_INVITES_COOLDOWN = 2.0
MAX_ACCOUNT_APPLICATIONS_COUNT = 100
MAX_CLAN_INVITES_COUNT = 100
MAX_CLAN_MEMBERS_COUNT = 100
COUNT_THRESHOLD = 2000
PERSONAL_INVITES_COUNT_THRESHOLD = 500
DATA_UNAVAILABLE_PLACEHOLDER = b'--'
ACTIVE_INVITE_LIFE_TIME = 259200
INVITE_LIMITS_LIFE_TIME = 300
CLAN_DOSSIER_LIFE_TIME = 3600
DEFAULT_EMBLEM_PATH = b'gui/maps/icons/clans'
DEFAULT_EMBLEM_NAME_PREFIX = b'default_clan_icon'
NO_EMBLEM_NAME_PREFIX = b'no_clan_icon'
CLAN_MEMBERS = {(CLAN_MEMBER_FLAGS.LEADER): b'leader', 
   (CLAN_MEMBER_FLAGS.VICE_LEADER): b'vice_leader', 
   (CLAN_MEMBER_FLAGS.RECRUITER): b'recruiter', 
   (CLAN_MEMBER_FLAGS.TREASURER): b'treasurer', 
   (CLAN_MEMBER_FLAGS.DIPLOMAT): b'diplomat', 
   (CLAN_MEMBER_FLAGS.COMMANDER): b'commander', 
   (CLAN_MEMBER_FLAGS.PRIVATE): b'private', 
   (CLAN_MEMBER_FLAGS.RECRUIT): b'recruit', 
   (CLAN_MEMBER_FLAGS.STAFF): b'staff', 
   (CLAN_MEMBER_FLAGS.JUNIOR): b'junior', 
   (CLAN_MEMBER_FLAGS.RESERVIST): b'reservist'}
_RE_SEARCH_CLANS = re.compile(b'^(\\[|\\])*[\\S]{2,}', re.IGNORECASE)
CLANS_SELECTABLE_REWARD_PREFIX = b'offer:clans:'

def isValidPattern(pattern):
    return pattern and _RE_SEARCH_CLANS.match(pattern)


class LOGIN_STATE(CONST_CONTAINER):
    LOGGED_OFF = 0
    LOGGING_IN = 1
    LOGGED_ON = 2

    @classmethod
    def canDoLogin(cls, state):
        return state == cls.LOGGED_OFF


class CLAN_INVITE_STATES(CONST_CONTAINER):
    ACTIVE = b'active'
    DECLINED = b'declined'
    DECLINED_RESENT = b'declined_resent'
    ACCEPTED = b'accepted'
    EXPIRED = b'expired'
    ERROR = b'error'
    DELETED = b'deleted'
    EXPIRED_RESENT = b'expired_resent'
    PROCESSED = (
     ACCEPTED, DECLINED)
    ALL = (ACTIVE, DECLINED, ACCEPTED, EXPIRED)

    @classmethod
    def isActive(cls, status):
        return status == cls.ACTIVE


class CLAN_APPLICATION_STATES(CONST_CONTAINER):
    ACTIVE = b'active'
    DECLINED = b'declined'
    ACCEPTED = b'accepted'
    ALL = (
     ACTIVE, DECLINED, ACCEPTED)


CLAN_INVITE_STATES_SORT_RULES = {(CLAN_INVITE_STATES.ACTIVE): 5, 
   (CLAN_INVITE_STATES.ACCEPTED): 4, 
   (CLAN_INVITE_STATES.DECLINED): 3, 
   (CLAN_INVITE_STATES.DECLINED_RESENT): 3, 
   (CLAN_INVITE_STATES.EXPIRED): 2, 
   (CLAN_INVITE_STATES.EXPIRED_RESENT): 2, 
   (CLAN_INVITE_STATES.ERROR): 1, 
   (CLAN_INVITE_STATES.DELETED): 0}

class CLIENT_CLAN_RESTRICTIONS(CONST_CONTAINER):
    NO_RESTRICTIONS = b'NO_RESTRICTIONS'
    DEFAULT = b'HAVE_NO_RIGHTS'
    OWN_CLAN = b'OWN_CLAN'
    RESYNCHRONIZE = b'RESYNCHRONIZE'
    ALREADY_IN_CLAN = b'ALREADY_IN_CLAN'
    FORBIDDEN_ACCOUNT_TYPE = b'FORBIDDEN_ACCOUNT_TYPE'
    CLAN_APPLICATION_ALREADY_SENT = b'CLAN_APPLICATION_ALREADY_SENT'
    CLAN_INVITE_ALREADY_RECEIVED = b'CLAN_INVITE_ALREADY_RECEIVED'
    SENT_INVITES_LIMIT_REACHED = b'SENT_INVITES_LIMIT_REACHED'
    CLAN_SEND_INVITES_LIMIT_REACHED = b'CLAN_SEND_INVITES_LIMIT_REACHED'
    CLAN_CONSCRIPTION_CLOSED = b'CLAN_CONSCRIPTION_CLOSED'
    CANT_SEE_TREASURY = b'HAVE_NO_RIGHTS_TO_SEE_TREASURY'
    CANT_HANDLE_INVITES = b'CANT_HANDLE_INVITES'
    CANT_SEND_INVITES = b'HAVE_NO_RIGHTS_TO_SEND_INVITES'
    SEARCH_PATTERN_INVALID = b'SEARCH_PATTERN_INVALID'
    CLAN_IS_FULL = b'CLAN_IS_FULL'
    CLAN_ENTER_COOLDOWN = b'CLAN_ENTER_COOLDOWN'


_RestrResult = namedtuple(b'_RestrResult', b'success reason')

def error(reason):
    return _RestrResult(False, reason)


def success():
    return _RestrResult(True, CLIENT_CLAN_RESTRICTIONS.NO_RESTRICTIONS)


def getDefaultEmblem16x16():
    return _getDefaultEmblemPath(16)


def getDefaultEmblem32x32():
    return _getDefaultEmblemPath(32)


def getDefaultEmblem64x64():
    return _getDefaultEmblemPath(64)


def getDefaultEmblem128x128():
    return _getDefaultEmblemPath(128)


def getDefaultEmblem256x256():
    return _getDefaultEmblemPath(256)


def getNoClanEmblem32x32():
    return _getNoClanEmblemPath(32)


def getClanRoleName(role):
    if role in CLAN_MEMBERS:
        return CLAN_MEMBERS[role]
    return b''


def _getDefaultEmblemPath(size):
    return b'%s/%s%dx%d.png' % (
     DEFAULT_EMBLEM_PATH, DEFAULT_EMBLEM_NAME_PREFIX, size, size)


def _getNoClanEmblemPath(size):
    return b'%s/%s%dx%d.png' % (
     DEFAULT_EMBLEM_PATH, NO_EMBLEM_NAME_PREFIX, size, size)


AccessTokenData = namedtuple(b'AccessTokenData', (b'accessToken', b'expiresAt'))
