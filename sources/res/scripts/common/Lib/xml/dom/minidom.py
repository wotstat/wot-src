import xml.dom
from xml.dom import EMPTY_NAMESPACE, EMPTY_PREFIX, XMLNS_NAMESPACE, domreg
from xml.dom.minicompat import *
from xml.dom.xmlbuilder import DOMImplementationLS, DocumentLS
_nodeTypes_with_children = (
 xml.dom.Node.ELEMENT_NODE,
 xml.dom.Node.ENTITY_REFERENCE_NODE)

class Node(xml.dom.Node):
    namespaceURI = None
    parentNode = None
    ownerDocument = None
    nextSibling = None
    previousSibling = None
    prefix = EMPTY_PREFIX

    def __nonzero__(self):
        return True

    def toxml(self, encoding=None):
        return self.toprettyxml(b'', b'', encoding)

    def toprettyxml(self, indent=b'\t', newl=b'\n', encoding=None):
        writer = _get_StringIO()
        if encoding is not None:
            import codecs
            writer = codecs.lookup(encoding)[3](writer)
        if self.nodeType == Node.DOCUMENT_NODE:
            self.writexml(writer, b'', indent, newl, encoding)
        else:
            self.writexml(writer, b'', indent, newl)
        return writer.getvalue()

    def hasChildNodes(self):
        if self.childNodes:
            return True
        else:
            return False

        return

    def _get_childNodes(self):
        return self.childNodes

    def _get_firstChild(self):
        if self.childNodes:
            return self.childNodes[0]
        return

    def _get_lastChild(self):
        if self.childNodes:
            return self.childNodes[-1]
        return

    def insertBefore(self, newChild, refChild):
        if newChild.nodeType == self.DOCUMENT_FRAGMENT_NODE:
            for c in tuple(newChild.childNodes):
                self.insertBefore(c, refChild)

            return newChild
        if newChild.nodeType not in self._child_node_types:
            raise xml.dom.HierarchyRequestErr(b'%s cannot be child of %s' % (repr(newChild), repr(self)))
        if newChild.parentNode is not None:
            newChild.parentNode.removeChild(newChild)
        if refChild is None:
            self.appendChild(newChild)
        else:
            try:
                index = self.childNodes.index(refChild)
            except ValueError:
                raise xml.dom.NotFoundErr()

            if newChild.nodeType in _nodeTypes_with_children:
                _clear_id_cache(self)
            self.childNodes.insert(index, newChild)
            newChild.nextSibling = refChild
            refChild.previousSibling = newChild
            if index:
                node = self.childNodes[index - 1]
                node.nextSibling = newChild
                newChild.previousSibling = node
            else:
                newChild.previousSibling = None
            newChild.parentNode = self
        return newChild

    def appendChild(self, node):
        if node.nodeType == self.DOCUMENT_FRAGMENT_NODE:
            for c in tuple(node.childNodes):
                self.appendChild(c)

            return node
        if node.nodeType not in self._child_node_types:
            raise xml.dom.HierarchyRequestErr(b'%s cannot be child of %s' % (repr(node), repr(self)))
        elif node.nodeType in _nodeTypes_with_children:
            _clear_id_cache(self)
        if node.parentNode is not None:
            node.parentNode.removeChild(node)
        _append_child(self, node)
        node.nextSibling = None
        return node

    def replaceChild(self, newChild, oldChild):
        if newChild.nodeType == self.DOCUMENT_FRAGMENT_NODE:
            refChild = oldChild.nextSibling
            self.removeChild(oldChild)
            return self.insertBefore(newChild, refChild)
        else:
            if newChild.nodeType not in self._child_node_types:
                raise xml.dom.HierarchyRequestErr(b'%s cannot be child of %s' % (repr(newChild), repr(self)))
            if newChild is oldChild:
                return
            if newChild.parentNode is not None:
                newChild.parentNode.removeChild(newChild)
            try:
                index = self.childNodes.index(oldChild)
            except ValueError:
                raise xml.dom.NotFoundErr()

            self.childNodes[index] = newChild
            newChild.parentNode = self
            oldChild.parentNode = None
            if newChild.nodeType in _nodeTypes_with_children or oldChild.nodeType in _nodeTypes_with_children:
                _clear_id_cache(self)
            newChild.nextSibling = oldChild.nextSibling
            newChild.previousSibling = oldChild.previousSibling
            oldChild.nextSibling = None
            oldChild.previousSibling = None
            if newChild.previousSibling:
                newChild.previousSibling.nextSibling = newChild
            if newChild.nextSibling:
                newChild.nextSibling.previousSibling = newChild
            return oldChild

    def removeChild(self, oldChild):
        try:
            self.childNodes.remove(oldChild)
        except ValueError:
            raise xml.dom.NotFoundErr()

        if oldChild.nextSibling is not None:
            oldChild.nextSibling.previousSibling = oldChild.previousSibling
        if oldChild.previousSibling is not None:
            oldChild.previousSibling.nextSibling = oldChild.nextSibling
        oldChild.nextSibling = oldChild.previousSibling = None
        if oldChild.nodeType in _nodeTypes_with_children:
            _clear_id_cache(self)
        oldChild.parentNode = None
        return oldChild

    def normalize(self):
        L = []
        for child in self.childNodes:
            if child.nodeType == Node.TEXT_NODE:
                if not child.data:
                    if L:
                        L[-1].nextSibling = child.nextSibling
                    if child.nextSibling:
                        child.nextSibling.previousSibling = child.previousSibling
                    child.unlink()
                elif L and L[-1].nodeType == child.nodeType:
                    node = L[-1]
                    node.data = node.data + child.data
                    node.nextSibling = child.nextSibling
                    if child.nextSibling:
                        child.nextSibling.previousSibling = node
                    child.unlink()
                else:
                    L.append(child)
            else:
                L.append(child)
                if child.nodeType == Node.ELEMENT_NODE:
                    child.normalize()

        self.childNodes[:] = L
        return

    def cloneNode(self, deep):
        return _clone_node(self, deep, self.ownerDocument or self)

    def isSupported(self, feature, version):
        return self.ownerDocument.implementation.hasFeature(feature, version)

    def _get_localName(self):
        return

    def isSameNode(self, other):
        return self is other

    def getInterface(self, feature):
        if self.isSupported(feature, None):
            return self
        else:
            return
            return

    def getUserData(self, key):
        try:
            return self._user_data[key][0]
        except (AttributeError, KeyError):
            return

        return

    def setUserData(self, key, data, handler):
        old = None
        try:
            d = self._user_data
        except AttributeError:
            d = {}
            self._user_data = d

        if key in d:
            old = d[key][0]
        if data is None:
            handler = None
            if old is not None:
                del d[key]
        else:
            d[key] = (
             data, handler)
        return old

    def _call_user_data_handler(self, operation, src, dst):
        if hasattr(self, b'_user_data'):
            for key, (data, handler) in self._user_data.items():
                if handler is not None:
                    handler.handle(operation, key, data, src, dst)

        return

    def unlink(self):
        self.parentNode = self.ownerDocument = None
        if self.childNodes:
            for child in self.childNodes:
                child.unlink()

            self.childNodes = NodeList()
        self.previousSibling = None
        self.nextSibling = None
        return


