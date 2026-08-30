from __future__ import absolute_import
import logging, typing
from account_helpers.AccountSettings import KEY_UI_FLAGS, AccountSettings
from journey_marathon.jm_helpers import jmCtrl
if typing.TYPE_CHECKING:
    from typing import Callable, Union, Set
_error = logging.getLogger(__name__).error
_UI = b'journeyMarathon'
_JM_ID = b'journeyMarathonID'
_IS_MAP_OPENED = b'jmIsMapViewOpened'
_MAP_QUEST_PROGRESS = b'jmMapViewQuestProgress'
_MAP_ABS_GAME_DAY = b'jmMapViewQuestProgressAbsGameDay'
_QUESTS_COMPLETE_DAY = b'jmMapQuestsCompletedAbsGameDay'
_LORE_HINT_SHOWN = b'jmLoreHintShown'
_IS_ANIM_APPEARED = b'jmIsAnimAppeared'

def makeUiDefaults():
    return {_UI: {_JM_ID: b'', 
             _IS_MAP_OPENED: False, 
             _MAP_QUEST_PROGRESS: {}, _MAP_ABS_GAME_DAY: 0, 
             _QUESTS_COMPLETE_DAY: 0, 
             _LORE_HINT_SHOWN: (set()), 
             _IS_ANIM_APPEARED: False}}


def initJmAccountSettings():
    AccountSettings.overrideDefaultSettings(KEY_UI_FLAGS, makeUiDefaults())
    return


def updateJmAccountSettings(currJMId):
    accSettings = AccountSettings.getUIFlag(_UI)
    lastJMId = accSettings[_JM_ID]
    if not lastJMId:
        accSettings[_JM_ID] = currJMId
        AccountSettings.setUIFlag(_UI, accSettings)
    elif lastJMId != currJMId:
        accSettings = makeUiDefaults()[_UI]
        accSettings[_JM_ID] = currJMId
        AccountSettings.setUIFlag(_UI, accSettings)
    return


def getJmMapViewOpened():
    return AccountSettings.getUIFlag(_UI)[_IS_MAP_OPENED]


def setJmMapViewOpened():
    section = AccountSettings.getUIFlag(_UI)
    section[_IS_MAP_OPENED] = True
    AccountSettings.setUIFlag(_UI, section)
    return


def makeJmMapViewQuestsProgressGetter():
    _tryResetQuestsProgress()
    questProgressSection = AccountSettings.getUIFlag(_UI)[_MAP_QUEST_PROGRESS]

    def getProgress(qID):
        return questProgressSection.get(qID, 0)

    return getProgress


def setJmMapViewQuestsProgress(qID, progress):
    _tryResetQuestsProgress()
    jmSection = AccountSettings.getUIFlag(_UI)
    questProgressSection = jmSection[_MAP_QUEST_PROGRESS]
    questProgressSection[qID] = int(progress)
    AccountSettings.setUIFlag(_UI, jmSection)
    return


def getJmLoreNodeShown():
    return AccountSettings.getUIFlag(_UI)[_LORE_HINT_SHOWN]


def updateJmLoreNodeShown(nodeId):
    settings = AccountSettings.getUIFlag(_UI)
    loreShown = settings[_LORE_HINT_SHOWN]
    if nodeId not in loreShown:
        loreShown.add(nodeId)
        AccountSettings.setUIFlag(_UI, settings)
    return


def _tryResetQuestsProgress():
    jmSection = AccountSettings.getUIFlag(_UI)
    lastAbsDay = jmSection[_MAP_ABS_GAME_DAY]
    currAbsDay = jmCtrl().jmTime.getAbsoluteGameDay()
    if currAbsDay != lastAbsDay:
        jmSection[_MAP_ABS_GAME_DAY] = currAbsDay
        jmSection[_MAP_QUEST_PROGRESS] = {}
        AccountSettings.setUIFlag(_UI, jmSection)
    return


def setJmQuestsCompleteAnimShown():
    jmSection = AccountSettings.getUIFlag(_UI)
    jmSection[_QUESTS_COMPLETE_DAY] = jmCtrl().jmTime.getAbsoluteGameDay()
    AccountSettings.setUIFlag(_UI, jmSection)
    return


def getJmQuestsCompleteAnimShown():
    jmSection = AccountSettings.getUIFlag(_UI)
    lastAbsDay = jmSection[_QUESTS_COMPLETE_DAY]
    currAbsDay = jmCtrl().jmTime.getAbsoluteGameDay()
    return lastAbsDay == currAbsDay


def getJmBannerAppearAnimSeen():
    return AccountSettings.getUIFlag(_UI)[_IS_ANIM_APPEARED]


def setJmBannerAppearAnimSeen():
    section = AccountSettings.getUIFlag(_UI)
    section[_IS_ANIM_APPEARED] = True
    AccountSettings.setUIFlag(_UI, section)
    return
