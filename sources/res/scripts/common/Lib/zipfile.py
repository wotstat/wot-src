import struct, os, time, sys, shutil, binascii, cStringIO, stat, io, re, string
try:
    import zlib
    crc32 = zlib.crc32
except ImportError:
    zlib = None
    crc32 = binascii.crc32

__all__ = [2, 3, 4, 5, 6, 
 7, 8, 9, 10]

class BadZipfile(Exception):
    pass


class LargeZipFile(Exception):
    pass


error = BadZipfile
ZIP64_LIMIT = (1 << 31) - 1
ZIP_FILECOUNT_LIMIT = (1 << 16) - 1
ZIP_MAX_COMMENT = (1 << 16) - 1
ZIP_STORED = 0
ZIP_DEFLATED = 8
structEndArchive = b'<4s4H2LH'
stringEndArchive = b'PK\x05\x06'
sizeEndCentDir = struct.calcsize(structEndArchive)
_ECD_SIGNATURE = 0
_ECD_DISK_NUMBER = 1
_ECD_DISK_START = 2
_ECD_ENTRIES_THIS_DISK = 3
_ECD_ENTRIES_TOTAL = 4
_ECD_SIZE = 5
_ECD_OFFSET = 6
_ECD_COMMENT_SIZE = 7
_ECD_COMMENT = 8
_ECD_LOCATION = 9
structCentralDir = b'<4s4B4HL2L5H2L'
stringCentralDir = b'PK\x01\x02'
sizeCentralDir = struct.calcsize(structCentralDir)
_CD_SIGNATURE = 0
_CD_CREATE_VERSION = 1
_CD_CREATE_SYSTEM = 2
_CD_EXTRACT_VERSION = 3
_CD_EXTRACT_SYSTEM = 4
_CD_FLAG_BITS = 5
_CD_COMPRESS_TYPE = 6
_CD_TIME = 7
_CD_DATE = 8
_CD_CRC = 9
_CD_COMPRESSED_SIZE = 10
_CD_UNCOMPRESSED_SIZE = 11
_CD_FILENAME_LENGTH = 12
_CD_EXTRA_FIELD_LENGTH = 13
_CD_COMMENT_LENGTH = 14
_CD_DISK_NUMBER_START = 15
_CD_INTERNAL_FILE_ATTRIBUTES = 16
_CD_EXTERNAL_FILE_ATTRIBUTES = 17
_CD_LOCAL_HEADER_OFFSET = 18
structFileHeader = b'<4s2B4HL2L2H'
stringFileHeader = b'PK\x03\x04'
sizeFileHeader = struct.calcsize(structFileHeader)
_FH_SIGNATURE = 0
_FH_EXTRACT_VERSION = 1
_FH_EXTRACT_SYSTEM = 2
_FH_GENERAL_PURPOSE_FLAG_BITS = 3
_FH_COMPRESSION_METHOD = 4
_FH_LAST_MOD_TIME = 5
_FH_LAST_MOD_DATE = 6
_FH_CRC = 7
_FH_COMPRESSED_SIZE = 8
_FH_UNCOMPRESSED_SIZE = 9
_FH_FILENAME_LENGTH = 10
_FH_EXTRA_FIELD_LENGTH = 11
structEndArchive64Locator = b'<4sLQL'
stringEndArchive64Locator = b'PK\x06\x07'
sizeEndCentDir64Locator = struct.calcsize(structEndArchive64Locator)
structEndArchive64 = b'<4sQ2H2L4Q'
stringEndArchive64 = b'PK\x06\x06'
sizeEndCentDir64 = struct.calcsize(structEndArchive64)
_CD64_SIGNATURE = 0
_CD64_DIRECTORY_RECSIZE = 1
_CD64_CREATE_VERSION = 2
_CD64_EXTRACT_VERSION = 3
_CD64_DISK_NUMBER = 4
_CD64_DISK_NUMBER_START = 5
_CD64_NUMBER_ENTRIES_THIS_DISK = 6
_CD64_NUMBER_ENTRIES_TOTAL = 7
_CD64_DIRECTORY_SIZE = 8
_CD64_OFFSET_START_CENTDIR = 9
_DD_SIGNATURE = 134695760
_EXTRA_FIELD_STRUCT = struct.Struct(b'<HH')

def _strip_extra(extra, xids):
    unpack = _EXTRA_FIELD_STRUCT.unpack
    modified = False
    buffer = []
    start = i = 0
    while i + 4 <= len(extra):
        xid, xlen = unpack(extra[i:i + 4])
        j = i + 4 + xlen
        if xid in xids:
            if i != start:
                buffer.append(extra[start:i])
            start = j
            modified = True
        i = j

    if not modified:
        return extra
    return (b'').join(buffer)


def _check_zipfile(fp):
    try:
        if _EndRecData(fp):
            return True
    except IOError:
        pass

    return False


def is_zipfile(filename):
    result = False
    try:
        if hasattr(filename, b'read'):
            result = _check_zipfile(fp=filename)
        else:
            with open(filename, b'rb') as fp:
                result = _check_zipfile(fp)
    except IOError:
        pass

    return result


