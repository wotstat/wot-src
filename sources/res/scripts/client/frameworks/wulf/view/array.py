import typing
from contextlib import contextmanager
from ..py_object_wrappers import PyObjectArray
if typing.TYPE_CHECKING:
    from typing import Iterable, Union
    from .. import ViewModel, Map
T = typing.TypeVar(b'T')

class Array(typing.Iterable[T]):
    slots = (b'proxy', b'__weakref__')

    def __init__(self):
        self.proxy = PyObjectArray()
        self.proxy.bindPyObject(self)
        super(Array, self).__init__()
        return

    def __repr__(self):
        return (b'Array(size={})').format(self.proxy.getSize() if self.proxy is not None else 0)

    def __str__(self):
        return self.proxy.toString()

    def __len__(self):
        return self.proxy.getSize()

    def __getitem__(self, index):
        if isinstance(index, slice):
            return (self.proxy.getValue(i) for i in xrange(index.start or 0, index.stop or len(self), index.step or 1))
        if index < 0:
            if abs(index) > self.proxy.getSize():
                raise IndexError((b'Array index %d out of range').format(index))
            index = len(self) + index
        return self.proxy.getValue(index)

    def __iter__(self):
        for index in xrange(0, self.proxy.getSize()):
            yield self.proxy.getValue(index)

        return

    def __reversed__(self):
        for index in xrange(self.proxy.getSize() - 1, -1, -1):
            yield self.proxy.getValue(index)

        return

    def reserve(self, capacity):
        self.proxy.reserve(capacity)
        return

    def clear(self):
        self.proxy.clear()
        return

    def getValue(self, index):
        return self.proxy.getValue(index)

    def addNumber(self, value):
        self.proxy.addNumber(value)
        return

    def addReal(self, value):
        self.proxy.addReal(value)
        return

    def addBool(self, value):
        self.proxy.addBool(value)
        return

    def addString(self, value):
        self.proxy.addString(value)
        return

    def addViewModel(self, value):
        self.proxy.addViewModel(value.proxy)
        return

    def addResource(self, value):
        self.proxy.addResource(value)
        return

    def addArray(self, value):
        self.proxy.addArray(value.proxy)
        return

    def addMap(self, value):
        self.proxy.addMap(value.proxy)
        return

    def setNumber(self, index, value):
        self.proxy.setNumber(index, value)
        return

    def setReal(self, index, value):
        self.proxy.setReal(index, value)
        return

    def setBool(self, index, value):
        self.proxy.setBool(index, value)
        return

    def setString(self, index, value):
        self.proxy.setString(index, value)
        return

    def setViewModel(self, index, value):
        self.proxy.setViewModel(index, value.proxy)
        return

    def setResource(self, index, value):
        self.proxy.setResource(index, value)
        return

    def setArray(self, index, value):
        self.proxy.setArray(index, value.proxy)
        return

    def setMap(self, index, value):
        self.proxy.setMap(index, value.proxy)
        return

    def remove(self, index):
        self.proxy.removeValue(index)
        return

    def removeValues(self, indexes):
        self.proxy.removeValues(indexes)
        return

    def invalidate(self):
        self.proxy.invalidate()
        return

    @contextmanager
    def transaction(self):
        yield self
        self.invalidate()
        return


def fillIntsArray(numbers, array):
    array.clear()
    for n in numbers:
        array.addNumber(n)

    array.invalidate()
    return


def fillFloatsArray(floats, array):
    array.clear()
    for f in floats:
        array.addReal(f)

    array.invalidate()
    return


def fillBoolsArray(bools, array):
    array.clear()
    for b in bools:
        array.addBool(b)

    array.invalidate()
    return


def fillStringsArray(strings, array):
    array.clear()
    for s in strings:
        array.addString(s)

    array.invalidate()
    return


def fillViewModelsArray(viewModels, array):
    array.clear()
    for vm in viewModels:
        array.addViewModel(vm)

    array.invalidate()
    return


def fillResourcesArray(resources, array):
    array.clear()
    for r in resources:
        array.addResource(r)

    array.invalidate()
    return


def fillArraysArray(arrays, array):
    array.clear()
    for a in arrays:
        array.addArray(a)

    array.invalidate()
    return
