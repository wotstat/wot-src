from __future__ import absolute_import, division
import imghdr, sys, inspect, uuid, struct
from builtins import filter, zip, range
from collections import namedtuple
from future.utils import viewitems
from past.builtins import cmp, unicode
import BigWorld, AccountCommands, Settings, constants
from debug_utils import LOG_CURRENT_EXCEPTION, LOG_ERROR, LOG_DEBUG, LOG_WARNING
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.sort_key import SortKey
from helpers import getLanguageCode
from items import vehicles as vehs_core
from account_helpers import getAccountDatabaseID
from account_helpers.AccountSettings import AccountSettings
from avatar_helpers import getAvatarDatabaseID
SHELLS_COUNT_PROP_NAME = b'shellsCount'
RELOAD_TIME_SECS_PROP_NAME = b'reloadTimeSecs'
RELOAD_TIME_PROP_NAME = b'reloadTime'
RELOAD_MAGAZINE_TIME_PROP_NAME = b'reloadMagazineTime'
SHELL_RELOADING_TIME_PROP_NAME = b'shellReloadingTime'
SHELL_LOADING_TIME_PROP_NAME = b'shellLoadingTime'
DISPERSION_RADIUS_PROP_NAME = b'dispersionRadius'
SHOT_DISPERSION_ANGLE = b'shotDispersionAngle'
DISPERSION_RADIUS = b'dispertionRadius'
AIMING_TIME_PROP_NAME = b'aimingTime'
PIERCING_POWER_PROP_NAME = b'piercingPower'
DAMAGE_PROP_NAME = b'damage'
MAX_MUTABLE_DAMAGE_PROP_NAME = b'maxMutableDamage'
MIN_MUTABLE_DAMAGE_PROP_NAME = b'minMutableDamage'
SHELLS_PROP_NAME = b'shells'
STUN_DURATION_PROP_NAME = b'stunDuration'
AUTO_RELOAD_PROP_NAME = b'autoReloadTime'
GUARANTEED_STUN_DURATION_PROP_NAME = b'guaranteedStunDuration'
CLIP_VEHICLES_PROP_NAME = b'clipVehicles'
UNICHARGED_VEHICLES_PROP_NAME = b'uniChargedVehicles'
VEHICLES_PROP_NAME = b'vehicles'
CLIP_VEHICLES_CD_PROP_NAME = b'clipVehiclesCD'
MAX_STEERING_LOCK_ANGLE = b'maxSteeringLockAngle'
NORMALIZATION_ANGLE = b'normalizationAngle'
RICOCHET_ANGLE = b'ricochetAngle'
PENETRATION_LOSS = b'penetrationLoss'
BURST_FIRE_RATE = b'burstFireRate'
BURST_TIME_INTERVAL = b'burstTimeInterval'
BURST_COUNT = b'burstCount'
BURST_SIZE = b'burstSize'
TEMPERATURE_RELOAD_TIME = b'temperatureReloadTime'
TEMPERATURE_AVG_DAMAGE_PER_MINUTE = b'temperatureAvgDamagePerMinute'
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
DUAL_GUN_CHARGE_TIME = b'chargeTime'
DUAL_GUN_RATE_TIME = b'rateTime'
DUAL_ACCURACY_AFTER_SHOT_DISPERSION_ANGLE = b'dualAccuracyAfterShotDispersionAngle'
DUAL_ACCURACY_COOLING_DELAY = b'dualAccuracyCoolingDelay'
AVG_DAMAGE_PER_SECOND = b'avgDamagePerSecond'
AUTO_SHOOT_CLIP_FIRE_RATE = b'autoShootClipFireRate'
CONTINUOUS_SHOTS_PER_MINUTE = b'continuousShotsPerMinute'
CONTINUOUS_DAMAGE_PER_SECOND = b'continuousDamagePerSecond'
TWIN_GUN_SWITCH_FIRE_MODE_TIME = b'twinGunSwitchFireModeTime'
TWIN_GUN_TOP_SPEED = b'twinGunTopSpeed'
TWIN_GUN_RELOAD_ONE_GUN_TIME = b'reloadTimeSingleGun'
TWIN_GUN_RELOAD_TWO_GUN_TIME = b'reloadTimeTwinGun'
TWIN_GUN_RELOAD_TIME = b'twinGunReloadTime'
CHASSIS_REPAIR_TIME = b'chassisRepairTime'
CHASSIS_REPAIR_TIME_YOH = b'chassisRepairTimeYoh'
CRITICAL_HIT_CHANCE = b'criticalHitChance'
GUN_CAN_BE_CLIP = 1
GUN_CLIP = 2
GUN_NORMAL = 4
GUN_CAN_BE_AUTO_RELOAD = 5
GUN_AUTO_RELOAD = 6
GUN_CAN_BE_DUAL_GUN = 7
GUN_DUAL_GUN = 8
GUN_CAN_BE_AUTO_SHOOT = 9
GUN_AUTO_SHOOT = 10
GUN_CAN_BE_TWIN_GUN = 11
GUN_TWIN_GUN = 12
GUN_CAN_BE_LOW_CHARGE_SHOT = 13
LOW_CHARGE_SHOT = 14
EXTRA_MODULE_INFO = b'extraModuleInfo'
FIELD_SPECIALIZATIONS = b'specs'
FIELD_HIGHLIGHT_TYPE = b'highlightType'
_FLASH_OBJECT_SYS_ATTRS = (b'isPrototypeOf', b'propertyIsEnumerable', b'hasOwnProperty')
ValidationResult = namedtuple(b'ValidationResult', [
 b'isValid',
 b'reason'])

