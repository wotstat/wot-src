__all__ = [
 0, 1, 2, 3, 
 4, 5, 6, 7, 
 8]
import re, urlparse, copy, time, urllib
try:
    import threading as _threading
except ImportError:
    import dummy_threading as _threading

import httplib
from calendar import timegm
debug = False
logger = None

def _debug(*args):
    global logger
    if not debug:
        return
    if not logger:
        import logging
        logger = logging.getLogger(b'cookielib')
    return logger.debug(*args)


DEFAULT_HTTP_PORT = str(httplib.HTTP_PORT)
MISSING_FILENAME_TEXT = b'a filename was not supplied (nor was the CookieJar instance initialised with one)'

def _warn_unhandled_exception():
    import warnings, traceback, StringIO
    f = StringIO.StringIO()
    traceback.print_exc(None, f)
    msg = f.getvalue()
    warnings.warn(b'cookielib bug!\n%s' % msg, stacklevel=2)
    return


EPOCH_YEAR = 1970

def _timegm(tt):
    year, month, mday, hour, min, sec = tt[:6]
    if year >= EPOCH_YEAR and 1 <= month <= 12 and 1 <= mday <= 31 and 0 <= hour <= 24 and 0 <= min <= 59 and 0 <= sec <= 61:
        return timegm(tt)
    else:
        return
        return


DAYS = [
 17, 18, 19, 20, 21, 22, 23]
MONTHS = [24, 25, 26, 27, 28, 29, 
 30, 31, 32, 33, 34, 35]
MONTHS_LOWER = []
for month in MONTHS:
    MONTHS_LOWER.append(month.lower())

def time2isoz(t=None):
    if t is None:
        t = time.time()
    year, mon, mday, hour, min, sec = time.gmtime(t)[:6]
    return b'%04d-%02d-%02d %02d:%02d:%02dZ' % (
     year, mon, mday, hour, min, sec)


def time2netscape(t=None):
    if t is None:
        t = time.time()
    year, mon, mday, hour, min, sec, wday = time.gmtime(t)[:7]
    return b'%s, %02d-%s-%04d %02d:%02d:%02d GMT' % (
     DAYS[wday], mday, MONTHS[mon - 1], year, hour, min, sec)


UTC_ZONES = {b'GMT': None, b'UTC': None, b'UT': None, b'Z': None}
TIMEZONE_RE = re.compile(b'^([-+])?(\\d\\d?):?(\\d\\d)?$')

def offset_from_tz_string(tz):
    offset = None
    if tz in UTC_ZONES:
        offset = 0
    else:
        m = TIMEZONE_RE.search(tz)
        if m:
            offset = 3600 * int(m.group(2))
            if m.group(3):
                offset = offset + 60 * int(m.group(3))
            if m.group(1) == b'-':
                offset = -offset
    return offset


def _str2time(day, mon, yr, hr, min, sec, tz):
    try:
        mon = MONTHS_LOWER.index(mon.lower()) + 1
    except ValueError:
        try:
            imon = int(mon)
        except ValueError:
            return

        if 1 <= imon <= 12:
            mon = imon
        else:
            return

    if hr is None:
        hr = 0
    if min is None:
        min = 0
    if sec is None:
        sec = 0
    yr = int(yr)
    day = int(day)
    hr = int(hr)
    min = int(min)
    sec = int(sec)
    if yr < 1000:
        cur_yr = time.localtime(time.time())[0]
        m = cur_yr % 100
        tmp = yr
        yr = yr + cur_yr - m
        m = m - tmp
        if abs(m) > 50:
            if m > 0:
                yr = yr + 100
            else:
                yr = yr - 100
    t = _timegm((yr, mon, day, hr, min, sec, tz))
    if t is not None:
        if tz is None:
            tz = b'UTC'
        tz = tz.upper()
        offset = offset_from_tz_string(tz)
        if offset is None:
            return
        t = t - offset
    return t


STRICT_DATE_RE = re.compile(b'^[SMTWF][a-z][a-z], (\\d\\d) ([JFMASOND][a-z][a-z]) (\\d\\d\\d\\d) (\\d\\d):(\\d\\d):(\\d\\d) GMT$')
WEEKDAY_RE = re.compile(b'^(?:Sun|Mon|Tue|Wed|Thu|Fri|Sat)[a-z]*,?\\s*', re.I)
LOOSE_HTTP_DATE_RE = re.compile(b'^\n    (\\d\\d?)            # day\n       (?:\\s+|[-\\/])\n    (\\w+)              # month\n        (?:\\s+|[-\\/])\n    (\\d+)              # year\n    (?:\n          (?:\\s+|:)    # separator before clock\n       (\\d\\d?):(\\d\\d)  # hour:min\n       (?::(\\d\\d))?    # optional seconds\n    )?                 # optional clock\n       \\s*\n    (?:\n       ([-+]?\\d{2,4}|(?![APap][Mm]\\b)[A-Za-z]+) # timezone\n       \\s*\n    )?\n    (?:\n       \\(\\w+\\)         # ASCII representation of timezone in parens.\n       \\s*\n    )?$', re.X)

