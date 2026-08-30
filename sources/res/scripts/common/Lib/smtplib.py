import socket, re, email.utils, base64, hmac
from email.base64mime import encode as encode_base64
from sys import stderr
__all__ = [
 4, 5, 6, 
 7, 8, 9, 
 10, 11, 12, 
 13, 14, 15]
SMTP_PORT = 25
SMTP_SSL_PORT = 465
CRLF = b'\r\n'
_MAXLINE = 8192
OLDSTYLE_AUTH = re.compile(b'auth=(.*)', re.I)

class SMTPException(Exception):
    pass


class SMTPServerDisconnected(SMTPException):
    pass


class SMTPResponseException(SMTPException):

    def __init__(self, code, msg):
        self.smtp_code = code
        self.smtp_error = msg
        self.args = (code, msg)
        return


class SMTPSenderRefused(SMTPResponseException):

    def __init__(self, code, msg, sender):
        self.smtp_code = code
        self.smtp_error = msg
        self.sender = sender
        self.args = (code, msg, sender)
        return


class SMTPRecipientsRefused(SMTPException):

    def __init__(self, recipients):
        self.recipients = recipients
        self.args = (recipients,)
        return


class SMTPDataError(SMTPResponseException):
    pass


class SMTPConnectError(SMTPResponseException):
    pass


class SMTPHeloError(SMTPResponseException):
    pass


class SMTPAuthenticationError(SMTPResponseException):
    pass


def quoteaddr(addr):
    m = (None, None)
    try:
        m = email.utils.parseaddr(addr)[1]
    except AttributeError:
        pass

    if m == (None, None):
        return b'<%s>' % addr
    else:
        if m is None:
            return b'<>'
        else:
            return b'<%s>' % m

        return


def _addr_only(addrstring):
    displayname, addr = email.utils.parseaddr(addrstring)
    if (displayname, addr) == (b'', b''):
        return addrstring
    return addr


def quotedata(data):
    return re.sub(b'(?m)^\\.', b'..', re.sub(b'(?:\\r\\n|\\n|\\r(?!\\n))', CRLF, data))


try:
    import ssl
except ImportError:
    _have_ssl = False
else:

    class SSLFakeFile():

        def __init__(self, sslobj):
            self.sslobj = sslobj
            return

        def readline(self, size=-1):
            if size < 0:
                size = None
            str = b''
            chr = None
            while chr != b'\n':
                if size is not None and len(str) >= size:
                    break
                chr = self.sslobj.read(1)
                if not chr:
                    break
                str += chr

            return str

        def close(self):
            return


    _have_ssl = True

