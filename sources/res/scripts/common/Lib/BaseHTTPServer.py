__version__ = b'0.3'
__all__ = [
 b'HTTPServer', b'BaseHTTPRequestHandler']
import sys, time, socket
from warnings import filterwarnings, catch_warnings
with catch_warnings():
    if sys.py3kwarning:
        filterwarnings(b'ignore', b'.*mimetools has been removed', DeprecationWarning)
    import mimetools
import SocketServer
DEFAULT_ERROR_MESSAGE = b'<head>\n<title>Error response</title>\n</head>\n<body>\n<h1>Error response</h1>\n<p>Error code %(code)d.\n<p>Message: %(message)s.\n<p>Error code explanation: %(code)s = %(explain)s.\n</body>\n'
DEFAULT_ERROR_CONTENT_TYPE = b'text/html'

def _quote_html(html):
    return html.replace(b'&', b'&amp;').replace(b'<', b'&lt;').replace(b'>', b'&gt;')


class HTTPServer(SocketServer.TCPServer):
    allow_reuse_address = 1

    def server_bind(self):
        SocketServer.TCPServer.server_bind(self)
        host, port = self.socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        return


class BaseHTTPRequestHandler(SocketServer.StreamRequestHandler):
    sys_version = b'Python/' + sys.version.split()[0]
    server_version = b'BaseHTTP/' + __version__
    default_request_version = b'HTTP/0.9'

    def parse_request(self):
        self.command = None
        self.request_version = version = self.default_request_version
        self.close_connection = 1
        requestline = self.raw_requestline
        requestline = requestline.rstrip(b'\r\n')
        self.requestline = requestline
        words = requestline.split()
        if len(words) == 3:
            command, path, version = words
            if version[:5] != b'HTTP/':
                self.send_error(400, b'Bad request version (%r)' % version)
                return False
            try:
                base_version_number = version.split(b'/', 1)[1]
                version_number = base_version_number.split(b'.')
                if len(version_number) != 2:
                    raise ValueError
                version_number = (
                 int(version_number[0]), int(version_number[1]))
            except (ValueError, IndexError):
                self.send_error(400, b'Bad request version (%r)' % version)
                return False

            if version_number >= (1, 1) and self.protocol_version >= b'HTTP/1.1':
                self.close_connection = 0
            if version_number >= (2, 0):
                self.send_error(505, b'Invalid HTTP Version (%s)' % base_version_number)
                return False
        elif len(words) == 2:
            command, path = words
            self.close_connection = 1
            if command != b'GET':
                self.send_error(400, b'Bad HTTP/0.9 request type (%r)' % command)
                return False
        else:
            if not words:
                return False
            else:
                self.send_error(400, b'Bad request syntax (%r)' % requestline)
                return False

        self.command, self.path, self.request_version = command, path, version
        self.headers = self.MessageClass(self.rfile, 0)
        conntype = self.headers.get(b'Connection', b'')
        if conntype.lower() == b'close':
            self.close_connection = 1
        elif conntype.lower() == b'keep-alive' and self.protocol_version >= b'HTTP/1.1':
            self.close_connection = 0
        return True

    def handle_one_request(self):
        try:
            self.raw_requestline = self.rfile.readline(65537)
            if len(self.raw_requestline) > 65536:
                self.requestline = b''
                self.request_version = b''
                self.command = b''
                self.send_error(414)
                return
            if not self.raw_requestline:
                self.close_connection = 1
                return
            if not self.parse_request():
                return
            mname = b'do_' + self.command
            if not hasattr(self, mname):
                self.send_error(501, b'Unsupported method (%r)' % self.command)
                return
            method = getattr(self, mname)
            method()
            self.wfile.flush()
        except socket.timeout as e:
            self.log_error(b'Request timed out: %r', e)
            self.close_connection = 1
            return

        return

    def handle(self):
        self.close_connection = 1
        self.handle_one_request()
        while not self.close_connection:
            self.handle_one_request()

        return

    def send_error(self, code, message=None):
        try:
            short, long = self.responses[code]
        except KeyError:
            short, long = (b'???', b'???')

        if message is None:
            message = short
        explain = long
        self.log_error(b'code %d, message %s', code, message)
        self.send_response(code, message)
        self.send_header(b'Connection', b'close')
        content = None
        if code >= 200 and code not in (204, 205, 304):
            content = self.error_message_format % {b'code': code, 
               b'message': (_quote_html(message)), 
               b'explain': explain}
            self.send_header(b'Content-Type', self.error_content_type)
        self.end_headers()
        if self.command != b'HEAD' and content:
            self.wfile.write(content)
        return

    error_message_format = DEFAULT_ERROR_MESSAGE
    error_content_type = DEFAULT_ERROR_CONTENT_TYPE

    def send_response(self, code, message=None):
        self.log_request(code)
        if message is None:
            if code in self.responses:
                message = self.responses[code][0]
            else:
                message = b''
        if self.request_version != b'HTTP/0.9':
            self.wfile.write(b'%s %d %s\r\n' % (
             self.protocol_version, code, message))
        self.send_header(b'Server', self.version_string())
        self.send_header(b'Date', self.date_time_string())
        return

    def send_header(self, keyword, value):
        if self.request_version != b'HTTP/0.9':
            self.wfile.write(b'%s: %s\r\n' % (keyword, value))
        if keyword.lower() == b'connection':
            if value.lower() == b'close':
                self.close_connection = 1
            elif value.lower() == b'keep-alive':
                self.close_connection = 0
        return

    def end_headers(self):
        if self.request_version != b'HTTP/0.9':
            self.wfile.write(b'\r\n')
        return

    def log_request(self, code=b'-', size=b'-'):
        self.log_message(b'"%s" %s %s', self.requestline, str(code), str(size))
        return

    def log_error(self, format, *args):
        self.log_message(format, *args)
        return

    def log_message(self, format, *args):
        sys.stderr.write(b'%s - - [%s] %s\n' % (
         self.client_address[0],
         self.log_date_time_string(),
         format % args))
        return

    def version_string(self):
        return self.server_version + b' ' + self.sys_version

    def date_time_string(self, timestamp=None):
        if timestamp is None:
            timestamp = time.time()
        year, month, day, hh, mm, ss, wd, y, z = time.gmtime(timestamp)
        s = b'%s, %02d %3s %4d %02d:%02d:%02d GMT' % (
         self.weekdayname[wd],
         day, self.monthname[month], year,
         hh, mm, ss)
        return s

    def log_date_time_string(self):
        now = time.time()
        year, month, day, hh, mm, ss, x, y, z = time.localtime(now)
        s = b'%02d/%3s/%04d %02d:%02d:%02d' % (
         day, self.monthname[month], year, hh, mm, ss)
        return s

    weekdayname = [
     18, 19, 20, 21, 22, 23, 24]
    monthname = [
     158, 
     25, 26, 27, 28, 29, 30, 
     31, 32, 
     33, 34, 35, 36]

    def address_string(self):
        host, port = self.client_address[:2]
        return socket.getfqdn(host)

    protocol_version = b'HTTP/1.0'
    MessageClass = mimetools.Message
    responses = {100: (b'Continue', b'Request received, please continue'), 
       101: (b'Switching Protocols', b'Switching to new protocol; obey Upgrade header'), 
       200: (b'OK', b'Request fulfilled, document follows'), 
       201: (b'Created', b'Document created, URL follows'), 
       202: (b'Accepted', b'Request accepted, processing continues off-line'), 
       203: (b'Non-Authoritative Information', b'Request fulfilled from cache'), 
       204: (b'No Content', b'Request fulfilled, nothing follows'), 
       205: (b'Reset Content', b'Clear input form for further input.'), 
       206: (b'Partial Content', b'Partial content follows.'), 
       300: (b'Multiple Choices', b'Object has several resources -- see URI list'), 
       301: (b'Moved Permanently', b'Object moved permanently -- see URI list'), 
       302: (b'Found', b'Object moved temporarily -- see URI list'), 
       303: (b'See Other', b'Object moved -- see Method and URL list'), 
       304: (b'Not Modified', b'Document has not changed since given time'), 
       305: (b'Use Proxy', b'You must use proxy specified in Location to access this resource.'), 
       307: (b'Temporary Redirect', b'Object moved temporarily -- see URI list'), 
       400: (b'Bad Request', b'Bad request syntax or unsupported method'), 
       401: (b'Unauthorized', b'No permission -- see authorization schemes'), 
       402: (b'Payment Required', b'No payment -- see charging schemes'), 
       403: (b'Forbidden', b'Request forbidden -- authorization will not help'), 
       404: (b'Not Found', b'Nothing matches the given URI'), 
       405: (b'Method Not Allowed', b'Specified method is invalid for this resource.'), 
       406: (b'Not Acceptable', b'URI not available in preferred format.'), 
       407: (b'Proxy Authentication Required', b'You must authenticate with this proxy before proceeding.'), 
       408: (b'Request Timeout', b'Request timed out; try again later.'), 
       409: (b'Conflict', b'Request conflict.'), 
       410: (b'Gone', b'URI no longer exists and has been permanently removed.'), 
       411: (b'Length Required', b'Client must specify Content-Length.'), 
       412: (b'Precondition Failed', b'Precondition in headers is false.'), 
       413: (b'Request Entity Too Large', b'Entity is too large.'), 
       414: (b'Request-URI Too Long', b'URI is too long.'), 
       415: (b'Unsupported Media Type', b'Entity body in unsupported format.'), 
       416: (b'Requested Range Not Satisfiable', b'Cannot satisfy request range.'), 
       417: (b'Expectation Failed', b'Expect condition could not be satisfied.'), 
       500: (b'Internal Server Error', b'Server got itself in trouble'), 
       501: (b'Not Implemented', b'Server does not support this operation'), 
       502: (b'Bad Gateway', b'Invalid responses from another server/proxy.'), 
       503: (b'Service Unavailable', b'The server cannot process the request due to a high load'), 
       504: (b'Gateway Timeout', b'The gateway server did not receive a timely response'), 
       505: (b'HTTP Version Not Supported', b'Cannot fulfill request.')}


def test(HandlerClass=BaseHTTPRequestHandler, ServerClass=HTTPServer, protocol=b'HTTP/1.0'):
    if sys.argv[1:]:
        port = int(sys.argv[1])
    else:
        port = 8000
    server_address = (
     b'', port)
    HandlerClass.protocol_version = protocol
    httpd = ServerClass(server_address, HandlerClass)
    sa = httpd.socket.getsockname()
    print b'Serving HTTP on', sa[0], b'port', sa[1], b'...'
    httpd.serve_forever()
    return


if __name__ == b'__main__':
    test()
