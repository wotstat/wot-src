from pve_battle_hud import getPveHudLogger, WidgetType
from visual_script.slot_types import SLOT_TYPE, arrayOf
from visual_script.dependency import dependencyImporter
from visual_script_client.pve_common import ClientBattleHUDWidgetSettings, PropertySlotSpec, SettingType
settings, = dependencyImporter(b'gui.battle_control.controllers.vse_hud_settings_ctrl.settings')
_logger = getPveHudLogger()

class SetProgressCounterSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.progress_counter.ProgressCounterClientModel
    _WIDGET_TYPE = WidgetType.PROGRESS_COUNTER
    _SETTING_TYPE = SettingType.ITEM
    _SETTINGS_CONFIG = [
     PropertySlotSpec(b'header', SLOT_TYPE.STR, required=True),
     PropertySlotSpec(b'icon', SLOT_TYPE.STR, editorData=[b'shield', b'swords', b'wave'], required=True)]


class SetEnemyListSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.enemy_list.EnemyListClientModel
    _WIDGET_TYPE = WidgetType.ENEMY_LIST
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG = [
     PropertySlotSpec(b'showSpottedIcon', SLOT_TYPE.BOOL, defaultValue=True),
     PropertySlotSpec(b'highlightElite', SLOT_TYPE.BOOL, defaultValue=False)]


class SetPrimaryObjectiveSettings(ClientBattleHUDWidgetSettings):
    _ICONS = [
     b'flagFailure', b'flagSuccess']
    _SETTINGS_MODEL = settings.primary_objective.PrimaryObjectiveClientModel
    _WIDGET_TYPE = WidgetType.PRIMARY_OBJECTIVE
    _SETTING_TYPE = SettingType.ITEM
    _SETTINGS_CONFIG = [
     PropertySlotSpec(b'header', SLOT_TYPE.STR),
     PropertySlotSpec(b'subheader', SLOT_TYPE.STR),
     PropertySlotSpec(b'startSound', SLOT_TYPE.SOUND),
     PropertySlotSpec(b'remindTimers', arrayOf(SLOT_TYPE.INT)),
     PropertySlotSpec(b'remindSound', SLOT_TYPE.SOUND),
     PropertySlotSpec(b'countdownTimer', SLOT_TYPE.INT),
     PropertySlotSpec(b'countdownSound', SLOT_TYPE.SOUND),
     PropertySlotSpec(b'success', SLOT_TYPE.STR),
     PropertySlotSpec(b'successIcon', SLOT_TYPE.STR, editorData=_ICONS),
     PropertySlotSpec(b'successSound', SLOT_TYPE.SOUND),
     PropertySlotSpec(b'failure', SLOT_TYPE.STR),
     PropertySlotSpec(b'failureIcon', SLOT_TYPE.STR, editorData=_ICONS),
     PropertySlotSpec(b'failureSound', SLOT_TYPE.SOUND)]


class SetSecondaryObjectiveSettings(ClientBattleHUDWidgetSettings):
    _ICONS = [
     b'icon_info', b'icon_quest', b'icon_win']
    _SETTINGS_MODEL = settings.secondary_objective.SecondaryObjectiveClientModel
    _WIDGET_TYPE = WidgetType.SECONDARY_OBJECTIVE
    _SETTING_TYPE = SettingType.ITEM
    _SETTINGS_CONFIG = [
     PropertySlotSpec(b'header', SLOT_TYPE.STR),
     PropertySlotSpec(b'subheader', SLOT_TYPE.STR),
     PropertySlotSpec(b'startSound', SLOT_TYPE.SOUND),
     PropertySlotSpec(b'icon', SLOT_TYPE.STR, editorData=_ICONS),
     PropertySlotSpec(b'countdownTimer', SLOT_TYPE.INT),
     PropertySlotSpec(b'countdownSound', SLOT_TYPE.SOUND),
     PropertySlotSpec(b'successSound', SLOT_TYPE.SOUND),
     PropertySlotSpec(b'failureSound', SLOT_TYPE.SOUND)]


class SetAllyListSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.ally_list.AllyListClientModel
    _WIDGET_TYPE = WidgetType.ALLY_LIST
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG = [
     PropertySlotSpec(b'showFrags', SLOT_TYPE.BOOL, defaultValue=True),
     PropertySlotSpec(b'showVehicleTypeIcon', SLOT_TYPE.BOOL, defaultValue=False),
     PropertySlotSpec(b'highlightElite', SLOT_TYPE.BOOL, defaultValue=False)]


class SetMinimapSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.minimap.MinimapClientModel
    _WIDGET_TYPE = WidgetType.MINIMAP
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG = [
     PropertySlotSpec(b'showGrid', SLOT_TYPE.BOOL),
     PropertySlotSpec(b'canToggleFullMap', SLOT_TYPE.BOOL),
     PropertySlotSpec(b'minimumAnimationDuration', SLOT_TYPE.FLOAT, defaultValue=0.3),
     PropertySlotSpec(b'maximumAnimationDuration', SLOT_TYPE.FLOAT, defaultValue=0.9),
     PropertySlotSpec(b'animationDurationPerMeter', SLOT_TYPE.FLOAT, defaultValue=0.0005),
     PropertySlotSpec(b'minimumAnimationDistance', SLOT_TYPE.FLOAT, defaultValue=10.0)]


class SetPrebattleCountdownSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.countdown.CountdownClientModel
    _WIDGET_TYPE = WidgetType.COUNTDOWN
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG = [
     PropertySlotSpec(b'header', SLOT_TYPE.STR, required=True),
     PropertySlotSpec(b'subheader', SLOT_TYPE.STR),
     PropertySlotSpec(b'battleStartMessage', SLOT_TYPE.STR, required=True)]


class SetChatSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.chat.ChatModel
    _WIDGET_TYPE = WidgetType.CHAT
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG = [
     PropertySlotSpec(b'hide', SLOT_TYPE.BOOL, defaultValue=False)]


class SetBattleCommunicationsSettings(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.battle_communication.BattleCommunicationModel
    _WIDGET_TYPE = WidgetType.BATTLE_COMMUNICATION
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG = [
     PropertySlotSpec(b'hide', SLOT_TYPE.BOOL, defaultValue=False)]


class SetRespawnHUDSetting(ClientBattleHUDWidgetSettings):
    _SETTINGS_MODEL = settings.respawn_hud.RespawnHUDClientModel
    _WIDGET_TYPE = WidgetType.RESPAWN_HUD
    _SETTING_TYPE = SettingType.GENERAL
    _SETTINGS_CONFIG = [
     PropertySlotSpec(b'showLivesInAlliesList', SLOT_TYPE.BOOL),
     PropertySlotSpec(b'showLivesInTankPanel', SLOT_TYPE.BOOL),
     PropertySlotSpec(b'dynamicRespawnHeader', SLOT_TYPE.STR),
     PropertySlotSpec(b'dynamicRespawnSubheader', SLOT_TYPE.STR),
     PropertySlotSpec(b'dynamicRespawnSound', SLOT_TYPE.SOUND),
     PropertySlotSpec(b'staticRespawnHeader', SLOT_TYPE.STR),
     PropertySlotSpec(b'staticRespawnSubheader', SLOT_TYPE.STR),
     PropertySlotSpec(b'staticRespawnSound', SLOT_TYPE.SOUND),
     PropertySlotSpec(b'battleOverHeader', SLOT_TYPE.STR),
     PropertySlotSpec(b'battleOverSubheader', SLOT_TYPE.STR),
     PropertySlotSpec(b'battleOverSound', SLOT_TYPE.SOUND)]
