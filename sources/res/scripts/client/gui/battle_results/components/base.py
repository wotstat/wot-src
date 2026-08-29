import copy, typing
from collections import defaultdict, namedtuple
import inspect, operator
from soft_exception import SoftException
from debug_utils import LOG_WARNING
from gui.shared.utils.decorators import ReprInjector

class StatsComponent(object):
    __slots__ = ()

    def clone(self, *exclude):
        raise NotImplementedError
        return

    def clear(self):
        return

    def addComponent(self, index, component):
        raise NotImplementedError
        return

    def getComponent(self, index):
        raise NotImplementedError
        return

    def getRecordPath(self):
        raise NotImplementedError
        return

    def setRecord(self, record, reusable):
        raise NotImplementedError
        return

    def getField(self):
        raise NotImplementedError
        return

    def getVO(self):
        raise NotImplementedError
        return

    def getMeta(self):
        raise NotImplementedError
        return


class StatsComponentError(SoftException):
    pass


@ReprInjector.simple((b'_field', b'field'))
class StatsItem(StatsComponent):
    __slots__ = (b'_field', b'_value', b'_path')

    def __init__(self, field, *path):
        super(StatsItem, self).__init__()
        self._field = field
        self._path = path
        self._value = None
        return

    def clone(self):
        return self.__class__(self._field, *self._path)

    def addComponent(self, index, component):
        raise SoftException(b'StatsItem is not supported method addComponent')
        return

    def getComponent(self, index):
        raise SoftException(b'StatsItem is not supported method getComponent')
        return

    def getRecordPath(self):
        return self._path

    def setRecord(self, record, reusable):
        if record is not None:
            self._value = self._convert(record, reusable)
        else:
            self._value = None
        return

    def getField(self):
        return self._field

    def getVO(self):
        return self._value

    def getMeta(self):
        return self._meta

    def _convert(self, value, reusable):
        return value


class DirectStatsItem(StatsItem):
    __slots__ = (b'_value',)

    def __init__(self, field, value=None):
        super(DirectStatsItem, self).__init__(field)
        self._value = value
        return

    def clone(self):
        return self.__class__(self._field, value=self._value)

    def setRecord(self, record, reusable):
        self._value = record
        return


class VOMeta(object):
    __slots__ = (b'_meta',)

    def __init__(self, meta):
        super(VOMeta, self).__init__()
        self._meta = meta
        return

    def clone(self):
        return self.__class__(self._meta)

    def bind(self, clazz):
        setattr(clazz, b'__vo_meta__', self.clone())
        return

    def addMeta(self, meta):
        return

    def getDefault(self, field):
        return

    def isComponentGenerated(self, index):
        return False

    def registerComponent(self, component):
        return

    def generateComponents(self):
        return ()

    def generateVO(self, components):
        raise NotImplementedError
        return


class DictMeta(VOMeta):
    __slots__ = (b'_auto', b'_unregistered')

    def __init__(self, meta=None, auto=None):
        if meta is None:
            meta = {}
        super(DictMeta, self).__init__(meta)
        self._auto = auto or ()
        self._unregistered = set(meta.keys())
        return

    def clone(self):
        auto = []
        for index, component in self._auto:
            auto.append((index, component.clone()))

        return DictMeta(self._meta, auto)

    def getDefault(self, field):
        return self._meta.get(field)

    def isComponentGenerated(self, index):
        return index in map(operator.itemgetter(0), self._auto)

    def registerComponent(self, component):
        field = component.getField()
        if field:
            if field not in self._meta:
                raise StatsComponentError((b'Field {} is not found in meta {}').format(field, self._meta))
            if field not in self._unregistered:
                raise StatsComponentError((b'Component is already set to field {}').format(field))
            self._unregistered.discard(field)
        return

    def generateComponents(self):
        for idx, component in self._auto:
            yield (
             idx, component)

        return

    def generateVO(self, components):
        vo = {}
        for field in self._unregistered:
            vo[field] = self.getDefault(field)

        for component in components:
            if component is None:
                continue
            field = component.getField()
            value = component.getVO()
            if field:
                if value is not None:
                    vo[field] = value
                else:
                    vo[field] = self._meta[field]
            elif value is not None:
                vo.update(value)

        return vo

    def addMeta(self, meta):
        self._meta.update(meta)
        return


class ListMeta(VOMeta):
    __slots__ = (b'_registered', b'_runtime')

    def __init__(self, meta=None, registered=False, runtime=True):
        super(ListMeta, self).__init__(meta or [])
        self._registered = registered
        self._runtime = runtime
        return

    def getDefault(self, field):
        return

    def copy(self):
        return self.__class__(copy.deepcopy(self._meta), self._registered, self._runtime)

    def isComponentGenerated(self, index):
        return not self._runtime

    def registerComponent(self, component):
        self._registered = True
        return

    def generateVO(self, components):
        if not self._registered:
            return self._meta[:]
        vo = []
        for component in components:
            vo.append(component.getVO())

        return vo

    def addMeta(self, meta):
        if meta not in self._meta:
            self._meta.append(meta)
        return

    def popMeta(self, meta):
        self._meta = [item for item in self._meta if item != meta]
        return


def _getPropertyGetter(idx):

    def _getter(self):
        component = self.getComponent(idx)
        if component is not None:
            return component.getVO()
        else:
            return

    return _getter


