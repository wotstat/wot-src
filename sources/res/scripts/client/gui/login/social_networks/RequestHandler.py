import httplib, base64
from urlparse import urlparse, parse_qsl
from BaseHTTPServer import BaseHTTPRequestHandler
from gui import GUI_SETTINGS
_TEMPLATE_EMPTY_GIF_BASE64 = b'R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        params = dict(parse_qsl(parsed.query))
        if (b'token' in params or b'token_encrypted' in params) and path == b'/login/' and b'account_id' in params:
            if b'next' in params and params[b'next'] == GUI_SETTINGS.socialNetworkLogin[b'redirectURL']:
                self.onLoginWithRedirect(**params)
            else:
                self.onLogin(**params)
        else:
            self.send_response(httplib.NOT_FOUND)
            self.end_headers()
        return

    def onLogin(self, **kwargs):
        token, accountId, socialNetwork = self.__fetchParams(kwargs)
        self.send_response(httplib.OK)
        self.send_header(b'Content-Type', b'image/gif')
        self.end_headers()
        self.wfile.write(base64.decodestring(_TEMPLATE_EMPTY_GIF_BASE64))
        self.wfile.close()
        self.server.keepData(token, accountId, socialNetwork)
        return

    def onLoginWithRedirect(self, **kwargs):
        token, accountId, socialNetwork = self.__fetchParams(kwargs)
        self.send_response(httplib.FOUND)
        self.send_header(b'Location', kwargs[b'next'])
        self.end_headers()
        self.server.keepData(token, accountId, socialNetwork)
        return

    def __fetchParams(self, params):
        if b'token_encrypted' in params:
            token = params[b'token_encrypted']
        else:
            token = params[b'token']
        socialNetwork = params.get(b'authentication_method', b'').partition(b':')[2]
        return (
         token, params[b'account_id'], socialNetwork)

    def log_request(self, code=b'-', size=b'-'):
        return
