import BigWorld, SoundGroups
from script_component.DynamicScriptComponent import DynamicScriptComponent
from gui.battle_control import avatar_getter
from gui.battle_control.battle_constants import VEHICLE_VIEW_STATE
from items import vehicles
from white_tiger.gui.gui_constants import FEEDBACK_EVENT_ID
from white_tiger.gui.battle_control.controllers.consumables.equipment_sound import playStunAreaHunterVO
from white_tiger.gui.Scaleform.daapi.view.battle.white_tiger.status_notifications.sn_items import WTTimerViewState

class WTVehicleFactorAppliers(DynamicScriptComponent):
    _ABILITIES_NOTIFICATION_TIMER = {b'wt_stun_area': (
                       VEHICLE_VIEW_STATE.WT_STUN_AREA, WTTimerViewState), 
       b'wt_impulse_mod_a': (
                           VEHICLE_VIEW_STATE.STUN, WTTimerViewState), 
       b'wt_stun_area_mod_a': (
                             VEHICLE_VIEW_STATE.WT_STUN_AREA_MOD_A, WTTimerViewState), 
       b'wt_extractor_shot': (
                            VEHICLE_VIEW_STATE.STUN, WTTimerViewState)}
    _ABILITIES_MARKERS = {b'wt_stun_area': (FEEDBACK_EVENT_ID.WT_VEHICLE_STUN_AREA_DEBUFF), 
       b'wt_stun_area_mod_a': (FEEDBACK_EVENT_ID.WT_VEHICLE_STUN_AREA_MOD_A_DEBUFF), 
       b'wt_extractor_shot': (FEEDBACK_EVENT_ID.WT_EXTRACTOR_SHOT_DEBUFF), 
       b'wt_impulse_mod_a': (FEEDBACK_EVENT_ID.WT_VEHICLE_SILENCE)}
    _ABILITIES_SOUNDS = {b'wt_impulse_mod_a': {b'start': b'ev_white_tiger_stun_effect_start', 
                             b'stop': b'ev_white_tiger_stun_effect_end'}, 
       b'wt_extractor_shot': {b'start': b'ev_white_tiger_stun_effect_imp_start', 
                              b'stop': b'ev_white_tiger_stun_effect_imp_end'}, 
       b'wt_stun_area_mod_a': {b'start': b'ev_white_tiger_stun_effect_start', 
                               b'stop': b'ev_white_tiger_stun_effect_end'}, 
       b'wt_stun_area': {b'start': b'ev_white_tiger_stun_effect_start', 
                         b'stop': b'ev_white_tiger_stun_effect_end'}}

    def __init__(self):
        super(WTVehicleFactorAppliers, self).__init__()
        self.__guiFeedback = self.entity.guiSessionProvider.shared.feedback
        self.__equipment = None
        if self.equipmentID > 0:
            self.set_equipmentID(self.equipmentID)
            self.__update()
        return

    def onDestroy(self):
        self.__update()
        self.__equipment = None
        super(WTVehicleFactorAppliers, self).onDestroy()
        return

    def set_equipmentID(self, prev):
        if self.equipmentID == prev:
            return
        self.__equipment = vehicles.g_cache.equipments().get(self.equipmentID)
        return

    def set_finishTime(self, prev):
        if self.finishTime == prev:
            return
        self.__update()
        return

    def _onAvatarReady(self):
        if self.equipmentID > 0:
            self.__equipment = vehicles.g_cache.equipments().get(self.equipmentID)
        self.__update()
        return

    def __update(self):
        if self.__equipment is None:
            return
        else:
            duration = self.finishTime - BigWorld.serverTime()
            isShown = duration > 0
            self.__commonUpdate(isShown, duration)
            return

    def __commonUpdate(self, isShown, duration):
        if self.__equipment.name in (b'wt_stun_area', b'wt_stun_area_mod_a'):
            self.__updateStunNotificationTimer(isShown, duration)
        if self.__equipment.name == b'wt_stun_area':
            self.__playStunVoiceOver(isShown)
        if self.__equipment.name in self._ABILITIES_MARKERS:
            self.__updateMarker(isShown, duration)
        if self.__equipment.name in self._ABILITIES_NOTIFICATION_TIMER:
            self.__updateNotificationTimer(isShown, duration)
        if self.__equipment.name in self._ABILITIES_SOUNDS:
            self.__playAbilitySound(isShown)
        return

    def __updateMarker(self, isShown, duration):
        self.__guiFeedback.onVehicleFeedbackReceived(self._ABILITIES_MARKERS[self.__equipment.name], self.entity.id, {b'isShown': isShown, b'duration': duration})
        return

    def __updateNotificationTimer(self, isShown, duration):
        timerID, clazz = self._ABILITIES_NOTIFICATION_TIMER[self.__equipment.name]
        value = clazz(isShown, duration, self.finishTime)
        self.entity.guiSessionProvider.invalidateVehicleState(timerID, value, vehicleID=self.entity.id)
        return

    def __updateStunNotificationTimer(self, isShown, duration):
        value = WTTimerViewState(isShown, duration, self.finishTime)
        self.entity.guiSessionProvider.invalidateVehicleState(VEHICLE_VIEW_STATE.WT_STUN_AREA, value, vehicleID=self.entity.id)
        return

    def __playAbilitySound(self, isActive):
        if self.entity.id != BigWorld.player().playerVehicleID:
            return
        else:
            ability = self._ABILITIES_SOUNDS.get(self.__equipment.name)
            eventType = b'start' if isActive else b'stop'
            event = ability.get(eventType)
            if event is None:
                return
            SoundGroups.g_instance.playSound2D(event)
            return

    def __playStunVoiceOver(self, isShown):
        vehicleID = avatar_getter.getPlayerVehicleID()
        if isShown and self.entity.health > 0 and vehicleID == self.entity.id:
            playStunAreaHunterVO()
        return
