__all__ = [
 b'Message']
import re, uu, binascii, warnings
from cStringIO import StringIO
import email.charset
from email import utils
from email import errors
SEMISPACE = b'; '
tspecials = re.compile(b'[ \\(\\)<>@,;:\\\\"/\\[\\]\\?=]')

def _splitparam(param):
    a, sep, b = param.partition(b';')
    if not sep:
        return (a.strip(), None)
    else:
        return (
         a.strip(), b.strip())


def _formatparam(param, value=None, quote=True):
    if value is not None and len(value) > 0:
        if isinstance(value, tuple):
            param += b'*'
            value = utils.encode_rfc2231(value[2], value[0], value[1])
        if quote or tspecials.search(value):
            return b'%s="%s"' % (param, utils.quote(value))
        return b'%s=%s' % (param, value)
    else:
        return param
    return


def _parseparam(s):
    plist = []
    while s[:1] == b';':
        s = s[1:]
        end = s.find(b';')
        while end > 0 and (s.count(b'"', 0, end) - s.count(b'\\"', 0, end)) % 2:
            end = s.find(b';', end + 1)

        if end < 0:
            end = len(s)
        f = s[:end]
        if b'=' in f:
            i = f.index(b'=')
            f = f[:i].strip().lower() + b'=' + f[i + 1:].strip()
        plist.append(f.strip())
        s = s[end:]

    return plist


def _unquotevalue(value):
    if isinstance(value, tuple):
        return (value[0], value[1], utils.unquote(value[2]))
    else:
        return utils.unquote(value)

    return


