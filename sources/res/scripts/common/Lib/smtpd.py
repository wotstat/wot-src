import sys, os, errno, getopt, time, socket, asyncore, asynchat
__all__ = [
 b'SMTPServer', b'DebuggingServer', b'PureProxy', b'MailmanProxy']
program = sys.argv[0]
__version__ = b'Python SMTP proxy version 0.2'

class Devnull:

    def write(self, msg):
        return

    def flush(self):
        return


DEBUGSTREAM = Devnull()
NEWLINE = b'\n'
EMPTYSTRING = b''
COMMASPACE = b', '

def usage(code, msg=b''):
    print >> sys.stderr, __doc__ % globals()
    if msg:
        print >> sys.stderr, msg
    sys.exit(code)
    return


class SMTPChannel(asynchat.async_chat):
    COMMAND = 0
    DATA = 1

    def __init__(self, server, conn, addr):
        global DEBUGSTREAM
        asynchat.async_chat.__init__(self, conn)
        self.__server = server
        self.__conn = conn
        self.__addr = addr
        self.__line = []
        self.__state = self.COMMAND
        self.__greeting = 0
        self.__mailfrom = None
        self.__rcpttos = []
        self.__data = b''
        self.__fqdn = socket.getfqdn()
        try:
            self.__peer = conn.getpeername()
        except socket.error as err:
            self.close()
            if err[0] != errno.ENOTCONN:
                raise
            return

        print >> DEBUGSTREAM, b'Peer:', repr(self.__peer)
        self.push(b'220 %s %s' % (self.__fqdn, __version__))
        self.set_terminator(b'\r\n')
        return

    def push(self, msg):
        asynchat.async_chat.push(self, msg + b'\r\n')
        return

    def collect_incoming_data(self, data):
        self.__line.append(data)
        return

    def found_terminator(self):
        line = EMPTYSTRING.join(self.__line)
        print >> DEBUGSTREAM, b'Data:', repr(line)
        self.__line = []
        if self.__state == self.COMMAND:
            if not line:
                self.push(b'500 Error: bad syntax')
                return
            method = None
            i = line.find(b' ')
            if i < 0:
                command = line.upper()
                arg = None
            else:
                command = line[:i].upper()
                arg = line[i + 1:].strip()
            method = getattr(self, b'smtp_' + command, None)
            if not method:
                self.push(b'502 Error: command "%s" not implemented' % command)
                return
            method(arg)
            return
        else:
            if self.__state != self.DATA:
                self.push(b'451 Internal confusion')
                return
            data = []
            for text in line.split(b'\r\n'):
                if text and text[0] == b'.':
                    data.append(text[1:])
                else:
                    data.append(text)

            self.__data = NEWLINE.join(data)
            status = self.__server.process_message(self.__peer, self.__mailfrom, self.__rcpttos, self.__data)
            self.__rcpttos = []
            self.__mailfrom = None
            self.__state = self.COMMAND
            self.set_terminator(b'\r\n')
            if not status:
                self.push(b'250 Ok')
            else:
                self.push(status)
            return

    def smtp_HELO(self, arg):
        if not arg:
            self.push(b'501 Syntax: HELO hostname')
            return
        if self.__greeting:
            self.push(b'503 Duplicate HELO/EHLO')
        else:
            self.__greeting = arg
            self.push(b'250 %s' % self.__fqdn)
        return

    def smtp_NOOP(self, arg):
        if arg:
            self.push(b'501 Syntax: NOOP')
        else:
            self.push(b'250 Ok')
        return

    def smtp_QUIT(self, arg):
        self.push(b'221 Bye')
        self.close_when_done()
        return

    def __getaddr(self, keyword, arg):
        address = None
        keylen = len(keyword)
        if arg[:keylen].upper() == keyword:
            address = arg[keylen:].strip()
            if not address:
                pass
            elif address[0] == b'<' and address[-1] == b'>' and address != b'<>':
                address = address[1:-1]
        return address

    def smtp_MAIL(self, arg):
        print >> DEBUGSTREAM, b'===> MAIL', arg
        address = self.__getaddr(b'FROM:', arg) if arg else None
        if not address:
            self.push(b'501 Syntax: MAIL FROM:<address>')
            return
        else:
            if self.__mailfrom:
                self.push(b'503 Error: nested MAIL command')
                return
            self.__mailfrom = address
            print >> DEBUGSTREAM, b'sender:', self.__mailfrom
            self.push(b'250 Ok')
            return

    def smtp_RCPT(self, arg):
        print >> DEBUGSTREAM, b'===> RCPT', arg
        if not self.__mailfrom:
            self.push(b'503 Error: need MAIL command')
            return
        else:
            address = self.__getaddr(b'TO:', arg) if arg else None
            if not address:
                self.push(b'501 Syntax: RCPT TO: <address>')
                return
            self.__rcpttos.append(address)
            print >> DEBUGSTREAM, b'recips:', self.__rcpttos
            self.push(b'250 Ok')
            return

    def smtp_RSET(self, arg):
        if arg:
            self.push(b'501 Syntax: RSET')
            return
        else:
            self.__mailfrom = None
            self.__rcpttos = []
            self.__data = b''
            self.__state = self.COMMAND
            self.push(b'250 Ok')
            return

    def smtp_DATA(self, arg):
        if not self.__rcpttos:
            self.push(b'503 Error: need RCPT command')
            return
        if arg:
            self.push(b'501 Syntax: DATA')
            return
        self.__state = self.DATA
        self.set_terminator(b'\r\n.\r\n')
        self.push(b'354 End data with <CR><LF>.<CR><LF>')
        return


