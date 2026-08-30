from __future__ import absolute_import
import typing
from collections import namedtuple
import BigWorld
from constants import CommendationsState, IS_CLIENT, ARENA_PERIOD
AVATAR_COMPONENT_NAME = b'commendations'
ARENA_COMPONENT_NAME = b'ArenaCommendationsMasterComponent'
ARENA_CONTROLLER_NAME = b'commendationsController'
TEAM_INFO_LIVETAGS_COMPONENT = b'liveTagsInfoComponent'

class CommendationsSource(object):
    EARS = b'ears'
    TAB_SCREEN = b'tab'
    CALLOUT = b'callout'


def canCommendNow(period):
    return period in (ARENA_PERIOD.PREBATTLE, ARENA_PERIOD.BATTLE)


CommendationStatistics = namedtuple(b'CommendationStatistics', b'received, sent')
if typing.TYPE_CHECKING:
    CommendationsStatisticsType = typing.Union[CommendationStatistics, typing.Tuple]

def getCommendationState(vehicleID):
    cmpt = getAvatarComponent(BigWorld.player())
    return cmpt.getMessageStateForVehID(vehicleID)


def getAvatarComponent(entity):
    if not entity:
        return
    else:
        return entity.dynamicComponents.get(AVATAR_COMPONENT_NAME, None)


def getArenaComponent(entity):
    if not entity:
        return
    else:
        return entity.components.get(ARENA_COMPONENT_NAME, None)


def getArenaController(entity):
    if not entity:
        return
    else:
        return entity.dynamicComponents.get(ARENA_CONTROLLER_NAME, None)


def getTeamInfoLiveTagsComponent(entity):
    if not entity:
        return
    else:
        return entity.dynamicComponents.get(TEAM_INFO_LIVETAGS_COMPONENT, None)


CommendationStateType = typing.Union[CommendationsState, int]
