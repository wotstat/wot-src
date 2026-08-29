import os, sys, posixpath, urllib
try:
    import _winreg
except ImportError:
    _winreg = None

__all__ = [
 2, 3, 4, 
 5, 6, 7]
knownfiles = [
 8, 
 9, 
 10, 
 11, 
 12, 
 13, 
 14, 
 13, 
 15]
inited = False
_db = None

class MimeTypes:

    def __init__(self, filenames=(), strict=True):
        global inited
        if not inited:
            init()
        self.encodings_map = encodings_map.copy()
        self.suffix_map = suffix_map.copy()
        self.types_map = ({}, {})
        self.types_map_inv = ({}, {})
        for ext, type in types_map.items():
            self.add_type(type, ext, True)

        for ext, type in common_types.items():
            self.add_type(type, ext, False)

        for name in filenames:
            self.read(name, strict)

        return

    def add_type(self, type, ext, strict=True):
        self.types_map[strict][ext] = type
        exts = self.types_map_inv[strict].setdefault(type, [])
        if ext not in exts:
            exts.append(ext)
        return

    def guess_type(self, url, strict=True):
        scheme, url = urllib.splittype(url)
        if scheme == b'data':
            comma = url.find(b',')
            if comma < 0:
                return (None, None)
            semi = url.find(b';', 0, comma)
            if semi >= 0:
                type = url[:semi]
            else:
                type = url[:comma]
            if b'=' in type or b'/' not in type:
                type = b'text/plain'
            return (type, None)
        else:
            base, ext = posixpath.splitext(url)
            while ext in self.suffix_map:
                base, ext = posixpath.splitext(base + self.suffix_map[ext])

            if ext in self.encodings_map:
                encoding = self.encodings_map[ext]
                base, ext = posixpath.splitext(base)
            else:
                encoding = None
            types_map = self.types_map[True]
            if ext in types_map:
                return (types_map[ext], encoding)
            if ext.lower() in types_map:
                return (types_map[ext.lower()], encoding)
            if strict:
                return (None, encoding)
            types_map = self.types_map[False]
            if ext in types_map:
                return (types_map[ext], encoding)
            if ext.lower() in types_map:
                return (types_map[ext.lower()], encoding)
            return (None, encoding)
            return

    def guess_all_extensions(self, type, strict=True):
        type = type.lower()
        extensions = self.types_map_inv[True].get(type, [])
        if not strict:
            for ext in self.types_map_inv[False].get(type, []):
                if ext not in extensions:
                    extensions.append(ext)

        return extensions

    def guess_extension(self, type, strict=True):
        extensions = self.guess_all_extensions(type, strict)
        if not extensions:
            return None
        else:
            return extensions[0]

    def read(self, filename, strict=True):
        with open(filename) as fp:
            self.readfp(fp, strict)
        return

    def readfp(self, fp, strict=True):
        while 1:
            line = fp.readline()
            if not line:
                break
            words = line.split()
            for i in range(len(words)):
                if words[i][0] == b'#':
                    del words[i:]
                    break

            if not words:
                continue
            type, suffixes = words[0], words[1:]
            for suff in suffixes:
                self.add_type(type, b'.' + suff, strict)

        return

    def read_windows_registry(self, strict=True):
        if not _winreg:
            return

        def enum_types(mimedb):
            i = 0
            while True:
                try:
                    ctype = _winreg.EnumKey(mimedb, i)
                except EnvironmentError:
                    break
                else:
                    if b'\x00' not in ctype:
                        yield ctype
                    i += 1

            return

        default_encoding = sys.getdefaultencoding()
        with _winreg.OpenKey(_winreg.HKEY_CLASSES_ROOT, b'') as hkcr:
            for subkeyname in enum_types(hkcr):
                try:
                    with _winreg.OpenKey(hkcr, subkeyname) as subkey:
                        if not subkeyname.startswith(b'.'):
                            continue
                        mimetype, datatype = _winreg.QueryValueEx(subkey, b'Content Type')
                        if datatype != _winreg.REG_SZ:
                            continue
                        try:
                            mimetype = mimetype.encode(default_encoding)
                        except UnicodeEncodeError:
                            continue

                        self.add_type(mimetype, subkeyname, strict)
                except EnvironmentError:
                    continue

        return


def guess_type(url, strict=True):
    global _db
    if _db is None:
        init()
    return _db.guess_type(url, strict)


def guess_all_extensions(type, strict=True):
    if _db is None:
        init()
    return _db.guess_all_extensions(type, strict)


def guess_extension(type, strict=True):
    if _db is None:
        init()
    return _db.guess_extension(type, strict)


