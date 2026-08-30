__all__ = [
 b'BaseManager', b'SyncManager', b'BaseProxy', b'Token']
import os, sys, weakref, threading, array, Queue
from traceback import format_exc
from multiprocessing import Process, current_process, active_children, Pool, util, connection
from multiprocessing.process import AuthenticationString
from multiprocessing.forking import exit, Popen, assert_spawning, ForkingPickler
from multiprocessing.util import Finalize, info
try:
    from cPickle import PicklingError
except ImportError:
    from pickle import PicklingError

def reduce_array(a):
    return (
     array.array, (a.typecode, a.tostring()))


ForkingPickler.register(array.array, reduce_array)
view_types = [type(getattr({}, name)()) for name in (b'items', b'keys', b'values')]

class Token(object):
    __slots__ = (b'typeid', b'address', b'id')

    def __init__(self, typeid, address, id):
        self.typeid, self.address, self.id = typeid, address, id
        return

    def __getstate__(self):
        return (self.typeid, self.address, self.id)

    def __setstate__(self, state):
        self.typeid, self.address, self.id = state
        return

    def __repr__(self):
        return b'Token(typeid=%r, address=%r, id=%r)' % (
         self.typeid, self.address, self.id)


def dispatch(c, id, methodname, args=(), kwds={}):
    c.send((id, methodname, args, kwds))
    kind, result = c.recv()
    if kind == b'#RETURN':
        return result
    raise convert_to_error(kind, result)
    return


def convert_to_error(kind, result):
    if kind == b'#ERROR':
        return result
    else:
        if kind == b'#TRACEBACK':
            return RemoteError(result)
        if kind == b'#UNSERIALIZABLE':
            return RemoteError(b'Unserializable message: %s\n' % result)
        return ValueError(b'Unrecognized message type')

    return


class RemoteError(Exception):

    def __str__(self):
        return b'\n' + b'-' * 75 + b'\n' + str(self.args[0]) + b'-' * 75


def all_methods(obj):
    temp = []
    for name in dir(obj):
        func = getattr(obj, name)
        if hasattr(func, b'__call__'):
            temp.append(name)

    return temp


def public_methods(obj):
    return [name for name in all_methods(obj) if name[0] != b'_']