defproperty(Node, b'firstChild', doc=b'First child node, or None.')
defproperty(Node, b'lastChild', doc=b'Last child node, or None.')
defproperty(Node, b'localName', doc=b'Namespace-local name of this node.')

def _append_child(self, node):
    childNodes = self.childNodes
    if childNodes:
        last = childNodes[-1]
        node.__dict__[b'previousSibling'] = last
        last.__dict__[b'nextSibling'] = node
    childNodes.append(node)
    node.__dict__[b'parentNode'] = self
    return


def _in_document(node):
    while node is not None:
        if node.nodeType == Node.DOCUMENT_NODE:
            return True
        node = node.parentNode

    return False


def _write_data(writer, data):
    if data:
        data = data.replace(b'&', b'&amp;').replace(b'<', b'&lt;').replace(b'"', b'&quot;').replace(b'>', b'&gt;')
        writer.write(data)
    return


def _get_elements_by_tagName_helper(parent, name, rc):
    for node in parent.childNodes:
        if node.nodeType == Node.ELEMENT_NODE and (name == b'*' or node.tagName == name):
            rc.append(node)
        _get_elements_by_tagName_helper(node, name, rc)

    return rc


def _get_elements_by_tagName_ns_helper(parent, nsURI, localName, rc):
    for node in parent.childNodes:
        if node.nodeType == Node.ELEMENT_NODE:
            if (localName == b'*' or node.localName == localName) and (nsURI == b'*' or node.namespaceURI == nsURI):
                rc.append(node)
            _get_elements_by_tagName_ns_helper(node, nsURI, localName, rc)

    return rc


class DocumentFragment(Node):
    nodeType = Node.DOCUMENT_FRAGMENT_NODE
    nodeName = b'#document-fragment'
    nodeValue = None
    attributes = None
    parentNode = None
    _child_node_types = (Node.ELEMENT_NODE,
     Node.TEXT_NODE,
     Node.CDATA_SECTION_NODE,
     Node.ENTITY_REFERENCE_NODE,
     Node.PROCESSING_INSTRUCTION_NODE,
     Node.COMMENT_NODE,
     Node.NOTATION_NODE)

    def __init__(self):
        self.childNodes = NodeList()
        return


class Attr(Node):
    nodeType = Node.ATTRIBUTE_NODE
    attributes = None
    ownerElement = None
    specified = False
    _is_id = False
    _child_node_types = (
     Node.TEXT_NODE, Node.ENTITY_REFERENCE_NODE)

    def __init__(self, qName, namespaceURI=EMPTY_NAMESPACE, localName=None, prefix=None):
        d = self.__dict__
        d[b'nodeName'] = d[b'name'] = qName
        d[b'namespaceURI'] = namespaceURI
        d[b'prefix'] = prefix
        d[b'childNodes'] = NodeList()
        self.childNodes.append(Text())
        return

    def _get_localName(self):
        return self.nodeName.split(b':', 1)[-1]

    def _get_specified(self):
        return self.specified

    def __setattr__(self, name, value):
        d = self.__dict__
        if name in (b'value', b'nodeValue'):
            d[b'value'] = d[b'nodeValue'] = value
            d2 = self.childNodes[0].__dict__
            d2[b'data'] = d2[b'nodeValue'] = value
            if self.ownerElement is not None:
                _clear_id_cache(self.ownerElement)
        elif name in (b'name', b'nodeName'):
            d[b'name'] = d[b'nodeName'] = value
            if self.ownerElement is not None:
                _clear_id_cache(self.ownerElement)
        else:
            d[name] = value
        return

    def _set_prefix(self, prefix):
        nsuri = self.namespaceURI
        if prefix == b'xmlns':
            if nsuri and nsuri != XMLNS_NAMESPACE:
                raise xml.dom.NamespaceErr(b"illegal use of 'xmlns' prefix for the wrong namespace")
        d = self.__dict__
        d[b'prefix'] = prefix
        if prefix is None:
            newName = self.localName
        else:
            newName = b'%s:%s' % (prefix, self.localName)
        if self.ownerElement:
            _clear_id_cache(self.ownerElement)
        d[b'nodeName'] = d[b'name'] = newName
        return

    def _set_value(self, value):
        d = self.__dict__
        d[b'value'] = d[b'nodeValue'] = value
        if self.ownerElement:
            _clear_id_cache(self.ownerElement)
        self.childNodes[0].data = value
        return

    def unlink(self):
        elem = self.ownerElement
        if elem is not None:
            del elem._attrs[self.nodeName]
            del elem._attrsNS[(self.namespaceURI, self.localName)]
            if self._is_id:
                self._is_id = False
                elem._magic_id_nodes -= 1
                self.ownerDocument._magic_id_count -= 1
        for child in self.childNodes:
            child.unlink()

        del self.childNodes[:]
        return

    def _get_isId(self):
        if self._is_id:
            return True
        else:
            doc = self.ownerDocument
            elem = self.ownerElement
            if doc is None or elem is None:
                return False
            info = doc._get_elem_info(elem)
            if info is None:
                return False
            if self.namespaceURI:
                return info.isIdNS(self.namespaceURI, self.localName)
            return info.isId(self.nodeName)
            return

    def _get_schemaType(self):
        doc = self.ownerDocument
        elem = self.ownerElement
        if doc is None or elem is None:
            return _no_type
        info = doc._get_elem_info(elem)
        if info is None:
            return _no_type
        else:
            if self.namespaceURI:
                return info.getAttributeTypeNS(self.namespaceURI, self.localName)
            else:
                return info.getAttributeType(self.nodeName)

            return


defproperty(Attr, b'isId', doc=b'True if this attribute is an ID.')
defproperty(Attr, b'localName', doc=b'Namespace-local name of this attribute.')
defproperty(Attr, b'schemaType', doc=b'Schema type for this attribute.')

