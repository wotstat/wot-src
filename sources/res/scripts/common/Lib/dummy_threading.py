from sys import modules as sys_modules
import dummy_thread
holding_thread = False
holding_threading = False
holding__threading_local = False
try:
    if b'thread' in sys_modules:
        held_thread = sys_modules[b'thread']
        holding_thread = True
    sys_modules[b'thread'] = sys_modules[b'dummy_thread']
    if b'threading' in sys_modules:
        held_threading = sys_modules[b'threading']
        holding_threading = True
        del sys_modules[b'threading']
    if b'_threading_local' in sys_modules:
        held__threading_local = sys_modules[b'_threading_local']
        holding__threading_local = True
        del sys_modules[b'_threading_local']
    import threading
    sys_modules[b'_dummy_threading'] = sys_modules[b'threading']
    del sys_modules[b'threading']
    sys_modules[b'_dummy__threading_local'] = sys_modules[b'_threading_local']
    del sys_modules[b'_threading_local']
    from _dummy_threading import *
    from _dummy_threading import __all__
finally:
    if holding_threading:
        sys_modules[b'threading'] = held_threading
        del held_threading
    del holding_threading
    if holding__threading_local:
        sys_modules[b'_threading_local'] = held__threading_local
        del held__threading_local
    del holding__threading_local
    if holding_thread:
        sys_modules[b'thread'] = held_thread
        del held_thread
    else:
        del sys_modules[b'thread']
    del holding_thread
    del dummy_thread
    del sys_modules
