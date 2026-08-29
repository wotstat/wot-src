from helpers import aop

class _ParametrizeInitAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InitHeroTankPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.game_control.hero_tank_controller', b'HeroTankController', b'isEnabled', aspects=(
         _ParametrizeInitAspect,))
        return
