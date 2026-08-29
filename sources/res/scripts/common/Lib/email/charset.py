__all__ = [
 b'Charset',
 b'add_alias',
 b'add_charset',
 b'add_codec']
import codecs, email.base64mime, email.quoprimime
from email import errors
from email.encoders import encode_7or8bit
QP = 1
BASE64 = 2
SHORTEST = 3
MISC_LEN = 7
DEFAULT_CHARSET = b'us-ascii'
CHARSETS = {b'iso-8859-1': (
                 QP, QP, None), 
   b'iso-8859-2': (
                 QP, QP, None), 
   b'iso-8859-3': (
                 QP, QP, None), 
   b'iso-8859-4': (
                 QP, QP, None), 
   b'iso-8859-9': (
                 QP, QP, None), 
   b'iso-8859-10': (
                  QP, QP, None), 
   b'iso-8859-13': (
                  QP, QP, None), 
   b'iso-8859-14': (
                  QP, QP, None), 
   b'iso-8859-15': (
                  QP, QP, None), 
   b'iso-8859-16': (
                  QP, QP, None), 
   b'windows-1252': (
                   QP, QP, None), 
   b'viscii': (
             QP, QP, None), 
   b'us-ascii': (None, None, None), 
   b'big5': (
           BASE64, BASE64, None), 
   b'gb2312': (
             BASE64, BASE64, None), 
   b'euc-jp': (
             BASE64, None, b'iso-2022-jp'), 
   b'shift_jis': (
                BASE64, None, b'iso-2022-jp'), 
   b'iso-2022-jp': (
                  BASE64, None, None), 
   b'koi8-r': (
             BASE64, BASE64, None), 
   b'utf-8': (
            SHORTEST, BASE64, b'utf-8'), 
   b'8bit': (
           None, BASE64, b'utf-8')}
ALIASES = {b'latin_1': b'iso-8859-1', 
   b'latin-1': b'iso-8859-1', 
   b'latin_2': b'iso-8859-2', 
   b'latin-2': b'iso-8859-2', 
   b'latin_3': b'iso-8859-3', 
   b'latin-3': b'iso-8859-3', 
   b'latin_4': b'iso-8859-4', 
   b'latin-4': b'iso-8859-4', 
   b'latin_5': b'iso-8859-9', 
   b'latin-5': b'iso-8859-9', 
   b'latin_6': b'iso-8859-10', 
   b'latin-6': b'iso-8859-10', 
   b'latin_7': b'iso-8859-13', 
   b'latin-7': b'iso-8859-13', 
   b'latin_8': b'iso-8859-14', 
   b'latin-8': b'iso-8859-14', 
   b'latin_9': b'iso-8859-15', 
   b'latin-9': b'iso-8859-15', 
   b'latin_10': b'iso-8859-16', 
   b'latin-10': b'iso-8859-16', 
   b'cp949': b'ks_c_5601-1987', 
   b'euc_jp': b'euc-jp', 
   b'euc_kr': b'euc-kr', 
   b'ascii': b'us-ascii'}
CODEC_MAP = {b'gb2312': b'eucgb2312_cn', 
   b'big5': b'big5_tw', 
   b'us-ascii': None}

def add_charset(charset, header_enc=None, body_enc=None, output_charset=None):
    if body_enc == SHORTEST:
        raise ValueError(b'SHORTEST not allowed for body_enc')
    CHARSETS[charset] = (
     header_enc, body_enc, output_charset)
    return


def add_alias(alias, canonical):
    ALIASES[alias] = canonical
    return


def add_codec(charset, codecname):
    CODEC_MAP[charset] = codecname
    return


class Charset:

    def __init__(self, input_charset=DEFAULT_CHARSET):
        try:
            if isinstance(input_charset, unicode):
                input_charset.encode(b'ascii')
            else:
                input_charset = unicode(input_charset, b'ascii')
        except UnicodeError:
            raise errors.CharsetError(input_charset)

        input_charset = input_charset.lower().encode(b'ascii')
        if not (input_charset in ALIASES or input_charset in CHARSETS):
            try:
                input_charset = codecs.lookup(input_charset).name
            except LookupError:
                pass

        self.input_charset = ALIASES.get(input_charset, input_charset)
        henc, benc, conv = CHARSETS.get(self.input_charset, (
         SHORTEST, BASE64, None))
        if not conv:
            conv = self.input_charset
        self.header_encoding = henc
        self.body_encoding = benc
        self.output_charset = ALIASES.get(conv, conv)
        self.input_codec = CODEC_MAP.get(self.input_charset, self.input_charset)
        self.output_codec = CODEC_MAP.get(self.output_charset, self.output_charset)
        return

    def __str__(self):
        return self.input_charset.lower()

    __repr__ = __str__

    def __eq__(self, other):
        return str(self) == str(other).lower()

    def __ne__(self, other):
        return not self.__eq__(other)

    def get_body_encoding(self):
        if self.body_encoding == QP:
            return b'quoted-printable'
        else:
            if self.body_encoding == BASE64:
                return b'base64'
            return encode_7or8bit

        return

    def convert(self, s):
        if self.input_codec != self.output_codec:
            return unicode(s, self.input_codec).encode(self.output_codec)
        else:
            return s

        return

    def to_splittable(self, s):
        if isinstance(s, unicode) or self.input_codec is None:
            return s
        try:
            return unicode(s, self.input_codec, b'replace')
        except LookupError:
            return s

        return

    def from_splittable(self, ustr, to_output=True):
        if to_output:
            codec = self.output_codec
        else:
            codec = self.input_codec
        if not isinstance(ustr, unicode) or codec is None:
            return ustr
        try:
            return ustr.encode(codec, b'replace')
        except LookupError:
            return ustr

        return

    def get_output_charset(self):
        return self.output_charset or self.input_charset

    def encoded_header_len(self, s):
        cset = self.get_output_charset()
        if self.header_encoding == BASE64:
            return email.base64mime.base64_len(s) + len(cset) + MISC_LEN
        else:
            if self.header_encoding == QP:
                return email.quoprimime.header_quopri_len(s) + len(cset) + MISC_LEN
            if self.header_encoding == SHORTEST:
                lenb64 = email.base64mime.base64_len(s)
                lenqp = email.quoprimime.header_quopri_len(s)
                return min(lenb64, lenqp) + len(cset) + MISC_LEN
            return len(s)

        return

    def header_encode(self, s, convert=False):
        cset = self.get_output_charset()
        if convert:
            s = self.convert(s)
        if self.header_encoding == BASE64:
            return email.base64mime.header_encode(s, cset)
        else:
            if self.header_encoding == QP:
                return email.quoprimime.header_encode(s, cset, maxlinelen=None)
            if self.header_encoding == SHORTEST:
                lenb64 = email.base64mime.base64_len(s)
                lenqp = email.quoprimime.header_quopri_len(s)
                if lenb64 < lenqp:
                    return email.base64mime.header_encode(s, cset)
                return email.quoprimime.header_encode(s, cset, maxlinelen=None)
            else:
                return s
            return

    def body_encode(self, s, convert=True):
        if convert:
            s = self.convert(s)
        if self.body_encoding is BASE64:
            return email.base64mime.body_encode(s)
        else:
            if self.body_encoding is QP:
                return email.quoprimime.body_encode(s)
            return s

        return
