from __future__ import absolute_import
from helpers.EntityExtra import EntityExtra

class AfterburningBattleRoyale(EntityExtra):

    def _start(self, data, args):
        vehicle = data[b'entity']
        appearance = vehicle.appearance
        if appearance is not None:
            effectMgr = appearance.customEffectManager
            if effectMgr:
                effectMgr.variables[b'Nitro'] = 1
        return

    def _cleanup(self, data):
        vehicle = data[b'entity']
        appearance = vehicle.appearance
        if appearance is not None:
            effectMgr = appearance.customEffectManager
            if effectMgr:
                effectMgr.variables[b'Nitro'] = 0
        return