def http2time(text):
    m = STRICT_DATE_RE.search(text)
    if m:
        g = m.groups()
        mon = MONTHS_LOWER.index(g[1].lower()) + 1
        tt = (int(g[2]), mon, int(g[0]),
         int(g[3]), int(g[4]), float(g[5]))
        return _timegm(tt)
    else:
        text = text.lstrip()
        text = WEEKDAY_RE.sub(b'', text, 1)
        day, mon, yr, hr, min, sec, tz = [
         None] * 7
        m = LOOSE_HTTP_DATE_RE.search(text)
        if m is not None:
            day, mon, yr, hr, min, sec, tz = m.groups()
        else:
            return
        return _str2time(day, mon, yr, hr, min, sec, tz)


ISO_DATE_RE = re.compile(b'^\n    (\\d{4})              # year\n       [-\\/]?\n    (\\d\\d?)              # numerical month\n       [-\\/]?\n    (\\d\\d?)              # day\n   (?:\n         (?:\\s+|[-:Tt])  # separator before clock\n      (\\d\\d?):?(\\d\\d)    # hour:min\n      (?::?(\\d\\d(?:\\.\\d*)?))?  # optional seconds (and fractional)\n   )?                    # optional clock\n      \\s*\n   (?:\n      ([-+]?\\d\\d?:?(:?\\d\\d)?\n       |Z|z)             # timezone  (Z is "zero meridian", i.e. GMT)\n      \\s*\n   )?$', re.X)

def iso2time(text):
    text = text.lstrip()
    day, mon, yr, hr, min, sec, tz = [
     None] * 7
    m = ISO_DATE_RE.search(text)
    if m is not None:
        yr, mon, day, hr, min, sec, tz, _ = m.groups()
    else:
        return
    return _str2time(day, mon, yr, hr, min, sec, tz)


def unmatched(match):
    start, end = match.span(0)
    return match.string[:start] + match.string[end:]


HEADER_TOKEN_RE = re.compile(b'^\\s*([^=\\s;,]+)')
HEADER_QUOTED_VALUE_RE = re.compile(b'^\\s*=\\s*\\"([^\\"\\\\]*(?:\\\\.[^\\"\\\\]*)*)\\"')
HEADER_VALUE_RE = re.compile(b'^\\s*=\\s*([^\\s;,]*)')
HEADER_ESCAPE_RE = re.compile(b'\\\\(.)')

def split_header_words(header_values):
    result = []
    for text in header_values:
        orig_text = text
        pairs = []
        while text:
            m = HEADER_TOKEN_RE.search(text)
            if m:
                text = unmatched(m)
                name = m.group(1)
                m = HEADER_QUOTED_VALUE_RE.search(text)
                if m:
                    text = unmatched(m)
                    value = m.group(1)
                    value = HEADER_ESCAPE_RE.sub(b'\\1', value)
                else:
                    m = HEADER_VALUE_RE.search(text)
                    if m:
                        text = unmatched(m)
                        value = m.group(1)
                        value = value.rstrip()
                    else:
                        value = None
                pairs.append((name, value))
            elif text.lstrip().startswith(b','):
                text = text.lstrip()[1:]
                if pairs:
                    result.append(pairs)
                pairs = []
            else:
                non_junk, nr_junk_chars = re.subn(b'^[=\\s;]*', b'', text)
                text = non_junk

        if pairs:
            result.append(pairs)

    return result


HEADER_JOIN_ESCAPE_RE = re.compile(b'([\\"\\\\])')

def join_header_words(lists):
    headers = []
    for pairs in lists:
        attr = []
        for k, v in pairs:
            if v is not None:
                if not re.search(b'^\\w+$', v):
                    v = HEADER_JOIN_ESCAPE_RE.sub(b'\\\\\\1', v)
                    v = b'"%s"' % v
                k = b'%s=%s' % (k, v)
            attr.append(k)

        if attr:
            headers.append((b'; ').join(attr))

    return (b', ').join(headers)


def _strip_quotes(text):
    if text.startswith(b'"'):
        text = text[1:]
    if text.endswith(b'"'):
        text = text[:-1]
    return text


def parse_ns_headers(ns_headers):
    known_attrs = (b'expires', b'domain', b'path', b'secure', b'version', b'port', b'max-age')
    result = []
    for ns_header in ns_headers:
        pairs = []
        version_set = False
        for ii, param in enumerate(ns_header.split(b';')):
            param = param.strip()
            key, sep, val = param.partition(b'=')
            key = key.strip()
            if not key:
                if ii == 0:
                    break
                else:
                    continue
            val = val.strip() if sep else None
            if ii != 0:
                lc = key.lower()
                if lc in known_attrs:
                    key = lc
                if key == b'version':
                    if val is not None:
                        val = _strip_quotes(val)
                    version_set = True
                elif key == b'expires':
                    if val is not None:
                        val = http2time(_strip_quotes(val))
            pairs.append((key, val))

        if pairs:
            if not version_set:
                pairs.append((b'version', b'0'))
            result.append(pairs)

    return result


