_XML_NAMESPACE_ATTR = b'xmlns'

class PyExtension(object):
    __slots__ = (b'_name', b'_children', b'_attributes')

    def __init__(self, name):
        super(PyExtension, self).__init__()
        self._name = name
        self._children = []
        self._attributes = []
        return

    def clear(self):
        self._name = b''
        self._attributes = []
        while self._children:
            self._children.pop().clear()

        return

    def getName(self):
        return self._name

    def getCData(self, pyGlooxTag):
        return pyGlooxTag.getCData()

    def getXmlNs(self):
        result = b''
        if self._attributes:
            key, value = self._attributes[0]
            if key == _XML_NAMESPACE_ATTR:
                result = value
        return result

    def setXmlNs(self, ns):
        self._attributes.insert(0, (_XML_NAMESPACE_ATTR, ns))
        return self

    def setAttribute(self, name, value):
        self._attributes.append((name, value))
        return self

    def getChild(self, index):
        child = None
        if index < len(self._children):
            child = self._children[index]
        return child

    def setChild(self, ext):
        self._children.append(ext)
        return self

    def getChildCount(self):
        return len(self._children)

    def getXPath(self, index=None, suffix=b'', name=None):
        if name is None:
            name = self._name
        attrName, attrValue = self._getXPathAttr()
        if attrName and attrValue:
            result = (b"{0}[@{1}='{2}']").format(name, attrName, attrValue)
        else:
            result = name
        if index is not None:
            child = self.getChild(index)
            if child:
                return self._addChildToXPath(result, child, suffix)
        return self._addSuffixToXPath(result, suffix)

    def getTag(self):
        subTags = self._makeChildrenString()
        if subTags:
            result = (b'<{0}{1}>{2}</{0}>').format(self._name, self._makeAttributesString(), subTags)
        elif self._name:
            result = (b'<{0}{1}/>').format(self._name, self._makeAttributesString())
        else:
            result = b''
        self.clear()
        return result

    def parseTag(self, pyGlooxTag):
        return

    @classmethod
    def getDefaultData(cls):
        return

    def _getXPathAttr(self):
        return (
         _XML_NAMESPACE_ATTR, self.getXmlNs())

    def _makeAttributesString(self):
        result = []
        for name, value in self._attributes:
            result.append((b" {0}='{1}'").format(name, value))

        return (b'').join(result)

    def _makeChildrenString(self):
        result = []
        for child in self._children:
            result.append(child.getTag())

        return (b'').join(result)

    def _addChildToXPath(self, xPath, child, suffix=b''):
        childPath = child.getXPath()
        if hasattr(childPath, b'__iter__'):
            xPath = (b'|').join([(b'/').join((xPath, path)) for path in childPath])
        else:
            xPath = (b'/').join((xPath, childPath))
        return self._addSuffixToXPath(xPath, suffix)

    def _addSuffixToXPath(self, xPath, suffix=b''):
        if suffix:
            xPath = (b'{0}/{1}').format(xPath, suffix)
        return xPath

    def _getChildTags(self, pyGlooxTag, index=0):
        result = pyGlooxTag.filterXPath(self.getXPath(index))
        for tag in result:
            yield tag

        return

    def _getChildData(self, pyGlooxTag, index=0, default=None):
        result = pyGlooxTag.filterXPath(self.getXPath(index))
        if result:
            data = self.getChild(index).parseTag(result[0])
        else:
            data = default
        return data


class SimpleExtension(PyExtension):
    __slots__ = (b'_value',)

    def __init__(self, name, value):
        super(SimpleExtension, self).__init__(name)
        self._value = str(value)
        return

    def _makeChildrenString(self):
        return self._value


class PyQuery(object):
    __slots__ = (b'_type', b'_to', b'_ext')

    def __init__(self, queryType, queryExt=None, to=b''):
        super(PyQuery, self).__init__()
        self._type = queryType
        self._ext = queryExt
        self._to = to
        return

    def getType(self):
        return self._type

    def getTo(self):
        return self._to

    def getTag(self):
        tag = b''
        if self._ext:
            tag = self._ext.getTag()
        return tag


class PyHandler(object):
    __slots__ = (b'_ext',)

    def __init__(self, ext):
        super(PyHandler, self).__init__()
        self._ext = ext
        return

    def clear(self):
        if self._ext:
            self._ext.clear()
            self._ext = None
        return

    def getFilterString(self):
        raise NotImplementedError
        return

    def handleTag(self, pyGlooxTag):
        result = pyGlooxTag.filterXPath(self.getFilterString())
        if result:
            result = self._ext.parseTag(result[0])
        else:
            result = self._ext.getDefaultData()
        return result
