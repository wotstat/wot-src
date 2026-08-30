NAMES = (b'ussr', b'germany', b'usa', b'china', b'france', b'uk', b'japan', b'czech', b'sweden', b'poland', b'italy')
INDICES = dict((n, i) for i, n in enumerate(NAMES))
MAP = dict(enumerate(NAMES))
AVAILABLE_NAMES = (b'ussr', b'germany', b'usa', b'china', b'france', b'uk', b'japan', b'czech', b'sweden', b'poland', b'italy')
NONE_INDEX = 15
ALL_NATIONS_INDEX = -1

class Alliances(object):
    USSR = b'Alliance-USSR'
    GERMANY = b'Alliance-Germany'
    USA = b'Alliance-USA'
    FRANCE = b'Alliance-France'


ALLIANCES_TAGS_ORDER = (
 Alliances.USSR, Alliances.GERMANY, Alliances.USA, Alliances.FRANCE)
ALLIANCES_TAGS = frozenset(ALLIANCES_TAGS_ORDER)
ALLIANCE_IDS = dict((value, index) for index, value in enumerate(ALLIANCES_TAGS_ORDER))
ALLIANCE_TO_NATIONS = {(Alliances.USSR): (frozenset((b'ussr', b'china'))), 
   (Alliances.GERMANY): (frozenset((b'germany', b'japan'))), 
   (Alliances.USA): (frozenset((b'usa', b'uk', b'poland'))), 
   (Alliances.FRANCE): (frozenset((b'france', b'czech', b'sweden', b'italy')))}
ALLIANCE_IDS_MAP = {ai: set(INDICES[n] for n in ALLIANCE_TO_NATIONS[an]) for an, ai in ALLIANCE_IDS.items()}
NATION_TO_ALLIANCE_IDS_MAP = {ni: ai for ni in ALLIANCE_IDS_MAP.items()}
