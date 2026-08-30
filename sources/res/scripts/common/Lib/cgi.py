__version__ = b'2.6'
from operator import attrgetter
import sys, os, UserDict, urlparse
from warnings import filterwarnings, catch_warnings, warn
with catch_warnings():
    if sys.py3kwarning:
        filterwarnings(b'ignore', b'.*mimetools has been removed', DeprecationWarning)
        filterwarnings(b'ignore', b'.*rfc822 has been removed', DeprecationWarning)
    import mimetools, rfc822
try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

__all__ = [
 9, 10, 11, 
 12, 13, 14, 
 15, 16, 17, 18, 
 19, 20, 21, 
 22, 
 23, 24, 
 25, 26]
logfile = b''
logfp = None

def initlog(*allargs):
    global log
    global logfp
    if logfile and not logfp:
        try:
            logfp = open(logfile, b'a')
        except IOError:
            pass

    if not logfp:
        log = nolog
    else:
        log = dolog
    log(*allargs)
    return


def dolog(fmt, *args):
    logfp.write(fmt % args + b'\n')
    return


def nolog(*allargs):
    return


log = initlog
maxlen = 0

def parse(fp=None, environ=os.environ, keep_blank_values=0, strict_parsing=0):
    global maxlen
    if fp is None:
        fp = sys.stdin
    if b'REQUEST_METHOD' not in environ:
        environ[b'REQUEST_METHOD'] = b'GET'
    if environ[b'REQUEST_METHOD'] == b'POST':
        ctype, pdict = parse_header(environ[b'CONTENT_TYPE'])
        if ctype == b'multipart/form-data':
            return parse_multipart(fp, pdict)
        if ctype == b'application/x-www-form-urlencoded':
            clength = int(environ[b'CONTENT_LENGTH'])
            if maxlen and clength > maxlen:
                raise ValueError, b'Maximum content length exceeded'
            qs = fp.read(clength)
        else:
            qs = b''
        if b'QUERY_STRING' in environ:
            if qs:
                qs = qs + b'&'
            qs = qs + environ[b'QUERY_STRING']
        elif sys.argv[1:]:
            if qs:
                qs = qs + b'&'
            qs = qs + sys.argv[1]
        environ[b'QUERY_STRING'] = qs
    elif b'QUERY_STRING' in environ:
        qs = environ[b'QUERY_STRING']
    else:
        if sys.argv[1:]:
            qs = sys.argv[1]
        else:
            qs = b''
        environ[b'QUERY_STRING'] = qs
    return urlparse.parse_qs(qs, keep_blank_values, strict_parsing)


def parse_qs(qs, keep_blank_values=0, strict_parsing=0):
    warn(b'cgi.parse_qs is deprecated, use urlparse.parse_qs instead', PendingDeprecationWarning, 2)
    return urlparse.parse_qs(qs, keep_blank_values, strict_parsing)


def parse_qsl(qs, keep_blank_values=0, strict_parsing=0, max_num_fields=None):
    warn(b'cgi.parse_qsl is deprecated, use urlparse.parse_qsl instead', PendingDeprecationWarning, 2)
    return urlparse.parse_qsl(qs, keep_blank_values, strict_parsing, max_num_fields)


def parse_multipart(fp, pdict):
    boundary = b''
    if b'boundary' in pdict:
        boundary = pdict[b'boundary']
    if not valid_boundary(boundary):
        raise ValueError, b'Invalid boundary in multipart form: %r' % (
         boundary,)
    nextpart = b'--' + boundary
    lastpart = b'--' + boundary + b'--'
    partdict = {}
    terminator = b''
    while terminator != lastpart:
        bytes = -1
        data = None
        if terminator:
            headers = mimetools.Message(fp)
            clength = headers.getheader(b'content-length')
            if clength:
                try:
                    bytes = int(clength)
                except ValueError:
                    pass

            if bytes > 0:
                if maxlen and bytes > maxlen:
                    raise ValueError, b'Maximum content length exceeded'
                data = fp.read(bytes)
            else:
                data = b''
        lines = []
        while 1:
            line = fp.readline()
            if not line:
                terminator = lastpart
                break
            if line[:2] == b'--':
                terminator = line.strip()
                if terminator in (nextpart, lastpart):
                    break
            lines.append(line)

        if data is None:
            continue
        if bytes < 0:
            if lines:
                line = lines[-1]
                if line[-2:] == b'\r\n':
                    line = line[:-2]
                elif line[-1:] == b'\n':
                    line = line[:-1]
                lines[-1] = line
                data = (b'').join(lines)
        line = headers[b'content-disposition']
        if not line:
            continue
        key, params = parse_header(line)
        if key != b'form-data':
            continue
        if b'name' in params:
            name = params[b'name']
        else:
            continue
        if name in partdict:
            partdict[name].append(data)
        else:
            partdict[name] = [
             data]

    return partdict


