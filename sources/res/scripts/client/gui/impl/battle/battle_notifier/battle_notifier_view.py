import logging
from collections import deque
import ArenaType
from constants import ARENA_BONUS_TYPE
from items.vehicles import getVehicleType, getVehicleClassFromVehicleType
from frameworks.wulf import ViewFlags, ViewSettings
from gui.impl.gen import R
from gui.impl.gen.view_models.views.battle.battle_notifier.battle_notifier_view_model import BattleNotifierViewModel, ResultEnum
from gui.impl.pub import ViewImpl
from gui.shared.money import Currency
_logger = logging.getLogger(__name__)

class BattleNotifierView(ViewImpl):
    __slots__ = (b'__resultsQueue', b'__uiReadyForData', b'__arenaLoaded')

    def __init__(self):
        settings = ViewSettings(R.views.battle.battle_notifier.BattleNotifierView(), ViewFlags.VIEW, BattleNotifierViewModel())
        super(BattleNotifierView, self).__init__(settings)
        self.__resultsQueue = deque()
        self.__uiReadyForData = True
        self.__arenaLoaded = False
        return

    @property
    def viewModel(self):
        return super(BattleNotifierView, self).getViewModel()

    def arenaLoadCompleted(self):
        self.__arenaLoaded = True
        self._sendNotificationData()
        return

    def addBattleResults(self, message):
        results = _collectResults(message)
        if results is None:
            return
        else:
            self.__resultsQueue.append(results)
            self._sendNotificationData()
            return

    def _initialize(self, *args, **kwargs):
        self.viewModel.onResultShown += self.__onResultShown
        return

    def _finalize(self):
        self.viewModel.onResultShown -= self.__onResultShown
        return

    def _sendNotificationData(self):
        if self.__arenaLoaded and self.__uiReadyForData:
            self._fillComponentModel()
        return

    def _fillComponentModel(self):
        if self.__resultsQueue:
            battleResult = self.__resultsQueue.popleft()
            with self.viewModel.transaction() as tr:
                tr.setBattleResult(battleResult[b'result'])
                tr.setBattleStartTime(battleResult[b'time'])
                tr.setMapName(battleResult[b'arenaName'])
                tr.setVehicleName(battleResult[b'vehicleName'])
                tr.setVehicleTier(battleResult[b'vehicleTier'])
                tr.setVehicleClass(battleResult[b'vehicleClass'])
                tr.setCreditsAmount(battleResult[Currency.CREDITS])
                tr.setExperienceAmount(battleResult[b'xp'])
                tr.setCrystalAmount(battleResult[Currency.CRYSTAL])
            self.__uiReadyForData = False
        return

    def __onResultShown(self):
        self.__uiReadyForData = True
        self._sendNotificationData()
        return


def _randomBattleResults(message):
    battleResults = message.data
    arenaTypeID = battleResults.get(b'arenaTypeID', 0)
    if arenaTypeID > 0 and arenaTypeID in ArenaType.g_cache:
        arenaType = ArenaType.g_cache[arenaTypeID]
    else:
        arenaType = None
    arenaCreateTime = battleResults.get(b'arenaCreateTime', None)
    if arenaCreateTime and arenaType:
        results = {b'time': arenaCreateTime, b'vehicleTier': b'N/A', 
           b'vehicleClass': b'N/A', 
           b'vehicleName': b'N/A', 
           b'result': (ResultEnum(battleResults.get(b'isWinner', 0))), 
           b'arenaName': (arenaType.name), 
           b'xp': 0, 
           (Currency.CREDITS): 0, 
           (Currency.CRYSTAL): 0}
        intCD = battleResults.get(b'playerVehicles', {}).keys()[0]
        vehicleType = getVehicleType(intCD)
        results[b'vehicleName'] = vehicleType.shortUserString
        results[b'vehicleClass'] = getVehicleClassFromVehicleType(vehicleType)
        results[b'vehicleTier'] = vehicleType.level
        xp = battleResults.get(b'xp')
        if xp:
            results[b'xp'] = int(xp)
        accCredits = battleResults.get(Currency.CREDITS) - battleResults.get(b'creditsToDraw', 0)
        if accCredits:
            results[Currency.CREDITS] = int(accCredits)
        crystal = battleResults.get(Currency.CRYSTAL)
        if crystal:
            results[Currency.CRYSTAL] = int(crystal)
        return results
    _logger.warning(b'Could not format message, no arena createTime or arenaType found in message.')
    return
    return


_formatters = {(ARENA_BONUS_TYPE.REGULAR): _randomBattleResults, 
   (ARENA_BONUS_TYPE.EPIC_RANDOM): _randomBattleResults, 
   (ARENA_BONUS_TYPE.VERSUS_AI): _randomBattleResults}

def _collectResults(message):
    arenaBonusType = message.data.get(b'bonusType', None)
    if arenaBonusType is None:
        _logger.warning(b'[BattleNotifier] no "bonusType" item found in battle results. Cannot parse results.')
        return
    else:
        formatter = _formatters.get(arenaBonusType, None)
        if formatter is None:
            _logger.debug(b'[BattleNotifier] The arena bonus type, %s, is not yet supported. Chat message: %s', arenaBonusType, message)
            return
        return formatter(message)
