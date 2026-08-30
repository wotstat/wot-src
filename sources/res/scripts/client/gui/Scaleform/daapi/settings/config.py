from constants import HAS_DEV_RESOURCES, ARENA_GUI_TYPE, IS_DEVELOPMENT_BUILD
from gui.Scaleform.genConsts.TOOLTIPS_CONSTANTS import TOOLTIPS_CONSTANTS as _TOOLTIPS
from gui.shared.system_factory import registerScaleformBattlePackages, registerScaleformLobbyPackages, registerLobbyTooltipsBuilders, registerBattleTooltipsBuilders
_COMMON_RELEASE_PACKAGES = (b'gui.Scaleform.daapi.view.common',)
_COMMON_DEBUG_PACKAGES = (b'gui.development.ui.GUIEditor', b'gui.development.ui.uilogging', b'gui.development.ui')
_LOBBY_DEVELOPMENT_BUILD_PACKAGES = tuple()
_LOBBY_RELEASE_PACKAGES = (b'gui.Scaleform.daapi.view.lobby', b'gui.Scaleform.daapi.view.lobby.barracks', b'gui.Scaleform.daapi.view.lobby.boosters', b'gui.Scaleform.daapi.view.lobby.clans', b'gui.Scaleform.daapi.view.lobby.crewOperations', b'gui.Scaleform.daapi.view.lobby.customization', b'gui.Scaleform.daapi.view.lobby.cyberSport', b'gui.Scaleform.daapi.view.lobby.exchange', b'gui.Scaleform.daapi.view.lobby.fortifications', b'gui.Scaleform.daapi.view.lobby.hangar', b'gui.Scaleform.daapi.view.lobby.header', b'gui.Scaleform.daapi.view.lobby.messengerBar', b'gui.Scaleform.daapi.view.lobby.prb_windows', b'gui.Scaleform.daapi.view.lobby.profile', b'gui.Scaleform.daapi.view.lobby.rankedBattles', b'gui.Scaleform.daapi.view.lobby.epicBattle', b'gui.Scaleform.daapi.view.lobby.store', b'gui.Scaleform.daapi.view.lobby.storage', b'gui.Scaleform.daapi.view.lobby.techtree', b'gui.Scaleform.daapi.view.lobby.trainings', b'gui.Scaleform.daapi.view.lobby.vehicle_preview', b'gui.Scaleform.daapi.view.lobby.vehicle_compare', b'gui.Scaleform.daapi.view.lobby.notify_center', b'gui.Scaleform.daapi.view.login', b'messenger.gui.Scaleform.view.lobby', b'gui.Scaleform.daapi.view.lobby.missions.regular', b'gui.Scaleform.daapi.view.lobby.missions.personal', b'gui.Scaleform.daapi.view.bootcamp.lobby', b'gui.Scaleform.daapi.view.lobby.event_boards', b'gui.Scaleform.daapi.view.lobby.shop', b'gui.Scaleform.daapi.view.lobby.session_stats', b'gui.Scaleform.daapi.view.lobby.epicBattleTraining', b'gui.Scaleform.daapi.view.lobby.tank_setup', b'gui.Scaleform.daapi.view.lobby.mapbox', b'gui.Scaleform.daapi.view.lobby.veh_post_progression', b'gui.Scaleform.daapi.view.lobby.comp7', b'gui.Scaleform.daapi.view.lobby.collection')
_LOBBY_DEBUG_PACKAGES = (b'gui.development.ui.messenger.view.lobby', b'gui.development.ui.demo', b'gui.Scaleform.daapi.view.lobby.epicBattleTraining', b'gui.development.ui.gf_viewer')
_BATTLE_RELEASE_PACKAGES = (b'gui.Scaleform.daapi.view.battle.shared', b'messenger.gui.Scaleform.view.battle')
_BATTLE_DEBUG_PACKAGES = (b'gui.development.ui.battle',)
_LOBBY_TOOLTIPS_BUILDERS_PATHS = [
 (
  b'gui.Scaleform.daapi.view.tooltips.achievement_builders', _TOOLTIPS.ACHIEVEMENTS_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.battle_consumable_builder', (_TOOLTIPS.BATTLE_CONSUMABLE,)),
 (
  b'gui.Scaleform.daapi.view.tooltips.boosters_builders', _TOOLTIPS.BOOSTERS_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.bootcamp_builders', _TOOLTIPS.BOOTCAMP_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.common_builders', _TOOLTIPS.COMMON_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.customization_builders', _TOOLTIPS.CUSTOMIZATION_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.cybersport_builders', _TOOLTIPS.CYBER_SPORT_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.elen_builders', _TOOLTIPS.ELEN_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.epic_battle_builders', _TOOLTIPS.EPIC_BATTLE_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.fortifications_builder', _TOOLTIPS.FORT_SORTIE_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.personal_missions_builders', _TOOLTIPS.PERSONAL_MISSION_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.quests_builders', _TOOLTIPS.QUESTS_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.ranked_builders', _TOOLTIPS.RANKED_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.settings_builders', _TOOLTIPS.SETTINGS_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.tankman_builders', _TOOLTIPS.TANKMAN_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.crew_skin_builders', _TOOLTIPS.CREW_SKIN_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.crew_book_builders', _TOOLTIPS.CREW_BOOK_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.tutorial_builders', _TOOLTIPS.TUTORIAL_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.veh_cmp_builders', _TOOLTIPS.VEH_CMP_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.vehicle_builders', _TOOLTIPS.VEHICLES_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.blueprint_builders', _TOOLTIPS.BLUEPRINTS_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.vehicle_items_builders', _TOOLTIPS.VEHICLES_ITEMS_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.wgm_currency_builders', _TOOLTIPS.WGM_CURRENCY_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.marathon_builders', _TOOLTIPS.MARATHON_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.frontline_builders', _TOOLTIPS.FRONTLINE_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.session_stats_builders', _TOOLTIPS.SESSION_STATS_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.trade_in_builders', _TOOLTIPS.TRADE_IN_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.crew_bundle_builders', _TOOLTIPS.CREW_BUNDLE_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.demount_kit_builders', _TOOLTIPS.DEMOUNT_KIT_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.vehicle_collector_builders', _TOOLTIPS.VEHICLE_COLLECTOR_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.badges_builders', _TOOLTIPS.BADGES_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.battle_pass_builders', _TOOLTIPS.BATTLE_PASS_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.mapbox_lobby_builders', _TOOLTIPS.MAPBOX_LOBBY_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.account_completion_builders', _TOOLTIPS.ACCOUNT_COMPLETION_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.referral_program_builder', _TOOLTIPS.REFERRAL_PROGRAM_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.resource_well_builders', _TOOLTIPS.RESOURCE_WELL_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.comp7_lobby_builders', _TOOLTIPS.COMP7_LOBBY_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.wot_plus_builders', _TOOLTIPS.WOT_PLUS_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.early_access_builders', _TOOLTIPS.EARLY_ACCESS_LOBBY_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.storage_builders', _TOOLTIPS.STORAGE_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.bonuses_builders', _TOOLTIPS.BONUSES_SET)]
_LOBBY_DEBUG_TOOLTIPS_BUILDERS_PATHS = (
 (
  b'gui.development.ui.tooltips.development_builders', _TOOLTIPS.DEVELOPMENT_SET),)
_BATTLE_TOOLTIPS_BUILDERS_PATHS = (
 (
  b'gui.Scaleform.daapi.view.tooltips.settings_builders', _TOOLTIPS.SETTINGS_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.battle_opt_devices_builder', _TOOLTIPS.BATTLE_BLOCK_TOOLTIPS),
 (
  b'gui.Scaleform.daapi.view.tooltips.epic_in_battle_builders', _TOOLTIPS.EPIC_IN_BATTE_SET),
 (
  b'gui.Scaleform.daapi.view.tooltips.comp7_battle_builders', _TOOLTIPS.COMP7_BATTLE_SET))
ADVANCED_COMPLEX_TOOLTIPS = {b'#tooltips:hangar/ammo_panel/device/empty': b'equipment', 
   b'#tooltips:hangar/ammo_panel/equipment/empty': b'service', 
   b'#tooltips:equipment/empty': b'service', 
   b'#tooltips:XP': b'economyTankExperience', 
   b'#tooltips:hangar/ammo_panel/battleBooster/empty': b'instructions', 
   b'#tooltips:battleTypes/standart': b'gamemodeRandom', 
   b'#tooltips:battleTypes/unit': b'gamemodeTeam', 
   b'#tooltips:battleTypes/strongholds': b'gamemodeStronghold', 
   b'#tooltips:battleTypes/strongholds/disabled': b'gamemodeStronghold', 
   b'#tooltips:battleTypes/spec': b'gamemodeSpecial', 
   b'#tooltips:battleTypes/training': b'gamemodeTraining', 
   b'#tooltips:header/premium_buy': b'economyPremium', 
   b'#tooltips:header/premium_extend': b'economyPremium', 
   b'#tooltips:header/premium_upgrade': b'economyPremium'}
COMMON_PACKAGES = _COMMON_RELEASE_PACKAGES
_LOBBY_PACKAGES = _LOBBY_RELEASE_PACKAGES
BATTLE_PACKAGES = _BATTLE_RELEASE_PACKAGES
if HAS_DEV_RESOURCES:
    COMMON_PACKAGES += _COMMON_DEBUG_PACKAGES
    _LOBBY_PACKAGES += _LOBBY_DEBUG_PACKAGES
    BATTLE_PACKAGES += _BATTLE_DEBUG_PACKAGES
    _LOBBY_TOOLTIPS_BUILDERS_PATHS += _LOBBY_DEBUG_TOOLTIPS_BUILDERS_PATHS
elif IS_DEVELOPMENT_BUILD:
    _LOBBY_PACKAGES += _LOBBY_DEVELOPMENT_BUILD_PACKAGES
BATTLE_PACKAGES_BY_DEFAULT = BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.classic',)
registerScaleformLobbyPackages(_LOBBY_PACKAGES)
registerScaleformBattlePackages(ARENA_GUI_TYPE.EVENT_BATTLES, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.event',))
registerScaleformBattlePackages(ARENA_GUI_TYPE.RANKED, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.ranked',))
registerScaleformBattlePackages(ARENA_GUI_TYPE.EPIC_RANDOM, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.epic_random',))
registerScaleformBattlePackages(ARENA_GUI_TYPE.EPIC_RANDOM_TRAINING, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.epic_random',))
registerScaleformBattlePackages(ARENA_GUI_TYPE.EPIC_BATTLE, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.epic',))
registerScaleformBattlePackages(ARENA_GUI_TYPE.EPIC_TRAINING, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.epic',))
registerScaleformBattlePackages(ARENA_GUI_TYPE.SORTIE_2, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.stronghold',))
registerScaleformBattlePackages(ARENA_GUI_TYPE.FORT_BATTLE_2, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.stronghold',))
registerScaleformBattlePackages(ARENA_GUI_TYPE.BOOTCAMP, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.bootcamp.battle',))
registerScaleformBattlePackages(ARENA_GUI_TYPE.MAPS_TRAINING, (b'messenger.gui.Scaleform.view.battle', b'gui.Scaleform.daapi.view.battle.maps_training') + (_BATTLE_DEBUG_PACKAGES if HAS_DEV_RESOURCES else ()))
registerScaleformBattlePackages(ARENA_GUI_TYPE.COMP7, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.comp7',))
registerScaleformBattlePackages(ARENA_GUI_TYPE.TOURNAMENT_COMP7, BATTLE_PACKAGES + (b'gui.Scaleform.daapi.view.battle.comp7',))
registerBattleTooltipsBuilders(_BATTLE_TOOLTIPS_BUILDERS_PATHS)
registerLobbyTooltipsBuilders(_LOBBY_TOOLTIPS_BUILDERS_PATHS)