class Message:

    def __init__(self):
        self._headers = []
        self._unixfrom = None
        self._payload = None
        self._charset = None
        self.preamble = self.epilogue = None
        self.defects = []
        self._default_type = b'text/plain'
        return

    def __str__(self):
        return self.as_string(unixfrom=True)

    def as_string(self, unixfrom=False):
        from email.generator import Generator
        fp = StringIO()
        g = Generator(fp)
        g.flatten(self, unixfrom=unixfrom)
        return fp.getvalue()

    def is_multipart(self):
        return isinstance(self._payload, list)

    def set_unixfrom(self, unixfrom):
        self._unixfrom = unixfrom
        return

    def get_unixfrom(self):
        return self._unixfrom

    def attach(self, payload):
        if self._payload is None:
            self._payload = [
             payload]
        else:
            self._payload.append(payload)
        return

    def get_payload(self, i=None, decode=False):
        if i is None:
            payload = self._payload
        elif not isinstance(self._payload, list):
            raise TypeError(b'Expected list, got %s' % type(self._payload))
        else:
            payload = self._payload[i]
        if decode:
            if self.is_multipart():
                return
            cte = self.get(b'content-transfer-encoding', b'').lower()
            if cte == b'quoted-printable':
                return utils._qdecode(payload)
            if cte == b'base64':
                try:
                    return utils._bdecode(payload)
                except binascii.Error:
                    return payload

            elif cte in (b'x-uuencode', b'uuencode', b'uue', b'x-uue'):
                sfp = StringIO()
                try:
                    uu.decode(StringIO(payload + b'\n'), sfp, quiet=True)
                    payload = sfp.getvalue()
                except uu.Error:
                    return payload

        return payload

    def set_payload(self, payload, charset=None):
        self._payload = payload
        if charset is not None:
            self.set_charset(charset)
        return

    def set_charset(self, charset):
        if charset is None:
            self.del_param(b'charset')
            self._charset = None
            return
        else:
            if isinstance(charset, basestring):
                charset = email.charset.Charset(charset)
            if not isinstance(charset, email.charset.Charset):
                raise TypeError(charset)
            self._charset = charset
            if b'MIME-Version' not in self:
                self.add_header(b'MIME-Version', b'1.0')
            if b'Content-Type' not in self:
                self.add_header(b'Content-Type', b'text/plain', charset=charset.get_output_charset())
            else:
                self.set_param(b'charset', charset.get_output_charset())
            if isinstance(self._payload, unicode):
                self._payload = self._payload.encode(charset.output_charset)
            if str(charset) != charset.get_output_charset():
                self._payload = charset.body_encode(self._payload)
            if b'Content-Transfer-Encoding' not in self:
                cte = charset.get_body_encoding()
                try:
                    cte(self)
                except TypeError:
                    self._payload = charset.body_encode(self._payload)
                    self.add_header(b'Content-Transfer-Encoding', cte)

            return

    def get_charset(self):
        return self._charset

    def __len__(self):
        return len(self._headers)

    def __getitem__(self, name):
        return self.get(name)

    def __setitem__(self, name, val):
        self._headers.append((name, val))
        return

    def __delitem__(self, name):
        name = name.lower()
        newheaders = []
        for k, v in self._headers:
            if k.lower() != name:
                newheaders.append((k, v))

        self._headers = newheaders
        return

    def __contains__(self, name):
        return name.lower() in [k.lower() for k, v in self._headers]

    def has_key(self, name):
        missing = object()
        return self.get(name, missing) is not missing

    def keys(self):
        return [k for k, v in self._headers]

    def values(self):
        return [v for k, v in self._headers]

    def items(self):
        return self._headers[:]

    def get(self, name, failobj=None):
        name = name.lower()
        for k, v in self._headers:
            if k.lower() == name:
                return v

        return failobj

    def get_all(self, name, failobj=None):
        values = []
        name = name.lower()
        for k, v in self._headers:
            if k.lower() == name:
                values.append(v)

        if not values:
            return failobj
        return values

    def add_header(self, _name, _value, **_params):
        parts = []
        for k, v in _params.items():
            if v is None:
                parts.append(k.replace(b'_', b'-'))
            else:
                parts.append(_formatparam(k.replace(b'_', b'-'), v))

        if _value is not None:
            parts.insert(0, _value)
        self._headers.append((_name, SEMISPACE.join(parts)))
        return

    def replace_header(self, _name, _value):
        _name = _name.lower()
        for i, (k, v) in zip(range(len(self._headers)), self._headers):
            if k.lower() == _name:
                self._headers[i] = (
                 k, _value)
                break
        else:
            raise KeyError(_name)

        return

    def get_content_type(self):
        missing = object()
        value = self.get(b'content-type', missing)
        if value is missing:
            return self.get_default_type()
        ctype = _splitparam(value)[0].lower()
        if ctype.count(b'/') != 1:
            return b'text/plain'
        return ctype

    def get_content_maintype(self):
        ctype = self.get_content_type()
        return ctype.split(b'/')[0]

    def get_content_subtype(self):
        ctype = self.get_content_type()
        return ctype.split(b'/')[1]

    def get_default_type(self):
        return self._default_type

    def set_default_type(self, ctype):
        self._default_type = ctype
        return

    def _get_params_preserve(self, failobj, header):
        missing = object()
        value = self.get(header, missing)
        if value is missing:
            return failobj
        params = []
        for p in _parseparam(b';' + value):
            try:
                name, val = p.split(b'=', 1)
                name = name.strip()
                val = val.strip()
            except ValueError:
                name = p.strip()
                val = b''

            params.append((name, val))

        params = utils.decode_params(params)
        return params

    def get_params(self, failobj=None, header=b'content-type', unquote=True):
        missing = object()
        params = self._get_params_preserve(missing, header)
        if params is missing:
            return failobj
        else:
            if unquote:
                return [(k, _unquotevalue(v)) for k, v in params]
            return params

        return

    def get_param(self, param, failobj=None, header=b'content-type', unquote=True):
        if header not in self:
            return failobj
        for k, v in self._get_params_preserve(failobj, header):
            if k.lower() == param.lower():
                if unquote:
                    return _unquotevalue(v)
                else:
                    return v

        return failobj

    def set_param(self, param, value, header=b'Content-Type', requote=True, charset=None, language=b''):
        if not isinstance(value, tuple) and charset:
            value = (
             charset, language, value)
        if header not in self and header.lower() == b'content-type':
            ctype = b'text/plain'
        else:
            ctype = self.get(header)
        if not self.get_param(param, header=header):
            if not ctype:
                ctype = _formatparam(param, value, requote)
            else:
                ctype = SEMISPACE.join([
                 ctype, _formatparam(param, value, requote)])
        else:
            ctype = b''
            for old_param, old_value in self.get_params(header=header, unquote=requote):
                append_param = b''
                if old_param.lower() == param.lower():
                    append_param = _formatparam(param, value, requote)
                else:
                    append_param = _formatparam(old_param, old_value, requote)
                if not ctype:
                    ctype = append_param
                else:
                    ctype = SEMISPACE.join([ctype, append_param])

        if ctype != self.get(header):
            del self[header]
            self[header] = ctype
        return

    def del_param(self, param, header=b'content-type', requote=True):
        if header not in self:
            return
        new_ctype = b''
        for p, v in self.get_params(header=header, unquote=requote):
            if p.lower() != param.lower():
                if not new_ctype:
                    new_ctype = _formatparam(p, v, requote)
                else:
                    new_ctype = SEMISPACE.join([new_ctype,
                     _formatparam(p, v, requote)])

        if new_ctype != self.get(header):
            del self[header]
            self[header] = new_ctype
        return

    def set_type(self, type, header=b'Content-Type', requote=True):
        if not type.count(b'/') == 1:
            raise ValueError
        if header.lower() == b'content-type':
            del self[b'mime-version']
            self[b'MIME-Version'] = b'1.0'
        if header not in self:
            self[header] = type
            return
        params = self.get_params(header=header, unquote=requote)
        del self[header]
        self[header] = type
        for p, v in params[1:]:
            self.set_param(p, v, header, requote)

        return

    def get_filename(self, failobj=None):
        missing = object()
        filename = self.get_param(b'filename', missing, b'content-disposition')
        if filename is missing:
            filename = self.get_param(b'name', missing, b'content-type')
        if filename is missing:
            return failobj
        return utils.collapse_rfc2231_value(filename).strip()

    def get_boundary(self, failobj=None):
        missing = object()
        boundary = self.get_param(b'boundary', missing)
        if boundary is missing:
            return failobj
        return utils.collapse_rfc2231_value(boundary).rstrip()

    def set_boundary(self, boundary):
        missing = object()
        params = self._get_params_preserve(missing, b'content-type')
        if params is missing:
            raise errors.HeaderParseError(b'No Content-Type header found')
        newparams = []
        foundp = False
        for pk, pv in params:
            if pk.lower() == b'boundary':
                newparams.append((b'boundary', b'"%s"' % boundary))
                foundp = True
            else:
                newparams.append((pk, pv))

        if not foundp:
            newparams.append((b'boundary', b'"%s"' % boundary))
        newheaders = []
        for h, v in self._headers:
            if h.lower() == b'content-type':
                parts = []
                for k, v in newparams:
                    if v == b'':
                        parts.append(k)
                    else:
                        parts.append(b'%s=%s' % (k, v))

                newheaders.append((h, SEMISPACE.join(parts)))
            else:
                newheaders.append((h, v))

        self._headers = newheaders
        return

    def get_content_charset(self, failobj=None):
        missing = object()
        charset = self.get_param(b'charset', missing)
        if charset is missing:
            return failobj
        if isinstance(charset, tuple):
            pcharset = charset[0] or b'us-ascii'
            try:
                charset = unicode(charset[2], pcharset).encode(b'us-ascii')
            except (LookupError, UnicodeError):
                charset = charset[2]

        try:
            if isinstance(charset, str):
                charset = unicode(charset, b'us-ascii')
            charset = charset.encode(b'us-ascii')
        except UnicodeError:
            return failobj

        return charset.lower()

    def get_charsets(self, failobj=None):
        return [part.get_content_charset(failobj) for part in self.walk()]

    from email.iterators import walk
