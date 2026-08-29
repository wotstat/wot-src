from constants import TOKEN_TYPE
from gui.shared.utils.requesters import getTokenRequester
from web.web_client_api import w2c, W2CSchema

class WgniTokenWebApiMixin(object):

    @w2c(W2CSchema, b'token1')
    def wgniToken(self, cmd):
        tokenRqs = getTokenRequester(TOKEN_TYPE.WGNI)
        if not tokenRqs.isInProcess():
            response = yield tokenRqs.request(timeout=10.0)
        else:
            response = None
        if response and response.isValid():
            yield {b'request_id': b'token1', b'spa_id': (str(response.getDatabaseID())), 
               b'token': (response.getToken())}
        else:
            coolDownExpiration = tokenRqs.getReqCoolDown() - tokenRqs.lastResponseDelta()
            yield {b'request_id': b'token1', 
               b'error': b'Unable to obtain token.', 
               b'cooldown': (coolDownExpiration if coolDownExpiration > 0 else tokenRqs.getReqCoolDown())}
        return
