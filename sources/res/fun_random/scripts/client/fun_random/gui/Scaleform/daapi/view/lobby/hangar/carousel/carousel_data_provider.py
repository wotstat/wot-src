from arena_bonus_type_caps import ARENA_BONUS_TYPE_CAPS
from constants import ARENA_BONUS_TYPE, Configs
from fun_random.gui.feature.util.fun_helpers import getVehicleComparisonKey
from fun_random.gui.feature.util.fun_mixins import FunAssetPacksMixin, FunSubModesWatcher
from fun_random.gui.feature.util.fun_wrappers import hasDesiredSubMode
from gui.Scaleform.daapi.view.lobby.hangar.carousels.battle_pass.carousel_data_provider import BattlePassCarouselDataProvider
from gui.Scaleform.daapi.view.lobby.hangar.carousels.carousel_helpers import getUnsuitable2queueTooltip
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS
from gui.impl.gen import R
from gui.shared.gui_items.Vehicle import Vehicle
from helpers import server_settings

class FunRandomCarouselDataProvider(BattlePassCarouselDataProvider, FunAssetPacksMixin, FunSubModesWatcher):

    def __init__(self, carouselFilter, itemsCache):
        super(FunRandomCarouselDataProvider, self).__init__(carouselFilter, itemsCache)
        self.__isCrystalsFarmEnabled = self.__isCrystalsFarmPossible()
        return

    def onSubModeSelected(self):
        self.filter.update({}, False)
        self._setBaseCriteria()
        return

    @classmethod
    def _vehicleComparisonKey(cls, vehicle):
        return (not cls._isSuitableForQueue(vehicle),) + getVehicleComparisonKey(vehicle)

    def _populate(self):
        super(FunRandomCarouselDataProvider, self)._populate()
        self._lobbyContext.onServerSettingsChanged += self.__onServerSettingsChanged
        return

    def _dispose(self):
        self._lobbyContext.onServerSettingsChanged -= self.__onServerSettingsChanged
        super(FunRandomCarouselDataProvider, self)._dispose()
        return

    def _isBattlePassHidden(self, vehicle):
        result = super(FunRandomCarouselDataProvider, self)._isBattlePassHidden(vehicle)
        return result or not self.battlePassController.isGameModeEnabled(ARENA_BONUS_TYPE.FUN_RANDOM)

    def _getVehicleStats(self, vehicle):
        return {b'statsText': b'', b'visibleStats': False}

    def _setBaseCriteria(self):
        super(FunRandomCarouselDataProvider, self)._setBaseCriteria()
        self._baseCriteria = self.__getBaseCriteria() or self._baseCriteria
        return

    def _buildVehicle(self, vehicle):
        result = super(FunRandomCarouselDataProvider, self)._buildVehicle(vehicle)
        state, _ = vehicle.getState()
        if state == Vehicle.VEHICLE_STATE.UNSUITABLE_TO_QUEUE:
            self.__specifyLockedTooltip(result, vehicle)
        result[b'tooltip'] = TOOLTIPS_CONSTANTS.FUN_RANDOM_CAROUSEL_VEHICLE
        result[b'isEarnCrystals'] = result[b'isEarnCrystals'] and self.__isCrystalsFarmEnabled
        if not ARENA_BONUS_TYPE_CAPS.checkAny(ARENA_BONUS_TYPE.FUN_RANDOM, ARENA_BONUS_TYPE_CAPS.DAILY_MULTIPLIED_XP):
            result[b'xpImgSource'] = b''
        return result

    def __isCrystalsFarmPossible(self):
        config = self._serverSettings.getCrystalRewardConfig()
        return config.isCrystalEarnPossible(ARENA_BONUS_TYPE.FUN_RANDOM)

    @hasDesiredSubMode()
    def __getBaseCriteria(self):
        return self.getDesiredSubMode().getCarouselBaseCriteria()

    @server_settings.serverSettingsChangeListener(Configs.CRYSTAL_REWARDS_CONFIG.value)
    def __onServerSettingsChanged(self, *_, **_FunRandomCarouselDataProvider__kwargs):
        self.__isCrystalsFarmEnabled = self.__isCrystalsFarmPossible()
        return

    @hasDesiredSubMode()
    def __specifyLockedTooltip(self, result, vehicle):
        validationResult = self.getDesiredSubMode().isSuitableVehicle(vehicle)
        if validationResult is not None:
            resPath = R.strings.fun_random.funRandomCarousel.lockedTooltip
            result[b'lockedTooltip'] = getUnsuitable2queueTooltip(validationResult, resPath, modeName=self.getModeUserName())
        return
