import os, urlparse, urllib, types, io, sys, handler, xmlreader
try:
    _StringTypes = [
     types.StringType, types.UnicodeType]
except AttributeError:
    _StringTypes = [
     types.StringType]

def __dict_replace(s, d):
    for key, value in d.items():
        s = s.replace(key, value)

    return s


def escape(data, entities={}):
    data = data.replace(b'&', b'&amp;')
    data = data.replace(b'>', b'&gt;')
    data = data.replace(b'<', b'&lt;')
    if entities:
        data = __dict_replace(data, entities)
    return data


def unescape(data, entities={}):
    data = data.replace(b'&lt;', b'<')
    data = data.replace(b'&gt;', b'>')
    if entities:
        data = __dict_replace(data, entities)
    return data.replace(b'&amp;', b'&')


def quoteattr(data, entities={}):
    entities = entities.copy()
    entities.update({b'\n': b'&#10;', b'\r': b'&#13;', b'\t': b'&#9;'})
    data = escape(data, entities)
    if b'"' in data:
        if b"'" in data:
            data = b'"%s"' % data.replace(b'"', b'&quot;')
        else:
            data = b"'%s'" % data
    else:
        data = b'"%s"' % data
    return data


def _gettextwriter(out, encoding):
    if out is None:
        import sys
        out = sys.stdout
    if isinstance(out, io.RawIOBase):
        buffer = io.BufferedIOBase(out)
        buffer.close = lambda : None
    else:
        buffer = io.BufferedIOBase()
        buffer.writable = lambda : True
        buffer.write = out.write
        try:
            buffer.seekable = out.seekable
            buffer.tell = out.tell
        except AttributeError:
            pass

    return _UnbufferedTextIOWrapper(buffer, encoding=encoding, errors=b'xmlcharrefreplace', newline=b'\n')


class _UnbufferedTextIOWrapper(io.TextIOWrapper):

    def write(self, s):
        super(_UnbufferedTextIOWrapper, self).write(s)
        self.flush()
        return


class XMLGenerator(handler.ContentHandler):

    def __init__(self, out=None, encoding=b'iso-8859-1'):
        handler.ContentHandler.__init__(self)
        out = _gettextwriter(out, encoding)
        self._write = out.write
        self._flush = out.flush
        self._ns_contexts = [{}]
        self._current_context = self._ns_contexts[-1]
        self._undeclared_ns_maps = []
        self._encoding = encoding
        return

    def _qname(self, name):
        if name[0]:
            if b'http://www.w3.org/XML/1998/namespace' == name[0]:
                return b'xml:' + name[1]
            prefix = self._current_context[name[0]]
            if prefix:
                return prefix + b':' + name[1]
        return name[1]

    def startDocument(self):
        self._write(u'<?xml version="1.0" encoding="%s"?>\n' % self._encoding)
        return

    def endDocument(self):
        self._flush()
        return

    def startPrefixMapping(self, prefix, uri):
        self._ns_contexts.append(self._current_context.copy())
        self._current_context[uri] = prefix
        self._undeclared_ns_maps.append((prefix, uri))
        return

    def endPrefixMapping(self, prefix):
        self._current_context = self._ns_contexts[-1]
        del self._ns_contexts[-1]
        return

    def startElement(self, name, attrs):
        self._write(u'<' + name)
        for name, value in attrs.items():
            self._write(u' %s=%s' % (name, quoteattr(value)))

        self._write(u'>')
        return

    def endElement(self, name):
        self._write(u'</%s>' % name)
        return

    def startElementNS(self, name, qname, attrs):
        self._write(u'<' + self._qname(name))
        for prefix, uri in self._undeclared_ns_maps:
            if prefix:
                self._write(u' xmlns:%s="%s"' % (prefix, uri))
            else:
                self._write(u' xmlns="%s"' % uri)

        self._undeclared_ns_maps = []
        for name, value in attrs.items():
            self._write(u' %s=%s' % (self._qname(name), quoteattr(value)))

        self._write(u'>')
        return

    def endElementNS(self, name, qname):
        self._write(u'</%s>' % self._qname(name))
        return

    def characters(self, content):
        if not isinstance(content, unicode):
            content = unicode(content, self._encoding)
        self._write(escape(content))
        return

    def ignorableWhitespace(self, content):
        if not isinstance(content, unicode):
            content = unicode(content, self._encoding)
        self._write(content)
        return

    def processingInstruction(self, target, data):
        self._write(u'<?%s %s?>' % (target, data))
        return


