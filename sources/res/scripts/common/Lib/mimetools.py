import os, sys, tempfile
from warnings import filterwarnings, catch_warnings
with catch_warnings():
    if sys.py3kwarning:
        filterwarnings(b'ignore', b'.*rfc822 has been removed', DeprecationWarning)
    import rfc822
from warnings import warnpy3k
warnpy3k(b'in 3.x, mimetools has been removed in favor of the email package', stacklevel=2)
__all__ = [
 9, 10, 11, 12, 13, 
 14]

class Message(rfc822.Message):

    def __init__(self, fp, seekable=1):
        rfc822.Message.__init__(self, fp, seekable)
        self.encodingheader = self.getheader(b'content-transfer-encoding')
        self.typeheader = self.getheader(b'content-type')
        self.parsetype()
        self.parseplist()
        return

    def parsetype(self):
        str = self.typeheader
        if str is None:
            str = b'text/plain'
        if b';' in str:
            i = str.index(b';')
            self.plisttext = str[i:]
            str = str[:i]
        else:
            self.plisttext = b''
        fields = str.split(b'/')
        for i in range(len(fields)):
            fields[i] = fields[i].strip().lower()

        self.type = (b'/').join(fields)
        self.maintype = fields[0]
        self.subtype = (b'/').join(fields[1:])
        return

    def parseplist(self):
        str = self.plisttext
        self.plist = []
        while str[:1] == b';':
            str = str[1:]
            if b';' in str:
                end = str.index(b';')
            else:
                end = len(str)
            f = str[:end]
            if b'=' in f:
                i = f.index(b'=')
                f = f[:i].strip().lower() + b'=' + f[i + 1:].strip()
            self.plist.append(f.strip())
            str = str[end:]

        return

    def getplist(self):
        return self.plist

    def getparam(self, name):
        name = name.lower() + b'='
        n = len(name)
        for p in self.plist:
            if p[:n] == name:
                return rfc822.unquote(p[n:])

        return

    def getparamnames(self):
        result = []
        for p in self.plist:
            i = p.find(b'=')
            if i >= 0:
                result.append(p[:i].lower())

        return result

    def getencoding(self):
        if self.encodingheader is None:
            return b'7bit'
        else:
            return self.encodingheader.lower()

    def gettype(self):
        return self.type

    def getmaintype(self):
        return self.maintype

    def getsubtype(self):
        return self.subtype


try:
    import thread
except ImportError:
    import dummy_thread as thread

_counter_lock = thread.allocate_lock()
del thread
_counter = 0

def _get_next_counter():
    global _counter
    _counter_lock.acquire()
    _counter += 1
    result = _counter
    _counter_lock.release()
    return result


_prefix = None

def choose_boundary():
    global _prefix
    import time
    if _prefix is None:
        import socket
        try:
            hostid = socket.gethostbyname(socket.gethostname())
        except socket.gaierror:
            hostid = b'127.0.0.1'

        try:
            uid = repr(os.getuid())
        except AttributeError:
            uid = b'1'

        try:
            pid = repr(os.getpid())
        except AttributeError:
            pid = b'1'

        _prefix = hostid + b'.' + uid + b'.' + pid
    return b'%s.%.3f.%d' % (_prefix, time.time(), _get_next_counter())


def decode(input, output, encoding):
    if encoding == b'base64':
        import base64
        return base64.decode(input, output)
    if encoding == b'quoted-printable':
        import quopri
        return quopri.decode(input, output)
    if encoding in (b'uuencode', b'x-uuencode', b'uue', b'x-uue'):
        import uu
        return uu.decode(input, output)
    if encoding in (b'7bit', b'8bit'):
        return output.write(input.read())
    if encoding in decodetab:
        pipethrough(input, decodetab[encoding], output)
    else:
        raise ValueError, b'unknown Content-Transfer-Encoding: %s' % encoding
    return


def encode(input, output, encoding):
    if encoding == b'base64':
        import base64
        return base64.encode(input, output)
    if encoding == b'quoted-printable':
        import quopri
        return quopri.encode(input, output, 0)
    if encoding in (b'uuencode', b'x-uuencode', b'uue', b'x-uue'):
        import uu
        return uu.encode(input, output)
    if encoding in (b'7bit', b'8bit'):
        return output.write(input.read())
    if encoding in encodetab:
        pipethrough(input, encodetab[encoding], output)
    else:
        raise ValueError, b'unknown Content-Transfer-Encoding: %s' % encoding
    return


uudecode_pipe = b'(\nTEMP=/tmp/@uu.$$\nsed "s%^begin [0-7][0-7]* .*%begin 600 $TEMP%" | uudecode\ncat $TEMP\nrm $TEMP\n)'
decodetab = {b'uuencode': uudecode_pipe, 
   b'x-uuencode': uudecode_pipe, 
   b'uue': uudecode_pipe, 
   b'x-uue': uudecode_pipe, 
   b'quoted-printable': b'mmencode -u -q', 
   b'base64': b'mmencode -u -b'}
encodetab = {b'x-uuencode': b'uuencode tempfile', 
   b'uuencode': b'uuencode tempfile', 
   b'x-uue': b'uuencode tempfile', 
   b'uue': b'uuencode tempfile', 
   b'quoted-printable': b'mmencode -q', 
   b'base64': b'mmencode -b'}

def pipeto(input, command):
    pipe = os.popen(command, b'w')
    copyliteral(input, pipe)
    pipe.close()
    return


def pipethrough(input, command, output):
    fd, tempname = tempfile.mkstemp()
    temp = os.fdopen(fd, b'w')
    copyliteral(input, temp)
    temp.close()
    pipe = os.popen(command + b' <' + tempname, b'r')
    copybinary(pipe, output)
    pipe.close()
    os.unlink(tempname)
    return


def copyliteral(input, output):
    while 1:
        line = input.readline()
        if not line:
            break
        output.write(line)

    return


def copybinary(input, output):
    BUFSIZE = 8192
    while 1:
        line = input.read(BUFSIZE)
        if not line:
            break
        output.write(line)

    return