def _parseparam(s):
    while s[:1] == b';':
        s = s[1:]
        end = s.find(b';')
        while end > 0 and (s.count(b'"', 0, end) - s.count(b'\\"', 0, end)) % 2:
            end = s.find(b';', end + 1)

        if end < 0:
            end = len(s)
        f = s[:end]
        yield f.strip()
        s = s[end:]

    return


def parse_header(line):
    parts = _parseparam(b';' + line)
    key = parts.next()
    pdict = {}
    for p in parts:
        i = p.find(b'=')
        if i >= 0:
            name = p[:i].strip().lower()
            value = p[i + 1:].strip()
            if len(value) >= 2 and value[0] == value[-1] == b'"':
                value = value[1:-1]
                value = value.replace(b'\\\\', b'\\').replace(b'\\"', b'"')
            pdict[name] = value

    return (
     key, pdict)


class MiniFieldStorage():
    filename = None
    list = None
    type = None
    file = None
    type_options = {}
    disposition = None
    disposition_options = {}
    headers = {}

    def __init__(self, name, value):
        self.name = name
        self.value = value
        return

    def __repr__(self):
        return b'MiniFieldStorage(%r, %r)' % (self.name, self.value)


class FieldStorage():

    def __init__(self, fp=None, headers=None, outerboundary=b'', environ=os.environ, keep_blank_values=0, strict_parsing=0, max_num_fields=None):
        method = b'GET'
        self.keep_blank_values = keep_blank_values
        self.strict_parsing = strict_parsing
        self.max_num_fields = max_num_fields
        if b'REQUEST_METHOD' in environ:
            method = environ[b'REQUEST_METHOD'].upper()
        self.qs_on_post = None
        if method == b'GET' or method == b'HEAD':
            if b'QUERY_STRING' in environ:
                qs = environ[b'QUERY_STRING']
            elif sys.argv[1:]:
                qs = sys.argv[1]
            else:
                qs = b''
            fp = StringIO(qs)
            if headers is None:
                headers = {b'content-type': b'application/x-www-form-urlencoded'}
        if headers is None:
            headers = {}
            if method == b'POST':
                headers[b'content-type'] = b'application/x-www-form-urlencoded'
            if b'CONTENT_TYPE' in environ:
                headers[b'content-type'] = environ[b'CONTENT_TYPE']
            if b'QUERY_STRING' in environ:
                self.qs_on_post = environ[b'QUERY_STRING']
            if b'CONTENT_LENGTH' in environ:
                headers[b'content-length'] = environ[b'CONTENT_LENGTH']
        self.fp = fp or sys.stdin
        self.headers = headers
        self.outerboundary = outerboundary
        cdisp, pdict = b'', {}
        if b'content-disposition' in self.headers:
            cdisp, pdict = parse_header(self.headers[b'content-disposition'])
        self.disposition = cdisp
        self.disposition_options = pdict
        self.name = None
        if b'name' in pdict:
            self.name = pdict[b'name']
        self.filename = None
        if b'filename' in pdict:
            self.filename = pdict[b'filename']
        if b'content-type' in self.headers:
            ctype, pdict = parse_header(self.headers[b'content-type'])
        elif self.outerboundary or method != b'POST':
            ctype, pdict = b'text/plain', {}
        else:
            ctype, pdict = b'application/x-www-form-urlencoded', {}
        self.type = ctype
        self.type_options = pdict
        self.innerboundary = b''
        if b'boundary' in pdict:
            self.innerboundary = pdict[b'boundary']
        clen = -1
        if b'content-length' in self.headers:
            try:
                clen = int(self.headers[b'content-length'])
            except ValueError:
                pass

            if maxlen and clen > maxlen:
                raise ValueError, b'Maximum content length exceeded'
        self.length = clen
        self.list = self.file = None
        self.done = 0
        if ctype == b'application/x-www-form-urlencoded':
            self.read_urlencoded()
        elif ctype[:10] == b'multipart/':
            self.read_multi(environ, keep_blank_values, strict_parsing)
        else:
            self.read_single()
        return

    def __repr__(self):
        return b'FieldStorage(%r, %r, %r)' % (
         self.name, self.filename, self.value)

    def __iter__(self):
        return iter(self.keys())

    def __getattr__(self, name):
        if name != b'value':
            raise AttributeError, name
        if self.file:
            self.file.seek(0)
            value = self.file.read()
            self.file.seek(0)
        elif self.list is not None:
            value = self.list
        else:
            value = None
        return value

    def __getitem__(self, key):
        if self.list is None:
            raise TypeError, b'not indexable'
        found = []
        for item in self.list:
            if item.name == key:
                found.append(item)

        if not found:
            raise KeyError, key
        if len(found) == 1:
            return found[0]
        else:
            return found
            return

    def getvalue(self, key, default=None):
        if key in self:
            value = self[key]
            if type(value) is type([]):
                return map(attrgetter(b'value'), value)
            return value.value
        else:
            return default
        return

    def getfirst(self, key, default=None):
        if key in self:
            value = self[key]
            if type(value) is type([]):
                return value[0].value
            return value.value
        else:
            return default
        return

    def getlist(self, key):
        if key in self:
            value = self[key]
            if type(value) is type([]):
                return map(attrgetter(b'value'), value)
            return [value.value]
        else:
            return []
        return

    def keys(self):
        if self.list is None:
            raise TypeError, b'not indexable'
        return list(set(item.name for item in self.list))

    def has_key(self, key):
        if self.list is None:
            raise TypeError, b'not indexable'
        return any(item.name == key for item in self.list)

    def __contains__(self, key):
        if self.list is None:
            raise TypeError, b'not indexable'
        return any(item.name == key for item in self.list)

    def __len__(self):
        return len(self.keys())

    def __nonzero__(self):
        return bool(self.list)

    def read_urlencoded(self):
        qs = self.fp.read(self.length)
        if self.qs_on_post:
            qs += b'&' + self.qs_on_post
        query = urlparse.parse_qsl(qs, self.keep_blank_values, self.strict_parsing, self.max_num_fields)
        self.list = [MiniFieldStorage(key, value) for key, value in query]
        self.skip_lines()
        return

    FieldStorageClass = None

    def read_multi(self, environ, keep_blank_values, strict_parsing):
        ib = self.innerboundary
        if not valid_boundary(ib):
            raise ValueError, b'Invalid boundary in multipart form: %r' % (ib,)
        self.list = []
        if self.qs_on_post:
            query = urlparse.parse_qsl(self.qs_on_post, self.keep_blank_values, self.strict_parsing, self.max_num_fields)
            self.list.extend(MiniFieldStorage(key, value) for key, value in query)
            FieldStorageClass = None
        max_num_fields = self.max_num_fields
        if max_num_fields is not None:
            max_num_fields -= len(self.list)
        klass = self.FieldStorageClass or self.__class__
        part = klass(self.fp, {}, ib, environ, keep_blank_values, strict_parsing, max_num_fields)
        while not part.done:
            headers = rfc822.Message(self.fp)
            part = klass(self.fp, headers, ib, environ, keep_blank_values, strict_parsing, max_num_fields)
            if max_num_fields is not None:
                max_num_fields -= 1
                if part.list:
                    max_num_fields -= len(part.list)
                if max_num_fields < 0:
                    raise ValueError(b'Max number of fields exceeded')
            self.list.append(part)

        self.skip_lines()
        return

    def read_single(self):
        if self.length >= 0:
            self.read_binary()
            self.skip_lines()
        else:
            self.read_lines()
        self.file.seek(0)
        return

    bufsize = 8192

    def read_binary(self):
        self.file = self.make_file(b'b')
        todo = self.length
        if todo >= 0:
            while todo > 0:
                data = self.fp.read(min(todo, self.bufsize))
                if not data:
                    self.done = -1
                    break
                self.file.write(data)
                todo = todo - len(data)

        return

    def read_lines(self):
        self.file = self.__file = StringIO()
        if self.outerboundary:
            self.read_lines_to_outerboundary()
        else:
            self.read_lines_to_eof()
        return

    def __write(self, line):
        if self.__file is not None:
            if self.__file.tell() + len(line) > 1000:
                self.file = self.make_file(b'')
                self.file.write(self.__file.getvalue())
                self.__file = None
        self.file.write(line)
        return

    def read_lines_to_eof(self):
        while 1:
            line = self.fp.readline(65536)
            if not line:
                self.done = -1
                break
            self.__write(line)

        return

    def read_lines_to_outerboundary(self):
        next = b'--' + self.outerboundary
        last = next + b'--'
        delim = b''
        last_line_lfend = True
        while 1:
            line = self.fp.readline(65536)
            if not line:
                self.done = -1
                break
            if delim == b'\r':
                line = delim + line
                delim = b''
            if line[:2] == b'--' and last_line_lfend:
                strippedline = line.strip()
                if strippedline == next:
                    break
                if strippedline == last:
                    self.done = 1
                    break
            odelim = delim
            if line[-2:] == b'\r\n':
                delim = b'\r\n'
                line = line[:-2]
                last_line_lfend = True
            elif line[-1] == b'\n':
                delim = b'\n'
                line = line[:-1]
                last_line_lfend = True
            elif line[-1] == b'\r':
                delim = b'\r'
                line = line[:-1]
                last_line_lfend = False
            else:
                delim = b''
                last_line_lfend = False
            self.__write(odelim + line)

        return

    def skip_lines(self):
        if not self.outerboundary or self.done:
            return
        next = b'--' + self.outerboundary
        last = next + b'--'
        last_line_lfend = True
        while 1:
            line = self.fp.readline(65536)
            if not line:
                self.done = -1
                break
            if line[:2] == b'--' and last_line_lfend:
                strippedline = line.strip()
                if strippedline == next:
                    break
                if strippedline == last:
                    self.done = 1
                    break
            last_line_lfend = line.endswith(b'\n')

        return

    def make_file(self, binary=None):
        import tempfile
        return tempfile.TemporaryFile(b'w+b')


