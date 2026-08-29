import functools, logging, BigWorld
_regions = {}
_logger = logging.getLogger(__name__)
_MAX_RGB_COLOR = 16581375

def _makeColorFromLabel(label):
    return hash(label) % _MAX_RGB_COLOR


def enterToRegion(label, color=None):
    if label not in _regions:
        if color is None:
            color = _makeColorFromLabel(label)
        _regions[label] = BigWorld.uniprofRegionEnter(label, color)
        _logger.debug(b'Region is entered: label=%s, color=0x%06X', label, color)
    else:
        _logger.debug(b'Region is already entered: label=%s', label)
    return


def exitFromRegion(label):
    if label in _regions:
        BigWorld.uniprofRegionExit(_regions.pop(label))
        _logger.debug(b'Region is exited: label=%s', label)
    else:
        _logger.debug(b'Region is not found to exit: label=%s', label)
    return


def regionDecorator(label, scope=b'wrap'):
    if not label:
        _logger.warning(b'Label is not defined')
        return _RegionDecorator(b'')
    if scope == b'wrap':
        return _RegionDecorator(label, trackEnter=True, trackExit=True)
    if scope == b'enter':
        return _RegionDecorator(label, trackEnter=True, trackExit=False)
    if scope == b'exit':
        return _RegionDecorator(label, trackEnter=False, trackExit=True)
    _logger.warning(b'Scope "%s" for label "%s" is not found', scope, label)
    return _RegionDecorator(label)


class _RegionDecorator(object):
    __slots__ = (b'_label', b'_trackEnter', b'_trackExit')

    def __init__(self, label, trackEnter=False, trackExit=False):
        super(_RegionDecorator, self).__init__()
        self._label = label
        self._trackEnter = trackEnter
        self._trackExit = trackExit
        return

    def __call__(self, func):

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            self._enter()
            result = func(*args, **kwargs)
            self._exit()
            return result

        return wrapper

    def _enter(self):
        if self._trackEnter:
            enterToRegion(self._label)
        return

    def _exit(self):
        if self._trackExit:
            exitFromRegion(self._label)
        return
