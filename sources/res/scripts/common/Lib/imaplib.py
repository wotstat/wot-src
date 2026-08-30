__version__ = b'2.58'
import binascii, errno, random, re, socket, subprocess, sys, time
__all__ = [
 3, 4, 5, 
 6, 7, 8]
CRLF = b'\r\n'
Debug = 0
IMAP4_PORT = 143
IMAP4_SSL_PORT = 993
AllowedVersions = (b'IMAP4REV1', b'IMAP4')
_MAXLINE = 1000000
Commands = {b'APPEND': (
             b'AUTH', b'SELECTED'), 
   b'AUTHENTICATE': (
                   b'NONAUTH',), 
   b'CAPABILITY': (
                 b'NONAUTH', b'AUTH', b'SELECTED', b'LOGOUT'), 
   b'CHECK': (
            b'SELECTED',), 
   b'CLOSE': (
            b'SELECTED',), 
   b'COPY': (
           b'SELECTED',), 
   b'CREATE': (
             b'AUTH', b'SELECTED'), 
   b'DELETE': (
             b'AUTH', b'SELECTED'), 
   b'DELETEACL': (
                b'AUTH', b'SELECTED'), 
   b'EXAMINE': (
              b'AUTH', b'SELECTED'), 
   b'EXPUNGE': (
              b'SELECTED',), 
   b'FETCH': (
            b'SELECTED',), 
   b'GETACL': (
             b'AUTH', b'SELECTED'), 
   b'GETANNOTATION': (
                    b'AUTH', b'SELECTED'), 
   b'GETQUOTA': (
               b'AUTH', b'SELECTED'), 
   b'GETQUOTAROOT': (
                   b'AUTH', b'SELECTED'), 
   b'MYRIGHTS': (
               b'AUTH', b'SELECTED'), 
   b'LIST': (
           b'AUTH', b'SELECTED'), 
   b'LOGIN': (
            b'NONAUTH',), 
   b'LOGOUT': (
             b'NONAUTH', b'AUTH', b'SELECTED', b'LOGOUT'), 
   b'LSUB': (
           b'AUTH', b'SELECTED'), 
   b'MOVE': (
           b'SELECTED',), 
   b'NAMESPACE': (
                b'AUTH', b'SELECTED'), 
   b'NOOP': (
           b'NONAUTH', b'AUTH', b'SELECTED', b'LOGOUT'), 
   b'PARTIAL': (
              b'SELECTED',), 
   b'PROXYAUTH': (
                b'AUTH',), 
   b'RENAME': (
             b'AUTH', b'SELECTED'), 
   b'SEARCH': (
             b'SELECTED',), 
   b'SELECT': (
             b'AUTH', b'SELECTED'), 
   b'SETACL': (
             b'AUTH', b'SELECTED'), 
   b'SETANNOTATION': (
                    b'AUTH', b'SELECTED'), 
   b'SETQUOTA': (
               b'AUTH', b'SELECTED'), 
   b'SORT': (
           b'SELECTED',), 
   b'STATUS': (
             b'AUTH', b'SELECTED'), 
   b'STORE': (
            b'SELECTED',), 
   b'SUBSCRIBE': (
                b'AUTH', b'SELECTED'), 
   b'THREAD': (
             b'SELECTED',), 
   b'UID': (
          b'SELECTED',), 
   b'UNSUBSCRIBE': (
                  b'AUTH', b'SELECTED')}
Continuation = re.compile(b'\\+( (?P<data>.*))?')
Flags = re.compile(b'.*FLAGS \\((?P<flags>[^\\)]*)\\)')
InternalDate = re.compile(b'.*INTERNALDATE "(?P<day>[ 0123][0-9])-(?P<mon>[A-Z][a-z][a-z])-(?P<year>[0-9][0-9][0-9][0-9]) (?P<hour>[0-9][0-9]):(?P<min>[0-9][0-9]):(?P<sec>[0-9][0-9]) (?P<zonen>[-+])(?P<zoneh>[0-9][0-9])(?P<zonem>[0-9][0-9])"')
Literal = re.compile(b'.*{(?P<size>\\d+)}$')
MapCRLF = re.compile(b'\\r\\n|\\r|\\n')
Response_code = re.compile(b'\\[(?P<type>[A-Z-]+)( (?P<data>[^\\]]*))?\\]')
Untagged_response = re.compile(b'\\* (?P<type>[A-Z-]+)( (?P<data>.*))?')
Untagged_status = re.compile(b'\\* (?P<data>\\d+) (?P<type>[A-Z-]+)( (?P<data2>.*))?')

