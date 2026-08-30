import os, sys
try:
    import SOCKS
    socket = SOCKS
    del SOCKS
    from socket import getfqdn
    socket.getfqdn = getfqdn
    del getfqdn
except ImportError:
    import socket

from socket import _GLOBAL_DEFAULT_TIMEOUT
__all__ = [
 b'FTP', b'Netrc']
MSG_OOB = 1
FTP_PORT = 21
MAXLINE = 8192

class Error(Exception):
    pass


class error_reply(Error):
    pass


class error_temp(Error):
    pass


class error_perm(Error):
    pass


class error_proto(Error):
    pass


all_errors = (
 Error, IOError, EOFError)
CRLF = b'\r\n'

class FTP():
    debugging = 0
    host = b''
    port = FTP_PORT
    maxline = MAXLINE
    sock = None
    file = None
    welcome = None
    passiveserver = 1

    def __init__(self, host=b'', user=b'', passwd=b'', acct=b'', timeout=_GLOBAL_DEFAULT_TIMEOUT):
        self.timeout = timeout
        if host:
            self.connect(host)
            if user:
                self.login(user, passwd, acct)
        return

    def connect(self, host=b'', port=0, timeout=-999):
        if host != b'':
            self.host = host
        if port > 0:
            self.port = port
        if timeout != -999:
            self.timeout = timeout
        self.sock = socket.create_connection((self.host, self.port), self.timeout)
        self.af = self.sock.family
        self.file = self.sock.makefile(b'rb')
        self.welcome = self.getresp()
        return self.welcome

    def getwelcome(self):
        if self.debugging:
            print b'*welcome*', self.sanitize(self.welcome)
        return self.welcome

    def set_debuglevel(self, level):
        self.debugging = level
        return

    debug = set_debuglevel

    def set_pasv(self, val):
        self.passiveserver = val
        return

    def sanitize(self, s):
        if s[:5] == b'pass ' or s[:5] == b'PASS ':
            i = len(s)
            while i > 5 and s[i - 1] in b'\r\n':
                i = i - 1

            s = s[:5] + b'*' * (i - 5) + s[i:]
        return repr(s)

    def putline(self, line):
        if b'\r' in line or b'\n' in line:
            raise ValueError(b'an illegal newline character should not be contained')
        line = line + CRLF
        if self.debugging > 1:
            print b'*put*', self.sanitize(line)
        self.sock.sendall(line)
        return

    def putcmd(self, line):
        if self.debugging:
            print b'*cmd*', self.sanitize(line)
        self.putline(line)
        return

    def getline(self):
        line = self.file.readline(self.maxline + 1)
        if len(line) > self.maxline:
            raise Error(b'got more than %d bytes' % self.maxline)
        if self.debugging > 1:
            print b'*get*', self.sanitize(line)
        if not line:
            raise EOFError
        if line[-2:] == CRLF:
            line = line[:-2]
        elif line[-1:] in CRLF:
            line = line[:-1]
        return line

    def getmultiline(self):
        line = self.getline()
        if line[3:4] == b'-':
            code = line[:3]
            while 1:
                nextline = self.getline()
                line = line + (b'\n' + nextline)
                if nextline[:3] == code and nextline[3:4] != b'-':
                    break

        return line

    def getresp(self):
        resp = self.getmultiline()
        if self.debugging:
            print b'*resp*', self.sanitize(resp)
        self.lastresp = resp[:3]
        c = resp[:1]
        if c in (b'1', b'2', b'3'):
            return resp
        if c == b'4':
            raise error_temp, resp
        if c == b'5':
            raise error_perm, resp
        raise error_proto, resp
        return

    def voidresp(self):
        resp = self.getresp()
        if resp[:1] != b'2':
            raise error_reply, resp
        return resp

    def abort(self):
        line = b'ABOR' + CRLF
        if self.debugging > 1:
            print b'*put urgent*', self.sanitize(line)
        self.sock.sendall(line, MSG_OOB)
        resp = self.getmultiline()
        if resp[:3] not in (b'426', b'225', b'226'):
            raise error_proto, resp
        return

    def sendcmd(self, cmd):
        self.putcmd(cmd)
        return self.getresp()

    def voidcmd(self, cmd):
        self.putcmd(cmd)
        return self.voidresp()

    def sendport(self, host, port):
        hbytes = host.split(b'.')
        pbytes = [repr(port // 256), repr(port % 256)]
        bytes = hbytes + pbytes
        cmd = b'PORT ' + (b',').join(bytes)
        return self.voidcmd(cmd)

    def sendeprt(self, host, port):
        af = 0
        if self.af == socket.AF_INET:
            af = 1
        if self.af == socket.AF_INET6:
            af = 2
        if af == 0:
            raise error_proto, b'unsupported address family'
        fields = [
         b'', repr(af), host, repr(port), b'']
        cmd = b'EPRT ' + (b'|').join(fields)
        return self.voidcmd(cmd)

    def makeport(self):
        err = None
        sock = None
        for res in socket.getaddrinfo(None, 0, self.af, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
            af, socktype, proto, canonname, sa = res
            try:
                sock = socket.socket(af, socktype, proto)
                sock.bind(sa)
            except socket.error as err:
                if sock:
                    sock.close()
                sock = None
                continue

            break

        if sock is None:
            if err is not None:
                raise err
            else:
                raise socket.error(b'getaddrinfo returns an empty list')
        sock.listen(1)
        port = sock.getsockname()[1]
        host = self.sock.getsockname()[0]
        if self.af == socket.AF_INET:
            resp = self.sendport(host, port)
        else:
            resp = self.sendeprt(host, port)
        if self.timeout is not _GLOBAL_DEFAULT_TIMEOUT:
            sock.settimeout(self.timeout)
        return sock

    def makepasv(self):
        if self.af == socket.AF_INET:
            host, port = parse227(self.sendcmd(b'PASV'))
        else:
            host, port = parse229(self.sendcmd(b'EPSV'), self.sock.getpeername())
        return (
         host, port)

    def ntransfercmd(self, cmd, rest=None):
        size = None
        if self.passiveserver:
            host, port = self.makepasv()
            conn = socket.create_connection((host, port), self.timeout)
            try:
                if rest is not None:
                    self.sendcmd(b'REST %s' % rest)
                resp = self.sendcmd(cmd)
                if resp[0] == b'2':
                    resp = self.getresp()
                if resp[0] != b'1':
                    raise error_reply, resp
            except:
                conn.close()
                raise

        else:
            sock = self.makeport()
            try:
                if rest is not None:
                    self.sendcmd(b'REST %s' % rest)
                resp = self.sendcmd(cmd)
                if resp[0] == b'2':
                    resp = self.getresp()
                if resp[0] != b'1':
                    raise error_reply, resp
                conn, sockaddr = sock.accept()
                if self.timeout is not _GLOBAL_DEFAULT_TIMEOUT:
                    conn.settimeout(self.timeout)
            finally:
                sock.close()

        if resp[:3] == b'150':
            size = parse150(resp)
        return (
         conn, size)

    def transfercmd(self, cmd, rest=None):
        return self.ntransfercmd(cmd, rest)[0]

    def login(self, user=b'', passwd=b'', acct=b''):
        if not user:
            user = b'anonymous'
        if not passwd:
            passwd = b''
        if not acct:
            acct = b''
        if user == b'anonymous' and passwd in (b'', b'-'):
            passwd = passwd + b'anonymous@'
        resp = self.sendcmd(b'USER ' + user)
        if resp[0] == b'3':
            resp = self.sendcmd(b'PASS ' + passwd)
        if resp[0] == b'3':
            resp = self.sendcmd(b'ACCT ' + acct)
        if resp[0] != b'2':
            raise error_reply, resp
        return resp

    def retrbinary(self, cmd, callback, blocksize=8192, rest=None):
        self.voidcmd(b'TYPE I')
        conn = self.transfercmd(cmd, rest)
        try:
            while 1:
                data = conn.recv(blocksize)
                if not data:
                    break
                callback(data)

        finally:
            conn.close()

        return self.voidresp()

    def retrlines(self, cmd, callback=None):
        if callback is None:
            callback = print_line
        resp = self.sendcmd(b'TYPE A')
        conn = self.transfercmd(cmd)
        fp = None
        try:
            fp = conn.makefile(b'rb')
            while 1:
                line = fp.readline(self.maxline + 1)
                if len(line) > self.maxline:
                    raise Error(b'got more than %d bytes' % self.maxline)
                if self.debugging > 2:
                    print b'*retr*', repr(line)
                if not line:
                    break
                if line[-2:] == CRLF:
                    line = line[:-2]
                elif line[-1:] == b'\n':
                    line = line[:-1]
                callback(line)

        finally:
            if fp:
                fp.close()
            conn.close()

        return self.voidresp()

    def storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None):
        self.voidcmd(b'TYPE I')
        conn = self.transfercmd(cmd, rest)
        try:
            while 1:
                buf = fp.read(blocksize)
                if not buf:
                    break
                conn.sendall(buf)
                if callback:
                    callback(buf)

        finally:
            conn.close()

        return self.voidresp()

    def storlines(self, cmd, fp, callback=None):
        self.voidcmd(b'TYPE A')
        conn = self.transfercmd(cmd)
        try:
            while 1:
                buf = fp.readline(self.maxline + 1)
                if len(buf) > self.maxline:
                    raise Error(b'got more than %d bytes' % self.maxline)
                if not buf:
                    break
                if buf[-2:] != CRLF:
                    if buf[-1] in CRLF:
                        buf = buf[:-1]
                    buf = buf + CRLF
                conn.sendall(buf)
                if callback:
                    callback(buf)

        finally:
            conn.close()

        return self.voidresp()

    def acct(self, password):
        cmd = b'ACCT ' + password
        return self.voidcmd(cmd)

    def nlst(self, *args):
        cmd = b'NLST'
        for arg in args:
            cmd = cmd + (b' ' + arg)

        files = []
        self.retrlines(cmd, files.append)
        return files

    def dir(self, *args):
        cmd = b'LIST'
        func = None
        if args[-1:] and type(args[-1]) != type(b''):
            args, func = args[:-1], args[-1]
        for arg in args:
            if arg:
                cmd = cmd + (b' ' + arg)

        self.retrlines(cmd, func)
        return

    def rename(self, fromname, toname):
        resp = self.sendcmd(b'RNFR ' + fromname)
        if resp[0] != b'3':
            raise error_reply, resp
        return self.voidcmd(b'RNTO ' + toname)

    def delete(self, filename):
        resp = self.sendcmd(b'DELE ' + filename)
        if resp[:3] in (b'250', b'200'):
            return resp
        raise error_reply, resp
        return

    def cwd(self, dirname):
        if dirname == b'..':
            try:
                return self.voidcmd(b'CDUP')
            except error_perm as msg:
                if msg.args[0][:3] != b'500':
                    raise

        elif dirname == b'':
            dirname = b'.'
        cmd = b'CWD ' + dirname
        return self.voidcmd(cmd)

    def size(self, filename):
        resp = self.sendcmd(b'SIZE ' + filename)
        if resp[:3] == b'213':
            s = resp[3:].strip()
            try:
                return int(s)
            except (OverflowError, ValueError):
                return long(s)

        return

    def mkd(self, dirname):
        resp = self.sendcmd(b'MKD ' + dirname)
        return parse257(resp)

    def rmd(self, dirname):
        return self.voidcmd(b'RMD ' + dirname)

    def pwd(self):
        resp = self.sendcmd(b'PWD')
        return parse257(resp)

    def quit(self):
        resp = self.voidcmd(b'QUIT')
        self.close()
        return resp

    def close(self):
        try:
            file = self.file
            self.file = None
            if file is not None:
                file.close()
        finally:
            sock = self.sock
            self.sock = None
            if sock is not None:
                sock.close()

        return


try:
    import ssl
except ImportError:
    pass
else:

    class FTP_TLS(FTP):
        ssl_version = ssl.PROTOCOL_SSLv23

        def __init__(self, host=b'', user=b'', passwd=b'', acct=b'', keyfile=None, certfile=None, context=None, timeout=_GLOBAL_DEFAULT_TIMEOUT, source_address=None):
            if context is not None and keyfile is not None:
                raise ValueError(b'context and keyfile arguments are mutually exclusive')
            if context is not None and certfile is not None:
                raise ValueError(b'context and certfile arguments are mutually exclusive')
            self.keyfile = keyfile
            self.certfile = certfile
            if context is None:
                context = ssl._create_stdlib_context(self.ssl_version, certfile=certfile, keyfile=keyfile)
            self.context = context
            self._prot_p = False
            FTP.__init__(self, host, user, passwd, acct, timeout)
            return

        def login(self, user=b'', passwd=b'', acct=b'', secure=True):
            if secure and not isinstance(self.sock, ssl.SSLSocket):
                self.auth()
            return FTP.login(self, user, passwd, acct)

        def auth(self):
            if isinstance(self.sock, ssl.SSLSocket):
                raise ValueError(b'Already using TLS')
            if self.ssl_version >= ssl.PROTOCOL_SSLv23:
                resp = self.voidcmd(b'AUTH TLS')
            else:
                resp = self.voidcmd(b'AUTH SSL')
            self.sock = self.context.wrap_socket(self.sock, server_hostname=self.host)
            self.file = self.sock.makefile(mode=b'rb')
            return resp

        def prot_p(self):
            self.voidcmd(b'PBSZ 0')
            resp = self.voidcmd(b'PROT P')
            self._prot_p = True
            return resp

        def prot_c(self):
            resp = self.voidcmd(b'PROT C')
            self._prot_p = False
            return resp

        def ntransfercmd(self, cmd, rest=None):
            conn, size = FTP.ntransfercmd(self, cmd, rest)
            if self._prot_p:
                conn = self.context.wrap_socket(conn, server_hostname=self.host)
            return (
             conn, size)

        def retrbinary(self, cmd, callback, blocksize=8192, rest=None):
            self.voidcmd(b'TYPE I')
            conn = self.transfercmd(cmd, rest)
            try:
                while 1:
                    data = conn.recv(blocksize)
                    if not data:
                        break
                    callback(data)

                if isinstance(conn, ssl.SSLSocket):
                    conn.unwrap()
            finally:
                conn.close()

            return self.voidresp()

        def retrlines(self, cmd, callback=None):
            if callback is None:
                callback = print_line
            resp = self.sendcmd(b'TYPE A')
            conn = self.transfercmd(cmd)
            fp = conn.makefile(b'rb')
            try:
                while 1:
                    line = fp.readline(self.maxline + 1)
                    if len(line) > self.maxline:
                        raise Error(b'got more than %d bytes' % self.maxline)
                    if self.debugging > 2:
                        print b'*retr*', repr(line)
                    if not line:
                        break
                    if line[-2:] == CRLF:
                        line = line[:-2]
                    elif line[-1:] == b'\n':
                        line = line[:-1]
                    callback(line)

                if isinstance(conn, ssl.SSLSocket):
                    conn.unwrap()
            finally:
                fp.close()
                conn.close()

            return self.voidresp()

        def storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None):
            self.voidcmd(b'TYPE I')
            conn = self.transfercmd(cmd, rest)
            try:
                while 1:
                    buf = fp.read(blocksize)
                    if not buf:
                        break
                    conn.sendall(buf)
                    if callback:
                        callback(buf)

                if isinstance(conn, ssl.SSLSocket):
                    conn.unwrap()
            finally:
                conn.close()

            return self.voidresp()

        def storlines(self, cmd, fp, callback=None):
            self.voidcmd(b'TYPE A')
            conn = self.transfercmd(cmd)
            try:
                while 1:
                    buf = fp.readline(self.maxline + 1)
                    if len(buf) > self.maxline:
                        raise Error(b'got more than %d bytes' % self.maxline)
                    if not buf:
                        break
                    if buf[-2:] != CRLF:
                        if buf[-1] in CRLF:
                            buf = buf[:-1]
                        buf = buf + CRLF
                    conn.sendall(buf)
                    if callback:
                        callback(buf)

                if isinstance(conn, ssl.SSLSocket):
                    conn.unwrap()
            finally:
                conn.close()

            return self.voidresp()


    __all__.append(b'FTP_TLS')
    all_errors = (Error, IOError, EOFError, ssl.SSLError)

_150_re = None

def parse150(resp):
    global _150_re
    if resp[:3] != b'150':
        raise error_reply, resp
    if _150_re is None:
        import re
        _150_re = re.compile(b'150 .* \\((\\d+) bytes\\)', re.IGNORECASE)
    m = _150_re.match(resp)
    if not m:
        return
    else:
        s = m.group(1)
        try:
            return int(s)
        except (OverflowError, ValueError):
            return long(s)

        return


_227_re = None

def parse227(resp):
    global _227_re
    if resp[:3] != b'227':
        raise error_reply, resp
    if _227_re is None:
        import re
        _227_re = re.compile(b'(\\d+),(\\d+),(\\d+),(\\d+),(\\d+),(\\d+)')
    m = _227_re.search(resp)
    if not m:
        raise error_proto, resp
    numbers = m.groups()
    host = (b'.').join(numbers[:4])
    port = (int(numbers[4]) << 8) + int(numbers[5])
    return (host, port)


def parse229(resp, peer):
    if resp[:3] != b'229':
        raise error_reply, resp
    left = resp.find(b'(')
    if left < 0:
        raise error_proto, resp
    right = resp.find(b')', left + 1)
    if right < 0:
        raise error_proto, resp
    if resp[left + 1] != resp[right - 1]:
        raise error_proto, resp
    parts = resp[left + 1:right].split(resp[left + 1])
    if len(parts) != 5:
        raise error_proto, resp
    host = peer[0]
    port = int(parts[3])
    return (host, port)


def parse257(resp):
    if resp[:3] != b'257':
        raise error_reply, resp
    if resp[3:5] != b' "':
        return b''
    dirname = b''
    i = 5
    n = len(resp)
    while i < n:
        c = resp[i]
        i = i + 1
        if c == b'"':
            if i >= n or resp[i] != b'"':
                break
            i = i + 1
        dirname = dirname + c

    return dirname


def print_line(line):
    print line
    return


def ftpcp(source, sourcename, target, targetname=b'', type=b'I'):
    if not targetname:
        targetname = sourcename
    type = b'TYPE ' + type
    source.voidcmd(type)
    target.voidcmd(type)
    sourcehost, sourceport = parse227(source.sendcmd(b'PASV'))
    target.sendport(sourcehost, sourceport)
    treply = target.sendcmd(b'STOR ' + targetname)
    if treply[:3] not in (b'125', b'150'):
        raise error_proto
    sreply = source.sendcmd(b'RETR ' + sourcename)
    if sreply[:3] not in (b'125', b'150'):
        raise error_proto
    source.voidresp()
    target.voidresp()
    return


class Netrc():
    __defuser = None
    __defpasswd = None
    __defacct = None

    def __init__(self, filename=None):
        if filename is None:
            if b'HOME' in os.environ:
                filename = os.path.join(os.environ[b'HOME'], b'.netrc')
            else:
                raise IOError, b'specify file to load or set $HOME'
        self.__hosts = {}
        self.__macros = {}
        fp = open(filename, b'r')
        in_macro = 0
        while 1:
            line = fp.readline(self.maxline + 1)
            if len(line) > self.maxline:
                raise Error(b'got more than %d bytes' % self.maxline)
            if not line:
                break
            if in_macro and line.strip():
                macro_lines.append(line)
                continue
            elif in_macro:
                self.__macros[macro_name] = tuple(macro_lines)
                in_macro = 0
            words = line.split()
            host = user = passwd = acct = None
            default = 0
            i = 0
            while i < len(words):
                w1 = words[i]
                if i + 1 < len(words):
                    w2 = words[i + 1]
                else:
                    w2 = None
                if w1 == b'default':
                    default = 1
                elif w1 == b'machine' and w2:
                    host = w2.lower()
                    i = i + 1
                elif w1 == b'login' and w2:
                    user = w2
                    i = i + 1
                elif w1 == b'password' and w2:
                    passwd = w2
                    i = i + 1
                elif w1 == b'account' and w2:
                    acct = w2
                    i = i + 1
                elif w1 == b'macdef' and w2:
                    macro_name = w2
                    macro_lines = []
                    in_macro = 1
                    break
                i = i + 1

            if default:
                self.__defuser = user or self.__defuser
                self.__defpasswd = passwd or self.__defpasswd
                self.__defacct = acct or self.__defacct
            if host:
                if host in self.__hosts:
                    ouser, opasswd, oacct = self.__hosts[host]
                    user = user or ouser
                    passwd = passwd or opasswd
                    acct = acct or oacct
                self.__hosts[host] = (
                 user, passwd, acct)

        fp.close()
        return

    def get_hosts(self):
        return self.__hosts.keys()

    def get_account(self, host):
        host = host.lower()
        user = passwd = acct = None
        if host in self.__hosts:
            user, passwd, acct = self.__hosts[host]
        user = user or self.__defuser
        passwd = passwd or self.__defpasswd
        acct = acct or self.__defacct
        return (user, passwd, acct)

    def get_macros(self):
        return self.__macros.keys()

    def get_macro(self, macro):
        return self.__macros[macro]


def test():
    if len(sys.argv) < 2:
        print test.__doc__
        sys.exit(0)
    debugging = 0
    rcfile = None
    while sys.argv[1] == b'-d':
        debugging = debugging + 1
        del sys.argv[1]

    if sys.argv[1][:2] == b'-r':
        rcfile = sys.argv[1][2:]
        del sys.argv[1]
    host = sys.argv[1]
    ftp = FTP(host)
    ftp.set_debuglevel(debugging)
    userid = passwd = acct = b''
    try:
        netrc = Netrc(rcfile)
    except IOError:
        if rcfile is not None:
            sys.stderr.write(b'Could not open account file -- using anonymous login.')
    else:
        try:
            userid, passwd, acct = netrc.get_account(host)
        except KeyError:
            sys.stderr.write(b'No account -- using anonymous login.')

    ftp.login(userid, passwd, acct)
    for file in sys.argv[2:]:
        if file[:2] == b'-l':
            ftp.dir(file[2:])
        elif file[:2] == b'-d':
            cmd = b'CWD'
            if file[2:]:
                cmd = cmd + b' ' + file[2:]
            resp = ftp.sendcmd(cmd)
        elif file == b'-p':
            ftp.set_pasv(not ftp.passiveserver)
        else:
            ftp.retrbinary(b'RETR ' + file, sys.stdout.write, 1024)

    ftp.quit()
    return


if __name__ == b'__main__':
    test()
