from __future__ import absolute_import
from helpers import dependency
from gui.impl.lobby.user_missions.hangar_widget.services import IMissionsContainerService

class IUserMissionPlugin(object):
    _missionsContainerService = dependency.descriptor(IMissionsContainerService)

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
    def _onUpdate(cls, *args, **kwargs):
        raise NotImplementedError
        return
