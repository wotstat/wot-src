from account_helpers.AccountSettings import KEY_SETTINGS, KEY_NOTIFICATIONS, DEFAULT_VALUES
from events_core_client.account_settings import AccountEventSettingsHandler
from wt_settings import g_wt_config
WT_ACCOUNT_SETTINGS_KEY = b'WhiteTiger'
WTA_EXPIRY_DATE_KEY = b'expiryDate'
WTA_IS_INTRO_VIEWED_KEY = b'isIntroVideoViewed'
WTA_IS_OUTRO_VIDEO_VIEWED_KEY = b'isOutroVideoViewed'
WTA_SAVED_VEHICLE_CD_KEY = b'savedVehCD'
WTA_SAVED_HUNTER_VEHICLE_CD_KEY = b'savedHunterVehCD'
WTA_SAVED_BOSS_VEHICLE_CD_KEY = b'savedBossVehCD'
WTA_BOSS_BATTLE_COUNT_KEY = b'bossBattleCount'
WTA_HUNTER_BATTLE_COUNT_KEY = b'hunterBattleCount'
WTA_DEFAULT_SETTINGS = {WTA_IS_INTRO_VIEWED_KEY: False, 
   WTA_IS_OUTRO_VIDEO_VIEWED_KEY: False, 
   WTA_BOSS_BATTLE_COUNT_KEY: 0, 
   WTA_HUNTER_BATTLE_COUNT_KEY: 0, 
   WTA_SAVED_VEHICLE_CD_KEY: None, 
   WTA_SAVED_HUNTER_VEHICLE_CD_KEY: None, 
   WTA_SAVED_BOSS_VEHICLE_CD_KEY: None}

class WTAccountSettings(object):

    def __init__(self, eventController):
        self.__accSettings = AccountEventSettingsHandler(WT_ACCOUNT_SETTINGS_KEY, WTA_EXPIRY_DATE_KEY, eventController)
        return

    def init(self):
        DEFAULT_VALUES[KEY_SETTINGS].setdefault(WT_ACCOUNT_SETTINGS_KEY, WTA_DEFAULT_SETTINGS)
        DEFAULT_VALUES[KEY_NOTIFICATIONS].setdefault(WT_ACCOUNT_SETTINGS_KEY, WTA_DEFAULT_SETTINGS)
        return

    def migrateAccount(self):
        self.__accSettings.migrateAccount()
        return

    def setIntroViewed(self, status):
        self.__accSettings.setSetting(WTA_IS_INTRO_VIEWED_KEY, status)
        return

    def setOutroVideoViewed(self, status):
        self.__accSettings.setSetting(WTA_IS_OUTRO_VIDEO_VIEWED_KEY, status)
        return

    def saveVehicleCD(self, vehicleCD):
        if vehicleCD not in g_wt_config.getAllVehiclesData():
            return
        if g_wt_config.isHunterVehicle(vehicleCD):
            self.__accSettings.setSetting(WTA_SAVED_HUNTER_VEHICLE_CD_KEY, vehicleCD)
        elif g_wt_config.isBossVehicle(vehicleCD):
            self.__accSettings.setSetting(WTA_SAVED_BOSS_VEHICLE_CD_KEY, vehicleCD)
        self.__accSettings.setSetting(WTA_SAVED_VEHICLE_CD_KEY, vehicleCD)
        return

    def increaseBossBattleCount(self):
        self.__accSettings.setSetting(WTA_BOSS_BATTLE_COUNT_KEY, self.bossBattleCount + 1)
        return

    def increaseHunterBattleCount(self):
        self.__accSettings.setSetting(WTA_HUNTER_BATTLE_COUNT_KEY, self.hunterBattleCount + 1)
        return

    @property
    def isIntroViewed(self):
        return self.__accSettings.settings.get(WTA_IS_INTRO_VIEWED_KEY)

    @property
    def isOutroVideoViewed(self):
        return self.__accSettings.settings.get(WTA_IS_OUTRO_VIDEO_VIEWED_KEY)

    @property
    def savedVehicleCD(self):
        return self.__accSettings.settings.get(WTA_SAVED_VEHICLE_CD_KEY)

    @property
    def savedHunterVehicleCD(self):
        return self.__accSettings.settings.get(WTA_SAVED_HUNTER_VEHICLE_CD_KEY)

    @property
    def savedBossVehicleCD(self):
        return self.__accSettings.settings.get(WTA_SAVED_BOSS_VEHICLE_CD_KEY)

    @property
    def bossBattleCount(self):
        return self.__accSettings.settings.get(WTA_BOSS_BATTLE_COUNT_KEY)

    @property
    def hunterBattleCount(self):
        return self.__accSettings.settings.get(WTA_HUNTER_BATTLE_COUNT_KEY)

    @property
    def settings(self):
        return self.__accSettings.settings
