from debug_utils import LOG_DEBUG_DEV

def _iterEventNames(events):
    return (name for name in dir(events) if name.startswith(b'on'))


class EventsDebugger(object):

    def __init__(self, events):
        for eventName in _iterEventNames(events):
            event = getattr(events, eventName)
            processor = getattr(self, eventName)
            event += processor

        return

    def _shouldHandle(self, eventName):
        return True

    def _getDebugPrefix(self):
        return b'[EVENT]'

    def _buildDebugString(self, item):
        return b'%s %s' % (self._getDebugPrefix(), item)

    def __getattr__(self, item):
        if self._shouldHandle(item):
            return (lambda *args, **kwargs: LOG_DEBUG_DEV(self._buildDebugString(item), *args, **kwargs))
        else:
            return (lambda *args, **kwargs: None)

        return
