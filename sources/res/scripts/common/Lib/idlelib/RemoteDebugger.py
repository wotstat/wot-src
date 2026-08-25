import types
from idlelib import Debugger
debugging = 0
idb_adap_oid = b'idb_adapter'
gui_adap_oid = b'gui_adapter'
frametable = {}
dicttable = {}
codetable = {}
tracebacktable = {}

def wrap_frame(frame):
    fid = id(frame)
    frametable[fid] = frame
    return fid


def wrap_info(info):
    if info is None:
        return
    else:
        traceback = info[2]
        traceback_id = id(traceback)
        tracebacktable[traceback_id] = traceback
        modified_info = (info[0], info[1], traceback_id)
        return modified_info
        return


class GUIProxy:

    def __init__(self, conn, gui_adap_oid):
        self.conn = conn
        self.oid = gui_adap_oid
        return

    def interaction(self, message, frame, info=None):
        self.conn.remotecall(self.oid, b'interaction', (
         message, wrap_frame(frame), wrap_info(info)), {})
        return


class IdbAdapter:

    def __init__(self, idb):
        self.idb = idb
        return

    def set_step(self):
        self.idb.set_step()
        return

    def set_quit(self):
        self.idb.set_quit()
        return

    def set_continue(self):
        self.idb.set_continue()
        return

    def set_next(self, fid):
        frame = frametable[fid]
        self.idb.set_next(frame)
        return

    def set_return(self, fid):
        frame = frametable[fid]
        self.idb.set_return(frame)
        return

    def get_stack(self, fid, tbid):
        frame = frametable[fid]
        if tbid is None:
            tb = None
        else:
            tb = tracebacktable[tbid]
        stack, i = self.idb.get_stack(frame, tb)
        stack = [(wrap_frame(frame2), k) for frame2, k in stack]
        return (
         stack, i)

    def run(self, cmd):
        import __main__
        self.idb.run(cmd, __main__.__dict__)
        return

    def set_break(self, filename, lineno):
        msg = self.idb.set_break(filename, lineno)
        return msg

    def clear_break(self, filename, lineno):
        msg = self.idb.clear_break(filename, lineno)
        return msg

    def clear_all_file_breaks(self, filename):
        msg = self.idb.clear_all_file_breaks(filename)
        return msg

    def frame_attr(self, fid, name):
        frame = frametable[fid]
        return getattr(frame, name)

    def frame_globals(self, fid):
        frame = frametable[fid]
        dict = frame.f_globals
        did = id(dict)
        dicttable[did] = dict
        return did

    def frame_locals(self, fid):
        frame = frametable[fid]
        dict = frame.f_locals
        did = id(dict)
        dicttable[did] = dict
        return did

    def frame_code(self, fid):
        frame = frametable[fid]
        code = frame.f_code
        cid = id(code)
        codetable[cid] = code
        return cid

    def code_name(self, cid):
        code = codetable[cid]
        return code.co_name

    def code_filename(self, cid):
        code = codetable[cid]
        return code.co_filename

    def dict_keys(self, did):
        dict = dicttable[did]
        return dict.keys()

    def dict_item(self, did, key):
        dict = dicttable[did]
        value = dict[key]
        value = repr(value)
        return value


def start_debugger(rpchandler, gui_adap_oid):
    global idb_adap_oid
    gui_proxy = GUIProxy(rpchandler, gui_adap_oid)
    idb = Debugger.Idb(gui_proxy)
    idb_adap = IdbAdapter(idb)
    rpchandler.register(idb_adap_oid, idb_adap)
    return idb_adap_oid