IPV4_RE = re.compile(b'\\.\\d+$')

def is_HDN(text):
    if IPV4_RE.search(text):
        return False
    if text == b'':
        return False
    if text[0] == b'.' or text[-1] == b'.':
        return False
    return True


def domain_match(A, B):
    A = A.lower()
    B = B.lower()
    if A == B:
        return True
    if not is_HDN(A):
        return False
    i = A.rfind(B)
    if i == -1 or i == 0:
        return False
    if not B.startswith(b'.'):
        return False
    if not is_HDN(B[1:]):
        return False
    return True


def liberal_is_HDN(text):
    if IPV4_RE.search(text):
        return False
    return True


def user_domain_match(A, B):
    A = A.lower()
    B = B.lower()
    if not (liberal_is_HDN(A) and liberal_is_HDN(B)):
        if A == B:
            return True
        return False
    initial_dot = B.startswith(b'.')
    if initial_dot and A.endswith(B):
        return True
    if not initial_dot and A == B:
        return True
    return False


cut_port_re = re.compile(b':\\d+$')

def request_host(request):
    url = request.get_full_url()
    host = urlparse.urlparse(url)[1]
    if host == b'':
        host = request.get_header(b'Host', b'')
    host = cut_port_re.sub(b'', host, 1)
    return host.lower()


def eff_request_host(request):
    erhn = req_host = request_host(request)
    if req_host.find(b'.') == -1 and not IPV4_RE.search(req_host):
        erhn = req_host + b'.local'
    return (
     req_host, erhn)


def request_path(request):
    url = request.get_full_url()
    parts = urlparse.urlsplit(url)
    path = escape_path(parts.path)
    if not path.startswith(b'/'):
        path = b'/' + path
    return path


def request_port(request):
    host = request.get_host()
    i = host.find(b':')
    if i >= 0:
        port = host[i + 1:]
        try:
            int(port)
        except ValueError:
            _debug(b"nonnumeric port: '%s'", port)
            return

    else:
        port = DEFAULT_HTTP_PORT
    return port


HTTP_PATH_SAFE = b"%/;:@&=+$,!~*'()"
ESCAPED_CHAR_RE = re.compile(b'%([0-9a-fA-F][0-9a-fA-F])')

def uppercase_escaped_char(match):
    return b'%%%s' % match.group(1).upper()


def escape_path(path):
    if isinstance(path, unicode):
        path = path.encode(b'utf-8')
    path = urllib.quote(path, HTTP_PATH_SAFE)
    path = ESCAPED_CHAR_RE.sub(uppercase_escaped_char, path)
    return path


def reach(h):
    i = h.find(b'.')
    if i >= 0:
        b = h[i + 1:]
        i = b.find(b'.')
        if is_HDN(h) and (i >= 0 or b == b'local'):
            return b'.' + b
    return h


def is_third_party(request):
    req_host = request_host(request)
    if not domain_match(req_host, reach(request.get_origin_req_host())):
        return True
    else:
        return False

    return


class Cookie():

    def __init__(self, version, name, value, port, port_specified, domain, domain_specified, domain_initial_dot, path, path_specified, secure, expires, discard, comment, comment_url, rest, rfc2109=False):
        if version is not None:
            version = int(version)
        if expires is not None:
            expires = int(expires)
        if port is None and port_specified is True:
            raise ValueError(b'if port is None, port_specified must be false')
        self.version = version
        self.name = name
        self.value = value
        self.port = port
        self.port_specified = port_specified
        self.domain = domain.lower()
        self.domain_specified = domain_specified
        self.domain_initial_dot = domain_initial_dot
        self.path = path
        self.path_specified = path_specified
        self.secure = secure
        self.expires = expires
        self.discard = discard
        self.comment = comment
        self.comment_url = comment_url
        self.rfc2109 = rfc2109
        self._rest = copy.copy(rest)
        return

    def has_nonstandard_attr(self, name):
        return name in self._rest

    def get_nonstandard_attr(self, name, default=None):
        return self._rest.get(name, default)

    def set_nonstandard_attr(self, name, value):
        self._rest[name] = value
        return

    def is_expired(self, now=None):
        if now is None:
            now = time.time()
        if self.expires is not None and self.expires <= now:
            return True
        else:
            return False

    def __str__(self):
        if self.port is None:
            p = b''
        else:
            p = b':' + self.port
        limit = self.domain + p + self.path
        if self.value is not None:
            namevalue = b'%s=%s' % (self.name, self.value)
        else:
            namevalue = self.name
        return b'<Cookie %s for %s>' % (namevalue, limit)

    def __repr__(self):
        args = []
        for name in (b'version', b'name', b'value', b'port', b'port_specified', b'domain', b'domain_specified', b'domain_initial_dot', b'path', b'path_specified', b'secure', b'expires', b'discard', b'comment', b'comment_url'):
            attr = getattr(self, name)
            args.append(b'%s=%s' % (name, repr(attr)))

        args.append(b'rest=%s' % repr(self._rest))
        args.append(b'rfc2109=%s' % repr(self.rfc2109))
        return b'Cookie(%s)' % (b', ').join(args)