class IMAP4():

    class error(Exception):
        pass

    class abort(error):
        pass

    class readonly(abort):
        pass

    mustquote = re.compile(b"[^\\w!#$%&'*+,.:;<=>?^`|~-]")

    def __init__(self, host=b'', port=IMAP4_PORT):
        self.debug = Debug
        self.state = b'LOGOUT'
        self.literal = None
        self.tagged_commands = {}
        self.untagged_responses = {}
        self.continuation_response = b''
        self.is_readonly = False
        self.tagnum = 0
        self.open(host, port)
        self.tagpre = Int2AP(random.randint(4096, 65535))
        self.tagre = re.compile(b'(?P<tag>' + self.tagpre + b'\\d+) (?P<type>[A-Z]+) (?P<data>.*)')
        self.welcome = self._get_response()
        if b'PREAUTH' in self.untagged_responses:
            self.state = b'AUTH'
        elif b'OK' in self.untagged_responses:
            self.state = b'NONAUTH'
        else:
            raise self.error(self.welcome)
        typ, dat = self.capability()
        if dat == [None]:
            raise self.error(b'no CAPABILITY response from server')
        self.capabilities = tuple(dat[-1].upper().split())
        for version in AllowedVersions:
            if version not in self.capabilities:
                continue
            self.PROTOCOL_VERSION = version
            return

        raise self.error(b'server not IMAP4 compliant')
        return

    def __getattr__(self, attr):
        if attr in Commands:
            return getattr(self, attr.lower())
        raise AttributeError(b"Unknown IMAP4 command: '%s'" % attr)
        return

    def open(self, host=b'', port=IMAP4_PORT):
        self.host = host
        self.port = port
        self.sock = socket.create_connection((host, port))
        self.file = self.sock.makefile(b'rb')
        return

    def read(self, size):
        return self.file.read(size)

    def readline(self):
        line = self.file.readline(_MAXLINE + 1)
        if len(line) > _MAXLINE:
            raise self.error(b'got more than %d bytes' % _MAXLINE)
        return line

    def send(self, data):
        self.sock.sendall(data)
        return

    def shutdown(self):
        self.file.close()
        try:
            try:
                self.sock.shutdown(socket.SHUT_RDWR)
            except socket.error as e:
                if e.errno not in (errno.ENOTCONN, 10022):
                    raise

        finally:
            self.sock.close()

        return

    def socket(self):
        return self.sock

    def recent(self):
        name = b'RECENT'
        typ, dat = self._untagged_response(b'OK', [None], name)
        if dat[-1]:
            return (typ, dat)
        else:
            typ, dat = self.noop()
            return self._untagged_response(typ, dat, name)

    def response(self, code):
        return self._untagged_response(code, [None], code.upper())

    def append(self, mailbox, flags, date_time, message):
        name = b'APPEND'
        if not mailbox:
            mailbox = b'INBOX'
        if flags:
            if (
             flags[0], flags[-1]) != (b'(', b')'):
                flags = b'(%s)' % flags
        else:
            flags = None
        if date_time:
            date_time = Time2Internaldate(date_time)
        else:
            date_time = None
        self.literal = MapCRLF.sub(CRLF, message)
        return self._simple_command(name, mailbox, flags, date_time)

    def authenticate(self, mechanism, authobject):
        mech = mechanism.upper()
        self.literal = _Authenticator(authobject).process
        typ, dat = self._simple_command(b'AUTHENTICATE', mech)
        if typ != b'OK':
            raise self.error(dat[-1])
        self.state = b'AUTH'
        return (typ, dat)

    def capability(self):
        name = b'CAPABILITY'
        typ, dat = self._simple_command(name)
        return self._untagged_response(typ, dat, name)

    def check(self):
        return self._simple_command(b'CHECK')

    def close(self):
        try:
            typ, dat = self._simple_command(b'CLOSE')
        finally:
            self.state = b'AUTH'

        return (
         typ, dat)

    def copy(self, message_set, new_mailbox):
        return self._simple_command(b'COPY', message_set, new_mailbox)

    def create(self, mailbox):
        return self._simple_command(b'CREATE', mailbox)

    def delete(self, mailbox):
        return self._simple_command(b'DELETE', mailbox)

    def deleteacl(self, mailbox, who):
        return self._simple_command(b'DELETEACL', mailbox, who)

    def expunge(self):
        name = b'EXPUNGE'
        typ, dat = self._simple_command(name)
        return self._untagged_response(typ, dat, name)

    def fetch(self, message_set, message_parts):
        name = b'FETCH'
        typ, dat = self._simple_command(name, message_set, message_parts)
        return self._untagged_response(typ, dat, name)

    def getacl(self, mailbox):
        typ, dat = self._simple_command(b'GETACL', mailbox)
        return self._untagged_response(typ, dat, b'ACL')

    def getannotation(self, mailbox, entry, attribute):
        typ, dat = self._simple_command(b'GETANNOTATION', mailbox, entry, attribute)
        return self._untagged_response(typ, dat, b'ANNOTATION')

    def getquota(self, root):
        typ, dat = self._simple_command(b'GETQUOTA', root)
        return self._untagged_response(typ, dat, b'QUOTA')

    def getquotaroot(self, mailbox):
        typ, dat = self._simple_command(b'GETQUOTAROOT', mailbox)
        typ, quota = self._untagged_response(typ, dat, b'QUOTA')
        typ, quotaroot = self._untagged_response(typ, dat, b'QUOTAROOT')
        return (typ, [quotaroot, quota])

    def list(self, directory=b'""', pattern=b'*'):
        name = b'LIST'
        typ, dat = self._simple_command(name, directory, pattern)
        return self._untagged_response(typ, dat, name)

    def login(self, user, password):
        typ, dat = self._simple_command(b'LOGIN', user, self._quote(password))
        if typ != b'OK':
            raise self.error(dat[-1])
        self.state = b'AUTH'
        return (typ, dat)

    def login_cram_md5(self, user, password):
        self.user, self.password = user, password
        return self.authenticate(b'CRAM-MD5', self._CRAM_MD5_AUTH)

    def _CRAM_MD5_AUTH(self, challenge):
        import hmac
        return self.user + b' ' + hmac.HMAC(self.password, challenge).hexdigest()

    def logout(self):
        self.state = b'LOGOUT'
        try:
            typ, dat = self._simple_command(b'LOGOUT')
        except:
            typ, dat = b'NO', [b'%s: %s' % sys.exc_info()[:2]]

        self.shutdown()
        if b'BYE' in self.untagged_responses:
            return (b'BYE', self.untagged_responses[b'BYE'])
        return (
         typ, dat)

    def lsub(self, directory=b'""', pattern=b'*'):
        name = b'LSUB'
        typ, dat = self._simple_command(name, directory, pattern)
        return self._untagged_response(typ, dat, name)

    def myrights(self, mailbox):
        typ, dat = self._simple_command(b'MYRIGHTS', mailbox)
        return self._untagged_response(typ, dat, b'MYRIGHTS')

    def namespace(self):
        name = b'NAMESPACE'
        typ, dat = self._simple_command(name)
        return self._untagged_response(typ, dat, name)

    def noop(self):
        return self._simple_command(b'NOOP')

    def partial(self, message_num, message_part, start, length):
        name = b'PARTIAL'
        typ, dat = self._simple_command(name, message_num, message_part, start, length)
        return self._untagged_response(typ, dat, b'FETCH')

    def proxyauth(self, user):
        name = b'PROXYAUTH'
        return self._simple_command(b'PROXYAUTH', user)

    def rename(self, oldmailbox, newmailbox):
        return self._simple_command(b'RENAME', oldmailbox, newmailbox)

    def search(self, charset, *criteria):
        name = b'SEARCH'
        if charset:
            typ, dat = self._simple_command(name, b'CHARSET', charset, *criteria)
        else:
            typ, dat = self._simple_command(name, *criteria)
        return self._untagged_response(typ, dat, name)

    def select(self, mailbox=b'INBOX', readonly=False):
        self.untagged_responses = {}
        self.is_readonly = readonly
        if readonly:
            name = b'EXAMINE'
        else:
            name = b'SELECT'
        typ, dat = self._simple_command(name, mailbox)
        if typ != b'OK':
            self.state = b'AUTH'
            return (
             typ, dat)
        else:
            self.state = b'SELECTED'
            if b'READ-ONLY' in self.untagged_responses and not readonly:
                raise self.readonly(b'%s is not writable' % mailbox)
            return (
             typ, self.untagged_responses.get(b'EXISTS', [None]))

    def setacl(self, mailbox, who, what):
        return self._simple_command(b'SETACL', mailbox, who, what)

    def setannotation(self, *args):
        typ, dat = self._simple_command(b'SETANNOTATION', *args)
        return self._untagged_response(typ, dat, b'ANNOTATION')

    def setquota(self, root, limits):
        typ, dat = self._simple_command(b'SETQUOTA', root, limits)
        return self._untagged_response(typ, dat, b'QUOTA')

    def sort(self, sort_criteria, charset, *search_criteria):
        name = b'SORT'
        if (
         sort_criteria[0], sort_criteria[-1]) != (b'(', b')'):
            sort_criteria = b'(%s)' % sort_criteria
        typ, dat = self._simple_command(name, sort_criteria, charset, *search_criteria)
        return self._untagged_response(typ, dat, name)

    def status(self, mailbox, names):
        name = b'STATUS'
        typ, dat = self._simple_command(name, mailbox, names)
        return self._untagged_response(typ, dat, name)

    def store(self, message_set, command, flags):
        if (
         flags[0], flags[-1]) != (b'(', b')'):
            flags = b'(%s)' % flags
        typ, dat = self._simple_command(b'STORE', message_set, command, flags)
        return self._untagged_response(typ, dat, b'FETCH')

    def subscribe(self, mailbox):
        return self._simple_command(b'SUBSCRIBE', mailbox)

    def thread(self, threading_algorithm, charset, *search_criteria):
        name = b'THREAD'
        typ, dat = self._simple_command(name, threading_algorithm, charset, *search_criteria)
        return self._untagged_response(typ, dat, name)

    def uid(self, command, *args):
        command = command.upper()
        if command not in Commands:
            raise self.error(b'Unknown IMAP4 UID command: %s' % command)
        if self.state not in Commands[command]:
            raise self.error(b'command %s illegal in state %s, only allowed in states %s' % (
             command, self.state,
             (b', ').join(Commands[command])))
        name = b'UID'
        typ, dat = self._simple_command(name, command, *args)
        if command in (b'SEARCH', b'SORT', b'THREAD'):
            name = command
        else:
            name = b'FETCH'
        return self._untagged_response(typ, dat, name)

    def unsubscribe(self, mailbox):
        return self._simple_command(b'UNSUBSCRIBE', mailbox)

    def xatom(self, name, *args):
        name = name.upper()
        if name not in Commands:
            Commands[name] = (
             self.state,)
        return self._simple_command(name, *args)

    def _append_untagged(self, typ, dat):
        if dat is None:
            dat = b''
        ur = self.untagged_responses
        if typ in ur:
            ur[typ].append(dat)
        else:
            ur[typ] = [
             dat]
        return

    def _check_bye(self):
        bye = self.untagged_responses.get(b'BYE')
        if bye:
            raise self.abort(bye[-1])
        return

    def _command(self, name, *args):
        if self.state not in Commands[name]:
            self.literal = None
            raise self.error(b'command %s illegal in state %s, only allowed in states %s' % (
             name, self.state,
             (b', ').join(Commands[name])))
        for typ in (b'OK', b'NO', b'BAD'):
            if typ in self.untagged_responses:
                del self.untagged_responses[typ]

        if b'READ-ONLY' in self.untagged_responses and not self.is_readonly:
            raise self.readonly(b'mailbox status changed to READ-ONLY')
        tag = self._new_tag()
        data = b'%s %s' % (tag, name)
        for arg in args:
            if arg is None:
                continue
            data = b'%s %s' % (data, self._checkquote(arg))

        literal = self.literal
        if literal is not None:
            self.literal = None
            if type(literal) is type(self._command):
                literator = literal
            else:
                literator = None
                data = b'%s {%s}' % (data, len(literal))
        try:
            self.send(b'%s%s' % (data, CRLF))
        except (socket.error, OSError) as val:
            raise self.abort(b'socket error: %s' % val)

        if literal is None:
            return tag
        else:
            while 1:
                while self._get_response():
                    if self.tagged_commands[tag]:
                        return tag

                if literator:
                    literal = literator(self.continuation_response)
                try:
                    self.send(literal)
                    self.send(CRLF)
                except (socket.error, OSError) as val:
                    raise self.abort(b'socket error: %s' % val)

                if not literator:
                    break

            return tag

    def _command_complete(self, name, tag):
        if name != b'LOGOUT':
            self._check_bye()
        try:
            typ, data = self._get_tagged_response(tag)
        except self.abort as val:
            raise self.abort(b'command: %s => %s' % (name, val))
        except self.error as val:
            raise self.error(b'command: %s => %s' % (name, val))

        if name != b'LOGOUT':
            self._check_bye()
        if typ == b'BAD':
            raise self.error(b'%s command error: %s %s' % (name, typ, data))
        return (
         typ, data)

    def _get_response(self):
        resp = self._get_line()
        if self._match(self.tagre, resp):
            tag = self.mo.group(b'tag')
            if tag not in self.tagged_commands:
                raise self.abort(b'unexpected tagged response: %s' % resp)
            typ = self.mo.group(b'type')
            dat = self.mo.group(b'data')
            self.tagged_commands[tag] = (typ, [dat])
        else:
            dat2 = None
            if not self._match(Untagged_response, resp):
                if self._match(Untagged_status, resp):
                    dat2 = self.mo.group(b'data2')
            if self.mo is None:
                if self._match(Continuation, resp):
                    self.continuation_response = self.mo.group(b'data')
                    return
                raise self.abort(b"unexpected response: '%s'" % resp)
            typ = self.mo.group(b'type')
            dat = self.mo.group(b'data')
            if dat is None:
                dat = b''
            if dat2:
                dat = dat + b' ' + dat2
            while self._match(Literal, dat):
                size = int(self.mo.group(b'size'))
                data = self.read(size)
                self._append_untagged(typ, (dat, data))
                dat = self._get_line()

            self._append_untagged(typ, dat)
        if typ in (b'OK', b'NO', b'BAD') and self._match(Response_code, dat):
            self._append_untagged(self.mo.group(b'type'), self.mo.group(b'data'))
        return resp

    def _get_tagged_response(self, tag):
        while 1:
            result = self.tagged_commands[tag]
            if result is not None:
                del self.tagged_commands[tag]
                return result
            self._check_bye()
            try:
                self._get_response()
            except self.abort as val:
                raise

        return

    def _get_line(self):
        line = self.readline()
        if not line:
            raise self.abort(b'socket error: EOF')
        if not line.endswith(b'\r\n'):
            raise self.abort(b'socket error: unterminated line')
        line = line[:-2]
        return line

    def _match(self, cre, s):
        self.mo = cre.match(s)
        return self.mo is not None

    def _new_tag(self):
        tag = b'%s%s' % (self.tagpre, self.tagnum)
        self.tagnum = self.tagnum + 1
        self.tagged_commands[tag] = None
        return tag

    def _checkquote(self, arg):
        if type(arg) is not type(b''):
            return arg
        else:
            if len(arg) >= 2 and (arg[0], arg[-1]) in ((b'(', b')'), (b'"', b'"')):
                return arg
            if arg and self.mustquote.search(arg) is None:
                return arg
            return self._quote(arg)

    def _quote(self, arg):
        arg = arg.replace(b'\\', b'\\\\')
        arg = arg.replace(b'"', b'\\"')
        return b'"%s"' % arg

    def _simple_command(self, name, *args):
        return self._command_complete(name, self._command(name, *args))

    def _untagged_response(self, typ, dat, name):
        if typ == b'NO':
            return (typ, dat)
        else:
            if name not in self.untagged_responses:
                return (typ, [None])
            data = self.untagged_responses.pop(name)
            return (
             typ, data)


