__version__ = b'5.1.2'
__license__ = b"\nCopyright (c) 2010-2012 Kurt McKee <contactme@kurtmckee.org>\nCopyright (c) 2002-2008 Mark Pilgrim\nAll rights reserved.\n\nRedistribution and use in source and binary forms, with or without modification,\nare permitted provided that the following conditions are met:\n\n* Redistributions of source code must retain the above copyright notice,\n  this list of conditions and the following disclaimer.\n* Redistributions in binary form must reproduce the above copyright notice,\n  this list of conditions and the following disclaimer in the documentation\n  and/or other materials provided with the distribution.\n\nTHIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS 'AS IS'\nAND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE\nIMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE\nARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE\nLIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR\nCONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF\nSUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS\nINTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN\nCONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)\nARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE\nPOSSIBILITY OF SUCH DAMAGE."
__author__ = b'Mark Pilgrim <http://diveintomark.org/>'
__contributors__ = [3, 
 4, 
 5, 
 6, 
 7, 
 8, 
 9, 
 10, 
 11]
USER_AGENT = b'UniversalFeedParser/%s +https://code.google.com/p/feedparser/' % __version__
ACCEPT_HEADER = b'application/atom+xml,application/rdf+xml,application/rss+xml,application/x-netcdf,application/xml;q=0.9,text/xml;q=0.2,*/*;q=0.1'
PREFERRED_XML_PARSERS = [
 b'drv_libxml2']
TIDY_MARKUP = 0
PREFERRED_TIDY_INTERFACES = [
 b'uTidy', b'mxTidy']
RESOLVE_RELATIVE_URIS = 1
SANITIZE_HTML = 1
PARSE_MICROFORMATS = 1
try:
    import rfc822
except ImportError:
    from email import _parseaddr as rfc822

try:
    _maketrans = bytes.maketrans
except (NameError, AttributeError):
    import string
    _maketrans = string.maketrans

try:
    import base64, binascii
except ImportError:
    base64 = binascii = None
else:
    _base64decode = getattr(base64, b'decodebytes', base64.decodestring)

try:
    if bytes is str:
        raise NameError
except NameError:

    def _s2bytes(s):
        return s


    def _l2bytes(l):
        return (b'').join(map(chr, l))


else:

    def _s2bytes(s):
        return bytes(s, b'utf8')


    def _l2bytes(l):
        return bytes(l)


ACCEPTABLE_URI_SCHEMES = (
 b'file', b'ftp', b'gopher', b'h323', b'hdl', b'http', b'https', b'imap', b'magnet',
 b'mailto', b'mms', b'news', b'nntp', b'prospero', b'rsync', b'rtsp', b'rtspu',
 b'sftp', b'shttp', b'sip', b'sips', b'snews', b'svn', b'svn+ssh', b'telnet',
 b'wais',
 b'aim', b'callto', b'cvs', b'facetime', b'feed', b'git', b'gtalk', b'irc', b'ircs',
 b'irc6', b'itms', b'mms', b'msnim', b'skype', b'ssh', b'smb', b'svn', b'ymsg')
import cgi, codecs, copy, datetime, re, struct, time, types, urllib, urllib2, urlparse, warnings
from htmlentitydefs import name2codepoint, codepoint2name, entitydefs
try:
    from io import BytesIO as _StringIO
except ImportError:
    try:
        from cStringIO import StringIO as _StringIO
    except ImportError:
        from StringIO import StringIO as _StringIO

try:
    import gzip
except ImportError:
    gzip = None

try:
    import zlib
except ImportError:
    zlib = None

try:
    import xml.sax
    from xml.sax.saxutils import escape as _xmlescape
except ImportError:
    _XML_AVAILABLE = 0

    def _xmlescape(data, entities={}):
        data = data.replace(b'&', b'&amp;')
        data = data.replace(b'>', b'&gt;')
        data = data.replace(b'<', b'&lt;')
        for char, entity in entities:
            data = data.replace(char, entity)

        return data


else:
    try:
        xml.sax.make_parser(PREFERRED_XML_PARSERS)
    except xml.sax.SAXReaderNotAvailable:
        _XML_AVAILABLE = 0
    else:
        _XML_AVAILABLE = 1

try:
    import sgmllib
except ImportError:
    _SGML_AVAILABLE = 0

    class sgmllib(object):

        class SGMLParser(object):

            def goahead(self, i):
                return

            def parse_starttag(self, i):
                return


else:
    _SGML_AVAILABLE = 1
    charref = re.compile(b'&#(\\d+|[xX][0-9a-fA-F]+);')
    tagfind = re.compile(b'[a-zA-Z][-_.:a-zA-Z0-9]*')
    attrfind = re.compile(b'\\s*([a-zA-Z_][-:.a-zA-Z_0-9]*)[$]?(\\s*=\\s*(\\\'[^\\\']*\\\'|"[^"]*"|[][\\-a-zA-Z0-9./,:;+*%?!&$\\(\\)_#=~\\\'"@]*))?')
    entityref = sgmllib.entityref
    incomplete = sgmllib.incomplete
    interesting = sgmllib.interesting
    shorttag = sgmllib.shorttag
    shorttagopen = sgmllib.shorttagopen
    starttagopen = sgmllib.starttagopen

    class _EndBracketRegEx():

        def __init__(self):
            self.endbracket = re.compile(b'([^\'"<>]|"[^"]*"(?=>|/|\\s|\\w+=)|\'[^\']*\'(?=>|/|\\s|\\w+=))*(?=[<>])|.*?(?=[<>])')
            return

        def search(self, target, index=0):
            match = self.endbracket.match(target, index)
            if match is not None:
                return EndBracketMatch(match)
            else:
                return


    class EndBracketMatch():

        def __init__(self, match):
            self.match = match
            return

        def start(self, n):
            return self.match.end(n)


    endbracket = _EndBracketRegEx()

try:
    import iconv_codec
except ImportError:
    pass

try:
    import chardet
except ImportError:
    chardet = None

try:
    import BeautifulSoup
except ImportError:
    BeautifulSoup = None
    PARSE_MICROFORMATS = False

try:
    codecs.lookup(b'utf_32')
except LookupError:
    _UTF32_AVAILABLE = False
else:
    _UTF32_AVAILABLE = True

class ThingsNobodyCaresAboutButMe(Exception):
    pass


class CharacterEncodingOverride(ThingsNobodyCaresAboutButMe):
    pass


class CharacterEncodingUnknown(ThingsNobodyCaresAboutButMe):
    pass


class NonXMLContentType(ThingsNobodyCaresAboutButMe):
    pass


class UndeclaredNamespace(Exception):
    pass


SUPPORTED_VERSIONS = {b'': u'unknown', b'rss090': u'RSS 0.90', 
   b'rss091n': u'RSS 0.91 (Netscape)', 
   b'rss091u': u'RSS 0.91 (Userland)', 
   b'rss092': u'RSS 0.92', 
   b'rss093': u'RSS 0.93', 
   b'rss094': u'RSS 0.94', 
   b'rss20': u'RSS 2.0', 
   b'rss10': u'RSS 1.0', 
   b'rss': u'RSS (unknown version)', 
   b'atom01': u'Atom 0.1', 
   b'atom02': u'Atom 0.2', 
   b'atom03': u'Atom 0.3', 
   b'atom10': u'Atom 1.0', 
   b'atom': u'Atom (unknown version)', 
   b'cdf': u'CDF'}

class FeedParserDict(dict):
    keymap = {b'channel': b'feed', b'items': b'entries', 
       b'guid': b'id', 
       b'date': b'updated', 
       b'date_parsed': b'updated_parsed', 
       b'description': [
                      b'summary', b'subtitle'], 
       b'description_detail': [
                             b'summary_detail', b'subtitle_detail'], 
       b'url': [
              b'href'], 
       b'modified': b'updated', 
       b'modified_parsed': b'updated_parsed', 
       b'issued': b'published', 
       b'issued_parsed': b'published_parsed', 
       b'copyright': b'rights', 
       b'copyright_detail': b'rights_detail', 
       b'tagline': b'subtitle', 
       b'tagline_detail': b'subtitle_detail'}

    def __getitem__(self, key):
        if key == b'category':
            try:
                return dict.__getitem__(self, b'tags')[0][b'term']
            except IndexError:
                raise KeyError, b"object doesn't have key 'category'"

        elif key == b'enclosures':
            norel = lambda link: FeedParserDict([(name, value) for name, value in link.items() if name != b'rel'])
            return [norel(link) for link in dict.__getitem__(self, b'links') if link[b'rel'] == u'enclosure']
        if key == b'license':
            for link in dict.__getitem__(self, b'links'):
                if link[b'rel'] == u'license' and b'href' in link:
                    return link[b'href']

        elif key == b'updated':
            if not dict.__contains__(self, b'updated') and dict.__contains__(self, b'published'):
                warnings.warn(b"To avoid breaking existing software while fixing issue 310, a temporary mapping has been created from `updated` to `published` if `updated` doesn't exist. This fallback will be removed in a future version of feedparser.", DeprecationWarning)
                return dict.__getitem__(self, b'published')
            return dict.__getitem__(self, b'updated')
        if key == b'updated_parsed':
            if not dict.__contains__(self, b'updated_parsed') and dict.__contains__(self, b'published_parsed'):
                warnings.warn(b"To avoid breaking existing software while fixing issue 310, a temporary mapping has been created from `updated_parsed` to `published_parsed` if `updated_parsed` doesn't exist. This fallback will be removed in a future version of feedparser.", DeprecationWarning)
                return dict.__getitem__(self, b'published_parsed')
            return dict.__getitem__(self, b'updated_parsed')
        realkey = self.keymap.get(key, key)
        if isinstance(realkey, list):
            for k in realkey:
                if dict.__contains__(self, k):
                    return dict.__getitem__(self, k)

        elif dict.__contains__(self, realkey):
            return dict.__getitem__(self, realkey)
        return dict.__getitem__(self, key)

    def __contains__(self, key):
        if key in (b'updated', b'updated_parsed'):
            return dict.__contains__(self, key)
        else:
            try:
                self.__getitem__(key)
            except KeyError:
                return False

            return True

        return

    has_key = __contains__

    def get(self, key, default=None):
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

        return

    def __setitem__(self, key, value):
        key = self.keymap.get(key, key)
        if isinstance(key, list):
            key = key[0]
        return dict.__setitem__(self, key, value)

    def setdefault(self, key, value):
        if key not in self:
            self[key] = value
            return value
        return self[key]

    def __getattr__(self, key):
        try:
            return self.__getitem__(key)
        except KeyError:
            raise AttributeError, b"object has no attribute '%s'" % key

        return

    def __hash__(self):
        return id(self)


_cp1252 = {128: (unichr(8364)), 
   130: (unichr(8218)), 
   131: (unichr(402)), 
   132: (unichr(8222)), 
   133: (unichr(8230)), 
   134: (unichr(8224)), 
   135: (unichr(8225)), 
   136: (unichr(710)), 
   137: (unichr(8240)), 
   138: (unichr(352)), 
   139: (unichr(8249)), 
   140: (unichr(338)), 
   142: (unichr(381)), 
   145: (unichr(8216)), 
   146: (unichr(8217)), 
   147: (unichr(8220)), 
   148: (unichr(8221)), 
   149: (unichr(8226)), 
   150: (unichr(8211)), 
   151: (unichr(8212)), 
   152: (unichr(732)), 
   153: (unichr(8482)), 
   154: (unichr(353)), 
   155: (unichr(8250)), 
   156: (unichr(339)), 
   158: (unichr(382)), 
   159: (unichr(376))}
_urifixer = re.compile(b'^([A-Za-z][A-Za-z0-9+-.]*://)(/*)(.*?)')

def _urljoin(base, uri):
    uri = _urifixer.sub(b'\\1\\3', uri)
    if not isinstance(uri, unicode):
        uri = uri.decode(b'utf-8', b'ignore')
    uri = urlparse.urljoin(base, uri)
    if not isinstance(uri, unicode):
        return uri.decode(b'utf-8', b'ignore')
    return uri


