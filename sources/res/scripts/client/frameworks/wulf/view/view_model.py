import logging
from contextlib import contextmanager
import typing as t
from soft_exception import SoftException
from .command import Command
from .array import Array
from .map import Map
from ..py_object_binder import PyObjectEntity
from ..py_object_wrappers import PyObjectViewModel
if t.TYPE_CHECKING:
    from types import TracebackType
T = t.TypeVar(b'T', bound=b'ViewModel')
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())

class ViewModel(object):
    __slots__ = (b'proxy', b'__weakref__')

    def __init__(self, properties=0, commands=0):
        self.proxy = PyObjectViewModel(properties, commands)
        self.proxy.bindPyObject(self)
        self._initialize()
        super(ViewModel, self).__init__()
        return

    def __repr__(self):
        return (b'{}(fields={})').format(self.__class__.__name__, self.proxy.toString() if self.proxy is not None else None)

    def __str__(self):
        return self.proxy.toString()

    def __enter__(self):
        self.proxy.hold()
        return self

    def __exit__(self, excType, _, traceback):
        if excType is None:
            self.proxy.commit()
        else:
            self.proxy.rollback()
        return False

    def hold(self):
        self.proxy.hold()
        return

    def commit(self):
        self.proxy.commit()
        return

    def rollback(self):
        self.proxy.rollback()
        return

    @contextmanager
    def transaction(self):
        self.hold()
        try:
            yield self
            self.commit()
        except Exception:
            self.rollback()
            raise

        return

    def _getValue(self, index, propertyType):
        _logger.warning(b'Method "_getValue" can be used for debug only.')
        return self.proxy.getValue(index, propertyType)

    def _getNumber(self, index):
        return self.proxy.getNumber(index)

    def _getReal(self, index):
        return self.proxy.getReal(index)

    def _getBool(self, index):
        return self.proxy.getBool(index)

    def _getString(self, index):
        return self.proxy.getString(index)

    def _getViewModel(self, index):
        return self.proxy.getViewModel(index)

    def _getView(self, index):
        return self.proxy.getView(index)

    def _getArray(self, index):
        return self.proxy.getArray(index)

    def _getMap(self, index):
        return self.proxy.getMap(index)

    def _getResource(self, index):
        return self.proxy.getResource(index)

    def _setValue(self, index, propertyType, value):
        _logger.warning(b'Method "_setValue" can be used for debug only.')
        self.proxy.setValue(index, propertyType, value)
        return

    def _setNumber(self, index, value):
        self.proxy.setNumber(index, int(value))
        return

    def _setReal(self, index, value):
        self.proxy.setReal(index, value)
        return

    def _setBool(self, index, value):
        self.proxy.setBool(index, value)
        return

    def _setString(self, index, value):
        self.proxy.setString(index, value)
        return

    def _setViewModel(self, index, value):
        self.proxy.setViewModel(index, value.proxy)
        return

    def _setView(self, index, pyValue):
        raise SoftException(b'Property with type ValueType.VIEW is not longer supported. Use View.setChildView method to add sub views.')
        return

    def _setArray(self, index, value):
        self.proxy.setArray(index, value.proxy)
        return

    def _setMap(self, index, value):
        self.proxy.setMap(index, value.proxy)
        return

    def _setResource(self, index, value):
        return self.proxy.setResource(index, value)

    def _addProperty(self, name, propertyType, defaultValue):
        self.proxy.addField(name, propertyType, defaultValue)
        return

    def _addPropertyAsPyObjectEntity(self, name, propertyType, pyValue=None):
        if pyValue is not None:
            proxy = pyValue.proxy
        else:
            proxy = None
        self.proxy.addField(name, propertyType, proxy)
        return

    def _addNumberProperty(self, name, defaultValue=0):
        self.proxy.addNumberField(name, defaultValue)
        return

    def _addRealProperty(self, name, defaultValue=0.0):
        self.proxy.addRealField(name, defaultValue)
        return

    def _addBoolProperty(self, name, defaultValue=False):
        self.proxy.addBoolField(name, defaultValue)
        return

    def _addStringProperty(self, name, defaultValue=b''):
        self.proxy.addStringField(name, defaultValue)
        return

    def _addViewModelProperty(self, name, defaultValue):
        self.proxy.addViewModelField(name, defaultValue.proxy)
        return

    def _addViewProperty(self, name, defaultValue=None):
        raise SoftException(b'Property with type ValueType.VIEW is not longer supported. Use View.setChildView method to add sub views.')
        return

    def _addArrayProperty(self, name, defaultValue=None):
        if defaultValue is None:
            defaultValue = Array()
        self.proxy.addArrayField(name, defaultValue.proxy)
        return

    def _addMapProperty(self, name, value):
        self.proxy.addMapField(name, value.proxy)
        return

    def _addResourceProperty(self, name, defaultValue):
        self.proxy.addResourceField(name, defaultValue)
        return

    def _addCommand(self, name):
        cmd = Command()
        self.proxy.addCommand(name, cmd.proxy)
        return cmd

    def _initialize(self):
        return