class FormContentDict(UserDict.UserDict):

    def __init__(self, environ=os.environ, keep_blank_values=0, strict_parsing=0):
        self.dict = self.data = parse(environ=environ, keep_blank_values=keep_blank_values, strict_parsing=strict_parsing)
        self.query_string = environ[b'QUERY_STRING']
        return


class SvFormContentDict(FormContentDict):

    def __getitem__(self, key):
        if len(self.dict[key]) > 1:
            raise IndexError, b'expecting a single value'
        return self.dict[key][0]

    def getlist(self, key):
        return self.dict[key]

    def values(self):
        result = []
        for value in self.dict.values():
            if len(value) == 1:
                result.append(value[0])
            else:
                result.append(value)

        return result

    def items(self):
        result = []
        for key, value in self.dict.items():
            if len(value) == 1:
                result.append((key, value[0]))
            else:
                result.append((key, value))

        return result


class InterpFormContentDict(SvFormContentDict):

    def __getitem__(self, key):
        v = SvFormContentDict.__getitem__(self, key)
        if v[0] in b'0123456789+-.':
            try:
                return int(v)
            except ValueError:
                try:
                    return float(v)
                except ValueError:
                    pass

        return v.strip()

    def values(self):
        result = []
        for key in self.keys():
            try:
                result.append(self[key])
            except IndexError:
                result.append(self.dict[key])

        return result

    def items(self):
        result = []
        for key in self.keys():
            try:
                result.append((key, self[key]))
            except IndexError:
                result.append((key, self.dict[key]))

        return result