def _getPropertySetter(idx):

    def _setter(self, value):
        component = self.getComponent(idx)
        if component is not None:
            if isinstance(value, PropertyValue):
                component.setRecord(value.record, value.reusable)
            elif isinstance(value, tuple) and len(value) == 2 and isinstance(value[0], tuple):
                component.setRecord(value[0], value[1])
            else:
                component.setRecord(value, None)
        return

    return _setter


PropertyValue = namedtuple(b'PropertyValue', b'record reusable')

class PropertyMeta(DictMeta):
    __slots__ = (b'_bind',)

    def __init__(self, meta):
        if not isinstance(meta, tuple):
            raise StatsComponentError(b'Meta must be tuple')
        converted = {}
        self._bind = []
        for idx, item in enumerate(meta):
            if not isinstance(item, tuple):
                raise StatsComponentError(b'Each item must be tuple in meta')
            length = len(item)
            if length > 1:
                field, default = item[:2]
                converted[field] = default
                if length > 2:
                    self._bind.append((idx, field, item[2], default))
            else:
                raise StatsComponentError(b'Number of items must be more than 1')

        super(PropertyMeta, self).__init__(converted)
        return

    def replace(self, *replace):
        bind = self._bind[:]
        for item in replace:
            if not isinstance(item, tuple):
                raise StatsComponentError(b'Each item must be tuple in meta')
            if len(item) != 3:
                raise StatsComponentError(b'Number of items must be 3!')
            searchField, default, attribute = item[:3]
            for idx, field, _, _ in self._bind:
                if field == searchField:
                    bind[idx] = (
                     idx, field, attribute, default)
                    break
            else:
                raise StatsComponentError((b'Item {} to replace is not found').format(searchField))

        destination = PropertyMeta(())
        destination._bind = bind
        destination._meta = self._meta.copy()
        destination._unregistered = self._unregistered.copy()
        return destination

    def clone(self):
        auto = []
        for index, component in self.generateComponents():
            auto.append((index, component))

        return DictMeta(self._meta, auto)

    def bind(self, clazz):
        super(PropertyMeta, self).bind(clazz)
        slots = set()
        for parent in inspect.getmro(clazz):
            slots = slots.union(getattr(parent, b'__slots__', ()))

        if not slots:
            raise StatsComponentError((b'__slots__ must be defined in stats component {}').format(clazz))
        for idx, _, attribute, _ in self._bind:
            if attribute not in slots:
                raise StatsComponentError((b'Attribute {} is not found in __slots__ for {}').format(attribute, clazz))
            setattr(clazz, attribute, property(_getPropertyGetter(idx), _getPropertySetter(idx)))

        return

    def generateComponents(self):
        for idx, field, _, default in self._bind:
            if isinstance(default, StatsComponent):
                yield (
                 idx, default.clone())
            else:
                yield (
                 idx, DirectStatsItem(field, default))

        return


@ReprInjector.simple((b'_field', b'field'), (b'_path', b'path'))
class StatsBlock(StatsComponent):
    __slots__ = (b'_meta', b'_components', b'_field', b'_path', b'_records')
    __vo_meta__ = None

    def __init__(self, meta=None, field=b'', *path):
        super(StatsBlock, self).__init__()
        if meta is None and self.__vo_meta__ is not None:
            meta = self.__vo_meta__
        if isinstance(meta, VOMeta):
            self._meta = meta.clone()
        else:
            raise StatsComponentError((b'Type of meta must be VOMeta. Received type is {}').format(type(meta)))
        self._components = []
        self._field = field
        self._path = path
        self._records = defaultdict(list)
        for index, component in self._meta.generateComponents():
            self.addComponent(index, component)

        return

    def clone(self, *exclude):
        block = self.__class__(self._meta.clone(), self._field, *self._path)
        for index, component in enumerate(self._components):
            if index in exclude or self._meta.isComponentGenerated(index):
                continue
            if component is not None:
                block.addComponent(index, component.clone())

        return block

    def addComponent(self, index, component):
        if index < 0:
            raise StatsComponentError((b'Index must be positive. Received index is {}').format(index))
        while index > len(self._components) - 1:
            self._components.append(None)

        if self._components[index] is not None:
            raise StatsComponentError((b'Component is already set to position {}').format(index))
        self._meta.registerComponent(component)
        self._records[component.getRecordPath()].append(index)
        self._components[index] = component
        return

    def getComponent(self, index):
        if -1 < index < len(self._components):
            return self._components[index]
        else:
            return

    def addNextComponent(self, component):
        self.addComponent(self.getNextComponentIndex(), component)
        return

    def getNextComponentIndex(self):
        return len(self._components)

    def getRecordPath(self):
        return self._path

    def setRecord(self, result, reusable):
        bypass = sorted(self._records.iteritems(), key=(lambda item: len(item[0])))
        for path, idxs in bypass:
            record = result
            for sub in path:
                if sub in record:
                    record = record[sub]
                else:
                    LOG_WARNING(b'Path of record is not found', path)
                    record = None

            for idx in idxs:
                component = self._components[idx]
                if component is not None:
                    component.setRecord(record, reusable)

        return

    def getField(self):
        return self._field

    def getMeta(self):
        return self._meta

    def getVO(self):
        return self._meta.generateVO(self._components)
