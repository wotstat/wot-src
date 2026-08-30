import BigWorld
from client_request_lib.requester import Requester as WebRequester
from constants import TOKEN_TYPE
from gui.shared.utils.requesters import TokenRequester, getTokenRequester
from gui.clientgw.requests import ClientgwRequester, ClientgwRequestsController
from helpers.server_settings import _Clientgw

def _webUrlFetcher(url, callback, headers=None, timeout=30.0, method=b'GET', postData=b''):
    return BigWorld.fetchURL(url, callback, headers, timeout, method, postData)


class _WebFactory(object):

    def createWebRequester(self, settings, *args, **kwargs):
        raise NotImplementedError
        return

    def createTokenRequester(self):
        raise NotImplementedError
        return

    def createClientgwRequester(self, webRequester):
        raise NotImplementedError
        return

    def createClientgwRequestsController(self, webCtrl, clanRequester):
        raise NotImplementedError
        return


class WebFactory(_WebFactory):

    def createWebRequester(self, settings, *args, **kwargs):
        return WebRequester.create_requester(_webUrlFetcher, settings, *args, **kwargs)

    def createTokenRequester(self):
        return getTokenRequester(TOKEN_TYPE.WGNI_JWT)

    def createClientgwRequester(self, webRequester):
        return ClientgwRequester(webRequester)

    def createClientgwRequestsController(self, webCtrl, clanRequester):
        return ClientgwRequestsController(webCtrl, clanRequester)


class FakeWebFactory(_WebFactory):

    def createWebRequester(self, settings, *args, **kwargs):
        return WebRequester.create_requester(_webUrlFetcher, _Clientgw(True, None, b'fake', False, False), *args, **kwargs)

    def createTokenRequester(self):
        return TokenRequester(TOKEN_TYPE.WGNI, cache=False)

    def createClientgwRequester(self, webRequester):
        return ClientgwRequester(webRequester)

    def createClientgwRequestsController(self, webCtrl, clanRequester):
        return ClientgwRequestsController(webCtrl, clanRequester)


g_webFactory = WebFactory()
