import enum, typing
MAX_CONFIG_SEQUENCE_SLIDES_COUNT = 250
MAX_CONFIG_SEQUENCES_COUNT = 50
MIN_SLIDES_COUNT_TO_VIEW = 5
DOWNLOAD_SLIDES_MULTIPLAYER = 2
CDN_CACHE_SYNC_TIMEOUT = 300.0
NEWBIES_BATTLES_LIMIT = 100
NEWBIES_VEHICLE_LEVEL = 6

@enum.unique
class SequenceOrders(str, enum.Enum):
    RANDOM = b'random'
    SUBSEQUENTLY = b'subsequently'


@enum.unique
class SequenceCohorts(str, enum.Enum):
    DEFAULT = b'default'
    NEWBIES = b'newbies'

    @classmethod
    def getDefaults(cls):
        return [
         cls.DEFAULT]
