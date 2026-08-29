import logging
from gui.battle_control.controllers.appearance_cache_ctrls.event_appearance_cache_ctrl import EventAppearanceCacheController
from helpers import uniprof
_logger = logging.getLogger(__name__)

class MapsTrainingAppearanceCacheController(EventAppearanceCacheController):

    @uniprof.regionDecorator(label=b'MapsTrainingAppearanceCacheController.updateSpawnList', scope=b'wrap')
    def updateSpawnList(self, spawnListData):
        self._updateSpawnList(spawnListData)
        _logger.debug(b'MapsTrainingAppearanceCacheController SpawnList cache updated=%s', spawnListData)
        return