class FormContent(FormContentDict):

    def values(self, key):
        if key in self.dict:
            return self.dict[key]
        else:
            return
            return

    def indexed_value(self, key, location):
        if key in self.dict:
            if len(self.dict[key]) > location:
                return self.dict[key][location]
            else:
                return

        else:
            return
        return

    def value(self, key):
        if key in self.dict:
            return self.dict[key][0]
        else:
            return
            return

    def length(self, key):
        return len(self.dict[key])

    def stripped(self, key):
        if key in self.dict:
            return self.dict[key][0].strip()
        else:
            return
            return

    def pars(self):
        return self.dict


def test(environ=os.environ):
    global maxlen
    print b'Content-type: text/html'
    print
    sys.stderr = sys.stdout
    try:
        form = FieldStorage()
        print_directory()
        print_arguments()
        print_form(form)
        print_environ(environ)
        print_environ_usage()

        def f():
            exec b'testing print_exception() -- <I>italics?</I>'
            return

        def g(f=f):
            f()
            return

        print b'<H3>What follows is a test, not an actual exception:</H3>'
        g()
    except:
        print_exception()

    print b'<H1>Second try with a small maxlen...</H1>'
    maxlen = 50
    try:
        form = FieldStorage()
        print_directory()
        print_arguments()
        print_form(form)
        print_environ(environ)
    except:
        print_exception()

    return