class SMTPServer(asyncore.dispatcher):

    def __init__(self, localaddr, remoteaddr):
        self._localaddr = localaddr
        self._remoteaddr = remoteaddr
        asyncore.dispatcher.__init__(self)
        try:
            self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
            self.set_reuse_addr()
            self.bind(localaddr)
            self.listen(5)
        except:
            self.close()
            raise
        else:
            print >> DEBUGSTREAM, b'%s started at %s\n\tLocal addr: %s\n\tRemote addr:%s' % (
             self.__class__.__name__, time.ctime(time.time()),
             localaddr, remoteaddr)

        return

    def handle_accept(self):
        pair = self.accept()
        if pair is not None:
            conn, addr = pair
            print >> DEBUGSTREAM, b'Incoming connection from %s' % repr(addr)
            channel = SMTPChannel(self, conn, addr)
        return

    def process_message(self, peer, mailfrom, rcpttos, data):
        raise NotImplementedError
        return


class DebuggingServer(SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        inheaders = 1
        lines = data.split(b'\n')
        print b'---------- MESSAGE FOLLOWS ----------'
        for line in lines:
            if inheaders and not line:
                print b'X-Peer:', peer[0]
                inheaders = 0
            print line

        print b'------------ END MESSAGE ------------'
        return


class PureProxy(SMTPServer):

    def process_message(self, peer, mailfrom, rcpttos, data):
        lines = data.split(b'\n')
        i = 0
        for line in lines:
            if not line:
                break
            i += 1

        lines.insert(i, b'X-Peer: %s' % peer[0])
        data = NEWLINE.join(lines)
        refused = self._deliver(mailfrom, rcpttos, data)
        print >> DEBUGSTREAM, b'we got some refusals:', refused
        return

    def _deliver(self, mailfrom, rcpttos, data):
        import smtplib
        refused = {}
        try:
            s = smtplib.SMTP()
            s.connect(self._remoteaddr[0], self._remoteaddr[1])
            try:
                refused = s.sendmail(mailfrom, rcpttos, data)
            finally:
                s.quit()

        except smtplib.SMTPRecipientsRefused as e:
            print >> DEBUGSTREAM, b'got SMTPRecipientsRefused'
            refused = e.recipients
        except (socket.error, smtplib.SMTPException) as e:
            print >> DEBUGSTREAM, b'got', e.__class__
            errcode = getattr(e, b'smtp_code', -1)
            errmsg = getattr(e, b'smtp_error', b'ignore')
            for r in rcpttos:
                refused[r] = (
                 errcode, errmsg)

        return refused


class MailmanProxy(PureProxy):

    def process_message(self, peer, mailfrom, rcpttos, data):
        from cStringIO import StringIO
        from Mailman import Utils
        from Mailman import Message
        from Mailman import MailList
        listnames = []
        for rcpt in rcpttos:
            local = rcpt.lower().split(b'@')[0]
            parts = local.split(b'-')
            if len(parts) > 2:
                continue
            listname = parts[0]
            if len(parts) == 2:
                command = parts[1]
            else:
                command = b''
            if not Utils.list_exists(listname) or command not in (b'', b'admin', b'owner', b'request', b'join', b'leave'):
                continue
            listnames.append((rcpt, listname, command))

        for rcpt, listname, command in listnames:
            rcpttos.remove(rcpt)

        print >> DEBUGSTREAM, b'forwarding recips:', (b' ').join(rcpttos)
        if rcpttos:
            refused = self._deliver(mailfrom, rcpttos, data)
            print >> DEBUGSTREAM, b'we got refusals:', refused
        mlists = {}
        s = StringIO(data)
        msg = Message.Message(s)
        if not msg.getheader(b'from'):
            msg[b'From'] = mailfrom
        if not msg.getheader(b'date'):
            msg[b'Date'] = time.ctime(time.time())
        for rcpt, listname, command in listnames:
            print >> DEBUGSTREAM, b'sending message to', rcpt
            mlist = mlists.get(listname)
            if not mlist:
                mlist = MailList.MailList(listname, lock=0)
                mlists[listname] = mlist
            if command == b'':
                msg.Enqueue(mlist, tolist=1)
            elif command == b'admin':
                msg.Enqueue(mlist, toadmin=1)
            elif command == b'owner':
                msg.Enqueue(mlist, toowner=1)
            elif command == b'request':
                msg.Enqueue(mlist, torequest=1)
            elif command in (b'join', b'leave'):
                if command == b'join':
                    msg[b'Subject'] = b'subscribe'
                else:
                    msg[b'Subject'] = b'unsubscribe'
                msg.Enqueue(mlist, torequest=1)

        return


class Options:
    setuid = 1
    classname = b'PureProxy'


def parseargs():
    global DEBUGSTREAM
    try:
        opts, args = getopt.getopt(sys.argv[1:], b'nVhc:d', [
         3, 4, 5, 6, 7])
    except getopt.error as e:
        usage(1, e)

    options = Options()
    for opt, arg in opts:
        if opt in (b'-h', b'--help'):
            usage(0)
        elif opt in (b'-V', b'--version'):
            print >> sys.stderr, __version__
            sys.exit(0)
        elif opt in (b'-n', b'--nosetuid'):
            options.setuid = 0
        elif opt in (b'-c', b'--class'):
            options.classname = arg
        elif opt in (b'-d', b'--debug'):
            DEBUGSTREAM = sys.stderr

    if len(args) < 1:
        localspec = b'localhost:8025'
        remotespec = b'localhost:25'
    elif len(args) < 2:
        localspec = args[0]
        remotespec = b'localhost:25'
    elif len(args) < 3:
        localspec = args[0]
        remotespec = args[1]
    else:
        usage(1, b'Invalid arguments: %s' % COMMASPACE.join(args))
    i = localspec.find(b':')
    if i < 0:
        usage(1, b'Bad local spec: %s' % localspec)
    options.localhost = localspec[:i]
    try:
        options.localport = int(localspec[i + 1:])
    except ValueError:
        usage(1, b'Bad local port: %s' % localspec)

    i = remotespec.find(b':')
    if i < 0:
        usage(1, b'Bad remote spec: %s' % remotespec)
    options.remotehost = remotespec[:i]
    try:
        options.remoteport = int(remotespec[i + 1:])
    except ValueError:
        usage(1, b'Bad remote port: %s' % remotespec)

    return options


if __name__ == b'__main__':
    options = parseargs()
    classname = options.classname
    if b'.' in classname:
        lastdot = classname.rfind(b'.')
        mod = __import__(classname[:lastdot], globals(), locals(), [b''])
        classname = classname[lastdot + 1:]
    else:
        import __main__ as mod
    class_ = getattr(mod, classname)
    proxy = class_((options.localhost, options.localport), (
     options.remotehost, options.remoteport))
    if options.setuid:
        try:
            import pwd
        except ImportError:
            print >> sys.stderr, b'Cannot import module "pwd"; try running with -n option.'
            sys.exit(1)

        nobody = pwd.getpwnam(b'nobody')[2]
        try:
            os.setuid(nobody)
        except OSError as e:
            if e.errno != errno.EPERM:
                raise
            print >> sys.stderr, b'Cannot setuid "nobody"; try running with -n option.'
            sys.exit(1)

    try:
        asyncore.loop()
    except KeyboardInterrupt:
        pass
