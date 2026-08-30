CREW_SKINS_XML_FILE = b'crewSkins.xml'
CREW_SKINS_PRICE_GROUPS_XML_FILE = b'priceGroups.xml'
NO_CREW_SKIN_ID = 0
NO_CREW_SKIN_SOUND_SET = b'-'

class CREW_SKIN_PROPERTIES_MASKS:
    SEX = 2
    NATION = 4
    EMPTY_MASK = 0


class CrewSkinType:
    CREW_SKIN = 1
    ITEM_GROUP = 2
    RANGE = {
     CREW_SKIN, ITEM_GROUP}


class TANKMAN_SEX:
    NONE = b''
    MALE = b'male'
    FEMALE = b'female'
    ALL = (
     MALE, FEMALE)
    AVAILABLE = (NONE, MALE, FEMALE)

    @staticmethod
    def getTankmanSex(tmanDescr):
        if tmanDescr.isFemale:
            return TANKMAN_SEX.FEMALE
        return TANKMAN_SEX.MALE


class CREW_SKIN_RARITY:
    COMMON = 1
    RARE = 2
    EPIC = 3
    ALL = (
     COMMON, RARE, EPIC)
