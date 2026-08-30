import imghdr, itertools, sys, inspect, uuid, struct
from collections import namedtuple
import BigWorld, AccountCommands, Settings, constants
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR, LOG_DEBUG, LOG_WARNING
from gui.impl import backport
from gui.impl.gen import R
from helpers import getLanguageCode, i18n
from items import vehicles as vehs_core
from account_helpers import getAccountDatabaseID
from account_helpers.AccountSettings import AccountSettings
from avatar_helpers import getAvatarDatabaseID, getAvatarSessionID
SHELLS_COUNT_PROP_NAME = b'shellsCount'
SHELLS_BURST_COUNT_PROP_NAME = b'shellsBurstCount'
SHELLS_FLAME_BURST_COUNT_PROP_NAME = b'shellsFlameBurstCount'
RELOAD_TIME_SECS_PROP_NAME = b'reloadTimeSecs'
RELOAD_TIME_PROP_NAME = b'reloadTime'
RELOAD_MAGAZINE_TIME_PROP_NAME = b'reloadMagazineTime'
SHELL_RELOADING_TIME_PROP_NAME = b'shellReloadingTime'
DISPERSION_RADIUS_PROP_NAME = b'dispersionRadius'
SHOT_DISPERSION_ANGLE = b'shotDispersionAngle'
DISPERSION_RADIUS = b'dispertionRadius'
AIMING_TIME_PROP_NAME = b'aimingTime'
PIERCING_POWER_PROP_NAME = b'piercingPower'
DAMAGE_PROP_NAME = b'damage'
SHOT_SPEED_ACCELERATED_PROP_NAME = b'shotSpeedAccelerated'
DISTANCE_DAMAGE_PROP_NAME = b'distanceDamage'
SHELLS_PROP_NAME = b'shells'
STUN_DURATION_PROP_NAME = b'stunDuration'
AUTO_RELOAD_PROP_NAME = b'autoReloadTime'
CLIP_VEHICLES_PROP_NAME = b'clipVehicles'
UNICHARGED_VEHICLES_PROP_NAME = b'uniChargedVehicles'
VEHICLES_PROP_NAME = b'vehicles'
CLIP_VEHICLES_CD_PROP_NAME = b'clipVehiclesCD'
MAX_STEERING_LOCK_ANGLE = b'maxSteeringLockAngle'
BURST_FIRE_RATE = b'burstFireRate'
BURST_TIME_INTERVAL = b'burstTimeInterval'
BURST_COUNT = b'burstCount'
BURST_SIZE = b'burstSize'
CLIP_FIRE_RATE = b'clipFireRate'
WHEELED_SWITCH_ON_TIME = b'wheeledSwitchOnTime'
WHEELED_SWITCH_OFF_TIME = b'wheeledSwitchOffTime'
WHEELED_SWITCH_TIME = b'wheeledSwitchTime'
WHEELED_SPEED_MODE_SPEED = b'wheeledSpeedModeSpeed'
TURBOSHAFT_SWITCH_ON_TIME = b'turboshaftSwitchOnTime'
TURBOSHAFT_SWITCH_OFF_TIME = b'turboshaftSwitchOffTime'
TURBOSHAFT_SWITCH_TIME = b'turboshaftSwitchTime'
TURBOSHAFT_SPEED_MODE_SPEED = b'turboshaftSpeedModeSpeed'
TURBOSHAFT_ENGINE_POWER = b'turboshaftEnginePower'
TURBOSHAFT_INVISIBILITY_STILL_FACTOR = b'turboshaftInvisibilityStillFactor'
TURBOSHAFT_INVISIBILITY_MOVING_FACTOR = b'turboshaftInvisibilityMovingFactor'
ROCKET_ACCELERATION_ENGINE_POWER = b'rocketAccelerationEnginePower'
ROCKET_ACCELERATION_SPEED_LIMITS = b'rocketAccelerationSpeedLimits'
ROCKET_ACCELERATION_REUSE_AND_DURATION = b'rocketAccelerationReuseAndDuration'
THERMAL_VISION_REUSE_AND_DURATION = b'thermalVisionReuseAndDuration'
THERMAL_VISION_DISTANCE = b'thermalVisionDistance'
THERMAL_VISION_RELOAD_TIME = b'thermalVisionReloadTime'
THERMAL_VISION_OBSERVE_TIME = b'thermalVisionObserveTime'
DUAL_GUN_CHARGE_TIME = b'chargeTime'
DUAL_GUN_RATE_TIME = b'rateTime'
DUAL_ACCURACY_AFTER_SHOT_DISPERSION_ANGLE = b'dualAccuracyAfterShotDispersionAngle'
DUAL_ACCURACY_COOLING_DELAY = b'dualAccuracyCoolingDelay'
RELOAD_TIME_PER_SECOND = b'reloadTimePerSecond'
AVG_DAMAGE_PER_SECOND = b'avgDamagePerSecond'
AUTOSHOOT_FLAME_CHANGE_SHELL_TIME = b'autoShootFlameChangeShellTime'
AUOTSHOOT_FLAME_OVERHEAT_COOLING_TIME = b'autoShootFlameOverheatCoolingTime'
AUTOSHOOT_FIRE_UNTIL_OVERHEAT_TIME = b'autoShootFireUntilOverheatTime'
FLAME_MAX_DISTANCE = b'flameMaxDistance'
GUN_RELOADING_TYPE = b'gunReloadingType'
CHASSIS_REPAIR_TIME = b'chassisRepairTime'
CHASSIS_REPAIR_TIME_YOH = b'chassisRepairTimeYoh'
CHASSIS_REPAIR_TIME_MULTITRACK_SEQUENT = b'chassisRepairTimeMultiTrackSequent'
CHASSIS_REPAIR_TIME_MULTITRACK_PARALLEL = b'chassisRepairTimeMultiTrackParallel'
GUN_CAN_BE_CLIP = 1
GUN_CLIP = 2
GUN_NORMAL = 4
GUN_CAN_BE_AUTO_RELOAD = 5
GUN_AUTO_RELOAD = 6
GUN_CAN_BE_DUAL_GUN = 7
GUN_DUAL_GUN = 8
GUN_CAN_BE_AUTOSHOOT_FLAME = 9
GUN_AUTOSHOOT_FLAME = 10
GUN_CLIP_DUAL_GUN = 11
GUN_CAN_BE_CLIP_DUAL_GUN = 12
GUN_CAN_BE_AUTO_RELOAD_DUAL_GUN = 13
GUN_AUTO_RELOAD_DUAL_GUN = 14
GUN_CAN_BE_AUTOSHOOT = 15
GUN_AUTOSHOOT = 16
GUN_DUAL_ACCURACY = 17
GUN_CAN_HAVE_DUAL_ACCURACY = 18
GUN_DUAL_GUN_DUAL_ACCURACY = 19
GUN_CAN_BE_DUAL_GUN_DUAL_ACCURACY = 20
EXTRA_MODULE_INFO = b'extraModuleInfo'
FIELD_SPECIALIZATIONS = b'specs'
FIELD_HIGHLIGHT_TYPE = b'highlightType'
_FLASH_OBJECT_SYS_ATTRS = (b'isPrototypeOf', b'propertyIsEnumerable', b'hasOwnProperty')
ValidationResult = namedtuple(b'ValidationResult', [
 b'isValid',
 b'reason'])

