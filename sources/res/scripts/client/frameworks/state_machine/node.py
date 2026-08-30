import weakref
from .exceptions import NodeError

class Node(object):
    __counter = 0
    __slots__ = (b'__weakref__', b'__id', b'__parent', b'__children')

    def __init__(self):
        super(Node, self).__init__()
        self.__id = self.__genID()
        self.__parent = lambda : None
        self.__children = []
        return

    def __repr__(self):
        return (b'{}(id={})').format(self.__class__.__name__, self.__id)

    def clear(self):
        self.__parent = lambda : None
        while self.__children:
            children = self.__children.pop()
            children.clear()

        return

    def getNodeID(self):
        return self.__id

    def getParent(self):
        return self.__parent()

    def getChildren(self, filter_=None):
        return filter(filter_, self.__children)

    def getChildByIndex(self, index):
        if 0 <= index < len(self.__children):
            return self.__children[index]
        else:
            return

    def addChild(self, child):
        self._addChild(child)
        return

    def removeChild(self, child):
        self._removeChild(child)
        return

    def visitInOrder(self, filter_=None):
        yield self
        for child in self.getChildren(filter_=filter_):
            for item in child.visitInOrder(filter_=filter_):
                yield item

        return

    def _addChild(self, child):
        if child is None:
            raise NodeError(b'Child is not defined')
        if not isinstance(child, Node):
            raise NodeError(b'Child must extend Node class')
        if child.getParent() is not None:
            raise NodeError(b'Parent is already added')
        child.__parent = weakref.ref(self)
        if child not in self.__children:
            self.__children.append(child)
        return

    def _removeChild(self, child):
        if child is None:
            raise NodeError(b'Child is not defined')
        if not isinstance(child, Node):
            raise NodeError(b'Child must extend Node class')
        if child in self.__children:
            self.__children.remove(child)
            child.clear()
        return

    @classmethod
    def __genID(cls):
        cls.__counter += 1
        return cls.__counter