class SMTP():
    debuglevel = 0
    file = None
    helo_resp = None
    ehlo_msg = b'ehlo'
    ehlo_resp = None
    does_esmtp = 0
    default_port = SMTP_PORT

    def __init__(self, host=b'', port=0, local_hostname=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
        self.timeout = timeout
        self.esmtp_features = {}
        if host:
            code, msg = self.connect(host, port)
            if code != 220:
                self.close()
                raise SMTPConnectError(code, msg)
        if local_hostname is not None:
            self.local_hostname = local_hostname
        else:
            fqdn = socket.getfqdn()
            if b'.' in fqdn:
                self.local_hostname = fqdn
            else:
                addr = b'127.0.0.1'
                try:
                    addr = socket.gethostbyname(socket.gethostname())
                except socket.gaierror:
                    pass

                self.local_hostname = b'[%s]' % addr
        return

    def set_debuglevel(self, debuglevel):
        self.debuglevel = debuglevel
        return

    def _get_socket(self, host, port, timeout):
        if self.debuglevel > 0:
            print >> stderr, b'connect:', (host, port)
        return socket.create_connection((host, port), timeout)

    def connect(self, host=b'localhost', port=0):
        if not port and host.find(b':') == host.rfind(b':'):
            i = host.rfind(b':')
            if i >= 0:
                host, port = host[:i], host[i + 1:]
                try:
                    port = int(port)
                except ValueError:
                    raise socket.error, b'nonnumeric port'

        if not port:
            port = self.default_port
        if self.debuglevel > 0:
            print >> stderr, b'connect:', (host, port)
        self.sock = self._get_socket(host, port, self.timeout)
        code, msg = self.getreply()
        if self.debuglevel > 0:
            print >> stderr, b'connect:', msg
        return (
         code, msg)

    def send(self, str):
        if self.debuglevel > 0:
            print >> stderr, b'send:', repr(str)
        if hasattr(self, b'sock') and self.sock:
            try:
                self.sock.sendall(str)
            except socket.error:
                self.close()
                raise SMTPServerDisconnected(b'Server not connected')

        else:
            raise SMTPServerDisconnected(b'please run connect() first')
        return

    def putcmd(self, cmd, args=b''):
        if args == b'':
            str = b'%s%s' % (cmd, CRLF)
        else:
            str = b'%s %s%s' % (cmd, args, CRLF)
        self.send(str)
        return

    def getreply(self):
        resp = []
        if self.file is None:
            self.file = self.sock.makefile(b'rb')
        while 1:
            try:
                line = self.file.readline(_MAXLINE + 1)
            except socket.error as e:
                self.close()
                raise SMTPServerDisconnected(b'Connection unexpectedly closed: ' + str(e))

            if line == b'':
                self.close()
                raise SMTPServerDisconnected(b'Connection unexpectedly closed')
            if self.debuglevel > 0:
                print >> stderr, b'reply:', repr(line)
            if len(line) > _MAXLINE:
                raise SMTPResponseException(500, b'Line too long.')
            resp.append(line[4:].strip())
            code = line[:3]
            try:
                errcode = int(code)
            except ValueError:
                errcode = -1
                break

            if line[3:4] != b'-':
                break

        errmsg = (b'\n').join(resp)
        if self.debuglevel > 0:
            print >> stderr, b'reply: retcode (%s); Msg: %s' % (errcode, errmsg)
        return (
         errcode, errmsg)

    def docmd(self, cmd, args=b''):
        self.putcmd(cmd, args)
        return self.getreply()

    def helo(self, name=b''):
        self.putcmd(b'helo', name or self.local_hostname)
        code, msg = self.getreply()
        self.helo_resp = msg
        return (code, msg)

    def ehlo(self, name=b''):
        self.esmtp_features = {}
        self.putcmd(self.ehlo_msg, name or self.local_hostname)
        code, msg = self.getreply()
        if code == -1 and len(msg) == 0:
            self.close()
            raise SMTPServerDisconnected(b'Server not connected')
        self.ehlo_resp = msg
        if code != 250:
            return (code, msg)
        self.does_esmtp = 1
        resp = self.ehlo_resp.split(b'\n')
        del resp[0]
        for each in resp:
            auth_match = OLDSTYLE_AUTH.match(each)
            if auth_match:
                self.esmtp_features[b'auth'] = self.esmtp_features.get(b'auth', b'') + b' ' + auth_match.groups(0)[0]
                continue
            m = re.match(b'(?P<feature>[A-Za-z0-9][A-Za-z0-9\\-]*) ?', each)
            if m:
                feature = m.group(b'feature').lower()
                params = m.string[m.end(b'feature'):].strip()
                if feature == b'auth':
                    self.esmtp_features[feature] = self.esmtp_features.get(feature, b'') + b' ' + params
                else:
                    self.esmtp_features[feature] = params

        return (
         code, msg)

    def has_extn(self, opt):
        return opt.lower() in self.esmtp_features

    def help(self, args=b''):
        self.putcmd(b'help', args)
        return self.getreply()[1]

    def rset(self):
        return self.docmd(b'rset')

    def noop(self):
        return self.docmd(b'noop')

    def mail(self, sender, options=[]):
        optionlist = b''
        if options and self.does_esmtp:
            optionlist = b' ' + (b' ').join(options)
        self.putcmd(b'mail', b'FROM:%s%s' % (quoteaddr(sender), optionlist))
        return self.getreply()

    def rcpt(self, recip, options=[]):
        optionlist = b''
        if options and self.does_esmtp:
            optionlist = b' ' + (b' ').join(options)
        self.putcmd(b'rcpt', b'TO:%s%s' % (quoteaddr(recip), optionlist))
        return self.getreply()

    def data(self, msg):
        self.putcmd(b'data')
        code, repl = self.getreply()
        if self.debuglevel > 0:
            print >> stderr, b'data:', (code, repl)
        if code != 354:
            raise SMTPDataError(code, repl)
        else:
            q = quotedata(msg)
            if q[-2:] != CRLF:
                q = q + CRLF
            q = q + b'.' + CRLF
            self.send(q)
            code, msg = self.getreply()
            if self.debuglevel > 0:
                print >> stderr, b'data:', (code, msg)
            return (
             code, msg)
        return

    def verify(self, address):
        self.putcmd(b'vrfy', _addr_only(address))
        return self.getreply()

    vrfy = verify

    def expn(self, address):
        self.putcmd(b'expn', _addr_only(address))
        return self.getreply()

    def ehlo_or_helo_if_needed(self):
        if self.helo_resp is None and self.ehlo_resp is None:
            if not 200 <= self.ehlo()[0] <= 299:
                code, resp = self.helo()
                if not 200 <= code <= 299:
                    raise SMTPHeloError(code, resp)
        return

    def login(self, user, password):

        def encode_cram_md5(challenge, user, password):
            challenge = base64.decodestring(challenge)
            response = user + b' ' + hmac.HMAC(password, challenge).hexdigest()
            return encode_base64(response, eol=b'')

        def encode_plain(user, password):
            return encode_base64(b'\x00%s\x00%s' % (user, password), eol=b'')

        AUTH_PLAIN = b'PLAIN'
        AUTH_CRAM_MD5 = b'CRAM-MD5'
        AUTH_LOGIN = b'LOGIN'
        self.ehlo_or_helo_if_needed()
        if not self.has_extn(b'auth'):
            raise SMTPException(b'SMTP AUTH extension not supported by server.')
        authlist = self.esmtp_features[b'auth'].split()
        preferred_auths = [
         AUTH_CRAM_MD5, AUTH_PLAIN, AUTH_LOGIN]
        authmethod = None
        for method in preferred_auths:
            if method in authlist:
                authmethod = method
                break

        if authmethod == AUTH_CRAM_MD5:
            code, resp = self.docmd(b'AUTH', AUTH_CRAM_MD5)
            if code == 503:
                return (
                 code, resp)
            code, resp = self.docmd(encode_cram_md5(resp, user, password))
        elif authmethod == AUTH_PLAIN:
            code, resp = self.docmd(b'AUTH', AUTH_PLAIN + b' ' + encode_plain(user, password))
        elif authmethod == AUTH_LOGIN:
            code, resp = self.docmd(b'AUTH', b'%s %s' % (AUTH_LOGIN, encode_base64(user, eol=b'')))
            if code != 334:
                raise SMTPAuthenticationError(code, resp)
            code, resp = self.docmd(encode_base64(password, eol=b''))
        elif authmethod is None:
            raise SMTPException(b'No suitable authentication method found.')
        if code not in (235, 503):
            raise SMTPAuthenticationError(code, resp)
        return (
         code, resp)

    def starttls(self, keyfile=None, certfile=None):
        self.ehlo_or_helo_if_needed()
        if not self.has_extn(b'starttls'):
            raise SMTPException(b'STARTTLS extension not supported by server.')
        resp, reply = self.docmd(b'STARTTLS')
        if resp == 220:
            if not _have_ssl:
                raise RuntimeError(b'No SSL support included in this Python')
            self.sock = ssl.wrap_socket(self.sock, keyfile, certfile)
            self.file = SSLFakeFile(self.sock)
            self.helo_resp = None
            self.ehlo_resp = None
            self.esmtp_features = {}
            self.does_esmtp = 0
        else:
            raise SMTPResponseException(resp, reply)
        return (
         resp, reply)

    def sendmail(self, from_addr, to_addrs, msg, mail_options=[], rcpt_options=[]):
        self.ehlo_or_helo_if_needed()
        esmtp_opts = []
        if self.does_esmtp:
            if self.has_extn(b'size'):
                esmtp_opts.append(b'size=%d' % len(msg))
            for option in mail_options:
                esmtp_opts.append(option)

        code, resp = self.mail(from_addr, esmtp_opts)
        if code != 250:
            self.rset()
            raise SMTPSenderRefused(code, resp, from_addr)
        senderrs = {}
        if isinstance(to_addrs, basestring):
            to_addrs = [
             to_addrs]
        for each in to_addrs:
            code, resp = self.rcpt(each, rcpt_options)
            if code != 250 and code != 251:
                senderrs[each] = (
                 code, resp)

        if len(senderrs) == len(to_addrs):
            self.rset()
            raise SMTPRecipientsRefused(senderrs)
        code, resp = self.data(msg)
        if code != 250:
            self.rset()
            raise SMTPDataError(code, resp)
        return senderrs

    def close(self):
        try:
            file = self.file
            self.file = None
            if file:
                file.close()
        finally:
            sock = self.sock
            self.sock = None
            if sock:
                sock.close()

        return

    def quit(self):
        res = self.docmd(b'quit')
        self.ehlo_resp = self.helo_resp = None
        self.esmtp_features = {}
        self.does_esmtp = False
        self.close()
        return res


if _have_ssl:

    class SMTP_SSL(SMTP):
        default_port = SMTP_SSL_PORT

        def __init__(self, host=b'', port=0, local_hostname=None, keyfile=None, certfile=None, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
            self.keyfile = keyfile
            self.certfile = certfile
            SMTP.__init__(self, host, port, local_hostname, timeout)
            return

        def _get_socket(self, host, port, timeout):
            if self.debuglevel > 0:
                print >> stderr, b'connect:', (host, port)
            new_socket = socket.create_connection((host, port), timeout)
            new_socket = ssl.wrap_socket(new_socket, self.keyfile, self.certfile)
            self.file = SSLFakeFile(new_socket)
            return new_socket


    __all__.append(b'SMTP_SSL')
LMTP_PORT = 2003

class LMTP(SMTP):
    ehlo_msg = b'lhlo'

    def __init__(self, host=b'', port=LMTP_PORT, local_hostname=None):
        SMTP.__init__(self, host, port, local_hostname)
        return

    def connect(self, host=b'localhost', port=0):
        if host[0] != b'/':
            return SMTP.connect(self, host, port)
        else:
            try:
                self.sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
                self.sock.connect(host)
            except socket.error:
                if self.debuglevel > 0:
                    print >> stderr, b'connect fail:', host
                if self.sock:
                    self.sock.close()
                self.sock = None
                raise

            code, msg = self.getreply()
            if self.debuglevel > 0:
                print >> stderr, b'connect:', msg
            return (
             code, msg)


if __name__ == b'__main__':
    import sys

    def prompt(prompt):
        sys.stdout.write(prompt + b': ')
        return sys.stdin.readline().strip()


    fromaddr = prompt(b'From')
    toaddrs = prompt(b'To').split(b',')
    print b'Enter message, end with ^D:'
    msg = b''
    while 1:
        line = sys.stdin.readline()
        if not line:
            break
        msg = msg + line

    print b'Message length is %d' % len(msg)
    server = SMTP(b'localhost')
    server.set_debuglevel(1)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
