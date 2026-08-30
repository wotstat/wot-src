from __future__ import absolute_import
from enum import IntEnum
RENT_TOKEN_NAME = b'telecom_rent_token'
PARTNERSHIP_TOKEN_NAME = b'telecom_partnership_token'
PARTNERSHIP_BLOCKED_TOKEN_NAME = b'telecom_partnership_blocked_token'
ROSTER_EXPIRATION_TOKEN_NAME = b'telecom_roster_expiration_token'
TELECOM_RENTALS_CONFIG = b'telecom_rentals_config'
TELECOM_RENTALS_RENT_KEY = b'telecom'

class PartnershipState(IntEnum):
    NO_PARTNERSHIP = 0
    ACTIVE_PARTNERSHIP = 1
    BLOCKED_PARTNERSHIP = 2