def flashObject2Dict(obj):
    if hasattr(obj, b'children'):
        filtered = itertools.ifilter((lambda (x, y): x not in _FLASH_OBJECT_SYS_ATTRS), obj.children.iteritems())
        return dict((k, flashObject2Dict(v)) for k, v in filtered)
    return obj


def code2str(code):
    if code == AccountCommands.RES_SUCCESS:
        return b'Request succedded'
    if code == AccountCommands.RES_STREAM:
        return b'Stream is sent to the client'
    if code == AccountCommands.RES_CACHE:
        return b'Data is taken from cache'
    if code == AccountCommands.RES_FAILURE:
        return b'Unknown reason'
    if code == AccountCommands.RES_WRONG_ARGS:
        return b'Wrong arguments'
    if code == AccountCommands.RES_NON_PLAYER:
        return b'Account become non player'
    if code == AccountCommands.RES_SHOP_DESYNC:
        return b'Shop cache is desynchronized'
    if code == AccountCommands.RES_COOLDOWN:
        return b'Identical requests cooldown'
    if code == AccountCommands.RES_HIDDEN_DOSSIER:
        return b'Player dossier is hidden'
    if code == AccountCommands.RES_CENTER_DISCONNECTED:
        return b'Dossiers are unavailable'
    return b'Unknown error code'


def isVehicleObserver(vehTypeCompDescr):
    if vehTypeCompDescr is not None:
        _, nation_id, item_id_within_nation = vehs_core.parseIntCompactDescr(vehTypeCompDescr)
        return b'observer' in vehs_core.g_cache.vehicle(nation_id, item_id_within_nation).tags
    else:
        return False


def class_for_name(module_name, class_name):
    __import__(module_name)
    m = sys.modules[module_name]
    c = getattr(m, class_name)
    if not inspect.isclass(c):
        LOG_ERROR(b'%s - is not a class, check module path or className' % class_name)
        return None
    else:
        return c


def sortByFields(fields, sequence, valueGetter=dict.get):

    def comparator(x, y):
        for field, order in fields:
            fieldValueX = valueGetter(x, field)
            fieldValueY = valueGetter(y, field)
            if fieldValueX != fieldValueY:
                if order:
                    return cmp(fieldValueX, fieldValueY)
                return cmp(fieldValueY, fieldValueX)

        return 0

    return sorted(sequence, cmp=comparator)


def roundByModulo(value, rate):
    left = value % rate
    if left > 0:
        value += rate - left
    return value


_STR_CASING_OPTIONS = {b'el': (8, 1, 0), 
   b'ro': (24, 1, 0), 
   b'tr': (31, 1, 0)}
