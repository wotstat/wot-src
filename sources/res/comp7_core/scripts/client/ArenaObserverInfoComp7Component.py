import logging, BigWorld
_logger = logging.getLogger(__name__)

class ArenaObserverInfoComp7Component(BigWorld.DynamicScriptComponent):

    def __init__(self):
        super(ArenaObserverInfoComp7Component, self).__init__()
        _logger.debug(b'__init__')
        return

    def onDestroy(self):
        super(ArenaObserverInfoComp7Component, self).onDestroy()
        _logger.debug(b'onDestroy')
        return

    def setNested_vehiclesInfo(self, changePath, oldValue):
        return

    def setSlice_vehiclesInfo(self, changePath, oldValue):
        return

    def setNested_poiInfo(self, changePath, oldValue):
        return

    def setSlice_poiInfo(self, changePath, oldValue):
        return

    def setNested_teamBasesInfo(self, changePath, oldValue):
        return

    def setSlice_teamBasesInfo(self, changePath, oldValue):
        return
