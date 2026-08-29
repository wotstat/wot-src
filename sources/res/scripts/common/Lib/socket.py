import _socket
from _socket import *
from functools import partial
from types import MethodType
try:
    import _ssl
except ImportError:
    pass
else:

    def ssl(sock, keyfile=None, certfile=None):
        import ssl as _realssl
        warnings.warn(b'socket.ssl() is deprecated.  Use ssl.wrap_socket() instead.', DeprecationWarning, stacklevel=2)
        return _realssl.sslwrap_simple(sock, keyfile, certfile)


    from _ssl import SSLError as sslerror
    from _ssl import RAND_add, RAND_status, SSL_ERROR_ZERO_RETURN, SSL_ERROR_WANT_READ, SSL_ERROR_WANT_WRITE, SSL_ERROR_WANT_X509_LOOKUP, SSL_ERROR_SYSCALL, SSL_ERROR_SSL, SSL_ERROR_WANT_CONNECT, SSL_ERROR_EOF, SSL_ERROR_INVALID_ERROR_CODE
    try:
        from _ssl import RAND_egd
    except ImportError:
        pass

    import os, sys, warnings
    try:
        from cStringIO import StringIO
    except ImportError:
        from StringIO import StringIO

    try:
        import errno
    except ImportError:
        errno = None

EBADF = getattr(errno, b'EBADF', 9)
EINTR = getattr(errno, b'EINTR', 4)
__all__ = [
 b'getfqdn', b'create_connection']
__all__.extend(os._get_exports_list(_socket))
_realsocket = socket
if sys.platform.lower().startswith(b'win'):
    errorTab = {}
    errorTab[10004] = b'The operation was interrupted.'
    errorTab[10009] = b'A bad file handle was passed.'
    errorTab[10013] = b'Permission denied.'
    errorTab[10014] = b'A fault occurred on the network??'
    errorTab[10022] = b'An invalid operation was attempted.'
    errorTab[10035] = b'The socket operation would block'
    errorTab[10036] = b'A blocking operation is already in progress.'
    errorTab[10048] = b'The network address is in use.'
    errorTab[10054] = b'The connection has been reset.'
    errorTab[10058] = b'The network has been shut down.'
    errorTab[10060] = b'The operation timed out.'
    errorTab[10061] = b'Connection refused.'
    errorTab[10063] = b'The name is too long.'
    errorTab[10064] = b'The host is down.'
    errorTab[10065] = b'The host is unreachable.'
    __all__.append(b'errorTab')

def getfqdn(name=b''):
    name = name.strip()
    if not name or name == b'0.0.0.0':
        name = gethostname()
    try:
        hostname, aliases, ipaddrs = gethostbyaddr(name)
    except error:
        pass

    aliases.insert(0, hostname)
    for name in aliases:
        if b'.' in name:
            break
    else:
        name = hostname

    return name


_socketmethods = (
 b'bind', b'connect', b'connect_ex', b'fileno', b'listen',
 b'getpeername', b'getsockname', b'getsockopt', b'setsockopt',
 b'sendall', b'setblocking',
 b'settimeout', b'gettimeout', b'shutdown')
if os.name == b'nt':
    _socketmethods = _socketmethods + (b'ioctl',)
if sys.platform == b'riscos':
    _socketmethods = _socketmethods + (b'sleeptaskw',)
_delegate_methods = (
 b'recv', b'recvfrom', b'recv_into', b'recvfrom_into',
 b'send', b'sendto')

class _closedsocket(object):
    __slots__ = []

    def _dummy(*args):
        raise error(EBADF, b'Bad file descriptor')
        return

    send = recv = recv_into = sendto = recvfrom = recvfrom_into = _dummy
    __getattr__ = _dummy


