from helpers import aop
import aspects

class MakeStrongholdsUnavailable(aop.Pointcut):

    def __init__(self):
        aop.Pointcut.__init__(self, b'gui.Scaleform.daapi.view.lobby.header.LobbyHeader', b'LobbyHeader', b'_updateStrongholdsSelector', aspects=(
         aspects.MakeStrongholdsUnavailable(),))
        return