class Server(object):
    public = [
     0, 1, 2, 3, 
     4, 5, 6, 7, 8]

    def __init__(self, registry, address, authkey, serializer):
        self.registry = registry
        self.authkey = AuthenticationString(authkey)
        Listener, Client = listener_client[serializer]
        self.listener = Listener(address=address, backlog=16)
        self.address = self.listener.address
        self.id_to_obj = {b'0': (None, ())}
        self.id_to_refcount = {}
        self.mutex = threading.RLock()
        self.stop = 0
        return

    def serve_forever(self):
        current_process()._manager_server = self
        try:
            try:
                while 1:
                    try:
                        c = self.listener.accept()
                    except (OSError, IOError):
                        continue

                    t = threading.Thread(target=self.handle_request, args=(c,))
                    t.daemon = True
                    t.start()

            except (KeyboardInterrupt, SystemExit):
                pass

        finally:
            self.stop = 999
            self.listener.close()

        return

    def handle_request(self, c):
        funcname = result = request = None
        try:
            connection.deliver_challenge(c, self.authkey)
            connection.answer_challenge(c, self.authkey)
            request = c.recv()
            ignore, funcname, args, kwds = request
            func = getattr(self, funcname)
        except Exception:
            msg = (
             b'#TRACEBACK', format_exc())
        else:
            try:
                result = func(c, *args, **kwds)
            except Exception:
                msg = (
                 b'#TRACEBACK', format_exc())
            else:
                msg = (
                 b'#RETURN', result)

        try:
            c.send(msg)
        except Exception as e:
            try:
                c.send((b'#TRACEBACK', format_exc()))
            except Exception:
                pass

            util.info(b'Failure to send message: %r', msg)
            util.info(b' ... request was %r', request)
            util.info(b' ... exception was %r', e)

        c.close()
        return

    def serve_client(self, conn):
        util.debug(b'starting server thread to service %r', threading.current_thread().name)
        recv = conn.recv
        send = conn.send
        id_to_obj = self.id_to_obj
        while not self.stop:
            try:
                methodname = obj = None
                request = recv()
                ident, methodname, args, kwds = request
                obj, exposed, gettypeid = id_to_obj[ident]
                if methodname not in exposed:
                    raise AttributeError(b'method %r of %r object is not in exposed=%r' % (
                     methodname, type(obj), exposed))
                function = getattr(obj, methodname)
                try:
                    res = function(*args, **kwds)
                except Exception as e:
                    msg = (
                     b'#ERROR', e)

                typeid = gettypeid and gettypeid.get(methodname, None)
                if typeid:
                    rident, rexposed = self.create(conn, typeid, res)
                    token = Token(typeid, self.address, rident)
                    msg = (b'#PROXY', (rexposed, token))
                else:
                    msg = (
                     b'#RETURN', res)
            except AttributeError:
                if methodname is None:
                    msg = (
                     b'#TRACEBACK', format_exc())
                else:
                    try:
                        fallback_func = self.fallback_mapping[methodname]
                        result = fallback_func(self, conn, ident, obj, *args, **kwds)
                        msg = (
                         b'#RETURN', result)
                    except Exception:
                        msg = (
                         b'#TRACEBACK', format_exc())

            except EOFError:
                util.debug(b'got EOF -- exiting thread serving %r', threading.current_thread().name)
                sys.exit(0)
            except Exception:
                msg = (
                 b'#TRACEBACK', format_exc())

            try:
                try:
                    send(msg)
                except Exception as e:
                    send((b'#UNSERIALIZABLE', format_exc()))

            except Exception as e:
                util.info(b'exception in thread serving %r', threading.current_thread().name)
                util.info(b' ... message was %r', msg)
                util.info(b' ... exception was %r', e)
                conn.close()
                sys.exit(1)

        return

    def fallback_getvalue(self, conn, ident, obj):
        return obj

    def fallback_str(self, conn, ident, obj):
        return str(obj)

    def fallback_repr(self, conn, ident, obj):
        return repr(obj)

    fallback_mapping = {b'__str__': fallback_str, 
       b'__repr__': fallback_repr, 
       b'#GETVALUE': fallback_getvalue}

    def dummy(self, c):
        return

    def debug_info(self, c):
        self.mutex.acquire()
        try:
            result = []
            keys = self.id_to_obj.keys()
            keys.sort()
            for ident in keys:
                if ident != b'0':
                    result.append(b'  %s:       refcount=%s\n    %s' % (
                     ident, self.id_to_refcount[ident],
                     str(self.id_to_obj[ident][0])[:75]))

            return (b'\n').join(result)
        finally:
            self.mutex.release()

        return

    def number_of_objects(self, c):
        return len(self.id_to_obj) - 1

    def shutdown(self, c):
        try:
            try:
                util.debug(b'manager received shutdown message')
                c.send((b'#RETURN', None))
                if sys.stdout != sys.__stdout__:
                    util.debug(b'resetting stdout, stderr')
                    sys.stdout = sys.__stdout__
                    sys.stderr = sys.__stderr__
                util._run_finalizers(0)
                for p in active_children():
                    util.debug(b'terminating a child process of manager')
                    p.terminate()

                for p in active_children():
                    util.debug(b'terminating a child process of manager')
                    p.join()

                util._run_finalizers()
                util.info(b'manager exiting with exitcode 0')
            except:
                import traceback
                traceback.print_exc()

        finally:
            exit(0)

        return

    def create(self, c, typeid, *args, **kwds):
        self.mutex.acquire()
        try:
            callable, exposed, method_to_typeid, proxytype = self.registry[typeid]
            if callable is None:
                obj = args[0]
            else:
                obj = callable(*args, **kwds)
            if exposed is None:
                exposed = public_methods(obj)
            if method_to_typeid is not None:
                exposed = list(exposed) + list(method_to_typeid)
            ident = b'%x' % id(obj)
            util.debug(b'%r callable returned object with id %r', typeid, ident)
            self.id_to_obj[ident] = (
             obj, set(exposed), method_to_typeid)
            if ident not in self.id_to_refcount:
                self.id_to_refcount[ident] = 0
            self.incref(c, ident)
            return (ident, tuple(exposed))
        finally:
            self.mutex.release()

        return

    def get_methods(self, c, token):
        return tuple(self.id_to_obj[token.id][1])

    def accept_connection(self, c, name):
        threading.current_thread().name = name
        c.send((b'#RETURN', None))
        self.serve_client(c)
        return

    def incref(self, c, ident):
        self.mutex.acquire()
        try:
            self.id_to_refcount[ident] += 1
        finally:
            self.mutex.release()

        return

    def decref(self, c, ident):
        self.mutex.acquire()
        try:
            self.id_to_refcount[ident] -= 1
            if self.id_to_refcount[ident] == 0:
                del self.id_to_obj[ident]
                del self.id_to_refcount[ident]
                util.debug(b'disposing of obj with id %r', ident)
        finally:
            self.mutex.release()

        return


