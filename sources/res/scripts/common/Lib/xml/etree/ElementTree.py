__all__ = [
 0, 
 1, 
 2, 3, 
 4, 5, 
 6, 7, 
 8, 9, 
 10, 11, 
 12, 
 13, 
 14, 
 15, 
 16, 
 17, 
 18, 
 19, 20]
VERSION = b'1.3.0'
import sys, re, warnings

class _SimpleElementPath(object):

    def find(self, element, tag, namespaces=None):
        for elem in element:
            if elem.tag == tag:
                return elem

        return

    def findtext(self, element, tag, default=None, namespaces=None):
        elem = self.find(element, tag)
        if elem is None:
            return default
        else:
            return elem.text or b''

    def iterfind(self, element, tag, namespaces=None):
        if tag[:3] == b'.//':
            for elem in element.iter(tag[3:]):
                yield elem

        for elem in element:
            if elem.tag == tag:
                yield elem

        return

    def findall(self, element, tag, namespaces=None):
        return list(self.iterfind(element, tag, namespaces))


try:
    from . import ElementPath
except ImportError:
    ElementPath = _SimpleElementPath()

class ParseError(SyntaxError):
    pass


def iselement(element):
    return isinstance(element, Element) or hasattr(element, b'tag')


class Element(object):
    tag = None
    attrib = None
    text = None
    tail = None

    def __init__(self, tag, attrib={}, **extra):
        attrib = attrib.copy()
        attrib.update(extra)
        self.tag = tag
        self.attrib = attrib
        self._children = []
        return

    def __repr__(self):
        return b'<Element %s at 0x%x>' % (repr(self.tag), id(self))

    def makeelement(self, tag, attrib):
        return self.__class__(tag, attrib)

    def copy(self):
        elem = self.makeelement(self.tag, self.attrib)
        elem.text = self.text
        elem.tail = self.tail
        elem[:] = self
        return elem

    def __len__(self):
        return len(self._children)

    def __nonzero__(self):
        warnings.warn(b"The behavior of this method will change in future versions.  Use specific 'len(elem)' or 'elem is not None' test instead.", FutureWarning, stacklevel=2)
        return len(self._children) != 0

    def __getitem__(self, index):
        return self._children[index]

    def __setitem__(self, index, element):
        self._children[index] = element
        return

    def __delitem__(self, index):
        del self._children[index]
        return

    def append(self, element):
        self._children.append(element)
        return

    def extend(self, elements):
        self._children.extend(elements)
        return

    def insert(self, index, element):
        self._children.insert(index, element)
        return

    def remove(self, element):
        self._children.remove(element)
        return

    def getchildren(self):
        warnings.warn(b"This method will be removed in future versions.  Use 'list(elem)' or iteration over elem instead.", DeprecationWarning, stacklevel=2)
        return self._children

    def find(self, path, namespaces=None):
        return ElementPath.find(self, path, namespaces)

    def findtext(self, path, default=None, namespaces=None):
        return ElementPath.findtext(self, path, default, namespaces)

    def findall(self, path, namespaces=None):
        return ElementPath.findall(self, path, namespaces)

    def iterfind(self, path, namespaces=None):
        return ElementPath.iterfind(self, path, namespaces)

    def clear(self):
        self.attrib.clear()
        self._children = []
        self.text = self.tail = None
        return

    def get(self, key, default=None):
        return self.attrib.get(key, default)

    def set(self, key, value):
        self.attrib[key] = value
        return

    def keys(self):
        return self.attrib.keys()

    def items(self):
        return self.attrib.items()

    def iter(self, tag=None):
        if tag == b'*':
            tag = None
        if tag is None or self.tag == tag:
            yield self
        for e in self._children:
            for e in e.iter(tag):
                yield e

        return

    def getiterator(self, tag=None):
        warnings.warn(b"This method will be removed in future versions.  Use 'elem.iter()' or 'list(elem.iter())' instead.", PendingDeprecationWarning, stacklevel=2)
        return list(self.iter(tag))

    def itertext(self):
        tag = self.tag
        if not isinstance(tag, basestring) and tag is not None:
            return
        else:
            if self.text:
                yield self.text
            for e in self:
                for s in e.itertext():
                    yield s

                if e.tail:
                    yield e.tail

            return


_Element = _ElementInterface = Element

def SubElement(parent, tag, attrib={}, **extra):
    attrib = attrib.copy()
    attrib.update(extra)
    element = parent.makeelement(tag, attrib)
    parent.append(element)
    return element


