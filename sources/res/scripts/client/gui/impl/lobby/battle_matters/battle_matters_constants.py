from enum import Enum
CARDS_CONFIG_XML_PATH_PATTERN = b'gui/battle_matters_cards_%s.xml'

class QuestCardSections(Enum):
    ID = b'id'
    SWF_PATH = b'swfPath'
    LESSON_ID = b'lessonId'


class SequenceNumber(Enum):
    SINGLE = 0
    FIRST = 1
    MIDDLE = 2
    LAST = 3