class NamedNodeMap(object):
    __slots__ = (b'_attrs', b'_attrsNS', b'_ownerElement')

    def __init__(self, attrs, attrsNS, ownerElement):
        self._attrs = attrs
        self._attrsNS = attrsNS
        self._ownerElement = ownerElement
        return

    def _get_length(self):
        return len(self._attrs)

    def item(self, index):
        try:
            return self[self._attrs.keys()[index]]
        except IndexError:
            return

        return

    def items(self):
        L = []
        for node in self._attrs.values():
            L.append((node.nodeName, node.value))

        return L

    def itemsNS(self):
        L = []
        for node in self._attrs.values():
            L.append(((node.namespaceURI, node.localName), node.value))

        return L

    def has_key(self, key):
        if isinstance(key, StringTypes):
            return key in self._attrs
        else:
            return key in self._attrsNS

        return

    def keys(self):
        return self._attrs.keys()

    def keysNS(self):
        return self._attrsNS.keys()

    def values(self):
        return self._attrs.values()

    def get(self, name, value=None):
        return self._attrs.get(name, value)

    __len__ = _get_length
    __hash__ = None

    def __cmp__(self, other):
        if self._attrs is getattr(other, b'_attrs', None):
            return 0
        else:
            return cmp(id(self), id(other))
            return

    def __getitem__(self, attname_or_tuple):
        if isinstance(attname_or_tuple, tuple):
            return self._attrsNS[attname_or_tuple]
        else:
            return self._attrs[attname_or_tuple]

        return

    def __setitem__(self, attname, value):
        if isinstance(value, StringTypes):
            try:
                node = self._attrs[attname]
            except KeyError:
                node = Attr(attname)
                node.ownerDocument = self._ownerElement.ownerDocument
                self.setNamedItem(node)

            node.value = value
        elif not isinstance(value, Attr):
            raise TypeError, b'value must be a string or Attr object'
        node = value
        self.setNamedItem(node)
        return

    def getNamedItem(self, name):
        try:
            return self._attrs[name]
        except KeyError:
            return

        return

    def getNamedItemNS(self, namespaceURI, localName):
        try:
            return self._attrsNS[namespaceURI, localName]
        except KeyError:
            return

        return

    def removeNamedItem(self, name):
        n = self.getNamedItem(name)
        if n is not None:
            _clear_id_cache(self._ownerElement)
            del self._attrs[n.nodeName]
            del self._attrsNS[(n.namespaceURI, n.localName)]
            if b'ownerElement' in n.__dict__:
                n.__dict__[b'ownerElement'] = None
            return n
        raise xml.dom.NotFoundErr()
        return

    def removeNamedItemNS(self, namespaceURI, localName):
        n = self.getNamedItemNS(namespaceURI, localName)
        if n is not None:
            _clear_id_cache(self._ownerElement)
            del self._attrsNS[(n.namespaceURI, n.localName)]
            del self._attrs[n.nodeName]
            if b'ownerElement' in n.__dict__:
                n.__dict__[b'ownerElement'] = None
            return n
        raise xml.dom.NotFoundErr()
        return

    def setNamedItem(self, node):
        if not isinstance(node, Attr):
            raise xml.dom.HierarchyRequestErr(b'%s cannot be child of %s' % (repr(node), repr(self)))
        old = self._attrs.get(node.name)
        if old:
            old.unlink()
        self._attrs[node.name] = node
        self._attrsNS[(node.namespaceURI, node.localName)] = node
        node.ownerElement = self._ownerElement
        _clear_id_cache(node.ownerElement)
        return old

    def setNamedItemNS(self, node):
        return self.setNamedItem(node)

    def __delitem__(self, attname_or_tuple):
        node = self[attname_or_tuple]
        _clear_id_cache(node.ownerElement)
        node.unlink()
        return

    def __getstate__(self):
        return (self._attrs, self._attrsNS, self._ownerElement)

    def __setstate__(self, state):
        self._attrs, self._attrsNS, self._ownerElement = state
        return


defproperty(NamedNodeMap, b'length', doc=b'Number of nodes in the NamedNodeMap.')
AttributeList = NamedNodeMap

class TypeInfo(object):
    __slots__ = (b'namespace', b'name')

    def __init__(self, namespace, name):
        self.namespace = namespace
        self.name = name
        return

    def __repr__(self):
        if self.namespace:
            return b'<TypeInfo %r (from %r)>' % (self.name, self.namespace)
        else:
            return b'<TypeInfo %r>' % self.name

        return

    def _get_name(self):
        return self.name

    def _get_namespace(self):
        return self.namespace


_no_type = TypeInfo(None, None)

