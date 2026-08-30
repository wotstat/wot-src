from warnings import warnpy3k
warnpy3k(b'the sunaudio module has been removed in Python 3.0; use the sunau module instead', stacklevel=2)
del warnpy3k
MAGIC = b'.snd'

class error(Exception):
    pass


def get_long_be(s):
    return ord(s[0]) << 24 | ord(s[1]) << 16 | ord(s[2]) << 8 | ord(s[3])


def gethdr(fp):
    if fp.read(4) != MAGIC:
        raise error, b'gethdr: bad magic word'
    hdr_size = get_long_be(fp.read(4))
    data_size = get_long_be(fp.read(4))
    encoding = get_long_be(fp.read(4))
    sample_rate = get_long_be(fp.read(4))
    channels = get_long_be(fp.read(4))
    excess = hdr_size - 24
    if excess < 0:
        raise error, b'gethdr: bad hdr_size'
    if excess > 0:
        info = fp.read(excess)
    else:
        info = b''
    return (
     data_size, encoding, sample_rate, channels, info)


def printhdr(file):
    hdr = gethdr(open(file, b'r'))
    data_size, encoding, sample_rate, channels, info = hdr
    while info[-1:] == b'\x00':
        info = info[:-1]

    print b'File name:  ', file
    print b'Data size:  ', data_size
    print b'Encoding:   ', encoding
    print b'Sample rate:', sample_rate
    print b'Channels:   ', channels
    print b'Info:       ', repr(info)
    return
