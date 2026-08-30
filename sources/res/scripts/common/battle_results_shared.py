import struct
from itertools import izip
from constants import PREMIUM_TYPE, PREM_BONUS_TYPES
VEH_INTERACTION_DETAILS = (
 (b'spotted', b'B', 1, 0),
 (b'deathReason', b'b', 10, -1),
 (b'directHits', b'H', 65535, 0),
 (b'directEnemyHits', b'H', 65535, 0),
 (b'explosionHits', b'H', 65535, 0),
 (b'piercings', b'H', 65535, 0),
 (b'piercingEnemyHits', b'H', 65535, 0),
 (b'damageDealt', b'I', 4294967295L, 0),
 (b'damageAssistedTrack', b'H', 65535, 0),
 (b'damageAssistedRadio', b'H', 65535, 0),
 (b'damageAssistedStun', b'H', 65535, 0),
 (b'damageAssistedSmoke', b'H', 65535, 0),
 (b'damageAssistedInspire', b'H', 65535, 0),
 (b'crits', b'I', 4294967295L, 0),
 (b'fire', b'H', 65535, 0),
 (b'stunNum', b'H', 65535, 0),
 (b'stunDuration', b'f', 65535.0, 0.0),
 (b'damageBlockedByArmor', b'I', 4294967295L, 0),
 (b'damageReceived', b'H', 65535, 0),
 (b'rickochetsReceived', b'H', 65535, 0),
 (b'noDamageDirectHitsReceived', b'H', 65535, 0),
 (b'targetKills', b'B', 255, 0))
VEH_INTERACTION_DETAILS_NAMES = [x[0] for x in VEH_INTERACTION_DETAILS]
VEH_INTERACTION_DETAILS_MAX_VALUES = dict((x[0], x[2]) for x in VEH_INTERACTION_DETAILS)
VEH_INTERACTION_DETAILS_INIT_VALUES = [x[3] for x in VEH_INTERACTION_DETAILS]
VEH_INTERACTION_DETAILS_LAYOUT = (b'').join([x[1] for x in VEH_INTERACTION_DETAILS])
VEH_INTERACTION_DETAILS_INDICES = dict((x[1][0], x[0]) for x in enumerate(VEH_INTERACTION_DETAILS))
VEH_INTERACTION_DETAILS_TYPES = dict((x[0], x[1]) for x in VEH_INTERACTION_DETAILS)
VEH_INTERACTIVE_STATS = (b'xp', b'damageDealt', b'capturePts', b'flagActions', b'winPoints', b'deathCount', b'resourceAbsorbed', b'stopRespawn', b'equipmentDamage', b'equipmentKills')
VEH_INTERACTIVE_STATS_INDICES = dict((x[1], x[0]) for x in enumerate(VEH_INTERACTIVE_STATS))
AVATAR_PRIVATE_STATS = (b'ragePoints',)
AVATAR_PRIVATE_STATS_INDICES = dict((x[1], x[0]) for x in enumerate(AVATAR_PRIVATE_STATS))
_PREM_TYPE_TO_FACTOR100_NAMES = {(PREM_BONUS_TYPES.CREDITS): {(PREMIUM_TYPE.BASIC): b'premiumCreditsFactor100', 
                                (PREMIUM_TYPE.PLUS): b'premiumPlusCreditsFactor100', 
                                (PREMIUM_TYPE.VIP): b'premiumVipCreditsFactor100'}, 
   (PREM_BONUS_TYPES.XP): {(PREMIUM_TYPE.BASIC): b'premiumXPFactor100', 
                           (PREMIUM_TYPE.PLUS): b'premiumPlusXPFactor100', 
                           (PREMIUM_TYPE.VIP): b'premiumVipXPFactor100'}, 
   (PREM_BONUS_TYPES.TMEN_XP): {(PREMIUM_TYPE.BASIC): b'premiumTmenXPFactor100', 
                                (PREMIUM_TYPE.PLUS): b'premiumPlusTmenXPFactor100', 
                                (PREMIUM_TYPE.VIP): b'premiumVipXPTmenFactor100'}, 
   (PREM_BONUS_TYPES.DYN_CURRENCIES): {(PREMIUM_TYPE.BASIC): b'premiumFactor100', 
                                       (PREMIUM_TYPE.PLUS): b'premiumPlusFactor100', 
                                       (PREMIUM_TYPE.VIP): b'premiumVipFactor100'}}

