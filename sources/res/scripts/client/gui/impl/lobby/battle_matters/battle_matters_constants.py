from __future__ import absolute_import
from enum import Enum
CARDS_CONFIG_XML_PATH = b'gui/battle_matters_cards.xml'

class QuestCardSections(Enum):
    ID = b'id'
    SWF_PATH = b'swfPath'
    LESSON_ID = b'lessonId'


class SequenceNumber(Enum):
    SINGLE = 0
    FIRST = 1
    MIDDLE = 2
    LAST = 3