class State(object):
    __slots__ = [
     b'value']
    INITIAL = 0
    STARTED = 1
    SHUTDOWN = 2


listener_client = {b'pickle': (
             connection.Listener, connection.Client), 
   b'xmlrpclib': (
                connection.XmlListener, connection.XmlClient)}

class BaseManager(object):
    _registry = {}
    _Server = Server

    def __init__(self, address=None, authkey=None, serializer=b'pickle'):
        if authkey is None:
            authkey = current_process().authkey
        self._address = address
        self._authkey = AuthenticationString(authkey)
        self._state = State()
        self._state.value = State.INITIAL
        self._serializer = serializer
        self._Listener, self._Client = listener_client[serializer]
        return

    def __reduce__(self):
        return (type(self).from_address,
         (
          self._address, self._authkey, self._serializer))

    def get_server(self):
        return Server(self._registry, self._address, self._authkey, self._serializer)

    def connect(self):
        Listener, Client = listener_client[self._serializer]
        conn = Client(self._address, authkey=self._authkey)
        dispatch(conn, None, b'dummy')
        self._state.value = State.STARTED
        return

    def start(self, initializer=None, initargs=()):
        if initializer is not None and not hasattr(initializer, b'__call__'):
            raise TypeError(b'initializer must be a callable')
        reader, writer = connection.Pipe(duplex=False)
        self._process = Process(target=type(self)._run_server, args=(
         self._registry, self._address, self._authkey,
         self._serializer, writer, initializer, initargs))
        ident = (b':').join(str(i) for i in self._process._identity)
        self._process.name = type(self).__name__ + b'-' + ident
        self._process.start()
        writer.close()
        self._address = reader.recv()
        reader.close()
        self._state.value = State.STARTED
        self.shutdown = util.Finalize(self, type(self)._finalize_manager, args=(
         self._process, self._address, self._authkey,
         self._state, self._Client), exitpriority=0)
        return

    @classmethod
    def _run_server(cls, registry, address, authkey, serializer, writer, initializer=None, initargs=()):
        if initializer is not None:
            initializer(*initargs)
        server = cls._Server(registry, address, authkey, serializer)
        writer.send(server.address)
        writer.close()
        util.info(b'manager serving at %r', server.address)
        server.serve_forever()
        return

    def _create(self, typeid, *args, **kwds):
        conn = self._Client(self._address, authkey=self._authkey)
        try:
            id, exposed = dispatch(conn, None, b'create', (typeid,) + args, kwds)
        finally:
            conn.close()

        return (
         Token(typeid, self._address, id), exposed)

    def join(self, timeout=None):
        self._process.join(timeout)
        return

    def _debug_info(self):
        conn = self._Client(self._address, authkey=self._authkey)
        try:
            return dispatch(conn, None, b'debug_info')
        finally:
            conn.close()

        return

    def _number_of_objects(self):
        conn = self._Client(self._address, authkey=self._authkey)
        try:
            return dispatch(conn, None, b'number_of_objects')
        finally:
            conn.close()

        return

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.shutdown()
        return

    @staticmethod
    def _finalize_manager(process, address, authkey, state, _Client):
        if process.is_alive():
            util.info(b'sending shutdown message to manager')
            try:
                conn = _Client(address, authkey=authkey)
                try:
                    dispatch(conn, None, b'shutdown')
                finally:
                    conn.close()

            except Exception:
                pass

            process.join(timeout=0.2)
            if process.is_alive():
                util.info(b'manager still alive')
                if hasattr(process, b'terminate'):
                    util.info(b'trying to `terminate()` manager process')
                    process.terminate()
                    process.join(timeout=0.1)
                    if process.is_alive():
                        util.info(b'manager still alive after terminate')
        state.value = State.SHUTDOWN
        try:
            del BaseProxy._address_to_local[address]
        except KeyError:
            pass

        return

    address = property((lambda self: self._address))

    @classmethod
    def register(cls, typeid, callable=None, proxytype=None, exposed=None, method_to_typeid=None, create_method=True):
        if b'_registry' not in cls.__dict__:
            cls._registry = cls._registry.copy()
        if proxytype is None:
            proxytype = AutoProxy
        exposed = exposed or getattr(proxytype, b'_exposed_', None)
        method_to_typeid = method_to_typeid or getattr(proxytype, b'_method_to_typeid_', None)
        if method_to_typeid:
            for key, value in method_to_typeid.items():
                pass

        cls._registry[typeid] = (callable, exposed, method_to_typeid, proxytype)
        if create_method:

            def temp(self, *args, **kwds):
                util.debug(b'requesting creation of a shared %r object', typeid)
                token, exp = self._create(typeid, *args, **kwds)
                proxy = proxytype(token, self._serializer, manager=self, authkey=self._authkey, exposed=exp)
                conn = self._Client(token.address, authkey=self._authkey)
                dispatch(conn, None, b'decref', (token.id,))
                return proxy

            temp.__name__ = typeid
            setattr(cls, typeid, temp)
        return