class _FeedParserMixin():
    namespaces = {b'': b'', 
       b'http://backend.userland.com/rss': b'', 
       b'http://blogs.law.harvard.edu/tech/rss': b'', 
       b'http://purl.org/rss/1.0/': b'', 
       b'http://my.netscape.com/rdf/simple/0.9/': b'', 
       b'http://example.com/newformat#': b'', 
       b'http://example.com/necho': b'', 
       b'http://purl.org/echo/': b'', 
       b'uri/of/echo/namespace#': b'', 
       b'http://purl.org/pie/': b'', 
       b'http://purl.org/atom/ns#': b'', 
       b'http://www.w3.org/2005/Atom': b'', 
       b'http://purl.org/rss/1.0/modules/rss091#': b'', 
       b'http://webns.net/mvcb/': b'admin', 
       b'http://purl.org/rss/1.0/modules/aggregation/': b'ag', 
       b'http://purl.org/rss/1.0/modules/annotate/': b'annotate', 
       b'http://media.tangent.org/rss/1.0/': b'audio', 
       b'http://backend.userland.com/blogChannelModule': b'blogChannel', 
       b'http://web.resource.org/cc/': b'cc', 
       b'http://backend.userland.com/creativeCommonsRssModule': b'creativeCommons', 
       b'http://purl.org/rss/1.0/modules/company': b'co', 
       b'http://purl.org/rss/1.0/modules/content/': b'content', 
       b'http://my.theinfo.org/changed/1.0/rss/': b'cp', 
       b'http://purl.org/dc/elements/1.1/': b'dc', 
       b'http://purl.org/dc/terms/': b'dcterms', 
       b'http://purl.org/rss/1.0/modules/email/': b'email', 
       b'http://purl.org/rss/1.0/modules/event/': b'ev', 
       b'http://rssnamespace.org/feedburner/ext/1.0': b'feedburner', 
       b'http://freshmeat.net/rss/fm/': b'fm', 
       b'http://xmlns.com/foaf/0.1/': b'foaf', 
       b'http://www.w3.org/2003/01/geo/wgs84_pos#': b'geo', 
       b'http://postneo.com/icbm/': b'icbm', 
       b'http://purl.org/rss/1.0/modules/image/': b'image', 
       b'http://www.itunes.com/DTDs/PodCast-1.0.dtd': b'itunes', 
       b'http://example.com/DTDs/PodCast-1.0.dtd': b'itunes', 
       b'http://purl.org/rss/1.0/modules/link/': b'l', 
       b'http://search.yahoo.com/mrss': b'media', 
       b'http://search.yahoo.com/mrss/': b'media', 
       b'http://madskills.com/public/xml/rss/module/pingback/': b'pingback', 
       b'http://prismstandard.org/namespaces/1.2/basic/': b'prism', 
       b'http://www.w3.org/1999/02/22-rdf-syntax-ns#': b'rdf', 
       b'http://www.w3.org/2000/01/rdf-schema#': b'rdfs', 
       b'http://purl.org/rss/1.0/modules/reference/': b'ref', 
       b'http://purl.org/rss/1.0/modules/richequiv/': b'reqv', 
       b'http://purl.org/rss/1.0/modules/search/': b'search', 
       b'http://purl.org/rss/1.0/modules/slash/': b'slash', 
       b'http://schemas.xmlsoap.org/soap/envelope/': b'soap', 
       b'http://purl.org/rss/1.0/modules/servicestatus/': b'ss', 
       b'http://hacks.benhammersley.com/rss/streaming/': b'str', 
       b'http://purl.org/rss/1.0/modules/subscription/': b'sub', 
       b'http://purl.org/rss/1.0/modules/syndication/': b'sy', 
       b'http://schemas.pocketsoap.com/rss/myDescModule/': b'szf', 
       b'http://purl.org/rss/1.0/modules/taxonomy/': b'taxo', 
       b'http://purl.org/rss/1.0/modules/threading/': b'thr', 
       b'http://purl.org/rss/1.0/modules/textinput/': b'ti', 
       b'http://madskills.com/public/xml/rss/module/trackback/': b'trackback', 
       b'http://wellformedweb.org/commentAPI/': b'wfw', 
       b'http://purl.org/rss/1.0/modules/wiki/': b'wiki', 
       b'http://www.w3.org/1999/xhtml': b'xhtml', 
       b'http://www.w3.org/1999/xlink': b'xlink', 
       b'http://www.w3.org/XML/1998/namespace': b'xml'}
    _matchnamespaces = {}
    can_be_relative_uri = set([107, 108, 109, 110, 111, 112, 113, 114, 115, 116])
    can_contain_relative_uris = set([29, 117, 118, 119, 120, 121, 122, 123, 124])
    can_contain_dangerous_markup = set([29, 117, 118, 119, 120, 121, 122, 123, 124])
    html_types = [u'text/html', u'application/xhtml+xml']

    def __init__(self, baseuri=None, baselang=None, encoding=u'utf-8'):
        if not self._matchnamespaces:
            for k, v in self.namespaces.items():
                self._matchnamespaces[k.lower()] = v

        self.feeddata = FeedParserDict()
        self.encoding = encoding
        self.entries = []
        self.version = u''
        self.namespacesInUse = {}
        self.infeed = 0
        self.inentry = 0
        self.incontent = 0
        self.intextinput = 0
        self.inimage = 0
        self.inauthor = 0
        self.incontributor = 0
        self.inpublisher = 0
        self.insource = 0
        self.sourcedata = FeedParserDict()
        self.contentparams = FeedParserDict()
        self._summaryKey = None
        self.namespacemap = {}
        self.elementstack = []
        self.basestack = []
        self.langstack = []
        self.baseuri = baseuri or u''
        self.lang = baselang or None
        self.svgOK = 0
        self.title_depth = -1
        self.depth = 0
        if baselang:
            self.feeddata[b'language'] = baselang.replace(b'_', b'-')
        self.property_depth_map = {}
        return

    def _normalize_attributes(self, kv):
        k = kv[0].lower()
        v = k in (b'rel', b'type') and kv[1].lower() or kv[1]
        if isinstance(self, _LooseFeedParser):
            v = v.replace(b'&amp;', b'&')
            if not isinstance(v, unicode):
                v = v.decode(b'utf-8')
        return (
         k, v)

    def unknown_starttag(self, tag, attrs):
        self.depth += 1
        attrs = map(self._normalize_attributes, attrs)
        attrsD = dict(attrs)
        baseuri = attrsD.get(b'xml:base', attrsD.get(b'base')) or self.baseuri
        if not isinstance(baseuri, unicode):
            baseuri = baseuri.decode(self.encoding, b'ignore')
        if self.baseuri:
            self.baseuri = _makeSafeAbsoluteURI(self.baseuri, baseuri) or self.baseuri
        else:
            self.baseuri = _urljoin(self.baseuri, baseuri)
        lang = attrsD.get(b'xml:lang', attrsD.get(b'lang'))
        if lang == b'':
            lang = None
        elif lang is None:
            lang = self.lang
        if lang:
            if tag in (b'feed', b'rss', b'rdf:RDF'):
                self.feeddata[b'language'] = lang.replace(b'_', b'-')
        self.lang = lang
        self.basestack.append(self.baseuri)
        self.langstack.append(lang)
        for prefix, uri in attrs:
            if prefix.startswith(b'xmlns:'):
                self.trackNamespace(prefix[6:], uri)
            elif prefix == b'xmlns':
                self.trackNamespace(None, uri)

        if self.incontent and not self.contentparams.get(b'type', u'xml').endswith(u'xml'):
            if tag in (b'xhtml:div', b'div'):
                return
            self.contentparams[b'type'] = u'application/xhtml+xml'
        if self.incontent and self.contentparams.get(b'type') == u'application/xhtml+xml':
            if tag.find(b':') != -1:
                prefix, tag = tag.split(b':', 1)
                namespace = self.namespacesInUse.get(prefix, b'')
                if tag == b'math' and namespace == b'http://www.w3.org/1998/Math/MathML':
                    attrs.append((b'xmlns', namespace))
                if tag == b'svg' and namespace == b'http://www.w3.org/2000/svg':
                    attrs.append((b'xmlns', namespace))
            if tag == b'svg':
                self.svgOK += 1
            return self.handle_data(b'<%s%s>' % (tag, self.strattrs(attrs)), escape=0)
        else:
            if tag.find(b':') != -1:
                prefix, suffix = tag.split(b':', 1)
            else:
                prefix, suffix = b'', tag
            prefix = self.namespacemap.get(prefix, prefix)
            if prefix:
                prefix = prefix + b'_'
            if not prefix and tag not in (b'title', b'link', b'description', b'name'):
                self.intextinput = 0
            if not prefix and tag not in (b'title', b'link', b'description', b'url', b'href', b'width', b'height'):
                self.inimage = 0
            methodname = b'_start_' + prefix + suffix
            try:
                method = getattr(self, methodname)
                return method(attrsD)
            except AttributeError:
                unknown_tag = prefix + suffix
                if not attrsD:
                    return self.push(unknown_tag, 1)
                context = self._getContext()
                context[unknown_tag] = attrsD

            return

    def unknown_endtag(self, tag):
        if tag.find(b':') != -1:
            prefix, suffix = tag.split(b':', 1)
        else:
            prefix, suffix = b'', tag
        prefix = self.namespacemap.get(prefix, prefix)
        if prefix:
            prefix = prefix + b'_'
        if suffix == b'svg' and self.svgOK:
            self.svgOK -= 1
        methodname = b'_end_' + prefix + suffix
        try:
            if self.svgOK:
                raise AttributeError()
            method = getattr(self, methodname)
            method()
        except AttributeError:
            self.pop(prefix + suffix)

        if self.incontent and not self.contentparams.get(b'type', u'xml').endswith(u'xml'):
            if tag in (b'xhtml:div', b'div'):
                return
            self.contentparams[b'type'] = u'application/xhtml+xml'
        if self.incontent and self.contentparams.get(b'type') == u'application/xhtml+xml':
            tag = tag.split(b':')[-1]
            self.handle_data(b'</%s>' % tag, escape=0)
        if self.basestack:
            self.basestack.pop()
            if self.basestack and self.basestack[-1]:
                self.baseuri = self.basestack[-1]
        if self.langstack:
            self.langstack.pop()
            if self.langstack:
                self.lang = self.langstack[-1]
        self.depth -= 1
        return

    def handle_charref(self, ref):
        if not self.elementstack:
            return
        ref = ref.lower()
        if ref in (b'34', b'38', b'39', b'60', b'62', b'x22', b'x26', b'x27', b'x3c', b'x3e'):
            text = b'&#%s;' % ref
        else:
            if ref[0] == b'x':
                c = int(ref[1:], 16)
            else:
                c = int(ref)
            text = unichr(c).encode(b'utf-8')
        self.elementstack[-1][2].append(text)
        return

    def handle_entityref(self, ref):
        if not self.elementstack:
            return
        if ref in (b'lt', b'gt', b'quot', b'amp', b'apos'):
            text = b'&%s;' % ref
        elif ref in self.entities:
            text = self.entities[ref]
            if text.startswith(b'&#') and text.endswith(b';'):
                return self.handle_entityref(text)
        else:
            try:
                name2codepoint[ref]
            except KeyError:
                text = b'&%s;' % ref
            else:
                text = unichr(name2codepoint[ref]).encode(b'utf-8')

        self.elementstack[-1][2].append(text)
        return

    def handle_data(self, text, escape=1):
        if not self.elementstack:
            return
        if escape and self.contentparams.get(b'type') == u'application/xhtml+xml':
            text = _xmlescape(text)
        self.elementstack[-1][2].append(text)
        return

    def handle_comment(self, text):
        return

    def handle_pi(self, text):
        return

    def handle_decl(self, text):
        return

    def parse_declaration(self, i):
        if self.rawdata[i:i + 9] == b'<![CDATA[':
            k = self.rawdata.find(b']]>', i)
            if k == -1:
                k = len(self.rawdata)
                return k
            self.handle_data(_xmlescape(self.rawdata[i + 9:k]), 0)
            return k + 3
        else:
            k = self.rawdata.find(b'>', i)
            if k >= 0:
                return k + 1
            return k

        return

    def mapContentType(self, contentType):
        contentType = contentType.lower()
        if contentType == b'text' or contentType == b'plain':
            contentType = u'text/plain'
        elif contentType == b'html':
            contentType = u'text/html'
        elif contentType == b'xhtml':
            contentType = u'application/xhtml+xml'
        return contentType

    def trackNamespace(self, prefix, uri):
        loweruri = uri.lower()
        if not self.version:
            if (
             prefix, loweruri) == (None, b'http://my.netscape.com/rdf/simple/0.9/'):
                self.version = u'rss090'
            elif loweruri == b'http://purl.org/rss/1.0/':
                self.version = u'rss10'
            elif loweruri == b'http://www.w3.org/2005/atom':
                self.version = u'atom10'
        if loweruri.find(u'backend.userland.com/rss') != -1:
            uri = u'http://backend.userland.com/rss'
            loweruri = uri
        if loweruri in self._matchnamespaces:
            self.namespacemap[prefix] = self._matchnamespaces[loweruri]
            self.namespacesInUse[self._matchnamespaces[loweruri]] = uri
        else:
            self.namespacesInUse[prefix or b''] = uri
        return

    def resolveURI(self, uri):
        return _urljoin(self.baseuri or u'', uri)

    def decodeEntities(self, element, data):
        return data

    def strattrs(self, attrs):
        return (b'').join([b' %s="%s"' % (t[0], _xmlescape(t[1], {b'"': b'&quot;'})) for t in attrs])

    def push(self, element, expectingText):
        self.elementstack.append([element, expectingText, []])
        return

    def pop(self, element, stripWhitespace=1):
        if not self.elementstack:
            return
        else:
            if self.elementstack[-1][0] != element:
                return
            element, expectingText, pieces = self.elementstack.pop()
            if self.version == u'atom10' and self.contentparams.get(b'type', u'text') == u'application/xhtml+xml':
                while pieces and len(pieces) > 1 and not pieces[-1].strip():
                    del pieces[-1]

                while pieces and len(pieces) > 1 and not pieces[0].strip():
                    del pieces[0]

                if pieces and (pieces[0] == b'<div>' or pieces[0].startswith(b'<div ')) and pieces[-1] == b'</div>':
                    depth = 0
                    for piece in pieces[:-1]:
                        if piece.startswith(b'</'):
                            depth -= 1
                            if depth == 0:
                                break
                        elif piece.startswith(b'<') and not piece.endswith(b'/>'):
                            depth += 1
                    else:
                        pieces = pieces[1:-1]

            for i, v in enumerate(pieces):
                if not isinstance(v, unicode):
                    pieces[i] = v.decode(b'utf-8')

            output = (u'').join(pieces)
            if stripWhitespace:
                output = output.strip()
            if not expectingText:
                return output
            if base64 and self.contentparams.get(b'base64', 0):
                try:
                    output = _base64decode(output)
                except binascii.Error:
                    pass
                except binascii.Incomplete:
                    pass
                except TypeError:
                    output = _base64decode(output.encode(b'utf-8')).decode(b'utf-8')

            if element in self.can_be_relative_uri and output:
                output = self.resolveURI(output)
            if not self.contentparams.get(b'base64', 0):
                output = self.decodeEntities(element, output)
            if not self.version.startswith(u'atom') and self.contentparams.get(b'type') == u'text/plain':
                if self.lookslikehtml(output):
                    self.contentparams[b'type'] = u'text/html'
            try:
                del self.contentparams[b'mode']
            except KeyError:
                pass

            try:
                del self.contentparams[b'base64']
            except KeyError:
                pass

            is_htmlish = self.mapContentType(self.contentparams.get(b'type', u'text/html')) in self.html_types
            if is_htmlish and RESOLVE_RELATIVE_URIS:
                if element in self.can_contain_relative_uris:
                    output = _resolveRelativeURIs(output, self.baseuri, self.encoding, self.contentparams.get(b'type', u'text/html'))
            if PARSE_MICROFORMATS and is_htmlish and element in (b'content', b'description', b'summary'):
                mfresults = _parseMicroformats(output, self.baseuri, self.encoding)
                if mfresults:
                    for tag in mfresults.get(b'tags', []):
                        self._addTag(tag[b'term'], tag[b'scheme'], tag[b'label'])

                    for enclosure in mfresults.get(b'enclosures', []):
                        self._start_enclosure(enclosure)

                    for xfn in mfresults.get(b'xfn', []):
                        self._addXFN(xfn[b'relationships'], xfn[b'href'], xfn[b'name'])

                    vcard = mfresults.get(b'vcard')
                    if vcard:
                        self._getContext()[b'vcard'] = vcard
            if is_htmlish and SANITIZE_HTML:
                if element in self.can_contain_dangerous_markup:
                    output = _sanitizeHTML(output, self.encoding, self.contentparams.get(b'type', u'text/html'))
            if self.encoding and not isinstance(output, unicode):
                output = output.decode(self.encoding, b'ignore')
            if self.encoding in (u'utf-8', u'utf-8_INVALID_PYTHON_3') and isinstance(output, unicode):
                try:
                    output = output.encode(b'iso-8859-1').decode(b'utf-8')
                except (UnicodeEncodeError, UnicodeDecodeError):
                    pass

            if isinstance(output, unicode):
                output = output.translate(_cp1252)
            if element == b'category':
                return output
            if element == b'title':
                if -1 < self.title_depth <= self.depth:
                    return output
                if self.inentry and not self.insource:
                    if element == b'content':
                        self.entries[-1].setdefault(element, [])
                        contentparams = copy.deepcopy(self.contentparams)
                        contentparams[b'value'] = output
                        self.entries[-1][element].append(contentparams)
                    elif element == b'link':
                        output = self.inimage or re.sub(b'&([A-Za-z0-9_]+);', b'&\\g<1>', output)
                        self.entries[-1][element] = output
                        if output:
                            self.entries[-1][b'links'][-1][b'href'] = output
                else:
                    if element == b'description':
                        element = b'summary'
                    old_value_depth = self.property_depth_map.setdefault(self.entries[-1], {}).get(element)
                    if old_value_depth is None or self.depth <= old_value_depth:
                        self.property_depth_map[self.entries[-1]][element] = self.depth
                        self.entries[-1][element] = output
                    if self.incontent:
                        contentparams = copy.deepcopy(self.contentparams)
                        contentparams[b'value'] = output
                        self.entries[-1][element + b'_detail'] = contentparams
            elif self.infeed or self.insource:
                context = self._getContext()
                if element == b'description':
                    element = b'subtitle'
                context[element] = output
                if element == b'link':
                    output = re.sub(b'&([A-Za-z0-9_]+);', b'&\\g<1>', output)
                    context[element] = output
                    context[b'links'][-1][b'href'] = output
                elif self.incontent:
                    contentparams = copy.deepcopy(self.contentparams)
                    contentparams[b'value'] = output
                    context[element + b'_detail'] = contentparams
            return output

    def pushContent(self, tag, attrsD, defaultContentType, expectingText):
        self.incontent += 1
        if self.lang:
            self.lang = self.lang.replace(b'_', b'-')
        self.contentparams = FeedParserDict({b'type': (self.mapContentType(attrsD.get(b'type', defaultContentType))), 
           b'language': (self.lang), 
           b'base': (self.baseuri)})
        self.contentparams[b'base64'] = self._isBase64(attrsD, self.contentparams)
        self.push(tag, expectingText)
        return

    def popContent(self, tag):
        value = self.pop(tag)
        self.incontent -= 1
        self.contentparams.clear()
        return value

    @staticmethod
    def lookslikehtml(s):
        if not (re.search(b'</(\\w+)>', s) or re.search(b'&#?\\w+;', s)):
            return
        if filter((lambda t: t.lower() not in _HTMLSanitizer.acceptable_elements), re.findall(b'</?(\\w+)', s)):
            return
        if filter((lambda e: e not in entitydefs.keys()), re.findall(b'&(\\w+);', s)):
            return
        return 1

    def _mapToStandardPrefix(self, name):
        colonpos = name.find(b':')
        if colonpos != -1:
            prefix = name[:colonpos]
            suffix = name[colonpos + 1:]
            prefix = self.namespacemap.get(prefix, prefix)
            name = prefix + b':' + suffix
        return name

    def _getAttribute(self, attrsD, name):
        return attrsD.get(self._mapToStandardPrefix(name))

    def _isBase64(self, attrsD, contentparams):
        if attrsD.get(b'mode', b'') == b'base64':
            return 1
        if self.contentparams[b'type'].startswith(u'text/'):
            return 0
        if self.contentparams[b'type'].endswith(u'+xml'):
            return 0
        if self.contentparams[b'type'].endswith(u'/xml'):
            return 0
        return 1

    def _itsAnHrefDamnIt(self, attrsD):
        href = attrsD.get(b'url', attrsD.get(b'uri', attrsD.get(b'href', None)))
        if href:
            try:
                del attrsD[b'url']
            except KeyError:
                pass

            try:
                del attrsD[b'uri']
            except KeyError:
                pass

            attrsD[b'href'] = href
        return attrsD

    def _save(self, key, value, overwrite=False):
        context = self._getContext()
        if overwrite:
            context[key] = value
        else:
            context.setdefault(key, value)
        return

    def _start_rss(self, attrsD):
        versionmap = {b'0.91': u'rss091u', b'0.92': u'rss092', b'0.93': u'rss093', 
           b'0.94': u'rss094'}
        if not self.version or not self.version.startswith(u'rss'):
            attr_version = attrsD.get(b'version', b'')
            version = versionmap.get(attr_version)
            if version:
                self.version = version
            elif attr_version.startswith(b'2.'):
                self.version = u'rss20'
            else:
                self.version = u'rss'
        return

    def _start_channel(self, attrsD):
        self.infeed = 1
        self._cdf_common(attrsD)
        return

    def _cdf_common(self, attrsD):
        if b'lastmod' in attrsD:
            self._start_modified({})
            self.elementstack[-1][-1] = attrsD[b'lastmod']
            self._end_modified()
        if b'href' in attrsD:
            self._start_link({})
            self.elementstack[-1][-1] = attrsD[b'href']
            self._end_link()
        return

    def _start_feed(self, attrsD):
        self.infeed = 1
        versionmap = {b'0.1': u'atom01', b'0.2': u'atom02', 
           b'0.3': u'atom03'}
        if not self.version:
            attr_version = attrsD.get(b'version')
            version = versionmap.get(attr_version)
            if version:
                self.version = version
            else:
                self.version = u'atom'
        return

    def _end_channel(self):
        self.infeed = 0
        return

    _end_feed = _end_channel

    def _start_image(self, attrsD):
        context = self._getContext()
        if not self.inentry:
            context.setdefault(b'image', FeedParserDict())
        self.inimage = 1
        self.title_depth = -1
        self.push(b'image', 0)
        return

    def _end_image(self):
        self.pop(b'image')
        self.inimage = 0
        return

    def _start_textinput(self, attrsD):
        context = self._getContext()
        context.setdefault(b'textinput', FeedParserDict())
        self.intextinput = 1
        self.title_depth = -1
        self.push(b'textinput', 0)
        return

    _start_textInput = _start_textinput

    def _end_textinput(self):
        self.pop(b'textinput')
        self.intextinput = 0
        return

    _end_textInput = _end_textinput

    def _start_author(self, attrsD):
        self.inauthor = 1
        self.push(b'author', 1)
        context = self._getContext()
        context.setdefault(b'authors', [])
        context[b'authors'].append(FeedParserDict())
        return

    _start_managingeditor = _start_author
    _start_dc_author = _start_author
    _start_dc_creator = _start_author
    _start_itunes_author = _start_author

    def _end_author(self):
        self.pop(b'author')
        self.inauthor = 0
        self._sync_author_detail()
        return

    _end_managingeditor = _end_author
    _end_dc_author = _end_author
    _end_dc_creator = _end_author
    _end_itunes_author = _end_author

    def _start_itunes_owner(self, attrsD):
        self.inpublisher = 1
        self.push(b'publisher', 0)
        return

    def _end_itunes_owner(self):
        self.pop(b'publisher')
        self.inpublisher = 0
        self._sync_author_detail(b'publisher')
        return

    def _start_contributor(self, attrsD):
        self.incontributor = 1
        context = self._getContext()
        context.setdefault(b'contributors', [])
        context[b'contributors'].append(FeedParserDict())
        self.push(b'contributor', 0)
        return

    def _end_contributor(self):
        self.pop(b'contributor')
        self.incontributor = 0
        return

    def _start_dc_contributor(self, attrsD):
        self.incontributor = 1
        context = self._getContext()
        context.setdefault(b'contributors', [])
        context[b'contributors'].append(FeedParserDict())
        self.push(b'name', 0)
        return

    def _end_dc_contributor(self):
        self._end_name()
        self.incontributor = 0
        return

    def _start_name(self, attrsD):
        self.push(b'name', 0)
        return

    _start_itunes_name = _start_name

    def _end_name(self):
        value = self.pop(b'name')
        if self.inpublisher:
            self._save_author(b'name', value, b'publisher')
        elif self.inauthor:
            self._save_author(b'name', value)
        elif self.incontributor:
            self._save_contributor(b'name', value)
        elif self.intextinput:
            context = self._getContext()
            context[b'name'] = value
        return

    _end_itunes_name = _end_name

    def _start_width(self, attrsD):
        self.push(b'width', 0)
        return

    def _end_width(self):
        value = self.pop(b'width')
        try:
            value = int(value)
        except ValueError:
            value = 0

        if self.inimage:
            context = self._getContext()
            context[b'width'] = value
        return

    def _start_height(self, attrsD):
        self.push(b'height', 0)
        return

    def _end_height(self):
        value = self.pop(b'height')
        try:
            value = int(value)
        except ValueError:
            value = 0

        if self.inimage:
            context = self._getContext()
            context[b'height'] = value
        return

    def _start_url(self, attrsD):
        self.push(b'href', 1)
        return

    _start_homepage = _start_url
    _start_uri = _start_url

    def _end_url(self):
        value = self.pop(b'href')
        if self.inauthor:
            self._save_author(b'href', value)
        elif self.incontributor:
            self._save_contributor(b'href', value)
        return

    _end_homepage = _end_url
    _end_uri = _end_url

    def _start_email(self, attrsD):
        self.push(b'email', 0)
        return

    _start_itunes_email = _start_email

    def _end_email(self):
        value = self.pop(b'email')
        if self.inpublisher:
            self._save_author(b'email', value, b'publisher')
        elif self.inauthor:
            self._save_author(b'email', value)
        elif self.incontributor:
            self._save_contributor(b'email', value)
        return

    _end_itunes_email = _end_email

    def _getContext(self):
        if self.insource:
            context = self.sourcedata
        elif self.inimage and b'image' in self.feeddata:
            context = self.feeddata[b'image']
        elif self.intextinput:
            context = self.feeddata[b'textinput']
        elif self.inentry:
            context = self.entries[-1]
        else:
            context = self.feeddata
        return context

    def _save_author(self, key, value, prefix=b'author'):
        context = self._getContext()
        context.setdefault(prefix + b'_detail', FeedParserDict())
        context[prefix + b'_detail'][key] = value
        self._sync_author_detail()
        context.setdefault(b'authors', [FeedParserDict()])
        context[b'authors'][-1][key] = value
        return

    def _save_contributor(self, key, value):
        context = self._getContext()
        context.setdefault(b'contributors', [FeedParserDict()])
        context[b'contributors'][-1][key] = value
        return

    def _sync_author_detail(self, key=b'author'):
        context = self._getContext()
        detail = context.get(b'%s_detail' % key)
        if detail:
            name = detail.get(b'name')
            email = detail.get(b'email')
            if name and email:
                context[key] = u'%s (%s)' % (name, email)
            elif name:
                context[key] = name
            elif email:
                context[key] = email
        else:
            author, email = context.get(key), None
            if not author:
                return
            emailmatch = re.search(u'(([a-zA-Z0-9\\_\\-\\.\\+]+)@((\\[[0-9]{1,3}\\.[0-9]{1,3}\\.[0-9]{1,3}\\.)|(([a-zA-Z0-9\\-]+\\.)+))([a-zA-Z]{2,4}|[0-9]{1,3})(\\]?))(\\?subject=\\S+)?', author)
            if emailmatch:
                email = emailmatch.group(0)
                author = author.replace(email, u'')
                author = author.replace(u'()', u'')
                author = author.replace(u'<>', u'')
                author = author.replace(u'&lt;&gt;', u'')
                author = author.strip()
                if author and author[0] == u'(':
                    author = author[1:]
                if author and author[-1] == u')':
                    author = author[:-1]
                author = author.strip()
            if author or email:
                context.setdefault(b'%s_detail' % key, FeedParserDict())
            if author:
                context[b'%s_detail' % key][b'name'] = author
            if email:
                context[b'%s_detail' % key][b'email'] = email
        return

    def _start_subtitle(self, attrsD):
        self.pushContent(b'subtitle', attrsD, u'text/plain', 1)
        return

    _start_tagline = _start_subtitle
    _start_itunes_subtitle = _start_subtitle

    def _end_subtitle(self):
        self.popContent(b'subtitle')
        return

    _end_tagline = _end_subtitle
    _end_itunes_subtitle = _end_subtitle

    def _start_rights(self, attrsD):
        self.pushContent(b'rights', attrsD, u'text/plain', 1)
        return

    _start_dc_rights = _start_rights
    _start_copyright = _start_rights

    def _end_rights(self):
        self.popContent(b'rights')
        return

    _end_dc_rights = _end_rights
    _end_copyright = _end_rights

    def _start_item(self, attrsD):
        self.entries.append(FeedParserDict())
        self.push(b'item', 0)
        self.inentry = 1
        self.guidislink = 0
        self.title_depth = -1
        id = self._getAttribute(attrsD, b'rdf:about')
        if id:
            context = self._getContext()
            context[b'id'] = id
        self._cdf_common(attrsD)
        return

    _start_entry = _start_item

    def _end_item(self):
        self.pop(b'item')
        self.inentry = 0
        return

    _end_entry = _end_item

    def _start_dc_language(self, attrsD):
        self.push(b'language', 1)
        return

    _start_language = _start_dc_language

    def _end_dc_language(self):
        self.lang = self.pop(b'language')
        return

    _end_language = _end_dc_language

    def _start_dc_publisher(self, attrsD):
        self.push(b'publisher', 1)
        return

    _start_webmaster = _start_dc_publisher

    def _end_dc_publisher(self):
        self.pop(b'publisher')
        self._sync_author_detail(b'publisher')
        return

    _end_webmaster = _end_dc_publisher

    def _start_published(self, attrsD):
        self.push(b'published', 1)
        return

    _start_dcterms_issued = _start_published
    _start_issued = _start_published
    _start_pubdate = _start_published

    def _end_published(self):
        value = self.pop(b'published')
        self._save(b'published_parsed', _parse_date(value), overwrite=True)
        return

    _end_dcterms_issued = _end_published
    _end_issued = _end_published
    _end_pubdate = _end_published

    def _start_updated(self, attrsD):
        self.push(b'updated', 1)
        return

    _start_modified = _start_updated
    _start_dcterms_modified = _start_updated
    _start_dc_date = _start_updated
    _start_lastbuilddate = _start_updated

    def _end_updated(self):
        value = self.pop(b'updated')
        parsed_value = _parse_date(value)
        self._save(b'updated_parsed', parsed_value, overwrite=True)
        return

    _end_modified = _end_updated
    _end_dcterms_modified = _end_updated
    _end_dc_date = _end_updated
    _end_lastbuilddate = _end_updated

    def _start_created(self, attrsD):
        self.push(b'created', 1)
        return

    _start_dcterms_created = _start_created

    def _end_created(self):
        value = self.pop(b'created')
        self._save(b'created_parsed', _parse_date(value), overwrite=True)
        return

    _end_dcterms_created = _end_created

    def _start_expirationdate(self, attrsD):
        self.push(b'expired', 1)
        return

    def _end_expirationdate(self):
        self._save(b'expired_parsed', _parse_date(self.pop(b'expired')), overwrite=True)
        return

    def _start_cc_license(self, attrsD):
        context = self._getContext()
        value = self._getAttribute(attrsD, b'rdf:resource')
        attrsD = FeedParserDict()
        attrsD[b'rel'] = u'license'
        if value:
            attrsD[b'href'] = value
        context.setdefault(b'links', []).append(attrsD)
        return

    def _start_creativecommons_license(self, attrsD):
        self.push(b'license', 1)
        return

    _start_creativeCommons_license = _start_creativecommons_license

    def _end_creativecommons_license(self):
        value = self.pop(b'license')
        context = self._getContext()
        attrsD = FeedParserDict()
        attrsD[b'rel'] = u'license'
        if value:
            attrsD[b'href'] = value
        context.setdefault(b'links', []).append(attrsD)
        del context[b'license']
        return

    _end_creativeCommons_license = _end_creativecommons_license

    def _addXFN(self, relationships, href, name):
        context = self._getContext()
        xfn = context.setdefault(b'xfn', [])
        value = FeedParserDict({b'relationships': relationships, b'href': href, b'name': name})
        if value not in xfn:
            xfn.append(value)
        return

    def _addTag(self, term, scheme, label):
        context = self._getContext()
        tags = context.setdefault(b'tags', [])
        if not term and not scheme and not label:
            return
        value = FeedParserDict({b'term': term, b'scheme': scheme, b'label': label})
        if value not in tags:
            tags.append(value)
        return

    def _start_category(self, attrsD):
        term = attrsD.get(b'term')
        scheme = attrsD.get(b'scheme', attrsD.get(b'domain'))
        label = attrsD.get(b'label')
        self._addTag(term, scheme, label)
        self.push(b'category', 1)
        return

    _start_dc_subject = _start_category
    _start_keywords = _start_category

    def _start_media_category(self, attrsD):
        attrsD.setdefault(b'scheme', u'http://search.yahoo.com/mrss/category_schema')
        self._start_category(attrsD)
        return

    def _end_itunes_keywords(self):
        for term in self.pop(b'itunes_keywords').split(b','):
            if term.strip():
                self._addTag(term.strip(), u'http://www.itunes.com/', None)

        return

    def _start_itunes_category(self, attrsD):
        self._addTag(attrsD.get(b'text'), u'http://www.itunes.com/', None)
        self.push(b'category', 1)
        return

    def _end_category(self):
        value = self.pop(b'category')
        if not value:
            return
        else:
            context = self._getContext()
            tags = context[b'tags']
            if value and len(tags) and not tags[-1][b'term']:
                tags[-1][b'term'] = value
            else:
                self._addTag(value, None, None)
            return

    _end_dc_subject = _end_category
    _end_keywords = _end_category
    _end_itunes_category = _end_category
    _end_media_category = _end_category

    def _start_cloud(self, attrsD):
        self._getContext()[b'cloud'] = FeedParserDict(attrsD)
        return

    def _start_link(self, attrsD):
        attrsD.setdefault(b'rel', u'alternate')
        if attrsD[b'rel'] == u'self':
            attrsD.setdefault(b'type', u'application/atom+xml')
        else:
            attrsD.setdefault(b'type', u'text/html')
        context = self._getContext()
        attrsD = self._itsAnHrefDamnIt(attrsD)
        if b'href' in attrsD:
            attrsD[b'href'] = self.resolveURI(attrsD[b'href'])
        expectingText = self.infeed or self.inentry or self.insource
        context.setdefault(b'links', [])
        if not (self.inentry and self.inimage):
            context[b'links'].append(FeedParserDict(attrsD))
        if b'href' in attrsD:
            expectingText = 0
            if attrsD.get(b'rel') == u'alternate' and self.mapContentType(attrsD.get(b'type')) in self.html_types:
                context[b'link'] = attrsD[b'href']
        else:
            self.push(b'link', expectingText)
        return

    def _end_link(self):
        value = self.pop(b'link')
        return

    def _start_guid(self, attrsD):
        self.guidislink = attrsD.get(b'ispermalink', b'true') == b'true'
        self.push(b'id', 1)
        return

    _start_id = _start_guid

    def _end_guid(self):
        value = self.pop(b'id')
        self._save(b'guidislink', self.guidislink and b'link' not in self._getContext())
        if self.guidislink:
            self._save(b'link', value)
        return

    _end_id = _end_guid

    def _start_title(self, attrsD):
        if self.svgOK:
            return self.unknown_starttag(b'title', attrsD.items())
        self.pushContent(b'title', attrsD, u'text/plain', self.infeed or self.inentry or self.insource)
        return

    _start_dc_title = _start_title
    _start_media_title = _start_title

    def _end_title(self):
        if self.svgOK:
            return
        value = self.popContent(b'title')
        if not value:
            return
        self.title_depth = self.depth
        return

    _end_dc_title = _end_title

    def _end_media_title(self):
        title_depth = self.title_depth
        self._end_title()
        self.title_depth = title_depth
        return

    def _start_description(self, attrsD):
        context = self._getContext()
        if b'summary' in context:
            self._summaryKey = b'content'
            self._start_content(attrsD)
        else:
            self.pushContent(b'description', attrsD, u'text/html', self.infeed or self.inentry or self.insource)
        return

    _start_dc_description = _start_description

    def _start_abstract(self, attrsD):
        self.pushContent(b'description', attrsD, u'text/plain', self.infeed or self.inentry or self.insource)
        return

    def _end_description(self):
        if self._summaryKey == b'content':
            self._end_content()
        else:
            value = self.popContent(b'description')
        self._summaryKey = None
        return

    _end_abstract = _end_description
    _end_dc_description = _end_description

    def _start_info(self, attrsD):
        self.pushContent(b'info', attrsD, u'text/plain', 1)
        return

    _start_feedburner_browserfriendly = _start_info

    def _end_info(self):
        self.popContent(b'info')
        return

    _end_feedburner_browserfriendly = _end_info

    def _start_generator(self, attrsD):
        if attrsD:
            attrsD = self._itsAnHrefDamnIt(attrsD)
            if b'href' in attrsD:
                attrsD[b'href'] = self.resolveURI(attrsD[b'href'])
        self._getContext()[b'generator_detail'] = FeedParserDict(attrsD)
        self.push(b'generator', 1)
        return

    def _end_generator(self):
        value = self.pop(b'generator')
        context = self._getContext()
        if b'generator_detail' in context:
            context[b'generator_detail'][b'name'] = value
        return

    def _start_admin_generatoragent(self, attrsD):
        self.push(b'generator', 1)
        value = self._getAttribute(attrsD, b'rdf:resource')
        if value:
            self.elementstack[-1][2].append(value)
        self.pop(b'generator')
        self._getContext()[b'generator_detail'] = FeedParserDict({b'href': value})
        return

    def _start_admin_errorreportsto(self, attrsD):
        self.push(b'errorreportsto', 1)
        value = self._getAttribute(attrsD, b'rdf:resource')
        if value:
            self.elementstack[-1][2].append(value)
        self.pop(b'errorreportsto')
        return

    def _start_summary(self, attrsD):
        context = self._getContext()
        if b'summary' in context:
            self._summaryKey = b'content'
            self._start_content(attrsD)
        else:
            self._summaryKey = b'summary'
            self.pushContent(self._summaryKey, attrsD, u'text/plain', 1)
        return

    _start_itunes_summary = _start_summary

    def _end_summary(self):
        if self._summaryKey == b'content':
            self._end_content()
        else:
            self.popContent(self._summaryKey or b'summary')
        self._summaryKey = None
        return

    _end_itunes_summary = _end_summary

    def _start_enclosure(self, attrsD):
        attrsD = self._itsAnHrefDamnIt(attrsD)
        context = self._getContext()
        attrsD[b'rel'] = u'enclosure'
        context.setdefault(b'links', []).append(FeedParserDict(attrsD))
        return

    def _start_source(self, attrsD):
        if b'url' in attrsD:
            self.sourcedata[b'href'] = attrsD[u'url']
        self.push(b'source', 1)
        self.insource = 1
        self.title_depth = -1
        return

    def _end_source(self):
        self.insource = 0
        value = self.pop(b'source')
        if value:
            self.sourcedata[b'title'] = value
        self._getContext()[b'source'] = copy.deepcopy(self.sourcedata)
        self.sourcedata.clear()
        return

    def _start_content(self, attrsD):
        self.pushContent(b'content', attrsD, u'text/plain', 1)
        src = attrsD.get(b'src')
        if src:
            self.contentparams[b'src'] = src
        self.push(b'content', 1)
        return

    def _start_body(self, attrsD):
        self.pushContent(b'content', attrsD, u'application/xhtml+xml', 1)
        return

    _start_xhtml_body = _start_body

    def _start_content_encoded(self, attrsD):
        self.pushContent(b'content', attrsD, u'text/html', 1)
        return

    _start_fullitem = _start_content_encoded

    def _end_content(self):
        copyToSummary = self.mapContentType(self.contentparams.get(b'type')) in [u'text/plain'] + self.html_types
        value = self.popContent(b'content')
        if copyToSummary:
            self._save(b'summary', value)
        return

    _end_body = _end_content
    _end_xhtml_body = _end_content
    _end_content_encoded = _end_content
    _end_fullitem = _end_content

    def _start_itunes_image(self, attrsD):
        self.push(b'itunes_image', 0)
        if attrsD.get(b'href'):
            self._getContext()[b'image'] = FeedParserDict({b'href': (attrsD.get(b'href'))})
        elif attrsD.get(b'url'):
            self._getContext()[b'image'] = FeedParserDict({b'href': (attrsD.get(b'url'))})
        return

    _start_itunes_link = _start_itunes_image

    def _end_itunes_block(self):
        value = self.pop(b'itunes_block', 0)
        self._getContext()[b'itunes_block'] = value == b'yes' and 1 or 0
        return

    def _end_itunes_explicit(self):
        value = self.pop(b'itunes_explicit', 0)
        self._getContext()[b'itunes_explicit'] = (
         None, False, True)[value == b'yes' and 2 or value == b'clean' or 0]
        return

    def _start_media_content(self, attrsD):
        context = self._getContext()
        context.setdefault(b'media_content', [])
        context[b'media_content'].append(attrsD)
        return

    def _start_media_thumbnail(self, attrsD):
        context = self._getContext()
        context.setdefault(b'media_thumbnail', [])
        self.push(b'url', 1)
        context[b'media_thumbnail'].append(attrsD)
        return

    def _end_media_thumbnail(self):
        url = self.pop(b'url')
        context = self._getContext()
        if url != None and len(url.strip()) != 0:
            if b'url' not in context[b'media_thumbnail'][-1]:
                context[b'media_thumbnail'][-1][b'url'] = url
        return

    def _start_media_player(self, attrsD):
        self.push(b'media_player', 0)
        self._getContext()[b'media_player'] = FeedParserDict(attrsD)
        return

    def _end_media_player(self):
        value = self.pop(b'media_player')
        context = self._getContext()
        context[b'media_player'][b'content'] = value
        return

    def _start_newlocation(self, attrsD):
        self.push(b'newlocation', 1)
        return

    def _end_newlocation(self):
        url = self.pop(b'newlocation')
        context = self._getContext()
        if context is not self.feeddata:
            return
        context[b'newlocation'] = _makeSafeAbsoluteURI(self.baseuri, url.strip())
        return


