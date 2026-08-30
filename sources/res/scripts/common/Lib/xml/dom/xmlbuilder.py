import copy, xml.dom
from xml.dom.NodeFilter import NodeFilter
__all__ = [
 b'DOMBuilder', b'DOMEntityResolver', b'DOMInputSource']

class Options:
    namespaces = 1
    namespace_declarations = True
    validation = False
    external_parameter_entities = True
    external_general_entities = True
    external_dtd_subset = True
    validate_if_schema = False
    validate = False
    datatype_normalization = False
    create_entity_ref_nodes = True
    entities = True
    whitespace_in_element_content = True
    cdata_sections = True
    comments = True
    charset_overrides_xml_encoding = True
    infoset = False
    supported_mediatypes_only = False
    errorHandler = None
    filter = None


class DOMBuilder:
    entityResolver = None
    errorHandler = None
    filter = None
    ACTION_REPLACE = 1
    ACTION_APPEND_AS_CHILDREN = 2
    ACTION_INSERT_AFTER = 3
    ACTION_INSERT_BEFORE = 4
    _legal_actions = (
     ACTION_REPLACE, ACTION_APPEND_AS_CHILDREN,
     ACTION_INSERT_AFTER, ACTION_INSERT_BEFORE)

    def __init__(self):
        self._options = Options()
        return

    def _get_entityResolver(self):
        return self.entityResolver

    def _set_entityResolver(self, entityResolver):
        self.entityResolver = entityResolver
        return

    def _get_errorHandler(self):
        return self.errorHandler

    def _set_errorHandler(self, errorHandler):
        self.errorHandler = errorHandler
        return

    def _get_filter(self):
        return self.filter

    def _set_filter(self, filter):
        self.filter = filter
        return

    def setFeature(self, name, state):
        if self.supportsFeature(name):
            state = state and 1 or 0
            try:
                settings = self._settings[_name_xform(name), state]
            except KeyError:
                raise xml.dom.NotSupportedErr(b'unsupported feature: %r' % (name,))

            for name, value in settings:
                setattr(self._options, name, value)

        else:
            raise xml.dom.NotFoundErr(b'unknown feature: ' + repr(name))
        return

    def supportsFeature(self, name):
        return hasattr(self._options, _name_xform(name))

    def canSetFeature(self, name, state):
        key = (
         _name_xform(name), state and 1 or 0)
        return key in self._settings

    _settings = {(b'namespace_declarations', 0): [
                                      (b'namespace_declarations', 0)], 
       (b'namespace_declarations', 1): [
                                      (b'namespace_declarations', 1)], 
       (b'validation', 0): [
                          (b'validation', 0)], 
       (b'external_general_entities', 0): [
                                         (b'external_general_entities', 0)], 
       (b'external_general_entities', 1): [
                                         (b'external_general_entities', 1)], 
       (b'external_parameter_entities', 0): [
                                           (b'external_parameter_entities', 0)], 
       (b'external_parameter_entities', 1): [
                                           (b'external_parameter_entities', 1)], 
       (b'validate_if_schema', 0): [
                                  (b'validate_if_schema', 0)], 
       (b'create_entity_ref_nodes', 0): [
                                       (b'create_entity_ref_nodes', 0)], 
       (b'create_entity_ref_nodes', 1): [
                                       (b'create_entity_ref_nodes', 1)], 
       (b'entities', 0): [
                        (b'create_entity_ref_nodes', 0),
                        (b'entities', 0)], 
       (b'entities', 1): [
                        (b'entities', 1)], 
       (b'whitespace_in_element_content', 0): [
                                             (b'whitespace_in_element_content', 0)], 
       (b'whitespace_in_element_content', 1): [
                                             (b'whitespace_in_element_content', 1)], 
       (b'cdata_sections', 0): [
                              (b'cdata_sections', 0)], 
       (b'cdata_sections', 1): [
                              (b'cdata_sections', 1)], 
       (b'comments', 0): [
                        (b'comments', 0)], 
       (b'comments', 1): [
                        (b'comments', 1)], 
       (b'charset_overrides_xml_encoding', 0): [
                                              (b'charset_overrides_xml_encoding', 0)], 
       (b'charset_overrides_xml_encoding', 1): [
                                              (b'charset_overrides_xml_encoding', 1)], 
       (b'infoset', 0): [], (b'infoset', 1): [
                       78, 
                       79, 
                       80, 
                       81, 
                       82, 
                       83, 
                       84, 
                       85, 
                       86], 
       (b'supported_mediatypes_only', 0): [
                                         (b'supported_mediatypes_only', 0)], 
       (b'namespaces', 0): [
                          (b'namespaces', 0)], 
       (b'namespaces', 1): [
                          (b'namespaces', 1)]}

    def getFeature(self, name):
        xname = _name_xform(name)
        try:
            return getattr(self._options, xname)
        except AttributeError:
            if name == b'infoset':
                options = self._options
                return options.datatype_normalization and options.whitespace_in_element_content and options.comments and options.charset_overrides_xml_encoding and not (options.namespace_declarations or options.validate_if_schema or options.create_entity_ref_nodes or options.entities or options.cdata_sections)
            raise xml.dom.NotFoundErr(b'feature %s not known' % repr(name))

        return

    def parseURI(self, uri):
        if self.entityResolver:
            input = self.entityResolver.resolveEntity(None, uri)
        else:
            input = DOMEntityResolver().resolveEntity(None, uri)
        return self.parse(input)

    def parse(self, input):
        options = copy.copy(self._options)
        options.filter = self.filter
        options.errorHandler = self.errorHandler
        fp = input.byteStream
        if fp is None and options.systemId:
            import urllib2
            fp = urllib2.urlopen(input.systemId)
        return self._parse_bytestream(fp, options)

    def parseWithContext(self, input, cnode, action):
        if action not in self._legal_actions:
            raise ValueError(b'not a legal action')
        raise NotImplementedError(b"Haven't written this yet...")
        return

    def _parse_bytestream(self, stream, options):
        import xml.dom.expatbuilder
        builder = xml.dom.expatbuilder.makeBuilder(options)
        return builder.parseFile(stream)


