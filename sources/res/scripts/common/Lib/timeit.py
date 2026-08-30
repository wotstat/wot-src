import gc, sys, time
try:
    import itertools
except ImportError:
    itertools = None

__all__ = [b'Timer']
dummy_src_name = b'<timeit-src>'
default_number = 1000000
default_repeat = 3
if sys.platform == b'win32':
    default_timer = time.clock
else:
    default_timer = time.time
template = b'\ndef inner(_it, _timer%(init)s):\n    %(setup)s\n    _t0 = _timer()\n    for _i in _it:\n        %(stmt)s\n    _t1 = _timer()\n    return _t1 - _t0\n'

def reindent(src, indent):
    return src.replace(b'\n', b'\n' + b' ' * indent)


def _template_func(setup, func):

    def inner(_it, _timer, _func=func):
        setup()
        _t0 = _timer()
        for _i in _it:
            _func()

        _t1 = _timer()
        return _t1 - _t0

    return inner


class Timer:

    def __init__(self, stmt=b'pass', setup=b'pass', timer=default_timer):
        self.timer = timer
        ns = {}
        if isinstance(stmt, basestring):
            if isinstance(setup, basestring):
                compile(setup, dummy_src_name, b'exec')
                compile(setup + b'\n' + stmt, dummy_src_name, b'exec')
            else:
                compile(stmt, dummy_src_name, b'exec')
            stmt = reindent(stmt, 8)
            if isinstance(setup, basestring):
                setup = reindent(setup, 4)
                src = template % {b'stmt': stmt, b'setup': setup, b'init': b''}
            elif hasattr(setup, b'__call__'):
                src = template % {b'stmt': stmt, b'setup': b'_setup()', b'init': b', _setup=_setup'}
                ns[b'_setup'] = setup
            else:
                raise ValueError(b'setup is neither a string nor callable')
            self.src = src
            code = compile(src, dummy_src_name, b'exec')
            exec code in globals(), ns
            self.inner = ns[b'inner']
        elif hasattr(stmt, b'__call__'):
            self.src = None
            if isinstance(setup, basestring):
                _setup = setup

                def setup():
                    exec _setup in globals(), ns
                    return

            elif not hasattr(setup, b'__call__'):
                raise ValueError(b'setup is neither a string nor callable')
            self.inner = _template_func(setup, stmt)
        else:
            raise ValueError(b'stmt is neither a string nor callable')
        return

    def print_exc(self, file=None):
        import linecache, traceback
        if self.src is not None:
            linecache.cache[dummy_src_name] = (
             len(self.src),
             None,
             self.src.split(b'\n'),
             dummy_src_name)
        traceback.print_exc(file=file)
        return

    def timeit(self, number=default_number):
        if itertools:
            it = itertools.repeat(None, number)
        else:
            it = [
             None] * number
        gcold = gc.isenabled()
        gc.disable()
        try:
            timing = self.inner(it, self.timer)
        finally:
            if gcold:
                gc.enable()

        return timing

    def repeat(self, repeat=default_repeat, number=default_number):
        r = []
        for i in range(repeat):
            t = self.timeit(number)
            r.append(t)

        return r


def timeit(stmt=b'pass', setup=b'pass', timer=default_timer, number=default_number):
    return Timer(stmt, setup, timer).timeit(number)


def repeat(stmt=b'pass', setup=b'pass', timer=default_timer, repeat=default_repeat, number=default_number):
    return Timer(stmt, setup, timer).repeat(repeat, number)


def main(args=None, _wrap_timer=None):
    if args is None:
        args = sys.argv[1:]
    import getopt
    try:
        opts, args = getopt.getopt(args, b'n:s:r:tcvh', [
         4, 5, 6, 
         7, 8, 9, 10])
    except getopt.error as err:
        print err
        print b'use -h/--help for command line help'
        return 2

    timer = default_timer
    stmt = (b'\n').join(args) or b'pass'
    number = 0
    setup = []
    repeat = default_repeat
    verbose = 0
    precision = 3
    for o, a in opts:
        if o in (b'-n', b'--number'):
            number = int(a)
        if o in (b'-s', b'--setup'):
            setup.append(a)
        if o in (b'-r', b'--repeat'):
            repeat = int(a)
            if repeat <= 0:
                repeat = 1
        if o in (b'-t', b'--time'):
            timer = time.time
        if o in (b'-c', b'--clock'):
            timer = time.clock
        if o in (b'-v', b'--verbose'):
            if verbose:
                precision += 1
            verbose += 1
        if o in (b'-h', b'--help'):
            print __doc__,
            return 0

    setup = (b'\n').join(setup) or b'pass'
    import os
    sys.path.insert(0, os.curdir)
    if _wrap_timer is not None:
        timer = _wrap_timer(timer)
    t = Timer(stmt, setup, timer)
    if number == 0:
        for i in range(1, 10):
            number = 10 ** i
            try:
                x = t.timeit(number)
            except:
                t.print_exc()
                return 1

            if verbose:
                print b'%d loops -> %.*g secs' % (number, precision, x)
            if x >= 0.2:
                break

    try:
        r = t.repeat(repeat, number)
    except:
        t.print_exc()
        return 1

    best = min(r)
    if verbose:
        print b'raw times:', (b' ').join([b'%.*g' % (precision, x) for x in r])
    print b'%d loops,' % number,
    usec = best * 1000000.0 / number
    if usec < 1000:
        print b'best of %d: %.*g usec per loop' % (repeat, precision, usec)
    else:
        msec = usec / 1000
        if msec < 1000:
            print b'best of %d: %.*g msec per loop' % (repeat, precision, msec)
        else:
            sec = msec / 1000
            print b'best of %d: %.*g sec per loop' % (repeat, precision, sec)
    return


if __name__ == b'__main__':
    sys.exit(main())
