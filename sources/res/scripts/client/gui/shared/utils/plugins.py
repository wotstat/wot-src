import operator, weakref
from debug_utils import LOG_ERROR
from shared_utils import forEach

class IPlugin(object):
    __slots__ = (b'_parentObj',)

    def __init__(self, parentObj):
        super(IPlugin, self).__init__()
        self._parentObj = parentObj
        return

    def init(self, *args):
        return

    def fini(self):
        self._parentObj = None
        return

    def start(self):
        return

    def stop(self):
        return

    def reset(self):
        return

    def update(self):
        return

    @property
    def parentObj(self):
        return self._parentObj


class PluginsCollection(IPlugin):
    __slots__ = (b'__plugins',)

    def __init__(self, parentObj):
        super(PluginsCollection, self).__init__(weakref.proxy(parentObj))
        self.__plugins = {}
        return

    def __iter__(self):
        return iter(self.__plugins)

    def addPlugins(self, plugins):
        for pluginName, pluginClass in plugins.iteritems():
            if pluginName in self.__plugins:
                LOG_ERROR(b'Plugin with this name was already added: ', pluginName, pluginClass)
                continue
            pluginObj = pluginClass(self._parentObj)
            self.__plugins[pluginName] = pluginObj

        return

    def removePlugins(self, *names):
        for name in names:
            plugin = self.__plugins.pop(name, None)
            if plugin is not None:
                plugin.stop()
                plugin.fini()

        return

    def getPlugin(self, name):
        if name in self.__plugins:
            return self.__plugins[name]
        else:
            return

    def init(self, *args):
        self._invoke(b'init', *args)
        return

    def fini(self):
        self._invoke(b'fini')
        self.__plugins.clear()
        super(PluginsCollection, self).fini()
        return

    def start(self):
        self._invoke(b'start')
        return

    def stop(self):
        self._invoke(b'stop')
        return

    def reset(self):
        self._invoke(b'reset')
        return

    def update(self):
        self._invoke(b'update')
        return

    def _invoke(self, method, *args):
        forEach(operator.methodcaller(method, *args), self.__plugins.itervalues())
        return