def _EndRecData64(fpin, offset, endrec):
    try:
        fpin.seek(offset - sizeEndCentDir64Locator, 2)
    except IOError:
        return endrec

    data = fpin.read(sizeEndCentDir64Locator)
    if len(data) != sizeEndCentDir64Locator:
        return endrec
    sig, diskno, reloff, disks = struct.unpack(structEndArchive64Locator, data)
    if sig != stringEndArchive64Locator:
        return endrec
    if diskno != 0 or disks != 1:
        raise BadZipfile(b'zipfiles that span multiple disks are not supported')
    fpin.seek(offset - sizeEndCentDir64Locator - sizeEndCentDir64, 2)
    data = fpin.read(sizeEndCentDir64)
    if len(data) != sizeEndCentDir64:
        return endrec
    sig, sz, create_version, read_version, disk_num, disk_dir, dircount, dircount2, dirsize, diroffset = struct.unpack(structEndArchive64, data)
    if sig != stringEndArchive64:
        return endrec
    endrec[_ECD_SIGNATURE] = sig
    endrec[_ECD_DISK_NUMBER] = disk_num
    endrec[_ECD_DISK_START] = disk_dir
    endrec[_ECD_ENTRIES_THIS_DISK] = dircount
    endrec[_ECD_ENTRIES_TOTAL] = dircount2
    endrec[_ECD_SIZE] = dirsize
    endrec[_ECD_OFFSET] = diroffset
    return endrec


def _EndRecData(fpin):
    fpin.seek(0, 2)
    filesize = fpin.tell()
    try:
        fpin.seek(-sizeEndCentDir, 2)
    except IOError:
        return

    data = fpin.read()
    if len(data) == sizeEndCentDir and data[0:4] == stringEndArchive and data[-2:] == b'\x00\x00':
        endrec = struct.unpack(structEndArchive, data)
        endrec = list(endrec)
        endrec.append(b'')
        endrec.append(filesize - sizeEndCentDir)
        return _EndRecData64(fpin, -sizeEndCentDir, endrec)
    else:
        maxCommentStart = max(filesize - 65536 - sizeEndCentDir, 0)
        fpin.seek(maxCommentStart, 0)
        data = fpin.read()
        start = data.rfind(stringEndArchive)
        if start >= 0:
            recData = data[start:start + sizeEndCentDir]
            if len(recData) != sizeEndCentDir:
                return
            endrec = list(struct.unpack(structEndArchive, recData))
            commentSize = endrec[_ECD_COMMENT_SIZE]
            comment = data[start + sizeEndCentDir:start + sizeEndCentDir + commentSize]
            endrec.append(comment)
            endrec.append(maxCommentStart + start)
            return _EndRecData64(fpin, maxCommentStart + start - filesize, endrec)
        return


class ZipInfo(object):
    __slots__ = (b'orig_filename', b'filename', b'date_time', b'compress_type', b'comment', b'extra', b'create_system', b'create_version', b'extract_version', b'reserved', b'flag_bits', b'volume', b'internal_attr', b'external_attr', b'header_offset', b'CRC', b'compress_size', b'file_size', b'_raw_time')

    def __init__(self, filename=b'NoName', date_time=(1980, 1, 1, 0, 0, 0)):
        self.orig_filename = filename
        null_byte = filename.find(chr(0))
        if null_byte >= 0:
            filename = filename[0:null_byte]
        if os.sep != b'/' and os.sep in filename:
            filename = filename.replace(os.sep, b'/')
        self.filename = filename
        self.date_time = date_time
        if date_time[0] < 1980:
            raise ValueError(b'ZIP does not support timestamps before 1980')
        self.compress_type = ZIP_STORED
        self.comment = b''
        self.extra = b''
        if sys.platform == b'win32':
            self.create_system = 0
        else:
            self.create_system = 3
        self.create_version = 20
        self.extract_version = 20
        self.reserved = 0
        self.flag_bits = 0
        self.volume = 0
        self.internal_attr = 0
        self.external_attr = 0
        return

    def FileHeader(self, zip64=None):
        dt = self.date_time
        dosdate = dt[0] - 1980 << 9 | dt[1] << 5 | dt[2]
        dostime = dt[3] << 11 | dt[4] << 5 | dt[5] // 2
        if self.flag_bits & 8:
            CRC = compress_size = file_size = 0
        else:
            CRC = self.CRC
            compress_size = self.compress_size
            file_size = self.file_size
        extra = self.extra
        if zip64 is None:
            zip64 = file_size > ZIP64_LIMIT or compress_size > ZIP64_LIMIT
        if zip64:
            fmt = b'<HHQQ'
            extra = extra + struct.pack(fmt, 1, struct.calcsize(fmt) - 4, file_size, compress_size)
        if file_size > ZIP64_LIMIT or compress_size > ZIP64_LIMIT:
            if not zip64:
                raise LargeZipFile(b'Filesize would require ZIP64 extensions')
            file_size = 4294967295L
            compress_size = 4294967295L
            self.extract_version = max(45, self.extract_version)
            self.create_version = max(45, self.extract_version)
        filename, flag_bits = self._encodeFilenameFlags()
        header = struct.pack(structFileHeader, stringFileHeader, self.extract_version, self.reserved, flag_bits, self.compress_type, dostime, dosdate, CRC, compress_size, file_size, len(filename), len(extra))
        return header + filename + extra

    def _encodeFilenameFlags(self):
        if isinstance(self.filename, unicode):
            try:
                return (
                 self.filename.encode(b'ascii'), self.flag_bits)
            except UnicodeEncodeError:
                return (
                 self.filename.encode(b'utf-8'), self.flag_bits | 2048)

        else:
            return (
             self.filename, self.flag_bits)
        return

    def _decodeFilename(self):
        if self.flag_bits & 2048:
            return self.filename.decode(b'utf-8')
        else:
            return self.filename

        return

    def _decodeExtra(self):
        extra = self.extra
        unpack = struct.unpack
        while len(extra) >= 4:
            tp, ln = unpack(b'<HH', extra[:4])
            if tp == 1:
                if ln >= 24:
                    counts = unpack(b'<QQQ', extra[4:28])
                elif ln == 16:
                    counts = unpack(b'<QQ', extra[4:20])
                elif ln == 8:
                    counts = unpack(b'<Q', extra[4:12])
                elif ln == 0:
                    counts = ()
                else:
                    raise RuntimeError, b'Corrupt extra field %s' % (ln,)
                idx = 0
                if self.file_size in (18446744073709551615L, 4294967295L):
                    self.file_size = counts[idx]
                    idx += 1
                if self.compress_size == 4294967295L:
                    self.compress_size = counts[idx]
                    idx += 1
                if self.header_offset == 4294967295L:
                    old = self.header_offset
                    self.header_offset = counts[idx]
                    idx += 1
            extra = extra[ln + 4:]

        return