def Comment(text=None):
    element = Element(Comment)
    element.text = text
    return element


def ProcessingInstruction(target, text=None):
    element = Element(ProcessingInstruction)
    element.text = target
    if text:
        element.text = element.text + b' ' + text
    return element


PI = ProcessingInstruction

class QName(object):

    def __init__(self, text_or_uri, tag=None):
        if tag:
            text_or_uri = b'{%s}%s' % (text_or_uri, tag)
        self.text = text_or_uri
        return

    def __str__(self):
        return self.text

    def __hash__(self):
        return hash(self.text)

    def __cmp__(self, other):
        if isinstance(other, QName):
            return cmp(self.text, other.text)
        return cmp(self.text, other)


class ElementTree(object):

    def __init__(self, element=None, file=None):
        self._root = element
        if file:
            self.parse(file)
        return

    def getroot(self):
        return self._root

    def _setroot(self, element):
        self._root = element
        return

    def parse(self, source, parser=None):
        close_source = False
        if not hasattr(source, b'read'):
            source = open(source, b'rb')
            close_source = True
        try:
            if not parser:
                parser = XMLParser(target=TreeBuilder())
            while 1:
                data = source.read(65536)
                if not data:
                    break
                parser.feed(data)

            self._root = parser.close()
            return self._root
        finally:
            if close_source:
                source.close()

        return

    def iter(self, tag=None):
        return self._root.iter(tag)

    def getiterator(self, tag=None):
        warnings.warn(b"This method will be removed in future versions.  Use 'tree.iter()' or 'list(tree.iter())' instead.", PendingDeprecationWarning, stacklevel=2)
        return list(self.iter(tag))

    def find(self, path, namespaces=None):
        if path[:1] == b'/':
            path = b'.' + path
            warnings.warn(b'This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path, FutureWarning, stacklevel=2)
        return self._root.find(path, namespaces)

    def findtext(self, path, default=None, namespaces=None):
        if path[:1] == b'/':
            path = b'.' + path
            warnings.warn(b'This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path, FutureWarning, stacklevel=2)
        return self._root.findtext(path, default, namespaces)

    def findall(self, path, namespaces=None):
        if path[:1] == b'/':
            path = b'.' + path
            warnings.warn(b'This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path, FutureWarning, stacklevel=2)
        return self._root.findall(path, namespaces)

    def iterfind(self, path, namespaces=None):
        if path[:1] == b'/':
            path = b'.' + path
            warnings.warn(b'This search is broken in 1.3 and earlier, and will be fixed in a future version.  If you rely on the current behaviour, change it to %r' % path, FutureWarning, stacklevel=2)
        return self._root.iterfind(path, namespaces)

    def write(self, file_or_filename, encoding=None, xml_declaration=None, default_namespace=None, method=None):
        if not method:
            method = b'xml'
        elif method not in _serialize:
            raise ValueError(b'unknown method %r' % method)
        if hasattr(file_or_filename, b'write'):
            file = file_or_filename
        else:
            file = open(file_or_filename, b'wb')
        write = file.write
        if not encoding:
            if method == b'c14n':
                encoding = b'utf-8'
            else:
                encoding = b'us-ascii'
        elif xml_declaration or xml_declaration is None and encoding not in (b'utf-8', b'us-ascii'):
            if method == b'xml':
                write(b"<?xml version='1.0' encoding='%s'?>\n" % encoding)
        if method == b'text':
            _serialize_text(write, self._root, encoding)
        else:
            qnames, namespaces = _namespaces(self._root, encoding, default_namespace)
            serialize = _serialize[method]
            serialize(write, self._root, encoding, qnames, namespaces)
        if file_or_filename is not file:
            file.close()
        return

    def write_c14n(self, file):
        return self.write(file, method=b'c14n')


def _namespaces(elem, encoding, default_namespace=None):
    qnames = {None: None}
    namespaces = {}
    if default_namespace:
        namespaces[default_namespace] = b''

    def encode(text):
        return text.encode(encoding)

    def add_qname(qname):
        try:
            if qname[:1] == b'{':
                uri, tag = qname[1:].rsplit(b'}', 1)
                prefix = namespaces.get(uri)
                if prefix is None:
                    prefix = _namespace_map.get(uri)
                    if prefix is None:
                        prefix = b'ns%d' % len(namespaces)
                    if prefix != b'xml':
                        namespaces[uri] = prefix
                if prefix:
                    qnames[qname] = encode(b'%s:%s' % (prefix, tag))
                else:
                    qnames[qname] = encode(tag)
            elif default_namespace:
                raise ValueError(b'cannot use non-qualified names with default_namespace option')
            qnames[qname] = encode(qname)
        except TypeError:
            _raise_serialization_error(qname)

        return

    try:
        iterate = elem.iter
    except AttributeError:
        iterate = elem.getiterator

    for elem in iterate():
        tag = elem.tag
        if isinstance(tag, QName):
            if tag.text not in qnames:
                add_qname(tag.text)
        elif isinstance(tag, basestring):
            if tag not in qnames:
                add_qname(tag)
        elif tag is not None and tag is not Comment and tag is not PI:
            _raise_serialization_error(tag)
        for key, value in elem.items():
            if isinstance(key, QName):
                key = key.text
            if key not in qnames:
                add_qname(key)
            if isinstance(value, QName) and value.text not in qnames:
                add_qname(value.text)

        text = elem.text
        if isinstance(text, QName) and text.text not in qnames:
            add_qname(text.text)

    return (
     qnames, namespaces)


def _serialize_xml(write, elem, encoding, qnames, namespaces):
    tag = elem.tag
    text = elem.text
    if tag is Comment:
        write(b'<!--%s-->' % _encode(text, encoding))
    elif tag is ProcessingInstruction:
        write(b'<?%s?>' % _encode(text, encoding))
    else:
        tag = qnames[tag]
        if tag is None:
            if text:
                write(_escape_cdata(text, encoding))
            for e in elem:
                _serialize_xml(write, e, encoding, qnames, None)

        else:
            write(b'<' + tag)
            items = elem.items()
            if items or namespaces:
                if namespaces:
                    for v, k in sorted(namespaces.items(), key=(lambda x: x[1])):
                        if k:
                            k = b':' + k
                        write(b' xmlns%s="%s"' % (
                         k.encode(encoding),
                         _escape_attrib(v, encoding)))

                for k, v in sorted(items):
                    if isinstance(k, QName):
                        k = k.text
                    if isinstance(v, QName):
                        v = qnames[v.text]
                    else:
                        v = _escape_attrib(v, encoding)
                    write(b' %s="%s"' % (qnames[k], v))

            if text or len(elem):
                write(b'>')
                if text:
                    write(_escape_cdata(text, encoding))
                for e in elem:
                    _serialize_xml(write, e, encoding, qnames, None)

                write(b'</' + tag + b'>')
            else:
                write(b' />')
    if elem.tail:
        write(_escape_cdata(elem.tail, encoding))
    return


HTML_EMPTY = (
 b'area', b'base', b'basefont', b'br', b'col', b'frame', b'hr',
 b'img', b'input', b'isindex', b'link', b'meta', b'param')
try:
    HTML_EMPTY = set(HTML_EMPTY)
except NameError:
    pass

def _serialize_html(write, elem, encoding, qnames, namespaces):
    tag = elem.tag
    text = elem.text
    if tag is Comment:
        write(b'<!--%s-->' % _escape_cdata(text, encoding))
    elif tag is ProcessingInstruction:
        write(b'<?%s?>' % _escape_cdata(text, encoding))
    else:
        tag = qnames[tag]
        if tag is None:
            if text:
                write(_escape_cdata(text, encoding))
            for e in elem:
                _serialize_html(write, e, encoding, qnames, None)

        else:
            write(b'<' + tag)
            items = elem.items()
            if items or namespaces:
                if namespaces:
                    for v, k in sorted(namespaces.items(), key=(lambda x: x[1])):
                        if k:
                            k = b':' + k
                        write(b' xmlns%s="%s"' % (
                         k.encode(encoding),
                         _escape_attrib(v, encoding)))

                for k, v in sorted(items):
                    if isinstance(k, QName):
                        k = k.text
                    if isinstance(v, QName):
                        v = qnames[v.text]
                    else:
                        v = _escape_attrib_html(v, encoding)
                    write(b' %s="%s"' % (qnames[k], v))

            write(b'>')
            ltag = tag.lower()
            if text:
                if ltag == b'script' or ltag == b'style':
                    write(_encode(text, encoding))
                else:
                    write(_escape_cdata(text, encoding))
            for e in elem:
                _serialize_html(write, e, encoding, qnames, None)

            if ltag not in HTML_EMPTY:
                write(b'</' + tag + b'>')
    if elem.tail:
        write(_escape_cdata(elem.tail, encoding))
    return


def _serialize_text(write, elem, encoding):
    for part in elem.itertext():
        write(part.encode(encoding))

    if elem.tail:
        write(elem.tail.encode(encoding))
    return


_serialize = {b'xml': _serialize_xml, 
   b'html': _serialize_html, 
   b'text': _serialize_text}

def register_namespace(prefix, uri):
    if re.match(b'ns\\d+$', prefix):
        raise ValueError(b'Prefix format reserved for internal use')
    for k, v in _namespace_map.items():
        if k == uri or v == prefix:
            del _namespace_map[k]

    _namespace_map[uri] = prefix
    return


_namespace_map = {b'http://www.w3.org/XML/1998/namespace': b'xml', 
   b'http://www.w3.org/1999/xhtml': b'html', 
   b'http://www.w3.org/1999/02/22-rdf-syntax-ns#': b'rdf', 
   b'http://schemas.xmlsoap.org/wsdl/': b'wsdl', 
   b'http://www.w3.org/2001/XMLSchema': b'xs', 
   b'http://www.w3.org/2001/XMLSchema-instance': b'xsi', 
   b'http://purl.org/dc/elements/1.1/': b'dc'}

def _raise_serialization_error(text):
    raise TypeError(b'cannot serialize %r (type %s)' % (text, type(text).__name__))
    return


def _encode(text, encoding):
    try:
        return text.encode(encoding, b'xmlcharrefreplace')
    except (TypeError, AttributeError):
        _raise_serialization_error(text)

    return


def _escape_cdata(text, encoding):
    try:
        if b'&' in text:
            text = text.replace(b'&', b'&amp;')
        if b'<' in text:
            text = text.replace(b'<', b'&lt;')
        if b'>' in text:
            text = text.replace(b'>', b'&gt;')
        return text.encode(encoding, b'xmlcharrefreplace')
    except (TypeError, AttributeError):
        _raise_serialization_error(text)

    return


def _escape_attrib(text, encoding):
    try:
        if b'&' in text:
            text = text.replace(b'&', b'&amp;')
        if b'<' in text:
            text = text.replace(b'<', b'&lt;')
        if b'>' in text:
            text = text.replace(b'>', b'&gt;')
        if b'"' in text:
            text = text.replace(b'"', b'&quot;')
        if b'\n' in text:
            text = text.replace(b'\n', b'&#10;')
        return text.encode(encoding, b'xmlcharrefreplace')
    except (TypeError, AttributeError):
        _raise_serialization_error(text)

    return


def _escape_attrib_html(text, encoding):
    try:
        if b'&' in text:
            text = text.replace(b'&', b'&amp;')
        if b'>' in text:
            text = text.replace(b'>', b'&gt;')
        if b'"' in text:
            text = text.replace(b'"', b'&quot;')
        return text.encode(encoding, b'xmlcharrefreplace')
    except (TypeError, AttributeError):
        _raise_serialization_error(text)

    return


def tostring(element, encoding=None, method=None):

    class dummy:
        pass

    data = []
    file = dummy()
    file.write = data.append
    ElementTree(element).write(file, encoding, method=method)
    return (b'').join(data)


def tostringlist(element, encoding=None, method=None):

    class dummy:
        pass

    data = []
    file = dummy()
    file.write = data.append
    ElementTree(element).write(file, encoding, method=method)
    return data


def dump(elem):
    if not isinstance(elem, ElementTree):
        elem = ElementTree(elem)
    elem.write(sys.stdout)
    tail = elem.getroot().tail
    if not tail or tail[-1] != b'\n':
        sys.stdout.write(b'\n')
    return


def parse(source, parser=None):
    tree = ElementTree()
    tree.parse(source, parser)
    return tree


def iterparse(source, events=None, parser=None):
    close_source = False
    if not hasattr(source, b'read'):
        source = open(source, b'rb')
        close_source = True
    try:
        if not parser:
            parser = XMLParser(target=TreeBuilder())
        return _IterParseIterator(source, events, parser, close_source)
    except:
        if close_source:
            source.close()
        raise

    return


class _IterParseIterator(object):

    def __init__(self, source, events, parser, close_source=False):
        self._file = source
        self._close_file = close_source
        self._events = []
        self._index = 0
        self._error = None
        self.root = self._root = None
        self._parser = parser
        parser = self._parser._parser
        append = self._events.append
        if events is None:
            events = [
             b'end']
        for event in events:
            if event == b'start':
                try:
                    parser.ordered_attributes = 1
                    parser.specified_attributes = 1

                    def handler(tag, attrib_in, event=event, append=append, start=self._parser._start_list):
                        append((event, start(tag, attrib_in)))
                        return

                    parser.StartElementHandler = handler
                except AttributeError:

                    def handler(tag, attrib_in, event=event, append=append, start=self._parser._start):
                        append((event, start(tag, attrib_in)))
                        return

                    parser.StartElementHandler = handler

            elif event == b'end':

                def handler(tag, event=event, append=append, end=self._parser._end):
                    append((event, end(tag)))
                    return

                parser.EndElementHandler = handler
            elif event == b'start-ns':

                def handler(prefix, uri, event=event, append=append):
                    try:
                        uri = (uri or b'').encode(b'ascii')
                    except UnicodeError:
                        pass

                    append((event, (prefix or b'', uri or b'')))
                    return

                parser.StartNamespaceDeclHandler = handler
            elif event == b'end-ns':

                def handler(prefix, event=event, append=append):
                    append((event, None))
                    return

                parser.EndNamespaceDeclHandler = handler
            else:
                raise ValueError(b'unknown event %r' % event)

        return

    def next(self):
        try:
            while 1:
                try:
                    item = self._events[self._index]
                    self._index += 1
                    return item
                except IndexError:
                    pass

                if self._error:
                    e = self._error
                    self._error = None
                    raise e
                if self._parser is None:
                    self.root = self._root
                    break
                del self._events[:]
                self._index = 0
                data = self._file.read(16384)
                if data:
                    try:
                        self._parser.feed(data)
                    except SyntaxError as exc:
                        self._error = exc

                else:
                    self._root = self._parser.close()
                    self._parser = None

        except:
            if self._close_file:
                self._file.close()
            raise

        if self._close_file:
            self._file.close()
        raise StopIteration
        return

    def __iter__(self):
        return self


def XML(text, parser=None):
    if not parser:
        parser = XMLParser(target=TreeBuilder())
    parser.feed(text)
    return parser.close()


def XMLID(text, parser=None):
    if not parser:
        parser = XMLParser(target=TreeBuilder())
    parser.feed(text)
    tree = parser.close()
    ids = {}
    for elem in tree.iter():
        id = elem.get(b'id')
        if id:
            ids[id] = elem

    return (
     tree, ids)


fromstring = XML

def fromstringlist(sequence, parser=None):
    if not parser:
        parser = XMLParser(target=TreeBuilder())
    for text in sequence:
        parser.feed(text)

    return parser.close()


class TreeBuilder(object):

    def __init__(self, element_factory=None):
        self._data = []
        self._elem = []
        self._last = None
        self._tail = None
        if element_factory is None:
            element_factory = Element
        self._factory = element_factory
        return

    def close(self):
        return self._last

    def _flush(self):
        if self._data:
            if self._last is not None:
                text = (b'').join(self._data)
                if self._tail:
                    self._last.tail = text
                else:
                    self._last.text = text
            self._data = []
        return

    def data(self, data):
        self._data.append(data)
        return

    def start(self, tag, attrs):
        self._flush()
        self._last = elem = self._factory(tag, attrs)
        if self._elem:
            self._elem[-1].append(elem)
        self._elem.append(elem)
        self._tail = 0
        return elem

    def end(self, tag):
        self._flush()
        self._last = self._elem.pop()
        self._tail = 1
        return self._last


_sentinel = [
 b'sentinel']

class XMLParser(object):

    def __init__(self, html=_sentinel, target=None, encoding=None):
        if html is not _sentinel:
            warnings.warnpy3k(b'The html argument of XMLParser() is deprecated', DeprecationWarning, stacklevel=2)
        try:
            from xml.parsers import expat
        except ImportError:
            try:
                import pyexpat as expat
            except ImportError:
                raise ImportError(b'No module named expat; use SimpleXMLTreeBuilder instead')

        parser = expat.ParserCreate(encoding, b'}')
        if target is None:
            target = TreeBuilder()
        self.parser = self._parser = parser
        self.target = self._target = target
        self._error = expat.error
        self._names = {}
        parser.DefaultHandlerExpand = self._default
        parser.StartElementHandler = self._start
        parser.EndElementHandler = self._end
        parser.CharacterDataHandler = self._data
        parser.CommentHandler = self._comment
        parser.ProcessingInstructionHandler = self._pi
        try:
            self._parser.buffer_text = 1
        except AttributeError:
            pass

        try:
            self._parser.ordered_attributes = 1
            self._parser.specified_attributes = 1
            parser.StartElementHandler = self._start_list
        except AttributeError:
            pass

        self._doctype = None
        self.entity = {}
        try:
            self.version = b'Expat %d.%d.%d' % expat.version_info
        except AttributeError:
            pass

        return

    def _raiseerror(self, value):
        err = ParseError(value)
        err.code = value.code
        err.position = (value.lineno, value.offset)
        raise err
        return

    def _fixtext(self, text):
        try:
            return text.encode(b'ascii')
        except UnicodeError:
            return text

        return

    def _fixname(self, key):
        try:
            name = self._names[key]
        except KeyError:
            name = key
            if b'}' in name:
                name = b'{' + name
            self._names[key] = name = self._fixtext(name)

        return name

    def _start(self, tag, attrib_in):
        fixname = self._fixname
        fixtext = self._fixtext
        tag = fixname(tag)
        attrib = {}
        for key, value in attrib_in.items():
            attrib[fixname(key)] = fixtext(value)

        return self.target.start(tag, attrib)

    def _start_list(self, tag, attrib_in):
        fixname = self._fixname
        fixtext = self._fixtext
        tag = fixname(tag)
        attrib = {}
        if attrib_in:
            for i in range(0, len(attrib_in), 2):
                attrib[fixname(attrib_in[i])] = fixtext(attrib_in[i + 1])

        return self.target.start(tag, attrib)

    def _data(self, text):
        return self.target.data(self._fixtext(text))

    def _end(self, tag):
        return self.target.end(self._fixname(tag))

    def _comment(self, data):
        try:
            comment = self.target.comment
        except AttributeError:
            pass
        else:
            return comment(self._fixtext(data))

        return

    def _pi(self, target, data):
        try:
            pi = self.target.pi
        except AttributeError:
            pass
        else:
            return pi(self._fixtext(target), self._fixtext(data))

        return

    def _default(self, text):
        prefix = text[:1]
        if prefix == b'&':
            try:
                self.target.data(self.entity[text[1:-1]])
            except KeyError:
                from xml.parsers import expat
                err = expat.error(b'undefined entity %s: line %d, column %d' % (
                 text, self._parser.ErrorLineNumber,
                 self._parser.ErrorColumnNumber))
                err.code = 11
                err.lineno = self._parser.ErrorLineNumber
                err.offset = self._parser.ErrorColumnNumber
                raise err

        elif prefix == b'<' and text[:9] == b'<!DOCTYPE':
            self._doctype = []
        elif self._doctype is not None:
            if prefix == b'>':
                self._doctype = None
                return
            text = text.strip()
            if not text:
                return
            self._doctype.append(text)
            n = len(self._doctype)
            if n > 2:
                type = self._doctype[1]
                if type == b'PUBLIC' and n == 4:
                    name, type, pubid, system = self._doctype
                elif type == b'SYSTEM' and n == 3:
                    name, type, system = self._doctype
                    pubid = None
                else:
                    return
                if pubid:
                    pubid = pubid[1:-1]
                if hasattr(self.target, b'doctype'):
                    self.target.doctype(name, pubid, system[1:-1])
                elif self.doctype != self.__doctype:
                    self.__doctype(name, pubid, system[1:-1])
                    self.doctype(name, pubid, system[1:-1])
                self._doctype = None
        return

    def doctype(self, name, pubid, system):
        warnings.warn(b'This method of XMLParser is deprecated.  Define doctype() method on the TreeBuilder target.', DeprecationWarning)
        return

    __doctype = doctype

    def feed(self, data):
        try:
            self._parser.Parse(data, 0)
        except self._error as v:
            self._raiseerror(v)

        return

    def close(self):
        try:
            self._parser.Parse(b'', 1)
        except self._error as v:
            self._raiseerror(v)

        tree = self.target.close()
        del self.target
        del self._target
        del self.parser
        del self._parser
        return tree


XMLTreeBuilder = XMLParser
try:
    from ElementC14N import _serialize_c14n
    _serialize[b'c14n'] = _serialize_c14n
except ImportError:
    pass
