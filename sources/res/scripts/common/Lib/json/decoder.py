import re, sys, struct
from json import scanner
try:
    from _json import scanstring as c_scanstring
except ImportError:
    c_scanstring = None

__all__ = [b'JSONDecoder']
FLAGS = re.VERBOSE | re.MULTILINE | re.DOTALL

def _floatconstants():
    nan, = struct.unpack(b'>d', b'\x7f\xf8\x00\x00\x00\x00\x00\x00')
    inf, = struct.unpack(b'>d', b'\x7f\xf0\x00\x00\x00\x00\x00\x00')
    return (nan, inf, -inf)


NaN, PosInf, NegInf = _floatconstants()

def linecol(doc, pos):
    lineno = doc.count(b'\n', 0, pos) + 1
    if lineno == 1:
        colno = pos + 1
    else:
        colno = pos - doc.rindex(b'\n', 0, pos)
    return (
     lineno, colno)


def errmsg(msg, doc, pos, end=None):
    lineno, colno = linecol(doc, pos)
    if end is None:
        fmt = b'{0}: line {1} column {2} (char {3})'
        return fmt.format(msg, lineno, colno, pos)
    else:
        endlineno, endcolno = linecol(doc, end)
        fmt = b'{0}: line {1} column {2} - line {3} column {4} (char {5} - {6})'
        return fmt.format(msg, lineno, colno, endlineno, endcolno, pos, end)


_CONSTANTS = {b'-Infinity': NegInf, 
   b'Infinity': PosInf, 
   b'NaN': NaN}
STRINGCHUNK = re.compile(b'(.*?)(["\\\\\\x00-\\x1f])', FLAGS)
BACKSLASH = {b'"': u'"', 
   b'\\': u'\\', b'/': u'/', b'b': u'\x08', 
   b'f': u'\x0c', b'n': u'\n', b'r': u'\r', b't': u'\t'}
DEFAULT_ENCODING = b'utf-8'

def _decode_uXXXX(s, pos):
    esc = s[pos + 1:pos + 5]
    if len(esc) == 4 and esc[1] not in b'xX':
        try:
            return int(esc, 16)
        except ValueError:
            pass

    msg = b'Invalid \\uXXXX escape'
    raise ValueError(errmsg(msg, s, pos))
    return


def py_scanstring(s, end, encoding=None, strict=True, _b=BACKSLASH, _m=STRINGCHUNK.match):
    if encoding is None:
        encoding = DEFAULT_ENCODING
    chunks = []
    _append = chunks.append
    begin = end - 1
    while 1:
        chunk = _m(s, end)
        if chunk is None:
            raise ValueError(errmsg(b'Unterminated string starting at', s, begin))
        end = chunk.end()
        content, terminator = chunk.groups()
        if content:
            if not isinstance(content, unicode):
                content = unicode(content, encoding)
            _append(content)
        if terminator == b'"':
            break
        elif terminator != b'\\':
            if strict:
                msg = (b'Invalid control character {0!r} at').format(terminator)
                raise ValueError(errmsg(msg, s, end))
            else:
                _append(terminator)
                continue
        try:
            esc = s[end]
        except IndexError:
            raise ValueError(errmsg(b'Unterminated string starting at', s, begin))

        if esc != b'u':
            try:
                char = _b[esc]
            except KeyError:
                msg = b'Invalid \\escape: ' + repr(esc)
                raise ValueError(errmsg(msg, s, end))

            end += 1
        else:
            uni = _decode_uXXXX(s, end)
            end += 5
            if sys.maxunicode > 65535 and 55296 <= uni <= 56319 and s[end:end + 2] == b'\\u':
                uni2 = _decode_uXXXX(s, end + 1)
                if 56320 <= uni2 <= 57343:
                    uni = 65536 + (uni - 55296 << 10 | uni2 - 56320)
                    end += 6
            char = unichr(uni)
        _append(char)

    return (
     (u'').join(chunks), end)


scanstring = c_scanstring or py_scanstring
WHITESPACE = re.compile(b'[ \\t\\n\\r]*', FLAGS)
WHITESPACE_STR = b' \t\n\r'

