import string
try:
    from cPickle import dumps, loads
except ImportError:
    from pickle import dumps, loads

import re, warnings
__all__ = [
 3, 4, 5, 6, 
 7, 8]
_nulljoin = (b'').join
_semispacejoin = (b'; ').join
_spacejoin = (b' ').join

class CookieError(Exception):
    pass


_LegalChars = string.ascii_letters + string.digits + b"!#$%&'*+-.^_`|~"
_Translator = {b'\x00': b'\\000', 
   b'\x01': b'\\001', b'\x02': b'\\002', b'\x03': b'\\003', 
   b'\x04': b'\\004', b'\x05': b'\\005', b'\x06': b'\\006', 
   b'\x07': b'\\007', b'\x08': b'\\010', b'\t': b'\\011', 
   b'\n': b'\\012', b'\x0b': b'\\013', b'\x0c': b'\\014', 
   b'\r': b'\\015', b'\x0e': b'\\016', b'\x0f': b'\\017', 
   b'\x10': b'\\020', b'\x11': b'\\021', b'\x12': b'\\022', 
   b'\x13': b'\\023', b'\x14': b'\\024', b'\x15': b'\\025', 
   b'\x16': b'\\026', b'\x17': b'\\027', b'\x18': b'\\030', 
   b'\x19': b'\\031', b'\x1a': b'\\032', b'\x1b': b'\\033', 
   b'\x1c': b'\\034', b'\x1d': b'\\035', b'\x1e': b'\\036', 
   b'\x1f': b'\\037', b',': b'\\054', 
   b';': b'\\073', b'"': b'\\"', 
   b'\\': b'\\\\', b'\x7f': b'\\177', 
   b'\x80': b'\\200', b'\x81': b'\\201', b'\x82': b'\\202', 
   b'\x83': b'\\203', b'\x84': b'\\204', b'\x85': b'\\205', 
   b'\x86': b'\\206', b'\x87': b'\\207', b'\x88': b'\\210', 
   b'\x89': b'\\211', b'\x8a': b'\\212', b'\x8b': b'\\213', 
   b'\x8c': b'\\214', b'\x8d': b'\\215', b'\x8e': b'\\216', 
   b'\x8f': b'\\217', b'\x90': b'\\220', b'\x91': b'\\221', 
   b'\x92': b'\\222', b'\x93': b'\\223', b'\x94': b'\\224', 
   b'\x95': b'\\225', b'\x96': b'\\226', b'\x97': b'\\227', 
   b'\x98': b'\\230', b'\x99': b'\\231', b'\x9a': b'\\232', 
   b'\x9b': b'\\233', b'\x9c': b'\\234', b'\x9d': b'\\235', 
   b'\x9e': b'\\236', b'\x9f': b'\\237', b'\xa0': b'\\240', 
   b'\xa1': b'\\241', b'\xa2': b'\\242', b'\xa3': b'\\243', 
   b'\xa4': b'\\244', b'\xa5': b'\\245', b'\xa6': b'\\246', 
   b'\xa7': b'\\247', b'\xa8': b'\\250', b'\xa9': b'\\251', 
   b'\xaa': b'\\252', b'\xab': b'\\253', b'\xac': b'\\254', 
   b'\xad': b'\\255', b'\xae': b'\\256', b'\xaf': b'\\257', 
   b'\xb0': b'\\260', b'\xb1': b'\\261', b'\xb2': b'\\262', 
   b'\xb3': b'\\263', b'\xb4': b'\\264', b'\xb5': b'\\265', 
   b'\xb6': b'\\266', b'\xb7': b'\\267', b'\xb8': b'\\270', 
   b'\xb9': b'\\271', b'\xba': b'\\272', b'\xbb': b'\\273', 
   b'\xbc': b'\\274', b'\xbd': b'\\275', b'\xbe': b'\\276', 
   b'\xbf': b'\\277', b'\xc0': b'\\300', b'\xc1': b'\\301', 
   b'\xc2': b'\\302', b'\xc3': b'\\303', b'\xc4': b'\\304', 
   b'\xc5': b'\\305', b'\xc6': b'\\306', b'\xc7': b'\\307', 
   b'\xc8': b'\\310', b'\xc9': b'\\311', b'\xca': b'\\312', 
   b'\xcb': b'\\313', b'\xcc': b'\\314', b'\xcd': b'\\315', 
   b'\xce': b'\\316', b'\xcf': b'\\317', b'\xd0': b'\\320', 
   b'\xd1': b'\\321', b'\xd2': b'\\322', b'\xd3': b'\\323', 
   b'\xd4': b'\\324', b'\xd5': b'\\325', b'\xd6': b'\\326', 
   b'\xd7': b'\\327', b'\xd8': b'\\330', b'\xd9': b'\\331', 
   b'\xda': b'\\332', b'\xdb': b'\\333', b'\xdc': b'\\334', 
   b'\xdd': b'\\335', b'\xde': b'\\336', b'\xdf': b'\\337', 
   b'\xe0': b'\\340', b'\xe1': b'\\341', b'\xe2': b'\\342', 
   b'\xe3': b'\\343', b'\xe4': b'\\344', b'\xe5': b'\\345', 
   b'\xe6': b'\\346', b'\xe7': b'\\347', b'\xe8': b'\\350', 
   b'\xe9': b'\\351', b'\xea': b'\\352', b'\xeb': b'\\353', 
   b'\xec': b'\\354', b'\xed': b'\\355', b'\xee': b'\\356', 
   b'\xef': b'\\357', b'\xf0': b'\\360', b'\xf1': b'\\361', 
   b'\xf2': b'\\362', b'\xf3': b'\\363', b'\xf4': b'\\364', 
   b'\xf5': b'\\365', b'\xf6': b'\\366', b'\xf7': b'\\367', 
   b'\xf8': b'\\370', b'\xf9': b'\\371', b'\xfa': b'\\372', 
   b'\xfb': b'\\373', b'\xfc': b'\\374', b'\xfd': b'\\375', 
   b'\xfe': b'\\376', b'\xff': b'\\377'}