class XMLFilterBase(xmlreader.XMLReader):

    def __init__(self, parent=None):
        xmlreader.XMLReader.__init__(self)
        self._parent = parent
        return

    def error(self, exception):
        self._err_handler.error(exception)
        return

    def fatalError(self, exception):
        self._err_handler.fatalError(exception)
        return

    def warning(self, exception):
        self._err_handler.warning(exception)
        return

    def setDocumentLocator(self, locator):
        self._cont_handler.setDocumentLocator(locator)
        return

    def startDocument(self):
        self._cont_handler.startDocument()
        return

    def endDocument(self):
        self._cont_handler.endDocument()
        return

    def startPrefixMapping(self, prefix, uri):
        self._cont_handler.startPrefixMapping(prefix, uri)
        return

    def endPrefixMapping(self, prefix):
        self._cont_handler.endPrefixMapping(prefix)
        return

    def startElement(self, name, attrs):
        self._cont_handler.startElement(name, attrs)
        return

    def endElement(self, name):
        self._cont_handler.endElement(name)
        return

    def startElementNS(self, name, qname, attrs):
        self._cont_handler.startElementNS(name, qname, attrs)
        return

    def endElementNS(self, name, qname):
        self._cont_handler.endElementNS(name, qname)
        return

    def characters(self, content):
        self._cont_handler.characters(content)
        return

    def ignorableWhitespace(self, chars):
        self._cont_handler.ignorableWhitespace(chars)
        return

    def processingInstruction(self, target, data):
        self._cont_handler.processingInstruction(target, data)
        return

    def skippedEntity(self, name):
        self._cont_handler.skippedEntity(name)
        return

    def notationDecl(self, name, publicId, systemId):
        self._dtd_handler.notationDecl(name, publicId, systemId)
        return

    def unparsedEntityDecl(self, name, publicId, systemId, ndata):
        self._dtd_handler.unparsedEntityDecl(name, publicId, systemId, ndata)
        return

    def resolveEntity(self, publicId, systemId):
        return self._ent_handler.resolveEntity(publicId, systemId)

    def parse(self, source):
        self._parent.setContentHandler(self)
        self._parent.setErrorHandler(self)
        self._parent.setEntityResolver(self)
        self._parent.setDTDHandler(self)
        self._parent.parse(source)
        return

    def setLocale(self, locale):
        self._parent.setLocale(locale)
        return

    def getFeature(self, name):
        return self._parent.getFeature(name)

    def setFeature(self, name, state):
        self._parent.setFeature(name, state)
        return

    def getProperty(self, name):
        return self._parent.getProperty(name)

    def setProperty(self, name, value):
        self._parent.setProperty(name, value)
        return

    def getParent(self):
        return self._parent

    def setParent(self, parent):
        self._parent = parent
        return


def prepare_input_source(source, base=b''):
    if type(source) in _StringTypes:
        source = xmlreader.InputSource(source)
    elif hasattr(source, b'read'):
        f = source
        source = xmlreader.InputSource()
        source.setByteStream(f)
        if hasattr(f, b'name'):
            source.setSystemId(f.name)
    if source.getByteStream() is None:
        try:
            sysid = source.getSystemId()
            basehead = os.path.dirname(os.path.normpath(base))
            encoding = sys.getfilesystemencoding()
            if isinstance(sysid, unicode):
                if not isinstance(basehead, unicode):
                    try:
                        basehead = basehead.decode(encoding)
                    except UnicodeDecodeError:
                        sysid = sysid.encode(encoding)

            elif isinstance(basehead, unicode):
                try:
                    sysid = sysid.decode(encoding)
                except UnicodeDecodeError:
                    basehead = basehead.encode(encoding)

            sysidfilename = os.path.join(basehead, sysid)
            isfile = os.path.isfile(sysidfilename)
        except UnicodeError:
            isfile = False

        if isfile:
            source.setSystemId(sysidfilename)
            f = open(sysidfilename, b'rb')
        else:
            source.setSystemId(urlparse.urljoin(base, source.getSystemId()))
            f = urllib.urlopen(source.getSystemId())
        source.setByteStream(f)
    return source