if _XML_AVAILABLE:

    class _StrictFeedParser(_FeedParserMixin, xml.sax.handler.ContentHandler):

        def __init__(self, baseuri, baselang, encoding):
            xml.sax.handler.ContentHandler.__init__(self)
            _FeedParserMixin.__init__(self, baseuri, baselang, encoding)
            self.bozo = 0
            self.exc = None
            self.decls = {}
            return

        def startPrefixMapping(self, prefix, uri):
            if not uri:
                return
            else:
                prefix = prefix or None
                self.trackNamespace(prefix, uri)
                if prefix and uri == b'http://www.w3.org/1999/xlink':
                    self.decls[b'xmlns:' + prefix] = uri
                return

        def startElementNS(self, name, qname, attrs):
            namespace, localname = name
            lowernamespace = str(namespace or b'').lower()
            if lowernamespace.find(u'backend.userland.com/rss') != -1:
                namespace = u'http://backend.userland.com/rss'
                lowernamespace = namespace
            if qname and qname.find(b':') > 0:
                givenprefix = qname.split(b':')[0]
            else:
                givenprefix = None
            prefix = self._matchnamespaces.get(lowernamespace, givenprefix)
            if givenprefix and (prefix == None or prefix == b'' and lowernamespace == b'') and givenprefix not in self.namespacesInUse:
                raise UndeclaredNamespace, b"'%s' is not associated with a namespace" % givenprefix
            localname = str(localname).lower()
            attrsD, self.decls = self.decls, {}
            if localname == b'math' and namespace == b'http://www.w3.org/1998/Math/MathML':
                attrsD[b'xmlns'] = namespace
            if localname == b'svg' and namespace == b'http://www.w3.org/2000/svg':
                attrsD[b'xmlns'] = namespace
            if prefix:
                localname = prefix.lower() + b':' + localname
            elif namespace and not qname:
                for name, value in self.namespacesInUse.items():
                    if name and value == namespace:
                        localname = name + b':' + localname
                        break

            for (namespace, attrlocalname), attrvalue in attrs.items():
                lowernamespace = (namespace or b'').lower()
                prefix = self._matchnamespaces.get(lowernamespace, b'')
                if prefix:
                    attrlocalname = prefix + b':' + attrlocalname
                attrsD[str(attrlocalname).lower()] = attrvalue

            for qname in attrs.getQNames():
                attrsD[str(qname).lower()] = attrs.getValueByQName(qname)

            self.unknown_starttag(localname, attrsD.items())
            return

        def characters(self, text):
            self.handle_data(text)
            return

        def endElementNS(self, name, qname):
            namespace, localname = name
            lowernamespace = str(namespace or b'').lower()
            if qname and qname.find(b':') > 0:
                givenprefix = qname.split(b':')[0]
            else:
                givenprefix = b''
            prefix = self._matchnamespaces.get(lowernamespace, givenprefix)
            if prefix:
                localname = prefix + b':' + localname
            elif namespace and not qname:
                for name, value in self.namespacesInUse.items():
                    if name and value == namespace:
                        localname = name + b':' + localname
                        break

            localname = str(localname).lower()
            self.unknown_endtag(localname)
            return

        def error(self, exc):
            self.bozo = 1
            self.exc = exc
            return

        warning = error

        def fatalError(self, exc):
            self.error(exc)
            raise exc
            return