def flashObject2Dict(obj):
    if hasattr(obj, b'children'):
        filtered = filter((lambda item: item[0] not in _FLASH_OBJECT_SYS_ATTRS), viewitems(obj.children))
        return {k: flashObject2Dict(v) for k, v in filtered}
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
    if code == AccountCommands.RES_RATE_LIMIT_COOLDOWN:
        return b'Identical requests rate limit cooldown'
    if code == AccountCommands.RES_LOCKED_VEHICLE:
        return b'Vehicle is locked for this request type'
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


class _SortKeyByFields(SortKey):
    __slots__ = (b'fields', b'valueGetter', b'item')

    def __init__(self, fields, valueGetter, item):
        super(_SortKeyByFields, self).__init__()
        self.fields = fields
        self.valueGetter = valueGetter
        self.item = item
        return

    def _cmp(self, other):
        for field, order in self.fields:
            fieldValueX = self.valueGetter(self.item, field)
            fieldValueY = self.valueGetter(other.item, field)
            if fieldValueX != fieldValueY:
                if order:
                    return cmp(fieldValueX, fieldValueY)
                return cmp(fieldValueY, fieldValueX)

        return 0


def sortByFields(fields, sequence, valueGetter=dict.get):
    return sorted(sequence, key=(lambda x: _SortKeyByFields(fields, valueGetter, x)))


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
                string = BigWorld.wg_changeStringCasing(string, plID, slID, sortOrder, isUpper)
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
    BigWorld.wg_copyToClipboard(unicode(text, b'utf-8', errors=b'ignore'))
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
            BigWorld.wg_addTempScaleformTexture(uniqueID, textureData)
        else:
            BigWorld.wg_addScaleformTexture(uniqueID, textureData)
        return uniqueID
    LOG_WARNING(b'There is invalid data for the memory mapping', textureData, uniqueID)
    return


def removeTextureFromMemory(textureID):
    BigWorld.wg_eraseScaleformTexture(textureID)
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
        BigWorld.WGWindowsNotifier.onInvitation()
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


def showAFKWarningInWindowsBar():
    try:
        BigWorld.WGWindowsNotifier.onAFKWarning()
    except AttributeError:
        LOG_CURRENT_EXCEPTION()

    return
