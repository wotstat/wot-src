import sys, linecache, time, socket, traceback, thread, threading, Queue
from idlelib import CallTips
from idlelib import AutoComplete
from idlelib import RemoteDebugger
from idlelib import RemoteObjectBrowser
from idlelib import StackViewer
from idlelib import rpc
from idlelib import PyShell
from idlelib import IOBinding
import __main__
LOCALHOST = b'127.0.0.1'
import warnings

def idle_showwarning_subproc(message, category, filename, lineno, file=None, line=None):
    if file is None:
        file = sys.stderr
    try:
        file.write(PyShell.idle_formatwarning(message, category, filename, lineno, line))
    except IOError:
        pass

    return


_warnings_showwarning = None

def capture_warnings(capture):
    global _warnings_showwarning
    if capture:
        if _warnings_showwarning is None:
            _warnings_showwarning = warnings.showwarning
            warnings.showwarning = idle_showwarning_subproc
    elif _warnings_showwarning is not None:
        warnings.showwarning = _warnings_showwarning
        _warnings_showwarning = None
    return


capture_warnings(True)
exit_now = False
quitting = False
interruptable = False

def main(del_exitfunc=False):
    global exit_now
    global no_exitfunc
    global quitting
    no_exitfunc = del_exitfunc
    try:
        port = int(sys.argv[-1])
    except:
        print >> sys.stderr, b'IDLE Subprocess: no IP port passed in sys.argv.'
        return

    capture_warnings(True)
    sys.argv[:] = [b'']
    sockthread = threading.Thread(target=manage_socket, name=b'SockThread', args=(
     (
      LOCALHOST, port),))
    sockthread.setDaemon(True)
    sockthread.start()
    while 1:
        try:
            if exit_now:
                try:
                    exit()
                except KeyboardInterrupt:
                    continue

            try:
                seq, request = rpc.request_queue.get(block=True, timeout=0.05)
            except Queue.Empty:
                continue

            method, args, kwargs = request
            ret = method(*args, **kwargs)
            rpc.response_queue.put((seq, ret))
        except KeyboardInterrupt:
            if quitting:
                exit_now = True
            continue
        except SystemExit:
            capture_warnings(False)
            raise
        except:
            type, value, tb = sys.exc_info()
            try:
                print_exception()
                rpc.response_queue.put((seq, None))
            except:
                traceback.print_exception(type, value, tb, file=sys.__stderr__)
                exit()
            else:
                continue

    return


def manage_socket(address):
    global exit_now
    for i in range(3):
        time.sleep(i)
        try:
            server = MyRPCServer(address, MyHandler)
            break
        except socket.error as err:
            print >> sys.__stderr__, b'IDLE Subprocess: socket error: ' + err.args[1] + b', retrying....'

    else:
        print >> sys.__stderr__, b'IDLE Subprocess: Connection to IDLE GUI failed, exiting.'
        show_socket_error(err, address)
        exit_now = True
        return

    server.handle_request()
    return


def show_socket_error(err, address):
    import Tkinter, tkMessageBox
    root = Tkinter.Tk()
    fix_scaling(root)
    root.withdraw()
    if err.args[0] == 61:
        msg = b"IDLE's subprocess can't connect to %s:%d.  This may be due to your personal firewall configuration.  It is safe to allow this internal connection because no data is visible on external ports." % address
        tkMessageBox.showerror(b'IDLE Subprocess Error', msg, parent=root)
    else:
        tkMessageBox.showerror(b'IDLE Subprocess Error', b'Socket Error: %s' % err.args[1], parent=root)
    root.destroy()
    return


def print_exception():
    import linecache
    linecache.checkcache()
    flush_stdout()
    efile = sys.stderr
    typ, val, tb = excinfo = sys.exc_info()
    sys.last_type, sys.last_value, sys.last_traceback = excinfo
    tbe = traceback.extract_tb(tb)
    print >> efile, b'\nTraceback (most recent call last):'
    exclude = (b'run.py', b'rpc.py', b'threading.py', b'Queue.py', b'RemoteDebugger.py', b'bdb.py')
    cleanup_traceback(tbe, exclude)
    traceback.print_list(tbe, file=efile)
    lines = traceback.format_exception_only(typ, val)
    for line in lines:
        print >> efile, line,

    return