class _BaseHTMLProcessor(sgmllib.SGMLParser):
    special = re.compile(b'[<>\'"]')
    bare_ampersand = re.compile(b'&(?!#\\d+;|#x[0-9a-fA-F]+;|\\w+;)')
    elements_no_end_tag = set([
     2, 3, 4, 5, 6, 7, 8, 9, 
     10, 11, 12, 13, 14, 
     15, 16, 17, 
     18, 19, 20])

    def __init__(self, encoding, _type):
        self.encoding = encoding
        self._type = _type
        sgmllib.SGMLParser.__init__(self)
        return

    def reset(self):
        self.pieces = []
        sgmllib.SGMLParser.reset(self)
        return

    def _shorttag_replace(self, match):
        tag = match.group(1)
        if tag in self.elements_no_end_tag:
            return b'<' + tag + b' />'
        else:
            return b'<' + tag + b'></' + tag + b'>'

        return

    def goahead(self, i):
        return

    goahead.func_code = sgmllib.SGMLParser.goahead.func_code

    def __parse_starttag(self, i):
        return

    __parse_starttag.func_code = sgmllib.SGMLParser.parse_starttag.func_code

    def parse_starttag(self, i):
        j = self.__parse_starttag(i)
        if self._type == b'application/xhtml+xml':
            if j > 2 and self.rawdata[j - 2:j] == b'/>':
                self.unknown_endtag(self.lasttag)
        return j

    def feed(self, data):
        data = re.compile(b'<!((?!DOCTYPE|--|\\[))', re.IGNORECASE).sub(b'&lt;!\\1', data)
        data = re.sub(b'<([^<>\\s]+?)\\s*/>', self._shorttag_replace, data)
        data = data.replace(b'&#39;', b"'")
        data = data.replace(b'&#34;', b'"')
        try:
            bytes
            if bytes is str:
                raise NameError
            self.encoding = self.encoding + u'_INVALID_PYTHON_3'
        except NameError:
            if self.encoding and isinstance(data, unicode):
                data = data.encode(self.encoding)

        sgmllib.SGMLParser.feed(self, data)
        sgmllib.SGMLParser.close(self)
        return

    def normalize_attrs(self, attrs):
        if not attrs:
            return attrs
        attrs = dict([(k.lower(), v) for k, v in attrs]).items()
        attrs = [(k, k in (b'rel', b'type') and v.lower() or v) for k, v in attrs]
        attrs.sort()
        return attrs

    def unknown_starttag(self, tag, attrs):
        uattrs = []
        strattrs = b''
        if attrs:
            for key, value in attrs:
                value = value.replace(b'>', b'&gt;').replace(b'<', b'&lt;').replace(b'"', b'&quot;')
                value = self.bare_ampersand.sub(b'&amp;', value)
                if not isinstance(value, unicode):
                    value = value.decode(self.encoding, b'ignore')
                try:
                    uattrs.append((unicode(key, self.encoding), value))
                except TypeError:
                    uattrs.append((key, value))

            strattrs = (u'').join([u' %s="%s"' % (key, value) for key, value in uattrs])
            if self.encoding:
                try:
                    strattrs = strattrs.encode(self.encoding)
                except (UnicodeEncodeError, LookupError):
                    pass

        if tag in self.elements_no_end_tag:
            self.pieces.append(b'<%s%s />' % (tag, strattrs))
        else:
            self.pieces.append(b'<%s%s>' % (tag, strattrs))
        return

    def unknown_endtag(self, tag):
        if tag not in self.elements_no_end_tag:
            self.pieces.append(b'</%s>' % tag)
        return

    def handle_charref(self, ref):
        if ref.startswith(b'x'):
            value = int(ref[1:], 16)
        else:
            value = int(ref)
        if value in _cp1252:
            self.pieces.append(b'&#%s;' % hex(ord(_cp1252[value]))[1:])
        else:
            self.pieces.append(b'&#%s;' % ref)
        return

    def handle_entityref(self, ref):
        if ref in name2codepoint or ref == b'apos':
            self.pieces.append(b'&%s;' % ref)
        else:
            self.pieces.append(b'&amp;%s' % ref)
        return

    def handle_data(self, text):
        self.pieces.append(text)
        return

    def handle_comment(self, text):
        self.pieces.append(b'<!--%s-->' % text)
        return

    def handle_pi(self, text):
        self.pieces.append(b'<?%s>' % text)
        return

    def handle_decl(self, text):
        self.pieces.append(b'<!%s>' % text)
        return

    _new_declname_match = re.compile(b'[a-zA-Z][-_.a-zA-Z0-9:]*\\s*').match

    def _scan_name(self, i, declstartpos):
        rawdata = self.rawdata
        n = len(rawdata)
        if i == n:
            return (None, -1)
        else:
            m = self._new_declname_match(rawdata, i)
            if m:
                s = m.group()
                name = s.strip()
                if i + len(s) == n:
                    return (None, -1)
                return (name.lower(), m.end())
            self.handle_data(rawdata)
            return (None, -1)
            return

    def convert_charref(self, name):
        return b'&#%s;' % name

    def convert_entityref(self, name):
        return b'&%s;' % name

    def output(self):
        return (b'').join([str(p) for p in self.pieces])

    def parse_declaration(self, i):
        try:
            return sgmllib.SGMLParser.parse_declaration(self, i)
        except sgmllib.SGMLParseError:
            self.handle_data(b'&lt;')
            return i + 1

        return


class _LooseFeedParser(_FeedParserMixin, _BaseHTMLProcessor):

    def __init__(self, baseuri, baselang, encoding, entities):
        sgmllib.SGMLParser.__init__(self)
        _FeedParserMixin.__init__(self, baseuri, baselang, encoding)
        _BaseHTMLProcessor.__init__(self, encoding, b'application/xhtml+xml')
        self.entities = entities
        return

    def decodeEntities(self, element, data):
        data = data.replace(b'&#60;', b'&lt;')
        data = data.replace(b'&#x3c;', b'&lt;')
        data = data.replace(b'&#x3C;', b'&lt;')
        data = data.replace(b'&#62;', b'&gt;')
        data = data.replace(b'&#x3e;', b'&gt;')
        data = data.replace(b'&#x3E;', b'&gt;')
        data = data.replace(b'&#38;', b'&amp;')
        data = data.replace(b'&#x26;', b'&amp;')
        data = data.replace(b'&#34;', b'&quot;')
        data = data.replace(b'&#x22;', b'&quot;')
        data = data.replace(b'&#39;', b'&apos;')
        data = data.replace(b'&#x27;', b'&apos;')
        if not self.contentparams.get(b'type', u'xml').endswith(u'xml'):
            data = data.replace(b'&lt;', b'<')
            data = data.replace(b'&gt;', b'>')
            data = data.replace(b'&amp;', b'&')
            data = data.replace(b'&quot;', b'"')
            data = data.replace(b'&apos;', b"'")
        return data

    def strattrs(self, attrs):
        return (b'').join([b' %s="%s"' % (n, v.replace(b'"', b'&quot;')) for n, v in attrs])


