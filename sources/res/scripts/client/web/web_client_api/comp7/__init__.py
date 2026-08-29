from helpers import dependency
from skeletons.gui.game_control import IComp7Controller
from web.web_client_api import w2capi, w2c, W2CSchema

@w2capi(name=b'comp7', key=b'action')
class Comp7WebApi(W2CSchema):
    __comp7Controller = dependency.descriptor(IComp7Controller)

    @w2c(W2CSchema, name=b'get_gamemode_state')
    def getGamemodeState(self, _):
        return {b'isEnabled': (self.__comp7Controller.isEnabled())}
