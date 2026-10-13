from __future__ import absolute_import
import BigWorld
from helpers import dependency
from gui.impl.lobby.user_missions.hangar_widget.services import IMissionsContainerService

class IUserMissionPlugin(object):
    _missionsContainerService = dependency.descriptor(IMissionsContainerService)
    _PLUGIN_DESTROY_DELAY = 0
    _pendingDestroyCallbackId = None

    @classmethod
    def getPathToResource(cls):
        raise NotImplementedError
        return

    @classmethod
    def getDependencies(cls):
        raise NotImplementedError
        return

    @classmethod
    def getViewAlias(cls):
        raise NotImplementedError
        return

    @classmethod
    def isPluginEnabled(cls):
        raise NotImplementedError
        return

    @classmethod
    def startListening(cls):
        raise NotImplementedError
        return

    @classmethod
    def stopListening(cls):
        raise NotImplementedError
        return

    @classmethod
    def cancelPendingUpdates(cls):
        if cls._pendingDestroyCallbackId is not None:
            BigWorld.cancelCallback(cls._pendingDestroyCallbackId)
            cls._pendingDestroyCallbackId = None
        return

    @classmethod
    def _onUpdate(cls, *args, **kwargs):
        cls.cancelPendingUpdates()
        if cls.isPluginEnabled() or cls._PLUGIN_DESTROY_DELAY == 0:
            cls._performUpdate(*args, **kwargs)
        else:
            cls._pendingDestroyCallbackId = BigWorld.callback(cls._PLUGIN_DESTROY_DELAY, (lambda : cls._performUpdate(*args, **kwargs)))
        return

    @classmethod
    def _performUpdate(cls, *args, **kwargs):
        cls._pendingDestroyCallbackId = None
        cls._missionsContainerService.setPluginVisibility(cls.getViewAlias(), cls.isPluginEnabled())
        return