class _MicroformatsParser():
    STRING = 1
    DATE = 2
    URI = 3
    NODE = 4
    EMAIL = 5
    known_xfn_relationships = set([5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 
     22, 23, 24, 25, 26, 27, 28, 29])
    known_binary_extensions = set([30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 
     46, 37, 47, 31, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 
     58, 59, 60])

    def __init__(self, data, baseuri, encoding):
        self.document = BeautifulSoup.BeautifulSoup(data)
        self.baseuri = baseuri
        self.encoding = encoding
        if isinstance(data, unicode):
            data = data.encode(encoding)
        self.tags = []
        self.enclosures = []
        self.xfn = []
        self.vcard = None
        return

    def vcardEscape(self, s):
        if isinstance(s, basestring):
            s = s.replace(b',', b'\\,').replace(b';', b'\\;').replace(b'\n', b'\\n')
        return s

    def vcardFold(self, s):
        s = re.sub(b';+$', b'', s)
        sFolded = b''
        iMax = 75
        sPrefix = b''
        while len(s) > iMax:
            sFolded += sPrefix + s[:iMax] + b'\n'
            s = s[iMax:]
            sPrefix = b' '
            iMax = 74

        sFolded += sPrefix + s
        return sFolded

    def normalize(self, s):
        return re.sub(b'\\s+', b' ', s).strip()

    def unique(self, aList):
        results = []
        for element in aList:
            if element not in results:
                results.append(element)

        return results

    def toISO8601(self, dt):
        return time.strftime(b'%Y-%m-%dT%H:%M:%SZ', dt)

    def getPropertyValue(self, elmRoot, sProperty, iPropertyType=4, bAllowMultiple=0, bAutoEscape=0):
        all = lambda x: 1
        sProperty = sProperty.lower()
        bFound = 0
        bNormalize = 1
        propertyMatch = {b'class': (re.compile(b'\\b%s\\b' % sProperty))}
        if bAllowMultiple and iPropertyType != self.NODE:
            snapResults = []
            containers = elmRoot([b'ul', b'ol'], propertyMatch)
            for container in containers:
                snapResults.extend(container(b'li'))

            bFound = len(snapResults) != 0
        if not bFound:
            snapResults = elmRoot(all, propertyMatch)
            bFound = len(snapResults) != 0
        if not bFound and sProperty == b'value':
            snapResults = elmRoot(b'pre')
            bFound = len(snapResults) != 0
            bNormalize = not bFound
            if not bFound:
                snapResults = [
                 elmRoot]
                bFound = len(snapResults) != 0
        arFilter = []
        if sProperty == b'vcard':
            snapFilter = elmRoot(all, propertyMatch)
            for node in snapFilter:
                if node.findParent(all, propertyMatch):
                    arFilter.append(node)

        arResults = []
        for node in snapResults:
            if node not in arFilter:
                arResults.append(node)

        bFound = len(arResults) != 0
        if not bFound:
            if bAllowMultiple:
                return []
            else:
                if iPropertyType == self.STRING:
                    return b''
                if iPropertyType == self.DATE:
                    return
                if iPropertyType == self.URI:
                    return b''
                if iPropertyType == self.NODE:
                    return
                return

        arValues = []
        for elmResult in arResults:
            sValue = None
            if iPropertyType == self.NODE:
                if bAllowMultiple:
                    arValues.append(elmResult)
                    continue
                else:
                    return elmResult
            sNodeName = elmResult.name.lower()
            if iPropertyType == self.EMAIL and sNodeName == b'a':
                sValue = (elmResult.get(b'href') or b'').split(b'mailto:').pop().split(b'?')[0]
            if sValue:
                sValue = bNormalize and self.normalize(sValue) or sValue.strip()
            if not sValue and sNodeName == b'abbr':
                sValue = elmResult.get(b'title')
            if sValue:
                sValue = bNormalize and self.normalize(sValue) or sValue.strip()
            if not sValue and iPropertyType == self.URI:
                if sNodeName == b'a':
                    sValue = elmResult.get(b'href')
                elif sNodeName == b'img':
                    sValue = elmResult.get(b'src')
                elif sNodeName == b'object':
                    sValue = elmResult.get(b'data')
            if sValue:
                sValue = bNormalize and self.normalize(sValue) or sValue.strip()
            if not sValue and sNodeName == b'img':
                sValue = elmResult.get(b'alt')
            if sValue:
                sValue = bNormalize and self.normalize(sValue) or sValue.strip()
            if not sValue:
                sValue = elmResult.renderContents()
                sValue = re.sub(b'<\\S[^>]*>', b'', sValue)
                sValue = sValue.replace(b'\r\n', b'\n')
                sValue = sValue.replace(b'\r', b'\n')
            if sValue:
                sValue = bNormalize and self.normalize(sValue) or sValue.strip()
            if not sValue:
                continue
            if iPropertyType == self.DATE:
                sValue = _parse_date_iso8601(sValue)
            if bAllowMultiple:
                arValues.append(bAutoEscape and self.vcardEscape(sValue) or sValue)
            else:
                return bAutoEscape and self.vcardEscape(sValue) or sValue

        return arValues

    def findVCards(self, elmRoot, bAgentParsing=0):
        sVCards = b''
        if not bAgentParsing:
            arCards = self.getPropertyValue(elmRoot, b'vcard', bAllowMultiple=1)
        else:
            arCards = [
             elmRoot]
        for elmCard in arCards:
            arLines = []

            def processSingleString(sProperty):
                sValue = self.getPropertyValue(elmCard, sProperty, self.STRING, bAutoEscape=1).decode(self.encoding)
                if sValue:
                    arLines.append(self.vcardFold(sProperty.upper() + b':' + sValue))
                return sValue or u''

            def processSingleURI(sProperty):
                sValue = self.getPropertyValue(elmCard, sProperty, self.URI)
                if sValue:
                    sContentType = b''
                    sEncoding = b''
                    sValueKey = b''
                    if sValue.startswith(b'data:'):
                        sEncoding = b';ENCODING=b'
                        sContentType = sValue.split(b';')[0].split(b'/').pop()
                        sValue = sValue.split(b',', 1).pop()
                    else:
                        elmValue = self.getPropertyValue(elmCard, sProperty)
                        if elmValue:
                            if sProperty != b'url':
                                sValueKey = b';VALUE=uri'
                            sContentType = elmValue.get(b'type', b'').strip().split(b'/').pop().strip()
                    sContentType = sContentType.upper()
                    if sContentType == b'OCTET-STREAM':
                        sContentType = b''
                    if sContentType:
                        sContentType = b';TYPE=' + sContentType.upper()
                    arLines.append(self.vcardFold(sProperty.upper() + sEncoding + sContentType + sValueKey + b':' + sValue))
                return

            def processTypeValue(sProperty, arDefaultType, arForceType=None):
                arResults = self.getPropertyValue(elmCard, sProperty, bAllowMultiple=1)
                for elmResult in arResults:
                    arType = self.getPropertyValue(elmResult, b'type', self.STRING, 1, 1)
                    if arForceType:
                        arType = self.unique(arForceType + arType)
                    if not arType:
                        arType = arDefaultType
                    sValue = self.getPropertyValue(elmResult, b'value', self.EMAIL, 0)
                    if sValue:
                        arLines.append(self.vcardFold(sProperty.upper() + b';TYPE=' + (b',').join(arType) + b':' + sValue))

                return

            arAgent = self.getPropertyValue(elmCard, b'agent', bAllowMultiple=1)
            for elmAgent in arAgent:
                if re.compile(b'\\bvcard\\b').search(elmAgent.get(b'class')):
                    sAgentValue = self.findVCards(elmAgent, 1) + b'\n'
                    sAgentValue = sAgentValue.replace(b'\n', b'\\n')
                    sAgentValue = sAgentValue.replace(b';', b'\\;')
                    if sAgentValue:
                        arLines.append(self.vcardFold(b'AGENT:' + sAgentValue))
                    elmAgent.extract()
                else:
                    sAgentValue = self.getPropertyValue(elmAgent, b'value', self.URI, bAutoEscape=1)
                    if sAgentValue:
                        arLines.append(self.vcardFold(b'AGENT;VALUE=uri:' + sAgentValue))

            sFN = processSingleString(b'fn')
            elmName = self.getPropertyValue(elmCard, b'n')
            if elmName:
                sFamilyName = self.getPropertyValue(elmName, b'family-name', self.STRING, bAutoEscape=1)
                sGivenName = self.getPropertyValue(elmName, b'given-name', self.STRING, bAutoEscape=1)
                arAdditionalNames = self.getPropertyValue(elmName, b'additional-name', self.STRING, 1, 1) + self.getPropertyValue(elmName, b'additional-names', self.STRING, 1, 1)
                arHonorificPrefixes = self.getPropertyValue(elmName, b'honorific-prefix', self.STRING, 1, 1) + self.getPropertyValue(elmName, b'honorific-prefixes', self.STRING, 1, 1)
                arHonorificSuffixes = self.getPropertyValue(elmName, b'honorific-suffix', self.STRING, 1, 1) + self.getPropertyValue(elmName, b'honorific-suffixes', self.STRING, 1, 1)
                arLines.append(self.vcardFold(b'N:' + sFamilyName + b';' + sGivenName + b';' + (b',').join(arAdditionalNames) + b';' + (b',').join(arHonorificPrefixes) + b';' + (b',').join(arHonorificSuffixes)))
            elif sFN:
                arNames = self.normalize(sFN).split()
                if len(arNames) == 2:
                    bFamilyNameFirst = arNames[0].endswith(b',') or len(arNames[1]) == 1 or len(arNames[1]) == 2 and arNames[1].endswith(b'.')
                    if bFamilyNameFirst:
                        arLines.append(self.vcardFold(b'N:' + arNames[0] + b';' + arNames[1]))
                    else:
                        arLines.append(self.vcardFold(b'N:' + arNames[1] + b';' + arNames[0]))
            sSortString = self.getPropertyValue(elmCard, b'sort-string', self.STRING, bAutoEscape=1)
            if sSortString:
                arLines.append(self.vcardFold(b'SORT-STRING:' + sSortString))
            arNickname = self.getPropertyValue(elmCard, b'nickname', self.STRING, 1, 1)
            if arNickname:
                arLines.append(self.vcardFold(b'NICKNAME:' + (b',').join(arNickname)))
            processSingleURI(b'photo')
            dtBday = self.getPropertyValue(elmCard, b'bday', self.DATE)
            if dtBday:
                arLines.append(self.vcardFold(b'BDAY:' + self.toISO8601(dtBday)))
            arAdr = self.getPropertyValue(elmCard, b'adr', bAllowMultiple=1)
            for elmAdr in arAdr:
                arType = self.getPropertyValue(elmAdr, b'type', self.STRING, 1, 1)
                if not arType:
                    arType = [
                     b'intl', b'postal', b'parcel', b'work']
                sPostOfficeBox = self.getPropertyValue(elmAdr, b'post-office-box', self.STRING, 0, 1)
                sExtendedAddress = self.getPropertyValue(elmAdr, b'extended-address', self.STRING, 0, 1)
                sStreetAddress = self.getPropertyValue(elmAdr, b'street-address', self.STRING, 0, 1)
                sLocality = self.getPropertyValue(elmAdr, b'locality', self.STRING, 0, 1)
                sRegion = self.getPropertyValue(elmAdr, b'region', self.STRING, 0, 1)
                sPostalCode = self.getPropertyValue(elmAdr, b'postal-code', self.STRING, 0, 1)
                sCountryName = self.getPropertyValue(elmAdr, b'country-name', self.STRING, 0, 1)
                arLines.append(self.vcardFold(b'ADR;TYPE=' + (b',').join(arType) + b':' + sPostOfficeBox + b';' + sExtendedAddress + b';' + sStreetAddress + b';' + sLocality + b';' + sRegion + b';' + sPostalCode + b';' + sCountryName))

            processTypeValue(b'label', [b'intl', b'postal', b'parcel', b'work'])
            processTypeValue(b'tel', [b'voice'])
            processTypeValue(b'email', [b'internet'], [b'internet'])
            processSingleString(b'mailer')
            processSingleString(b'tz')
            elmGeo = self.getPropertyValue(elmCard, b'geo')
            if elmGeo:
                sLatitude = self.getPropertyValue(elmGeo, b'latitude', self.STRING, 0, 1)
                sLongitude = self.getPropertyValue(elmGeo, b'longitude', self.STRING, 0, 1)
                arLines.append(self.vcardFold(b'GEO:' + sLatitude + b';' + sLongitude))
            processSingleString(b'title')
            processSingleString(b'role')
            processSingleURI(b'logo')
            elmOrg = self.getPropertyValue(elmCard, b'org')
            if elmOrg:
                sOrganizationName = self.getPropertyValue(elmOrg, b'organization-name', self.STRING, 0, 1)
                if not sOrganizationName:
                    sOrganizationName = self.getPropertyValue(elmCard, b'org', self.STRING, 0, 1)
                    if sOrganizationName:
                        arLines.append(self.vcardFold(b'ORG:' + sOrganizationName))
                else:
                    arOrganizationUnit = self.getPropertyValue(elmOrg, b'organization-unit', self.STRING, 1, 1)
                    arLines.append(self.vcardFold(b'ORG:' + sOrganizationName + b';' + (b';').join(arOrganizationUnit)))
            arCategory = self.getPropertyValue(elmCard, b'category', self.STRING, 1, 1) + self.getPropertyValue(elmCard, b'categories', self.STRING, 1, 1)
            if arCategory:
                arLines.append(self.vcardFold(b'CATEGORIES:' + (b',').join(arCategory)))
            processSingleString(b'note')
            processSingleString(b'rev')
            processSingleURI(b'sound')
            processSingleString(b'uid')
            processSingleURI(b'url')
            processSingleString(b'class')
            processSingleURI(b'key')
            if arLines:
                arLines = [
                 u'BEGIN:vCard', u'VERSION:3.0'] + arLines + [u'END:vCard']
                for i, s in enumerate(arLines):
                    if not isinstance(s, unicode):
                        arLines[i] = s.decode(b'utf-8', b'ignore')

                sVCards += (u'\n').join(arLines) + u'\n'

        return sVCards.strip()

    def isProbablyDownloadable(self, elm):
        attrsD = elm.attrMap
        if b'href' not in attrsD:
            return 0
        linktype = attrsD.get(b'type', b'').strip()
        if linktype.startswith(b'audio/') or linktype.startswith(b'video/') or linktype.startswith(b'application/') and not linktype.endswith(b'xml'):
            return 1
        path = urlparse.urlparse(attrsD[b'href'])[2]
        if path.find(b'.') == -1:
            return 0
        fileext = path.split(b'.').pop().lower()
        return fileext in self.known_binary_extensions

    def findTags(self):
        all = lambda x: 1
        for elm in self.document(all, {b'rel': (re.compile(b'\\btag\\b'))}):
            href = elm.get(b'href')
            if not href:
                continue
            urlscheme, domain, path, params, query, fragment = urlparse.urlparse(_urljoin(self.baseuri, href))
            segments = path.split(b'/')
            tag = segments.pop()
            if not tag:
                if segments:
                    tag = segments.pop()
                else:
                    continue
            tagscheme = urlparse.urlunparse((urlscheme, domain, (b'/').join(segments), b'', b'', b''))
            if not tagscheme.endswith(b'/'):
                tagscheme += b'/'
            self.tags.append(FeedParserDict({b'term': tag, b'scheme': tagscheme, b'label': (elm.string or b'')}))

        return

    def findEnclosures(self):
        all = lambda x: 1
        enclosure_match = re.compile(b'\\benclosure\\b')
        for elm in self.document(all, {b'href': (re.compile(b'.+'))}):
            if not enclosure_match.search(elm.get(b'rel', u'')) and not self.isProbablyDownloadable(elm):
                continue
            if elm.attrMap not in self.enclosures:
                self.enclosures.append(elm.attrMap)
                if elm.string and not elm.get(b'title'):
                    self.enclosures[-1][b'title'] = elm.string

        return

    def findXFN(self):
        all = lambda x: 1
        for elm in self.document(all, {b'rel': (re.compile(b'.+')), b'href': (re.compile(b'.+'))}):
            rels = elm.get(b'rel', u'').split()
            xfn_rels = [r for r in rels if r in self.known_xfn_relationships]
            if xfn_rels:
                self.xfn.append({b'relationships': xfn_rels, b'href': (elm.get(b'href', b'')), b'name': (elm.string)})

        return


def _parseMicroformats(htmlSource, baseURI, encoding):
    if not BeautifulSoup:
        return
    try:
        p = _MicroformatsParser(htmlSource, baseURI, encoding)
    except UnicodeEncodeError:
        return

    p.vcard = p.findVCards(p.document)
    p.findTags()
    p.findEnclosures()
    p.findXFN()
    return {b'tags': (p.tags), b'enclosures': (p.enclosures), b'xfn': (p.xfn), b'vcard': (p.vcard)}


class _RelativeURIResolver(_BaseHTMLProcessor):
    relative_uris = set([31, 
     32, 
     33, 
     34, 
     35, 
     36, 
     37, 
     38, 
     39, 
     40, 
     41, 
     42, 
     43, 
     44, 
     45, 
     46, 
     47, 
     48, 
     49, 
     50, 
     51, 
     52, 
     53, 
     54, 
     55])

    def __init__(self, baseuri, encoding, _type):
        _BaseHTMLProcessor.__init__(self, encoding, _type)
        self.baseuri = baseuri
        return

    def resolveURI(self, uri):
        return _makeSafeAbsoluteURI(self.baseuri, uri.strip())

    def unknown_starttag(self, tag, attrs):
        attrs = self.normalize_attrs(attrs)
        attrs = [(key, (tag, key) in self.relative_uris and self.resolveURI(value) or value) for key, value in attrs]
        _BaseHTMLProcessor.unknown_starttag(self, tag, attrs)
        return


def _resolveRelativeURIs(htmlSource, baseURI, encoding, _type):
    if not _SGML_AVAILABLE:
        return htmlSource
    p = _RelativeURIResolver(baseURI, encoding, _type)
    p.feed(htmlSource)
    return p.output()


