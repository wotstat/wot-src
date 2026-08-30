import re
__all__ = [
 2, 3, 4, 5, 
 6, 7, 8, 9]
uses_relative = [
 10, 11, 12, 13, 14, 
 15, 16, 17, 18, 19, 
 20, 21, 22, 23, 24, 
 25, 
 26]
uses_netloc = [10, 11, 12, 13, 27, 
 14, 15, 16, 19, 17, 18, 
 28, 20, 21, 22, 29, 
 23, 
 25, 26, 24, 30, 31, 32]
uses_params = [10, 33, 20, 11, 14, 
 17, 18, 21, 22, 34, 35, 
 19, 23, 24, 36]
non_hierarchical = [
 12, 33, 37, 38, 
 27, 15, 14, 28, 34, 35]
uses_query = [11, 15, 14, 17, 18, 19, 
 12, 21, 22, 34, 35, 23]
uses_fragment = [10, 33, 11, 12, 38, 
 13, 15, 17, 18, 28, 
 16, 20, 23]
scheme_chars = b'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-.'
MAX_CACHE_SIZE = 20
_parse_cache = {}

def clear_cache():
    _parse_cache.clear()
    return


class ResultMixin(object):

    @property
    def username(self):
        netloc = self.netloc
        if b'@' in netloc:
            userinfo = netloc.rsplit(b'@', 1)[0]
            if b':' in userinfo:
                userinfo = userinfo.split(b':', 1)[0]
            return userinfo
        return

    @property
    def password(self):
        netloc = self.netloc
        if b'@' in netloc:
            userinfo = netloc.rsplit(b'@', 1)[0]
            if b':' in userinfo:
                return userinfo.split(b':', 1)[1]
        return

    @property
    def hostname(self):
        netloc = self.netloc.split(b'@')[-1]
        if b'[' in netloc and b']' in netloc:
            return netloc.split(b']')[0][1:].lower()
        else:
            if b':' in netloc:
                return netloc.split(b':')[0].lower()
            else:
                if netloc == b'':
                    return
                return netloc.lower()

            return

    @property
    def port(self):
        netloc = self.netloc.split(b'@')[-1].split(b']')[-1]
        if b':' in netloc:
            port = netloc.split(b':')[1]
            if port:
                port = int(port, 10)
                if 0 <= port <= 65535:
                    return port
        return


from collections import namedtuple

class SplitResult(namedtuple(b'SplitResult', b'scheme netloc path query fragment'), ResultMixin):
    __slots__ = ()

    def geturl(self):
        return urlunsplit(self)


class ParseResult(namedtuple(b'ParseResult', b'scheme netloc path params query fragment'), ResultMixin):
    __slots__ = ()

    def geturl(self):
        return urlunparse(self)


def urlparse(url, scheme=b'', allow_fragments=True):
    tuple = urlsplit(url, scheme, allow_fragments)
    scheme, netloc, url, query, fragment = tuple
    if scheme in uses_params and b';' in url:
        url, params = _splitparams(url)
    else:
        params = b''
    return ParseResult(scheme, netloc, url, params, query, fragment)


def _splitparams(url):
    if b'/' in url:
        i = url.find(b';', url.rfind(b'/'))
        if i < 0:
            return (url, b'')
    else:
        i = url.find(b';')
    return (
     url[:i], url[i + 1:])


def _splitnetloc(url, start=0):
    delim = len(url)
    for c in b'/?#':
        wdelim = url.find(c, start)
        if wdelim >= 0:
            delim = min(delim, wdelim)

    return (
     url[start:delim], url[delim:])


def _checknetloc(netloc):
    if not netloc or not isinstance(netloc, unicode):
        return
    import unicodedata
    n = netloc.replace(u'@', u'')
    n = n.replace(u':', u'')
    n = n.replace(u'#', u'')
    n = n.replace(u'?', u'')
    netloc2 = unicodedata.normalize(b'NFKC', n)
    if n == netloc2:
        return
    for c in b'/?#@:':
        if c in netloc2:
            raise ValueError(b'netloc %r contains invalid characters under NFKC normalization' % netloc)

    return


def urlsplit(url, scheme=b'', allow_fragments=True):
    allow_fragments = bool(allow_fragments)
    key = (url, scheme, allow_fragments, type(url), type(scheme))
    cached = _parse_cache.get(key, None)
    if cached:
        return cached
    else:
        if len(_parse_cache) >= MAX_CACHE_SIZE:
            clear_cache()
        netloc = query = fragment = b''
        i = url.find(b':')
        if i > 0:
            if url[:i] == b'http':
                scheme = url[:i].lower()
                url = url[i + 1:]
                if url[:2] == b'//':
                    netloc, url = _splitnetloc(url, 2)
                    if b'[' in netloc and b']' not in netloc or b']' in netloc and b'[' not in netloc:
                        raise ValueError(b'Invalid IPv6 URL')
                if allow_fragments and b'#' in url:
                    url, fragment = url.split(b'#', 1)
                if b'?' in url:
                    url, query = url.split(b'?', 1)
                _checknetloc(netloc)
                v = SplitResult(scheme, netloc, url, query, fragment)
                _parse_cache[key] = v
                return v
            for c in url[:i]:
                if c not in scheme_chars:
                    break
            else:
                rest = url[i + 1:]
                if not rest or any(c not in b'0123456789' for c in rest):
                    scheme, url = url[:i].lower(), rest
        if url[:2] == b'//':
            netloc, url = _splitnetloc(url, 2)
            if b'[' in netloc and b']' not in netloc or b']' in netloc and b'[' not in netloc:
                raise ValueError(b'Invalid IPv6 URL')
        if allow_fragments and b'#' in url:
            url, fragment = url.split(b'#', 1)
        if b'?' in url:
            url, query = url.split(b'?', 1)
        _checknetloc(netloc)
        v = SplitResult(scheme, netloc, url, query, fragment)
        _parse_cache[key] = v
        return v