_idmap = (b'').join(chr(x) for x in xrange(256))

def _quote(str, LegalChars=_LegalChars, idmap=_idmap, translate=string.translate):
    if b'' == translate(str, idmap, LegalChars):
        return str
    else:
        return b'"' + _nulljoin(map(_Translator.get, str, str)) + b'"'

    return


_OctalPatt = re.compile(b'\\\\[0-3][0-7][0-7]')
_QuotePatt = re.compile(b'[\\\\].')

def _unquote(str):
    if len(str) < 2:
        return str
    if str[0] != b'"' or str[-1] != b'"':
        return str
    str = str[1:-1]
    i = 0
    n = len(str)
    res = []
    while 0 <= i < n:
        Omatch = _OctalPatt.search(str, i)
        Qmatch = _QuotePatt.search(str, i)
        if not Omatch and not Qmatch:
            res.append(str[i:])
            break
        j = k = -1
        if Omatch:
            j = Omatch.start(0)
        if Qmatch:
            k = Qmatch.start(0)
        if Qmatch and (not Omatch or k < j):
            res.append(str[i:k])
            res.append(str[k + 1])
            i = k + 2
        else:
            res.append(str[i:j])
            res.append(chr(int(str[j + 1:j + 4], 8)))
            i = j + 4

    return _nulljoin(res)


_weekdayname = [
 350, 351, 352, 353, 354, 355, 356]
_monthname = [
 1, 
 357, 358, 359, 360, 361, 362, 
 363, 364, 365, 366, 367, 368]

def _getdate(future=0, weekdayname=_weekdayname, monthname=_monthname):
    from time import gmtime, time
    now = time()
    year, month, day, hh, mm, ss, wd, y, z = gmtime(now + future)
    return b'%s, %02d %3s %4d %02d:%02d:%02d GMT' % (
     weekdayname[wd], day, monthname[month], year, hh, mm, ss)


class Morsel(dict):
    _reserved = {b'expires': b'expires', b'path': b'Path', 
       b'comment': b'Comment', 
       b'domain': b'Domain', 
       b'max-age': b'Max-Age', 
       b'secure': b'secure', 
       b'httponly': b'httponly', 
       b'version': b'Version'}
    _flags = {
     b'secure', b'httponly'}

    def __init__(self):
        self.key = self.value = self.coded_value = None
        for K in self._reserved:
            dict.__setitem__(self, K, b'')

        return

    def __setitem__(self, K, V):
        K = K.lower()
        if K not in self._reserved:
            raise CookieError(b'Invalid Attribute %s' % K)
        dict.__setitem__(self, K, V)
        return

    def isReservedKey(self, K):
        return K.lower() in self._reserved

    def set(self, key, val, coded_val, LegalChars=_LegalChars, idmap=_idmap, translate=string.translate):
        if key.lower() in self._reserved:
            raise CookieError(b'Attempt to set a reserved key: %s' % key)
        if b'' != translate(key, idmap, LegalChars):
            raise CookieError(b'Illegal key value: %s' % key)
        self.key = key
        self.value = val
        self.coded_value = coded_val
        return

    def output(self, attrs=None, header=b'Set-Cookie:'):
        return b'%s %s' % (header, self.OutputString(attrs))

    __str__ = output

    def __repr__(self):
        return b'<%s: %s=%s>' % (self.__class__.__name__,
         self.key, repr(self.value))

    def js_output(self, attrs=None):
        return b'\n        <script type="text/javascript">\n        <!-- begin hiding\n        document.cookie = "%s";\n        // end hiding -->\n        </script>\n        ' % (self.OutputString(attrs).replace(b'"', b'\\"'),)

    def OutputString(self, attrs=None):
        result = []
        RA = result.append
        RA(b'%s=%s' % (self.key, self.coded_value))
        if attrs is None:
            attrs = self._reserved
        items = self.items()
        items.sort()
        for K, V in items:
            if V == b'':
                continue
            if K not in attrs:
                continue
            if K == b'expires' and type(V) == type(1):
                RA(b'%s=%s' % (self._reserved[K], _getdate(V)))
            elif K == b'max-age' and type(V) == type(1):
                RA(b'%s=%d' % (self._reserved[K], V))
            elif K == b'secure':
                RA(str(self._reserved[K]))
            elif K == b'httponly':
                RA(str(self._reserved[K]))
            else:
                RA(b'%s=%s' % (self._reserved[K], V))

        return _semispacejoin(result)