def _makeSafeAbsoluteURI(base, rel=None):
    if not ACCEPTABLE_URI_SCHEMES:
        try:
            return _urljoin(base, rel or u'')
        except ValueError:
            return u''

    if not base:
        return rel or u''
    if not rel:
        try:
            scheme = urlparse.urlparse(base)[0]
        except ValueError:
            return u''

        if not scheme or scheme in ACCEPTABLE_URI_SCHEMES:
            return base
        return u''
    try:
        uri = _urljoin(base, rel)
    except ValueError:
        return u''

    if uri.strip().split(b':', 1)[0] not in ACCEPTABLE_URI_SCHEMES:
        return u''
    return uri


class _HTMLSanitizer(_BaseHTMLProcessor):
    acceptable_elements = set([0, 1, 2, 3, 4, 
     5, 6, 7, 8, 9, 10, 11, 12, 
     13, 
     14, 15, 16, 17, 18, 19, 
     20, 21, 22, 23, 24, 25, 
     26, 
     27, 28, 29, 30, 31, 32, 33, 34, 
     35, 
     36, 37, 38, 39, 40, 41, 
     42, 43, 44, 45, 46, 47, 
     48, 49, 50, 51, 
     52, 53, 54, 55, 56, 57, 58, 59, 
     60, 
     61, 62, 63, 64, 65, 66, 67, 
     68, 69, 
     70, 71, 72, 73, 74, 75, 
     76, 77, 78, 79, 80, 81, 
     82, 
     83, 84, 85, 86, 87, 88, 89, 90, 
     91, 
     92, 93, 94, 95, 96, 97, 98, 99])
    acceptable_attributes = set([1, 100, 101, 102, 
     103, 104, 105, 106, 107, 108, 
     109, 
     110, 111, 112, 113, 
     114, 115, 116, 117, 
     118, 
     119, 120, 121, 122, 123, 
     124, 125, 126, 16, 127, 
     128, 129, 130, 
     131, 132, 133, 134, 135, 136, 
     137, 
     138, 139, 140, 141, 142, 
     28, 143, 144, 145, 146, 
     147, 148, 149, 
     39, 150, 151, 152, 153, 154, 155, 
     156, 
     157, 158, 159, 160, 161, 162, 163, 
     164, 165, 54, 
     166, 167, 168, 169, 
     170, 171, 172, 173, 174, 175, 
     176, 
     177, 178, 179, 180, 181, 182, 183, 
     184, 
     185, 186, 187, 188, 189, 190, 
     191, 192, 193, 194, 
     195, 196, 
     197, 198, 199, 200, 201, 202, 
     203, 
     204, 205, 206, 207, 208, 80, 209, 
     210, 211, 212, 
     213, 214, 215, 216, 
     217, 218, 219, 220, 221, 222, 
     223, 
     224, 225, 226, 227, 228, 229, 230, 
     231])
    unacceptable_elements_with_end_tag = set([b'script', b'applet', b'style'])
    acceptable_css_properties = set([235, 236, 
     237, 238, 239, 
     240, 241, 242, 128, 
     129, 
     243, 244, 245, 246, 247, 38, 
     248, 249, 250, 251, 
     252, 
     154, 253, 254, 255, 256, 
     257, 258, 
     259, 260, 261, 
     262, 263, 264, 265, 
     266, 
     267, 268, 269, 270, 
     271, 272, 273, 226, 
     274, 
     229])
    acceptable_css_keywords = set([275, 276, 277, 278, 279, 
     280, 281, 282, 283, 15, 284, 285, 
     286, 
     287, 288, 289, 290, 291, 292, 
     293, 294, 295, 296, 
     297, 298, 185, 299, 
     300, 301, 302, 303, 304, 305, 
     306, 307, 
     308, 309, 310, 311])
    valid_css_values = re.compile(b'^(#[0-9a-f]+|rgb\\(\\d+%?,\\d*%?,?\\d*%?\\)?|' + b'\\d{0,2}\\.?\\d{0,2}(cm|em|ex|in|mm|pc|pt|px|%|,|\\))?)$')
    mathml_elements = set([314, 315, 316, 317, 
     318, 319, 320, 321, 322, 323, 324, 325, 
     326, 
     327, 328, 329, 330, 331, 332, 333, 
     334, 
     335, 336, 337, 338, 339, 340, 341, 
     342, 296, 343])
    mathml_attributes = set([344, 104, 345, 345, 
     345, 346, 347, 348, 349, 350, 
     245, 
     351, 352, 353, 354, 
     355, 356, 357, 150, 154, 358, 
     359, 
     360, 361, 362, 362, 
     363, 364, 186, 365, 366, 366, 
     366, 
     367, 368, 203, 369, 370, 371, 
     372, 
     373, 374, 229, 229, 375, 
     376, 377, 378, 379])
    svg_elements = set([0, 380, 381, 382, 
     383, 384, 385, 386, 387, 388, 
     389, 
     390, 391, 392, 393, 394, 
     395, 396, 397, 398, 399, 
     400, 
     401, 402, 403, 404, 405, 406, 407, 
     408, 
     409, 410, 217, 411, 412])
    svg_attributes = set([413, 414, 415, 416, 
     417, 418, 419, 420, 
     421, 422, 
     423, 424, 425, 426, 
     127, 129, 427, 428, 429, 430, 
     431, 432, 
     433, 434, 245, 435, 147, 436, 437, 
     438, 
     248, 249, 439, 250, 
     251, 252, 440, 441, 442, 443, 
     444, 
     445, 446, 447, 154, 448, 
     449, 162, 
     450, 451, 452, 453, 
     454, 167, 455, 456, 457, 
     458, 
     459, 460, 461, 176, 
     180, 182, 462, 463, 464, 465, 
     466, 
     467, 468, 401, 
     469, 470, 471, 472, 473, 474, 
     475, 
     476, 477, 478, 
     479, 480, 481, 482, 483, 484, 485, 
     486, 
     487, 488, 
     489, 490, 491, 
     492, 493, 494, 
     495, 
     496, 497, 498, 
     215, 499, 500, 501, 219, 502, 503, 
     504, 
     505, 506, 507, 
     508, 509, 510, 511, 512, 229, 
     513, 
     514, 515, 516, 517, 518, 519, 
     375, 520, 376, 521, 
     377, 
     522, 231, 523, 378, 379, 524, 525, 
     526, 
     527])
    svg_attr_map = None
    svg_elem_map = None
    acceptable_svg_properties = set([436, 437, 438, 
     490, 497, 493, 494, 
     496])

    def reset(self):
        _BaseHTMLProcessor.reset(self)
        self.unacceptablestack = 0
        self.mathmlOK = 0
        self.svgOK = 0
        return

    def unknown_starttag(self, tag, attrs):
        acceptable_attributes = self.acceptable_attributes
        keymap = {}
        if tag not in self.acceptable_elements or self.svgOK:
            if tag in self.unacceptable_elements_with_end_tag:
                self.unacceptablestack += 1
            if self._type.endswith(b'html'):
                if not dict(attrs).get(b'xmlns'):
                    if tag == b'svg':
                        attrs.append((b'xmlns', b'http://www.w3.org/2000/svg'))
                    if tag == b'math':
                        attrs.append((b'xmlns', b'http://www.w3.org/1998/Math/MathML'))
            if tag == b'math' and (b'xmlns', b'http://www.w3.org/1998/Math/MathML') in attrs:
                self.mathmlOK += 1
            if tag == b'svg' and (b'xmlns', b'http://www.w3.org/2000/svg') in attrs:
                self.svgOK += 1
            if self.mathmlOK and tag in self.mathml_elements:
                acceptable_attributes = self.mathml_attributes
            elif self.svgOK and tag in self.svg_elements:
                if not self.svg_attr_map:
                    lower = [attr.lower() for attr in self.svg_attributes]
                    mix = [a for a in self.svg_attributes if a not in lower]
                    self.svg_attributes = lower
                    self.svg_attr_map = dict([(a.lower(), a) for a in mix])
                    lower = [attr.lower() for attr in self.svg_elements]
                    mix = [a for a in self.svg_elements if a not in lower]
                    self.svg_elements = lower
                    self.svg_elem_map = dict([(a.lower(), a) for a in mix])
                acceptable_attributes = self.svg_attributes
                tag = self.svg_elem_map.get(tag, tag)
                keymap = self.svg_attr_map
            elif tag not in self.acceptable_elements:
                return
        if self.mathmlOK or self.svgOK:
            if filter((lambda (n, v): n.startswith(b'xlink:')), attrs):
                if (b'xmlns:xlink', b'http://www.w3.org/1999/xlink') not in attrs:
                    attrs.append((b'xmlns:xlink', b'http://www.w3.org/1999/xlink'))
        clean_attrs = []
        for key, value in self.normalize_attrs(attrs):
            if key in acceptable_attributes:
                key = keymap.get(key, key)
                if key == u'href':
                    value = _makeSafeAbsoluteURI(value)
                clean_attrs.append((key, value))
            elif key == b'style':
                clean_value = self.sanitize_style(value)
                if clean_value:
                    clean_attrs.append((key, clean_value))

        _BaseHTMLProcessor.unknown_starttag(self, tag, clean_attrs)
        return

    def unknown_endtag(self, tag):
        if tag not in self.acceptable_elements:
            if tag in self.unacceptable_elements_with_end_tag:
                self.unacceptablestack -= 1
            if self.mathmlOK and tag in self.mathml_elements:
                if tag == b'math' and self.mathmlOK:
                    self.mathmlOK -= 1
            elif self.svgOK and tag in self.svg_elements:
                tag = self.svg_elem_map.get(tag, tag)
                if tag == b'svg' and self.svgOK:
                    self.svgOK -= 1
            else:
                return
        _BaseHTMLProcessor.unknown_endtag(self, tag)
        return

    def handle_pi(self, text):
        return

    def handle_decl(self, text):
        return

    def handle_data(self, text):
        if not self.unacceptablestack:
            _BaseHTMLProcessor.handle_data(self, text)
        return

    def sanitize_style(self, style):
        style = re.compile(b'url\\s*\\(\\s*[^\\s)]+?\\s*\\)\\s*').sub(b' ', style)
        if not re.match(b'^([:,;#%.\\sa-zA-Z0-9!]|\\w-\\w|\'[\\s\\w]+\'|"[\\s\\w]+"|\\([\\d,\\s]+\\))*$', style):
            return b''
        if re.sub(b'\\s*[-\\w]+\\s*:\\s*[^:;]*;?', b'', style).strip():
            return b''
        clean = []
        for prop, value in re.findall(b'([-\\w]+)\\s*:\\s*([^:;]*)', style):
            if not value:
                continue
            if prop.lower() in self.acceptable_css_properties:
                clean.append(prop + b': ' + value + b';')
            elif prop.split(b'-')[0].lower() in (b'background', b'border', b'margin', b'padding'):
                for keyword in value.split():
                    if keyword not in self.acceptable_css_keywords and not self.valid_css_values.match(keyword):
                        break
                else:
                    clean.append(prop + b': ' + value + b';')

            elif self.svgOK and prop.lower() in self.acceptable_svg_properties:
                clean.append(prop + b': ' + value + b';')

        return (b' ').join(clean)

    def parse_comment(self, i, report=1):
        ret = _BaseHTMLProcessor.parse_comment(self, i, report)
        if ret >= 0:
            return ret
        match = re.compile(b'--[^>]*>').search(self.rawdata, i + 4)
        if match:
            return match.end()
        return len(self.rawdata)


def _sanitizeHTML(htmlSource, encoding, _type):
    if not _SGML_AVAILABLE:
        return htmlSource
    else:
        p = _HTMLSanitizer(encoding, _type)
        htmlSource = htmlSource.replace(b'<![CDATA[', b'&lt;![CDATA[')
        p.feed(htmlSource)
        data = p.output()
        if TIDY_MARKUP:
            _tidy = None
            for tidy_interface in PREFERRED_TIDY_INTERFACES:
                try:
                    if tidy_interface == b'uTidy':
                        from tidy import parseString as _utidy

                        def _tidy(data, **kwargs):
                            return str(_utidy(data, **kwargs))

                        break
                    elif tidy_interface == b'mxTidy':
                        from mx.Tidy import Tidy as _mxtidy

                        def _tidy(data, **kwargs):
                            nerrors, nwarnings, data, errordata = _mxtidy.tidy(data, **kwargs)
                            return data

                        break
                except Exception:
                    pass

            if _tidy:
                utf8 = isinstance(data, unicode)
                if utf8:
                    data = data.encode(b'utf-8')
                data = _tidy(data, output_xhtml=1, numeric_entities=1, wrap=0, char_encoding=b'utf8')
                if utf8:
                    data = unicode(data, b'utf-8')
                if data.count(b'<body'):
                    data = data.split(b'<body', 1)[1]
                    if data.count(b'>'):
                        data = data.split(b'>', 1)[1]
                if data.count(b'</body'):
                    data = data.split(b'</body', 1)[0]
        data = data.strip().replace(b'\r\n', b'\n')
        return data


class _FeedURLHandler(urllib2.HTTPDigestAuthHandler, urllib2.HTTPRedirectHandler, urllib2.HTTPDefaultErrorHandler):

    def http_error_default(self, req, fp, code, msg, headers):
        fp.status = code
        return fp

    def http_error_301(self, req, fp, code, msg, hdrs):
        result = urllib2.HTTPRedirectHandler.http_error_301(self, req, fp, code, msg, hdrs)
        result.status = code
        result.newurl = result.geturl()
        return result

    http_error_300 = http_error_301
    http_error_302 = http_error_301
    http_error_303 = http_error_301
    http_error_307 = http_error_301

    def http_error_401(self, req, fp, code, msg, headers):
        host = urlparse.urlparse(req.get_full_url())[1]
        if base64 is None or b'Authorization' not in req.headers or b'WWW-Authenticate' not in headers:
            return self.http_error_default(req, fp, code, msg, headers)
        else:
            auth = _base64decode(req.headers[b'Authorization'].split(b' ')[1])
            user, passw = auth.split(b':')
            realm = re.findall(b'realm="([^"]*)"', headers[b'WWW-Authenticate'])[0]
            self.add_password(realm, host, user, passw)
            retry = self.http_error_auth_reqed(b'www-authenticate', host, req, headers)
            self.reset_retry_count()
            return retry


def _open_resource(url_file_stream_or_string, etag, modified, agent, referrer, handlers, request_headers):
    if hasattr(url_file_stream_or_string, b'read'):
        return url_file_stream_or_string
    else:
        if isinstance(url_file_stream_or_string, basestring) and urlparse.urlparse(url_file_stream_or_string)[0] in (b'http', b'https', b'ftp', b'file', b'feed'):
            if url_file_stream_or_string.startswith(b'feed:http'):
                url_file_stream_or_string = url_file_stream_or_string[5:]
            elif url_file_stream_or_string.startswith(b'feed:'):
                url_file_stream_or_string = b'http:' + url_file_stream_or_string[5:]
            if not agent:
                agent = USER_AGENT
            auth = None
            if base64:
                urltype, rest = urllib.splittype(url_file_stream_or_string)
                realhost, rest = urllib.splithost(rest)
                if realhost:
                    user_passwd, realhost = urllib.splituser(realhost)
                    if user_passwd:
                        url_file_stream_or_string = b'%s://%s%s' % (urltype, realhost, rest)
                        auth = base64.standard_b64encode(user_passwd).strip()
            if isinstance(url_file_stream_or_string, unicode):
                url_file_stream_or_string = _convert_to_idn(url_file_stream_or_string)
            request = _build_urllib2_request(url_file_stream_or_string, agent, etag, modified, referrer, auth, request_headers)
            opener = urllib2.build_opener(*tuple(handlers + [_FeedURLHandler()]))
            opener.addheaders = []
            try:
                return opener.open(request)
            finally:
                opener.close()

        try:
            return open(url_file_stream_or_string, b'rb')
        except (IOError, UnicodeEncodeError, TypeError):
            pass

        if isinstance(url_file_stream_or_string, unicode):
            return _StringIO(url_file_stream_or_string.encode(b'utf-8'))
        return _StringIO(url_file_stream_or_string)


def _convert_to_idn(url):
    parts = list(urlparse.urlsplit(url))
    try:
        parts[1].encode(b'ascii')
    except UnicodeEncodeError:
        host = parts[1].rsplit(b':', 1)
        newhost = []
        port = u''
        if len(host) == 2:
            port = host.pop()
        for h in host[0].split(b'.'):
            newhost.append(h.encode(b'idna').decode(b'utf-8'))

        parts[1] = (b'.').join(newhost)
        if port:
            parts[1] += b':' + port
        return urlparse.urlunsplit(parts)

    return url
    return