def _name_xform(name):
    return name.lower().replace(b'-', b'_')


class DOMEntityResolver(object):
    __slots__ = (b'_opener',)

    def resolveEntity(self, publicId, systemId):
        source = DOMInputSource()
        source.publicId = publicId
        source.systemId = systemId
        source.byteStream = self._get_opener().open(systemId)
        source.encoding = self._guess_media_encoding(source)
        import posixpath, urlparse
        parts = urlparse.urlparse(systemId)
        scheme, netloc, path, params, query, fragment = parts
        if path and not path.endswith(b'/'):
            path = posixpath.dirname(path) + b'/'
            parts = (scheme, netloc, path, params, query, fragment)
            source.baseURI = urlparse.urlunparse(parts)
        return source

    def _get_opener(self):
        try:
            return self._opener
        except AttributeError:
            self._opener = self._create_opener()
            return self._opener

        return

    def _create_opener(self):
        import urllib2
        return urllib2.build_opener()

    def _guess_media_encoding(self, source):
        info = source.byteStream.info()
        if b'Content-Type' in info:
            for param in info.getplist():
                if param.startswith(b'charset='):
                    return param.split(b'=', 1)[1].lower()

        return


class DOMInputSource(object):
    __slots__ = (b'byteStream', b'characterStream', b'stringData', b'encoding', b'publicId', b'systemId', b'baseURI')

    def __init__(self):
        self.byteStream = None
        self.characterStream = None
        self.stringData = None
        self.encoding = None
        self.publicId = None
        self.systemId = None
        self.baseURI = None
        return

    def _get_byteStream(self):
        return self.byteStream

    def _set_byteStream(self, byteStream):
        self.byteStream = byteStream
        return

    def _get_characterStream(self):
        return self.characterStream

    def _set_characterStream(self, characterStream):
        self.characterStream = characterStream
        return

    def _get_stringData(self):
        return self.stringData

    def _set_stringData(self, data):
        self.stringData = data
        return

    def _get_encoding(self):
        return self.encoding

    def _set_encoding(self, encoding):
        self.encoding = encoding
        return

    def _get_publicId(self):
        return self.publicId

    def _set_publicId(self, publicId):
        self.publicId = publicId
        return

    def _get_systemId(self):
        return self.systemId

    def _set_systemId(self, systemId):
        self.systemId = systemId
        return

    def _get_baseURI(self):
        return self.baseURI

    def _set_baseURI(self, uri):
        self.baseURI = uri
        return


class DOMBuilderFilter:
    FILTER_ACCEPT = 1
    FILTER_REJECT = 2
    FILTER_SKIP = 3
    FILTER_INTERRUPT = 4
    whatToShow = NodeFilter.SHOW_ALL

    def _get_whatToShow(self):
        return self.whatToShow

    def acceptNode(self, element):
        return self.FILTER_ACCEPT

    def startContainer(self, element):
        return self.FILTER_ACCEPT


del NodeFilter

class DocumentLS:
    async = False

    def _get_async(self):
        return False

    def _set_async(self, async):
        if async:
            raise xml.dom.NotSupportedErr(b'asynchronous document loading is not supported')
        return

    def abort(self):
        raise NotImplementedError(b"haven't figured out what this means yet")
        return

    def load(self, uri):
        raise NotImplementedError(b"haven't written this yet")
        return

    def loadXML(self, source):
        raise NotImplementedError(b"haven't written this yet")
        return

    def saveXML(self, snode):
        if snode is None:
            snode = self
        elif snode.ownerDocument is not self:
            raise xml.dom.WrongDocumentErr()
        return snode.toxml()


class DOMImplementationLS:
    MODE_SYNCHRONOUS = 1
    MODE_ASYNCHRONOUS = 2

    def createDOMBuilder(self, mode, schemaType):
        if schemaType is not None:
            raise xml.dom.NotSupportedErr(b'schemaType not yet supported')
        if mode == self.MODE_SYNCHRONOUS:
            return DOMBuilder()
        else:
            if mode == self.MODE_ASYNCHRONOUS:
                raise xml.dom.NotSupportedErr(b'asynchronous builders are not supported')
            raise ValueError(b'unknown value for mode')
            return

    def createDOMWriter(self):
        raise NotImplementedError(b"the writer interface hasn't been written yet!")
        return

    def createDOMInputSource(self):
        return DOMInputSource()
