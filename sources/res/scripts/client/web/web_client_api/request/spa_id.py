from helpers import dependency
from skeletons.connection_mgr import IConnectionManager
from web.web_client_api import w2c, W2CSchema

class SpaIdWebApiMixin(object):
    connectionMgr = dependency.descriptor(IConnectionManager)

    @w2c(W2CSchema, b'spa_id')
    def spaId(self, cmd):
        if self.connectionMgr is not None:
            yield {b'spa_id': (str(self.connectionMgr.databaseID))}
        else:
            yield {b'error': b'Unable to obtain spa id'}
        return