class ProcessLocalSet(set):

    def __init__(self):
        util.register_after_fork(self, (lambda obj: obj.clear()))
        return

    def __reduce__(self):
        return (
         type(self), ())


class BaseProxy(object):
    _address_to_local = {}
    _mutex = util.ForkAwareThreadLock()

    def __init__(self, token, serializer, manager=None, authkey=None, exposed=None, incref=True):
        BaseProxy._mutex.acquire()
        try:
            tls_idset = BaseProxy._address_to_local.get(token.address, None)
            if tls_idset is None:
                tls_idset = (
                 util.ForkAwareLocal(), ProcessLocalSet())
                BaseProxy._address_to_local[token.address] = tls_idset
        finally:
            BaseProxy._mutex.release()

        self._tls = tls_idset[0]
        self._idset = tls_idset[1]
        self._token = token
        self._id = self._token.id
        self._manager = manager
        self._serializer = serializer
        self._Client = listener_client[serializer][1]
        if authkey is not None:
            self._authkey = AuthenticationString(authkey)
        elif self._manager is not None:
            self._authkey = self._manager._authkey
        else:
            self._authkey = current_process().authkey
        if incref:
            self._incref()
        util.register_after_fork(self, BaseProxy._after_fork)
        return

    def _connect(self):
        util.debug(b'making connection to manager')
        name = current_process().name
        if threading.current_thread().name != b'MainThread':
            name += b'|' + threading.current_thread().name
        conn = self._Client(self._token.address, authkey=self._authkey)
        dispatch(conn, None, b'accept_connection', (name,))
        self._tls.connection = conn
        return

    def _callmethod(self, methodname, args=(), kwds={}):
        try:
            conn = self._tls.connection
        except AttributeError:
            util.debug(b'thread %r does not own a connection', threading.current_thread().name)
            self._connect()
            conn = self._tls.connection

        conn.send((self._id, methodname, args, kwds))
        kind, result = conn.recv()
        if kind == b'#RETURN':
            return result
        else:
            if kind == b'#PROXY':
                exposed, token = result
                proxytype = self._manager._registry[token.typeid][-1]
                token.address = self._token.address
                proxy = proxytype(token, self._serializer, manager=self._manager, authkey=self._authkey, exposed=exposed)
                conn = self._Client(token.address, authkey=self._authkey)
                dispatch(conn, None, b'decref', (token.id,))
                return proxy
            raise convert_to_error(kind, result)
            return

    def _getvalue(self):
        return self._callmethod(b'#GETVALUE')

    def _incref(self):
        conn = self._Client(self._token.address, authkey=self._authkey)
        dispatch(conn, None, b'incref', (self._id,))
        util.debug(b'INCREF %r', self._token.id)
        self._idset.add(self._id)
        state = self._manager and self._manager._state
        self._close = util.Finalize(self, BaseProxy._decref, args=(
         self._token, self._authkey, state,
         self._tls, self._idset, self._Client), exitpriority=10)
        return

    @staticmethod
    def _decref(token, authkey, state, tls, idset, _Client):
        idset.discard(token.id)
        if state is None or state.value == State.STARTED:
            try:
                util.debug(b'DECREF %r', token.id)
                conn = _Client(token.address, authkey=authkey)
                dispatch(conn, None, b'decref', (token.id,))
            except Exception as e:
                util.debug(b'... decref failed %s', e)

        else:
            util.debug(b'DECREF %r -- manager already shutdown', token.id)
        if not idset and hasattr(tls, b'connection'):
            util.debug(b'thread %r has no more proxies so closing conn', threading.current_thread().name)
            tls.connection.close()
            del tls.connection
        return

    def _after_fork(self):
        self._manager = None
        try:
            self._incref()
        except Exception as e:
            util.info(b'incref failed: %s' % e)

        return

    def __reduce__(self):
        kwds = {}
        if Popen.thread_is_spawning():
            kwds[b'authkey'] = self._authkey
        if getattr(self, b'_isauto', False):
            kwds[b'exposed'] = self._exposed_
            return (
             RebuildProxy,
             (
              AutoProxy, self._token, self._serializer, kwds))
        else:
            return (
             RebuildProxy,
             (
              type(self), self._token, self._serializer, kwds))

        return

    def __deepcopy__(self, memo):
        return self._getvalue()

    def __repr__(self):
        return b'<%s object, typeid %r at %s>' % (
         type(self).__name__, self._token.typeid, b'0x%x' % id(self))

    def __str__(self):
        try:
            return self._callmethod(b'__repr__')
        except Exception:
            return repr(self)[:-1] + b"; '__str__()' failed>"

        return


