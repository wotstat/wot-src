import sys, os, socket, select, SocketServer, struct, cPickle as pickle, threading, Queue, traceback, copy_reg, types, marshal

def unpickle_code(ms):
    co = marshal.loads(ms)
    return co


def pickle_code(co):
    ms = marshal.dumps(co)
    return (unpickle_code, (ms,))


copy_reg.pickle(types.CodeType, pickle_code, unpickle_code)
BUFSIZE = 8 * 1024
LOCALHOST = b'127.0.0.1'

class RPCServer(SocketServer.TCPServer):

    def __init__(self, addr, handlerclass=None):
        if handlerclass is None:
            handlerclass = RPCHandler
        SocketServer.TCPServer.__init__(self, addr, handlerclass)
        return

    def server_bind(self):
        return

    def server_activate(self):
        self.socket.connect(self.server_address)
        return

    def get_request(self):
        return (
         self.socket, self.server_address)

    def handle_error(self, request, client_address):
        try:
            raise
        except SystemExit:
            raise
        except:
            erf = sys.__stderr__
            print >> erf, b'\n' + b'-' * 40
            print >> erf, b'Unhandled server exception!'
            print >> erf, b'Thread: %s' % threading.currentThread().getName()
            print >> erf, b'Client Address: ', client_address
            print >> erf, b'Request: ', repr(request)
            traceback.print_exc(file=erf)
            print >> erf, b'\n*** Unrecoverable, server exiting!'
            print >> erf, b'-' * 40
            os._exit(0)

        return


objecttable = {}
request_queue = Queue.Queue(0)
response_queue = Queue.Queue(0)