def add_type(type, ext, strict=True):
    if _db is None:
        init()
    return _db.add_type(type, ext, strict)


def init(files=None):
    global _db
    global common_types
    global encodings_map
    global inited
    global suffix_map
    global types_map
    inited = True
    db = MimeTypes()
    if files is None:
        if _winreg:
            db.read_windows_registry()
        files = knownfiles
    for file in files:
        if os.path.isfile(file):
            db.read(file)

    encodings_map = db.encodings_map
    suffix_map = db.suffix_map
    types_map = db.types_map[True]
    common_types = db.types_map[False]
    _db = db
    return


def read_mime_types(file):
    try:
        f = open(file)
    except IOError:
        return

    with f:
        db = MimeTypes()
        db.readfp(f, True)
        return db.types_map[True]
    return


def _default_mime_types():
    global common_types
    global encodings_map
    global suffix_map
    global types_map
    suffix_map = {b'.svgz': b'.svg.gz', 
       b'.tgz': b'.tar.gz', 
       b'.taz': b'.tar.gz', 
       b'.tz': b'.tar.gz', 
       b'.tbz2': b'.tar.bz2', 
       b'.txz': b'.tar.xz'}
    encodings_map = {b'.gz': b'gzip', 
       b'.Z': b'compress', 
       b'.bz2': b'bzip2', 
       b'.xz': b'xz'}
    types_map = {b'.a': b'application/octet-stream', 
       b'.ai': b'application/postscript', 
       b'.aif': b'audio/x-aiff', 
       b'.aifc': b'audio/x-aiff', 
       b'.aiff': b'audio/x-aiff', 
       b'.au': b'audio/basic', 
       b'.avi': b'video/x-msvideo', 
       b'.bat': b'text/plain', 
       b'.bcpio': b'application/x-bcpio', 
       b'.bin': b'application/octet-stream', 
       b'.bmp': b'image/x-ms-bmp', 
       b'.c': b'text/plain', 
       b'.cdf': b'application/x-cdf', 
       b'.cdf': b'application/x-netcdf', 
       b'.cpio': b'application/x-cpio', 
       b'.csh': b'application/x-csh', 
       b'.css': b'text/css', 
       b'.csv': b'text/csv', 
       b'.dll': b'application/octet-stream', 
       b'.doc': b'application/msword', 
       b'.dot': b'application/msword', 
       b'.dvi': b'application/x-dvi', 
       b'.eml': b'message/rfc822', 
       b'.eps': b'application/postscript', 
       b'.etx': b'text/x-setext', 
       b'.exe': b'application/octet-stream', 
       b'.gif': b'image/gif', 
       b'.gtar': b'application/x-gtar', 
       b'.h': b'text/plain', 
       b'.hdf': b'application/x-hdf', 
       b'.htm': b'text/html', 
       b'.html': b'text/html', 
       b'.ico': b'image/vnd.microsoft.icon', 
       b'.ief': b'image/ief', 
       b'.jpe': b'image/jpeg', 
       b'.jpeg': b'image/jpeg', 
       b'.jpg': b'image/jpeg', 
       b'.js': b'application/javascript', 
       b'.json': b'application/json', 
       b'.ksh': b'text/plain', 
       b'.latex': b'application/x-latex', 
       b'.m1v': b'video/mpeg', 
       b'.man': b'application/x-troff-man', 
       b'.me': b'application/x-troff-me', 
       b'.mht': b'message/rfc822', 
       b'.mhtml': b'message/rfc822', 
       b'.mif': b'application/x-mif', 
       b'.mjs': b'application/javascript', 
       b'.mov': b'video/quicktime', 
       b'.movie': b'video/x-sgi-movie', 
       b'.mp2': b'audio/mpeg', 
       b'.mp3': b'audio/mpeg', 
       b'.mp4': b'video/mp4', 
       b'.mpa': b'video/mpeg', 
       b'.mpe': b'video/mpeg', 
       b'.mpeg': b'video/mpeg', 
       b'.mpg': b'video/mpeg', 
       b'.ms': b'application/x-troff-ms', 
       b'.nc': b'application/x-netcdf', 
       b'.nws': b'message/rfc822', 
       b'.o': b'application/octet-stream', 
       b'.obj': b'application/octet-stream', 
       b'.oda': b'application/oda', 
       b'.p12': b'application/x-pkcs12', 
       b'.p7c': b'application/pkcs7-mime', 
       b'.pbm': b'image/x-portable-bitmap', 
       b'.pdf': b'application/pdf', 
       b'.pfx': b'application/x-pkcs12', 
       b'.pgm': b'image/x-portable-graymap', 
       b'.pl': b'text/plain', 
       b'.png': b'image/png', 
       b'.pnm': b'image/x-portable-anymap', 
       b'.pot': b'application/vnd.ms-powerpoint', 
       b'.ppa': b'application/vnd.ms-powerpoint', 
       b'.ppm': b'image/x-portable-pixmap', 
       b'.pps': b'application/vnd.ms-powerpoint', 
       b'.ppt': b'application/vnd.ms-powerpoint', 
       b'.ps': b'application/postscript', 
       b'.pwz': b'application/vnd.ms-powerpoint', 
       b'.py': b'text/x-python', 
       b'.pyc': b'application/x-python-code', 
       b'.pyo': b'application/x-python-code', 
       b'.qt': b'video/quicktime', 
       b'.ra': b'audio/x-pn-realaudio', 
       b'.ram': b'application/x-pn-realaudio', 
       b'.ras': b'image/x-cmu-raster', 
       b'.rdf': b'application/xml', 
       b'.rgb': b'image/x-rgb', 
       b'.roff': b'application/x-troff', 
       b'.rtx': b'text/richtext', 
       b'.sgm': b'text/x-sgml', 
       b'.sgml': b'text/x-sgml', 
       b'.sh': b'application/x-sh', 
       b'.shar': b'application/x-shar', 
       b'.snd': b'audio/basic', 
       b'.so': b'application/octet-stream', 
       b'.src': b'application/x-wais-source', 
       b'.sv4cpio': b'application/x-sv4cpio', 
       b'.sv4crc': b'application/x-sv4crc', 
       b'.svg': b'image/svg+xml', 
       b'.swf': b'application/x-shockwave-flash', 
       b'.t': b'application/x-troff', 
       b'.tar': b'application/x-tar', 
       b'.tcl': b'application/x-tcl', 
       b'.tex': b'application/x-tex', 
       b'.texi': b'application/x-texinfo', 
       b'.texinfo': b'application/x-texinfo', 
       b'.tif': b'image/tiff', 
       b'.tiff': b'image/tiff', 
       b'.tr': b'application/x-troff', 
       b'.tsv': b'text/tab-separated-values', 
       b'.txt': b'text/plain', 
       b'.ustar': b'application/x-ustar', 
       b'.vcf': b'text/x-vcard', 
       b'.wav': b'audio/x-wav', 
       b'.webm': b'video/webm', 
       b'.wiz': b'application/msword', 
       b'.wsdl': b'application/xml', 
       b'.xbm': b'image/x-xbitmap', 
       b'.xlb': b'application/vnd.ms-excel', 
       b'.xls': b'application/excel', 
       b'.xls': b'application/vnd.ms-excel', 
       b'.xml': b'text/xml', 
       b'.xpdl': b'application/xml', 
       b'.xpm': b'image/x-xpixmap', 
       b'.xsl': b'application/xml', 
       b'.xwd': b'image/x-xwindowdump', 
       b'.zip': b'application/zip'}
    common_types = {b'.jpg': b'image/jpg', 
       b'.mid': b'audio/midi', 
       b'.midi': b'audio/midi', 
       b'.pct': b'image/pict', 
       b'.pic': b'image/pict', 
       b'.pict': b'image/pict', 
       b'.rtf': b'application/rtf', 
       b'.xul': b'text/xul'}
    return