def _build_urllib2_request(url, agent, etag, modified, referrer, auth, request_headers):
    request = urllib2.Request(url)
    request.add_header(b'User-Agent', agent)
    if etag:
        request.add_header(b'If-None-Match', etag)
    if isinstance(modified, basestring):
        modified = _parse_date(modified)
    elif isinstance(modified, datetime.datetime):
        modified = modified.utctimetuple()
    if modified:
        short_weekdays = [
         3, 4, 5, 6, 7, 8, 9]
        months = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]
        request.add_header(b'If-Modified-Since', b'%s, %02d %s %04d %02d:%02d:%02d GMT' % (short_weekdays[modified[6]], modified[2], months[modified[1] - 1], modified[0], modified[3], modified[4], modified[5]))
    if referrer:
        request.add_header(b'Referer', referrer)
    if gzip and zlib:
        request.add_header(b'Accept-encoding', b'gzip, deflate')
    elif gzip:
        request.add_header(b'Accept-encoding', b'gzip')
    elif zlib:
        request.add_header(b'Accept-encoding', b'deflate')
    else:
        request.add_header(b'Accept-encoding', b'')
    if auth:
        request.add_header(b'Authorization', b'Basic %s' % auth)
    if ACCEPT_HEADER:
        request.add_header(b'Accept', ACCEPT_HEADER)
    for header_name, header_value in request_headers.items():
        request.add_header(header_name, header_value)

    request.add_header(b'A-IM', b'feed')
    return request


_date_handlers = []

def registerDateHandler(func):
    _date_handlers.insert(0, func)
    return


_iso8601_tmpl = [
 208, 209, 210, 211, 
 212, 213, 214, 
 215, 216, 217, 
 218, 219, 
 220, 
 221, 
 95]
_iso8601_re = [tmpl.replace(b'YYYY', b'(?P<year>\\d{4})').replace(b'YY', b'(?P<year>\\d\\d)').replace(b'MM', b'(?P<month>[01]\\d)').replace(b'DD', b'(?P<day>[0123]\\d)').replace(b'OOO', b'(?P<ordinal>[0123]\\d\\d)').replace(b'CC', b'(?P<century>\\d\\d$)') + b'(T?(?P<hour>\\d{2}):(?P<minute>\\d{2})' + b'(:(?P<second>\\d{2}))?' + b'(\\.(?P<fracsecond>\\d+))?' + b'(?P<tz>[+-](?P<tzhour>\\d{2})(:(?P<tzmin>\\d{2}))?|Z)?)?' for tmpl in _iso8601_tmpl]
try:
    del tmpl
except NameError:
    pass

_iso8601_matches = [re.compile(regex).match for regex in _iso8601_re]
try:
    del regex
except NameError:
    pass

def _parse_date_iso8601(dateString):
    m = None
    for _iso8601_match in _iso8601_matches:
        m = _iso8601_match(dateString)
        if m:
            break

    if not m:
        return
    else:
        if m.span() == (0, 0):
            return
        params = m.groupdict()
        ordinal = params.get(b'ordinal', 0)
        if ordinal:
            ordinal = int(ordinal)
        else:
            ordinal = 0
        year = params.get(b'year', b'--')
        if not year or year == b'--':
            year = time.gmtime()[0]
        elif len(year) == 2:
            year = 100 * int(time.gmtime()[0] / 100) + int(year)
        else:
            year = int(year)
        month = params.get(b'month', b'-')
        if not month or month == b'-':
            if ordinal:
                month = 1
            else:
                month = time.gmtime()[1]
        month = int(month)
        day = params.get(b'day', 0)
        if not day:
            if ordinal:
                day = ordinal
            elif params.get(b'century', 0) or params.get(b'year', 0) or params.get(b'month', 0):
                day = 1
            else:
                day = time.gmtime()[2]
        else:
            day = int(day)
        if b'century' in params:
            year = (int(params[b'century']) - 1) * 100 + 1
        for field in [12, 13, 14, 15, 16]:
            if not params.get(field, None):
                params[field] = 0

        hour = int(params.get(b'hour', 0))
        minute = int(params.get(b'minute', 0))
        second = int(float(params.get(b'second', 0)))
        weekday = 0
        daylight_savings_flag = -1
        tm = [year, month, day, hour, minute, second, weekday, 
         ordinal, 
         daylight_savings_flag]
        tz = params.get(b'tz')
        if tz and tz != b'Z':
            if tz[0] == b'-':
                tm[3] += int(params.get(b'tzhour', 0))
                tm[4] += int(params.get(b'tzmin', 0))
            elif tz[0] == b'+':
                tm[3] -= int(params.get(b'tzhour', 0))
                tm[4] -= int(params.get(b'tzmin', 0))
            else:
                return
        return time.localtime(time.mktime(tuple(tm)))


registerDateHandler(_parse_date_iso8601)
_korean_year = u'\ub144'
_korean_month = u'\uc6d4'
_korean_day = u'\uc77c'
_korean_am = u'\uc624\uc804'
_korean_pm = u'\uc624\ud6c4'
_korean_onblog_date_re = re.compile(b'(\\d{4})%s\\s+(\\d{2})%s\\s+(\\d{2})%s\\s+(\\d{2}):(\\d{2}):(\\d{2})' % (
 _korean_year, _korean_month, _korean_day))
_korean_nate_date_re = re.compile(u'(\\d{4})-(\\d{2})-(\\d{2})\\s+(%s|%s)\\s+(\\d{,2}):(\\d{,2}):(\\d{,2})' % (
 _korean_am, _korean_pm))

def _parse_date_onblog(dateString):
    m = _korean_onblog_date_re.match(dateString)
    if not m:
        return
    w3dtfdate = b'%(year)s-%(month)s-%(day)sT%(hour)s:%(minute)s:%(second)s%(zonediff)s' % {b'year': (m.group(1)), b'month': (m.group(2)), b'day': (m.group(3)), b'hour': (m.group(4)), 
       b'minute': (m.group(5)), b'second': (m.group(6)), b'zonediff': b'+09:00'}
    return _parse_date_w3dtf(w3dtfdate)


registerDateHandler(_parse_date_onblog)

def _parse_date_nate(dateString):
    m = _korean_nate_date_re.match(dateString)
    if not m:
        return
    hour = int(m.group(5))
    ampm = m.group(4)
    if ampm == _korean_pm:
        hour += 12
    hour = str(hour)
    if len(hour) == 1:
        hour = b'0' + hour
    w3dtfdate = b'%(year)s-%(month)s-%(day)sT%(hour)s:%(minute)s:%(second)s%(zonediff)s' % {b'year': (m.group(1)), b'month': (m.group(2)), b'day': (m.group(3)), b'hour': hour, 
       b'minute': (m.group(6)), b'second': (m.group(7)), b'zonediff': b'+09:00'}
    return _parse_date_w3dtf(w3dtfdate)


registerDateHandler(_parse_date_nate)
_greek_months = {u'\u0399\u03b1\u03bd': u'Jan', 
   u'\u03a6\u03b5\u03b2': u'Feb', 
   u'\u039c\u03ac\u03ce': u'Mar', 
   u'\u039c\u03b1\u03ce': u'Mar', 
   u'\u0391\u03c0\u03c1': u'Apr', 
   u'\u039c\u03ac\u03b9': u'May', 
   u'\u039c\u03b1\u03ca': u'May', 
   u'\u039c\u03b1\u03b9': u'May', 
   u'\u0399\u03bf\u03cd\u03bd': u'Jun', 
   u'\u0399\u03bf\u03bd': u'Jun', 
   u'\u0399\u03bf\u03cd\u03bb': u'Jul', 
   u'\u0399\u03bf\u03bb': u'Jul', 
   u'\u0391\u03cd\u03b3': u'Aug', 
   u'\u0391\u03c5\u03b3': u'Aug', 
   u'\u03a3\u03b5\u03c0': u'Sep', 
   u'\u039f\u03ba\u03c4': u'Oct', 
   u'\u039d\u03bf\u03ad': u'Nov', 
   u'\u039d\u03bf\u03b5': u'Nov', 
   u'\u0394\u03b5\u03ba': u'Dec'}
_greek_wdays = {u'\u039a\u03c5\u03c1': u'Sun', 
   u'\u0394\u03b5\u03c5': u'Mon', 
   u'\u03a4\u03c1\u03b9': u'Tue', 
   u'\u03a4\u03b5\u03c4': u'Wed', 
   u'\u03a0\u03b5\u03bc': u'Thu', 
   u'\u03a0\u03b1\u03c1': u'Fri', 
   u'\u03a3\u03b1\u03b2': u'Sat'}
_greek_date_format_re = re.compile(u'([^,]+),\\s+(\\d{2})\\s+([^\\s]+)\\s+(\\d{4})\\s+(\\d{2}):(\\d{2}):(\\d{2})\\s+([^\\s]+)')

def _parse_date_greek(dateString):
    m = _greek_date_format_re.match(dateString)
    if not m:
        return
    wday = _greek_wdays[m.group(1)]
    month = _greek_months[m.group(3)]
    rfc822date = b'%(wday)s, %(day)s %(month)s %(year)s %(hour)s:%(minute)s:%(second)s %(zonediff)s' % {b'wday': wday, b'day': (m.group(2)), b'month': month, b'year': (m.group(4)), b'hour': (m.group(5)), 
       b'minute': (m.group(6)), b'second': (m.group(7)), b'zonediff': (m.group(8))}
    return _parse_date_rfc822(rfc822date)


registerDateHandler(_parse_date_greek)
_hungarian_months = {u'janu\xe1r': u'01', 
   u'febru\xe1ri': u'02', 
   u'm\xe1rcius': u'03', 
   u'\xe1prilis': u'04', 
   u'm\xe1ujus': u'05', 
   u'j\xfanius': u'06', 
   u'j\xfalius': u'07', 
   u'augusztus': u'08', 
   u'szeptember': u'09', 
   u'okt\xf3ber': u'10', 
   u'november': u'11', 
   u'december': u'12'}
_hungarian_date_format_re = re.compile(u'(\\d{4})-([^-]+)-(\\d{,2})T(\\d{,2}):(\\d{2})((\\+|-)(\\d{,2}:\\d{2}))')

def _parse_date_hungarian(dateString):
    m = _hungarian_date_format_re.match(dateString)
    if not m or m.group(2) not in _hungarian_months:
        return None
    month = _hungarian_months[m.group(2)]
    day = m.group(3)
    if len(day) == 1:
        day = b'0' + day
    hour = m.group(4)
    if len(hour) == 1:
        hour = b'0' + hour
    w3dtfdate = b'%(year)s-%(month)s-%(day)sT%(hour)s:%(minute)s%(zonediff)s' % {b'year': (m.group(1)), b'month': month, b'day': day, b'hour': hour, 
       b'minute': (m.group(5)), b'zonediff': (m.group(6))}
    return _parse_date_w3dtf(w3dtfdate)


registerDateHandler(_parse_date_hungarian)

def _parse_date_w3dtf(dateString):

    def __extract_date(m):
        year = int(m.group(b'year'))
        if year < 100:
            year = 100 * int(time.gmtime()[0] / 100) + int(year)
        if year < 1000:
            return (0, 0, 0)
        else:
            julian = m.group(b'julian')
            if julian:
                julian = int(julian)
                month = julian / 30 + 1
                day = julian % 30 + 1
                jday = None
                while jday != julian:
                    t = time.mktime((year, month, day, 0, 0, 0, 0, 0, 0))
                    jday = time.gmtime(t)[-2]
                    diff = abs(jday - julian)
                    if jday > julian:
                        if diff < day:
                            day = day - diff
                        else:
                            month = month - 1
                            day = 31
                    elif jday < julian:
                        if day + diff < 28:
                            day = day + diff
                        else:
                            month = month + 1

                return (
                 year, month, day)
            month = m.group(b'month')
            day = 1
            if month is None:
                month = 1
            else:
                month = int(month)
                day = m.group(b'day')
                if day:
                    day = int(day)
                else:
                    day = 1
            return (
             year, month, day)

    def __extract_time(m):
        if not m:
            return (0, 0, 0)
        hours = m.group(b'hours')
        if not hours:
            return (0, 0, 0)
        hours = int(hours)
        minutes = int(m.group(b'minutes'))
        seconds = m.group(b'seconds')
        if seconds:
            seconds = int(seconds)
        else:
            seconds = 0
        return (
         hours, minutes, seconds)

    def __extract_tzd(m):
        if not m:
            return 0
        tzd = m.group(b'tzd')
        if not tzd:
            return 0
        if tzd == b'Z':
            return 0
        hours = int(m.group(b'tzdhours'))
        minutes = m.group(b'tzdminutes')
        if minutes:
            minutes = int(minutes)
        else:
            minutes = 0
        offset = (hours * 60 + minutes) * 60
        if tzd[0] == b'+':
            return -offset
        return offset

    __date_re = b'(?P<year>\\d\\d\\d\\d)(?:(?P<dsep>-|)(?:(?P<month>\\d\\d)(?:(?P=dsep)(?P<day>\\d\\d))?|(?P<julian>\\d\\d\\d)))?'
    __tzd_re = b' ?(?P<tzd>[-+](?P<tzdhours>\\d\\d)(?::?(?P<tzdminutes>\\d\\d))|Z)?'
    __time_re = b'(?P<hours>\\d\\d)(?P<tsep>:|)(?P<minutes>\\d\\d)(?:(?P=tsep)(?P<seconds>\\d\\d)(?:[.,]\\d+)?)?' + __tzd_re
    __datetime_re = b'%s(?:[T ]%s)?' % (__date_re, __time_re)
    __datetime_rx = re.compile(__datetime_re)
    m = __datetime_rx.match(dateString)
    if m is None or m.group() != dateString:
        return
    gmt = __extract_date(m) + __extract_time(m) + (0, 0, 0)
    if gmt[0] == 0:
        return
    else:
        return time.gmtime(time.mktime(gmt) + __extract_tzd(m) - time.timezone)


registerDateHandler(_parse_date_w3dtf)
_rfc822_months = [
 320, 321, 322, 323, 324, 325, 
 326, 327, 328, 329, 330, 331]
_rfc822_daynames = [332, 333, 334, 335, 336, 337, 338]
_rfc822_month = b'(?P<month>%s)(?:[a-z]*,?)' % (b'|').join(_rfc822_months)
_rfc822_year = b'(?P<year>(?:\\d{2})?\\d{2})'
_rfc822_day = b'(?P<day> *\\d{1,2})'
_rfc822_date = b'%s %s %s' % (_rfc822_day, _rfc822_month, _rfc822_year)
_rfc822_hour = b'(?P<hour>\\d{2}):(?P<minute>\\d{2})(?::(?P<second>\\d{2}))?'
_rfc822_tz = b'(?P<tz>ut|gmt(?:[+-]\\d{2}:\\d{2})?|[aecmp][sd]?t|[zamny]|[+-]\\d{4})'
_rfc822_tznames = {b'ut': 0, 
   b'gmt': 0, b'z': 0, b'adt': (-3), 
   b'ast': (-4), b'at': (-4), b'edt': (-4), 
   b'est': (-5), b'et': (-5), b'cdt': (-5), 
   b'cst': (-6), b'ct': (-6), b'mdt': (-6), 
   b'mst': (-7), b'mt': (-7), b'pdt': (-7), 
   b'pst': (-8), b'pt': (-8), b'a': (-1), 
   b'n': 1, b'm': (-12), 
   b'y': 12}
_rfc822_time = b'%s (?:etc/)?%s' % (_rfc822_hour, _rfc822_tz)
_rfc822_dayname = b'(?P<dayname>%s)' % (b'|').join(_rfc822_daynames)
_rfc822_match = re.compile(b'(?:%s, )?%s(?: %s)?' % (_rfc822_dayname, _rfc822_date, _rfc822_time)).match

def _parse_date_rfc822(dt):
    try:
        m = _rfc822_match(dt.lower()).groupdict(0)
    except AttributeError:
        return

    for k in (b'year', b'day', b'hour', b'minute', b'second'):
        m[k] = int(m[k])

    m[b'month'] = _rfc822_months.index(m[b'month']) + 1
    if m[b'year'] < 100:
        m[b'year'] += (1900, 2000)[m[b'year'] < 90]
    stamp = datetime.datetime(*[m[i] for i in (b'year', b'month', b'day', b'hour', b'minute', b'second')])
    tzhour = 0
    tzmin = 0
    if m[b'tz'] and m[b'tz'].startswith(b'gmt'):
        m[b'tz'] = (b'').join(m[b'tz'][3:].split(b':')) or b'gmt'
    if not m[b'tz']:
        pass
    elif m[b'tz'].startswith(b'+'):
        tzhour = int(m[b'tz'][1:3])
        tzmin = int(m[b'tz'][3:])
    elif m[b'tz'].startswith(b'-'):
        tzhour = int(m[b'tz'][1:3]) * -1
        tzmin = int(m[b'tz'][3:]) * -1
    else:
        tzhour = _rfc822_tznames[m[b'tz']]
    delta = datetime.timedelta(0, 0, 0, 0, tzmin, tzhour)
    return (stamp - delta).utctimetuple()