class _ZipDecrypter():

    def _GenerateCRCTable():
        poly = 3988292384L
        table = [0] * 256
        for i in range(256):
            crc = i
            for j in range(8):
                if crc & 1:
                    crc = crc >> 1 & 2147483647 ^ poly
                else:
                    crc = crc >> 1 & 2147483647

            table[i] = crc

        return table

    crctable = _GenerateCRCTable()

    def _crc32(self, ch, crc):
        return crc >> 8 & 16777215 ^ self.crctable[(crc ^ ord(ch)) & 255]

    def __init__(self, pwd):
        self.key0 = 305419896
        self.key1 = 591751049
        self.key2 = 878082192
        for p in pwd:
            self._UpdateKeys(p)

        return

    def _UpdateKeys(self, c):
        self.key0 = self._crc32(c, self.key0)
        self.key1 = self.key1 + (self.key0 & 255) & 4294967295L
        self.key1 = self.key1 * 134775813 + 1 & 4294967295L
        self.key2 = self._crc32(chr(self.key1 >> 24 & 255), self.key2)
        return

    def __call__(self, c):
        c = ord(c)
        k = self.key2 | 2
        c = c ^ k * (k ^ 1) >> 8 & 255
        c = chr(c)
        self._UpdateKeys(c)
        return c


compressor_names = {0: b'store', 
   1: b'shrink', 
   2: b'reduce', 
   3: b'reduce', 
   4: b'reduce', 
   5: b'reduce', 
   6: b'implode', 
   7: b'tokenize', 
   8: b'deflate', 
   9: b'deflate64', 
   10: b'implode', 
   12: b'bzip2', 
   14: b'lzma', 
   18: b'terse', 
   19: b'lz77', 
   97: b'wavpack', 
   98: b'ppmd'}

class ZipExtFile(io.BufferedIOBase):
    MAX_N = 1 << 30
    MIN_READ_SIZE = 4096
    PATTERN = re.compile(b'^(?P<chunk>[^\\r\\n]+)|(?P<newline>\\n|\\r\\n?)')

    def __init__(self, fileobj, mode, zipinfo, decrypter=None, close_fileobj=False):
        self._fileobj = fileobj
        self._decrypter = decrypter
        self._close_fileobj = close_fileobj
        self._compress_type = zipinfo.compress_type
        self._compress_size = zipinfo.compress_size
        self._compress_left = zipinfo.compress_size
        if self._compress_type == ZIP_DEFLATED:
            self._decompressor = zlib.decompressobj(-15)
        elif self._compress_type != ZIP_STORED:
            descr = compressor_names.get(self._compress_type)
            if descr:
                raise NotImplementedError(b'compression type %d (%s)' % (self._compress_type, descr))
            else:
                raise NotImplementedError(b'compression type %d' % (self._compress_type,))
        self._unconsumed = b''
        self._readbuffer = b''
        self._offset = 0
        self._universal = b'U' in mode
        self.newlines = None
        if self._decrypter is not None:
            self._compress_left -= 12
        self.mode = mode
        self.name = zipinfo.filename
        if hasattr(zipinfo, b'CRC'):
            self._expected_crc = zipinfo.CRC
            self._running_crc = crc32(b'') & 4294967295L
        else:
            self._expected_crc = None
        return

    def readline(self, limit=-1):
        if not self._universal and limit < 0:
            i = self._readbuffer.find(b'\n', self._offset) + 1
            if i > 0:
                line = self._readbuffer[self._offset:i]
                self._offset = i
                return line
        if not self._universal:
            return io.BufferedIOBase.readline(self, limit)
        else:
            line = b''
            while limit < 0 or len(line) < limit:
                readahead = self.peek(2)
                if readahead == b'':
                    return line
                match = self.PATTERN.search(readahead)
                newline = match.group(b'newline')
                if newline is not None:
                    if self.newlines is None:
                        self.newlines = []
                    if newline not in self.newlines:
                        self.newlines.append(newline)
                    self._offset += len(newline)
                    return line + b'\n'
                chunk = match.group(b'chunk')
                if limit >= 0:
                    chunk = chunk[:limit - len(line)]
                self._offset += len(chunk)
                line += chunk

            return line

    def peek(self, n=1):
        if n > len(self._readbuffer) - self._offset:
            chunk = self.read(n)
            if len(chunk) > self._offset:
                self._readbuffer = chunk + self._readbuffer[self._offset:]
                self._offset = 0
            else:
                self._offset -= len(chunk)
        return self._readbuffer[self._offset:self._offset + 512]

    def readable(self):
        return True

    def read(self, n=-1):
        buf = b''
        if n is None:
            n = -1
        while True:
            if n < 0:
                data = self.read1(n)
            elif n > len(buf):
                data = self.read1(n - len(buf))
            else:
                return buf
            if len(data) == 0:
                return buf
            buf += data

        return

    def _update_crc(self, newdata, eof):
        if self._expected_crc is None:
            return
        else:
            self._running_crc = crc32(newdata, self._running_crc) & 4294967295L
            if eof and self._running_crc != self._expected_crc:
                raise BadZipfile(b'Bad CRC-32 for file %r' % self.name)
            return

    def read1(self, n):
        if n < 0 or n is None:
            n = self.MAX_N
        len_readbuffer = len(self._readbuffer) - self._offset
        if self._compress_left > 0 and n > len_readbuffer + len(self._unconsumed):
            nbytes = n - len_readbuffer - len(self._unconsumed)
            nbytes = max(nbytes, self.MIN_READ_SIZE)
            nbytes = min(nbytes, self._compress_left)
            data = self._fileobj.read(nbytes)
            self._compress_left -= len(data)
            if data and self._decrypter is not None:
                data = (b'').join(map(self._decrypter, data))
            if self._compress_type == ZIP_STORED:
                self._update_crc(data, eof=self._compress_left == 0)
                self._readbuffer = self._readbuffer[self._offset:] + data
                self._offset = 0
            else:
                self._unconsumed += data
        if len(self._unconsumed) > 0 and n > len_readbuffer and self._compress_type == ZIP_DEFLATED:
            data = self._decompressor.decompress(self._unconsumed, max(n - len_readbuffer, self.MIN_READ_SIZE))
            self._unconsumed = self._decompressor.unconsumed_tail
            eof = len(self._unconsumed) == 0 and self._compress_left == 0
            if eof:
                data += self._decompressor.flush()
            self._update_crc(data, eof=eof)
            self._readbuffer = self._readbuffer[self._offset:] + data
            self._offset = 0
        data = self._readbuffer[self._offset:self._offset + n]
        self._offset += len(data)
        return data

    def close(self):
        try:
            if self._close_fileobj:
                self._fileobj.close()
        finally:
            super(ZipExtFile, self).close()

        return