_REPLACEMENTS = {b'el': (u'\u0386\u0388\u038a\u0389\u038e\u038c\u038f', u'\u0391\u0395\u0399\u0397\u03a5\u039f\u03a9')}

def changeStringCasing(string, isUpper):
    langID = getLanguageCode()
    try:
        if not isinstance(string, unicode):
            string = string.decode(b'utf-8')
        if langID is not None:
            langID = str(langID).lower()
            if langID in _STR_CASING_OPTIONS:
                plID, slID, sortOrder = _STR_CASING_OPTIONS[langID]
                string = BigWorld.changeStringCasing(string, plID, slID, sortOrder, isUpper)
            else:
                string = string.upper() if isUpper else string.lower()
            if langID in _REPLACEMENTS:
                for wrong, right in zip(*_REPLACEMENTS[langID]):
                    string = string.replace(wrong, right)

    except Exception:
        LOG_CURRENT_EXCEPTION()

    return string


def toLower(string):
    return changeStringCasing(string, False)


def toUpper(string):
    return changeStringCasing(string, True)


def copyToClipboard(text):
    BigWorld.copyToClipboard(unicode(text, b'utf-8', errors=b'ignore'))
    LOG_DEBUG(b'Text has been copied to the clipboard', text)
    return


class SettingRecord(dict):

    def __setattr__(self, name, value):
        if self:
            raise AttributeError(b"can't set attribute")
        self.__setitem__(name, value)
        return

    def __getattr__(self, item):
        if item in self:
            return self.__getitem__(item)
        return dict.__getattribute__(self, item)

    def _asdict(self):
        return dict(self)

    def __repr__(self):
        return b'%s(%s)' % (self.__class__.__name__, super(SettingRecord, self).__repr__())


class SettingRootRecord(SettingRecord):

    @classmethod
    def load(cls):
        try:
            return cls(**AccountSettings.getSettings(cls._getSettingName()))
        except Exception:
            LOG_ERROR((b'There is error while unpacking {} settings').format(cls._getSettingName()), AccountSettings.getSettings(cls._getSettingName()))
            LOG_CURRENT_EXCEPTION()
            return

        return

    def save(self):
        return AccountSettings.setSettings(self._getSettingName(), self._asdict())

    @classmethod
    def _getSettingName(cls):
        raise NotImplementedError
        return


def mapTextureToTheMemory(textureData, uniqueID=None, temp=True):
    if textureData and imghdr.what(None, textureData) is not None:
        uniqueID = str(uniqueID or uuid.uuid4())
        if temp:
            BigWorld.addTempScaleformTexture(uniqueID, textureData)
        else:
            BigWorld.addScaleformTexture(uniqueID, textureData)
        return uniqueID
    LOG_WARNING(b'There is invalid data for the memory mapping', textureData, uniqueID)
    return


def removeTextureFromMemory(textureID):
    BigWorld.eraseScaleformTexture(textureID)
    return


def getImageSize(imageData):
    width, height = (None, None)
    if imageData:
        imgType = imghdr.what(None, imageData)
        if imgType == b'png':
            check = struct.unpack(b'>i', imageData[4:8])[0]
            if check != 218765834:
                return
            width, height = struct.unpack(b'>ii', imageData[16:24])
        elif imgType == b'gif':
            width, height = struct.unpack(b'<HH', imageData[6:10])
        elif imgType == b'jpeg':
            LOG_WARNING(b'JPEG image type is not supported')
            width, height = (None, None)
    return (
     width, height)


def showInvitationInWindowsBar():
    try:
        BigWorld.WindowsNotifier.onInvitation()
    except AttributeError:
        LOG_CURRENT_EXCEPTION()

    return


def getPlayerDatabaseID():
    return getAccountDatabaseID() or getAvatarDatabaseID()


def getPlayerName():
    return getattr(BigWorld.player(), b'name', b'')


def avg(devidend, devider):
    if devider > 0:
        return float(devidend) / devider
    return 0


def weightedAvg(*args):
    values, weights = args
    valSum = 0
    weightSum = 0
    itemsCount = len(values)
    for i in range(itemsCount):
        weight = weights[i]
        valSum += values[i] * weight
        weightSum += weight

    if weightSum != 0:
        return float(valSum) / weightSum
    return 0


def makeSearchableString(inputString):
    try:
        return inputString.decode(b'utf-8').lower()
    except ValueError:
        LOG_ERROR(b'Given string cannot be decoded from UTF-8', inputString)

    return


def isPopupsWindowsOpenDisabled():
    userPrefs = Settings.g_instance.userPrefs
    ds = userPrefs[b'development']
    if ds is not None:
        return ds.readBool(Settings.POPUPS_WINDOWS_DISABLED) and constants.IS_DEVELOPMENT
    else:
        return False


_ROMAN_FORBIDDEN_LANGUAGES = {
 b'ko', b'no'}

def isRomanNumberForbidden():
    return bool(_ROMAN_FORBIDDEN_LANGUAGES.intersection((backport.text(R.strings.settings.LANGUAGE_CODE()),)))
