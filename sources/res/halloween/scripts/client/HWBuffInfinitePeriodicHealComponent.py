from __future__ import absolute_import
import BigWorld
from dyn_components_groups import groupComponent
from halloween.gui.halloween_gui_constants import BATTLE_CTRL_ID
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from xml_config_specs import StrParam
from HWBuffSequencesComponent import HWBuffSequencesComponent
from shared_utils import nextTick
from vehicle_systems.stricted_loading import makeCallbackWeak

@groupComponent(buffKey=StrParam())
class HWBuffInfinitePeriodicHealComponent(HWBuffSequencesComponent):
    guiSessionProvider = dependency.descriptor(IBattleSessionProvider)

    def __init__(self):
        super(HWBuffInfinitePeriodicHealComponent, self).__init__()
        self._buffKey = self.groupComponentConfig.buffKey
        return

    def set_isActive(self, prev):
        self._onChangeBuffState()
        return

    def onDestroy(self):
        BigWorld.player().arena.onVehicleHealthChanged -= self._onVehicleHealthChanged
        super(HWBuffInfinitePeriodicHealComponent, self).onDestroy()
        return

    def _onAvatarReady(self):
        super(HWBuffInfinitePeriodicHealComponent, self)._onAvatarReady()
        BigWorld.player().arena.onVehicleHealthChanged += self._onVehicleHealthChanged
        self._onChangeBuffState()
        return

    def _activateEffects(self):
        super(HWBuffInfinitePeriodicHealComponent, self)._activateEffects()
        nextTick(makeCallbackWeak(self._playEffect))()
        return

    def _onChangeBuffState(self):
        hwBattleGuiCtrl = self.guiSessionProvider.dynamic.getControllerByID(BATTLE_CTRL_ID.HW_BATTLE_GUI_CTRL)
        if hwBattleGuiCtrl:
            ctx = {b'buffKey': (self._buffKey), b'isActive': (self.isActive), 
               b'vehicleID': (self.entity.id)}
            hwBattleGuiCtrl.buffStateChanged(ctx)
        self._playEffect()
        return

    def _onVehicleHealthChanged(self, vehicleID, attackerID, damage):
        if self.entity.id == vehicleID:
            self._playEffect()
        return

    def _playEffect(self):
        if self.isActive and self.entity.health < self.entity.maxHealth:
            self._startEffects()
        else:
            self._stopEffects()
        return
