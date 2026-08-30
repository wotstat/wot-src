import typing
if typing.TYPE_CHECKING:
    from uilogging.types import FeatureType, GroupType, ActionType, LogLevelType

class IUILoggingCore(object):

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def isFeatureEnabled(self, feature):
        raise NotImplementedError
        return

    def log(self, feature, group, action, loglevel, **params):
        raise NotImplementedError
        return

    def ensureSession(self):
        raise NotImplementedError
        return

    def start(self, ensureSession=False):
        raise NotImplementedError
        return

    def send(self):
        raise NotImplementedError
        return


class IUILoggingListener(object):

    def fini(self):
        raise NotImplementedError
        return
