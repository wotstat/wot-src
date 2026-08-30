from types import StringType
from util import FileWrapper, guess_scheme, is_hop_by_hop
from headers import Headers
import sys, os, time
__all__ = [
 b'BaseHandler', b'SimpleHandler', b'BaseCGIHandler', b'CGIHandler']
try:
    dict
except NameError:

    def dict(items):
        d = {}
        for k, v in items:
            d[k] = v

        return d


_weekdayname = [
 10, 11, 12, 13, 14, 15, 16]
_monthname = [None, 
 17, 18, 19, 20, 21, 22, 
 23, 24, 25, 26, 27, 28]

def format_date_time(timestamp):
    year, month, day, hh, mm, ss, wd, y, z = time.gmtime(timestamp)
    return b'%s, %02d %3s %4d %02d:%02d:%02d GMT' % (
     _weekdayname[wd], day, _monthname[month], year, hh, mm, ss)


class BaseHandler():
    wsgi_version = (1, 0)
    wsgi_multithread = True
    wsgi_multiprocess = True
    wsgi_run_once = False
    origin_server = True
    http_version = b'1.0'
    server_software = None
    os_environ = dict(os.environ.items())
    wsgi_file_wrapper = FileWrapper
    headers_class = Headers
    traceback_limit = None
    error_status = b'500 Internal Server Error'
    error_headers = [(b'Content-Type', b'text/plain')]
    error_body = b'A server error occurred.  Please contact the administrator.'
    status = result = None
    headers_sent = False
    headers = None
    bytes_sent = 0

    def run(self, application):
        try:
            self.setup_environ()
            self.result = application(self.environ, self.start_response)
            self.finish_response()
        except:
            try:
                self.handle_error()
            except:
                self.close()
                raise

        return

    def setup_environ(self):
        env = self.environ = self.os_environ.copy()
        self.add_cgi_vars()
        env[b'wsgi.input'] = self.get_stdin()
        env[b'wsgi.errors'] = self.get_stderr()
        env[b'wsgi.version'] = self.wsgi_version
        env[b'wsgi.run_once'] = self.wsgi_run_once
        env[b'wsgi.url_scheme'] = self.get_scheme()
        env[b'wsgi.multithread'] = self.wsgi_multithread
        env[b'wsgi.multiprocess'] = self.wsgi_multiprocess
        if self.wsgi_file_wrapper is not None:
            env[b'wsgi.file_wrapper'] = self.wsgi_file_wrapper
        if self.origin_server and self.server_software:
            env.setdefault(b'SERVER_SOFTWARE', self.server_software)
        return

    def finish_response(self):
        try:
            if not self.result_is_file() or not self.sendfile():
                for data in self.result:
                    self.write(data)

                self.finish_content()
        finally:
            self.close()

        return

    def get_scheme(self):
        return guess_scheme(self.environ)

    def set_content_length(self):
        try:
            blocks = len(self.result)
        except (TypeError, AttributeError, NotImplementedError):
            pass
        else:
            if blocks == 1:
                self.headers[b'Content-Length'] = str(self.bytes_sent)
                return

        return

    def cleanup_headers(self):
        if b'Content-Length' not in self.headers:
            self.set_content_length()
        return

    def start_response(self, status, headers, exc_info=None):
        if exc_info:
            try:
                if self.headers_sent:
                    raise exc_info[0], exc_info[1], exc_info[2]
            finally:
                exc_info = None

        elif self.headers is not None:
            raise AssertionError(b'Headers already set!')
        self.status = status
        self.headers = self.headers_class(headers)
        return self.write

    def send_preamble(self):
        if self.origin_server:
            if self.client_is_modern():
                self._write(b'HTTP/%s %s\r\n' % (self.http_version, self.status))
                if b'Date' not in self.headers:
                    self._write(b'Date: %s\r\n' % format_date_time(time.time()))
                if self.server_software and b'Server' not in self.headers:
                    self._write(b'Server: %s\r\n' % self.server_software)
        else:
            self._write(b'Status: %s\r\n' % self.status)
        return

    def write(self, data):
        if not self.status:
            raise AssertionError(b'write() before start_response()')
        elif not self.headers_sent:
            self.bytes_sent = len(data)
            self.send_headers()
        else:
            self.bytes_sent += len(data)
        self._write(data)
        self._flush()
        return

    def sendfile(self):
        return False

    def finish_content(self):
        if not self.headers_sent:
            self.headers.setdefault(b'Content-Length', b'0')
            self.send_headers()
        return

    def close(self):
        try:
            if hasattr(self.result, b'close'):
                self.result.close()
        finally:
            self.result = self.headers = self.status = self.environ = None
            self.bytes_sent = 0
            self.headers_sent = False

        return

    def send_headers(self):
        self.cleanup_headers()
        self.headers_sent = True
        if not self.origin_server or self.client_is_modern():
            self.send_preamble()
            self._write(str(self.headers))
        return

    def result_is_file(self):
        wrapper = self.wsgi_file_wrapper
        return wrapper is not None and isinstance(self.result, wrapper)

    def client_is_modern(self):
        return self.environ[b'SERVER_PROTOCOL'].upper() != b'HTTP/0.9'

    def log_exception(self, exc_info):
        try:
            from traceback import print_exception
            stderr = self.get_stderr()
            print_exception(exc_info[0], exc_info[1], exc_info[2], self.traceback_limit, stderr)
            stderr.flush()
        finally:
            exc_info = None

        return

    def handle_error(self):
        self.log_exception(sys.exc_info())
        if not self.headers_sent:
            self.result = self.error_output(self.environ, self.start_response)
            self.finish_response()
        return

    def error_output(self, environ, start_response):
        start_response(self.error_status, self.error_headers[:], sys.exc_info())
        return [self.error_body]

    def _write(self, data):
        raise NotImplementedError
        return

    def _flush(self):
        raise NotImplementedError
        return

    def get_stdin(self):
        raise NotImplementedError
        return

    def get_stderr(self):
        raise NotImplementedError
        return

    def add_cgi_vars(self):
        raise NotImplementedError
        return


class SimpleHandler(BaseHandler):

    def __init__(self, stdin, stdout, stderr, environ, multithread=True, multiprocess=False):
        self.stdin = stdin
        self.stdout = stdout
        self.stderr = stderr
        self.base_env = environ
        self.wsgi_multithread = multithread
        self.wsgi_multiprocess = multiprocess
        return

    def get_stdin(self):
        return self.stdin

    def get_stderr(self):
        return self.stderr

    def add_cgi_vars(self):
        self.environ.update(self.base_env)
        return

    def _write(self, data):
        self.stdout.write(data)
        self._write = self.stdout.write
        return

    def _flush(self):
        self.stdout.flush()
        self._flush = self.stdout.flush
        return


class BaseCGIHandler(SimpleHandler):
    origin_server = False


class CGIHandler(BaseCGIHandler):
    wsgi_run_once = True
    os_environ = {}

    def __init__(self):
        BaseCGIHandler.__init__(self, sys.stdin, sys.stdout, sys.stderr, dict(os.environ.items()), multithread=False, multiprocess=True)
        return