class SocketIO(object):
    nextseq = 0

    def __init__(self, sock, objtable=None, debugging=None):
        self.sockthread = threading.currentThread()
        if debugging is not None:
            self.debugging = debugging
        self.sock = sock
        if objtable is None:
            objtable = objecttable
        self.objtable = objtable
        self.responses = {}
        self.cvars = {}
        return

    def close(self):
        sock = self.sock
        self.sock = None
        if sock is not None:
            sock.close()
        return

    def exithook(self):
        os._exit(0)
        return

    def debug(self, *args):
        if not self.debugging:
            return
        s = self.location + b' ' + str(threading.currentThread().getName())
        for a in args:
            s = s + b' ' + str(a)

        print >> sys.__stderr__, s
        return

    def register(self, oid, object):
        self.objtable[oid] = object
        return

    def unregister(self, oid):
        try:
            del self.objtable[oid]
        except KeyError:
            pass

        return

    def localcall(self, seq, request):
        self.debug(b'localcall:', request)
        try:
            how, (oid, methodname, args, kwargs) = request
        except TypeError:
            return (b'ERROR', b'Bad request format')

        if oid not in self.objtable:
            return (b'ERROR', b'Unknown object id: %r' % (oid,))
        else:
            obj = self.objtable[oid]
            if methodname == b'__methods__':
                methods = {}
                _getmethods(obj, methods)
                return (
                 b'OK', methods)
            if methodname == b'__attributes__':
                attributes = {}
                _getattributes(obj, attributes)
                return (
                 b'OK', attributes)
            if not hasattr(obj, methodname):
                return (b'ERROR', b'Unsupported method name: %r' % (methodname,))
            method = getattr(obj, methodname)
            try:
                if how == b'CALL':
                    ret = method(*args, **kwargs)
                    if isinstance(ret, RemoteObject):
                        ret = remoteref(ret)
                    return (b'OK', ret)
                else:
                    if how == b'QUEUE':
                        request_queue.put((seq, (method, args, kwargs)))
                        return (b'QUEUED', None)
                    return (b'ERROR', b'Unsupported message type: %s' % how)

            except SystemExit:
                raise
            except socket.error:
                raise
            except:
                msg = b'*** Internal Error: rpc.py:SocketIO.localcall()\n\n Object: %s \n Method: %s \n Args: %s\n'
                print >> sys.__stderr__, msg % (oid, method, args)
                traceback.print_exc(file=sys.__stderr__)
                return (b'EXCEPTION', None)

            return

    def remotecall(self, oid, methodname, args, kwargs):
        self.debug(b'remotecall:asynccall: ', oid, methodname)
        seq = self.asynccall(oid, methodname, args, kwargs)
        return self.asyncreturn(seq)

    def remotequeue(self, oid, methodname, args, kwargs):
        self.debug(b'remotequeue:asyncqueue: ', oid, methodname)
        seq = self.asyncqueue(oid, methodname, args, kwargs)
        return self.asyncreturn(seq)

    def asynccall(self, oid, methodname, args, kwargs):
        request = (
         b'CALL', (oid, methodname, args, kwargs))
        seq = self.newseq()
        if threading.currentThread() != self.sockthread:
            cvar = threading.Condition()
            self.cvars[seq] = cvar
        self.debug(b'asynccall:%d:' % seq, oid, methodname, args, kwargs)
        self.putmessage((seq, request))
        return seq

    def asyncqueue(self, oid, methodname, args, kwargs):
        request = (
         b'QUEUE', (oid, methodname, args, kwargs))
        seq = self.newseq()
        if threading.currentThread() != self.sockthread:
            cvar = threading.Condition()
            self.cvars[seq] = cvar
        self.debug(b'asyncqueue:%d:' % seq, oid, methodname, args, kwargs)
        self.putmessage((seq, request))
        return seq

    def asyncreturn(self, seq):
        self.debug(b'asyncreturn:%d:call getresponse(): ' % seq)
        response = self.getresponse(seq, wait=0.05)
        self.debug(b'asyncreturn:%d:response: ' % seq, response)
        return self.decoderesponse(response)

    def decoderesponse(self, response):
        how, what = response
        if how == b'OK':
            return what
        else:
            if how == b'QUEUED':
                return
            if how == b'EXCEPTION':
                self.debug(b'decoderesponse: EXCEPTION')
                return
            if how == b'EOF':
                self.debug(b'decoderesponse: EOF')
                self.decode_interrupthook()
                return
            if how == b'ERROR':
                self.debug(b'decoderesponse: Internal ERROR:', what)
                raise RuntimeError, what
            raise SystemError, (how, what)
            return

    def decode_interrupthook(self):
        raise EOFError
        return

    def mainloop(self):
        try:
            self.getresponse(myseq=None, wait=0.05)
        except EOFError:
            self.debug(b'mainloop:return')
            return

        return

    def getresponse(self, myseq, wait):
        response = self._getresponse(myseq, wait)
        if response is not None:
            how, what = response
            if how == b'OK':
                response = (
                 how, self._proxify(what))
        return response

    def _proxify(self, obj):
        if isinstance(obj, RemoteProxy):
            return RPCProxy(self, obj.oid)
        if isinstance(obj, types.ListType):
            return map(self._proxify, obj)
        return obj

    def _getresponse(self, myseq, wait):
        self.debug(b'_getresponse:myseq:', myseq)
        if threading.currentThread() is self.sockthread:
            while 1:
                response = self.pollresponse(myseq, wait)
                if response is not None:
                    return response

        else:
            cvar = self.cvars[myseq]
            cvar.acquire()
            while myseq not in self.responses:
                cvar.wait()

            response = self.responses[myseq]
            self.debug(b'_getresponse:%s: thread woke up: response: %s' % (
             myseq, response))
            del self.responses[myseq]
            del self.cvars[myseq]
            cvar.release()
            return response
        return

    def newseq(self):
        self.nextseq = seq = self.nextseq + 2
        return seq

    def putmessage(self, message):
        self.debug(b'putmessage:%d:' % message[0])
        try:
            s = pickle.dumps(message)
        except pickle.PicklingError:
            print >> sys.__stderr__, b'Cannot pickle:', repr(message)
            raise

        s = struct.pack(b'<i', len(s)) + s
        while len(s) > 0:
            try:
                r, w, x = select.select([], [self.sock], [])
                n = self.sock.send(s[:BUFSIZE])
            except (AttributeError, TypeError):
                raise IOError, b'socket no longer exists'

            s = s[n:]

        return

    buffer = b''
    bufneed = 4
    bufstate = 0

    def pollpacket(self, wait):
        self._stage0()
        if len(self.buffer) < self.bufneed:
            r, w, x = select.select([self.sock.fileno()], [], [], wait)
            if len(r) == 0:
                return None
            try:
                s = self.sock.recv(BUFSIZE)
            except socket.error:
                raise EOFError

            if len(s) == 0:
                raise EOFError
            self.buffer += s
            self._stage0()
        return self._stage1()

    def _stage0(self):
        if self.bufstate == 0 and len(self.buffer) >= 4:
            s = self.buffer[:4]
            self.buffer = self.buffer[4:]
            self.bufneed = struct.unpack(b'<i', s)[0]
            self.bufstate = 1
        return

    def _stage1(self):
        if self.bufstate == 1 and len(self.buffer) >= self.bufneed:
            packet = self.buffer[:self.bufneed]
            self.buffer = self.buffer[self.bufneed:]
            self.bufneed = 4
            self.bufstate = 0
            return packet
        return

    def pollmessage(self, wait):
        packet = self.pollpacket(wait)
        if packet is None:
            return
        else:
            try:
                message = pickle.loads(packet)
            except pickle.UnpicklingError:
                print >> sys.__stderr__, b'-----------------------'
                print >> sys.__stderr__, b'cannot unpickle packet:', repr(packet)
                traceback.print_stack(file=sys.__stderr__)
                print >> sys.__stderr__, b'-----------------------'
                raise

            return message

    def pollresponse(self, myseq, wait):
        while 1:
            try:
                qmsg = response_queue.get(0)
            except Queue.Empty:
                pass
            else:
                seq, response = qmsg
                message = (seq, (b'OK', response))
                self.putmessage(message)

            try:
                message = self.pollmessage(wait)
                if message is None:
                    return
            except EOFError:
                self.handle_EOF()
                return
            except AttributeError:
                return

            seq, resq = message
            how = resq[0]
            self.debug(b'pollresponse:%d:myseq:%s' % (seq, myseq))
            if how in (b'CALL', b'QUEUE'):
                self.debug(b'pollresponse:%d:localcall:call:' % seq)
                response = self.localcall(seq, resq)
                self.debug(b'pollresponse:%d:localcall:response:%s' % (
                 seq, response))
                if how == b'CALL':
                    self.putmessage((seq, response))
                elif how == b'QUEUE':
                    continue
                continue
            else:
                if seq == myseq:
                    return resq
                cv = self.cvars.get(seq, None)
                if cv is not None:
                    cv.acquire()
                    self.responses[seq] = resq
                    cv.notify()
                    cv.release()
                else:
                    continue

        return

    def handle_EOF(self):
        self.EOFhook()
        self.debug(b'handle_EOF')
        for key in self.cvars:
            cv = self.cvars[key]
            cv.acquire()
            self.responses[key] = (b'EOF', None)
            cv.notify()
            cv.release()

        self.exithook()
        return

    def EOFhook(self):
        return


