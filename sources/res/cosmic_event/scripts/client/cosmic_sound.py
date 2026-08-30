import WWISE
from typing import TYPE_CHECKING
from debug_utils import LOG_ERROR
from sound_gui_manager import CommonSoundSpaceSettings

def play2DSoundEvent(name):
    import SoundGroups
    return SoundGroups.g_instance.playSound2D(name)


def play3DSoundEvent(name, point):
    import SoundGroups
    return SoundGroups.g_instance.playSoundPos(name, point)


def playVoiceover(eventName):
    from gui.battle_control import avatar_getter
    soundNotifications = avatar_getter.getSoundNotifications()
    if soundNotifications:
        soundNotifications.play(eventName)
    else:
        LOG_ERROR((b'[COSMIC] Error on playing voiceover event {}').format(eventName))
    return


def setCutSceneSoundGlobalEvent(state):
    WWISE.WW_eventGlobal(state)
    return


if TYPE_CHECKING:
    from Math import Vector3

class CosmicHangarSounds(object):
    _COSMIC_PRB_ENTER = b'ev_cosmic_lobby_enter'
    _COSMIC_PRB_EXIT = b'ev_cosmic_lobby_exit'
    _COSMIC_BATTLE_RESULTS = b'ev_cosmic_music_pbs'

    @classmethod
    def playCosmicPrbEnter(cls):
        play2DSoundEvent(cls._COSMIC_PRB_ENTER)
        return

    @classmethod
    def playCosmicPrbExit(cls):
        play2DSoundEvent(cls._COSMIC_PRB_EXIT)
        return

    @classmethod
    def playCosmicBattleResultsEnter(cls):
        play2DSoundEvent(cls._COSMIC_BATTLE_RESULTS)
        return

    class CosmicProgression(object):
        COSMIC_RTPC_PROGRESSION = b'RTPC_ext_cosmic_lobby_progress'
        _COSMIC_LOBBY_FIRST_ENTER = b'ev_cosmic_vo_lobby_first_enter'
        _COSMIC_PROGRESSION_RULE_TO_SOUND = (
         (
          (lambda stage: 0 <= stage < 3), b'ev_cosmic_vo_lobby_progression_0_3'),
         (
          (lambda stage: 3 <= stage <= 6), b'ev_cosmic_vo_lobby_progression_3_7'),
         (
          (lambda stage: 7 <= stage < 10), b'ev_cosmic_vo_lobby_progression_7_10'),
         (
          (lambda stage: stage == 10), b'ev_cosmic_vo_lobby_progression_completed'))
        _COSMIC_PROGRESSION_AMBIENT_START = b'ev_cosmic_hangar_progress_enter'
        _COSMIC_PROGRESSION_AMBIENT_STOP = b'ev_cosmic_hangar_progress_exit'

        @classmethod
        def getSoundObject(cls, currentStage):
            import SoundGroups
            for isRuleMatched, sound in cls._COSMIC_PROGRESSION_RULE_TO_SOUND:
                if isRuleMatched(currentStage):
                    return SoundGroups.g_instance.getSound2D(sound)

            LOG_ERROR((b'[COSMIC_SOUND]: unable to find sound object for {} progression stage').format(currentStage))
            return

        @classmethod
        def playAmbient(cls):
            play2DSoundEvent(cls._COSMIC_PROGRESSION_AMBIENT_START)
            return

        @classmethod
        def stopAmbient(cls):
            play2DSoundEvent(cls._COSMIC_PROGRESSION_AMBIENT_STOP)
            return

        @classmethod
        def getProgressionFirstEnterSound(cls):
            import SoundGroups
            return SoundGroups.g_instance.getSound2D(cls._COSMIC_LOBBY_FIRST_ENTER)


