from warnings import warnpy3k
warnpy3k(b'the toaiff module has been removed in Python 3.0', stacklevel=2)
del warnpy3k
import os, tempfile, pipes, sndhdr
__all__ = [
 b'error', b'toaiff']
table = {}
t = pipes.Template()
t.append(b'sox -t au - -t aiff -r 8000 -', b'--')
table[b'au'] = t
t = pipes.Template()
t.append(b'sox -t hcom - -t aiff -r 22050 -', b'--')
table[b'hcom'] = t
t = pipes.Template()
t.append(b'sox -t voc - -t aiff -r 11025 -', b'--')
table[b'voc'] = t
t = pipes.Template()
t.append(b'sox -t wav - -t aiff -', b'--')
table[b'wav'] = t
t = pipes.Template()
t.append(b'sox -t 8svx - -t aiff -r 16000 -', b'--')
table[b'8svx'] = t
t = pipes.Template()
t.append(b'sox -t sndt - -t aiff -r 16000 -', b'--')
table[b'sndt'] = t
t = pipes.Template()
t.append(b'sox -t sndr - -t aiff -r 16000 -', b'--')
table[b'sndr'] = t
uncompress = pipes.Template()
uncompress.append(b'uncompress', b'--')

class error(Exception):
    pass


def toaiff(filename):
    temps = []
    ret = None
    try:
        ret = _toaiff(filename, temps)
    finally:
        for temp in temps[:]:
            if temp != ret:
                try:
                    os.unlink(temp)
                except os.error:
                    pass

                temps.remove(temp)

    return ret


def _toaiff(filename, temps):
    if filename[-2:] == b'.Z':
        fd, fname = tempfile.mkstemp()
        os.close(fd)
        temps.append(fname)
        sts = uncompress.copy(filename, fname)
        if sts:
            raise error, filename + b': uncompress failed'
    else:
        fname = filename
    try:
        ftype = sndhdr.whathdr(fname)
        if ftype:
            ftype = ftype[0]
    except IOError as msg:
        if type(msg) == type(()) and len(msg) == 2 and type(msg[0]) == type(0) and type(msg[1]) == type(b''):
            msg = msg[1]
        if type(msg) != type(b''):
            msg = repr(msg)
        raise error, filename + b': ' + msg

    if ftype == b'aiff':
        return fname
    else:
        if ftype is None or ftype not in table:
            raise error, b'%s: unsupported audio file type %r' % (filename, ftype)
        fd, temp = tempfile.mkstemp()
        os.close(fd)
        temps.append(temp)
        sts = table[ftype].copy(fname, temp)
        if sts:
            raise error, filename + b': conversion to aiff failed'
        return temp