class _socketobject(object):
    __doc__ = _realsocket.__doc__
    __slots__ = [
     b'_sock', b'__weakref__'] + list(_delegate_methods)

    def __init__(self, family=AF_INET, type=SOCK_STREAM, proto=0, _sock=None):
        if _sock is None:
            _sock = _realsocket(family, type, proto)
        self._sock = _sock
        for method in _delegate_methods:
            setattr(self, method, getattr(_sock, method))

        return

    def close(self, _closedsocket=_closedsocket, _delegate_methods=_delegate_methods, setattr=setattr):
        self._sock = _closedsocket()
        dummy = self._sock._dummy
        for method in _delegate_methods:
            setattr(self, method, dummy)

        return

    close.__doc__ = _realsocket.close.__doc__

    def accept(self):
        sock, addr = self._sock.accept()
        return (_socketobject(_sock=sock), addr)

    accept.__doc__ = _realsocket.accept.__doc__

    def dup(self):
        return _socketobject(_sock=self._sock)

    def makefile(self, mode=b'r', bufsize=-1):
        return _fileobject(self._sock, mode, bufsize)

    family = property((lambda self: self._sock.family), doc=b'the socket family')
    type = property((lambda self: self._sock.type), doc=b'the socket type')
    proto = property((lambda self: self._sock.proto), doc=b'the socket protocol')


def meth(name, self, *args):
    return getattr(self._sock, name)(*args)


for _m in _socketmethods:
    p = partial(meth, _m)
    p.__name__ = _m
    p.__doc__ = getattr(_realsocket, _m).__doc__
    m = MethodType(p, None, _socketobject)
    setattr(_socketobject, _m, m)

socket = SocketType = _socketobject

