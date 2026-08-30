__all__ = [
 b'NodeList', b'EmptyNodeList', b'StringTypes', b'defproperty']
import xml.dom
try:
    unicode
except NameError:
    StringTypes = (
     type(b''),)
else:
    StringTypes = (
     type(b''), type(unicode(b'')))

class NodeList(list):
    __slots__ = ()

    def item(self, index):
        if 0 <= index < len(self):
            return self[index]
        return

    def _get_length(self):
        return len(self)

    def _set_length(self, value):
        raise xml.dom.NoModificationAllowedErr(b"attempt to modify read-only attribute 'length'")
        return

    length = property(_get_length, _set_length, doc=b'The number of nodes in the NodeList.')

    def __setstate__(self, state):
        if state is None:
            state = []
        self[:] = state
        return


class EmptyNodeList(tuple):
    __slots__ = ()

    def __add__(self, other):
        NL = NodeList()
        NL.extend(other)
        return NL

    def __radd__(self, other):
        NL = NodeList()
        NL.extend(other)
        return NL

    def item(self, index):
        return

    def _get_length(self):
        return 0

    def _set_length(self, value):
        raise xml.dom.NoModificationAllowedErr(b"attempt to modify read-only attribute 'length'")
        return

    length = property(_get_length, _set_length, doc=b'The number of nodes in the NodeList.')


def defproperty(klass, name, doc):
    get = getattr(klass, b'_get_' + name).im_func

    def set(self, value, name=name):
        raise xml.dom.NoModificationAllowedErr(b'attempt to modify read-only attribute ' + repr(name))
        return

    prop = property(get, set, doc=doc)
    setattr(klass, name, prop)
    return
