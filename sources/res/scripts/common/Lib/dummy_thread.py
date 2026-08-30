__all__ = [
 0, 1, 2, 3, 4, 
 5, 6]
import traceback as _traceback

class error(Exception):

    def __init__(self, *args):
        self.args = args
        return


def start_new_thread(function, args, kwargs={}):
    global _interrupt
    global _main
    if type(args) != type(tuple()):
        raise TypeError(b'2nd arg must be a tuple')
    if type(kwargs) != type(dict()):
        raise TypeError(b'3rd arg must be a dict')
    _main = False
    try:
        function(*args, **kwargs)
    except SystemExit:
        pass
    except:
        _traceback.print_exc()

    _main = True
    if _interrupt:
        _interrupt = False
        raise KeyboardInterrupt
    return


def exit():
    raise SystemExit
    return


def get_ident():
    return -1


def allocate_lock():
    return LockType()


def stack_size(size=None):
    if size is not None:
        raise error(b'setting thread stack size not supported')
    return 0


class LockType(object):

    def __init__(self):
        self.locked_status = False
        return

    def acquire(self, waitflag=None):
        if waitflag is None or waitflag:
            self.locked_status = True
            return True
        else:
            if not self.locked_status:
                self.locked_status = True
                return True
            else:
                return False

            return

    __enter__ = acquire

    def __exit__(self, typ, val, tb):
        self.release()
        return

    def release(self):
        if not self.locked_status:
            raise error
        self.locked_status = False
        return True

    def locked(self):
        return self.locked_status


_interrupt = False
_main = True

def interrupt_main():
    global _interrupt
    if _main:
        raise KeyboardInterrupt
    else:
        _interrupt = True
    return