class _fileobject(object):
    default_bufsize = 8192
    name = b'<socket>'
    __slots__ = [
     2, 3, 4, 
     5, 6, 7, 8, 9, 10, 
     11]

    def __init__(self, sock, mode=b'rb', bufsize=-1, close=False):
        self._sock = sock
        self.mode = mode
        if bufsize < 0:
            bufsize = self.default_bufsize
        self.bufsize = bufsize
        self.softspace = False
        if bufsize == 0:
            self._rbufsize = 1
        elif bufsize == 1:
            self._rbufsize = self.default_bufsize
        else:
            self._rbufsize = bufsize
        self._wbufsize = bufsize
        self._rbuf = StringIO()
        self._wbuf = []
        self._wbuf_len = 0
        self._close = close
        return

    def _getclosed(self):
        return self._sock is None

    closed = property(_getclosed, doc=b'True if the file is closed')

    def close(self):
        try:
            if self._sock:
                self.flush()
        finally:
            if self._close:
                self._sock.close()
            self._sock = None

        return

    def __del__(self):
        try:
            self.close()
        except:
            pass

        return

    def flush(self):
        if self._wbuf:
            data = (b'').join(self._wbuf)
            self._wbuf = []
            self._wbuf_len = 0
            buffer_size = max(self._rbufsize, self.default_bufsize)
            data_size = len(data)
            write_offset = 0
            view = memoryview(data)
            try:
                while write_offset < data_size:
                    self._sock.sendall(view[write_offset:write_offset + buffer_size])
                    write_offset += buffer_size

            finally:
                if write_offset < data_size:
                    remainder = data[write_offset:]
                    del view
                    del data
                    self._wbuf.append(remainder)
                    self._wbuf_len = len(remainder)

        return

    def fileno(self):
        return self._sock.fileno()

    def write(self, data):
        data = str(data)
        if not data:
            return
        self._wbuf.append(data)
        self._wbuf_len += len(data)
        if self._wbufsize == 0 or self._wbufsize == 1 and b'\n' in data or self._wbufsize > 1 and self._wbuf_len >= self._wbufsize:
            self.flush()
        return

    def writelines(self, list):
        lines = filter(None, map(str, list))
        self._wbuf_len += sum(map(len, lines))
        self._wbuf.extend(lines)
        if self._wbufsize <= 1 or self._wbuf_len >= self._wbufsize:
            self.flush()
        return

    def read(self, size=-1):
        rbufsize = max(self._rbufsize, self.default_bufsize)
        buf = self._rbuf
        buf.seek(0, 2)
        if size < 0:
            self._rbuf = StringIO()
            while True:
                try:
                    data = self._sock.recv(rbufsize)
                except error as e:
                    if e.args[0] == EINTR:
                        continue
                    raise

                if not data:
                    break
                buf.write(data)

            return buf.getvalue()
        else:
            buf_len = buf.tell()
            if buf_len >= size:
                buf.seek(0)
                rv = buf.read(size)
                self._rbuf = StringIO()
                self._rbuf.write(buf.read())
                return rv
            self._rbuf = StringIO()
            while True:
                left = size - buf_len
                try:
                    data = self._sock.recv(left)
                except error as e:
                    if e.args[0] == EINTR:
                        continue
                    raise

                if not data:
                    break
                n = len(data)
                if n == size and not buf_len:
                    return data
                if n == left:
                    buf.write(data)
                    del data
                    break
                buf.write(data)
                buf_len += n
                del data

            return buf.getvalue()

        return

    def readline(self, size=-1):
        buf = self._rbuf
        buf.seek(0, 2)
        if buf.tell() > 0:
            buf.seek(0)
            bline = buf.readline(size)
            if bline.endswith(b'\n') or len(bline) == size:
                self._rbuf = StringIO()
                self._rbuf.write(buf.read())
                return bline
            del bline
        if size < 0:
            if self._rbufsize <= 1:
                buf.seek(0)
                buffers = [buf.read()]
                self._rbuf = StringIO()
                data = None
                recv = self._sock.recv
                while True:
                    try:
                        while data != b'\n':
                            data = recv(1)
                            if not data:
                                break
                            buffers.append(data)

                    except error as e:
                        if e.args[0] == EINTR:
                            continue
                        raise

                    break

                return (b'').join(buffers)
            buf.seek(0, 2)
            self._rbuf = StringIO()
            while True:
                try:
                    data = self._sock.recv(self._rbufsize)
                except error as e:
                    if e.args[0] == EINTR:
                        continue
                    raise

                if not data:
                    break
                nl = data.find(b'\n')
                if nl >= 0:
                    nl += 1
                    buf.write(data[:nl])
                    self._rbuf.write(data[nl:])
                    del data
                    break
                buf.write(data)

            return buf.getvalue()
        else:
            buf.seek(0, 2)
            buf_len = buf.tell()
            if buf_len >= size:
                buf.seek(0)
                rv = buf.read(size)
                self._rbuf = StringIO()
                self._rbuf.write(buf.read())
                return rv
            self._rbuf = StringIO()
            while True:
                try:
                    data = self._sock.recv(self._rbufsize)
                except error as e:
                    if e.args[0] == EINTR:
                        continue
                    raise

                if not data:
                    break
                left = size - buf_len
                nl = data.find(b'\n', 0, left)
                if nl >= 0:
                    nl += 1
                    self._rbuf.write(data[nl:])
                    if buf_len:
                        buf.write(data[:nl])
                        break
                    else:
                        return data[:nl]
                n = len(data)
                if n == size and not buf_len:
                    return data
                if n >= left:
                    buf.write(data[:left])
                    self._rbuf.write(data[left:])
                    break
                buf.write(data)
                buf_len += n

            return buf.getvalue()
            return

    def readlines(self, sizehint=0):
        total = 0
        list = []
        while True:
            line = self.readline()
            if not line:
                break
            list.append(line)
            total += len(line)
            if sizehint and total >= sizehint:
                break

        return list

    def __iter__(self):
        return self

    def next(self):
        line = self.readline()
        if not line:
            raise StopIteration
        return line


_GLOBAL_DEFAULT_TIMEOUT = object()

def create_connection(address, timeout=_GLOBAL_DEFAULT_TIMEOUT, source_address=None):
    host, port = address
    err = None
    for res in getaddrinfo(host, port, 0, SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        sock = None
        try:
            sock = socket(af, socktype, proto)
            if timeout is not _GLOBAL_DEFAULT_TIMEOUT:
                sock.settimeout(timeout)
            if source_address:
                sock.bind(source_address)
            sock.connect(sa)
            return sock
        except error as _:
            err = _
            if sock is not None:
                sock.close()

    if err is not None:
        raise err
    else:
        raise error(b'getaddrinfo returns an empty list')
    return