class CookiePolicy():

    def set_ok(self, cookie, request):
        raise NotImplementedError()
        return

    def return_ok(self, cookie, request):
        raise NotImplementedError()
        return

    def domain_return_ok(self, domain, request):
        return True

    def path_return_ok(self, path, request):
        return True


class DefaultCookiePolicy(CookiePolicy):
    DomainStrictNoDots = 1
    DomainStrictNonDomain = 2
    DomainRFC2965Match = 4
    DomainLiberal = 0
    DomainStrict = DomainStrictNoDots | DomainStrictNonDomain

    def __init__(self, blocked_domains=None, allowed_domains=None, netscape=True, rfc2965=False, rfc2109_as_netscape=None, hide_cookie2=False, strict_domain=False, strict_rfc2965_unverifiable=True, strict_ns_unverifiable=False, strict_ns_domain=DomainLiberal, strict_ns_set_initial_dollar=False, strict_ns_set_path=False):
        self.netscape = netscape
        self.rfc2965 = rfc2965
        self.rfc2109_as_netscape = rfc2109_as_netscape
        self.hide_cookie2 = hide_cookie2
        self.strict_domain = strict_domain
        self.strict_rfc2965_unverifiable = strict_rfc2965_unverifiable
        self.strict_ns_unverifiable = strict_ns_unverifiable
        self.strict_ns_domain = strict_ns_domain
        self.strict_ns_set_initial_dollar = strict_ns_set_initial_dollar
        self.strict_ns_set_path = strict_ns_set_path
        if blocked_domains is not None:
            self._blocked_domains = tuple(blocked_domains)
        else:
            self._blocked_domains = ()
        if allowed_domains is not None:
            allowed_domains = tuple(allowed_domains)
        self._allowed_domains = allowed_domains
        return

    def blocked_domains(self):
        return self._blocked_domains

    def set_blocked_domains(self, blocked_domains):
        self._blocked_domains = tuple(blocked_domains)
        return

    def is_blocked(self, domain):
        for blocked_domain in self._blocked_domains:
            if user_domain_match(domain, blocked_domain):
                return True

        return False

    def allowed_domains(self):
        return self._allowed_domains

    def set_allowed_domains(self, allowed_domains):
        if allowed_domains is not None:
            allowed_domains = tuple(allowed_domains)
        self._allowed_domains = allowed_domains
        return

    def is_not_allowed(self, domain):
        if self._allowed_domains is None:
            return False
        else:
            for allowed_domain in self._allowed_domains:
                if user_domain_match(domain, allowed_domain):
                    return False

            return True

    def set_ok(self, cookie, request):
        _debug(b' - checking cookie %s=%s', cookie.name, cookie.value)
        for n in (b'version', b'verifiability', b'name', b'path', b'domain', b'port'):
            fn_name = b'set_ok_' + n
            fn = getattr(self, fn_name)
            if not fn(cookie, request):
                return False

        return True

    def set_ok_version(self, cookie, request):
        if cookie.version is None:
            _debug(b'   Set-Cookie2 without version attribute (%s=%s)', cookie.name, cookie.value)
            return False
        else:
            if cookie.version > 0 and not self.rfc2965:
                _debug(b'   RFC 2965 cookies are switched off')
                return False
            if cookie.version == 0 and not self.netscape:
                _debug(b'   Netscape cookies are switched off')
                return False
            return True

    def set_ok_verifiability(self, cookie, request):
        if request.is_unverifiable() and is_third_party(request):
            if cookie.version > 0 and self.strict_rfc2965_unverifiable:
                _debug(b'   third-party RFC 2965 cookie during unverifiable transaction')
                return False
            if cookie.version == 0 and self.strict_ns_unverifiable:
                _debug(b'   third-party Netscape cookie during unverifiable transaction')
                return False
        return True

    def set_ok_name(self, cookie, request):
        if cookie.version == 0 and self.strict_ns_set_initial_dollar and cookie.name.startswith(b'$'):
            _debug(b"   illegal name (starts with '$'): '%s'", cookie.name)
            return False
        return True

    def set_ok_path(self, cookie, request):
        if cookie.path_specified:
            req_path = request_path(request)
            if (cookie.version > 0 or cookie.version == 0 and self.strict_ns_set_path) and not self.path_return_ok(cookie.path, request):
                _debug(b'   path attribute %s is not a prefix of request path %s', cookie.path, req_path)
                return False
        return True

    def set_ok_domain(self, cookie, request):
        if self.is_blocked(cookie.domain):
            _debug(b'   domain %s is in user block-list', cookie.domain)
            return False
        if self.is_not_allowed(cookie.domain):
            _debug(b'   domain %s is not in user allow-list', cookie.domain)
            return False
        if cookie.domain_specified:
            req_host, erhn = eff_request_host(request)
            domain = cookie.domain
            if self.strict_domain and domain.count(b'.') >= 2:
                i = domain.rfind(b'.')
                j = domain.rfind(b'.', 0, i)
                if j == 0:
                    tld = domain[i + 1:]
                    sld = domain[j + 1:i]
                    if sld.lower() in (b'co', b'ac', b'com', b'edu', b'org', b'net', b'gov', b'mil', b'int', b'aero', b'biz', b'cat', b'coop', b'info', b'jobs', b'mobi', b'museum', b'name', b'pro', b'travel', b'eu') and len(tld) == 2:
                        _debug(b'   country-code second level domain %s', domain)
                        return False
            if domain.startswith(b'.'):
                undotted_domain = domain[1:]
            else:
                undotted_domain = domain
            embedded_dots = undotted_domain.find(b'.') >= 0
            if not embedded_dots and domain != b'.local':
                _debug(b'   non-local domain %s contains no embedded dot', domain)
                return False
            if cookie.version == 0 and not erhn.endswith(domain) and not erhn.startswith(b'.'):
                if not (b'.' + erhn).endswith(domain):
                    _debug(b'   effective request-host %s (even with added initial dot) does not end with %s', erhn, domain)
                    return False
            if cookie.version > 0 or self.strict_ns_domain & self.DomainRFC2965Match:
                if not domain_match(erhn, domain):
                    _debug(b'   effective request-host %s does not domain-match %s', erhn, domain)
                    return False
            if cookie.version > 0 or self.strict_ns_domain & self.DomainStrictNoDots:
                host_prefix = req_host[:-len(domain)]
                if host_prefix.find(b'.') >= 0 and not IPV4_RE.search(req_host):
                    _debug(b'   host prefix %s for domain %s contains a dot', host_prefix, domain)
                    return False
        return True

    def set_ok_port(self, cookie, request):
        if cookie.port_specified:
            req_port = request_port(request)
            if req_port is None:
                req_port = b'80'
            else:
                req_port = str(req_port)
            for p in cookie.port.split(b','):
                try:
                    int(p)
                except ValueError:
                    _debug(b'   bad port %s (not numeric)', p)
                    return False

                if p == req_port:
                    break
            else:
                _debug(b'   request port (%s) not found in %s', req_port, cookie.port)
                return False

        return True

    def return_ok(self, cookie, request):
        _debug(b' - checking cookie %s=%s', cookie.name, cookie.value)
        for n in (b'version', b'verifiability', b'secure', b'expires', b'port', b'domain'):
            fn_name = b'return_ok_' + n
            fn = getattr(self, fn_name)
            if not fn(cookie, request):
                return False

        return True

    def return_ok_version(self, cookie, request):
        if cookie.version > 0 and not self.rfc2965:
            _debug(b'   RFC 2965 cookies are switched off')
            return False
        if cookie.version == 0 and not self.netscape:
            _debug(b'   Netscape cookies are switched off')
            return False
        return True

    def return_ok_verifiability(self, cookie, request):
        if request.is_unverifiable() and is_third_party(request):
            if cookie.version > 0 and self.strict_rfc2965_unverifiable:
                _debug(b'   third-party RFC 2965 cookie during unverifiable transaction')
                return False
            if cookie.version == 0 and self.strict_ns_unverifiable:
                _debug(b'   third-party Netscape cookie during unverifiable transaction')
                return False
        return True

    def return_ok_secure(self, cookie, request):
        if cookie.secure and request.get_type() != b'https':
            _debug(b'   secure cookie with non-secure request')
            return False
        return True

    def return_ok_expires(self, cookie, request):
        if cookie.is_expired(self._now):
            _debug(b'   cookie expired')
            return False
        return True

    def return_ok_port(self, cookie, request):
        if cookie.port:
            req_port = request_port(request)
            if req_port is None:
                req_port = b'80'
            for p in cookie.port.split(b','):
                if p == req_port:
                    break
            else:
                _debug(b'   request port %s does not match cookie port %s', req_port, cookie.port)
                return False

        return True

    def return_ok_domain(self, cookie, request):
        req_host, erhn = eff_request_host(request)
        domain = cookie.domain
        if domain and not domain.startswith(b'.'):
            dotdomain = b'.' + domain
        else:
            dotdomain = domain
        if cookie.version == 0 and self.strict_ns_domain & self.DomainStrictNonDomain and not cookie.domain_specified and domain != erhn:
            _debug(b'   cookie with unspecified domain does not string-compare equal to request domain')
            return False
        if cookie.version > 0 and not domain_match(erhn, domain):
            _debug(b'   effective request-host name %s does not domain-match RFC 2965 cookie domain %s', erhn, domain)
            return False
        if cookie.version == 0 and not (b'.' + erhn).endswith(dotdomain):
            _debug(b'   request-host %s does not match Netscape cookie domain %s', req_host, domain)
            return False
        return True

    def domain_return_ok(self, domain, request):
        req_host, erhn = eff_request_host(request)
        if not req_host.startswith(b'.'):
            req_host = b'.' + req_host
        if not erhn.startswith(b'.'):
            erhn = b'.' + erhn
        if domain and not domain.startswith(b'.'):
            dotdomain = b'.' + domain
        else:
            dotdomain = domain
        if not (req_host.endswith(dotdomain) or erhn.endswith(dotdomain)):
            return False
        if self.is_blocked(domain):
            _debug(b'   domain %s is in user block-list', domain)
            return False
        if self.is_not_allowed(domain):
            _debug(b'   domain %s is not in user allow-list', domain)
            return False
        return True

    def path_return_ok(self, path, request):
        _debug(b'- checking cookie path=%s', path)
        req_path = request_path(request)
        pathlen = len(path)
        if req_path == path:
            return True
        if req_path.startswith(path) and (path.endswith(b'/') or req_path[pathlen:pathlen + 1] == b'/'):
            return True
        _debug(b'  %s does not path-match %s', req_path, path)
        return False


