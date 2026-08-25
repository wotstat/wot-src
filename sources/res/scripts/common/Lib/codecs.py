import __builtin__, sys
try:
    from _codecs import *
except ImportError as why:
    raise SystemError(b'Failed to load the builtin codecs: %s' % why)

__all__ = [4, 5, 6, 7, 8, 9, 
 10, 11, 12, 13, 14, 
 15, 16, 17, 18, 
 19, 
 20, 21, 
 22, 23, 24, 25, 
 26, 27, 
 28, 29, 
 30, 31, 32, 
 33, 
 34, 35, 
 36, 37, 38, 39, 
 40, 41, 42, 
 43, 44, 
 45, 46]
BOM_UTF8 = b'\xef\xbb\xbf'
BOM_LE = BOM_UTF16_LE = b'\xff\xfe'
BOM_BE = BOM_UTF16_BE = b'\xfe\xff'
BOM_UTF32_LE = b'\xff\xfe\x00\x00'
BOM_UTF32_BE = b'\x00\x00\xfe\xff'
if sys.byteorder == b'little':
    BOM = BOM_UTF16 = BOM_UTF16_LE
    BOM_UTF32 = BOM_UTF32_LE
else:
    BOM = BOM_UTF16 = BOM_UTF16_BE
    BOM_UTF32 = BOM_UTF32_BE
BOM32_LE = BOM_UTF16_LE
BOM32_BE = BOM_UTF16_BE
BOM64_LE = BOM_UTF32_LE
BOM64_BE = BOM_UTF32_BE

class CodecInfo(tuple):
    _is_text_encoding = True

    def __new__(cls, encode, decode, streamreader=None, streamwriter=None, incrementalencoder=None, incrementaldecoder=None, name=None, _is_text_encoding=None):
        self = tuple.__new__(cls, (encode, decode, streamreader, streamwriter))
        self.name = name
        self.encode = encode
        self.decode = decode
        self.incrementalencoder = incrementalencoder
        self.incrementaldecoder = incrementaldecoder
        self.streamwriter = streamwriter
        self.streamreader = streamreader
        if _is_text_encoding is not None:
            self._is_text_encoding = _is_text_encoding
        return self

    def __repr__(self):
        return b'<%s.%s object for encoding %s at 0x%x>' % (self.__class__.__module__, self.__class__.__name__, self.name, id(self))


class Codec:

    def encode(self, input, errors=b'strict'):
        raise NotImplementedError
        return

    def decode(self, input, errors=b'strict'):
        raise NotImplementedError
        return


class IncrementalEncoder(object):

    def __init__(self, errors=b'strict'):
        self.errors = errors
        self.buffer = b''
        return

    def encode(self, input, final=False):
        raise NotImplementedError
        return

    def reset(self):
        return

    def getstate(self):
        return 0

    def setstate(self, state):
        return


class BufferedIncrementalEncoder(IncrementalEncoder):

    def __init__(self, errors=b'strict'):
        IncrementalEncoder.__init__(self, errors)
        self.buffer = b''
        return

    def _buffer_encode(self, input, errors, final):
        raise NotImplementedError
        return

    def encode(self, input, final=False):
        data = self.buffer + input
        result, consumed = self._buffer_encode(data, self.errors, final)
        self.buffer = data[consumed:]
        return result

    def reset(self):
        IncrementalEncoder.reset(self)
        self.buffer = b''
        return

    def getstate(self):
        return self.buffer or 0

    def setstate(self, state):
        self.buffer = state or b''
        return


class IncrementalDecoder(object):

    def __init__(self, errors=b'strict'):
        self.errors = errors
        return

    def decode(self, input, final=False):
        raise NotImplementedError
        return

    def reset(self):
        return

    def getstate(self):
        return (b'', 0)

    def setstate(self, state):
        return


class BufferedIncrementalDecoder(IncrementalDecoder):

    def __init__(self, errors=b'strict'):
        IncrementalDecoder.__init__(self, errors)
        self.buffer = b''
        return

    def _buffer_decode(self, input, errors, final):
        raise NotImplementedError
        return

    def decode(self, input, final=False):
        data = self.buffer + input
        result, consumed = self._buffer_decode(data, self.errors, final)
        self.buffer = data[consumed:]
        return result

    def reset(self):
        IncrementalDecoder.reset(self)
        self.buffer = b''
        return

    def getstate(self):
        return (
         self.buffer, 0)

    def setstate(self, state):
        self.buffer = state[0]
        return


