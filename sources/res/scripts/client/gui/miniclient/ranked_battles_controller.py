from helpers import aop

class _ParametrizeInitAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InitRankedPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.game_control.ranked_battles_controller', b'RankedBattlesController', b'isAvailable', aspects=(
         _ParametrizeInitAspect,))
        return
