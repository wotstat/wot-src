from __future__ import absolute_import
from collections import namedtuple
from future.utils import iteritems
import BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IGoodiesRequester
GoodieVariable = namedtuple(b'GoodieVariable', b'state finishTime count expirations')

class _ClanReserveInfo(namedtuple(b'_ClanReserveInfo', b'finishTime value duration')):
    __slots__ = ()

    def __new__(cls, finishTime, value, duration=3600):
        return super(_ClanReserveInfo, cls).__new__(cls, finishTime, value, duration)


class GoodiesRequester(AbstractSyncDataRequester, IGoodiesRequester):

    def _requestCache(self, callback=None):
        BigWorld.player().goodies.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    @property
    def goodies(self):
        return self.getCacheValue(b'goodies', {})

    def getActiveClanReserves(self):
        return self.getCacheValue(b'clanReserves', {})

    def _preprocessValidData(self, data):
        processed = dict(data)
        goodies = data.get(b'goodies', {})
        processed[b'goodies'] = {gID: GoodieVariable(status, finishTime, count, expirations) for gID, (status, finishTime, count, expirations) in iteritems(goodies)}
        clanReserves = {}
        for crID, crData in iteritems(data.get(b'clanReserves', {})):
            clanReserves[crID] = _ClanReserveInfo(crData[b'timeExpiration'], crData[b'factors'], crData[b'duration'])

        processed[b'clanReserves'] = clanReserves
        return processed
