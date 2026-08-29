from helpers import aop

class _ParametrizeInitAspect(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class _DisableEventBoards(aop.Aspect):

    def atCall(self, cd):
        cd.avoid()
        return False


class InitEventPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.game_control.event_battles_controller', b'EventBattlesController', b'isEnabled', aspects=(
         _ParametrizeInitAspect,))
        return


class DisableEventBoards(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'helpers.server_settings', b'ServerSettings', b'isElenEnabled', aspects=(
         _DisableEventBoards,))
        return