class ZipFile(object):
    fp = None

    def __init__(self, file, mode=b'r', compression=ZIP_STORED, allowZip64=False):
        if mode not in (b'r', b'w', b'a'):
            raise RuntimeError(b'ZipFile() requires mode "r", "w", or "a"')
        if compression == ZIP_STORED:
            pass
        else:
            if compression == ZIP_DEFLATED:
                if not zlib:
                    raise RuntimeError, b'Compression requires the (missing) zlib module'
            else:
                raise RuntimeError, b'That compression method is not supported'
            self._allowZip64 = allowZip64
            self._didModify = False
            self.debug = 0
            self.NameToInfo = {}
            self.filelist = []
            self.compression = compression
            self.mode = key = mode.replace(b'b', b'')[0]
            self.pwd = None
            self._comment = b''
            if isinstance(file, basestring):
                self._filePassed = 0
                self.filename = file
                modeDict = {b'r': b'rb', b'w': b'wb', b'a': b'r+b'}
                try:
                    self.fp = open(file, modeDict[mode])
                except IOError:
                    if mode == b'a':
                        mode = key = b'w'
                        self.fp = open(file, modeDict[mode])
                    else:
                        raise

            else:
                self._filePassed = 1
                self.fp = file
                self.filename = getattr(file, b'name', None)
            try:
                if key == b'r':
                    self._RealGetContents()
                elif key == b'w':
                    self._didModify = True
                elif key == b'a':
                    try:
                        self._RealGetContents()
                        self.fp.seek(self.start_dir, 0)
                    except BadZipfile:
                        self.fp.seek(0, 2)
                        self._didModify = True

                else:
                    raise RuntimeError(b'Mode must be "r", "w" or "a"')
            except:
                fp = self.fp
                self.fp = None
                if not self._filePassed:
                    fp.close()
                raise

        return

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()
        return

    def _RealGetContents(self):
        fp = self.fp
        try:
            endrec = _EndRecData(fp)
        except IOError:
            raise BadZipfile(b'File is not a zip file')

        if not endrec:
            raise BadZipfile, b'File is not a zip file'
        if self.debug > 1:
            print endrec
        size_cd = endrec[_ECD_SIZE]
        offset_cd = endrec[_ECD_OFFSET]
        self._comment = endrec[_ECD_COMMENT]
        concat = endrec[_ECD_LOCATION] - size_cd - offset_cd
        if endrec[_ECD_SIGNATURE] == stringEndArchive64:
            concat -= sizeEndCentDir64 + sizeEndCentDir64Locator
        if self.debug > 2:
            inferred = concat + offset_cd
            print b'given, inferred, offset', offset_cd, inferred, concat
        self.start_dir = offset_cd + concat
        fp.seek(self.start_dir, 0)
        data = fp.read(size_cd)
        fp = cStringIO.StringIO(data)
        total = 0
        while total < size_cd:
            centdir = fp.read(sizeCentralDir)
            if len(centdir) != sizeCentralDir:
                raise BadZipfile(b'Truncated central directory')
            centdir = struct.unpack(structCentralDir, centdir)
            if centdir[_CD_SIGNATURE] != stringCentralDir:
                raise BadZipfile(b'Bad magic number for central directory')
            if self.debug > 2:
                print centdir
            filename = fp.read(centdir[_CD_FILENAME_LENGTH])
            x = ZipInfo(filename)
            x.extra = fp.read(centdir[_CD_EXTRA_FIELD_LENGTH])
            x.comment = fp.read(centdir[_CD_COMMENT_LENGTH])
            x.header_offset = centdir[_CD_LOCAL_HEADER_OFFSET]
            x.create_version, x.create_system, x.extract_version, x.reserved, x.flag_bits, x.compress_type, t, d, x.CRC, x.compress_size, x.file_size = centdir[1:12]
            x.volume, x.internal_attr, x.external_attr = centdir[15:18]
            x._raw_time = t
            x.date_time = ((d >> 9) + 1980, d >> 5 & 15, d & 31,
             t >> 11, t >> 5 & 63, (t & 31) * 2)
            x._decodeExtra()
            x.header_offset = x.header_offset + concat
            x.filename = x._decodeFilename()
            self.filelist.append(x)
            self.NameToInfo[x.filename] = x
            total = total + sizeCentralDir + centdir[_CD_FILENAME_LENGTH] + centdir[_CD_EXTRA_FIELD_LENGTH] + centdir[_CD_COMMENT_LENGTH]
            if self.debug > 2:
                print b'total', total

        return

    def namelist(self):
        l = []
        for data in self.filelist:
            l.append(data.filename)

        return l

    def infolist(self):
        return self.filelist

    def printdir(self):
        print b'%-46s %19s %12s' % (b'File Name', b'Modified    ', b'Size')
        for zinfo in self.filelist:
            date = b'%d-%02d-%02d %02d:%02d:%02d' % zinfo.date_time[:6]
            print b'%-46s %s %12d' % (zinfo.filename, date, zinfo.file_size)

        return

    def testzip(self):
        chunk_size = 1048576
        for zinfo in self.filelist:
            try:
                with self.open(zinfo.filename, b'r') as f:
                    while f.read(chunk_size):
                        pass

            except BadZipfile:
                return zinfo.filename

        return

    def getinfo(self, name):
        info = self.NameToInfo.get(name)
        if info is None:
            raise KeyError(b'There is no item named %r in the archive' % name)
        return info

    def setpassword(self, pwd):
        self.pwd = pwd
        return

    @property
    def comment(self):
        return self._comment

    @comment.setter
    def comment(self, comment):
        if len(comment) > ZIP_MAX_COMMENT:
            import warnings
            warnings.warn(b'Archive comment is too long; truncating to %d bytes' % ZIP_MAX_COMMENT, stacklevel=2)
            comment = comment[:ZIP_MAX_COMMENT]
        self._comment = comment
        self._didModify = True
        return

    def read(self, name, pwd=None):
        return self.open(name, b'r', pwd).read()

    def open(self, name, mode=b'r', pwd=None):
        if mode not in (b'r', b'U', b'rU'):
            raise RuntimeError, b'open() requires mode "r", "U", or "rU"'
        if not self.fp:
            raise RuntimeError, b'Attempt to read ZIP archive that was already closed'
        if self._filePassed:
            zef_file = self.fp
            should_close = False
        else:
            zef_file = open(self.filename, b'rb')
            should_close = True
        try:
            if isinstance(name, ZipInfo):
                zinfo = name
            else:
                zinfo = self.getinfo(name)
            zef_file.seek(zinfo.header_offset, 0)
            fheader = zef_file.read(sizeFileHeader)
            if len(fheader) != sizeFileHeader:
                raise BadZipfile(b'Truncated file header')
            fheader = struct.unpack(structFileHeader, fheader)
            if fheader[_FH_SIGNATURE] != stringFileHeader:
                raise BadZipfile(b'Bad magic number for file header')
            fname = zef_file.read(fheader[_FH_FILENAME_LENGTH])
            if fheader[_FH_EXTRA_FIELD_LENGTH]:
                zef_file.read(fheader[_FH_EXTRA_FIELD_LENGTH])
            if fname != zinfo.orig_filename:
                raise BadZipfile, b'File name in directory "%s" and header "%s" differ.' % (
                 zinfo.orig_filename, fname)
            is_encrypted = zinfo.flag_bits & 1
            zd = None
            if is_encrypted:
                if not pwd:
                    pwd = self.pwd
                if not pwd:
                    raise RuntimeError, b'File %s is encrypted, password required for extraction' % name
                zd = _ZipDecrypter(pwd)
                bytes = zef_file.read(12)
                h = map(zd, bytes[0:12])
                if zinfo.flag_bits & 8:
                    check_byte = zinfo._raw_time >> 8 & 255
                else:
                    check_byte = zinfo.CRC >> 24 & 255
                if ord(h[11]) != check_byte:
                    raise RuntimeError(b'Bad password for file', name)
            return ZipExtFile(zef_file, mode, zinfo, zd, close_fileobj=should_close)
        except:
            if should_close:
                zef_file.close()
            raise

        return

    def extract(self, member, path=None, pwd=None):
        if not isinstance(member, ZipInfo):
            member = self.getinfo(member)
        if path is None:
            path = os.getcwd()
        return self._extract_member(member, path, pwd)

    def extractall(self, path=None, members=None, pwd=None):
        if members is None:
            members = self.namelist()
        for zipinfo in members:
            self.extract(zipinfo, path, pwd)

        return

    def _extract_member(self, member, targetpath, pwd):
        arcname = member.filename.replace(b'/', os.path.sep)
        if os.path.altsep:
            arcname = arcname.replace(os.path.altsep, os.path.sep)
        arcname = os.path.splitdrive(arcname)[1]
        arcname = os.path.sep.join(x for x in arcname.split(os.path.sep) if x not in (b'', os.path.curdir, os.path.pardir))
        if os.path.sep == b'\\':
            illegal = b':<>|"?*'
            if isinstance(arcname, unicode):
                table = {ord(c): ord(b'_') for c in illegal}
            else:
                table = string.maketrans(illegal, b'_' * len(illegal))
            arcname = arcname.translate(table)
            arcname = (x.rstrip(b'.') for x in arcname.split(os.path.sep))
            arcname = os.path.sep.join(x for x in arcname if x)
        targetpath = os.path.join(targetpath, arcname)
        targetpath = os.path.normpath(targetpath)
        upperdirs = os.path.dirname(targetpath)
        if upperdirs and not os.path.exists(upperdirs):
            os.makedirs(upperdirs)
        if member.filename[-1] == b'/':
            if not os.path.isdir(targetpath):
                os.mkdir(targetpath)
            return targetpath
        with self.open(member, pwd=pwd) as source:
            with file(targetpath, b'wb') as target:
                shutil.copyfileobj(source, target)
        return targetpath

    def _writecheck(self, zinfo):
        if zinfo.filename in self.NameToInfo:
            import warnings
            warnings.warn(b'Duplicate name: %r' % zinfo.filename, stacklevel=3)
        if self.mode not in (b'w', b'a'):
            raise RuntimeError, b'write() requires mode "w" or "a"'
        if not self.fp:
            raise RuntimeError, b'Attempt to write ZIP archive that was already closed'
        if zinfo.compress_type == ZIP_DEFLATED and not zlib:
            raise RuntimeError, b'Compression requires the (missing) zlib module'
        if zinfo.compress_type not in (ZIP_STORED, ZIP_DEFLATED):
            raise RuntimeError, b'That compression method is not supported'
        if not self._allowZip64:
            requires_zip64 = None
            if len(self.filelist) >= ZIP_FILECOUNT_LIMIT:
                requires_zip64 = b'Files count'
            elif zinfo.file_size > ZIP64_LIMIT:
                requires_zip64 = b'Filesize'
            elif zinfo.header_offset > ZIP64_LIMIT:
                requires_zip64 = b'Zipfile size'
            if requires_zip64:
                raise LargeZipFile(requires_zip64 + b' would require ZIP64 extensions')
        return

    def write(self, filename, arcname=None, compress_type=None):
        if not self.fp:
            raise RuntimeError(b'Attempt to write to ZIP archive that was already closed')
        st = os.stat(filename)
        isdir = stat.S_ISDIR(st.st_mode)
        mtime = time.localtime(st.st_mtime)
        date_time = mtime[0:6]
        if arcname is None:
            arcname = filename
        arcname = os.path.normpath(os.path.splitdrive(arcname)[1])
        while arcname[0] in (os.sep, os.altsep):
            arcname = arcname[1:]

        if isdir:
            arcname += b'/'
        zinfo = ZipInfo(arcname, date_time)
        zinfo.external_attr = (st[0] & 65535) << 16L
        if isdir:
            zinfo.compress_type = ZIP_STORED
        elif compress_type is None:
            zinfo.compress_type = self.compression
        else:
            zinfo.compress_type = compress_type
        zinfo.file_size = st.st_size
        zinfo.flag_bits = 0
        zinfo.header_offset = self.fp.tell()
        self._writecheck(zinfo)
        self._didModify = True
        if isdir:
            zinfo.file_size = 0
            zinfo.compress_size = 0
            zinfo.CRC = 0
            zinfo.external_attr |= 16
            self.filelist.append(zinfo)
            self.NameToInfo[zinfo.filename] = zinfo
            self.fp.write(zinfo.FileHeader(False))
            return
        else:
            with open(filename, b'rb') as fp:
                zinfo.CRC = CRC = 0
                zinfo.compress_size = compress_size = 0
                zip64 = self._allowZip64 and zinfo.file_size * 1.05 > ZIP64_LIMIT
                self.fp.write(zinfo.FileHeader(zip64))
                if zinfo.compress_type == ZIP_DEFLATED:
                    cmpr = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
                else:
                    cmpr = None
                file_size = 0
                while 1:
                    buf = fp.read(8192)
                    if not buf:
                        break
                    file_size = file_size + len(buf)
                    CRC = crc32(buf, CRC) & 4294967295L
                    if cmpr:
                        buf = cmpr.compress(buf)
                        compress_size = compress_size + len(buf)
                    self.fp.write(buf)

            if cmpr:
                buf = cmpr.flush()
                compress_size = compress_size + len(buf)
                self.fp.write(buf)
                zinfo.compress_size = compress_size
            else:
                zinfo.compress_size = file_size
            zinfo.CRC = CRC
            zinfo.file_size = file_size
            if not zip64 and self._allowZip64:
                if file_size > ZIP64_LIMIT:
                    raise RuntimeError(b'File size has increased during compressing')
                if compress_size > ZIP64_LIMIT:
                    raise RuntimeError(b'Compressed size larger than uncompressed size')
            position = self.fp.tell()
            self.fp.seek(zinfo.header_offset, 0)
            self.fp.write(zinfo.FileHeader(zip64))
            self.fp.seek(position, 0)
            self.filelist.append(zinfo)
            self.NameToInfo[zinfo.filename] = zinfo
            return

    def writestr(self, zinfo_or_arcname, bytes, compress_type=None):
        if not isinstance(zinfo_or_arcname, ZipInfo):
            zinfo = ZipInfo(filename=zinfo_or_arcname, date_time=time.localtime(time.time())[:6])
            zinfo.compress_type = self.compression
            if zinfo.filename[-1] == b'/':
                zinfo.external_attr = 1107099648
                zinfo.external_attr |= 16
            else:
                zinfo.external_attr = 25165824
        else:
            zinfo = zinfo_or_arcname
        if not self.fp:
            raise RuntimeError(b'Attempt to write to ZIP archive that was already closed')
        if compress_type is not None:
            zinfo.compress_type = compress_type
        zinfo.file_size = len(bytes)
        zinfo.header_offset = self.fp.tell()
        self._writecheck(zinfo)
        self._didModify = True
        zinfo.CRC = crc32(bytes) & 4294967295L
        if zinfo.compress_type == ZIP_DEFLATED:
            co = zlib.compressobj(zlib.Z_DEFAULT_COMPRESSION, zlib.DEFLATED, -15)
            bytes = co.compress(bytes) + co.flush()
            zinfo.compress_size = len(bytes)
        else:
            zinfo.compress_size = zinfo.file_size
        zip64 = zinfo.file_size > ZIP64_LIMIT or zinfo.compress_size > ZIP64_LIMIT
        if zip64 and not self._allowZip64:
            raise LargeZipFile(b'Filesize would require ZIP64 extensions')
        self.fp.write(zinfo.FileHeader(zip64))
        self.fp.write(bytes)
        if zinfo.flag_bits & 8:
            fmt = b'<LLQQ' if zip64 else b'<LLLL'
            self.fp.write(struct.pack(fmt, _DD_SIGNATURE, zinfo.CRC, zinfo.compress_size, zinfo.file_size))
        self.fp.flush()
        self.filelist.append(zinfo)
        self.NameToInfo[zinfo.filename] = zinfo
        return

    def __del__(self):
        self.close()
        return

    def close(self):
        if self.fp is None:
            return
        else:
            try:
                if self.mode in (b'w', b'a') and self._didModify:
                    pos1 = self.fp.tell()
                    for zinfo in self.filelist:
                        dt = zinfo.date_time
                        dosdate = dt[0] - 1980 << 9 | dt[1] << 5 | dt[2]
                        dostime = dt[3] << 11 | dt[4] << 5 | dt[5] // 2
                        extra = []
                        if zinfo.file_size > ZIP64_LIMIT or zinfo.compress_size > ZIP64_LIMIT:
                            extra.append(zinfo.file_size)
                            extra.append(zinfo.compress_size)
                            file_size = 4294967295L
                            compress_size = 4294967295L
                        else:
                            file_size = zinfo.file_size
                            compress_size = zinfo.compress_size
                        if zinfo.header_offset > ZIP64_LIMIT:
                            extra.append(zinfo.header_offset)
                            header_offset = 4294967295L
                        else:
                            header_offset = zinfo.header_offset
                        extra_data = zinfo.extra
                        if extra:
                            extra_data = _strip_extra(extra_data, (1,))
                            extra_data = struct.pack((b'<HH' + b'Q' * len(extra)), 1, (8 * len(extra)), *extra) + extra_data
                            extract_version = max(45, zinfo.extract_version)
                            create_version = max(45, zinfo.create_version)
                        else:
                            extract_version = zinfo.extract_version
                            create_version = zinfo.create_version
                        try:
                            filename, flag_bits = zinfo._encodeFilenameFlags()
                            centdir = struct.pack(structCentralDir, stringCentralDir, create_version, zinfo.create_system, extract_version, zinfo.reserved, flag_bits, zinfo.compress_type, dostime, dosdate, zinfo.CRC, compress_size, file_size, len(filename), len(extra_data), len(zinfo.comment), 0, zinfo.internal_attr, zinfo.external_attr, header_offset)
                        except DeprecationWarning:
                            print >> sys.stderr, (structCentralDir,
                             stringCentralDir, create_version,
                             zinfo.create_system, extract_version, zinfo.reserved,
                             zinfo.flag_bits, zinfo.compress_type, dostime, dosdate,
                             zinfo.CRC, compress_size, file_size,
                             len(zinfo.filename), len(extra_data), len(zinfo.comment),
                             0, zinfo.internal_attr, zinfo.external_attr,
                             header_offset)
                            raise

                        self.fp.write(centdir)
                        self.fp.write(filename)
                        self.fp.write(extra_data)
                        self.fp.write(zinfo.comment)

                    pos2 = self.fp.tell()
                    centDirCount = len(self.filelist)
                    centDirSize = pos2 - pos1
                    centDirOffset = pos1
                    requires_zip64 = None
                    if centDirCount > ZIP_FILECOUNT_LIMIT:
                        requires_zip64 = b'Files count'
                    elif centDirOffset > ZIP64_LIMIT:
                        requires_zip64 = b'Central directory offset'
                    elif centDirSize > ZIP64_LIMIT:
                        requires_zip64 = b'Central directory size'
                    if requires_zip64:
                        if not self._allowZip64:
                            raise LargeZipFile(requires_zip64 + b' would require ZIP64 extensions')
                        zip64endrec = struct.pack(structEndArchive64, stringEndArchive64, 44, 45, 45, 0, 0, centDirCount, centDirCount, centDirSize, centDirOffset)
                        self.fp.write(zip64endrec)
                        zip64locrec = struct.pack(structEndArchive64Locator, stringEndArchive64Locator, 0, pos2, 1)
                        self.fp.write(zip64locrec)
                        centDirCount = min(centDirCount, 65535)
                        centDirSize = min(centDirSize, 4294967295L)
                        centDirOffset = min(centDirOffset, 4294967295L)
                    endrec = struct.pack(structEndArchive, stringEndArchive, 0, 0, centDirCount, centDirCount, centDirSize, centDirOffset, len(self._comment))
                    self.fp.write(endrec)
                    self.fp.write(self._comment)
                    self.fp.flush()
            finally:
                fp = self.fp
                self.fp = None
                if not self._filePassed:
                    fp.close()

            return


