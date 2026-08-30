from helpers import aop

def weave(weaver):
    weaver.weave(pointcut=_PointcutToggleFullStats, avoid=True)
    weaver.weave(pointcut=_PointcutComputePiercingPowerAtDist)
    weaver.weave(pointcut=_PointcutComputePiercingPowerRandomization)
    weaver.weave(pointcut=_PointcutKeepArenaSoundsPlayingOnResultScreen)
    return


class _PointcutToggleFullStats(aop.Pointcut):

    def __init__(self):
        super(_PointcutToggleFullStats, self).__init__(b'gui.battle_control', b'event_dispatcher', b'toggleFullStats')
        return


class _PointcutComputePiercingPowerAtDist(aop.Pointcut):

    def __init__(self):
        super(_PointcutComputePiercingPowerAtDist, self).__init__(b'AvatarInputHandler', b'gun_marker_ctrl', b'_computePiercingPowerAtDistImpl', aspects=(
         _AspectComputePiercingPowerAtDist,))
        return


class _PointcutComputePiercingPowerRandomization(aop.Pointcut):

    def __init__(self):
        super(_PointcutComputePiercingPowerRandomization, self).__init__(b'AvatarInputHandler', b'gun_marker_ctrl', b'_computePiercingPowerRandomizationImpl', aspects=(
         _AspectComputePiercingPowerRandomization,))
        return


class _PointcutKeepArenaSoundsPlayingOnResultScreen(aop.Pointcut):

    def __init__(self):
        super(_PointcutKeepArenaSoundsPlayingOnResultScreen, self).__init__(b'SoundGroups', b'SoundGroups', b'enableArenaSounds', aspects=(
         _AspectKeepArenaSoundsPlayingOnResultScreen,))
        return


class _AspectComputePiercingPowerAtDist(aop.Aspect):

    def atCall(self, cd):
        from bootcamp.Bootcamp import g_bootcamp
        bootcampPP = g_bootcamp.getPredefinedPiercingPower()
        if bootcampPP:
            cd.avoid()
            piercingPower = bootcampPP[b'data'][0][1]
            return piercingPower
        return


class _AspectComputePiercingPowerRandomization(aop.Aspect):

    def atCall(self, cd):
        from bootcamp.Bootcamp import g_bootcamp
        if g_bootcamp.getPredefinedPiercingPower():
            cd.avoid()
            return (100.0, 100.0)
        return


class _AspectKeepArenaSoundsPlayingOnResultScreen(aop.Aspect):

    def atCall(self, cd):
        enable = cd.findArg(0, b'enable')
        if not enable:
            cd.avoid()
        return