class RemoteObject(object):
    pass


def remoteref(obj):
    oid = id(obj)
    objecttable[oid] = obj
    return RemoteProxy(oid)


class RemoteProxy(object):

    def __init__(self, oid):
        self.oid = oid
        return


class RPCHandler(SocketServer.BaseRequestHandler, SocketIO):
    debugging = False
    location = b'#S'

    def __init__(self, sock, addr, svr):
        svr.current_handler = self
        SocketIO.__init__(self, sock)
        SocketServer.BaseRequestHandler.__init__(self, sock, addr, svr)
        return

    def handle(self):
        self.mainloop()
        return

    def get_remote_proxy(self, oid):
        return RPCProxy(self, oid)


class RPCClient(SocketIO):
    debugging = False
    location = b'#C'
    nextseq = 1

    def __init__(self, address, family=socket.AF_INET, type=socket.SOCK_STREAM):
        self.listening_sock = socket.socket(family, type)
        self.listening_sock.bind(address)
        self.listening_sock.listen(1)
        return

    def accept(self):
        working_sock, address = self.listening_sock.accept()
        if self.debugging:
            print >> sys.__stderr__, b'****** Connection request from ', address
        if address[0] == LOCALHOST:
            SocketIO.__init__(self, working_sock)
        else:
            print >> sys.__stderr__, b'** Invalid host: ', address
            raise socket.error
        return

    def get_remote_proxy(self, oid):
        return RPCProxy(self, oid)


class RPCProxy(object):
    __methods = None
    __attributes = None

    def __init__(self, sockio, oid):
        self.sockio = sockio
        self.oid = oid
        return

    def __getattr__(self, name):
        if self.__methods is None:
            self.__getmethods()
        if self.__methods.get(name):
            return MethodProxy(self.sockio, self.oid, name)
        else:
            if self.__attributes is None:
                self.__getattributes()
            if name in self.__attributes:
                value = self.sockio.remotecall(self.oid, b'__getattribute__', (
                 name,), {})
                return value
            raise AttributeError, name
            return

    def __getattributes(self):
        self.__attributes = self.sockio.remotecall(self.oid, b'__attributes__', (), {})
        return

    def __getmethods(self):
        self.__methods = self.sockio.remotecall(self.oid, b'__methods__', (), {})
        return


def _getmethods(obj, methods):
    for name in dir(obj):
        attr = getattr(obj, name)
        if hasattr(attr, b'__call__'):
            methods[name] = 1

    if type(obj) == types.InstanceType:
        _getmethods(obj.__class__, methods)
    if type(obj) == types.ClassType:
        for super in obj.__bases__:
            _getmethods(super, methods)

    return


def _getattributes(obj, attributes):
    for name in dir(obj):
        attr = getattr(obj, name)
        if not hasattr(attr, b'__call__'):
            attributes[name] = 1

    return


class MethodProxy(object):

    def __init__(self, sockio, oid, name):
        self.sockio = sockio
        self.oid = oid
        self.name = name
        return

    def __call__(self, *args, **kwargs):
        value = self.sockio.remotecall(self.oid, self.name, args, kwargs)
        return value
