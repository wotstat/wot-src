from helpers.EntityExtra import EntityExtra

class AfterburningBattleRoyale(EntityExtra):

    def _start(self, extraData, activate=None):
        vehicle = extraData[b'entity']
        appearance = vehicle.appearance
        if appearance is not None:
            effectMgr = appearance.customEffectManager
            if effectMgr:
                effectMgr.variables[b'Nitro'] = 1
        return

    def _cleanup(self, extraData):
        vehicle = extraData[b'entity']
        appearance = vehicle.appearance
        if appearance is not None:
            effectMgr = appearance.customEffectManager
            if effectMgr:
                effectMgr.variables[b'Nitro'] = 0
        return