def print_exception(type=None, value=None, tb=None, limit=None):
    if type is None:
        type, value, tb = sys.exc_info()
    import traceback
    print
    print b'<H3>Traceback (most recent call last):</H3>'
    list = traceback.format_tb(tb, limit) + traceback.format_exception_only(type, value)
    print b'<PRE>%s<B>%s</B></PRE>' % (
     escape((b'').join(list[:-1])),
     escape(list[-1]))
    del tb
    return


def print_environ(environ=os.environ):
    keys = environ.keys()
    keys.sort()
    print
    print b'<H3>Shell Environment:</H3>'
    print b'<DL>'
    for key in keys:
        print b'<DT>', escape(key), b'<DD>', escape(environ[key])

    print b'</DL>'
    print
    return


def print_form(form):
    keys = form.keys()
    keys.sort()
    print
    print b'<H3>Form Contents:</H3>'
    if not keys:
        print b'<P>No form fields.'
    print b'<DL>'
    for key in keys:
        print b'<DT>' + escape(key) + b':',
        value = form[key]
        print b'<i>' + escape(repr(type(value))) + b'</i>'
        print b'<DD>' + escape(repr(value))

    print b'</DL>'
    print
    return


def print_directory():
    print
    print b'<H3>Current Working Directory:</H3>'
    try:
        pwd = os.getcwd()
    except os.error as msg:
        print b'os.error:', escape(str(msg))
    else:
        print escape(pwd)

    print
    return


def print_arguments():
    print
    print b'<H3>Command Line Arguments:</H3>'
    print
    print sys.argv
    print
    return


def print_environ_usage():
    print b'\n<H3>These environment variables could have been set:</H3>\n<UL>\n<LI>AUTH_TYPE\n<LI>CONTENT_LENGTH\n<LI>CONTENT_TYPE\n<LI>DATE_GMT\n<LI>DATE_LOCAL\n<LI>DOCUMENT_NAME\n<LI>DOCUMENT_ROOT\n<LI>DOCUMENT_URI\n<LI>GATEWAY_INTERFACE\n<LI>LAST_MODIFIED\n<LI>PATH\n<LI>PATH_INFO\n<LI>PATH_TRANSLATED\n<LI>QUERY_STRING\n<LI>REMOTE_ADDR\n<LI>REMOTE_HOST\n<LI>REMOTE_IDENT\n<LI>REMOTE_USER\n<LI>REQUEST_METHOD\n<LI>SCRIPT_NAME\n<LI>SERVER_NAME\n<LI>SERVER_PORT\n<LI>SERVER_PROTOCOL\n<LI>SERVER_ROOT\n<LI>SERVER_SOFTWARE\n</UL>\nIn addition, HTTP headers sent by the server may be passed in the\nenvironment as well.  Here are some common variable names:\n<UL>\n<LI>HTTP_ACCEPT\n<LI>HTTP_CONNECTION\n<LI>HTTP_HOST\n<LI>HTTP_PRAGMA\n<LI>HTTP_REFERER\n<LI>HTTP_USER_AGENT\n</UL>\n'
    return


def escape(s, quote=None):
    s = s.replace(b'&', b'&amp;')
    s = s.replace(b'<', b'&lt;')
    s = s.replace(b'>', b'&gt;')
    if quote:
        s = s.replace(b'"', b'&quot;')
    return s


def valid_boundary(s, _vb_pattern=b'^[ -~]{0,200}[!-~]$'):
    import re
    return re.match(_vb_pattern, s)


if __name__ == b'__main__':
    test()
