import time, re
from cookielib import _warn_unhandled_exception, FileCookieJar, LoadError, Cookie, MISSING_FILENAME_TEXT, join_header_words, split_header_words, iso2time, time2isoz

def lwp_cookie_str(cookie):
    h = [
     (
      cookie.name, cookie.value),
     (
      b'path', cookie.path),
     (
      b'domain', cookie.domain)]
    if cookie.port is not None:
        h.append((b'port', cookie.port))
    if cookie.path_specified:
        h.append((b'path_spec', None))
    if cookie.port_specified:
        h.append((b'port_spec', None))
    if cookie.domain_initial_dot:
        h.append((b'domain_dot', None))
    if cookie.secure:
        h.append((b'secure', None))
    if cookie.expires:
        h.append((b'expires',
         time2isoz(float(cookie.expires))))
    if cookie.discard:
        h.append((b'discard', None))
    if cookie.comment:
        h.append((b'comment', cookie.comment))
    if cookie.comment_url:
        h.append((b'commenturl', cookie.comment_url))
    keys = cookie._rest.keys()
    keys.sort()
    for k in keys:
        h.append((k, str(cookie._rest[k])))

    h.append((b'version', str(cookie.version)))
    return join_header_words([h])


class LWPCookieJar(FileCookieJar):

    def as_lwp_str(self, ignore_discard=True, ignore_expires=True):
        now = time.time()
        r = []
        for cookie in self:
            if not ignore_discard and cookie.discard:
                continue
            if not ignore_expires and cookie.is_expired(now):
                continue
            r.append(b'Set-Cookie3: %s' % lwp_cookie_str(cookie))

        return (b'\n').join(r + [b''])

    def save(self, filename=None, ignore_discard=False, ignore_expires=False):
        if filename is None:
            if self.filename is not None:
                filename = self.filename
            else:
                raise ValueError(MISSING_FILENAME_TEXT)
        f = open(filename, b'w')
        try:
            f.write(b'#LWP-Cookies-2.0\n')
            f.write(self.as_lwp_str(ignore_discard, ignore_expires))
        finally:
            f.close()

        return

    def _really_load(self, f, filename, ignore_discard, ignore_expires):
        magic = f.readline()
        if not re.search(self.magic_re, magic):
            msg = b'%r does not look like a Set-Cookie3 (LWP) format file' % filename
            raise LoadError(msg)
        now = time.time()
        header = b'Set-Cookie3:'
        boolean_attrs = (b'port_spec', b'path_spec', b'domain_dot', b'secure', b'discard')
        value_attrs = (b'version', b'port', b'path', b'domain', b'expires', b'comment', b'commenturl')
        try:
            while 1:
                line = f.readline()
                if line == b'':
                    break
                if not line.startswith(header):
                    continue
                line = line[len(header):].strip()
                for data in split_header_words([line]):
                    name, value = data[0]
                    standard = {}
                    rest = {}
                    for k in boolean_attrs:
                        standard[k] = False

                    for k, v in data[1:]:
                        if k is not None:
                            lc = k.lower()
                        else:
                            lc = None
                        if lc in value_attrs or lc in boolean_attrs:
                            k = lc
                        if k in boolean_attrs:
                            if v is None:
                                v = True
                            standard[k] = v
                        elif k in value_attrs:
                            standard[k] = v
                        else:
                            rest[k] = v

                    h = standard.get
                    expires = h(b'expires')
                    discard = h(b'discard')
                    if expires is not None:
                        expires = iso2time(expires)
                    if expires is None:
                        discard = True
                    domain = h(b'domain')
                    domain_specified = domain.startswith(b'.')
                    c = Cookie(h(b'version'), name, value, h(b'port'), h(b'port_spec'), domain, domain_specified, h(b'domain_dot'), h(b'path'), h(b'path_spec'), h(b'secure'), expires, discard, h(b'comment'), h(b'commenturl'), rest)
                    if not ignore_discard and c.discard:
                        continue
                    if not ignore_expires and c.is_expired(now):
                        continue
                    self.set_cookie(c)

        except IOError:
            raise
        except Exception:
            _warn_unhandled_exception()
            raise LoadError(b'invalid Set-Cookie3 format file %r: %r' % (
             filename, line))

        return
