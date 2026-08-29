__all__ = [
 b'register']
import sys
_exithandlers = []

def _run_exitfuncs():
    exc_info = None
    while _exithandlers:
        func, targs, kargs = _exithandlers.pop()
        try:
            func(*targs, **kargs)
        except SystemExit:
            exc_info = sys.exc_info()
        except:
            import traceback
            print >> sys.stderr, b'Error in atexit._run_exitfuncs:'
            traceback.print_exc()
            exc_info = sys.exc_info()

    if exc_info is not None:
        raise exc_info[0], exc_info[1], exc_info[2]
    return


def register(func, *targs, **kargs):
    _exithandlers.append((func, targs, kargs))
    return func


if hasattr(sys, b'exitfunc'):
    register(sys.exitfunc)
sys.exitfunc = _run_exitfuncs
if __name__ == b'__main__':

    def x1():
        print b'running x1'
        return


    def x2(n):
        print b'running x2(%r)' % (n,)
        return


    def x3(n, kwd=None):
        print b'running x3(%r, kwd=%r)' % (n, kwd)
        return


    register(x1)
    register(x2, 12)
    register(x3, 5, b'bar')
    register(x3, b'no kwd args')