class Element(Node):
    nodeType = Node.ELEMENT_NODE
    nodeValue = None
    schemaType = _no_type
    _magic_id_nodes = 0
    _child_node_types = (
     Node.ELEMENT_NODE,
     Node.PROCESSING_INSTRUCTION_NODE,
     Node.COMMENT_NODE,
     Node.TEXT_NODE,
     Node.CDATA_SECTION_NODE,
     Node.ENTITY_REFERENCE_NODE)

    def __init__(self, tagName, namespaceURI=EMPTY_NAMESPACE, prefix=None, localName=None):
        self.tagName = self.nodeName = tagName
        self.prefix = prefix
        self.namespaceURI = namespaceURI
        self.childNodes = NodeList()
        self._attrs = {}
        self._attrsNS = {}
        return

    def _get_localName(self):
        return self.tagName.split(b':', 1)[-1]

    def _get_tagName(self):
        return self.tagName

    def unlink(self):
        for attr in self._attrs.values():
            attr.unlink()

        self._attrs = None
        self._attrsNS = None
        Node.unlink(self)
        return

    def getAttribute(self, attname):
        try:
            return self._attrs[attname].value
        except KeyError:
            return b''

        return

    def getAttributeNS(self, namespaceURI, localName):
        try:
            return self._attrsNS[namespaceURI, localName].value
        except KeyError:
            return b''

        return

    def setAttribute(self, attname, value):
        attr = self.getAttributeNode(attname)
        if attr is None:
            attr = Attr(attname)
            d = attr.__dict__
            d[b'value'] = d[b'nodeValue'] = value
            d[b'ownerDocument'] = self.ownerDocument
            self.setAttributeNode(attr)
        elif value != attr.value:
            d = attr.__dict__
            d[b'value'] = d[b'nodeValue'] = value
            if attr.isId:
                _clear_id_cache(self)
        return

    def setAttributeNS(self, namespaceURI, qualifiedName, value):
        prefix, localname = _nssplit(qualifiedName)
        attr = self.getAttributeNodeNS(namespaceURI, localname)
        if attr is None:
            attr = Attr(qualifiedName, namespaceURI, localname, prefix)
            d = attr.__dict__
            d[b'prefix'] = prefix
            d[b'nodeName'] = qualifiedName
            d[b'value'] = d[b'nodeValue'] = value
            d[b'ownerDocument'] = self.ownerDocument
            self.setAttributeNode(attr)
        else:
            d = attr.__dict__
            if value != attr.value:
                d[b'value'] = d[b'nodeValue'] = value
                if attr.isId:
                    _clear_id_cache(self)
            if attr.prefix != prefix:
                d[b'prefix'] = prefix
                d[b'nodeName'] = qualifiedName
        return

    def getAttributeNode(self, attrname):
        return self._attrs.get(attrname)

    def getAttributeNodeNS(self, namespaceURI, localName):
        return self._attrsNS.get((namespaceURI, localName))

    def setAttributeNode(self, attr):
        if attr.ownerElement not in (None, self):
            raise xml.dom.InuseAttributeErr(b'attribute node already owned')
        old1 = self._attrs.get(attr.name, None)
        if old1 is not None:
            self.removeAttributeNode(old1)
        old2 = self._attrsNS.get((attr.namespaceURI, attr.localName), None)
        if old2 is not None and old2 is not old1:
            self.removeAttributeNode(old2)
        _set_attribute_node(self, attr)
        if old1 is not attr:
            return old1
        else:
            if old2 is not attr:
                return old2
            return

    setAttributeNodeNS = setAttributeNode

    def removeAttribute(self, name):
        try:
            attr = self._attrs[name]
        except KeyError:
            raise xml.dom.NotFoundErr()

        self.removeAttributeNode(attr)
        return

    def removeAttributeNS(self, namespaceURI, localName):
        try:
            attr = self._attrsNS[namespaceURI, localName]
        except KeyError:
            raise xml.dom.NotFoundErr()

        self.removeAttributeNode(attr)
        return

    def removeAttributeNode(self, node):
        if node is None:
            raise xml.dom.NotFoundErr()
        try:
            self._attrs[node.name]
        except KeyError:
            raise xml.dom.NotFoundErr()

        _clear_id_cache(self)
        node.unlink()
        node.ownerDocument = self.ownerDocument
        return

    removeAttributeNodeNS = removeAttributeNode

    def hasAttribute(self, name):
        return name in self._attrs

    def hasAttributeNS(self, namespaceURI, localName):
        return (
         namespaceURI, localName) in self._attrsNS

    def getElementsByTagName(self, name):
        return _get_elements_by_tagName_helper(self, name, NodeList())

    def getElementsByTagNameNS(self, namespaceURI, localName):
        return _get_elements_by_tagName_ns_helper(self, namespaceURI, localName, NodeList())

    def __repr__(self):
        return b'<DOM Element: %s at %#x>' % (self.tagName, id(self))

    def writexml(self, writer, indent=b'', addindent=b'', newl=b''):
        writer.write(indent + b'<' + self.tagName)
        attrs = self._get_attributes()
        a_names = attrs.keys()
        a_names.sort()
        for a_name in a_names:
            writer.write(b' %s="' % a_name)
            _write_data(writer, attrs[a_name].value)
            writer.write(b'"')

        if self.childNodes:
            writer.write(b'>')
            if len(self.childNodes) == 1 and self.childNodes[0].nodeType == Node.TEXT_NODE:
                self.childNodes[0].writexml(writer, b'', b'', b'')
            else:
                writer.write(newl)
                for node in self.childNodes:
                    node.writexml(writer, indent + addindent, addindent, newl)

                writer.write(indent)
            writer.write(b'</%s>%s' % (self.tagName, newl))
        else:
            writer.write(b'/>%s' % newl)
        return

    def _get_attributes(self):
        return NamedNodeMap(self._attrs, self._attrsNS, self)

    def hasAttributes(self):
        if self._attrs:
            return True
        else:
            return False

        return

    def setIdAttribute(self, name):
        idAttr = self.getAttributeNode(name)
        self.setIdAttributeNode(idAttr)
        return

    def setIdAttributeNS(self, namespaceURI, localName):
        idAttr = self.getAttributeNodeNS(namespaceURI, localName)
        self.setIdAttributeNode(idAttr)
        return

    def setIdAttributeNode(self, idAttr):
        if idAttr is None or not self.isSameNode(idAttr.ownerElement):
            raise xml.dom.NotFoundErr()
        if _get_containing_entref(self) is not None:
            raise xml.dom.NoModificationAllowedErr()
        if not idAttr._is_id:
            idAttr.__dict__[b'_is_id'] = True
            self._magic_id_nodes += 1
            self.ownerDocument._magic_id_count += 1
            _clear_id_cache(self)
        return


defproperty(Element, b'attributes', doc=b'NamedNodeMap of attributes on the element.')
defproperty(Element, b'localName', doc=b'Namespace-local name of this element.')

def _set_attribute_node(element, attr):
    _clear_id_cache(element)
    element._attrs[attr.name] = attr
    element._attrsNS[(attr.namespaceURI, attr.localName)] = attr
    attr.__dict__[b'ownerElement'] = element
    return


class Childless():
    attributes = None
    childNodes = EmptyNodeList()
    firstChild = None
    lastChild = None

    def _get_firstChild(self):
        return

    def _get_lastChild(self):
        return

    def appendChild(self, node):
        raise xml.dom.HierarchyRequestErr(self.nodeName + b' nodes cannot have children')
        return

    def hasChildNodes(self):
        return False

    def insertBefore(self, newChild, refChild):
        raise xml.dom.HierarchyRequestErr(self.nodeName + b' nodes do not have children')
        return

    def removeChild(self, oldChild):
        raise xml.dom.NotFoundErr(self.nodeName + b' nodes do not have children')
        return

    def normalize(self):
        return

    def replaceChild(self, newChild, oldChild):
        raise xml.dom.HierarchyRequestErr(self.nodeName + b' nodes do not have children')
        return


class ProcessingInstruction(Childless, Node):
    nodeType = Node.PROCESSING_INSTRUCTION_NODE

    def __init__(self, target, data):
        self.target = self.nodeName = target
        self.data = self.nodeValue = data
        return

    def _get_data(self):
        return self.data

    def _set_data(self, value):
        d = self.__dict__
        d[b'data'] = d[b'nodeValue'] = value
        return

    def _get_target(self):
        return self.target

    def _set_target(self, value):
        d = self.__dict__
        d[b'target'] = d[b'nodeName'] = value
        return

    def __setattr__(self, name, value):
        if name == b'data' or name == b'nodeValue':
            self.__dict__[b'data'] = self.__dict__[b'nodeValue'] = value
        elif name == b'target' or name == b'nodeName':
            self.__dict__[b'target'] = self.__dict__[b'nodeName'] = value
        else:
            self.__dict__[name] = value
        return

    def writexml(self, writer, indent=b'', addindent=b'', newl=b''):
        writer.write(b'%s<?%s %s?>%s' % (indent, self.target, self.data, newl))
        return


