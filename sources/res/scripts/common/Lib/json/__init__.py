__version__ = b'2.0.9'
__all__ = [
 1, 2, 3, 4, 
 5, 6]
__author__ = b'Bob Ippolito <bob@redivi.com>'
from .decoder import JSONDecoder
from .encoder import JSONEncoder
_default_encoder = JSONEncoder(skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, indent=None, separators=None, encoding=b'utf-8', default=None)

def dump(obj, fp, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding=b'utf-8', default=None, sort_keys=False, **kw):
    if not skipkeys and ensure_ascii and check_circular and allow_nan and cls is None and indent is None and separators is None and encoding == b'utf-8' and default is None and not sort_keys and not kw:
        iterable = _default_encoder.iterencode(obj)
    elif cls is None:
        cls = JSONEncoder
    iterable = cls(skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, indent=indent, separators=separators, encoding=encoding, default=default, sort_keys=sort_keys, **kw).iterencode(obj)
    for chunk in iterable:
        fp.write(chunk)

    return


def dumps(obj, skipkeys=False, ensure_ascii=True, check_circular=True, allow_nan=True, cls=None, indent=None, separators=None, encoding=b'utf-8', default=None, sort_keys=False, **kw):
    if not skipkeys and ensure_ascii and check_circular and allow_nan and cls is None and indent is None and separators is None and encoding == b'utf-8' and default is None and not sort_keys and not kw:
        return _default_encoder.encode(obj)
    else:
        if cls is None:
            cls = JSONEncoder
        return cls(skipkeys=skipkeys, ensure_ascii=ensure_ascii, check_circular=check_circular, allow_nan=allow_nan, indent=indent, separators=separators, encoding=encoding, default=default, sort_keys=sort_keys, **kw).encode(obj)


_default_decoder = JSONDecoder(encoding=None, object_hook=None, object_pairs_hook=None)

def load(fp, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    return loads(fp.read(), encoding=encoding, cls=cls, object_hook=object_hook, parse_float=parse_float, parse_int=parse_int, parse_constant=parse_constant, object_pairs_hook=object_pairs_hook, **kw)


def loads(s, encoding=None, cls=None, object_hook=None, parse_float=None, parse_int=None, parse_constant=None, object_pairs_hook=None, **kw):
    if cls is None and encoding is None and object_hook is None and parse_int is None and parse_float is None and parse_constant is None and object_pairs_hook is None and not kw:
        return _default_decoder.decode(s)
    else:
        if cls is None:
            cls = JSONDecoder
        if object_hook is not None:
            kw[b'object_hook'] = object_hook
        if object_pairs_hook is not None:
            kw[b'object_pairs_hook'] = object_pairs_hook
        if parse_float is not None:
            kw[b'parse_float'] = parse_float
        if parse_int is not None:
            kw[b'parse_int'] = parse_int
        if parse_constant is not None:
            kw[b'parse_constant'] = parse_constant
        return cls(encoding=encoding, **kw).decode(s)
