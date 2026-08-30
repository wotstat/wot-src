import struct, __builtin__
__all__ = [
 b'Error', b'open', b'openfp']

class Error(Exception):
    pass


_AIFC_version = 2726318400L

def _read_long(file):
    try:
        return struct.unpack(b'>l', file.read(4))[0]
    except struct.error:
        raise EOFError

    return


def _read_ulong(file):
    try:
        return struct.unpack(b'>L', file.read(4))[0]
    except struct.error:
        raise EOFError

    return


def _read_short(file):
    try:
        return struct.unpack(b'>h', file.read(2))[0]
    except struct.error:
        raise EOFError

    return


def _read_ushort(file):
    try:
        return struct.unpack(b'>H', file.read(2))[0]
    except struct.error:
        raise EOFError

    return


def _read_string(file):
    length = ord(file.read(1))
    if length == 0:
        data = b''
    else:
        data = file.read(length)
    if length & 1 == 0:
        dummy = file.read(1)
    return data


_HUGE_VAL = 1.79769313486231e+308

def _read_float(f):
    expon = _read_short(f)
    sign = 1
    if expon < 0:
        sign = -1
        expon = expon + 32768
    himant = _read_ulong(f)
    lomant = _read_ulong(f)
    if expon == himant == lomant == 0:
        f = 0.0
    elif expon == 32767:
        f = _HUGE_VAL
    else:
        expon = expon - 16383
        f = (himant * 4294967296L + lomant) * pow(2.0, expon - 63)
    return sign * f


def _write_short(f, x):
    f.write(struct.pack(b'>h', x))
    return


def _write_ushort(f, x):
    f.write(struct.pack(b'>H', x))
    return


def _write_long(f, x):
    f.write(struct.pack(b'>l', x))
    return


def _write_ulong(f, x):
    f.write(struct.pack(b'>L', x))
    return


def _write_string(f, s):
    if len(s) > 255:
        raise ValueError(b'string exceeds maximum pstring length')
    f.write(struct.pack(b'B', len(s)))
    f.write(s)
    if len(s) & 1 == 0:
        f.write(chr(0))
    return


def _write_float(f, x):
    import math
    if x < 0:
        sign = 32768
        x = x * -1
    else:
        sign = 0
    if x == 0:
        expon = 0
        himant = 0
        lomant = 0
    else:
        fmant, expon = math.frexp(x)
        if expon > 16384 or fmant >= 1 or fmant != fmant:
            expon = sign | 32767
            himant = 0
            lomant = 0
        else:
            expon = expon + 16382
            if expon < 0:
                fmant = math.ldexp(fmant, expon)
                expon = 0
            expon = expon | sign
            fmant = math.ldexp(fmant, 32)
            fsmant = math.floor(fmant)
            himant = long(fsmant)
            fmant = math.ldexp(fmant - fsmant, 32)
            fsmant = math.floor(fmant)
            lomant = long(fsmant)
    _write_ushort(f, expon)
    _write_ulong(f, himant)
    _write_ulong(f, lomant)
    return


from chunk import Chunk