class FrameProxy:

    def __init__(self, conn, fid):
        self._conn = conn
        self._fid = fid
        self._oid = b'idb_adapter'
        self._dictcache = {}
        return

    def __getattr__(self, name):
        if name[:1] == b'_':
            raise AttributeError, name
        if name == b'f_code':
            return self._get_f_code()
        if name == b'f_globals':
            return self._get_f_globals()
        if name == b'f_locals':
            return self._get_f_locals()
        return self._conn.remotecall(self._oid, b'frame_attr', (
         self._fid, name), {})

    def _get_f_code(self):
        cid = self._conn.remotecall(self._oid, b'frame_code', (self._fid,), {})
        return CodeProxy(self._conn, self._oid, cid)

    def _get_f_globals(self):
        did = self._conn.remotecall(self._oid, b'frame_globals', (
         self._fid,), {})
        return self._get_dict_proxy(did)

    def _get_f_locals(self):
        did = self._conn.remotecall(self._oid, b'frame_locals', (
         self._fid,), {})
        return self._get_dict_proxy(did)

    def _get_dict_proxy(self, did):
        if did in self._dictcache:
            return self._dictcache[did]
        dp = DictProxy(self._conn, self._oid, did)
        self._dictcache[did] = dp
        return dp


class CodeProxy:

    def __init__(self, conn, oid, cid):
        self._conn = conn
        self._oid = oid
        self._cid = cid
        return

    def __getattr__(self, name):
        if name == b'co_name':
            return self._conn.remotecall(self._oid, b'code_name', (
             self._cid,), {})
        if name == b'co_filename':
            return self._conn.remotecall(self._oid, b'code_filename', (
             self._cid,), {})
        return


class DictProxy:

    def __init__(self, conn, oid, did):
        self._conn = conn
        self._oid = oid
        self._did = did
        return

    def keys(self):
        return self._conn.remotecall(self._oid, b'dict_keys', (self._did,), {})

    def __getitem__(self, key):
        return self._conn.remotecall(self._oid, b'dict_item', (
         self._did, key), {})

    def __getattr__(self, name):
        raise AttributeError, name
        return


class GUIAdapter:

    def __init__(self, conn, gui):
        self.conn = conn
        self.gui = gui
        return

    def interaction(self, message, fid, modified_info):
        frame = FrameProxy(self.conn, fid)
        self.gui.interaction(message, frame, modified_info)
        return


class IdbProxy:

    def __init__(self, conn, shell, oid):
        self.oid = oid
        self.conn = conn
        self.shell = shell
        return

    def call(self, methodname, *args, **kwargs):
        value = self.conn.remotecall(self.oid, methodname, args, kwargs)
        return value

    def run(self, cmd, locals):
        seq = self.conn.asyncqueue(self.oid, b'run', (cmd,), {})
        self.shell.interp.active_seq = seq
        return

    def get_stack(self, frame, tbid):
        stack, i = self.call(b'get_stack', frame._fid, tbid)
        stack = [(FrameProxy(self.conn, fid), k) for fid, k in stack]
        return (stack, i)

    def set_continue(self):
        self.call(b'set_continue')
        return

    def set_step(self):
        self.call(b'set_step')
        return

    def set_next(self, frame):
        self.call(b'set_next', frame._fid)
        return

    def set_return(self, frame):
        self.call(b'set_return', frame._fid)
        return

    def set_quit(self):
        self.call(b'set_quit')
        return

    def set_break(self, filename, lineno):
        msg = self.call(b'set_break', filename, lineno)
        return msg

    def clear_break(self, filename, lineno):
        msg = self.call(b'clear_break', filename, lineno)
        return msg

    def clear_all_file_breaks(self, filename):
        msg = self.call(b'clear_all_file_breaks', filename)
        return msg


def start_remote_debugger(rpcclt, pyshell):
    global idb_adap_oid
    idb_adap_oid = rpcclt.remotecall(b'exec', b'start_the_debugger', (
     gui_adap_oid,), {})
    idb_proxy = IdbProxy(rpcclt, pyshell, idb_adap_oid)
    gui = Debugger.Debugger(pyshell, idb_proxy)
    gui_adap = GUIAdapter(rpcclt, gui)
    rpcclt.register(gui_adap_oid, gui_adap)
    return gui


def close_remote_debugger(rpcclt):
    close_subprocess_debugger(rpcclt)
    rpcclt.unregister(gui_adap_oid)
    return


def close_subprocess_debugger(rpcclt):
    rpcclt.remotecall(b'exec', b'stop_the_debugger', (idb_adap_oid,), {})
    return


def restart_subprocess_debugger(rpcclt):
    idb_adap_oid_ret = rpcclt.remotecall(b'exec', b'start_the_debugger', (
     gui_adap_oid,), {})
    return
