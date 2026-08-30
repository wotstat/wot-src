from collections import namedtuple
import BigWorld
from adisp import adisp_async
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IGoodiesRequester
GoodieVariable = namedtuple(b'GoodieVariable', b'state finishTime count')

class _ClanReserveInfo(namedtuple(b'_ClanReserveInfo', b'finishTime value duration')):
    __slots__ = ()

    def __new__(cls, finishTime, value, duration=3600):
        return super(_ClanReserveInfo, cls).__new__(cls, finishTime, value, duration)


class GoodiesRequester(AbstractSyncDataRequester, IGoodiesRequester):

    @adisp_async
    def _requestCache(self, callback):
        BigWorld.player().goodies.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    @property
    def goodies(self):
        return self.getCacheValue(b'goodies', {})

    @property
    def pr2ConversionResult(self):
        return self.getCacheValue(b'pr2_conversion', tuple())

    def getActiveClanReserves(self):
        return self.getCacheValue(b'clanReserves', {})

    def _preprocessValidData(self, data):
        data = dict(data)
        goodies = data.get(b'goodies', {})
        data[b'goodies'] = {gID: GoodieVariable(*data) for gID, data in goodies.iteritems()}
        clanReserves = {}
        for crID, crData in data.get(b'clanReserves', {}).iteritems():
            clanReserves[crID] = _ClanReserveInfo(crData[b'timeExpiration'], crData[b'factors'], crData[b'duration'])

        data[b'clanReserves'] = clanReserves
        return data