class CharacterData(Childless, Node):

    def _get_length(self):
        return len(self.data)

    __len__ = _get_length

    def _get_data(self):
        return self.__dict__[b'data']

    def _set_data(self, data):
        d = self.__dict__
        d[b'data'] = d[b'nodeValue'] = data
        return

    _get_nodeValue = _get_data
    _set_nodeValue = _set_data

    def __setattr__(self, name, value):
        if name == b'data' or name == b'nodeValue':
            self.__dict__[b'data'] = self.__dict__[b'nodeValue'] = value
        else:
            self.__dict__[name] = value
        return

    def __repr__(self):
        data = self.data
        if len(data) > 10:
            dotdotdot = b'...'
        else:
            dotdotdot = b''
        return b'<DOM %s node "%r%s">' % (
         self.__class__.__name__, data[0:10], dotdotdot)

    def substringData(self, offset, count):
        if offset < 0:
            raise xml.dom.IndexSizeErr(b'offset cannot be negative')
        if offset >= len(self.data):
            raise xml.dom.IndexSizeErr(b'offset cannot be beyond end of data')
        if count < 0:
            raise xml.dom.IndexSizeErr(b'count cannot be negative')
        return self.data[offset:offset + count]

    def appendData(self, arg):
        self.data = self.data + arg
        return

    def insertData(self, offset, arg):
        if offset < 0:
            raise xml.dom.IndexSizeErr(b'offset cannot be negative')
        if offset >= len(self.data):
            raise xml.dom.IndexSizeErr(b'offset cannot be beyond end of data')
        if arg:
            self.data = b'%s%s%s' % (
             self.data[:offset], arg, self.data[offset:])
        return

    def deleteData(self, offset, count):
        if offset < 0:
            raise xml.dom.IndexSizeErr(b'offset cannot be negative')
        if offset >= len(self.data):
            raise xml.dom.IndexSizeErr(b'offset cannot be beyond end of data')
        if count < 0:
            raise xml.dom.IndexSizeErr(b'count cannot be negative')
        if count:
            self.data = self.data[:offset] + self.data[offset + count:]
        return

    def replaceData(self, offset, count, arg):
        if offset < 0:
            raise xml.dom.IndexSizeErr(b'offset cannot be negative')
        if offset >= len(self.data):
            raise xml.dom.IndexSizeErr(b'offset cannot be beyond end of data')
        if count < 0:
            raise xml.dom.IndexSizeErr(b'count cannot be negative')
        if count:
            self.data = b'%s%s%s' % (
             self.data[:offset], arg, self.data[offset + count:])
        return


defproperty(CharacterData, b'length', doc=b'Length of the string data.')

class Text(CharacterData):
    nodeType = Node.TEXT_NODE
    nodeName = b'#text'
    attributes = None

    def splitText(self, offset):
        if offset < 0 or offset > len(self.data):
            raise xml.dom.IndexSizeErr(b'illegal offset value')
        newText = self.__class__()
        newText.data = self.data[offset:]
        newText.ownerDocument = self.ownerDocument
        next = self.nextSibling
        if self.parentNode and self in self.parentNode.childNodes:
            if next is None:
                self.parentNode.appendChild(newText)
            else:
                self.parentNode.insertBefore(newText, next)
        self.data = self.data[:offset]
        return newText

    def writexml(self, writer, indent=b'', addindent=b'', newl=b''):
        _write_data(writer, b'%s%s%s' % (indent, self.data, newl))
        return

    def _get_wholeText(self):
        L = [
         self.data]
        n = self.previousSibling
        while n is not None:
            if n.nodeType in (Node.TEXT_NODE, Node.CDATA_SECTION_NODE):
                L.insert(0, n.data)
                n = n.previousSibling
            else:
                break

        n = self.nextSibling
        while n is not None:
            if n.nodeType in (Node.TEXT_NODE, Node.CDATA_SECTION_NODE):
                L.append(n.data)
                n = n.nextSibling
            else:
                break

        return (b'').join(L)

    def replaceWholeText(self, content):
        parent = self.parentNode
        n = self.previousSibling
        while n is not None:
            if n.nodeType in (Node.TEXT_NODE, Node.CDATA_SECTION_NODE):
                next = n.previousSibling
                parent.removeChild(n)
                n = next
            else:
                break

        n = self.nextSibling
        if not content:
            parent.removeChild(self)
        while n is not None:
            if n.nodeType in (Node.TEXT_NODE, Node.CDATA_SECTION_NODE):
                next = n.nextSibling
                parent.removeChild(n)
                n = next
            else:
                break

        if content:
            d = self.__dict__
            d[b'data'] = content
            d[b'nodeValue'] = content
            return self
        else:
            return
            return

    def _get_isWhitespaceInElementContent(self):
        if self.data.strip():
            return False
        else:
            elem = _get_containing_element(self)
            if elem is None:
                return False
            info = self.ownerDocument._get_elem_info(elem)
            if info is None:
                return False
            return info.isElementContent()
            return


defproperty(Text, b'isWhitespaceInElementContent', doc=b'True iff this text node contains only whitespace and is in element content.')
defproperty(Text, b'wholeText', doc=b'The text of all logically-adjacent text nodes.')

def _get_containing_element(node):
    c = node.parentNode
    while c is not None:
        if c.nodeType == Node.ELEMENT_NODE:
            return c
        c = c.parentNode

    return


def _get_containing_entref(node):
    c = node.parentNode
    while c is not None:
        if c.nodeType == Node.ENTITY_REFERENCE_NODE:
            return c
        c = c.parentNode

    return


class Comment(Childless, CharacterData):
    nodeType = Node.COMMENT_NODE
    nodeName = b'#comment'

    def __init__(self, data):
        self.data = self.nodeValue = data
        return

    def writexml(self, writer, indent=b'', addindent=b'', newl=b''):
        if b'--' in self.data:
            raise ValueError(b"'--' is not allowed in a comment node")
        writer.write(b'%s<!--%s-->%s' % (indent, self.data, newl))
        return


class CDATASection(Text):
    nodeType = Node.CDATA_SECTION_NODE
    nodeName = b'#cdata-section'

    def writexml(self, writer, indent=b'', addindent=b'', newl=b''):
        if self.data.find(b']]>') >= 0:
            raise ValueError(b"']]>' not allowed in a CDATA section")
        writer.write(b'<![CDATA[%s]]>' % self.data)
        return


class ReadOnlySequentialNamedNodeMap(object):
    __slots__ = (b'_seq',)

    def __init__(self, seq=()):
        self._seq = seq
        return

    def __len__(self):
        return len(self._seq)

    def _get_length(self):
        return len(self._seq)

    def getNamedItem(self, name):
        for n in self._seq:
            if n.nodeName == name:
                return n

        return

    def getNamedItemNS(self, namespaceURI, localName):
        for n in self._seq:
            if n.namespaceURI == namespaceURI and n.localName == localName:
                return n

        return

    def __getitem__(self, name_or_tuple):
        if isinstance(name_or_tuple, tuple):
            node = self.getNamedItemNS(*name_or_tuple)
        else:
            node = self.getNamedItem(name_or_tuple)
        if node is None:
            raise KeyError, name_or_tuple
        return node

    def item(self, index):
        if index < 0:
            return
        else:
            try:
                return self._seq[index]
            except IndexError:
                return

            return

    def removeNamedItem(self, name):
        raise xml.dom.NoModificationAllowedErr(b'NamedNodeMap instance is read-only')
        return

    def removeNamedItemNS(self, namespaceURI, localName):
        raise xml.dom.NoModificationAllowedErr(b'NamedNodeMap instance is read-only')
        return

    def setNamedItem(self, node):
        raise xml.dom.NoModificationAllowedErr(b'NamedNodeMap instance is read-only')
        return

    def setNamedItemNS(self, node):
        raise xml.dom.NoModificationAllowedErr(b'NamedNodeMap instance is read-only')
        return

    def __getstate__(self):
        return [self._seq]

    def __setstate__(self, state):
        self._seq = state[0]
        return


