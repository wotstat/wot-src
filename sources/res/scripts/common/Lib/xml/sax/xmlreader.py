import handler
from _exceptions import SAXNotSupportedException, SAXNotRecognizedException

class XMLReader:

    def __init__(self):
        self._cont_handler = handler.ContentHandler()
        self._dtd_handler = handler.DTDHandler()
        self._ent_handler = handler.EntityResolver()
        self._err_handler = handler.ErrorHandler()
        return

    def parse(self, source):
        raise NotImplementedError(b'This method must be implemented!')
        return

    def getContentHandler(self):
        return self._cont_handler

    def setContentHandler(self, handler):
        self._cont_handler = handler
        return

    def getDTDHandler(self):
        return self._dtd_handler

    def setDTDHandler(self, handler):
        self._dtd_handler = handler
        return

    def getEntityResolver(self):
        return self._ent_handler

    def setEntityResolver(self, resolver):
        self._ent_handler = resolver
        return

    def getErrorHandler(self):
        return self._err_handler

    def setErrorHandler(self, handler):
        self._err_handler = handler
        return

    def setLocale(self, locale):
        raise SAXNotSupportedException(b'Locale support not implemented')
        return

    def getFeature(self, name):
        raise SAXNotRecognizedException(b"Feature '%s' not recognized" % name)
        return

    def setFeature(self, name, state):
        raise SAXNotRecognizedException(b"Feature '%s' not recognized" % name)
        return

    def getProperty(self, name):
        raise SAXNotRecognizedException(b"Property '%s' not recognized" % name)
        return

    def setProperty(self, name, value):
        raise SAXNotRecognizedException(b"Property '%s' not recognized" % name)
        return


class IncrementalParser(XMLReader):

    def __init__(self, bufsize=65536):
        self._bufsize = bufsize
        XMLReader.__init__(self)
        return

    def parse(self, source):
        import saxutils
        source = saxutils.prepare_input_source(source)
        self.prepareParser(source)
        file = source.getByteStream()
        buffer = file.read(self._bufsize)
        while buffer != b'':
            self.feed(buffer)
            buffer = file.read(self._bufsize)

        self.close()
        return

    def feed(self, data):
        raise NotImplementedError(b'This method must be implemented!')
        return

    def prepareParser(self, source):
        raise NotImplementedError(b'prepareParser must be overridden!')
        return

    def close(self):
        raise NotImplementedError(b'This method must be implemented!')
        return

    def reset(self):
        raise NotImplementedError(b'This method must be implemented!')
        return


class Locator:

    def getColumnNumber(self):
        return -1

    def getLineNumber(self):
        return -1

    def getPublicId(self):
        return

    def getSystemId(self):
        return


class InputSource:

    def __init__(self, system_id=None):
        self.__system_id = system_id
        self.__public_id = None
        self.__encoding = None
        self.__bytefile = None
        self.__charfile = None
        return

    def setPublicId(self, public_id):
        self.__public_id = public_id
        return

    def getPublicId(self):
        return self.__public_id

    def setSystemId(self, system_id):
        self.__system_id = system_id
        return

    def getSystemId(self):
        return self.__system_id

    def setEncoding(self, encoding):
        self.__encoding = encoding
        return

    def getEncoding(self):
        return self.__encoding

    def setByteStream(self, bytefile):
        self.__bytefile = bytefile
        return

    def getByteStream(self):
        return self.__bytefile

    def setCharacterStream(self, charfile):
        self.__charfile = charfile
        return

    def getCharacterStream(self):
        return self.__charfile


class AttributesImpl:

    def __init__(self, attrs):
        self._attrs = attrs
        return

    def getLength(self):
        return len(self._attrs)

    def getType(self, name):
        return b'CDATA'

    def getValue(self, name):
        return self._attrs[name]

    def getValueByQName(self, name):
        return self._attrs[name]

    def getNameByQName(self, name):
        if name not in self._attrs:
            raise KeyError, name
        return name

    def getQNameByName(self, name):
        if name not in self._attrs:
            raise KeyError, name
        return name

    def getNames(self):
        return self._attrs.keys()

    def getQNames(self):
        return self._attrs.keys()

    def __len__(self):
        return len(self._attrs)

    def __getitem__(self, name):
        return self._attrs[name]

    def keys(self):
        return self._attrs.keys()

    def has_key(self, name):
        return name in self._attrs

    def __contains__(self, name):
        return name in self._attrs

    def get(self, name, alternative=None):
        return self._attrs.get(name, alternative)

    def copy(self):
        return self.__class__(self._attrs)

    def items(self):
        return self._attrs.items()

    def values(self):
        return self._attrs.values()


class AttributesNSImpl(AttributesImpl):

    def __init__(self, attrs, qnames):
        self._attrs = attrs
        self._qnames = qnames
        return

    def getValueByQName(self, name):
        for nsname, qname in self._qnames.items():
            if qname == name:
                return self._attrs[nsname]

        raise KeyError, name
        return

    def getNameByQName(self, name):
        for nsname, qname in self._qnames.items():
            if qname == name:
                return nsname

        raise KeyError, name
        return

    def getQNameByName(self, name):
        return self._qnames[name]

    def getQNames(self):
        return self._qnames.values()

    def copy(self):
        return self.__class__(self._attrs, self._qnames)


def _test():
    XMLReader()
    IncrementalParser()
    Locator()
    return


if __name__ == b'__main__':
    _test()
