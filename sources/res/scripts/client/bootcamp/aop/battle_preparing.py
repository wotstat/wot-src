from helpers import aop
from bootcamp.aop import common

def weave(weaver, stateBattlePreparing):
    weaver.weave(pointcut=_PointcutDelayStartFirstBattle(stateBattlePreparing))
    return


class _PointcutDelayStartFirstBattle(aop.Pointcut):

    def __init__(self, stateBattlePreparing):
        super(_PointcutDelayStartFirstBattle, self).__init__(b'Avatar', b'PlayerAvatar', b'^(vehicle_onAppearanceReady|onEnterWorld|onSpaceLoaded)$', aspects=(
         common.AspectRedirectMethod({b'vehicle_onAppearanceReady': (stateBattlePreparing.onVehicleOnAppearanceReady), 
            b'onEnterWorld': (stateBattlePreparing.onAvatarOnEnterWorld), 
            b'onSpaceLoaded': (stateBattlePreparing.onSpaceLoaded)}),))
        return
