from __future__ import absolute_import
from future.utils import viewitems
import BigWorld, WWISE
from gui.Scaleform.daapi.view.meta.SituationIndicatorsMeta import SituationIndicatorsMeta
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE, VEHICLE_VIEW_STATE_ID_TO_WEATHER_ZONE_NAME
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.utils.functions import makeTooltip
from helpers import dependency
from items import tankmen
from items.components.perks_constants import PerkState
from shared_utils import CONST_CONTAINER
from skeletons.gui.battle_session import IBattleSessionProvider
from ReplayEvents import g_replayEvents

class PerksSounds(CONST_CONTAINER):
    PERK = b'detachment_perk'
    PERK_STOP = b'detachment_perk_stop'


class WeatherState(object):
    INACTIVE = 0
    ACTIVE = 1


def _getTooltip(weatherName):
    toolTipRes = R.strings.tooltips.weather.dyn(weatherName)
    toolTipStr = makeTooltip(header=backport.text(toolTipRes.header()), body=backport.text(toolTipRes.body()))
    return toolTipStr


class SituationIndicators(SituationIndicatorsMeta):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)

    def setPerks(self, perks):
        self.clearHUD()
        perksData = []
        for perkData in sorted(perks, key=(lambda k: k[b'perkID'])):
            perkID = perkData[b'perkID']
            skillName = tankmen.getSkillsConfig().vsePerkToSkill.get(perkID)
            perk = {b'perkName': skillName, 
               b'state': (perkData[b'state']), 
               b'duration': (perkData[b'coolDown']), 
               b'lifeTime': (self._getLifeTime(perkData))}
            perksData.append(perk)

        self.as_setPerksS(perksData)
        return

    def updatePerks(self, changedPerks, prevPerks):
        for perkID, perkData in viewitems(changedPerks):
            lifeTime = self._getLifeTime(perkData)
            state = perkData[b'state']
            skillName = tankmen.getSkillsConfig().vsePerkToSkill.get(perkID)
            self.as_updatePerkS(skillName, state, perkData[b'coolDown'], lifeTime)
            if state == PerkState.ACTIVE:
                if perkID not in prevPerks or prevPerks[perkID][b'state'] != PerkState.ACTIVE:
                    WWISE.WW_eventGlobal(PerksSounds.PERK)
            elif perkID in prevPerks and prevPerks[perkID][b'state'] == PerkState.ACTIVE:
                WWISE.WW_eventGlobal(PerksSounds.PERK_STOP)

        return

    def clearHUD(self):
        self.as_clearPanelS()
        return

    def _populate(self):
        super(SituationIndicators, self)._populate()
        vStateCtrl = self.sessionProvider.shared.vehicleState
        if vStateCtrl is not None:
            vStateCtrl.onVehicleStateUpdated += self.__onVehicleStateUpdated
            vStateCtrl.onVehicleControlling += self.__onVehicleControlling
        g_replayEvents.onPause += self._onReplayPaused
        return

    def _dispose(self):
        g_replayEvents.onPause -= self._onReplayPaused
        super(SituationIndicators, self)._dispose()
        return

    def _destroy(self):
        vStateCtrl = self.sessionProvider.shared.vehicleState
        if vStateCtrl is not None:
            vStateCtrl.onVehicleStateUpdated -= self.__onVehicleStateUpdated
            vStateCtrl.onVehicleControlling -= self.__onVehicleControlling
        super(SituationIndicators, self)._destroy()
        return

    def _getLifeTime(self, perkData):
        lifeTimeServer = perkData[b'lifeTime']
        if BigWorld.serverTime() < lifeTimeServer:
            return lifeTimeServer - BigWorld.serverTime()
        return -1

    def __onVehicleStateUpdated(self, state, value):
        if state in VEHICLE_VIEW_STATE.WEATHER_ZONES:
            weatherName = VEHICLE_VIEW_STATE_ID_TO_WEATHER_ZONE_NAME[state]
            self.as_updateWeatherS(weatherName, (value.needToCloseTimer() or WeatherState).ACTIVE if 1 else WeatherState.INACTIVE, _getTooltip(weatherName))
        return

    def __onVehicleControlling(self, _):
        ctrl = self.sessionProvider.shared.vehicleState
        if ctrl is None:
            return
        else:
            weatherItemsToSet = []
            for state in VEHICLE_VIEW_STATE.WEATHER_ZONES:
                value = ctrl.getStateValue(state)
                weatherName = VEHICLE_VIEW_STATE_ID_TO_WEATHER_ZONE_NAME[state]
                weatherItemsToSet.append({b'weatherName': weatherName, 
                   b'state': (WeatherState.ACTIVE if value is not None and not value.needToCloseTimer() else WeatherState.INACTIVE), 
                   b'toolTip': (_getTooltip(weatherName))})

            self.as_setWeatherS(weatherItemsToSet)
            return

    def _onReplayPaused(self, isPaused):
        self.as_replayPauseS(isPaused)
        return