class CosmicBattleSounds(object):
    START_BATTLE = b'ev_cosmic_vo_gameplay_start_battle'
    KILL = b'ev_cosmic_vo_gameplay_enemy_destroyed'
    CORAL_LOSE_PC = b'ev_cosmic_coral_ray_out_PC'
    CORAL_LOSE_NPC = b'ev_cosmic_coral_ray_out_NPC'
    CORAL_RESEARCH_DONE_PC = b'ev_cosmic_coral_scanning_end_PC'
    CORAL_RESEARCH_DONE_NPC = b'ev_cosmic_coral_ray_out_NPC'
    CORAL_SPAWNED_STATE_TRIGGER = b'ev_cosmic_music_object_active'
    CORAL_DISAPPEARED_STATE_TRIGGER = b'ev_cosmic_music_object_inactive'
    _SCORE_NOTIFICATION = b'ev_cosmic_score_notification'
    _SPECIAL_HINT = b'ev_cosmic_special_hint'
    _KILL_STREAK_NOTIFICATION = {2: b'ev_cosmic_x2_kill_hint', 
       3: b'ev_cosmic_x3_kill_hint', 
       4: b'ev_cosmic_x4_kill_hint'}
    _ABILITY_PICK_UP_NOTIFICATION = b'ev_cosmic_pickup_notification'
    _ENEMY_KILLED_NOTIFICATION = b'ev_cosmic_enemy_killed'
    _ABILITY_PICK_UP = b'ev_cosmic_ability_pickup'
    _ABILITY_PICK_UP_MUSIC = b'ev_cosmic_music_pickup'
    _BATTLE_PERIOD_MUSIC = b'ev_cosmic_music_start_battle'
    _AFTERBATTLE_PERIOD_MUSIC = b'ev_cosmic_music_end_battle'
    _RAMMING = b'ev_cosmic_tank_ram'
    _DRON_APPEAR_3D = b'ev_cosmic_ability_drone_appear'
    _DRON_DISAPPEAR_3D = b'ev_cosmic_ability_drone_disappear'
    _BOARD_JUMP_3D = b'ev_cosmic_booster_jump'
    _GEYSER_SPLASH_3D = b'ev_cosmic_geyser_big'
    _CORALL_TIMER_RTPC_EVENT = b'RTPC_ext_cosmic_corall_timer'
    _AFTER_BATTLE_RESULTS_VOICES = (b'ev_cosmic_vo_gameplay_finish_battle_first_place', b'ev_cosmic_vo_gameplay_finish_battle_other_place')

    class ScanningZone(object):
        SCANNING_ZONE_PREPARING = b'ev_cosmic_vo_gameplay_scan_prepare'
        SCANNING_ZONE_FINAL_PREPARING = b'ev_cosmic_vo_gameplay_scan_prepare_final'
        _STATE_GROUP = b'STATE_ev_cosmic_object'
        _ACTIVE_STATE_VAL = b'STATE_ev_cosmic_object_active_on'
        _INACTIVE_STATE_VAL = b'STATE_ev_cosmic_object_active_off'
        _FINAL_CYCLE = b'ev_cosmic_coda'

        @classmethod
        def setActive(cls, isLast):
            WWISE.WW_setState(cls._STATE_GROUP, cls._ACTIVE_STATE_VAL)
            if isLast:
                play2DSoundEvent(cls._FINAL_CYCLE)
            return

        @classmethod
        def setInactive(cls, isLast):
            cls.switchInactiveState()
            return

        @classmethod
        def switchInactiveState(cls):
            WWISE.WW_setState(cls._STATE_GROUP, cls._INACTIVE_STATE_VAL)
            return

    class Announcements(object):
        PICK_UP_ANNOUNCE_START = b'ev_cosmic_ability_announce'
        PICK_UP_ANNOUNCE_END = b'ev_cosmic_ability_appear'
        ABILITIES_SPAWNED = b'ev_cosmic_vo_gameplay_booster_spawn'
        _STEP = b'ev_cosmic_timer_1shot'
        FINISHED = b'ev_cosmic_timer_last'

        @classmethod
        def playStep(cls):
            play2DSoundEvent(cls._STEP)
            return

        @classmethod
        def playFinish(cls):
            play2DSoundEvent(cls.FINISHED)
            return

    class Abilities(object):
        _NOT_READY = b'ev_cosmic_ability_not_ready'
        _ACTIVATED = b'ev_cosmic_ability_apply'
        _BOOSTER_ACTIVATED = b'ev_cosmic_ability_booster'
        _HOOK_SHOT_ACTIVATED = b'ev_cosmic_ability_overcharge_shot_start'
        _HOOK_SHOT_ELAPSED = b'ev_cosmic_ability_overcharge_shot_stop'
        _INSTALLED_ABILITY_ACTIVATED = b'ev_cosmic_ability_aim_charge'
        _INSTALLED_ABILITY_CANCELED = b'ev_cosmic_ability_aim_cancel'
        _RESPAWN_PROTECTION_ACTIVATED = b'ev_cosmic_ability_respawn_protection_start'
        _RESPAWN_PROTECTION_ELAPSED = b'ev_cosmic_ability_respawn_protection_stop'
        _POWER_SHOT_ACTIVATED = b'ev_cosmic_ability_superShot_start'
        _POWER_SHOT_ELAPSED = b'ev_cosmic_ability_superShot_stop'
        _STUN_SHOT_ACTIVATED = b'ev_cosmic_ability_superShot_start'
        _STUN_SHOT_ELAPSED = b'ev_cosmic_ability_superShot_stop'

        @classmethod
        def playActivated(cls):
            play2DSoundEvent(cls._ACTIVATED)
            return

        @classmethod
        def playNotReady(cls):
            play2DSoundEvent(cls._NOT_READY)
            return

        @classmethod
        def playBoosterActivated(cls):
            play2DSoundEvent(cls._BOOSTER_ACTIVATED)
            return

        @classmethod
        def playHookShotActivated(cls):
            play2DSoundEvent(cls._HOOK_SHOT_ACTIVATED)
            return

        @classmethod
        def playHookShotElapsed(cls):
            play2DSoundEvent(cls._HOOK_SHOT_ELAPSED)
            return

        @classmethod
        def handleInstalledAbility(cls, isActive):
            if isActive:
                play2DSoundEvent(cls._INSTALLED_ABILITY_ACTIVATED)
            else:
                play2DSoundEvent(cls._INSTALLED_ABILITY_CANCELED)
            return

        @classmethod
        def playRespawnProtectionActivated(cls):
            play2DSoundEvent(cls._RESPAWN_PROTECTION_ACTIVATED)
            return

        @classmethod
        def playRespawnProtectionElapsed(cls):
            play2DSoundEvent(cls._RESPAWN_PROTECTION_ELAPSED)
            return

        @classmethod
        def playPowerShotActivated(cls):
            play2DSoundEvent(cls._POWER_SHOT_ACTIVATED)
            return

        @classmethod
        def playPowerShotElapsed(cls):
            play2DSoundEvent(cls._POWER_SHOT_ELAPSED)
            return

        @classmethod
        def playStunShotActivated(cls):
            play2DSoundEvent(cls._STUN_SHOT_ACTIVATED)
            return

        @classmethod
        def playStunShotElapsed(cls):
            play2DSoundEvent(cls._STUN_SHOT_ELAPSED)
            return

    @classmethod
    def setTimerSound(cls, time):
        WWISE.WW_setRTPCBus(cls._CORALL_TIMER_RTPC_EVENT, time)
        return

    @classmethod
    def playScoreNotification(cls):
        play2DSoundEvent(cls._SCORE_NOTIFICATION)
        return

    @classmethod
    def playSpecialHint(cls):
        play2DSoundEvent(cls._SPECIAL_HINT)
        return

    @classmethod
    def playKillStreak(cls, killStreak):
        if killStreak > 1:
            event = cls._KILL_STREAK_NOTIFICATION.get(killStreak, b'ev_cosmic_x4_kill_hint')
            play2DSoundEvent(event)
        return

    @classmethod
    def playAbilityPickup(cls):
        play2DSoundEvent(cls._ABILITY_PICK_UP_NOTIFICATION)
        play2DSoundEvent(cls._ABILITY_PICK_UP_MUSIC)
        play2DSoundEvent(cls._ABILITY_PICK_UP)
        return

    @classmethod
    def playEnemyKilled(cls):
        play2DSoundEvent(cls._ENEMY_KILLED_NOTIFICATION)
        return

    @classmethod
    def startBattlePeriodMusic(cls):
        play2DSoundEvent(cls._BATTLE_PERIOD_MUSIC)
        return

    @classmethod
    def startAfterBattlePeriodMusic(cls):
        play2DSoundEvent(cls._AFTERBATTLE_PERIOD_MUSIC)
        return

    @classmethod
    def playAfterBattleResultVoice(cls, playerPositionInRankedTable):
        if playerPositionInRankedTable == 1:
            playVoiceover(cls._AFTER_BATTLE_RESULTS_VOICES[0])
        elif playerPositionInRankedTable > 1:
            playVoiceover(cls._AFTER_BATTLE_RESULTS_VOICES[1])
        return

    @classmethod
    def playRammingSound(cls, point):
        play3DSoundEvent(cls._RAMMING, point)
        return

    @classmethod
    def playDronDisappear(cls, point):
        play3DSoundEvent(cls._DRON_DISAPPEAR_3D, point)
        return

    @classmethod
    def playDronAppear(cls, point):
        play3DSoundEvent(cls._DRON_APPEAR_3D, point)
        return

    @classmethod
    def playBoardJump(cls, point):
        play3DSoundEvent(cls._BOARD_JUMP_3D, point)
        return

    @classmethod
    def playGeyserSplash(cls, point):
        play3DSoundEvent(cls._GEYSER_SPLASH_3D, point)
        return


class IntroVideoSound(object):
    START = b'ev_cosmic_intro_video_start'
    PAUSE = b'ev_cosmic_intro_video_pause'
    RESUME = b'ev_cosmic_intro_video_resume'
    STOP = b'ev_cosmic_intro_video_stop'


class CosmicVideoState(object):
    STATE_GROUP = b'STATE_video_overlay'
    OFF = b'STATE_video_overlay_off'
    ON = b'STATE_video_overlay_on'


COSMIC_VIDEO_VIEW_SOUND_SPACE = CommonSoundSpaceSettings(name=b'COSMIC_VIDEO_VIEW', entranceStates={(CosmicVideoState.STATE_GROUP): (CosmicVideoState.ON)}, exitStates={(CosmicVideoState.STATE_GROUP): (CosmicVideoState.OFF)}, persistentSounds=(), stoppableSounds=(), priorities=(), autoStart=True, enterEvent=b'', exitEvent=b'')
