from __future__ import absolute_import
import json, logging, weakref
from collections import defaultdict
import GUI
from gui.Scaleform import SCALEFORM_SWF_PATH_V3
_logger = logging.getLogger(__name__)
_DEFAULT_FLASH_COMPONENT_CLASS = b'Flash'

class InputKeyMode(object):
    DEFAULT = 0
    IGNORE_RESULT = 1
    NO_HANDLE = 2


class FlashComponentWrapper(object):

    def __init__(self):
        super(FlashComponentWrapper, self).__init__()
        self.__exCbs = defaultdict(set)
        self.__component = None
        self.__flashSize = (2, 2)
        self.__isActive = False
        self.__isVisible = True
        return

    def __del__(self):
        _logger.debug(b'Deleted: %s', self)
        return

    @property
    def isActive(self):
        return self.__isActive

    @property
    def component(self):
        return self.__component

    @property
    def movie(self):
        if self.__component is not None:
            return self.__component.movie
        else:
            return

    @property
    def moviePath(self):
        if self.__component is not None:
            return self.__component.moviePath
        else:
            return b''

    @property
    def movieUid(self):
        if self.__component is not None:
            return self.__component.movie.movieUid
        else:
            return 0

    def isVisible(self):
        return self.component.visible

    def setVisible(self, visible):
        self.__isVisible = visible
        if self.__component is not None:
            self.__component.visible = visible
        return

    def afterCreate(self):
        return

    def beforeDelete(self):
        self.removeAllCallbacks()
        self.__exCbs.clear()
        self.__flashSize = None
        del self.__component
        self.__component = None
        return

    def createComponent(self, swf=b'', className=_DEFAULT_FLASH_COMPONENT_CLASS, args=None, path=SCALEFORM_SWF_PATH_V3, **kwargs):
        if swf:
            fileName = (b'{}/{}').format(path, swf)
        else:
            fileName = b''
        if self.__component is None:
            args = args or []
            self.__component = getattr(GUI, className)(fileName, *args, **kwargs)
            self.__component.focus = True
            self.__component.moveFocus = True
            self.__component.position.z = 0.5
            movie = self.__component.movie
            movie.setExternalInterfaceCallback(_ExternalInterfaceObj(self))
            if self.__isActive:
                self.__doActivate(True)
            self.__component.visible = self.__isVisible
        else:
            _logger.warning(b'Flash is already created: %r', self.__component)
        return

    def active(self, state):
        if self.__isActive != state:
            self.__isActive = state
            if self.__component is not None:
                self.__doActivate(state)
        return

    def close(self):
        if self.__component is not None:
            self.__component.script = None
        self.active(False)
        self.beforeDelete()
        return

    def getMember(self, path):
        return getattr(self.movie, path, None)

    def addExternalCallback(self, command, function):
        self.__exCbs[command].add(function)
        return

    def removeExternalCallback(self, command, function=None):
        try:
            if function is None:
                self.__exCbs.pop(command)
            elif function in self.__exCbs[command]:
                self.__exCbs[command].remove(function)
        except KeyError:
            pass

        return

    def addExternalCallbacks(self, commands):
        add = self.addExternalCallback
        for command, function in commands.items():
            add(command, function)

        return

    def removeExternalCallbacks(self, *args):
        remove = self.removeExternalCallback
        for command in args:
            remove(command)

        return

    def removeAllCallbacks(self):
        self.__exCbs.clear()
        return

    def handleExternalInterfaceCallback(self, command, args):
        result = False
        if command == b'callNice':
            tmp = list(json.loads(args[0]))
            command = tmp.pop(0)
            args = tmp
        if command in self.__exCbs:
            result = True
            callbacks = self.__exCbs[command]
            for callback in callbacks:
                callback(*args)

        else:
            _logger.debug(b'ExternalInterfaceCallback "%s" not found: %r', command, args)
        return result

    def __doActivate(self, flag):
        if flag:
            GUI.addRoot(self.__component)
            self.__component.size = self.__flashSize
        else:
            GUI.delRoot(self.__component)
        return


class Flash(FlashComponentWrapper):

    def __init__(self, swf=b'', className=b'Flash', args=None, path=SCALEFORM_SWF_PATH_V3):
        super(Flash, self).__init__()
        self.createComponent(swf=swf, className=className, args=args, path=path)
        return


class _ExternalInterfaceObj(object):

    def __init__(self, obj):
        self.__weakObj = weakref.ref(obj)
        return

    def __call__(self, command, args):
        obj = self.__weakObj()
        if obj is not None:
            obj.handleExternalInterfaceCallback(command, args)
        else:
            _logger.warning(b'Weak object has been already destroyed: command = %s, args = %r.', command, args)
        return
