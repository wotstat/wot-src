version = b'2.0beta'

class ErrorHandler:

    def error(self, exception):
        raise exception
        return

    def fatalError(self, exception):
        raise exception
        return

    def warning(self, exception):
        print exception
        return


class ContentHandler:

    def __init__(self):
        self._locator = None
        return

    def setDocumentLocator(self, locator):
        self._locator = locator
        return

    def startDocument(self):
        return

    def endDocument(self):
        return

    def startPrefixMapping(self, prefix, uri):
        return

    def endPrefixMapping(self, prefix):
        return

    def startElement(self, name, attrs):
        return

    def endElement(self, name):
        return

    def startElementNS(self, name, qname, attrs):
        return

    def endElementNS(self, name, qname):
        return

    def characters(self, content):
        return

    def ignorableWhitespace(self, whitespace):
        return

    def processingInstruction(self, target, data):
        return

    def skippedEntity(self, name):
        return


class DTDHandler:

    def notationDecl(self, name, publicId, systemId):
        return

    def unparsedEntityDecl(self, name, publicId, systemId, ndata):
        return


class EntityResolver:

    def resolveEntity(self, publicId, systemId):
        return systemId


feature_namespaces = b'http://xml.org/sax/features/namespaces'
feature_namespace_prefixes = b'http://xml.org/sax/features/namespace-prefixes'
feature_string_interning = b'http://xml.org/sax/features/string-interning'
feature_validation = b'http://xml.org/sax/features/validation'
feature_external_ges = b'http://xml.org/sax/features/external-general-entities'
feature_external_pes = b'http://xml.org/sax/features/external-parameter-entities'
all_features = [
 feature_namespaces, 
 feature_namespace_prefixes, 
 feature_string_interning, 
 feature_validation, 
 feature_external_ges, 
 feature_external_pes]
property_lexical_handler = b'http://xml.org/sax/properties/lexical-handler'
property_declaration_handler = b'http://xml.org/sax/properties/declaration-handler'
property_dom_node = b'http://xml.org/sax/properties/dom-node'
property_xml_string = b'http://xml.org/sax/properties/xml-string'
property_encoding = b'http://www.python.org/sax/properties/encoding'
property_interning_dict = b'http://www.python.org/sax/properties/interning-dict'
all_properties = [
 property_lexical_handler, 
 property_dom_node, 
 property_declaration_handler, 
 property_xml_string, 
 property_encoding, 
 property_interning_dict]
