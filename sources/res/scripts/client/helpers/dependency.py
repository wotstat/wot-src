import functools, inspect, logging, typing
from ids_generators import SequenceIDGenerator
from py2to3.backport.inspect import getargspec
from soft_exception import SoftException
InterfaceType = typing.TypeVar(b'InterfaceType')
_logger = logging.getLogger(__name__)
_logger.addHandler(logging.NullHandler())
_g_manager = None
_MAX_ORDER_NUMBER = 32767
_orderGen = SequenceIDGenerator(lowBound=0, highBound=_MAX_ORDER_NUMBER)

def configure(config):
    global _g_manager
    if _g_manager is not None:
        raise DependencyError(b'Manager of dependencies is already created and configured')
    _g_manager = DependencyManager()
    _g_manager.addConfig(config)
    return _g_manager


def isConfigured():
    return _g_manager is not None


def replaceInstance(class_, obj, finalizer=None):
    _g_manager.replaceInstance(class_, obj, finalizer)
    return


def clear():
    global _g_manager
    if _g_manager is not None:
        _g_manager.clear()
        _g_manager = None
    _orderGen.clear()
    return


def instance(class_):
    if _g_manager is None:
        raise DependencyError(b'Manager of dependencies is not created and configured')
    return _g_manager.getService(class_)


def descriptor(class_):
    return _ServiceDescriptor(class_)


class replace_none_kwargs(object):

    def __init__(self, **services):
        super(replace_none_kwargs, self).__init__()
        self.__services = {}
        for name, class_ in services.iteritems():
            if not inspect.isclass(class_):
                raise DependencyError((b'Value is not class, {}').format(class_))
            self.__services[name] = class_

        return

    def __call__(self, func):
        spec = getargspec(func)
        for name, _ in self.__services.iteritems():
            if name not in spec.args:
                raise DependencyError((b'Argument {} is not found in {}').format(name, func))

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for serviceName, clazz in self.__services.iteritems():
                actual = kwargs.get(serviceName)
                if actual is None:
                    kwargs[serviceName] = instance(clazz)

            return func(*args, **kwargs)

        return wrapper


class DependencyError(SoftException):
    pass


class DependencyManager(object):
    __slots__ = (b'__services', b'__replacedServices')

    def __init__(self):
        super(DependencyManager, self).__init__()
        self.__services = {}
        self.__replacedServices = set()
        return

    def getService(self, class_):
        try:
            result = self.__services[class_].value()
        except KeyError:
            raise DependencyError((b'Service {} is not created').format(class_))

        return result

    def addInstance(self, class_, obj, finalizer=None):
        self._validate(class_)
        self.__services[class_] = _DependencyItem(order=_orderGen.next(), service=obj, finalizer=finalizer)
        _logger.debug(b'Instance of service is added: %r->%r', class_, obj)
        return

    def replaceInstance(self, class_, obj, finalizer=None, force=True):
        if class_ not in self.__services:
            _logger.warning(b'No implementation found for Service %r prior to replace!', class_)
        elif class_ in self.__replacedServices and not force:
            raise DependencyError((b'Service {} is already replaced').format(class_))
        else:
            self.__services[class_].finalize()
            self.__services[class_].clear()
            self.__services.pop(class_, None)
        self.addInstance(class_, obj, finalizer)
        self.__replacedServices.add(class_)
        return

    def addRuntime(self, class_, creator, finalizer=None):
        self._validate(class_)
        self.__services[class_] = _RuntimeItem(creator, finalizer=finalizer)
        _logger.debug(b'Factory of service is added: %r', class_)
        return

    def addConfig(self, config):
        if not callable(config):
            raise DependencyError(b'Config must be callable')
        config(self)
        return

    def clear(self):
        services = sorted(self.__services.itervalues(), key=(lambda item: item.order()), reverse=True)
        for service in services:
            service.finalize()

        for service in services:
            service.clear()

        self.__services.clear()
        return

    def _validate(self, class_):
        if not inspect.isclass(class_):
            raise DependencyError((b'First argument is not class, {}').format(class_))
        if class_ in self.__services:
            raise DependencyError((b'Service {} is already added').format(class_))
        return


class _ServiceDescriptor(object):
    __slots__ = (b'__class',)

    def __init__(self, class_):
        super(_ServiceDescriptor, self).__init__()
        self.__class = class_
        return

    def __set__(self, _, value):
        raise AttributeError((b'Service {} can not be rewritten').format(self.__class))
        return

    def __get__(self, inst, owner=None):
        if _g_manager is None:
            raise AttributeError(b'Manager of dependencies is not created and configured')
        return _g_manager.getService(self.__class)


class _DependencyItem(object):
    __slots__ = (b'_order', b'_service', b'_finalizer')

    def __init__(self, order=_MAX_ORDER_NUMBER, service=None, finalizer=None):
        super(_DependencyItem, self).__init__()
        self._order = order
        self._service = service
        if finalizer is not None and not callable(finalizer) and not isinstance(finalizer, basestring):
            raise DependencyError((b'Finalizer {} is invalid').format(finalizer))
        self._finalizer = finalizer
        return

    def value(self):
        return self._service

    def order(self):
        return self._order

    def finalize(self):
        if self._service is None or self._finalizer is None:
            return
        if callable(self._finalizer):
            self._finalizer(self._service)
        else:
            finalizer = getattr(self._service, self._finalizer, None)
            if finalizer is not None and callable(finalizer):
                try:
                    finalizer()
                except Exception:
                    _logger.exception(b'Error finalizing %r', self._service)

            else:
                raise DependencyError((b'Finalizer {} is not found').format(self._finalizer))
        return

    def clear(self):
        self._finalizer = None
        self._service = None
        return


class _RuntimeItem(_DependencyItem):
    __slots__ = (b'__isCreatorInvoked', b'__creator')

    def __init__(self, creator, finalizer=None):
        super(_RuntimeItem, self).__init__(finalizer=finalizer)
        self.__isCreatorInvoked = False
        self.__creator = creator
        return

    def value(self):
        if not self.__isCreatorInvoked:
            self.__isCreatorInvoked = True
            self._service = self.__creator()
            self._order = _orderGen.next()
        return self._service

    def clear(self):
        self.__creator = None
        super(_RuntimeItem, self).clear()
        return