class PyZipFile(ZipFile):

    def writepy(self, pathname, basename=b''):
        dir, name = os.path.split(pathname)
        if os.path.isdir(pathname):
            initname = os.path.join(pathname, b'__init__.py')
            if os.path.isfile(initname):
                if basename:
                    basename = b'%s/%s' % (basename, name)
                else:
                    basename = name
                if self.debug:
                    print b'Adding package in', pathname, b'as', basename
                fname, arcname = self._get_codename(initname[0:-3], basename)
                if self.debug:
                    print b'Adding', arcname
                self.write(fname, arcname)
                dirlist = os.listdir(pathname)
                dirlist.remove(b'__init__.py')
                for filename in dirlist:
                    path = os.path.join(pathname, filename)
                    root, ext = os.path.splitext(filename)
                    if os.path.isdir(path):
                        if os.path.isfile(os.path.join(path, b'__init__.py')):
                            self.writepy(path, basename)
                    elif ext == b'.py':
                        fname, arcname = self._get_codename(path[0:-3], basename)
                        if self.debug:
                            print b'Adding', arcname
                        self.write(fname, arcname)

            elif self.debug:
                print b'Adding files from directory', pathname
            for filename in os.listdir(pathname):
                path = os.path.join(pathname, filename)
                root, ext = os.path.splitext(filename)
                if ext == b'.py':
                    fname, arcname = self._get_codename(path[0:-3], basename)
                    if self.debug:
                        print b'Adding', arcname
                    self.write(fname, arcname)

        elif pathname[-3:] != b'.py':
            raise RuntimeError, b'Files added with writepy() must end with ".py"'
        fname, arcname = self._get_codename(pathname[0:-3], basename)
        if self.debug:
            print b'Adding file', arcname
        self.write(fname, arcname)
        return

    def _get_codename(self, pathname, basename):
        file_py = pathname + b'.py'
        file_pyc = pathname + b'.pyc'
        file_pyo = pathname + b'.pyo'
        if os.path.isfile(file_pyo) and os.stat(file_pyo).st_mtime >= os.stat(file_py).st_mtime:
            fname = file_pyo
        elif not os.path.isfile(file_pyc) or os.stat(file_pyc).st_mtime < os.stat(file_py).st_mtime:
            import py_compile
            if self.debug:
                print b'Compiling', file_py
            try:
                py_compile.compile(file_py, file_pyc, None, True)
            except py_compile.PyCompileError as err:
                print err.msg

            fname = file_pyc
        else:
            fname = file_pyc
        archivename = os.path.split(fname)[1]
        if basename:
            archivename = b'%s/%s' % (basename, archivename)
        return (
         fname, archivename)


