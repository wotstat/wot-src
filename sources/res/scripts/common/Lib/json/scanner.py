import re
try:
    from _json import make_scanner as c_make_scanner
except ImportError:
    c_make_scanner = None

__all__ = [b'make_scanner']
NUMBER_RE = re.compile(b'(-?(?:0|[1-9]\\d*))(\\.\\d+)?([eE][-+]?\\d+)?', re.VERBOSE | re.MULTILINE | re.DOTALL)

def py_make_scanner(context):
    parse_object = context.parse_object
    parse_array = context.parse_array
    parse_string = context.parse_string
    match_number = NUMBER_RE.match
    encoding = context.encoding
    strict = context.strict
    parse_float = context.parse_float
    parse_int = context.parse_int
    parse_constant = context.parse_constant
    object_hook = context.object_hook
    object_pairs_hook = context.object_pairs_hook

    def _scan_once(string, idx):
        try:
            nextchar = string[idx]
        except IndexError:
            raise StopIteration

        if nextchar == b'"':
            return parse_string(string, idx + 1, encoding, strict)
        else:
            if nextchar == b'{':
                return parse_object((string, idx + 1), encoding, strict, _scan_once, object_hook, object_pairs_hook)
            if nextchar == b'[':
                return parse_array((string, idx + 1), _scan_once)
            if nextchar == b'n' and string[idx:idx + 4] == b'null':
                return (None, idx + 4)
            if nextchar == b't' and string[idx:idx + 4] == b'true':
                return (True, idx + 4)
            if nextchar == b'f' and string[idx:idx + 5] == b'false':
                return (False, idx + 5)
            m = match_number(string, idx)
            if m is not None:
                integer, frac, exp = m.groups()
                if frac or exp:
                    res = parse_float(integer + (frac or b'') + (exp or b''))
                else:
                    res = parse_int(integer)
                return (res, m.end())
            if nextchar == b'N' and string[idx:idx + 3] == b'NaN':
                return (parse_constant(b'NaN'), idx + 3)
            if nextchar == b'I' and string[idx:idx + 8] == b'Infinity':
                return (parse_constant(b'Infinity'), idx + 8)
            if nextchar == b'-' and string[idx:idx + 9] == b'-Infinity':
                return (parse_constant(b'-Infinity'), idx + 9)
            raise StopIteration
            return

    return _scan_once


make_scanner = c_make_scanner or py_make_scanner
