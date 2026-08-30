import re, socket
__all__ = [
 b'POP3', b'error_proto']

class error_proto(Exception):
    pass


POP3_PORT = 110
POP3_SSL_PORT = 995
CR = b'\r'
LF = b'\n'
CRLF = CR + LF
_MAXLINE = 2048

class POP3():

    def __init__(self, host, port=POP3_PORT, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.sock = socket.create_connection((host, port), timeout)
        self.file = self.sock.makefile(b'rb')
        self._debugging = 0
        self.welcome = self._getresp()
        return

    def _putline(self, line):
        if self._debugging > 1:
            print b'*put*', repr(line)
        self.sock.sendall(b'%s%s' % (line, CRLF))
        return

    def _putcmd(self, line):
        if self._debugging:
            print b'*cmd*', repr(line)
        self._putline(line)
        return

    def _getline(self):
        line = self.file.readline(_MAXLINE + 1)
        if len(line) > _MAXLINE:
            raise error_proto(b'line too long')
        if self._debugging > 1:
            print b'*get*', repr(line)
        if not line:
            raise error_proto(b'-ERR EOF')
        octets = len(line)
        if line[-2:] == CRLF:
            return (line[:-2], octets)
        if line[0] == CR:
            return (line[1:-1], octets)
        return (
         line[:-1], octets)

    def _getresp(self):
        resp, o = self._getline()
        if self._debugging > 1:
            print b'*resp*', repr(resp)
        c = resp[:1]
        if c != b'+':
            raise error_proto(resp)
        return resp

    def _getlongresp(self):
        resp = self._getresp()
        list = []
        octets = 0
        line, o = self._getline()
        while line != b'.':
            if line[:2] == b'..':
                o = o - 1
                line = line[1:]
            octets = octets + o
            list.append(line)
            line, o = self._getline()

        return (
         resp, list, octets)

    def _shortcmd(self, line):
        self._putcmd(line)
        return self._getresp()

    def _longcmd(self, line):
        self._putcmd(line)
        return self._getlongresp()

    def getwelcome(self):
        return self.welcome

    def set_debuglevel(self, level):
        self._debugging = level
        return

    def user(self, user):
        return self._shortcmd(b'USER %s' % user)

    def pass_(self, pswd):
        return self._shortcmd(b'PASS %s' % pswd)

    def stat(self):
        retval = self._shortcmd(b'STAT')
        rets = retval.split()
        if self._debugging:
            print b'*stat*', repr(rets)
        numMessages = int(rets[1])
        sizeMessages = int(rets[2])
        return (numMessages, sizeMessages)

    def list(self, which=None):
        if which is not None:
            return self._shortcmd(b'LIST %s' % which)
        else:
            return self._longcmd(b'LIST')

    def retr(self, which):
        return self._longcmd(b'RETR %s' % which)

    def dele(self, which):
        return self._shortcmd(b'DELE %s' % which)

    def noop(self):
        return self._shortcmd(b'NOOP')

    def rset(self):
        return self._shortcmd(b'RSET')

    def quit(self):
        try:
            resp = self._shortcmd(b'QUIT')
        except error_proto as val:
            resp = val

        self.file.close()
        self.sock.close()
        del self.file
        del self.sock
        return resp

    def rpop(self, user):
        return self._shortcmd(b'RPOP %s' % user)

    timestamp = re.compile(b'\\+OK.[^<]*(<.*>)')

    def apop(self, user, secret):
        m = self.timestamp.match(self.welcome)
        if not m:
            raise error_proto(b'-ERR APOP not supported by server')
        import hashlib
        digest = hashlib.md5(m.group(1) + secret).digest()
        digest = (b'').join(map((lambda x: b'%02x' % ord(x)), digest))
        return self._shortcmd(b'APOP %s %s' % (user, digest))

    def top(self, which, howmuch):
        return self._longcmd(b'TOP %s %s' % (which, howmuch))

    def uidl(self, which=None):
        if which is not None:
            return self._shortcmd(b'UIDL %s' % which)
        else:
            return self._longcmd(b'UIDL')


try:
    import ssl
except ImportError:
    pass
else:

    class POP3_SSL(POP3):

        def __init__(self, host, port=POP3_SSL_PORT, keyfile=None, certfile=None):
            self.host = host
            self.port = port
            self.keyfile = keyfile
            self.certfile = certfile
            self.buffer = b''
            msg = b'getaddrinfo returns an empty list'
            self.sock = None
            for res in socket.getaddrinfo(self.host, self.port, 0, socket.SOCK_STREAM):
                af, socktype, proto, canonname, sa = res
                try:
                    self.sock = socket.socket(af, socktype, proto)
                    self.sock.connect(sa)
                except socket.error as msg:
                    if self.sock:
                        self.sock.close()
                    self.sock = None
                    continue

                break

            if not self.sock:
                raise socket.error, msg
            self.file = self.sock.makefile(b'rb')
            self.sslobj = ssl.wrap_socket(self.sock, self.keyfile, self.certfile)
            self._debugging = 0
            self.welcome = self._getresp()
            return

        def _fillBuffer(self):
            localbuf = self.sslobj.read()
            if len(localbuf) == 0:
                raise error_proto(b'-ERR EOF')
            self.buffer += localbuf
            return

        def _getline(self):
            line = b''
            renewline = re.compile(b'.*?\\n')
            match = renewline.match(self.buffer)
            while not match:
                self._fillBuffer()
                if len(self.buffer) > _MAXLINE:
                    raise error_proto(b'line too long')
                match = renewline.match(self.buffer)

            line = match.group(0)
            self.buffer = renewline.sub(b'', self.buffer, 1)
            if self._debugging > 1:
                print b'*get*', repr(line)
            octets = len(line)
            if line[-2:] == CRLF:
                return (line[:-2], octets)
            if line[0] == CR:
                return (line[1:-1], octets)
            return (
             line[:-1], octets)

        def _putline(self, line):
            if self._debugging > 1:
                print b'*put*', repr(line)
            line += CRLF
            bytes = len(line)
            while bytes > 0:
                sent = self.sslobj.write(line)
                if sent == bytes:
                    break
                line = line[sent:]
                bytes = bytes - sent

            return

        def quit(self):
            try:
                resp = self._shortcmd(b'QUIT')
            except error_proto as val:
                resp = val

            self.sock.close()
            del self.sslobj
            del self.sock
            return resp


    __all__.append(b'POP3_SSL')

if __name__ == b'__main__':
    import sys
    a = POP3(sys.argv[1])
    print a.getwelcome()
    a.user(sys.argv[2])
    a.pass_(sys.argv[3])
    a.list()
    numMsgs, totalSize = a.stat()
    for i in range(1, numMsgs + 1):
        header, msg, octets = a.retr(i)
        print b'Message %d:' % i
        for line in msg:
            print b'   ' + line

        print b'-----------------------'

    a.quit()