defproperty(ReadOnlySequentialNamedNodeMap, b'length', doc=b'Number of entries in the NamedNodeMap.')

class Identified():

    def _identified_mixin_init(self, publicId, systemId):
        self.publicId = publicId
        self.systemId = systemId
        return

    def _get_publicId(self):
        return self.publicId

    def _get_systemId(self):
        return self.systemId


class DocumentType(Identified, Childless, Node):
    nodeType = Node.DOCUMENT_TYPE_NODE
    nodeValue = None
    name = None
    publicId = None
    systemId = None
    internalSubset = None

    def __init__(self, qualifiedName):
        self.entities = ReadOnlySequentialNamedNodeMap()
        self.notations = ReadOnlySequentialNamedNodeMap()
        if qualifiedName:
            prefix, localname = _nssplit(qualifiedName)
            self.name = localname
        self.nodeName = self.name
        return

    def _get_internalSubset(self):
        return self.internalSubset

    def cloneNode(self, deep):
        if self.ownerDocument is None:
            clone = DocumentType(None)
            clone.name = self.name
            clone.nodeName = self.name
            operation = xml.dom.UserDataHandler.NODE_CLONED
            if deep:
                clone.entities._seq = []
                clone.notations._seq = []
                for n in self.notations._seq:
                    notation = Notation(n.nodeName, n.publicId, n.systemId)
                    clone.notations._seq.append(notation)
                    n._call_user_data_handler(operation, n, notation)

                for e in self.entities._seq:
                    entity = Entity(e.nodeName, e.publicId, e.systemId, e.notationName)
                    entity.actualEncoding = e.actualEncoding
                    entity.encoding = e.encoding
                    entity.version = e.version
                    clone.entities._seq.append(entity)
                    e._call_user_data_handler(operation, e, entity)

            self._call_user_data_handler(operation, self, clone)
            return clone
        else:
            return
            return

    def writexml(self, writer, indent=b'', addindent=b'', newl=b''):
        writer.write(b'<!DOCTYPE ')
        writer.write(self.name)
        if self.publicId:
            writer.write(b"%s  PUBLIC '%s'%s  '%s'" % (
             newl, self.publicId, newl, self.systemId))
        elif self.systemId:
            writer.write(b"%s  SYSTEM '%s'" % (newl, self.systemId))
        if self.internalSubset is not None:
            writer.write(b' [')
            writer.write(self.internalSubset)
            writer.write(b']')
        writer.write(b'>' + newl)
        return


class Entity(Identified, Node):
    attributes = None
    nodeType = Node.ENTITY_NODE
    nodeValue = None
    actualEncoding = None
    encoding = None
    version = None

    def __init__(self, name, publicId, systemId, notation):
        self.nodeName = name
        self.notationName = notation
        self.childNodes = NodeList()
        self._identified_mixin_init(publicId, systemId)
        return

    def _get_actualEncoding(self):
        return self.actualEncoding

    def _get_encoding(self):
        return self.encoding

    def _get_version(self):
        return self.version

    def appendChild(self, newChild):
        raise xml.dom.HierarchyRequestErr(b'cannot append children to an entity node')
        return

    def insertBefore(self, newChild, refChild):
        raise xml.dom.HierarchyRequestErr(b'cannot insert children below an entity node')
        return

    def removeChild(self, oldChild):
        raise xml.dom.HierarchyRequestErr(b'cannot remove children from an entity node')
        return

    def replaceChild(self, newChild, oldChild):
        raise xml.dom.HierarchyRequestErr(b'cannot replace children of an entity node')
        return


class Notation(Identified, Childless, Node):
    nodeType = Node.NOTATION_NODE
    nodeValue = None

    def __init__(self, name, publicId, systemId):
        self.nodeName = name
        self._identified_mixin_init(publicId, systemId)
        return


class DOMImplementation(DOMImplementationLS):
    _features = [
     11, 
     12, 
     14, 
     15, 
     16, 
     17, 
     18, 
     19]

    def hasFeature(self, feature, version):
        if version == b'':
            version = None
        return (
         feature.lower(), version) in self._features

    def createDocument(self, namespaceURI, qualifiedName, doctype):
        if doctype and doctype.parentNode is not None:
            raise xml.dom.WrongDocumentErr(b'doctype object owned by another DOM tree')
        doc = self._create_document()
        add_root_element = not (namespaceURI is None and qualifiedName is None and doctype is None)
        if not qualifiedName and add_root_element:
            raise xml.dom.InvalidCharacterErr(b'Element with no name')
        if add_root_element:
            prefix, localname = _nssplit(qualifiedName)
            if prefix == b'xml' and namespaceURI != b'http://www.w3.org/XML/1998/namespace':
                raise xml.dom.NamespaceErr(b"illegal use of 'xml' prefix")
            if prefix and not namespaceURI:
                raise xml.dom.NamespaceErr(b'illegal use of prefix without namespaces')
            element = doc.createElementNS(namespaceURI, qualifiedName)
            if doctype:
                doc.appendChild(doctype)
            doc.appendChild(element)
        if doctype:
            doctype.parentNode = doctype.ownerDocument = doc
        doc.doctype = doctype
        doc.implementation = self
        return doc

    def createDocumentType(self, qualifiedName, publicId, systemId):
        doctype = DocumentType(qualifiedName)
        doctype.publicId = publicId
        doctype.systemId = systemId
        return doctype

    def getInterface(self, feature):
        if self.hasFeature(feature, None):
            return self
        else:
            return
            return

    def _create_document(self):
        return Document()


class ElementInfo(object):
    __slots__ = (b'tagName',)

    def __init__(self, name):
        self.tagName = name
        return

    def getAttributeType(self, aname):
        return _no_type

    def getAttributeTypeNS(self, namespaceURI, localName):
        return _no_type

    def isElementContent(self):
        return False

    def isEmpty(self):
        return False

    def isId(self, aname):
        return False

    def isIdNS(self, namespaceURI, localName):
        return False

    def __getstate__(self):
        return self.tagName

    def __setstate__(self, state):
        self.tagName = state
        return


def _clear_id_cache(node):
    if node.nodeType == Node.DOCUMENT_NODE:
        node._id_cache.clear()
        node._id_search_stack = None
    elif _in_document(node):
        node.ownerDocument._id_cache.clear()
        node.ownerDocument._id_search_stack = None
    return


