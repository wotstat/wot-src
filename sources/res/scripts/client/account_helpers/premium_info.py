from constants import PREMIUM_TYPE

class PremiumInfo(object):

    def __init__(self):
        self._rawPremiumInfo = {p: 0 for p in PREMIUM_TYPE.TYPES_SORTED}
        self._rawPremiumInfo[b'premMask'] = 0
        return

    def update(self, rawPremiumInfo):
        self._rawPremiumInfo.update(rawPremiumInfo)
        return

    def isActivePremium(self, checkPremiumType):
        return self.activePremiumType >= checkPremiumType

    @property
    def isPremium(self):
        return self.activePremiumType != PREMIUM_TYPE.NONE

    @property
    def totalPremiumExpiryTime(self):
        premiumMask = self._rawPremiumInfo[b'premMask']
        return max(tuple(self._rawPremiumInfo[p] for p in PREMIUM_TYPE.TYPES_SORTED if bool(premiumMask & p)) + (0,))

    @property
    def activePremiumExpiryTime(self):
        activePremiumType = self.activePremiumType
        if activePremiumType != PREMIUM_TYPE.NONE:
            return self._rawPremiumInfo[activePremiumType]
        return 0

    @property
    def activePremiumType(self):
        return PREMIUM_TYPE.activePremium(self._rawPremiumInfo[b'premMask'])

    @property
    def data(self):
        premiumMask = self._rawPremiumInfo[b'premMask']
        return {pType: {b'active': (bool(premiumMask & pType)), b'expiryTime': (self._rawPremiumInfo[pType])} for pType in PREMIUM_TYPE.TYPES_SORTED}
