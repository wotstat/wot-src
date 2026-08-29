from warnings import warnpy3k
warnpy3k(b'the user module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
import os
home = os.curdir
if b'HOME' in os.environ:
    home = os.environ[b'HOME']
elif os.name == b'posix':
    home = os.path.expanduser(b'~/')
elif os.name == b'nt':
    if b'HOMEPATH' in os.environ:
        if b'HOMEDRIVE' in os.environ:
            home = os.environ[b'HOMEDRIVE'] + os.environ[b'HOMEPATH']
        else:
            home = os.environ[b'HOMEPATH']
pythonrc = os.path.join(home, b'.pythonrc.py')
try:
    f = open(pythonrc)
except IOError:
    pass
else:
    f.close()
    execfile(pythonrc)