def urlunparse(data):
    scheme, netloc, url, params, query, fragment = data
    if params:
        url = b'%s;%s' % (url, params)
    return urlunsplit((scheme, netloc, url, query, fragment))


def urlunsplit(data):
    scheme, netloc, url, query, fragment = data
    if netloc or scheme and scheme in uses_netloc and url[:2] != b'//':
        if url and url[:1] != b'/':
            url = b'/' + url
        url = b'//' + (netloc or b'') + url
    if scheme:
        url = scheme + b':' + url
    if query:
        url = url + b'?' + query
    if fragment:
        url = url + b'#' + fragment
    return url


def urljoin(base, url, allow_fragments=True):
    if not base:
        return url
    if not url:
        return base
    bscheme, bnetloc, bpath, bparams, bquery, bfragment = urlparse(base, b'', allow_fragments)
    scheme, netloc, path, params, query, fragment = urlparse(url, bscheme, allow_fragments)
    if scheme != bscheme or scheme not in uses_relative:
        return url
    if scheme in uses_netloc:
        if netloc:
            return urlunparse((scheme, netloc, path,
             params, query, fragment))
        netloc = bnetloc
    if path[:1] == b'/':
        return urlunparse((scheme, netloc, path,
         params, query, fragment))
    if not path and not params:
        path = bpath
        params = bparams
        if not query:
            query = bquery
        return urlunparse((scheme, netloc, path,
         params, query, fragment))
    segments = bpath.split(b'/')[:-1] + path.split(b'/')
    if segments[-1] == b'.':
        segments[-1] = b''
    while b'.' in segments:
        segments.remove(b'.')

    while 1:
        i = 1
        n = len(segments) - 1
        while 1:
            if i < n:
                if segments[i] == b'..' and segments[i - 1] not in (b'', b'..'):
                    del segments[i - 1:i + 1]
                    break
                i = i + 1
        else:
            break

    if segments == [b'', b'..']:
        segments[-1] = b''
    elif len(segments) >= 2 and segments[-1] == b'..':
        segments[(-2):] = [
         b'']
    return urlunparse((scheme, netloc, (b'/').join(segments),
     params, query, fragment))


def urldefrag(url):
    if b'#' in url:
        s, n, p, a, q, frag = urlparse(url)
        defrag = urlunparse((s, n, p, a, q, b''))
        return (
         defrag, frag)
    else:
        return (
         url, b'')

    return


try:
    unicode
except NameError:

    def _is_unicode(x):
        return 0


else:

    def _is_unicode(x):
        return isinstance(x, unicode)


_hexdig = b'0123456789ABCDEFabcdef'
_hextochr = dict((a + b, chr(int(a + b, 16))) for a in _hexdig for b in _hexdig)
_asciire = re.compile(b'([\x00-\x7f]+)')

def unquote(s):
    if _is_unicode(s):
        if b'%' not in s:
            return s
        bits = _asciire.split(s)
        res = [bits[0]]
        append = res.append
        for i in range(1, len(bits), 2):
            append(unquote(str(bits[i])).decode(b'latin1'))
            append(bits[i + 1])

        return (b'').join(res)
    bits = s.split(b'%')
    if len(bits) == 1:
        return s
    res = [
     bits[0]]
    append = res.append
    for item in bits[1:]:
        try:
            append(_hextochr[item[:2]])
            append(item[2:])
        except KeyError:
            append(b'%')
            append(item)

    return (b'').join(res)


def parse_qs(qs, keep_blank_values=0, strict_parsing=0, max_num_fields=None):
    dict = {}
    for name, value in parse_qsl(qs, keep_blank_values, strict_parsing, max_num_fields):
        if name in dict:
            dict[name].append(value)
        else:
            dict[name] = [
             value]

    return dict


def parse_qsl(qs, keep_blank_values=0, strict_parsing=0, max_num_fields=None):
    if max_num_fields is not None:
        num_fields = 1 + qs.count(b'&') + qs.count(b';')
        if max_num_fields < num_fields:
            raise ValueError(b'Max number of fields exceeded')
    pairs = [s2 for s1 in qs.split(b'&') for s2 in s1.split(b';')]
    r = []
    for name_value in pairs:
        if not name_value and not strict_parsing:
            continue
        nv = name_value.split(b'=', 1)
        if len(nv) != 2:
            if strict_parsing:
                raise ValueError, b'bad query field: %r' % (name_value,)
            if keep_blank_values:
                nv.append(b'')
            else:
                continue
        if len(nv[1]) or keep_blank_values:
            name = unquote(nv[0].replace(b'+', b' '))
            value = unquote(nv[1].replace(b'+', b' '))
            r.append((name, value))

    return r