class Document(Node, DocumentLS):
    _child_node_types = (Node.ELEMENT_NODE, Node.PROCESSING_INSTRUCTION_NODE,
     Node.COMMENT_NODE, Node.DOCUMENT_TYPE_NODE)
    nodeType = Node.DOCUMENT_NODE
    nodeName = b'#document'
    nodeValue = None
    attributes = None
    doctype = None
    parentNode = None
    previousSibling = nextSibling = None
    implementation = DOMImplementation()
    actualEncoding = None
    encoding = None
    standalone = None
    version = None
    strictErrorChecking = False
    errorHandler = None
    documentURI = None
    _magic_id_count = 0

    def __init__(self):
        self.childNodes = NodeList()
        self._elem_info = {}
        self._id_cache = {}
        self._id_search_stack = None
        return

    def _get_elem_info(self, element):
        if element.namespaceURI:
            key = (
             element.namespaceURI, element.localName)
        else:
            key = element.tagName
        return self._elem_info.get(key)

    def _get_actualEncoding(self):
        return self.actualEncoding

    def _get_doctype(self):
        return self.doctype

    def _get_documentURI(self):
        return self.documentURI

    def _get_encoding(self):
        return self.encoding

    def _get_errorHandler(self):
        return self.errorHandler

    def _get_standalone(self):
        return self.standalone

    def _get_strictErrorChecking(self):
        return self.strictErrorChecking

    def _get_version(self):
        return self.version

    def appendChild(self, node):
        if node.nodeType not in self._child_node_types:
            raise xml.dom.HierarchyRequestErr(b'%s cannot be child of %s' % (repr(node), repr(self)))
        if node.parentNode is not None:
            node.parentNode.removeChild(node)
        if node.nodeType == Node.ELEMENT_NODE and self._get_documentElement():
            raise xml.dom.HierarchyRequestErr(b'two document elements disallowed')
        return Node.appendChild(self, node)

    def removeChild(self, oldChild):
        try:
            self.childNodes.remove(oldChild)
        except ValueError:
            raise xml.dom.NotFoundErr()

        oldChild.nextSibling = oldChild.previousSibling = None
        oldChild.parentNode = None
        if self.documentElement is oldChild:
            self.documentElement = None
        return oldChild

    def _get_documentElement(self):
        for node in self.childNodes:
            if node.nodeType == Node.ELEMENT_NODE:
                return node

        return

    def unlink(self):
        if self.doctype is not None:
            self.doctype.unlink()
            self.doctype = None
        Node.unlink(self)
        return

    def cloneNode(self, deep):
        if not deep:
            return
        else:
            clone = self.implementation.createDocument(None, None, None)
            clone.encoding = self.encoding
            clone.standalone = self.standalone
            clone.version = self.version
            for n in self.childNodes:
                childclone = _clone_node(n, deep, clone)
                clone.childNodes.append(childclone)
                if childclone.nodeType == Node.DOCUMENT_NODE:
                    pass
                elif childclone.nodeType == Node.DOCUMENT_TYPE_NODE:
                    clone.doctype = childclone
                childclone.parentNode = clone

            self._call_user_data_handler(xml.dom.UserDataHandler.NODE_CLONED, self, clone)
            return clone

    def createDocumentFragment(self):
        d = DocumentFragment()
        d.ownerDocument = self
        return d

    def createElement(self, tagName):
        e = Element(tagName)
        e.ownerDocument = self
        return e

    def createTextNode(self, data):
        if not isinstance(data, StringTypes):
            raise TypeError, b'node contents must be a string'
        t = Text()
        t.data = data
        t.ownerDocument = self
        return t

    def createCDATASection(self, data):
        if not isinstance(data, StringTypes):
            raise TypeError, b'node contents must be a string'
        c = CDATASection()
        c.data = data
        c.ownerDocument = self
        return c

    def createComment(self, data):
        c = Comment(data)
        c.ownerDocument = self
        return c

    def createProcessingInstruction(self, target, data):
        p = ProcessingInstruction(target, data)
        p.ownerDocument = self
        return p

    def createAttribute(self, qName):
        a = Attr(qName)
        a.ownerDocument = self
        a.value = b''
        return a

    def createElementNS(self, namespaceURI, qualifiedName):
        prefix, localName = _nssplit(qualifiedName)
        e = Element(qualifiedName, namespaceURI, prefix)
        e.ownerDocument = self
        return e

    def createAttributeNS(self, namespaceURI, qualifiedName):
        prefix, localName = _nssplit(qualifiedName)
        a = Attr(qualifiedName, namespaceURI, localName, prefix)
        a.ownerDocument = self
        a.value = b''
        return a

    def _create_entity(self, name, publicId, systemId, notationName):
        e = Entity(name, publicId, systemId, notationName)
        e.ownerDocument = self
        return e

    def _create_notation(self, name, publicId, systemId):
        n = Notation(name, publicId, systemId)
        n.ownerDocument = self
        return n

    def getElementById(self, id):
        if id in self._id_cache:
            return self._id_cache[id]
        else:
            if not (self._elem_info or self._magic_id_count):
                return
            stack = self._id_search_stack
            if stack is None:
                stack = [self.documentElement]
                self._id_search_stack = stack
            elif not stack:
                return
            result = None
            while stack:
                node = stack.pop()
                stack.extend([child for child in node.childNodes if child.nodeType in _nodeTypes_with_children])
                info = self._get_elem_info(node)
                if info:
                    for attr in node.attributes.values():
                        if attr.namespaceURI:
                            if info.isIdNS(attr.namespaceURI, attr.localName):
                                self._id_cache[attr.value] = node
                                if attr.value == id:
                                    result = node
                                elif not node._magic_id_nodes:
                                    break
                        elif info.isId(attr.name):
                            self._id_cache[attr.value] = node
                            if attr.value == id:
                                result = node
                            elif not node._magic_id_nodes:
                                break
                        elif attr._is_id:
                            self._id_cache[attr.value] = node
                            if attr.value == id:
                                result = node
                            elif node._magic_id_nodes == 1:
                                break

                elif node._magic_id_nodes:
                    for attr in node.attributes.values():
                        if attr._is_id:
                            self._id_cache[attr.value] = node
                            if attr.value == id:
                                result = node

                if result is not None:
                    break

            return result

    def getElementsByTagName(self, name):
        return _get_elements_by_tagName_helper(self, name, NodeList())

    def getElementsByTagNameNS(self, namespaceURI, localName):
        return _get_elements_by_tagName_ns_helper(self, namespaceURI, localName, NodeList())

    def isSupported(self, feature, version):
        return self.implementation.hasFeature(feature, version)

    def importNode(self, node, deep):
        if node.nodeType == Node.DOCUMENT_NODE:
            raise xml.dom.NotSupportedErr(b'cannot import document nodes')
        elif node.nodeType == Node.DOCUMENT_TYPE_NODE:
            raise xml.dom.NotSupportedErr(b'cannot import document type nodes')
        return _clone_node(node, deep, self)

    def writexml(self, writer, indent=b'', addindent=b'', newl=b'', encoding=None):
        if encoding is None:
            writer.write(b'<?xml version="1.0" ?>' + newl)
        else:
            writer.write(b'<?xml version="1.0" encoding="%s"?>%s' % (encoding, newl))
        for node in self.childNodes:
            node.writexml(writer, indent, addindent, newl)

        return

    def renameNode(self, n, namespaceURI, name):
        if n.ownerDocument is not self:
            raise xml.dom.WrongDocumentErr(b'cannot rename nodes from other documents;\nexpected %s,\nfound %s' % (
             self, n.ownerDocument))
        if n.nodeType not in (Node.ELEMENT_NODE, Node.ATTRIBUTE_NODE):
            raise xml.dom.NotSupportedErr(b'renameNode() only applies to element and attribute nodes')
        if namespaceURI != EMPTY_NAMESPACE:
            if b':' in name:
                prefix, localName = name.split(b':', 1)
                if prefix == b'xmlns' and namespaceURI != xml.dom.XMLNS_NAMESPACE:
                    raise xml.dom.NamespaceErr(b"illegal use of 'xmlns' prefix")
            elif name == b'xmlns' and namespaceURI != xml.dom.XMLNS_NAMESPACE and n.nodeType == Node.ATTRIBUTE_NODE:
                raise xml.dom.NamespaceErr(b"illegal use of the 'xmlns' attribute")
            prefix = None
            localName = name
        else:
            prefix = None
            localName = None
        if n.nodeType == Node.ATTRIBUTE_NODE:
            element = n.ownerElement
            if element is not None:
                is_id = n._is_id
                element.removeAttributeNode(n)
        else:
            element = None
        d = n.__dict__
        d[b'prefix'] = prefix
        d[b'localName'] = localName
        d[b'namespaceURI'] = namespaceURI
        d[b'nodeName'] = name
        if n.nodeType == Node.ELEMENT_NODE:
            d[b'tagName'] = name
        else:
            d[b'name'] = name
            if element is not None:
                element.setAttributeNode(n)
                if is_id:
                    element.setIdAttributeNode(n)
        return n


