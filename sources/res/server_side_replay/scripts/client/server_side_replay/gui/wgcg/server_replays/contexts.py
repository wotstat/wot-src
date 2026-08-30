from __future__ import absolute_import
from builtins import str
from future.utils import viewitems
from typing import Dict, List
from gui.wgcg.base.contexts import CommonWebRequestCtx
from py2to3.compat import base64compat
from server_side_replay.gui.wgcg.data_wrappers import server_replays
from server_side_replay.gui.wgcg.requests import SERVER_SIDE_REPLAY_REQUEST_TYPE

def makeTupleByDict(ntClass, data):
    unsupportedFields = set(data) - set(ntClass._fields)
    supported = {}
    fieldTypes = getattr(ntClass, b'_field_types', None)
    for k, v in viewitems(data):
        if k not in unsupportedFields:
            if fieldTypes and v is None:
                try:
                    supported[k] = fieldTypes[k]()
                    continue
                except Exception:
                    pass

            supported[k] = v

    return ntClass(**supported)


class JwtWebRequestCtx(CommonWebRequestCtx):

    def __init__(self):
        super(JwtWebRequestCtx, self).__init__()
        self.jwtToken = None
        return


class BestReplaysCtx(JwtWebRequestCtx):

    def __init__(self, account_id=None, vehicleCDs=None, sortBy=None, nation=None, vehicleLevel=None, vehicleType=None, fromDate=None, isPrimeTime=None):
        super(BestReplaysCtx, self).__init__()
        self.__accountId = account_id
        self.__vehicleCDs = vehicleCDs
        self.__nation = nation
        self.__vehicleLevel = vehicleLevel
        self.__vehicleType = vehicleType
        self.__fromDate = fromDate
        self.__isPrimeTime = isPrimeTime
        self.__sortBy = sortBy
        return

    def getRequestType(self):
        return SERVER_SIDE_REPLAY_REQUEST_TYPE.GET_BEST_REPLAYS

    def getRequestKwargs(self):
        result = {}
        if self.__vehicleCDs:
            result[b'vehicle_cd'] = self.__vehicleCDs
        if self.__nation:
            result[b'nation'] = self.__nation
        if self.__vehicleLevel:
            result[b'vehicle_level'] = self.__vehicleLevel
        if self.__vehicleType:
            result[b'vehicle_type'] = self.__vehicleType
        if self.__sortBy:
            result[b'sort_by'] = self.__sortBy
        if self.__accountId:
            result[b'account_id'] = self.__accountId
        if self.__fromDate is not None:
            result[b'from_date'] = self.__fromDate
        if self.__isPrimeTime is not None:
            result[b'is_prime_time'] = self.__isPrimeTime
        return result

    def getDataObj(self, incomeData):
        incomeData = incomeData or {}
        rankings = []
        incomeRankings = incomeData.get(b'rankings', [])
        for rawReplay in sorted(incomeRankings, key=(lambda r: r.get(b'rank'))):
            rankings.append(makeTupleByDict(server_replays.ShortReplay, rawReplay))

        incomeData[b'rankings'] = rankings
        return makeTupleByDict(server_replays.PageReplays, incomeData)


class TopReplaysCtx(JwtWebRequestCtx):

    def getRequestType(self):
        return SERVER_SIDE_REPLAY_REQUEST_TYPE.GET_TOP_REPLAYS

    def getDataObj(self, incomeData):
        incomeData = incomeData or {}
        incomeData = {k: makeTupleByDict(server_replays.ShortReplay, v) for k, v in incomeData.items()}
        return makeTupleByDict(server_replays.TopReplays, incomeData)


class ReplayLinkCtx(JwtWebRequestCtx):

    def __init__(self, replayID=None):
        super(ReplayLinkCtx, self).__init__()
        self.__replayID = replayID
        return

    def getReplayID(self):
        return self.__replayID

    def getRequestType(self):
        return SERVER_SIDE_REPLAY_REQUEST_TYPE.GET_REPLAY_LINK

    def getDataObj(self, incomeData):
        return makeTupleByDict(server_replays.ReplayLink, incomeData or {})


class FindReplayCtx(JwtWebRequestCtx):

    def __init__(self, replayName):
        super(FindReplayCtx, self).__init__()
        self.__replayName = replayName
        return

    def getReplayName(self):
        return base64compat.b64encode(str(self.__replayName))

    def getRequestType(self):
        return SERVER_SIDE_REPLAY_REQUEST_TYPE.POST_FIND_REPLAY

    def getDataObj(self, incomeData):
        return makeTupleByDict(server_replays.ReplayLink, incomeData or {})
