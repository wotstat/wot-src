__all__ = [
 b'validator']
import re, sys
from types import DictType, StringType, TupleType, ListType
import warnings
header_re = re.compile(b'^[a-zA-Z][a-zA-Z0-9\\-_]*$')
bad_header_value_re = re.compile(b'[\\000-\\037]')

class WSGIWarning(Warning):
    pass


def assert_(cond, *args):
    assert cond, args
    return


def validator(application):

    def lint_app(*args, **kw):
        assert_(len(args) == 2, b'Two arguments required')
        assert_(not kw, b'No keyword arguments allowed')
        environ, start_response = args
        check_environ(environ)
        start_response_started = []

        def start_response_wrapper(*args, **kw):
            assert_(len(args) == 2 or len(args) == 3, b'Invalid number of arguments: %s' % (args,))
            assert_(not kw, b'No keyword arguments allowed')
            status = args[0]
            headers = args[1]
            if len(args) == 3:
                exc_info = args[2]
            else:
                exc_info = None
            check_status(status)
            check_headers(headers)
            check_content_type(status, headers)
            check_exc_info(exc_info)
            start_response_started.append(None)
            return WriteWrapper(start_response(*args))

        environ[b'wsgi.input'] = InputWrapper(environ[b'wsgi.input'])
        environ[b'wsgi.errors'] = ErrorWrapper(environ[b'wsgi.errors'])
        iterator = application(environ, start_response_wrapper)
        assert_(iterator is not None and iterator != False, b'The application must return an iterator, if only an empty list')
        check_iterator(iterator)
        return IteratorWrapper(iterator, start_response_started)

    return lint_app


class InputWrapper:

    def __init__(self, wsgi_input):
        self.input = wsgi_input
        return

    def read(self, *args):
        assert_(len(args) <= 1)
        v = self.input.read(*args)
        assert_(type(v) is type(b''))
        return v

    def readline(self):
        v = self.input.readline()
        assert_(type(v) is type(b''))
        return v

    def readlines(self, *args):
        assert_(len(args) <= 1)
        lines = self.input.readlines(*args)
        assert_(type(lines) is type([]))
        for line in lines:
            assert_(type(line) is type(b''))

        return lines

    def __iter__(self):
        while 1:
            line = self.readline()
            if not line:
                return
            yield line

        return

    def close(self):
        assert_(0, b'input.close() must not be called')
        return


class ErrorWrapper:

    def __init__(self, wsgi_errors):
        self.errors = wsgi_errors
        return

    def write(self, s):
        assert_(type(s) is type(b''))
        self.errors.write(s)
        return

    def flush(self):
        self.errors.flush()
        return

    def writelines(self, seq):
        for line in seq:
            self.write(line)

        return

    def close(self):
        assert_(0, b'errors.close() must not be called')
        return


class WriteWrapper:

    def __init__(self, wsgi_writer):
        self.writer = wsgi_writer
        return

    def __call__(self, s):
        assert_(type(s) is type(b''))
        self.writer(s)
        return


class PartialIteratorWrapper:

    def __init__(self, wsgi_iterator):
        self.iterator = wsgi_iterator
        return

    def __iter__(self):
        return IteratorWrapper(self.iterator, None)


class IteratorWrapper:

    def __init__(self, wsgi_iterator, check_start_response):
        self.original_iterator = wsgi_iterator
        self.iterator = iter(wsgi_iterator)
        self.closed = False
        self.check_start_response = check_start_response
        return

    def __iter__(self):
        return self

    def next(self):
        assert_(not self.closed, b'Iterator read after closed')
        v = self.iterator.next()
        if self.check_start_response is not None:
            assert_(self.check_start_response, b'The application returns and we started iterating over its body, but start_response has not yet been called')
            self.check_start_response = None
        return v

    def close(self):
        self.closed = True
        if hasattr(self.original_iterator, b'close'):
            self.original_iterator.close()
        return

    def __del__(self):
        if not self.closed:
            sys.stderr.write(b'Iterator garbage collected without being closed')
        assert_(self.closed, b'Iterator garbage collected without being closed')
        return