def vals_sorted_by_key(adict):
    keys = adict.keys()
    keys.sort()
    return map(adict.get, keys)


def deepvalues(mapping):
    values = vals_sorted_by_key(mapping)
    for obj in values:
        mapping = False
        try:
            obj.items
        except AttributeError:
            pass
        else:
            mapping = True
            for subobj in deepvalues(obj):
                yield subobj

            if not mapping:
                yield obj

    return


class Absent():
    pass


class CookieJar():
    non_word_re = re.compile(b'\\W')
    quote_re = re.compile(b'([\\"\\\\])')
    strict_domain_re = re.compile(b'\\.?[^.]*')
    domain_re = re.compile(b'[^.]*')
    dots_re = re.compile(b'^\\.+')
    magic_re = b'^\\#LWP-Cookies-(\\d+\\.\\d+)'

    def __init__(self, policy=None):
        if policy is None:
            policy = DefaultCookiePolicy()
        self._policy = policy
        self._cookies_lock = _threading.RLock()
        self._cookies = {}
        return

    def set_policy(self, policy):
        self._policy = policy
        return

    def _cookies_for_domain(self, domain, request):
        cookies = []
        if not self._policy.domain_return_ok(domain, request):
            return []
        _debug(b'Checking %s for cookies to return', domain)
        cookies_by_path = self._cookies[domain]
        for path in cookies_by_path.keys():
            if not self._policy.path_return_ok(path, request):
                continue
            cookies_by_name = cookies_by_path[path]
            for cookie in cookies_by_name.values():
                if not self._policy.return_ok(cookie, request):
                    _debug(b'   not returning cookie')
                    continue
                _debug(b"   it's a match")
                cookies.append(cookie)

        return cookies

    def _cookies_for_request(self, request):
        cookies = []
        for domain in self._cookies.keys():
            cookies.extend(self._cookies_for_domain(domain, request))

        return cookies

    def _cookie_attrs(self, cookies):
        cookies.sort(key=(lambda arg: len(arg.path)), reverse=True)
        version_set = False
        attrs = []
        for cookie in cookies:
            version = cookie.version
            if not version_set:
                version_set = True
                if version > 0:
                    attrs.append(b'$Version=%s' % version)
            if cookie.value is not None and self.non_word_re.search(cookie.value) and version > 0:
                value = self.quote_re.sub(b'\\\\\\1', cookie.value)
            else:
                value = cookie.value
            if cookie.value is None:
                attrs.append(cookie.name)
            else:
                attrs.append(b'%s=%s' % (cookie.name, value))
            if version > 0:
                if cookie.path_specified:
                    attrs.append(b'$Path="%s"' % cookie.path)
                if cookie.domain.startswith(b'.'):
                    domain = cookie.domain
                    if not cookie.domain_initial_dot and domain.startswith(b'.'):
                        domain = domain[1:]
                    attrs.append(b'$Domain="%s"' % domain)
                if cookie.port is not None:
                    p = b'$Port'
                    if cookie.port_specified:
                        p = p + b'="%s"' % cookie.port
                    attrs.append(p)

        return attrs

    def add_cookie_header(self, request):
        _debug(b'add_cookie_header')
        self._cookies_lock.acquire()
        try:
            self._policy._now = self._now = int(time.time())
            cookies = self._cookies_for_request(request)
            attrs = self._cookie_attrs(cookies)
            if attrs:
                if not request.has_header(b'Cookie'):
                    request.add_unredirected_header(b'Cookie', (b'; ').join(attrs))
            if self._policy.rfc2965 and not self._policy.hide_cookie2 and not request.has_header(b'Cookie2'):
                for cookie in cookies:
                    if cookie.version != 1:
                        request.add_unredirected_header(b'Cookie2', b'$Version="1"')
                        break

        finally:
            self._cookies_lock.release()

        self.clear_expired_cookies()
        return

    def _normalized_cookie_tuples(self, attrs_set):
        cookie_tuples = []
        boolean_attrs = (b'discard', b'secure')
        value_attrs = (b'version', b'expires', b'max-age', b'domain', b'path', b'port', b'comment', b'commenturl')
        for cookie_attrs in attrs_set:
            name, value = cookie_attrs[0]
            max_age_set = False
            bad_cookie = False
            standard = {}
            rest = {}
            for k, v in cookie_attrs[1:]:
                lc = k.lower()
                if lc in value_attrs or lc in boolean_attrs:
                    k = lc
                if k in boolean_attrs and v is None:
                    v = True
                if k in standard:
                    continue
                if k == b'domain':
                    if v is None:
                        _debug(b'   missing value for domain attribute')
                        bad_cookie = True
                        break
                    v = v.lower()
                if k == b'expires':
                    if max_age_set:
                        continue
                    if v is None:
                        _debug(b'   missing or invalid value for expires attribute: treating as session cookie')
                        continue
                if k == b'max-age':
                    max_age_set = True
                    try:
                        v = int(v)
                    except ValueError:
                        _debug(b'   missing or invalid (non-numeric) value for max-age attribute')
                        bad_cookie = True
                        break

                    k = b'expires'
                    v = self._now + v
                if k in value_attrs or k in boolean_attrs:
                    if v is None and k not in (b'port', b'comment', b'commenturl'):
                        _debug(b'   missing value for %s attribute' % k)
                        bad_cookie = True
                        break
                    standard[k] = v
                else:
                    rest[k] = v

            if bad_cookie:
                continue
            cookie_tuples.append((name, value, standard, rest))

        return cookie_tuples

    def _cookie_from_cookie_tuple(self, tup, request):
        name, value, standard, rest = tup
        domain = standard.get(b'domain', Absent)
        path = standard.get(b'path', Absent)
        port = standard.get(b'port', Absent)
        expires = standard.get(b'expires', Absent)
        version = standard.get(b'version', None)
        if version is not None:
            try:
                version = int(version)
            except ValueError:
                return

        secure = standard.get(b'secure', False)
        discard = standard.get(b'discard', False)
        comment = standard.get(b'comment', None)
        comment_url = standard.get(b'commenturl', None)
        if path is not Absent and path != b'':
            path_specified = True
            path = escape_path(path)
        else:
            path_specified = False
            path = request_path(request)
            i = path.rfind(b'/')
            if i != -1:
                if version == 0:
                    path = path[:i]
                else:
                    path = path[:i + 1]
            if len(path) == 0:
                path = b'/'
        domain_specified = domain is not Absent
        domain_initial_dot = False
        if domain_specified:
            domain_initial_dot = bool(domain.startswith(b'.'))
        if domain is Absent:
            req_host, erhn = eff_request_host(request)
            domain = erhn
        elif not domain.startswith(b'.'):
            domain = b'.' + domain
        port_specified = False
        if port is not Absent:
            if port is None:
                port = request_port(request)
            else:
                port_specified = True
                port = re.sub(b'\\s+', b'', port)
        else:
            port = None
        if expires is Absent:
            expires = None
            discard = True
        elif expires <= self._now:
            try:
                self.clear(domain, path, name)
            except KeyError:
                pass

            _debug(b"Expiring cookie, domain='%s', path='%s', name='%s'", domain, path, name)
            return
        return Cookie(version, name, value, port, port_specified, domain, domain_specified, domain_initial_dot, path, path_specified, secure, expires, discard, comment, comment_url, rest)

    def _cookies_from_attrs_set(self, attrs_set, request):
        cookie_tuples = self._normalized_cookie_tuples(attrs_set)
        cookies = []
        for tup in cookie_tuples:
            cookie = self._cookie_from_cookie_tuple(tup, request)
            if cookie:
                cookies.append(cookie)

        return cookies

    def _process_rfc2109_cookies(self, cookies):
        rfc2109_as_ns = getattr(self._policy, b'rfc2109_as_netscape', None)
        if rfc2109_as_ns is None:
            rfc2109_as_ns = not self._policy.rfc2965
        for cookie in cookies:
            if cookie.version == 1:
                cookie.rfc2109 = True
                if rfc2109_as_ns:
                    cookie.version = 0

        return

    def make_cookies(self, response, request):
        headers = response.info()
        rfc2965_hdrs = headers.getheaders(b'Set-Cookie2')
        ns_hdrs = headers.getheaders(b'Set-Cookie')
        rfc2965 = self._policy.rfc2965
        netscape = self._policy.netscape
        if not rfc2965_hdrs and not ns_hdrs or not ns_hdrs and not rfc2965 or not rfc2965_hdrs and not netscape or not netscape and not rfc2965:
            return []
        try:
            cookies = self._cookies_from_attrs_set(split_header_words(rfc2965_hdrs), request)
        except Exception:
            _warn_unhandled_exception()
            cookies = []

        if ns_hdrs and netscape:
            try:
                ns_cookies = self._cookies_from_attrs_set(parse_ns_headers(ns_hdrs), request)
            except Exception:
                _warn_unhandled_exception()
                ns_cookies = []

            self._process_rfc2109_cookies(ns_cookies)
            if rfc2965:
                lookup = {}
                for cookie in cookies:
                    lookup[(cookie.domain, cookie.path, cookie.name)] = None

                def no_matching_rfc2965(ns_cookie, lookup=lookup):
                    key = (ns_cookie.domain, ns_cookie.path, ns_cookie.name)
                    return key not in lookup

                ns_cookies = filter(no_matching_rfc2965, ns_cookies)
            if ns_cookies:
                cookies.extend(ns_cookies)
        return cookies

    def set_cookie_if_ok(self, cookie, request):
        self._cookies_lock.acquire()
        try:
            self._policy._now = self._now = int(time.time())
            if self._policy.set_ok(cookie, request):
                self.set_cookie(cookie)
        finally:
            self._cookies_lock.release()

        return

    def set_cookie(self, cookie):
        c = self._cookies
        self._cookies_lock.acquire()
        try:
            if cookie.domain not in c:
                c[cookie.domain] = {}
            c2 = c[cookie.domain]
            if cookie.path not in c2:
                c2[cookie.path] = {}
            c3 = c2[cookie.path]
            c3[cookie.name] = cookie
        finally:
            self._cookies_lock.release()

        return

    def extract_cookies(self, response, request):
        _debug(b'extract_cookies: %s', response.info())
        self._cookies_lock.acquire()
        try:
            self._policy._now = self._now = int(time.time())
            for cookie in self.make_cookies(response, request):
                if self._policy.set_ok(cookie, request):
                    _debug(b' setting cookie: %s', cookie)
                    self.set_cookie(cookie)

        finally:
            self._cookies_lock.release()

        return

    def clear(self, domain=None, path=None, name=None):
        if name is not None:
            if domain is None or path is None:
                raise ValueError(b'domain and path must be given to remove a cookie by name')
            del self._cookies[domain][path][name]
        elif path is not None:
            if domain is None:
                raise ValueError(b'domain must be given to remove cookies by path')
            del self._cookies[domain][path]
        elif domain is not None:
            del self._cookies[domain]
        else:
            self._cookies = {}
        return

    def clear_session_cookies(self):
        self._cookies_lock.acquire()
        try:
            for cookie in self:
                if cookie.discard:
                    self.clear(cookie.domain, cookie.path, cookie.name)

        finally:
            self._cookies_lock.release()

        return

    def clear_expired_cookies(self):
        self._cookies_lock.acquire()
        try:
            now = time.time()
            for cookie in self:
                if cookie.is_expired(now):
                    self.clear(cookie.domain, cookie.path, cookie.name)

        finally:
            self._cookies_lock.release()

        return

    def __iter__(self):
        return deepvalues(self._cookies)

    def __len__(self):
        i = 0
        for cookie in self:
            i = i + 1

        return i

    def __repr__(self):
        r = []
        for cookie in self:
            r.append(repr(cookie))

        return b'<%s[%s]>' % (self.__class__.__name__, (b', ').join(r))

    def __str__(self):
        r = []
        for cookie in self:
            r.append(str(cookie))

        return b'<%s[%s]>' % (self.__class__.__name__, (b', ').join(r))