def RebuildProxy(func, token, serializer, kwds):
    server = getattr(current_process(), b'_manager_server', None)
    if server and server.address == token.address:
        return server.id_to_obj[token.id][0]
    else:
        incref = kwds.pop(b'incref', True) and not getattr(current_process(), b'_inheriting', False)
        return func(token, serializer, incref=incref, **kwds)
        return


def MakeProxyType(name, exposed, _cache={}):
    exposed = tuple(exposed)
    try:
        return _cache[name, exposed]
    except KeyError:
        pass

    dic = {}
    for meth in exposed:
        exec b'def %s(self, *args, **kwds):\n        return self._callmethod(%r, args, kwds)' % (meth, meth) in dic

    ProxyType = type(name, (BaseProxy,), dic)
    ProxyType._exposed_ = exposed
    _cache[(name, exposed)] = ProxyType
    return ProxyType


def AutoProxy(token, serializer, manager=None, authkey=None, exposed=None, incref=True):
    _Client = listener_client[serializer][1]
    if exposed is None:
        conn = _Client(token.address, authkey=authkey)
        try:
            exposed = dispatch(conn, None, b'get_methods', (token,))
        finally:
            conn.close()

    if authkey is None and manager is not None:
        authkey = manager._authkey
    if authkey is None:
        authkey = current_process().authkey
    ProxyType = MakeProxyType(b'AutoProxy[%s]' % token.typeid, exposed)
    proxy = ProxyType(token, serializer, manager=manager, authkey=authkey, incref=incref)
    proxy._isauto = True
    return proxy


class Namespace(object):

    def __init__(self, **kwds):
        self.__dict__.update(kwds)
        return

    def __repr__(self):
        items = self.__dict__.items()
        temp = []
        for name, value in items:
            if not name.startswith(b'_'):
                temp.append(b'%s=%r' % (name, value))

        temp.sort()
        return b'Namespace(%s)' % str.join(b', ', temp)


class Value(object):

    def __init__(self, typecode, value, lock=True):
        self._typecode = typecode
        self._value = value
        return

    def get(self):
        return self._value

    def set(self, value):
        self._value = value
        return

    def __repr__(self):
        return b'%s(%r, %r)' % (type(self).__name__, self._typecode, self._value)

    value = property(get, set)


def Array(typecode, sequence, lock=True):
    return array.array(typecode, sequence)


class IteratorProxy(BaseProxy):
    _exposed_ = (b'__next__', b'next', b'send', b'throw', b'close')

    def __iter__(self):
        return self

    def __next__(self, *args):
        return self._callmethod(b'__next__', args)

    def next(self, *args):
        return self._callmethod(b'next', args)

    def send(self, *args):
        return self._callmethod(b'send', args)

    def throw(self, *args):
        return self._callmethod(b'throw', args)

    def close(self, *args):
        return self._callmethod(b'close', args)


class AcquirerProxy(BaseProxy):
    _exposed_ = (b'acquire', b'release')

    def acquire(self, blocking=True):
        return self._callmethod(b'acquire', (blocking,))

    def release(self):
        return self._callmethod(b'release')

    def __enter__(self):
        return self._callmethod(b'acquire')

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._callmethod(b'release')


class ConditionProxy(AcquirerProxy):
    _exposed_ = (b'acquire', b'release', b'wait', b'notify', b'notify_all')

    def wait(self, timeout=None):
        return self._callmethod(b'wait', (timeout,))

    def notify(self):
        return self._callmethod(b'notify')

    def notify_all(self):
        return self._callmethod(b'notify_all')


