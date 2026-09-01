from __future__ import absolute_import, division
from functools import total_ordering
from past.builtins import cmp
from typing import Optional, FrozenSet, Tuple, Dict
from cache import cached_property
from intervals import Interval
from soft_exception import SoftException
EXTRA_RANK_TAG = b'extra'
COMP7_UNDEFINED_RANK_ID = 0
COMP7_UNDEFINED_DIVISION_ID = 0
COMP7_UNDEFINED_DIVISION_SERIAL_IDX = 0

@total_ordering
class Comp7Division(object):
    __slots__ = (b'range', b'tags', b'rank', b'dvsnID', b'index', b'activityPointsPerBattle', b'hasRankInactivity', b'seasonPoints', b'serialIdx', b'ratingPointsPenalty')

    def __init__(self, serialIdx, divisionInfo):
        pointsRange = divisionInfo[b'range']
        self.range = pointsRange if isinstance(pointsRange, Interval) else Interval(*pointsRange)
        self.rank = divisionInfo[b'rank']
        self.dvsnID = divisionInfo[b'id']
        self.index = divisionInfo[b'index']
        self.tags = frozenset(divisionInfo.get(b'tags', ()))
        self.activityPointsPerBattle = divisionInfo.get(b'rankInactivity', {}).get(b'activityPointsPerBattle', 0)
        self.ratingPointsPenalty = divisionInfo.get(b'rankInactivity', {}).get(b'ratingPointsPenalty', 0)
        self.hasRankInactivity = divisionInfo.get(b'hasRankInactivity', False)
        self.seasonPoints = divisionInfo.get(b'seasonPoints', 0)
        self.serialIdx = serialIdx
        return

    def __eq__(self, other):
        return self.__compare(other) == 0

    def __lt__(self, other):
        return self.__compare(other) < 0

    def __hash__(self):
        return hash((self.rank, self.range))

    def __compare(self, other):
        if not isinstance(other, Comp7Division):
            raise TypeError
        return cmp(self.rank, other.rank) or cmp(self.range, other.range)

    def __repr__(self):
        return (b'{}[{}]').format(self.__class__.__name__, {s: getattr(self, s) for s in self.__slots__})


class Comp7Rank(object):
    __slots__ = (b'id', b'name')

    def __init__(self, rankDict):
        self.id = rankDict[b'id']
        self.name = rankDict.get(b'name')
        return

    @property
    def index(self):
        return self.id


class Comp7RanksConfig(object):

    def __init__(self, config):
        self._config = config
        return

    @cached_property
    def businessDayStartHour(self):
        return self._config.get(b'businessDayStartHour', 0)

    @cached_property
    def divisions(self):
        divisions = self._config.get(b'divisions', ())
        return tuple(Comp7Division(serialIdx, divisionInfo) for serialIdx, divisionInfo in enumerate(divisions))

    @cached_property
    def ranks(self):
        ranks = self._config.get(b'ranks', {})
        ranksOrder = self._config.get(b'ranksOrder', ())
        return tuple(Comp7Rank(ranks[rankID]) for rankID in ranksOrder)

    def getDivisionByRating(self, points, hasEliteEntitlement):
        eliteDiv = self.eliteDivision
        if hasEliteEntitlement and points in eliteDiv.range:
            return eliteDiv
        for div in self.divisions:
            if points in div.range:
                return div

        raise SoftException((b'Comp7: No ranks configured for {}').format(points))
        return

    def getStartRatingForDivision(self, divisionSerialIdx):
        if not 0 <= divisionSerialIdx < len(self.divisions):
            raise SoftException(b'Comp7: Invalid division serial index', divisionSerialIdx)
        division = self.divisions[divisionSerialIdx]
        return division.range.begin

    @cached_property
    def eliteDivision(self):
        return self.divisions[-1]

    def getActivityPointsForBattle(self, rank, divisionIdx):
        for div in self.divisions:
            if div.rank == rank and div.index == divisionIdx:
                return div.activityPointsPerBattle

        return 0