try:
    import ssl
except ImportError:
    pass
else:

    class IMAP4_SSL(IMAP4):

        def __init__(self, host=b'', port=IMAP4_SSL_PORT, keyfile=None, certfile=None):
            self.keyfile = keyfile
            self.certfile = certfile
            IMAP4.__init__(self, host, port)
            return

        def open(self, host=b'', port=IMAP4_SSL_PORT):
            self.host = host
            self.port = port
            self.sock = socket.create_connection((host, port))
            self.sslobj = ssl.wrap_socket(self.sock, self.keyfile, self.certfile)
            self.file = self.sslobj.makefile(b'rb')
            return

        def send(self, data):
            bytes = len(data)
            while bytes > 0:
                sent = self.sslobj.write(data)
                if sent == bytes:
                    break
                data = data[sent:]
                bytes = bytes - sent

            return

        def shutdown(self):
            self.file.close()
            self.sock.close()
            return

        def socket(self):
            return self.sock

        def ssl(self):
            return self.sslobj


    __all__.append(b'IMAP4_SSL')

class IMAP4_stream(IMAP4):

    def __init__(self, command):
        self.command = command
        IMAP4.__init__(self)
        return

    def open(self, host=None, port=None):
        self.host = None
        self.port = None
        self.sock = None
        self.file = None
        self.process = subprocess.Popen(self.command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, close_fds=True)
        self.writefile = self.process.stdin
        self.readfile = self.process.stdout
        return

    def read(self, size):
        return self.readfile.read(size)

    def readline(self):
        return self.readfile.readline()

    def send(self, data):
        self.writefile.write(data)
        self.writefile.flush()
        return

    def shutdown(self):
        self.readfile.close()
        self.writefile.close()
        self.process.wait()
        return


