from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import urllib, sys
from wsgiref.handlers import SimpleHandler
__version__ = b'0.1'
__all__ = [b'WSGIServer', b'WSGIRequestHandler', b'demo_app', b'make_server']
server_version = b'WSGIServer/' + __version__
sys_version = b'Python/' + sys.version.split()[0]
software_version = server_version + b' ' + sys_version

class ServerHandler(SimpleHandler):
    server_software = software_version

    def close(self):
        try:
            self.request_handler.log_request(self.status.split(b' ', 1)[0], self.bytes_sent)
        finally:
            SimpleHandler.close(self)

        return


class WSGIServer(HTTPServer):
    application = None

    def server_bind(self):
        HTTPServer.server_bind(self)
        self.setup_environ()
        return

    def setup_environ(self):
        env = self.base_environ = {}
        env[b'SERVER_NAME'] = self.server_name
        env[b'GATEWAY_INTERFACE'] = b'CGI/1.1'
        env[b'SERVER_PORT'] = str(self.server_port)
        env[b'REMOTE_HOST'] = b''
        env[b'CONTENT_LENGTH'] = b''
        env[b'SCRIPT_NAME'] = b''
        return

    def get_app(self):
        return self.application

    def set_app(self, application):
        self.application = application
        return


class WSGIRequestHandler(BaseHTTPRequestHandler):
    server_version = b'WSGIServer/' + __version__

    def get_environ(self):
        env = self.server.base_environ.copy()
        env[b'SERVER_PROTOCOL'] = self.request_version
        env[b'REQUEST_METHOD'] = self.command
        if b'?' in self.path:
            path, query = self.path.split(b'?', 1)
        else:
            path, query = self.path, b''
        env[b'PATH_INFO'] = urllib.unquote(path)
        env[b'QUERY_STRING'] = query
        host = self.address_string()
        if host != self.client_address[0]:
            env[b'REMOTE_HOST'] = host
        env[b'REMOTE_ADDR'] = self.client_address[0]
        if self.headers.typeheader is None:
            env[b'CONTENT_TYPE'] = self.headers.type
        else:
            env[b'CONTENT_TYPE'] = self.headers.typeheader
        length = self.headers.getheader(b'content-length')
        if length:
            env[b'CONTENT_LENGTH'] = length
        for h in self.headers.headers:
            k, v = h.split(b':', 1)
            k = k.replace(b'-', b'_').upper()
            v = v.strip()
            if k in env:
                continue
            if b'HTTP_' + k in env:
                env[b'HTTP_' + k] += b',' + v
            else:
                env[b'HTTP_' + k] = v

        return env

    def get_stderr(self):
        return sys.stderr

    def handle(self):
        self.raw_requestline = self.rfile.readline(65537)
        if len(self.raw_requestline) > 65536:
            self.requestline = b''
            self.request_version = b''
            self.command = b''
            self.send_error(414)
            return
        if not self.parse_request():
            return
        handler = ServerHandler(self.rfile, self.wfile, self.get_stderr(), self.get_environ())
        handler.request_handler = self
        handler.run(self.server.get_app())
        return


def demo_app(environ, start_response):
    from StringIO import StringIO
    stdout = StringIO()
    print >> stdout, b'Hello world!'
    print >> stdout
    h = environ.items()
    h.sort()
    for k, v in h:
        print >> stdout, k, b'=', repr(v)

    start_response(b'200 OK', [(b'Content-Type', b'text/plain')])
    return [stdout.getvalue()]


def make_server(host, port, app, server_class=WSGIServer, handler_class=WSGIRequestHandler):
    server = server_class((host, port), handler_class)
    server.set_app(app)
    return server


if __name__ == b'__main__':
    httpd = make_server(b'', 8000, demo_app)
    sa = httpd.socket.getsockname()
    print b'Serving HTTP on', sa[0], b'port', sa[1], b'...'
    import webbrowser
    webbrowser.open(b'http://localhost:8000/xyz?abc')
    httpd.handle_request()
    httpd.server_close()
