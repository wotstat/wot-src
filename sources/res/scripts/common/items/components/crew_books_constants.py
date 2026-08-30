from __future__ import absolute_import
from builtins import range
CREW_BOOKS_XML_FILE = b'crewBooks.xml'
CREW_BOOKS_PRICE_GROUPS_XML_FILE = b'priceGroups.xml'
CREW_BOOK_TYPES_XML_FILE = b'crewBookTypes.xml'
CREW_BOOK_DISPLAYED_AWARDS_COUNT = 11

class CREW_BOOK_PROPERTIES_MASKS:
    FULL_CREW = 1
    ROLE_LEVEL = 2
    SPECIALIZATION = 4
    EMPTY_MASK = 0
    ALL = (
     FULL_CREW, ROLE_LEVEL, SPECIALIZATION)


class CrewBookCacheType:
    CREW_BOOK = 1
    ITEM_GROUP = 2
    RANGE = {
     CREW_BOOK, ITEM_GROUP}


class CREW_BOOK_RARITY:
    CREW_COMMON = b'brochure'
    CREW_RARE = b'guide'
    CREW_EPIC = b'crewBook'
    PERSONAL = b'personalBook'
    UNIVERSAL = b'universalBook'
    UNIVERSAL_GUIDE = b'universalGuide'
    UNIVERSAL_BROCHURE = b'universalBrochure'
    ALL_TYPES = (
     CREW_COMMON, CREW_RARE, CREW_EPIC, PERSONAL, UNIVERSAL_BROCHURE, UNIVERSAL_GUIDE, UNIVERSAL)
    NO_NATION_TYPES = (PERSONAL, UNIVERSAL, UNIVERSAL_GUIDE, UNIVERSAL_BROCHURE)
    ORDER = dict(zip(ALL_TYPES, range(len(ALL_TYPES))))


class CREW_BOOK_SPREAD:
    CREW_BOOK = b'crewBook'
    PERSONAL_BOOK = b'personalBook'
    CREW_BOOK_NO_NATION = b'universalBook'
    ALL_SPREADS = (
     CREW_BOOK, PERSONAL_BOOK, CREW_BOOK_NO_NATION)