_LegalKeyChars = b"\\w\\d!#%&'~_`><@,:/\\$\\*\\+\\-\\.\\^\\|\\)\\(\\?\\}\\{\\="
_LegalValueChars = _LegalKeyChars + b'\\[\\]'
_CookiePattern = re.compile(b'(?x)\\s*(?P<key>[' + _LegalKeyChars + b']+?)(\\s*=\\s*(?P<val>"(?:[^\\\\"]|\\\\.)*"|\\w{3},\\s[\\s\\w\\d-]{9,11}\\s[\\d:]{8}\\sGMT|[' + _LegalValueChars + b']*))?\\s*(\\s+|;|$)')

class BaseCookie(dict):

    def value_decode(self, val):
        return (
         val, val)

    def value_encode(self, val):
        strval = str(val)
        return (strval, strval)

    def __init__(self, input=None):
        if input:
            self.load(input)
        return

    def __set(self, key, real_value, coded_value):
        M = self.get(key, Morsel())
        M.set(key, real_value, coded_value)
        dict.__setitem__(self, key, M)
        return

    def __setitem__(self, key, value):
        if isinstance(value, Morsel):
            dict.__setitem__(self, key, value)
        else:
            rval, cval = self.value_encode(value)
            self.__set(key, rval, cval)
        return

    def output(self, attrs=None, header=b'Set-Cookie:', sep=b'\r\n'):
        result = []
        items = self.items()
        items.sort()
        for K, V in items:
            result.append(V.output(attrs, header))

        return sep.join(result)

    __str__ = output

    def __repr__(self):
        L = []
        items = self.items()
        items.sort()
        for K, V in items:
            L.append(b'%s=%s' % (K, repr(V.value)))

        return b'<%s: %s>' % (self.__class__.__name__, _spacejoin(L))

    def js_output(self, attrs=None):
        result = []
        items = self.items()
        items.sort()
        for K, V in items:
            result.append(V.js_output(attrs))

        return _nulljoin(result)

    def load(self, rawdata):
        if type(rawdata) == type(b''):
            self.__ParseString(rawdata)
        else:
            for k, v in rawdata.items():
                self[k] = v

        return

    def __ParseString(self, str, patt=_CookiePattern):
        i = 0
        n = len(str)
        M = None
        while 0 <= i < n:
            match = patt.match(str, i)
            if not match:
                break
            K, V = match.group(b'key'), match.group(b'val')
            i = match.end(0)
            if K[0] == b'$':
                if M:
                    M[K[1:]] = V
            elif K.lower() in Morsel._reserved:
                if M:
                    if V is None:
                        if K.lower() in Morsel._flags:
                            M[K] = True
                    else:
                        M[K] = _unquote(V)
            elif V is not None:
                rval, cval = self.value_decode(V)
                self.__set(K, rval, cval)
                M = self[K]

        return


class SimpleCookie(BaseCookie):

    def value_decode(self, val):
        return (
         _unquote(val), val)

    def value_encode(self, val):
        strval = str(val)
        return (strval, _quote(strval))


class SerialCookie(BaseCookie):

    def __init__(self, input=None):
        warnings.warn(b'SerialCookie class is insecure; do not use it', DeprecationWarning)
        BaseCookie.__init__(self, input)
        return

    def value_decode(self, val):
        return (
         loads(_unquote(val)), val)

    def value_encode(self, val):
        return (val, _quote(dumps(val)))


class SmartCookie(BaseCookie):

    def __init__(self, input=None):
        warnings.warn(b'Cookie/SmartCookie class is insecure; do not use it', DeprecationWarning)
        BaseCookie.__init__(self, input)
        return

    def value_decode(self, val):
        strval = _unquote(val)
        try:
            return (
             loads(strval), val)
        except:
            return (
             strval, val)

        return

    def value_encode(self, val):
        if type(val) == type(b''):
            return (val, _quote(val))
        else:
            return (
             val, _quote(dumps(val)))

        return


Cookie = SmartCookie

def _test():
    import doctest, Cookie
    return doctest.testmod(Cookie)


if __name__ == b'__main__':
    _test()