class EventProxy(BaseProxy):
    _exposed_ = (b'is_set', b'set', b'clear', b'wait')

    def is_set(self):
        return self._callmethod(b'is_set')

    def set(self):
        return self._callmethod(b'set')

    def clear(self):
        return self._callmethod(b'clear')

    def wait(self, timeout=None):
        return self._callmethod(b'wait', (timeout,))


class NamespaceProxy(BaseProxy):
    _exposed_ = (b'__getattribute__', b'__setattr__', b'__delattr__')

    def __getattr__(self, key):
        if key[0] == b'_':
            return object.__getattribute__(self, key)
        callmethod = object.__getattribute__(self, b'_callmethod')
        return callmethod(b'__getattribute__', (key,))

    def __setattr__(self, key, value):
        if key[0] == b'_':
            return object.__setattr__(self, key, value)
        callmethod = object.__getattribute__(self, b'_callmethod')
        return callmethod(b'__setattr__', (key, value))

    def __delattr__(self, key):
        if key[0] == b'_':
            return object.__delattr__(self, key)
        callmethod = object.__getattribute__(self, b'_callmethod')
        return callmethod(b'__delattr__', (key,))


class ValueProxy(BaseProxy):
    _exposed_ = (b'get', b'set')

    def get(self):
        return self._callmethod(b'get')

    def set(self, value):
        return self._callmethod(b'set', (value,))

    value = property(get, set)


BaseListProxy = MakeProxyType(b'BaseListProxy', (
 b'__add__', b'__contains__', b'__delitem__', b'__delslice__',
 b'__getitem__', b'__getslice__', b'__len__', b'__mul__',
 b'__reversed__', b'__rmul__', b'__setitem__', b'__setslice__',
 b'append', b'count', b'extend', b'index', b'insert', b'pop', b'remove',
 b'reverse', b'sort', b'__imul__'))

class ListProxy(BaseListProxy):

    def __iadd__(self, value):
        self._callmethod(b'extend', (value,))
        return self

    def __imul__(self, value):
        self._callmethod(b'__imul__', (value,))
        return self


DictProxy = MakeProxyType(b'DictProxy', (
 b'__contains__', b'__delitem__', b'__getitem__', b'__iter__', b'__len__',
 b'__setitem__', b'clear', b'copy', b'get', b'has_key', b'items',
 b'keys', b'pop', b'popitem', b'setdefault', b'update', b'values'))
DictProxy._method_to_typeid_ = {b'__iter__': b'Iterator'}
ArrayProxy = MakeProxyType(b'ArrayProxy', (
 b'__len__', b'__getitem__', b'__setitem__', b'__getslice__', b'__setslice__'))
PoolProxy = MakeProxyType(b'PoolProxy', (
 b'apply', b'apply_async', b'close', b'imap', b'imap_unordered', b'join',
 b'map', b'map_async', b'terminate'))
PoolProxy._method_to_typeid_ = {b'apply_async': b'AsyncResult', 
   b'map_async': b'AsyncResult', 
   b'imap': b'Iterator', 
   b'imap_unordered': b'Iterator'}

class SyncManager(BaseManager):
    pass


SyncManager.register(b'Queue', Queue.Queue)
SyncManager.register(b'JoinableQueue', Queue.Queue)
SyncManager.register(b'Event', threading.Event, EventProxy)
SyncManager.register(b'Lock', threading.Lock, AcquirerProxy)
SyncManager.register(b'RLock', threading.RLock, AcquirerProxy)
SyncManager.register(b'Semaphore', threading.Semaphore, AcquirerProxy)
SyncManager.register(b'BoundedSemaphore', threading.BoundedSemaphore, AcquirerProxy)
SyncManager.register(b'Condition', threading.Condition, ConditionProxy)
SyncManager.register(b'Pool', Pool, PoolProxy)
SyncManager.register(b'list', list, ListProxy)
SyncManager.register(b'dict', dict, DictProxy)
SyncManager.register(b'Value', Value, ValueProxy)
SyncManager.register(b'Array', Array, ArrayProxy)
SyncManager.register(b'Namespace', Namespace, NamespaceProxy)
SyncManager.register(b'Iterator', proxytype=IteratorProxy, create_method=False)
SyncManager.register(b'AsyncResult', create_method=False)