def JSONObject(s_and_end, encoding, strict, scan_once, object_hook, object_pairs_hook, _w=WHITESPACE.match, _ws=WHITESPACE_STR):
    s, end = s_and_end
    pairs = []
    pairs_append = pairs.append
    nextchar = s[end:end + 1]
    if nextchar != b'"':
        if nextchar in _ws:
            end = _w(s, end).end()
            nextchar = s[end:end + 1]
        if nextchar == b'}':
            if object_pairs_hook is not None:
                result = object_pairs_hook(pairs)
                return (result, end + 1)
            pairs = {}
            if object_hook is not None:
                pairs = object_hook(pairs)
            return (pairs, end + 1)
        if nextchar != b'"':
            raise ValueError(errmsg(b'Expecting property name enclosed in double quotes', s, end))
    end += 1
    while True:
        key, end = scanstring(s, end, encoding, strict)
        if s[end:end + 1] != b':':
            end = _w(s, end).end()
            if s[end:end + 1] != b':':
                raise ValueError(errmsg(b"Expecting ':' delimiter", s, end))
        end += 1
        try:
            if s[end] in _ws:
                end += 1
                if s[end] in _ws:
                    end = _w(s, end + 1).end()
        except IndexError:
            pass

        try:
            value, end = scan_once(s, end)
        except StopIteration:
            raise ValueError(errmsg(b'Expecting object', s, end))

        pairs_append((key, value))
        try:
            nextchar = s[end]
            if nextchar in _ws:
                end = _w(s, end + 1).end()
                nextchar = s[end]
        except IndexError:
            nextchar = b''

        end += 1
        if nextchar == b'}':
            break
        elif nextchar != b',':
            raise ValueError(errmsg(b"Expecting ',' delimiter", s, end - 1))
        try:
            nextchar = s[end]
            if nextchar in _ws:
                end += 1
                nextchar = s[end]
                if nextchar in _ws:
                    end = _w(s, end + 1).end()
                    nextchar = s[end]
        except IndexError:
            nextchar = b''

        end += 1
        if nextchar != b'"':
            raise ValueError(errmsg(b'Expecting property name enclosed in double quotes', s, end - 1))

    if object_pairs_hook is not None:
        result = object_pairs_hook(pairs)
        return (
         result, end)
    else:
        pairs = dict(pairs)
        if object_hook is not None:
            pairs = object_hook(pairs)
        return (
         pairs, end)


def JSONArray(s_and_end, scan_once, _w=WHITESPACE.match, _ws=WHITESPACE_STR):
    s, end = s_and_end
    values = []
    nextchar = s[end:end + 1]
    if nextchar in _ws:
        end = _w(s, end + 1).end()
        nextchar = s[end:end + 1]
    if nextchar == b']':
        return (values, end + 1)
    _append = values.append
    while True:
        try:
            value, end = scan_once(s, end)
        except StopIteration:
            raise ValueError(errmsg(b'Expecting object', s, end))

        _append(value)
        nextchar = s[end:end + 1]
        if nextchar in _ws:
            end = _w(s, end + 1).end()
            nextchar = s[end:end + 1]
        end += 1
        if nextchar == b']':
            break
        elif nextchar != b',':
            raise ValueError(errmsg(b"Expecting ',' delimiter", s, end))
        try:
            if s[end] in _ws:
                end += 1
                if s[end] in _ws:
                    end = _w(s, end + 1).end()
        except IndexError:
            pass

    return (values, end)


class JSONDecoder(object):

    def __init__(self, encoding=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, strict=True, object_pairs_hook=None):
        self.encoding = encoding
        self.object_hook = object_hook
        self.object_pairs_hook = object_pairs_hook
        self.parse_float = parse_float or float
        self.parse_int = parse_int or int
        self.parse_constant = parse_constant or _CONSTANTS.__getitem__
        self.strict = strict
        self.parse_object = JSONObject
        self.parse_array = JSONArray
        self.parse_string = scanstring
        self.scan_once = scanner.make_scanner(self)
        return

    def decode(self, s, _w=WHITESPACE.match):
        obj, end = self.raw_decode(s, idx=_w(s, 0).end())
        end = _w(s, end).end()
        if end != len(s):
            raise ValueError(errmsg(b'Extra data', s, end, len(s)))
        return obj

    def raw_decode(self, s, idx=0):
        try:
            obj, end = self.scan_once(s, idx)
        except StopIteration:
            raise ValueError(b'No JSON object could be decoded')

        return (
         obj, end)