class _Authenticator():

    def __init__(self, mechinst):
        self.mech = mechinst
        return

    def process(self, data):
        ret = self.mech(self.decode(data))
        if ret is None:
            return b'*'
        else:
            return self.encode(ret)

    def encode(self, inp):
        oup = b''
        while inp:
            if len(inp) > 48:
                t = inp[:48]
                inp = inp[48:]
            else:
                t = inp
                inp = b''
            e = binascii.b2a_base64(t)
            if e:
                oup = oup + e[:-1]

        return oup

    def decode(self, inp):
        if not inp:
            return b''
        return binascii.a2b_base64(inp)


Mon2num = {b'Jan': 1, b'Feb': 2, b'Mar': 3, b'Apr': 4, b'May': 5, b'Jun': 6, b'Jul': 7, 
   b'Aug': 8, b'Sep': 9, b'Oct': 10, b'Nov': 11, b'Dec': 12}

def Internaldate2tuple(resp):
    mo = InternalDate.match(resp)
    if not mo:
        return None
    else:
        mon = Mon2num[mo.group(b'mon')]
        zonen = mo.group(b'zonen')
        day = int(mo.group(b'day'))
        year = int(mo.group(b'year'))
        hour = int(mo.group(b'hour'))
        min = int(mo.group(b'min'))
        sec = int(mo.group(b'sec'))
        zoneh = int(mo.group(b'zoneh'))
        zonem = int(mo.group(b'zonem'))
        zone = (zoneh * 60 + zonem) * 60
        if zonen == b'-':
            zone = -zone
        tt = (year, mon, day, hour, min, sec, -1, -1, -1)
        utc = time.mktime(tt)
        lt = time.localtime(utc)
        if time.daylight and lt[-1]:
            zone = zone + time.altzone
        else:
            zone = zone + time.timezone
        return time.localtime(utc - zone)