def check_environ(environ):
    assert_(type(environ) is DictType, b'Environment is not of the right type: %r (environment: %r)' % (
     type(environ), environ))
    for key in [2, 3, 4, 
     5, 6, 7, 
     8, 9, 
     10]:
        assert_(key in environ, b'Environment missing required key: %r' % (key,))

    for key in [b'HTTP_CONTENT_TYPE', b'HTTP_CONTENT_LENGTH']:
        assert_(key not in environ, b'Environment should not have the key: %s (use %s instead)' % (
         key, key[5:]))

    if b'QUERY_STRING' not in environ:
        warnings.warn(b'QUERY_STRING is not in the WSGI environment; the cgi module will use sys.argv when this variable is missing, so application errors are more likely', WSGIWarning)
    for key in environ.keys():
        if b'.' in key:
            continue
        assert_(type(environ[key]) is StringType, b'Environmental variable %s is not a string: %r (value: %r)' % (
         key, type(environ[key]), environ[key]))

    assert_(type(environ[b'wsgi.version']) is TupleType, b'wsgi.version should be a tuple (%r)' % (environ[b'wsgi.version'],))
    assert_(environ[b'wsgi.url_scheme'] in (b'http', b'https'), b'wsgi.url_scheme unknown: %r' % environ[b'wsgi.url_scheme'])
    check_input(environ[b'wsgi.input'])
    check_errors(environ[b'wsgi.errors'])
    if environ[b'REQUEST_METHOD'] not in (b'GET', b'HEAD', b'POST', b'OPTIONS', b'PATCH', b'PUT', b'DELETE', b'TRACE'):
        warnings.warn(b'Unknown REQUEST_METHOD: %r' % environ[b'REQUEST_METHOD'], WSGIWarning)
    assert_(not environ.get(b'SCRIPT_NAME') or environ[b'SCRIPT_NAME'].startswith(b'/'), b"SCRIPT_NAME doesn't start with /: %r" % environ[b'SCRIPT_NAME'])
    assert_(not environ.get(b'PATH_INFO') or environ[b'PATH_INFO'].startswith(b'/'), b"PATH_INFO doesn't start with /: %r" % environ[b'PATH_INFO'])
    if environ.get(b'CONTENT_LENGTH'):
        assert_(int(environ[b'CONTENT_LENGTH']) >= 0, b'Invalid CONTENT_LENGTH: %r' % environ[b'CONTENT_LENGTH'])
    if not environ.get(b'SCRIPT_NAME'):
        assert_(b'PATH_INFO' in environ, b"One of SCRIPT_NAME or PATH_INFO are required (PATH_INFO should at least be '/' if SCRIPT_NAME is empty)")
    assert_(environ.get(b'SCRIPT_NAME') != b'/', b"SCRIPT_NAME cannot be '/'; it should instead be '', and PATH_INFO should be '/'")
    return


def check_input(wsgi_input):
    for attr in [b'read', b'readline', b'readlines', b'__iter__']:
        assert_(hasattr(wsgi_input, attr), b"wsgi.input (%r) doesn't have the attribute %s" % (
         wsgi_input, attr))

    return


def check_errors(wsgi_errors):
    for attr in [b'flush', b'write', b'writelines']:
        assert_(hasattr(wsgi_errors, attr), b"wsgi.errors (%r) doesn't have the attribute %s" % (
         wsgi_errors, attr))

    return


def check_status(status):
    assert_(type(status) is StringType, b'Status must be a string (not %r)' % status)
    status_code = status.split(None, 1)[0]
    assert_(len(status_code) == 3, b'Status codes must be three characters: %r' % status_code)
    status_int = int(status_code)
    assert_(status_int >= 100, b'Status code is invalid: %r' % status_int)
    if len(status) < 4 or status[3] != b' ':
        warnings.warn(b'The status string (%r) should be a three-digit integer followed by a single space and a status explanation' % status, WSGIWarning)
    return


def check_headers(headers):
    assert_(type(headers) is ListType, b'Headers (%r) must be of type list: %r' % (
     headers, type(headers)))
    header_names = {}
    for item in headers:
        assert_(type(item) is TupleType, b'Individual headers (%r) must be of type tuple: %r' % (
         item, type(item)))
        assert_(len(item) == 2)
        name, value = item
        assert_(name.lower() != b'status', b'The Status header cannot be used; it conflicts with CGI script, and HTTP status is not given through headers (value: %r).' % value)
        header_names[name.lower()] = None
        assert_(b'\n' not in name and b':' not in name, b"Header names may not contain ':' or '\\n': %r" % name)
        assert_(header_re.search(name), b'Bad header name: %r' % name)
        assert_(not name.endswith(b'-') and not name.endswith(b'_'), b"Names may not end in '-' or '_': %r" % name)
        if bad_header_value_re.search(value):
            assert_(0, b'Bad header value: %r (bad char: %r)' % (
             value, bad_header_value_re.search(value).group(0)))

    return


def check_content_type(status, headers):
    code = int(status.split(None, 1)[0])
    NO_MESSAGE_BODY = (204, 304)
    for name, value in headers:
        if name.lower() == b'content-type':
            if code not in NO_MESSAGE_BODY:
                return
            assert_(0, b'Content-Type header found in a %s response, which must not return content.' % code)

    if code not in NO_MESSAGE_BODY:
        assert_(0, b'No Content-Type header found in headers (%s)' % headers)
    return


def check_exc_info(exc_info):
    assert_(exc_info is None or type(exc_info) is type(()), b'exc_info (%r) is not a tuple: %r' % (exc_info, type(exc_info)))
    return


def check_iterator(iterator):
    assert_(not isinstance(iterator, str), b'You should not return a string as your application iterator, instead return a single-item list containing that string.')
    return