def cleanup_traceback(tb, exclude):
    orig_tb = tb[:]
    while tb:
        for rpcfile in exclude:
            if tb[0][0].count(rpcfile):
                break
        else:
            break

        del tb[0]

    while tb:
        for rpcfile in exclude:
            if tb[-1][0].count(rpcfile):
                break
        else:
            break

        del tb[-1]

    if len(tb) == 0:
        tb[:] = orig_tb[:]
        print >> sys.stderr, b'** IDLE Internal Exception: '
    rpchandler = rpc.objecttable[b'exec'].rpchandler
    for i in range(len(tb)):
        fn, ln, nm, line = tb[i]
        if nm == b'?':
            nm = b'-toplevel-'
        if fn.startswith(b'<pyshell#') and IOBinding.encoding != b'utf-8':
            ln -= 1
        if not line and fn.startswith(b'<pyshell#'):
            line = rpchandler.remotecall(b'linecache', b'getline', (
             fn, ln), {})
        tb[i] = (
         fn, ln, nm, line)

    return


def flush_stdout():
    try:
        if sys.stdout.softspace:
            sys.stdout.softspace = 0
            sys.stdout.write(b'\n')
    except (AttributeError, EOFError):
        pass

    return


def exit():
    if no_exitfunc:
        try:
            del sys.exitfunc
        except AttributeError:
            pass

    capture_warnings(False)
    sys.exit(0)
    return


def fix_scaling(root):
    import tkFont
    scaling = float(root.tk.call(b'tk', b'scaling'))
    if scaling > 1.4:
        for name in tkFont.names(root):
            font = tkFont.Font(root=root, name=name, exists=True)
            size = int(font[b'size'])
            if size < 0:
                font[b'size'] = int(round(-0.75 * size))

    return


class MyRPCServer(rpc.RPCServer):

    def handle_error(self, request, client_address):
        global exit_now
        global quitting
        try:
            raise
        except SystemExit:
            raise
        except EOFError:
            exit_now = True
            thread.interrupt_main()
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
            quitting = True
            thread.interrupt_main()

        return


class MyHandler(rpc.RPCHandler):

    def handle(self):
        executive = Executive(self)
        self.register(b'exec', executive)
        self.console = self.get_remote_proxy(b'console')
        sys.stdin = PyShell.PseudoInputFile(self.console, b'stdin', IOBinding.encoding)
        sys.stdout = PyShell.PseudoOutputFile(self.console, b'stdout', IOBinding.encoding)
        sys.stderr = PyShell.PseudoOutputFile(self.console, b'stderr', IOBinding.encoding)
        self._keep_stdin = sys.stdin
        self.interp = self.get_remote_proxy(b'interp')
        rpc.RPCHandler.getresponse(self, myseq=None, wait=0.05)
        return

    def exithook(self):
        time.sleep(10)
        return

    def EOFhook(self):
        global quitting
        quitting = True
        thread.interrupt_main()
        return

    def decode_interrupthook(self):
        global quitting
        quitting = True
        thread.interrupt_main()
        return


class Executive(object):

    def __init__(self, rpchandler):
        self.rpchandler = rpchandler
        self.locals = __main__.__dict__
        self.calltip = CallTips.CallTips()
        self.autocomplete = AutoComplete.AutoComplete()
        return

    def runcode(self, code):
        global interruptable
        try:
            self.usr_exc_info = None
            interruptable = True
            try:
                exec code in self.locals
            finally:
                interruptable = False

        except SystemExit:
            pass
        except:
            self.usr_exc_info = sys.exc_info()
            if quitting:
                exit()
            print_exception()
            jit = self.rpchandler.console.getvar(b'<<toggle-jit-stack-viewer>>')
            if jit:
                self.rpchandler.interp.open_remote_stack_viewer()
        else:
            flush_stdout()

        return

    def interrupt_the_server(self):
        if interruptable:
            thread.interrupt_main()
        return

    def start_the_debugger(self, gui_adap_oid):
        return RemoteDebugger.start_debugger(self.rpchandler, gui_adap_oid)

    def stop_the_debugger(self, idb_adap_oid):
        self.rpchandler.unregister(idb_adap_oid)
        return

    def get_the_calltip(self, name):
        return self.calltip.fetch_tip(name)

    def get_the_completion_list(self, what, mode):
        return self.autocomplete.fetch_completions(what, mode)

    def stackviewer(self, flist_oid=None):
        if self.usr_exc_info:
            typ, val, tb = self.usr_exc_info
        else:
            return
        flist = None
        if flist_oid is not None:
            flist = self.rpchandler.get_remote_proxy(flist_oid)
        while tb and tb.tb_frame.f_globals[b'__name__'] in (b'rpc', b'run'):
            tb = tb.tb_next

        sys.last_type = typ
        sys.last_value = val
        item = StackViewer.StackTreeItem(flist, tb)
        return RemoteObjectBrowser.remote_object_tree_item(item)


capture_warnings(False)