def Int2AP(num):
    val = b''
    AP = b'ABCDEFGHIJKLMNOP'
    num = int(abs(num))
    while num:
        num, mod = divmod(num, 16)
        val = AP[mod] + val

    return val


def ParseFlags(resp):
    mo = Flags.match(resp)
    if not mo:
        return ()
    return tuple(mo.group(b'flags').split())


def Time2Internaldate(date_time):
    if isinstance(date_time, (int, long, float)):
        tt = time.localtime(date_time)
    elif isinstance(date_time, (tuple, time.struct_time)):
        tt = date_time
    elif isinstance(date_time, str) and (date_time[0], date_time[-1]) == (b'"', b'"'):
        return date_time
    raise ValueError(b'date_time not of a known type')
    dt = time.strftime(b'%d-%b-%Y %H:%M:%S', tt)
    if dt[0] == b'0':
        dt = b' ' + dt[1:]
    if time.daylight and tt[-1]:
        zone = -time.altzone
    else:
        zone = -time.timezone
    return b'"' + dt + b' %+03d%02d' % divmod(zone // 60, 60) + b'"'


if __name__ == b'__main__':
    import getopt, getpass
    try:
        optlist, args = getopt.getopt(sys.argv[1:], b'd:s:')
    except getopt.error as val:
        optlist, args = ((), ())

    stream_command = None
    for opt, val in optlist:
        if opt == b'-d':
            Debug = int(val)
        elif opt == b'-s':
            stream_command = val
            if not args:
                args = (stream_command,)

    if not args:
        args = (b'',)
    host = args[0]
    USER = getpass.getuser()
    PASSWD = getpass.getpass(b'IMAP password for %s on %s: ' % (USER, host or b'localhost'))
    test_mesg = b'From: %(user)s@localhost%(lf)sSubject: IMAP4 test%(lf)s%(lf)sdata...%(lf)s' % {b'user': USER, b'lf': b'\n'}
    test_seq1 = (
     (
      b'login', (USER, PASSWD)),
     (
      b'create', (b'/tmp/xxx 1',)),
     (
      b'rename', (b'/tmp/xxx 1', b'/tmp/yyy')),
     (
      b'CREATE', (b'/tmp/yyz 2',)),
     (
      b'append', (b'/tmp/yyz 2', None, None, test_mesg)),
     (
      b'list', (b'/tmp', b'yy*')),
     (
      b'select', (b'/tmp/yyz 2',)),
     (
      b'search', (None, b'SUBJECT', b'test')),
     (
      b'fetch', (b'1', b'(FLAGS INTERNALDATE RFC822)')),
     (
      b'store', (b'1', b'FLAGS', b'(\\Deleted)')),
     (
      b'namespace', ()),
     (
      b'expunge', ()),
     (
      b'recent', ()),
     (
      b'close', ()))
    test_seq2 = (
     (
      b'select', ()),
     (
      b'response', (b'UIDVALIDITY',)),
     (
      b'uid', (b'SEARCH', b'ALL')),
     (
      b'response', (b'EXISTS',)),
     (
      b'append', (None, None, None, test_mesg)),
     (
      b'recent', ()),
     (
      b'logout', ()))

    def run(cmd, args):
        M._mesg(b'%s %s' % (cmd, args))
        typ, dat = getattr(M, cmd)(*args)
        M._mesg(b'%s => %s %s' % (cmd, typ, dat))
        if typ == b'NO':
            raise dat[0]
        return dat


    try:
        if stream_command:
            M = IMAP4_stream(stream_command)
        else:
            M = IMAP4(host)
        if M.state == b'AUTH':
            test_seq1 = test_seq1[1:]
        M._mesg(b'PROTOCOL_VERSION = %s' % M.PROTOCOL_VERSION)
        M._mesg(b'CAPABILITIES = %r' % (M.capabilities,))
        for cmd, args in test_seq1:
            run(cmd, args)

        for ml in run(b'list', (b'/tmp/', b'yy%')):
            mo = re.match(b'.*"([^"]+)"$', ml)
            if mo:
                path = mo.group(1)
            else:
                path = ml.split()[-1]
            run(b'delete', (path,))

        for cmd, args in test_seq2:
            dat = run(cmd, args)
            if (
             cmd, args) != (b'uid', (b'SEARCH', b'ALL')):
                continue
            uid = dat[-1].split()
            if not uid:
                continue
            run(b'uid', (b'FETCH', b'%s' % uid[-1],
             b'(FLAGS INTERNALDATE RFC822.SIZE RFC822.HEADER RFC822.TEXT)'))

        print b'\nAll tests OK.'
    except:
        print b'\nTests failed.'
        if not Debug:
            print b'\nIf you would like to see debugging output,\ntry: %s -d5\n' % sys.argv[0]
        raise