class StreamWriter(Codec):

    def __init__(self, stream, errors=b'strict'):
        self.stream = stream
        self.errors = errors
        return

    def write(self, object):
        data, consumed = self.encode(object, self.errors)
        self.stream.write(data)
        return

    def writelines(self, list):
        self.write((b'').join(list))
        return

    def reset(self):
        return

    def seek(self, offset, whence=0):
        self.stream.seek(offset, whence)
        if whence == 0 and offset == 0:
            self.reset()
        return

    def __getattr__(self, name, getattr=getattr):
        return getattr(self.stream, name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.stream.close()
        return


class StreamReader(Codec):

    def __init__(self, stream, errors=b'strict'):
        self.stream = stream
        self.errors = errors
        self.bytebuffer = b''
        self.charbuffer = b''
        self.linebuffer = None
        return

    def decode(self, input, errors=b'strict'):
        raise NotImplementedError
        return

    def read(self, size=-1, chars=-1, firstline=False):
        if self.linebuffer:
            self.charbuffer = (b'').join(self.linebuffer)
            self.linebuffer = None
        if chars < 0:
            chars = size
        while True:
            if chars >= 0:
                if len(self.charbuffer) >= chars:
                    break
            if size < 0:
                newdata = self.stream.read()
            else:
                newdata = self.stream.read(size)
            data = self.bytebuffer + newdata
            try:
                newchars, decodedbytes = self.decode(data, self.errors)
            except UnicodeDecodeError as exc:
                if firstline:
                    newchars, decodedbytes = self.decode(data[:exc.start], self.errors)
                    lines = newchars.splitlines(True)
                    if len(lines) <= 1:
                        raise
                else:
                    raise

            self.bytebuffer = data[decodedbytes:]
            self.charbuffer += newchars
            if not newdata:
                break

        if chars < 0:
            result = self.charbuffer
            self.charbuffer = b''
        else:
            result = self.charbuffer[:chars]
            self.charbuffer = self.charbuffer[chars:]
        return result

    def readline(self, size=None, keepends=True):
        if self.linebuffer:
            line = self.linebuffer[0]
            del self.linebuffer[0]
            if len(self.linebuffer) == 1:
                self.charbuffer = self.linebuffer[0]
                self.linebuffer = None
            if not keepends:
                line = line.splitlines(False)[0]
            return line
        readsize = size or 72
        line = b''
        while True:
            data = self.read(readsize, firstline=True)
            if data:
                if data.endswith(b'\r'):
                    data += self.read(size=1, chars=1)
            line += data
            lines = line.splitlines(True)
            if lines:
                if len(lines) > 1:
                    line = lines[0]
                    del lines[0]
                    if len(lines) > 1:
                        lines[-1] += self.charbuffer
                        self.linebuffer = lines
                        self.charbuffer = None
                    else:
                        self.charbuffer = lines[0] + self.charbuffer
                    if not keepends:
                        line = line.splitlines(False)[0]
                    break
                line0withend = lines[0]
                line0withoutend = lines[0].splitlines(False)[0]
                if line0withend != line0withoutend:
                    self.charbuffer = (b'').join(lines[1:]) + self.charbuffer
                    if keepends:
                        line = line0withend
                    else:
                        line = line0withoutend
                    break
            if not data or size is not None:
                if line and not keepends:
                    line = line.splitlines(False)[0]
                break
            if readsize < 8000:
                readsize *= 2

        return line

    def readlines(self, sizehint=None, keepends=True):
        data = self.read()
        return data.splitlines(keepends)

    def reset(self):
        self.bytebuffer = b''
        self.charbuffer = u''
        self.linebuffer = None
        return

    def seek(self, offset, whence=0):
        self.stream.seek(offset, whence)
        self.reset()
        return

    def next(self):
        line = self.readline()
        if line:
            return line
        raise StopIteration
        return

    def __iter__(self):
        return self

    def __getattr__(self, name, getattr=getattr):
        return getattr(self.stream, name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.stream.close()
        return


class StreamReaderWriter:
    encoding = b'unknown'

    def __init__(self, stream, Reader, Writer, errors=b'strict'):
        self.stream = stream
        self.reader = Reader(stream, errors)
        self.writer = Writer(stream, errors)
        self.errors = errors
        return

    def read(self, size=-1):
        return self.reader.read(size)

    def readline(self, size=None):
        return self.reader.readline(size)

    def readlines(self, sizehint=None):
        return self.reader.readlines(sizehint)

    def next(self):
        return self.reader.next()

    def __iter__(self):
        return self

    def write(self, data):
        return self.writer.write(data)

    def writelines(self, list):
        return self.writer.writelines(list)

    def reset(self):
        self.reader.reset()
        self.writer.reset()
        return

    def seek(self, offset, whence=0):
        self.stream.seek(offset, whence)
        self.reader.reset()
        if whence == 0 and offset == 0:
            self.writer.reset()
        return

    def __getattr__(self, name, getattr=getattr):
        return getattr(self.stream, name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.stream.close()
        return


class StreamRecoder:
    data_encoding = b'unknown'
    file_encoding = b'unknown'

    def __init__(self, stream, encode, decode, Reader, Writer, errors=b'strict'):
        self.stream = stream
        self.encode = encode
        self.decode = decode
        self.reader = Reader(stream, errors)
        self.writer = Writer(stream, errors)
        self.errors = errors
        return

    def read(self, size=-1):
        data = self.reader.read(size)
        data, bytesencoded = self.encode(data, self.errors)
        return data

    def readline(self, size=None):
        if size is None:
            data = self.reader.readline()
        else:
            data = self.reader.readline(size)
        data, bytesencoded = self.encode(data, self.errors)
        return data

    def readlines(self, sizehint=None):
        data = self.reader.read()
        data, bytesencoded = self.encode(data, self.errors)
        return data.splitlines(1)

    def next(self):
        data = self.reader.next()
        data, bytesencoded = self.encode(data, self.errors)
        return data

    def __iter__(self):
        return self

    def write(self, data):
        data, bytesdecoded = self.decode(data, self.errors)
        return self.writer.write(data)

    def writelines(self, list):
        data = (b'').join(list)
        data, bytesdecoded = self.decode(data, self.errors)
        return self.writer.write(data)

    def reset(self):
        self.reader.reset()
        self.writer.reset()
        return

    def __getattr__(self, name, getattr=getattr):
        return getattr(self.stream, name)

    def __enter__(self):
        return self

    def __exit__(self, type, value, tb):
        self.stream.close()
        return


def open(filename, mode=b'rb', encoding=None, errors=b'strict', buffering=1):
    if encoding is not None:
        if b'U' in mode:
            mode = mode.strip().replace(b'U', b'')
            if mode[:1] not in set(b'rwa'):
                mode = b'r' + mode
        if b'b' not in mode:
            mode = mode + b'b'
    file = __builtin__.open(filename, mode, buffering)
    if encoding is None:
        return file
    else:
        info = lookup(encoding)
        srw = StreamReaderWriter(file, info.streamreader, info.streamwriter, errors)
        srw.encoding = encoding
        return srw


def EncodedFile(file, data_encoding, file_encoding=None, errors=b'strict'):
    if file_encoding is None:
        file_encoding = data_encoding
    data_info = lookup(data_encoding)
    file_info = lookup(file_encoding)
    sr = StreamRecoder(file, data_info.encode, data_info.decode, file_info.streamreader, file_info.streamwriter, errors)
    sr.data_encoding = data_encoding
    sr.file_encoding = file_encoding
    return sr


def getencoder(encoding):
    return lookup(encoding).encode


def getdecoder(encoding):
    return lookup(encoding).decode


def getincrementalencoder(encoding):
    encoder = lookup(encoding).incrementalencoder
    if encoder is None:
        raise LookupError(encoding)
    return encoder


def getincrementaldecoder(encoding):
    decoder = lookup(encoding).incrementaldecoder
    if decoder is None:
        raise LookupError(encoding)
    return decoder


def getreader(encoding):
    return lookup(encoding).streamreader


def getwriter(encoding):
    return lookup(encoding).streamwriter


def iterencode(iterator, encoding, errors=b'strict', **kwargs):
    encoder = getincrementalencoder(encoding)(errors, **kwargs)
    for input in iterator:
        output = encoder.encode(input)
        if output:
            yield output

    output = encoder.encode(b'', True)
    if output:
        yield output
    return


def iterdecode(iterator, encoding, errors=b'strict', **kwargs):
    decoder = getincrementaldecoder(encoding)(errors, **kwargs)
    for input in iterator:
        output = decoder.decode(input)
        if output:
            yield output

    output = decoder.decode(b'', True)
    if output:
        yield output
    return


def make_identity_dict(rng):
    res = {}
    for i in rng:
        res[i] = i

    return res


def make_encoding_map(decoding_map):
    m = {}
    for k, v in decoding_map.items():
        if v not in m:
            m[v] = k
        else:
            m[v] = None

    return m


try:
    strict_errors = lookup_error(b'strict')
    ignore_errors = lookup_error(b'ignore')
    replace_errors = lookup_error(b'replace')
    xmlcharrefreplace_errors = lookup_error(b'xmlcharrefreplace')
    backslashreplace_errors = lookup_error(b'backslashreplace')
except LookupError:
    strict_errors = None
    ignore_errors = None
    replace_errors = None
    xmlcharrefreplace_errors = None
    backslashreplace_errors = None

_false = 0
if _false:
    import encodings
if __name__ == b'__main__':
    sys.stdout = EncodedFile(sys.stdout, b'latin-1', b'utf-8')
    sys.stdin = EncodedFile(sys.stdin, b'utf-8', b'latin-1')
