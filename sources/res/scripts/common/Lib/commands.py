from warnings import warnpy3k
warnpy3k(b'the commands module has been removed in Python 3.0; use the subprocess module instead', stacklevel=2)
del warnpy3k
__all__ = [
 b'getstatusoutput', b'getoutput', b'getstatus']

def getstatus(file):
    import warnings
    warnings.warn(b'commands.getstatus() is deprecated', DeprecationWarning, 2)
    return getoutput(b'ls -ld' + mkarg(file))


def getoutput(cmd):
    return getstatusoutput(cmd)[1]


def getstatusoutput(cmd):
    import os
    pipe = os.popen(b'{ ' + cmd + b'; } 2>&1', b'r')
    text = pipe.read()
    sts = pipe.close()
    if sts is None:
        sts = 0
    if text[-1:] == b'\n':
        text = text[:-1]
    return (
     sts, text)


def mk2arg(head, x):
    import os
    return mkarg(os.path.join(head, x))


def mkarg(x):
    if b"'" not in x:
        return b" '" + x + b"'"
    s = b' "'
    for c in x:
        if c in b'\\$"`':
            s = s + b'\\'
        s = s + c

    s = s + b'"'
    return s
