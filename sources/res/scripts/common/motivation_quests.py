from __future__ import absolute_import
import os
from pprint import pformat
from quest_cache_helpers import readQuestsFromFile, makeI18nString
from constants import ITEM_DEFS_PATH, EVENT_TYPE
from debug_utils import LOG_WARNING
_QUESTS_DIR = os.path.join(ITEM_DEFS_PATH, b'motivation_quests/')
_QUESTS_FILE = b'quests.xml'

def __parseMotivationsQuest(node):
    try:
        info = node.info
        return (makeI18nString(info[b'advice'][b'key']),
         makeI18nString(info[b'requirements'][b'key']),
         makeI18nString(info[b'congratulation'][b'key']))
    except:
        return

    return


class MotivationQuest(object):
    __slots__ = (b'questID', b'questName', b'questDescr', b'advice', b'requirements', b'congratulation', b'questData')

    def __init__(self, questID, questName, questDescr, advice, requirements, congratulation, questData):
        self.questID = questID
        self.questName = questName
        self.questDescr = questDescr
        self.advice = advice
        self.requirements = requirements
        self.congratulation = congratulation
        self.questData = questData
        return


def motivationQuestsFromFile(pathToFile):
    quests = {}
    for quest in readQuestsFromFile(pathToFile, EVENT_TYPE.MOTIVE_QUEST):
        questID, questName, questDescr, questClientData, node = quest
        questData = __parseMotivationsQuest(node)
        if questData is None:
            LOG_WARNING((b'Not all required fields are specified in quest for {}.').format(questID))
            continue
        advice, requirements, congratulation = questData
        quests[questID] = MotivationQuest(questID, questName, questDescr, advice, requirements, congratulation, questClientData)

    return quests


class _QuestsCache(object):

    def __init__(self, quests):
        self.__quests = quests
        return

    def getAllQuests(self):
        return self.__quests.values()

    def getQuestIDs(self):
        return self.__quests.keys()

    def getQuestByID(self, questID):
        return self.__quests[questID]

    def __repr__(self):
        res = pformat(self.__quests, depth=3)
        return res


g_cache = None

def init():
    global g_cache
    if g_cache is None:
        questFilePath = os.path.join(_QUESTS_DIR, _QUESTS_FILE)
        g_cache = _QuestsCache(motivationQuestsFromFile(questFilePath))
    return