def main(args=None):
    import textwrap
    USAGE = textwrap.dedent(b'        Usage:\n            zipfile.py -l zipfile.zip        # Show listing of a zipfile\n            zipfile.py -t zipfile.zip        # Test if a zipfile is valid\n            zipfile.py -e zipfile.zip target # Extract zipfile into target dir\n            zipfile.py -c zipfile.zip src ... # Create zipfile from sources\n        ')
    if args is None:
        args = sys.argv[1:]
    if not args or args[0] not in (b'-l', b'-c', b'-e', b'-t'):
        print USAGE
        sys.exit(1)
    if args[0] == b'-l':
        if len(args) != 2:
            print USAGE
            sys.exit(1)
        with ZipFile(args[1], b'r') as zf:
            zf.printdir()
    elif args[0] == b'-t':
        if len(args) != 2:
            print USAGE
            sys.exit(1)
        with ZipFile(args[1], b'r') as zf:
            badfile = zf.testzip()
        if badfile:
            print (b'The following enclosed file is corrupted: {!r}').format(badfile)
        print b'Done testing'
    elif args[0] == b'-e':
        if len(args) != 3:
            print USAGE
            sys.exit(1)
        with ZipFile(args[1], b'r') as zf:
            zf.extractall(args[2])
    elif args[0] == b'-c':
        if len(args) < 3:
            print USAGE
            sys.exit(1)

        def addToZip(zf, path, zippath):
            if os.path.isfile(path):
                zf.write(path, zippath, ZIP_DEFLATED)
            elif os.path.isdir(path):
                if zippath:
                    zf.write(path, zippath)
                for nm in os.listdir(path):
                    addToZip(zf, os.path.join(path, nm), os.path.join(zippath, nm))

            return

        with ZipFile(args[1], b'w', allowZip64=True) as zf:
            for path in args[2:]:
                zippath = os.path.basename(path)
                if not zippath:
                    zippath = os.path.basename(os.path.dirname(path))
                if zippath in (b'', os.curdir, os.pardir):
                    zippath = b''
                addToZip(zf, path, zippath)

    return


if __name__ == b'__main__':
    main()