class UNIT_CLAN_MEMBERSHIP:
    NONE = 0
    ANY = 1
    SAME = 2


def dictToList(indices, d):
    l = [
     None] * len(indices)
    for name, index in indices.iteritems():
        l[index] = d[name]

    return l


def listToDict(names, l):
    d = {}
    for x in enumerate(names):
        d[x[1]] = l[x[0]]

    return d


class _VehicleInteractionDetailsItem(object):

    @staticmethod
    def __fmt2py(format):
        if format in (b'f',):
            return float
        return int

    def __init__(self, values, offset):
        self.__values = values
        self.__offset = offset
        return

    def __getitem__(self, key):
        return self.__values[self.__offset + VEH_INTERACTION_DETAILS_INDICES[key]]

    def __setitem__(self, key, value):
        self.__values[self.__offset + VEH_INTERACTION_DETAILS_INDICES[key]] = min(self.__fmt2py(VEH_INTERACTION_DETAILS_TYPES[key])(value), VEH_INTERACTION_DETAILS_MAX_VALUES[key])
        return

    def __str__(self):
        return str(dict(self))

    def __iter__(self):
        return izip(VEH_INTERACTION_DETAILS_NAMES, self.__values[self.__offset:])


class VehicleInteractionDetails(object):

    def __init__(self, uniqueVehIDs, values):
        self.__uniqueVehIDs = uniqueVehIDs
        self.__values = values
        size = len(VEH_INTERACTION_DETAILS)
        self.__offsets = dict((x[1], x[0] * size) for x in enumerate(uniqueVehIDs))
        return

    @staticmethod
    def fromPacked(packed):
        count = len(packed) / struct.calcsize((b'').join([b'<2I', VEH_INTERACTION_DETAILS_LAYOUT]))
        packedVehIDsLayout = b'<%dI' % (2 * count,)
        packedVehIDsLen = struct.calcsize(packedVehIDsLayout)
        flatIDs = struct.unpack(packedVehIDsLayout, packed[:packedVehIDsLen])
        uniqueVehIDs = []
        for i in xrange(0, len(flatIDs), 2):
            uniqueVehIDs.append((flatIDs[i], flatIDs[i + 1]))

        values = struct.unpack(b'<' + VEH_INTERACTION_DETAILS_LAYOUT * count, packed[packedVehIDsLen:])
        return VehicleInteractionDetails(uniqueVehIDs, values)

    def __getitem__(self, uniqueVehID):
        if not isinstance(uniqueVehID, tuple):
            raise UserWarning((b'Argument uniqueVehID should be tuple: {}').format(uniqueVehID))
        offset = self.__offsets.get(uniqueVehID, None)
        if offset is None:
            self.__uniqueVehIDs.append(uniqueVehID)
            offset = len(self.__values)
            self.__values += VEH_INTERACTION_DETAILS_INIT_VALUES
            self.__offsets[uniqueVehID] = offset
        return _VehicleInteractionDetailsItem(self.__values, offset)

    def __contains__(self, uniqueVehID):
        if not isinstance(uniqueVehID, tuple):
            raise UserWarning((b'Argument uniqueVehID should be tuple: {}').format(uniqueVehID))
        return uniqueVehID in self.__offsets

    def __str__(self):
        return str(self.toDict())

    def pack(self):
        count = len(self.__uniqueVehIDs)
        flatIDs = []
        for uniqueID in self.__uniqueVehIDs:
            flatIDs.append(uniqueID[0])
            flatIDs.append(uniqueID[1])

        try:
            packed = struct.pack((b'<%dI' % (2 * count)), *flatIDs) + struct.pack((b'<' + VEH_INTERACTION_DETAILS_LAYOUT * count), *self.__values)
        except Exception as e:
            from debug_utils import LOG_ERROR
            LOG_ERROR(b'PACKING EXCEPTION', e, str(self))
            packed = b''

        return packed

    def toDict(self):
        return dict(self.iteritems())

    def iteritems(self):
        for vehInfo, offset in self.__offsets.iteritems():
            yield (vehInfo, dict(_VehicleInteractionDetailsItem(self.__values, offset)))

        return