class LoadError(IOError):
    pass


class FileCookieJar(CookieJar):

    def __init__(self, filename=None, delayload=False, policy=None):
        CookieJar.__init__(self, policy)
        if filename is not None:
            try:
                filename + b''
            except:
                raise ValueError(b'filename must be string-like')

        self.filename = filename
        self.delayload = bool(delayload)
        return

    def save(self, filename=None, ignore_discard=False, ignore_expires=False):
        raise NotImplementedError()
        return

    def load(self, filename=None, ignore_discard=False, ignore_expires=False):
        if filename is None:
            if self.filename is not None:
                filename = self.filename
            else:
                raise ValueError(MISSING_FILENAME_TEXT)
        f = open(filename)
        try:
            self._really_load(f, filename, ignore_discard, ignore_expires)
        finally:
            f.close()

        return

    def revert(self, filename=None, ignore_discard=False, ignore_expires=False):
        if filename is None:
            if self.filename is not None:
                filename = self.filename
            else:
                raise ValueError(MISSING_FILENAME_TEXT)
        self._cookies_lock.acquire()
        try:
            old_state = copy.deepcopy(self._cookies)
            self._cookies = {}
            try:
                self.load(filename, ignore_discard, ignore_expires)
            except (LoadError, IOError):
                self._cookies = old_state
                raise

        finally:
            self._cookies_lock.release()

        return


from _LWPCookieJar import LWPCookieJar, lwp_cookie_str
from _MozillaCookieJar import MozillaCookieJar