defproperty(Document, b'documentElement', doc=b'Top-level element of this document.')

def _clone_node(node, deep, newOwnerDocument):
    if node.ownerDocument.isSameNode(newOwnerDocument):
        operation = xml.dom.UserDataHandler.NODE_CLONED
    else:
        operation = xml.dom.UserDataHandler.NODE_IMPORTED
    if node.nodeType == Node.ELEMENT_NODE:
        clone = newOwnerDocument.createElementNS(node.namespaceURI, node.nodeName)
        for attr in node.attributes.values():
            clone.setAttributeNS(attr.namespaceURI, attr.nodeName, attr.value)
            a = clone.getAttributeNodeNS(attr.namespaceURI, attr.localName)
            a.specified = attr.specified

        if deep:
            for child in node.childNodes:
                c = _clone_node(child, deep, newOwnerDocument)
                clone.appendChild(c)

    elif node.nodeType == Node.DOCUMENT_FRAGMENT_NODE:
        clone = newOwnerDocument.createDocumentFragment()
        if deep:
            for child in node.childNodes:
                c = _clone_node(child, deep, newOwnerDocument)
                clone.appendChild(c)

    elif node.nodeType == Node.TEXT_NODE:
        clone = newOwnerDocument.createTextNode(node.data)
    elif node.nodeType == Node.CDATA_SECTION_NODE:
        clone = newOwnerDocument.createCDATASection(node.data)
    elif node.nodeType == Node.PROCESSING_INSTRUCTION_NODE:
        clone = newOwnerDocument.createProcessingInstruction(node.target, node.data)
    elif node.nodeType == Node.COMMENT_NODE:
        clone = newOwnerDocument.createComment(node.data)
    elif node.nodeType == Node.ATTRIBUTE_NODE:
        clone = newOwnerDocument.createAttributeNS(node.namespaceURI, node.nodeName)
        clone.specified = True
        clone.value = node.value
    elif node.nodeType == Node.DOCUMENT_TYPE_NODE:
        operation = xml.dom.UserDataHandler.NODE_IMPORTED
        clone = newOwnerDocument.implementation.createDocumentType(node.name, node.publicId, node.systemId)
        clone.ownerDocument = newOwnerDocument
        if deep:
            clone.entities._seq = []
            clone.notations._seq = []
            for n in node.notations._seq:
                notation = Notation(n.nodeName, n.publicId, n.systemId)
                notation.ownerDocument = newOwnerDocument
                clone.notations._seq.append(notation)
                if hasattr(n, b'_call_user_data_handler'):
                    n._call_user_data_handler(operation, n, notation)

            for e in node.entities._seq:
                entity = Entity(e.nodeName, e.publicId, e.systemId, e.notationName)
                entity.actualEncoding = e.actualEncoding
                entity.encoding = e.encoding
                entity.version = e.version
                entity.ownerDocument = newOwnerDocument
                clone.entities._seq.append(entity)
                if hasattr(e, b'_call_user_data_handler'):
                    e._call_user_data_handler(operation, e, entity)

    else:
        raise xml.dom.NotSupportedErr(b'Cannot clone node %s' % repr(node))
    if hasattr(node, b'_call_user_data_handler'):
        node._call_user_data_handler(operation, node, clone)
    return clone


def _nssplit(qualifiedName):
    fields = qualifiedName.split(b':', 1)
    if len(fields) == 2:
        return fields
    else:
        return (
         None, fields[0])
        return


def _get_StringIO():
    from StringIO import StringIO
    return StringIO()


def _do_pulldom_parse(func, args, kwargs):
    events = func(*args, **kwargs)
    toktype, rootNode = events.getEvent()
    events.expandNode(rootNode)
    events.clear()
    return rootNode


def parse(file, parser=None, bufsize=None):
    if parser is None and not bufsize:
        from xml.dom import expatbuilder
        return expatbuilder.parse(file)
    else:
        from xml.dom import pulldom
        return _do_pulldom_parse(pulldom.parse, (file,), {b'parser': parser, b'bufsize': bufsize})
        return


def parseString(string, parser=None):
    if parser is None:
        from xml.dom import expatbuilder
        return expatbuilder.parseString(string)
    else:
        from xml.dom import pulldom
        return _do_pulldom_parse(pulldom.parseString, (string,), {b'parser': parser})
        return


def getDOMImplementation(features=None):
    if features:
        if isinstance(features, StringTypes):
            features = domreg._parse_feature_string(features)
        for f, v in features:
            if not Document.implementation.hasFeature(f, v):
                return None

    return Document.implementation