registerDateHandler(_parse_date_rfc822)

def _parse_date_asctime(dt):
    dayname, month, day, remainder = dt.split(None, 3)
    month = b'%02i ' % (_rfc822_months.index(month.lower()) + 1)
    day = b'%02i ' % (int(day),)
    dt = month + day + remainder
    return time.strptime(dt, b'%m %d %H:%M:%S %Y')[:-1] + (0,)


registerDateHandler(_parse_date_asctime)

def _parse_date_perforce(aDateString):
    _my_date_pattern = re.compile(b'(\\w{,3}), (\\d{,4})/(\\d{,2})/(\\d{2}) (\\d{,2}):(\\d{2}):(\\d{2}) (\\w{,3})')
    m = _my_date_pattern.search(aDateString)
    if m is None:
        return
    else:
        dow, year, month, day, hour, minute, second, tz = m.groups()
        months = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        dateString = b'%s, %s %s %s %s:%s:%s %s' % (dow, day, months[int(month) - 1], year, hour, minute, second, tz)
        tm = rfc822.parsedate_tz(dateString)
        if tm:
            return time.gmtime(rfc822.mktime_tz(tm))
        return


registerDateHandler(_parse_date_perforce)

def _parse_date(dateString):
    if not dateString:
        return
    else:
        for handler in _date_handlers:
            try:
                date9tuple = handler(dateString)
            except (KeyError, OverflowError, ValueError):
                continue

            if not date9tuple:
                continue
            if len(date9tuple) != 9:
                continue
            return date9tuple

        return


def _getCharacterEncoding(http_headers, xml_data):

    def _parseHTTPContentType(content_type):
        content_type = content_type or b''
        content_type, params = cgi.parse_header(content_type)
        charset = params.get(b'charset', b'').replace(b"'", b'')
        if not isinstance(charset, unicode):
            charset = charset.decode(b'utf-8', b'ignore')
        return (
         content_type, charset)

    sniffed_xml_encoding = u''
    xml_encoding = u''
    true_encoding = u''
    http_content_type, http_encoding = _parseHTTPContentType(http_headers.get(b'content-type'))
    try:
        if xml_data[:4] == _l2bytes([76, 111, 167, 148]):
            sniffed_xml_encoding = u'cp037'
            xml_data = xml_data.decode(b'cp037').encode(b'utf-8')
        elif xml_data[:4] == _l2bytes([0, 60, 0, 63]):
            sniffed_xml_encoding = u'utf-16be'
            xml_data = unicode(xml_data, b'utf-16be').encode(b'utf-8')
        elif len(xml_data) >= 4 and xml_data[:2] == _l2bytes([254, 255]) and xml_data[2:4] != _l2bytes([0, 0]):
            sniffed_xml_encoding = u'utf-16be'
            xml_data = unicode(xml_data[2:], b'utf-16be').encode(b'utf-8')
        elif xml_data[:4] == _l2bytes([60, 0, 63, 0]):
            sniffed_xml_encoding = u'utf-16le'
            xml_data = unicode(xml_data, b'utf-16le').encode(b'utf-8')
        elif len(xml_data) >= 4 and xml_data[:2] == _l2bytes([255, 254]) and xml_data[2:4] != _l2bytes([0, 0]):
            sniffed_xml_encoding = u'utf-16le'
            xml_data = unicode(xml_data[2:], b'utf-16le').encode(b'utf-8')
        elif xml_data[:4] == _l2bytes([0, 0, 0, 60]):
            sniffed_xml_encoding = u'utf-32be'
            if _UTF32_AVAILABLE:
                xml_data = unicode(xml_data, b'utf-32be').encode(b'utf-8')
        elif xml_data[:4] == _l2bytes([60, 0, 0, 0]):
            sniffed_xml_encoding = u'utf-32le'
            if _UTF32_AVAILABLE:
                xml_data = unicode(xml_data, b'utf-32le').encode(b'utf-8')
        elif xml_data[:4] == _l2bytes([0, 0, 254, 255]):
            sniffed_xml_encoding = u'utf-32be'
            if _UTF32_AVAILABLE:
                xml_data = unicode(xml_data[4:], b'utf-32be').encode(b'utf-8')
        elif xml_data[:4] == _l2bytes([255, 254, 0, 0]):
            sniffed_xml_encoding = u'utf-32le'
            if _UTF32_AVAILABLE:
                xml_data = unicode(xml_data[4:], b'utf-32le').encode(b'utf-8')
        elif xml_data[:3] == _l2bytes([239, 187, 191]):
            sniffed_xml_encoding = u'utf-8'
            xml_data = unicode(xml_data[3:], b'utf-8').encode(b'utf-8')
        xml_encoding_match = re.compile(_s2bytes(b'^<\\?.*encoding=[\'"](.*?)[\'"].*\\?>')).match(xml_data)
    except UnicodeDecodeError:
        xml_encoding_match = None

    if xml_encoding_match:
        xml_encoding = xml_encoding_match.groups()[0].decode(b'utf-8').lower()
        if sniffed_xml_encoding and xml_encoding in (u'iso-10646-ucs-2', u'ucs-2', u'csunicode', u'iso-10646-ucs-4', u'ucs-4', u'csucs4', u'utf-16', u'utf-32', u'utf_16', u'utf_32', u'utf16', u'u16'):
            xml_encoding = sniffed_xml_encoding
    acceptable_content_type = 0
    application_content_types = (u'application/xml', u'application/xml-dtd', u'application/xml-external-parsed-entity')
    text_content_types = (u'text/xml', u'text/xml-external-parsed-entity')
    if http_content_type in application_content_types or http_content_type.startswith(u'application/') and http_content_type.endswith(u'+xml'):
        acceptable_content_type = 1
        true_encoding = http_encoding or xml_encoding or u'utf-8'
    elif http_content_type in text_content_types or http_content_type.startswith(u'text/') and http_content_type.endswith(u'+xml'):
        acceptable_content_type = 1
        true_encoding = http_encoding or u'us-ascii'
    elif http_content_type.startswith(u'text/'):
        true_encoding = http_encoding or u'us-ascii'
    elif http_headers and b'content-type' not in http_headers:
        true_encoding = xml_encoding or u'iso-8859-1'
    else:
        true_encoding = xml_encoding or u'utf-8'
    if true_encoding.lower() == u'gb2312':
        true_encoding = u'gb18030'
    return (
     true_encoding, http_encoding, xml_encoding, sniffed_xml_encoding, acceptable_content_type)


def _toUTF8(data, encoding):
    if len(data) >= 4 and data[:2] == _l2bytes([254, 255]) and data[2:4] != _l2bytes([0, 0]):
        encoding = b'utf-16be'
        data = data[2:]
    elif len(data) >= 4 and data[:2] == _l2bytes([255, 254]) and data[2:4] != _l2bytes([0, 0]):
        encoding = b'utf-16le'
        data = data[2:]
    elif data[:3] == _l2bytes([239, 187, 191]):
        encoding = b'utf-8'
        data = data[3:]
    elif data[:4] == _l2bytes([0, 0, 254, 255]):
        encoding = b'utf-32be'
        data = data[4:]
    elif data[:4] == _l2bytes([255, 254, 0, 0]):
        encoding = b'utf-32le'
        data = data[4:]
    newdata = unicode(data, encoding)
    declmatch = re.compile(b'^<\\?xml[^>]*?>')
    newdecl = b"<?xml version='1.0' encoding='utf-8'?>"
    if declmatch.search(newdata):
        newdata = declmatch.sub(newdecl, newdata)
    else:
        newdata = newdecl + u'\n' + newdata
    return newdata.encode(b'utf-8')


def _stripDoctype(data):
    start = re.search(_s2bytes(b'<\\w'), data)
    start = start and start.start() or -1
    head, data = data[:start + 1], data[start + 1:]
    entity_pattern = re.compile(_s2bytes(b'^\\s*<!ENTITY([^>]*?)>'), re.MULTILINE)
    entity_results = entity_pattern.findall(head)
    head = entity_pattern.sub(_s2bytes(b''), head)
    doctype_pattern = re.compile(_s2bytes(b'^\\s*<!DOCTYPE([^>]*?)>'), re.MULTILINE)
    doctype_results = doctype_pattern.findall(head)
    doctype = doctype_results and doctype_results[0] or _s2bytes(b'')
    if doctype.lower().count(_s2bytes(b'netscape')):
        version = u'rss091n'
    else:
        version = None
    replacement = _s2bytes(b'')
    if len(doctype_results) == 1 and entity_results:
        safe_pattern = re.compile(_s2bytes(b'\\s+(\\w+)\\s+"(&#\\w+;|[^&"]*)"'))
        safe_entities = filter((lambda e: safe_pattern.match(e)), entity_results)
        if safe_entities:
            replacement = _s2bytes(b'<!DOCTYPE feed [\n  <!ENTITY') + _s2bytes(b'>\n  <!ENTITY ').join(safe_entities) + _s2bytes(b'>\n]>')
    data = doctype_pattern.sub(replacement, head) + data
    return (
     version, data, dict(replacement and [(k.decode(b'utf-8'), v.decode(b'utf-8')) for k, v in safe_pattern.findall(replacement)]))


def parse(url_file_stream_or_string, etag=None, modified=None, agent=None, referrer=None, handlers=None, request_headers=None, response_headers=None):
    if handlers is None:
        handlers = []
    if request_headers is None:
        request_headers = {}
    if response_headers is None:
        response_headers = {}
    result = FeedParserDict()
    result[b'feed'] = FeedParserDict()
    result[b'entries'] = []
    result[b'bozo'] = 0
    if not isinstance(handlers, list):
        handlers = [
         handlers]
    try:
        f = _open_resource(url_file_stream_or_string, etag, modified, agent, referrer, handlers, request_headers)
        data = f.read()
    except Exception as e:
        result[b'bozo'] = 1
        result[b'bozo_exception'] = e
        data = None
        f = None

    if hasattr(f, b'headers'):
        result[b'headers'] = dict(f.headers)
    if b'headers' in result:
        result[b'headers'].update(response_headers)
    elif response_headers:
        result[b'headers'] = copy.deepcopy(response_headers)
    if b'headers' in result:
        http_headers = dict((k.lower(), v) for k, v in result[b'headers'].items())
    else:
        http_headers = {}
    if f and data and http_headers:
        if gzip and b'gzip' in http_headers.get(b'content-encoding', b''):
            try:
                data = gzip.GzipFile(fileobj=_StringIO(data)).read()
            except (IOError, struct.error) as e:
                result[b'bozo'] = 1
                result[b'bozo_exception'] = e
                if isinstance(e, struct.error):
                    data = None

        elif zlib and b'deflate' in http_headers.get(b'content-encoding', b''):
            try:
                data = zlib.decompress(data)
            except zlib.error as e:
                try:
                    data = zlib.decompress(data, -15)
                except zlib.error as e:
                    result[b'bozo'] = 1
                    result[b'bozo_exception'] = e

    if http_headers:
        if b'etag' in http_headers:
            etag = http_headers.get(b'etag', u'')
            if not isinstance(etag, unicode):
                etag = etag.decode(b'utf-8', b'ignore')
            if etag:
                result[b'etag'] = etag
        if b'last-modified' in http_headers:
            modified = http_headers.get(b'last-modified', u'')
            if modified:
                result[b'modified'] = modified
                result[b'modified_parsed'] = _parse_date(modified)
    if hasattr(f, b'url'):
        if not isinstance(f.url, unicode):
            result[b'href'] = f.url.decode(b'utf-8', b'ignore')
        else:
            result[b'href'] = f.url
        result[b'status'] = 200
    if hasattr(f, b'status'):
        result[b'status'] = f.status
    if hasattr(f, b'close'):
        f.close()
    if data is None:
        return result
    else:
        result[b'encoding'], http_encoding, xml_encoding, sniffed_xml_encoding, acceptable_content_type = _getCharacterEncoding(http_headers, data)
        if http_headers and not acceptable_content_type:
            if b'content-type' in http_headers:
                bozo_message = b'%s is not an XML media type' % http_headers[b'content-type']
            else:
                bozo_message = b'no Content-type specified'
            result[b'bozo'] = 1
            result[b'bozo_exception'] = NonXMLContentType(bozo_message)
        contentloc = http_headers.get(b'content-location', u'')
        href = result.get(b'href', u'')
        baseuri = _makeSafeAbsoluteURI(href, contentloc) or _makeSafeAbsoluteURI(contentloc) or href
        baselang = http_headers.get(b'content-language', None)
        if not isinstance(baselang, unicode) and baselang is not None:
            baselang = baselang.decode(b'utf-8', b'ignore')
        if getattr(f, b'code', 0) == 304:
            result[b'version'] = u''
            result[b'debug_message'] = b'The feed has not changed since you last checked, ' + b'so the server sent no data.  This is a feature, not a bug!'
            return result
        if data is None:
            return result
        use_strict_parser = 0
        known_encoding = 0
        tried_encodings = []
        for proposed_encoding in (result[b'encoding'], xml_encoding, sniffed_xml_encoding):
            if not proposed_encoding:
                continue
            if proposed_encoding in tried_encodings:
                continue
            tried_encodings.append(proposed_encoding)
            try:
                data = _toUTF8(data, proposed_encoding)
            except (UnicodeDecodeError, LookupError):
                pass
            else:
                known_encoding = use_strict_parser = 1
                break

        if not known_encoding and chardet:
            proposed_encoding = unicode(chardet.detect(data)[b'encoding'], b'ascii', b'ignore')
            if proposed_encoding and proposed_encoding not in tried_encodings:
                tried_encodings.append(proposed_encoding)
                try:
                    data = _toUTF8(data, proposed_encoding)
                except (UnicodeDecodeError, LookupError):
                    pass
                else:
                    known_encoding = use_strict_parser = 1

        if not known_encoding and u'utf-8' not in tried_encodings:
            proposed_encoding = u'utf-8'
            tried_encodings.append(proposed_encoding)
            try:
                data = _toUTF8(data, proposed_encoding)
            except UnicodeDecodeError:
                pass
            else:
                known_encoding = use_strict_parser = 1

        if not known_encoding and u'windows-1252' not in tried_encodings:
            proposed_encoding = u'windows-1252'
            tried_encodings.append(proposed_encoding)
            try:
                data = _toUTF8(data, proposed_encoding)
            except UnicodeDecodeError:
                pass
            else:
                known_encoding = use_strict_parser = 1

        if not known_encoding and u'iso-8859-2' not in tried_encodings:
            proposed_encoding = u'iso-8859-2'
            tried_encodings.append(proposed_encoding)
            try:
                data = _toUTF8(data, proposed_encoding)
            except UnicodeDecodeError:
                pass
            else:
                known_encoding = use_strict_parser = 1

        if not known_encoding:
            result[b'bozo'] = 1
            result[b'bozo_exception'] = CharacterEncodingUnknown(b'document encoding unknown, I tried ' + b'%s, %s, utf-8, windows-1252, and iso-8859-2 but nothing worked' % (
             result[b'encoding'], xml_encoding))
            result[b'encoding'] = u''
        elif proposed_encoding != result[b'encoding']:
            result[b'bozo'] = 1
            result[b'bozo_exception'] = CharacterEncodingOverride(b'document declared as %s, but parsed as %s' % (
             result[b'encoding'], proposed_encoding))
            result[b'encoding'] = proposed_encoding
        result[b'version'], data, entities = _stripDoctype(data)
        if not _XML_AVAILABLE:
            use_strict_parser = 0
        if use_strict_parser:
            feedparser = _StrictFeedParser(baseuri, baselang, b'utf-8')
            saxparser = xml.sax.make_parser(PREFERRED_XML_PARSERS)
            saxparser.setFeature(xml.sax.handler.feature_namespaces, 1)
            try:
                saxparser.setFeature(xml.sax.handler.feature_external_ges, 0)
            except xml.sax.SAXNotSupportedException:
                pass

            saxparser.setContentHandler(feedparser)
            saxparser.setErrorHandler(feedparser)
            source = xml.sax.xmlreader.InputSource()
            source.setByteStream(_StringIO(data))
            try:
                saxparser.parse(source)
            except xml.sax.SAXParseException as e:
                result[b'bozo'] = 1
                result[b'bozo_exception'] = feedparser.exc or e
                use_strict_parser = 0

        if not use_strict_parser and _SGML_AVAILABLE:
            feedparser = _LooseFeedParser(baseuri, baselang, b'utf-8', entities)
            feedparser.feed(data.decode(b'utf-8', b'replace'))
        result[b'feed'] = feedparser.feeddata
        result[b'entries'] = feedparser.entries
        result[b'version'] = result[b'version'] or feedparser.version
        result[b'namespaces'] = feedparser.namespacesInUse
        return result