_default_mime_types()
if __name__ == b'__main__':
    import getopt
    USAGE = b'Usage: mimetypes.py [options] type\n\nOptions:\n    --help / -h       -- print this message and exit\n    --lenient / -l    -- additionally search of some common, but non-standard\n                         types.\n    --extension / -e  -- guess extension instead of type\n\nMore than one type argument may be given.\n'

    def usage(code, msg=b''):
        print USAGE
        if msg:
            print msg
        sys.exit(code)
        return


    try:
        opts, args = getopt.getopt(sys.argv[1:], b'hle', [
         b'help', b'lenient', b'extension'])
    except getopt.error as msg:
        usage(1, msg)

    strict = 1
    extension = 0
    for opt, arg in opts:
        if opt in (b'-h', b'--help'):
            usage(0)
        elif opt in (b'-l', b'--lenient'):
            strict = 0
        elif opt in (b'-e', b'--extension'):
            extension = 1

    for gtype in args:
        if extension:
            guess = guess_extension(gtype, strict)
            if not guess:
                print b"I don't know anything about type", gtype
            else:
                print guess
        else:
            guess, encoding = guess_type(gtype, strict)
            if not guess:
                print b"I don't know anything about type", gtype
            else:
                print b'type:', guess, b'encoding:', encoding
