from shared_utils import CONST_CONTAINER

class SoundEffectsId(CONST_CONTAINER):
    SPEND_DEFAULT_SOUND = b'wwspend_default_currency'
    SPEND_CREDITS_GOLD = b'wwspend_credits_and_gold'
    SPEND_CREDITS = b'wwspend_credits'
    SPEND_GOLD = b'wwspend_gold'
    SPEND_CRYSTAL = b'wwspend_crystal'
    SPEND_EVENT_COIN = b'wwspend_event_coin'
    EARN_DEFAULT_SOUND = b'wwearn_default_currency'
    EARN_CREDITS_GOLD = b'wwearn_credits_and_gold'
    EARN_CREDITS = b'wwearn_credits'
    EARN_GOLD = b'wwearn_gold'
    EARN_CRYSTAL = b'wwearn_crystal'
    EARN_EVENT_COIN = b'wwearn_event_coin'
    EARN_EQUIP_COIN = b'wwearn_equip_coin'
    TRANSPORT_ENTER = b'wwtransport_enter'
    TRANSPORT_EXIT = b'wwtransport_exit'
    TRANSPORT_FIRST_STEP = b'wwtransport_first_step'
    TRANSPORT_NEXT_STEP = b'wwtransport_next_step'
    TRANSPORT_APPROVE = b'wwtransport_approve'
    ACTIVATE_REQUISITION = b'wwactivate_requisition'
    ACTIVATE_EVACUATION = b'wwactivate_evacuation'
    ACTIVATE_HEAVY_TRUCKS = b'wwactivate_heavyTrucks'
    ACTIVATE_MILITARY_MANEUVERS = b'wwactivate_militaryManeuvers'
    ACTIVATE_ADDITIONAL_BRIEFING = b'wwactivate_additionalBriefing'
    ACTIVATE_TACTICAL_TRAINING = b'wwactivate_tacticalTraining'
    ACTIVATE_BATTLE_PAYMENTS = b'wwactivate_battlePayments'
    ACTIVATE_SPECIALMISSION = b'wwactivate_specialMission'
    END_BUILDING_PROCESS_POSTFIX = b'_endPrcBld'
    ACTIVATE_DEFENCE_PERIOD = b'wwactivate_defencePeriod'
    DEACTIVATE_DEFENCE_PERIOD = b'wwdeactivate_defencePeriod'
    ENEMY_DIRECTION_SELECTED = b'wwenemyDirection_selected'
    ENEMY_DIRECTION_HOVER = b'wwenemyDirection_hover'
    MY_DIRECTION_SELECTED = b'wwmyDirection_selected'
    FORT_CLAN_WAR_DECLARED = b'wwfortClanWar_declared'
    BATTLE_ROOM_TIMER_ALERT = b'wwbattleRoom_timerAlert'
    _FORT_CLAN_WAR_RESULT_PREFIX = b'wwfortClanWarResult_'
    CS_ANIMATION_LEAGUE_UP = b'wwcs_animation_league_up'
    CS_ANIMATION_LEAGUE_DOWN = b'wwcs_animation_league_down'
    CS_ANIMATION_DIVISION_UP = b'wwcs_animation_division_up'
    CS_ANIMATION_DIVISION_UP_ALT = b'wwcs_animation_division_up_alt'
    CS_ANIMATION_DIVISION_DOWN = b'wwcs_animation_division_down'
    DYN_SQUAD_STARTING_DYNAMIC_PLATOON = b'wwdyn_squad_starting_dynamic_platoon'
    SELECT_RADIAL_BUTTON = b'wwselect_radial_button'
    RUDY_DOG = b'wwrody_dog'

    @classmethod
    def getEndBuildingProcess(cls, buildingID):
        result = b'ww%s%s' % (buildingID, cls.END_BUILDING_PROCESS_POSTFIX)
        return result

    @classmethod
    def getFortClanWarResult(cls, battleResult):
        result = b'%s%s' % (cls._FORT_CLAN_WAR_RESULT_PREFIX, battleResult)
        return result
