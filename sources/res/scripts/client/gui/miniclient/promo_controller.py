from helpers import aop

class ShowPromoBrowserPointcut(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.game_control.PromoController', b'PromoController', b'onLobbyInited', aspects=(
         aop.DummyAspect,))
        return