class Aifc_read():
    _file = None

    def initfp(self, file):
        self._version = 0
        self._decomp = None
        self._convert = None
        self._markers = []
        self._soundpos = 0
        self._file = file
        chunk = Chunk(file)
        if chunk.getname() != b'FORM':
            raise Error, b'file does not start with FORM id'
        formdata = chunk.read(4)
        if formdata == b'AIFF':
            self._aifc = 0
        elif formdata == b'AIFC':
            self._aifc = 1
        else:
            raise Error, b'not an AIFF or AIFF-C file'
        self._comm_chunk_read = 0
        self._ssnd_chunk = None
        while 1:
            self._ssnd_seek_needed = 1
            try:
                chunk = Chunk(self._file)
            except EOFError:
                break

            chunkname = chunk.getname()
            if chunkname == b'COMM':
                self._read_comm_chunk(chunk)
                self._comm_chunk_read = 1
            elif chunkname == b'SSND':
                self._ssnd_chunk = chunk
                dummy = chunk.read(8)
                self._ssnd_seek_needed = 0
            elif chunkname == b'FVER':
                self._version = _read_ulong(chunk)
            elif chunkname == b'MARK':
                self._readmark(chunk)
            chunk.skip()

        if not self._comm_chunk_read or not self._ssnd_chunk:
            raise Error, b'COMM chunk and/or SSND chunk missing'
        if self._aifc and self._decomp:
            import cl
            params = [
             cl.ORIGINAL_FORMAT, 0,
             cl.BITS_PER_COMPONENT, self._sampwidth * 8,
             cl.FRAME_RATE, self._framerate]
            if self._nchannels == 1:
                params[1] = cl.MONO
            elif self._nchannels == 2:
                params[1] = cl.STEREO_INTERLEAVED
            else:
                raise Error, b'cannot compress more than 2 channels'
            self._decomp.SetParams(params)
        return

    def __init__(self, f):
        if isinstance(f, basestring):
            f = __builtin__.open(f, b'rb')
            try:
                self.initfp(f)
            except:
                f.close()
                raise

        else:
            self.initfp(f)
        return

    def getfp(self):
        return self._file

    def rewind(self):
        self._ssnd_seek_needed = 1
        self._soundpos = 0
        return

    def close(self):
        decomp = self._decomp
        try:
            if decomp:
                self._decomp = None
                decomp.CloseDecompressor()
        finally:
            self._file.close()

        return

    def tell(self):
        return self._soundpos

    def getnchannels(self):
        return self._nchannels

    def getnframes(self):
        return self._nframes

    def getsampwidth(self):
        return self._sampwidth

    def getframerate(self):
        return self._framerate

    def getcomptype(self):
        return self._comptype

    def getcompname(self):
        return self._compname

    def getparams(self):
        return (
         self.getnchannels(), self.getsampwidth(),
         self.getframerate(), self.getnframes(),
         self.getcomptype(), self.getcompname())

    def getmarkers(self):
        if len(self._markers) == 0:
            return None
        else:
            return self._markers

    def getmark(self, id):
        for marker in self._markers:
            if id == marker[0]:
                return marker

        raise Error, b'marker %r does not exist' % (id,)
        return

    def setpos(self, pos):
        if pos < 0 or pos > self._nframes:
            raise Error, b'position not in range'
        self._soundpos = pos
        self._ssnd_seek_needed = 1
        return

    def readframes(self, nframes):
        if self._ssnd_seek_needed:
            self._ssnd_chunk.seek(0)
            dummy = self._ssnd_chunk.read(8)
            pos = self._soundpos * self._framesize
            if pos:
                self._ssnd_chunk.seek(pos + 8)
            self._ssnd_seek_needed = 0
        if nframes == 0:
            return b''
        data = self._ssnd_chunk.read(nframes * self._framesize)
        if self._convert and data:
            data = self._convert(data)
        self._soundpos = self._soundpos + len(data) // (self._nchannels * self._sampwidth)
        return data

    def _decomp_data(self, data):
        import cl
        dummy = self._decomp.SetParam(cl.FRAME_BUFFER_SIZE, len(data) * 2)
        return self._decomp.Decompress(len(data) // self._nchannels, data)

    def _ulaw2lin(self, data):
        import audioop
        return audioop.ulaw2lin(data, 2)

    def _adpcm2lin(self, data):
        import audioop
        if not hasattr(self, b'_adpcmstate'):
            self._adpcmstate = None
        data, self._adpcmstate = audioop.adpcm2lin(data, 2, self._adpcmstate)
        return data

    def _read_comm_chunk(self, chunk):
        self._nchannels = _read_short(chunk)
        self._nframes = _read_long(chunk)
        self._sampwidth = (_read_short(chunk) + 7) // 8
        self._framerate = int(_read_float(chunk))
        self._framesize = self._nchannels * self._sampwidth
        if self._aifc:
            kludge = 0
            if chunk.chunksize == 18:
                kludge = 1
                print b'Warning: bad COMM chunk size'
                chunk.chunksize = 23
            self._comptype = chunk.read(4)
            if kludge:
                length = ord(chunk.file.read(1))
                if length & 1 == 0:
                    length = length + 1
                chunk.chunksize = chunk.chunksize + length
                chunk.file.seek(-1, 1)
            self._compname = _read_string(chunk)
            if self._comptype != b'NONE':
                if self._comptype == b'G722':
                    try:
                        import audioop
                    except ImportError:
                        pass
                    else:
                        self._convert = self._adpcm2lin
                        self._sampwidth = 2
                        return

                try:
                    import cl
                except ImportError:
                    if self._comptype in (b'ULAW', b'ulaw'):
                        try:
                            import audioop
                            self._convert = self._ulaw2lin
                            self._sampwidth = 2
                            return
                        except ImportError:
                            pass

                    raise Error, b'cannot read compressed AIFF-C files'

                if self._comptype in (b'ULAW', b'ulaw'):
                    scheme = cl.G711_ULAW
                elif self._comptype in (b'ALAW', b'alaw'):
                    scheme = cl.G711_ALAW
                else:
                    raise Error, b'unsupported compression type'
                self._decomp = cl.OpenDecompressor(scheme)
                self._convert = self._decomp_data
                self._sampwidth = 2
        else:
            self._comptype = b'NONE'
            self._compname = b'not compressed'
        return

    def _readmark(self, chunk):
        nmarkers = _read_short(chunk)
        try:
            for i in range(nmarkers):
                id = _read_short(chunk)
                pos = _read_long(chunk)
                name = _read_string(chunk)
                if pos or name:
                    self._markers.append((id, pos, name))

        except EOFError:
            print b'Warning: MARK chunk contains only',
            print len(self._markers),
            if len(self._markers) == 1:
                print b'marker',
            else:
                print b'markers',
            print b'instead of', nmarkers

        return


class Aifc_write():
    _file = None

    def __init__(self, f):
        if isinstance(f, basestring):
            filename = f
            f = __builtin__.open(f, b'wb')
        else:
            filename = b'???'
        self.initfp(f)
        if filename[-5:] == b'.aiff':
            self._aifc = 0
        else:
            self._aifc = 1
        return

    def initfp(self, file):
        self._file = file
        self._version = _AIFC_version
        self._comptype = b'NONE'
        self._compname = b'not compressed'
        self._comp = None
        self._convert = None
        self._nchannels = 0
        self._sampwidth = 0
        self._framerate = 0
        self._nframes = 0
        self._nframeswritten = 0
        self._datawritten = 0
        self._datalength = 0
        self._markers = []
        self._marklength = 0
        self._aifc = 1
        return

    def __del__(self):
        if self._file:
            self.close()
        return

    def aiff(self):
        if self._nframeswritten:
            raise Error, b'cannot change parameters after starting to write'
        self._aifc = 0
        return

    def aifc(self):
        if self._nframeswritten:
            raise Error, b'cannot change parameters after starting to write'
        self._aifc = 1
        return

    def setnchannels(self, nchannels):
        if self._nframeswritten:
            raise Error, b'cannot change parameters after starting to write'
        if nchannels < 1:
            raise Error, b'bad # of channels'
        self._nchannels = nchannels
        return

    def getnchannels(self):
        if not self._nchannels:
            raise Error, b'number of channels not set'
        return self._nchannels

    def setsampwidth(self, sampwidth):
        if self._nframeswritten:
            raise Error, b'cannot change parameters after starting to write'
        if sampwidth < 1 or sampwidth > 4:
            raise Error, b'bad sample width'
        self._sampwidth = sampwidth
        return

    def getsampwidth(self):
        if not self._sampwidth:
            raise Error, b'sample width not set'
        return self._sampwidth

    def setframerate(self, framerate):
        if self._nframeswritten:
            raise Error, b'cannot change parameters after starting to write'
        if framerate <= 0:
            raise Error, b'bad frame rate'
        self._framerate = framerate
        return

    def getframerate(self):
        if not self._framerate:
            raise Error, b'frame rate not set'
        return self._framerate

    def setnframes(self, nframes):
        if self._nframeswritten:
            raise Error, b'cannot change parameters after starting to write'
        self._nframes = nframes
        return

    def getnframes(self):
        return self._nframeswritten

    def setcomptype(self, comptype, compname):
        if self._nframeswritten:
            raise Error, b'cannot change parameters after starting to write'
        if comptype not in (b'NONE', b'ULAW', b'ulaw', b'ALAW', b'alaw', b'G722'):
            raise Error, b'unsupported compression type'
        self._comptype = comptype
        self._compname = compname
        return

    def getcomptype(self):
        return self._comptype

    def getcompname(self):
        return self._compname

    def setparams(self, info):
        nchannels, sampwidth, framerate, nframes, comptype, compname = info
        if self._nframeswritten:
            raise Error, b'cannot change parameters after starting to write'
        if comptype not in (b'NONE', b'ULAW', b'ulaw', b'ALAW', b'alaw', b'G722'):
            raise Error, b'unsupported compression type'
        self.setnchannels(nchannels)
        self.setsampwidth(sampwidth)
        self.setframerate(framerate)
        self.setnframes(nframes)
        self.setcomptype(comptype, compname)
        return

    def getparams(self):
        if not self._nchannels or not self._sampwidth or not self._framerate:
            raise Error, b'not all parameters set'
        return (
         self._nchannels, self._sampwidth, self._framerate,
         self._nframes, self._comptype, self._compname)

    def setmark(self, id, pos, name):
        if id <= 0:
            raise Error, b'marker ID must be > 0'
        if pos < 0:
            raise Error, b'marker position must be >= 0'
        if type(name) != type(b''):
            raise Error, b'marker name must be a string'
        for i in range(len(self._markers)):
            if id == self._markers[i][0]:
                self._markers[i] = (
                 id, pos, name)
                return

        self._markers.append((id, pos, name))
        return

    def getmark(self, id):
        for marker in self._markers:
            if id == marker[0]:
                return marker

        raise Error, b'marker %r does not exist' % (id,)
        return

    def getmarkers(self):
        if len(self._markers) == 0:
            return None
        else:
            return self._markers

    def tell(self):
        return self._nframeswritten

    def writeframesraw(self, data):
        self._ensure_header_written(len(data))
        nframes = len(data) // (self._sampwidth * self._nchannels)
        if self._convert:
            data = self._convert(data)
        self._file.write(data)
        self._nframeswritten = self._nframeswritten + nframes
        self._datawritten = self._datawritten + len(data)
        return

    def writeframes(self, data):
        self.writeframesraw(data)
        if self._nframeswritten != self._nframes or self._datalength != self._datawritten:
            self._patchheader()
        return

    def close(self):
        if self._file is None:
            return
        else:
            try:
                self._ensure_header_written(0)
                if self._datawritten & 1:
                    self._file.write(chr(0))
                    self._datawritten = self._datawritten + 1
                self._writemarkers()
                if self._nframeswritten != self._nframes or self._datalength != self._datawritten or self._marklength:
                    self._patchheader()
                if self._comp:
                    self._comp.CloseCompressor()
                    self._comp = None
            finally:
                self._convert = None
                f = self._file
                self._file = None
                f.close()

            return

    def _comp_data(self, data):
        import cl
        dummy = self._comp.SetParam(cl.FRAME_BUFFER_SIZE, len(data))
        dummy = self._comp.SetParam(cl.COMPRESSED_BUFFER_SIZE, len(data))
        return self._comp.Compress(self._nframes, data)

    def _lin2ulaw(self, data):
        import audioop
        return audioop.lin2ulaw(data, 2)

    def _lin2adpcm(self, data):
        import audioop
        if not hasattr(self, b'_adpcmstate'):
            self._adpcmstate = None
        data, self._adpcmstate = audioop.lin2adpcm(data, 2, self._adpcmstate)
        return data

    def _ensure_header_written(self, datasize):
        if not self._nframeswritten:
            if self._comptype in (b'ULAW', b'ulaw', b'ALAW', b'alaw'):
                if not self._sampwidth:
                    self._sampwidth = 2
                if self._sampwidth != 2:
                    raise Error, b'sample width must be 2 when compressing with ULAW or ALAW'
            if self._comptype == b'G722':
                if not self._sampwidth:
                    self._sampwidth = 2
                if self._sampwidth != 2:
                    raise Error, b'sample width must be 2 when compressing with G7.22 (ADPCM)'
            if not self._nchannels:
                raise Error, b'# channels not specified'
            if not self._sampwidth:
                raise Error, b'sample width not specified'
            if not self._framerate:
                raise Error, b'sampling rate not specified'
            self._write_header(datasize)
        return

    def _init_compression(self):
        if self._comptype == b'G722':
            self._convert = self._lin2adpcm
            return
        try:
            import cl
        except ImportError:
            if self._comptype in (b'ULAW', b'ulaw'):
                try:
                    import audioop
                    self._convert = self._lin2ulaw
                    return
                except ImportError:
                    pass

            raise Error, b'cannot write compressed AIFF-C files'

        if self._comptype in (b'ULAW', b'ulaw'):
            scheme = cl.G711_ULAW
        elif self._comptype in (b'ALAW', b'alaw'):
            scheme = cl.G711_ALAW
        else:
            raise Error, b'unsupported compression type'
        self._comp = cl.OpenCompressor(scheme)
        params = [cl.ORIGINAL_FORMAT, 0,
         cl.BITS_PER_COMPONENT, self._sampwidth * 8,
         cl.FRAME_RATE, self._framerate,
         cl.FRAME_BUFFER_SIZE, 100,
         cl.COMPRESSED_BUFFER_SIZE, 100]
        if self._nchannels == 1:
            params[1] = cl.MONO
        elif self._nchannels == 2:
            params[1] = cl.STEREO_INTERLEAVED
        else:
            raise Error, b'cannot compress more than 2 channels'
        self._comp.SetParams(params)
        dummy = self._comp.Compress(0, b'')
        self._convert = self._comp_data
        return

    def _write_header(self, initlength):
        if self._aifc and self._comptype != b'NONE':
            self._init_compression()
        self._file.write(b'FORM')
        if not self._nframes:
            self._nframes = initlength // (self._nchannels * self._sampwidth)
        self._datalength = self._nframes * self._nchannels * self._sampwidth
        if self._datalength & 1:
            self._datalength = self._datalength + 1
        if self._aifc:
            if self._comptype in (b'ULAW', b'ulaw', b'ALAW', b'alaw'):
                self._datalength = self._datalength // 2
                if self._datalength & 1:
                    self._datalength = self._datalength + 1
            elif self._comptype == b'G722':
                self._datalength = (self._datalength + 3) // 4
                if self._datalength & 1:
                    self._datalength = self._datalength + 1
        try:
            self._form_length_pos = self._file.tell()
        except (AttributeError, IOError):
            self._form_length_pos = None

        commlength = self._write_form_length(self._datalength)
        if self._aifc:
            self._file.write(b'AIFC')
            self._file.write(b'FVER')
            _write_ulong(self._file, 4)
            _write_ulong(self._file, self._version)
        else:
            self._file.write(b'AIFF')
        self._file.write(b'COMM')
        _write_ulong(self._file, commlength)
        _write_short(self._file, self._nchannels)
        if self._form_length_pos is not None:
            self._nframes_pos = self._file.tell()
        _write_ulong(self._file, self._nframes)
        if self._comptype in (b'ULAW', b'ulaw', b'ALAW', b'alaw', b'G722'):
            _write_short(self._file, 8)
        else:
            _write_short(self._file, self._sampwidth * 8)
        _write_float(self._file, self._framerate)
        if self._aifc:
            self._file.write(self._comptype)
            _write_string(self._file, self._compname)
        self._file.write(b'SSND')
        if self._form_length_pos is not None:
            self._ssnd_length_pos = self._file.tell()
        _write_ulong(self._file, self._datalength + 8)
        _write_ulong(self._file, 0)
        _write_ulong(self._file, 0)
        return

    def _write_form_length(self, datalength):
        if self._aifc:
            commlength = 23 + len(self._compname)
            if commlength & 1:
                commlength = commlength + 1
            verslength = 12
        else:
            commlength = 18
            verslength = 0
        _write_ulong(self._file, 4 + verslength + self._marklength + 8 + commlength + 16 + datalength)
        return commlength

    def _patchheader(self):
        curpos = self._file.tell()
        if self._datawritten & 1:
            datalength = self._datawritten + 1
            self._file.write(chr(0))
        else:
            datalength = self._datawritten
        if datalength == self._datalength and self._nframes == self._nframeswritten and self._marklength == 0:
            self._file.seek(curpos, 0)
            return
        self._file.seek(self._form_length_pos, 0)
        dummy = self._write_form_length(datalength)
        self._file.seek(self._nframes_pos, 0)
        _write_ulong(self._file, self._nframeswritten)
        self._file.seek(self._ssnd_length_pos, 0)
        _write_ulong(self._file, datalength + 8)
        self._file.seek(curpos, 0)
        self._nframes = self._nframeswritten
        self._datalength = datalength
        return

    def _writemarkers(self):
        if len(self._markers) == 0:
            return
        self._file.write(b'MARK')
        length = 2
        for marker in self._markers:
            id, pos, name = marker
            length = length + len(name) + 1 + 6
            if len(name) & 1 == 0:
                length = length + 1

        _write_ulong(self._file, length)
        self._marklength = length + 8
        _write_short(self._file, len(self._markers))
        for marker in self._markers:
            id, pos, name = marker
            _write_short(self._file, id)
            _write_ulong(self._file, pos)
            _write_string(self._file, name)

        return


def open(f, mode=None):
    if mode is None:
        if hasattr(f, b'mode'):
            mode = f.mode
        else:
            mode = b'rb'
    if mode in (b'r', b'rb'):
        return Aifc_read(f)
    else:
        if mode in (b'w', b'wb'):
            return Aifc_write(f)
        raise Error, b"mode must be 'r', 'rb', 'w', or 'wb'"
        return


openfp = open
if __name__ == b'__main__':
    import sys
    if not sys.argv[1:]:
        sys.argv.append(b'/usr/demos/data/audio/bach.aiff')
    fn = sys.argv[1]
    f = open(fn, b'r')
    try:
        print b'Reading', fn
        print b'nchannels =', f.getnchannels()
        print b'nframes   =', f.getnframes()
        print b'sampwidth =', f.getsampwidth()
        print b'framerate =', f.getframerate()
        print b'comptype  =', f.getcomptype()
        print b'compname  =', f.getcompname()
        if sys.argv[2:]:
            gn = sys.argv[2]
            print b'Writing', gn
            g = open(gn, b'w')
            try:
                g.setparams(f.getparams())
                while 1:
                    data = f.readframes(1024)
                    if not data:
                        break
                    g.writeframes(data)

            finally:
                g.close()

            print b'Done.'
    finally:
        f.close()
