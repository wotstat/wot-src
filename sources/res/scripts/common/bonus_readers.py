from __future__ import absolute_import, division
import time
from future.utils import lmap, viewitems
from past.builtins import xrange
from past.utils import old_div
from typing import Union, TYPE_CHECKING
import dossiers2
from dynamic_currencies import g_dynamicCurrenciesData
import items, calendar
from account_shared import validateCustomizationItem
from battle_pass_common import NON_VEH_CD
from blueprints.BlueprintTypes import BlueprintTypes
from blueprints.FragmentTypes import isUniversalFragment
from dossiers2.custom.account_layout import ACCOUNT_DOSSIER_DICT_BLOCKS
from invoices_helpers import checkAccountDossierOperation
from items import vehicles, tankmen, utils
from items.components.c11n_constants import SeasonType
from items.components.crew_skins_constants import NO_CREW_SKIN_ID
from items.components.skills_constants import ROLES_BY_SKILLS
from constants import DOSSIER_TYPE, SEASON_TYPE_BY_NAME, EVENT_TYPE, INVOICE_LIMITS, ENTITLEMENT_OPS, DailyQuestsLevels, MAX_LOG_EXT_INFO_LEN
from soft_exception import SoftException
from customization_quests_common import validateCustomizationQuestToken
from py2to3.compat import base64compat
if TYPE_CHECKING:
    from ResMgr import DataSection
__all__ = [
 b'readBonusSection', b'readUTC', b'SUPPORTED_BONUSES']

def bonusReaderLimitDecorator(invoiceLimit, readFunction):

    def wrapper(bonus, name, section, eventType, checkLimit):
        readFunction(bonus, name, section, eventType, checkLimit)
        if checkLimit and bonus[name] > invoiceLimit:
            raise SoftException(b'Invalid count of %s with amount %d when limit is %d. ' % (
             name, bonus[name], invoiceLimit))
        return

    return wrapper


def getBonusReaders(bonusTypes):
    return dict((k, __BONUS_READERS[k]) for k in bonusTypes)


def timeDataToUTC(timeData, default=None):
    try:
        if timeData is None:
            raise SoftException(b'Wrong timeData')
        if timeData != b'':
            timeData = int(calendar.timegm(time.strptime(timeData, b'%d.%m.%Y %H:%M')))
        else:
            return default
    except:
        raise SoftException(b'Invalid format (%s). Format must be like %s, for example 23.01.2011 00:00.' % (
         timeData, b"'%d.%m.%Y %H:%M'"))

    return timeData


def readUTC(section, field, default=None):
    timeData = section.readString(field, b'')
    try:
        return timeDataToUTC(timeData, default)
    except Exception as e:
        raise SoftException(b'Invalid field %s: %s' % (field, e))

    return


def __readBonus_bool(bonus, name, section, eventType, checkLimit):
    bonus[name] = section.asBool
    return


def __readBonus_string_set(bonus, name, section, eventType, checkLimit):
    data = section.asString
    bonus[name] = data.strip().split()
    return


def checkLogExtInfoLen(info, infoName):
    if len(info) > MAX_LOG_EXT_INFO_LEN:
        raise SoftException(b'Length of %s id "%s" is %d more than max length %d' % (
         infoName, id, len(info), MAX_LOG_EXT_INFO_LEN))
    return


class IntHolder(int):
    newval = 0
    rate = 1

    def __new__(cls, value, **kwargs):
        return super(IntHolder, cls).__new__(cls, value, **{k: v for k, v in viewitems(kwargs) if k in (b'base',)})

    def __init__(self, value, **kwargs):
        super(IntHolder, self).__init__()
        self.ukey = kwargs.get(b'ukey')
        self.rate = int(kwargs.get(b'rate', self.rate))
        self._materialized = False
        return

    def materialize(self, substitutions):
        if self.ukey is not None and substitutions and not self.isMaterialized():
            self.newval = substitutions.get(self.ukey, 0)
            self.newval = int(max(0, self.newval * self.rate))
            self._materialized = True
        return int(self)

    def isMaterialized(self):
        return self._materialized

    def __int__(self):
        if self.isMaterialized():
            return self.newval
        return super(IntHolder, self).__int__()

    def __repr__(self):
        return int(self).__repr__()

    def bit_length(self):
        return int(self).bit_length()

    def __add__(self, x):
        return int(self).__add__(x)

    def __sub__(self, x):
        return int(self).__sub__(x)

    def __mul__(self, x):
        return int(self).__mul__(x)

    def __floordiv__(self, x):
        return int(self).__floordiv__(x)

    def __div__(self, x):
        return old_div(int(self), x)

    def __truediv__(self, x):
        return int(self).__truediv__(x)

    def __mod__(self, x):
        return int(self).__mod__(x)

    def __divmod__(self, x):
        return int(self).__divmod__(x)

    def __radd__(self, x):
        return int(self).__radd__(x)

    def __rsub__(self, x):
        return int(self).__rsub__(x)

    def __rmul__(self, x):
        return int(self).__rmul__(x)

    def __rfloordiv__(self, x):
        return int(self).__rfloordiv__(x)

    def __rdiv__(self, x):
        return old_div(x, int(self))

    def __rtruediv__(self, x):
        return int(self).__rtruediv__(x)

    def __rmod__(self, x):
        return int(self).__rmod__(x)

    def __rdivmod__(self, x):
        return int(self).__rdivmod__(x)

    def __pow__(self, x):
        return int(self).__pow__(x)

    def __rpow__(self, x):
        return int(self).__rpow__(x)

    def __and__(self, n):
        return int(self).__and__(n)

    def __or__(self, n):
        return int(self).__or__(n)

    def __xor__(self, n):
        return int(self).__xor__(n)

    def __lshift__(self, n):
        return int(self).__lshift__(n)

    def __rshift__(self, n):
        return int(self).__rshift__(n)

    def __rand__(self, n):
        return int(self).__rand__(n)

    def __ror__(self, n):
        return int(self).__ror__(n)

    def __rxor__(self, n):
        return int(self).__rxor__(n)

    def __rlshift__(self, n):
        return int(self).__rlshift__(n)

    def __rrshift__(self, n):
        return int(self).__rrshift__(n)

    def __neg__(self):
        return int(self).__neg__()

    def __pos__(self):
        return int(self).__pos__()

    def __invert__(self):
        return int(self).__invert__()

    def __eq__(self, x):
        return int(self) == x

    def __ne__(self, x):
        return int(self) != x

    def __lt__(self, x):
        return int(self) < x

    def __le__(self, x):
        return int(self) <= x

    def __gt__(self, x):
        return int(self) > x

    def __ge__(self, x):
        return int(self) >= x

    def __str__(self):
        return (b'{}: [val = {}, ukey = {}, rate = {}, isMaterialized = {}]').format(self.__class__.__name__, int(self), self.ukey, self.rate, self.isMaterialized())

    def __float__(self):
        return int(self).__float__()

    def __abs__(self):
        return int(self).__abs__()

    def __hash__(self):
        return object.__hash__(self)

    def __bool__(self):
        return bool(int(self))

    __nonzero__ = __bool__


class FloatHolder(float):
    newval = 0.0
    rate = 1.0

    def __new__(cls, value, **kwargs):
        return super(FloatHolder, cls).__new__(cls, value)

    def __init__(self, value, **kwargs):
        super(FloatHolder, self).__init__()
        self.ukey = kwargs.get(b'ukey')
        self.rate = float(kwargs.get(b'rate', self.rate))
        self._materialized = False
        return

    def materialize(self, substitutions):
        if self.ukey is not None and substitutions and not self.isMaterialized():
            self.newval = substitutions.get(self.ukey, 0.0)
            self.newval = float(max(0.0, self.newval * self.rate))
            self._materialized = True
        return float(self)

    def isMaterialized(self):
        return self._materialized

    def __float__(self):
        if self.isMaterialized():
            return self.newval
        return super(FloatHolder, self).__float__()

    def __repr__(self):
        return float(self).__repr__()

    def as_integer_ratio(self):
        return float(self).as_integer_ratio()

    def hex(self):
        return float(self).hex()

    def is_integer(self):
        return float(self).is_integer()

    @classmethod
    def fromhex(cls, s):
        return super(FloatHolder, cls).fromhex(s)

    def __add__(self, x):
        return float(self).__add__(x)

    def __sub__(self, x):
        return float(self).__sub__(x)

    def __mul__(self, x):
        return float(self).__mul__(x)

    def __floordiv__(self, x):
        return float(self).__floordiv__(x)

    def __div__(self, x):
        return float(self) / x

    def __truediv__(self, x):
        return float(self).__truediv__(x)

    def __mod__(self, x):
        return float(self).__mod__(x)

    def __divmod__(self, x):
        return float(self).__divmod__(x)

    def __pow__(self, x):
        return float(self).__pow__(x)

    def __radd__(self, x):
        return float(self).__radd__(x)

    def __rsub__(self, x):
        return float(self).__rsub__(x)

    def __rmul__(self, x):
        return float(self).__rmul__(x)

    def __rfloordiv__(self, x):
        return float(self).__rfloordiv__(x)

    def __rdiv__(self, x):
        return x / float(self)

    def __rtruediv__(self, x):
        return float(self).__rtruediv__(x)

    def __rmod__(self, x):
        return float(self).__rmod__(x)

    def __rdivmod__(self, x):
        return float(self).__rdivmod__(x)

    def __rpow__(self, x):
        return float(self).__rpow__(x)

    def __eq__(self, x):
        return float(self).__eq__(x)

    def __ne__(self, x):
        return float(self).__ne__(x)

    def __lt__(self, x):
        return float(self).__lt__(x)

    def __le__(self, x):
        return float(self).__le__(x)

    def __gt__(self, x):
        return float(self).__gt__(x)

    def __ge__(self, x):
        return float(self).__ge__(x)

    def __neg__(self):
        return float(self).__neg__()

    def __pos__(self):
        return float(self).__pos__()

    def __str__(self):
        return float(self).__str__()

    def __int__(self):
        return float(self).__int__()

    def __abs__(self):
        return float(self).__abs__()

    def __hash__(self):
        return object.__hash__(self)

    def __bool__(self):
        return bool(float(self))

    __nonzero__ = __bool__


def __readIntWithTokenExpansion(section):
    bindingToken = section.readString(b'token2int', b'')
    rate = section.readInt(b'rate', 1)
    value = section.asInt
    if value < 0:
        raise SoftException(b'Negative value (%s)' % section.name)
    if bindingToken:
        return IntHolder(value, ukey=bindingToken, rate=rate)
    return value


def __readBonus_int(bonus, name, section, eventType, checkLimit):
    bonus[name] = __readIntWithTokenExpansion(section)
    return


def __readBonus_signed_int(bonus, name, section, eventType, checkLimit):
    bonus[name] = section.asInt
    return


def __readBonus_factor(bonus, name, section, eventType, checkLimit):
    bindingToken = section.readString(b'token2float', b'')
    rate = section.readFloat(b'rate', 1.0)
    value = section.asFloat
    if value < 0:
        raise SoftException(b'Negative value (%s)' % name)
    bonus[name] = FloatHolder(value, ukey=bindingToken, rate=rate) if bindingToken else value
    return


def __readBonus_equipment(bonus, _name, section, eventType, checkLimit):
    eqName = section.asString
    cache = vehicles.g_cache
    eqID = cache.equipmentIDs().get(eqName)
    if eqID is None:
        raise SoftException(b"Unknown equipment '%s'" % eqName)
    eqCompDescr = cache.equipments()[eqID].compactDescr
    count = 1
    if section.has_key(b'count'):
        count = section[b'count'].asInt
    bonus.setdefault(b'items', {})[eqCompDescr] = count
    return


def __readBonus_optionalDevice(bonus, _name, section, eventType, checkLimit):
    name = section.asString
    cache = vehicles.g_cache
    odID = cache.optionalDeviceIDs().get(name)
    if odID is None:
        raise SoftException(b"Unknown optional device '%s'" % name)
    odCompDescr = cache.optionalDevices()[odID].compactDescr
    count = 1
    if section.has_key(b'count'):
        count = section[b'count'].asInt
    bonus.setdefault(b'items', {})[odCompDescr] = count
    return


def __readBonus_item(bonus, _name, section, eventType, checkLimit):
    compDescr = section.asInt
    try:
        descr = utils.getItemDescrByCompactDescr(compDescr)
        if descr.itemTypeName not in items.SIMPLE_ITEM_TYPE_NAMES:
            raise SoftException(b'Wrong compact descriptor (%d). Not simple item.' % compDescr)
    except:
        raise SoftException(b'Wrong compact descriptor (%d)' % compDescr)

    count = 1
    if section.has_key(b'count'):
        count = section[b'count'].asInt
    bonus.setdefault(b'items', {})[compDescr] = count
    return


def __readBonus_vehicle(bonus, _name, section, eventType, checkLimit):
    vehCompDescr = None
    if section.has_key(b'vehCompDescr'):
        vehCompDescr = base64compat.b64decode(section[b'vehCompDescr'].asString)
        vehTypeCompDescr = vehicles.VehicleDescr(vehCompDescr).type.compactDescr
    elif section.has_key(b'vehTypeCompDescr'):
        vehTypeCompDescr = section[b'vehTypeCompDescr'].asInt
    else:
        nationID, innationID = vehicles.g_list.getIDsByName(section.asString)
        vehTypeCompDescr = vehicles.makeIntCompactDescrByID(b'vehicle', nationID, innationID)
    extra = {}
    if section.has_key(b'tankmen'):
        __readBonus_tankmen(extra, vehTypeCompDescr, section[b'tankmen'], eventType, checkLimit)
    elif section.has_key(b'noCrew'):
        extra[b'noCrew'] = True
    if section.has_key(b'crewLvl'):
        extra[b'crewLvl'] = section[b'crewLvl'].asInt
    if section.has_key(b'crewFreeXP'):
        extra[b'crewFreeXP'] = section[b'crewFreeXP'].asInt
    if section.has_key(b'rent'):
        __readBonus_rent(extra, None, section[b'rent'])
    if section.has_key(b'customization'):
        __readBonus_vehicleCustomizations(extra, None, section[b'customization'])
    if section.has_key(b'customCompensation'):
        __readBonus_customCompensation(extra, None, section[b'customCompensation'])
    if section.has_key(b'customCompensationDetails'):
        __readBonus_customCompensationDetails(extra, None, section[b'customCompensationDetails'])
    if section.has_key(b'outfits'):
        __readBonus_outfits(extra, None, section[b'outfits'])
    if section.has_key(b'ammo'):
        ammo = section[b'ammo'].asString
        extra[b'ammo'] = [int(item) for item in ammo.split(b' ')]
    if section.has_key(b'eqsLayout'):
        eqsLayout = section[b'eqsLayout'].asString
        extra[b'eqsLayout'] = [int(item) for item in eqsLayout.split(b' ')]
    if section.has_key(b'unlock'):
        extra[b'unlock'] = True
    if section.has_key(b'unlockModules'):
        extra[b'unlockModules'] = True
    if section.has_key(b'bonusOrder'):
        extra[b'bonusOrder'] = section[b'bonusOrder'].asInt
    vehicleBonuses = bonus.setdefault(b'vehicles', {})
    vehKey = vehCompDescr if vehCompDescr else vehTypeCompDescr
    if vehKey in vehicleBonuses:
        raise SoftException(b'Duplicate vehicle', vehKey)
    vehicleBonuses[vehKey] = extra
    return


def __readBonus_customCompensation(bonus, _name, section):
    credits = section.readInt(b'credits', 0)
    gold = section.readInt(b'gold', 0)
    bonus[b'customCompensation'] = (credits, gold)
    return


def __readBonus_customCompensationDetails(bonus, _name, section):
    bonus[b'customCompensationDetails'] = {}
    if section.has_key(b'noCrew'):
        bonus[b'customCompensationDetails'][b'noCrew'] = True
    return


def __readBonus_vehicleCustomizations(bonus, _name, section):
    custData = {b'value': 1, 
       b'custType': b'style', 
       b'id': (section.readInt(b'styleId', -1))}
    if section.has_key(b'customCompensation'):
        __readBonus_customCompensation(custData, None, section[b'customCompensation'])
    if section.has_key(b'serialNumberSequence'):
        custData[b'serialNumberSequence'] = section.readString(b'serialNumberSequence')
    isValid, item = validateCustomizationItem(custData)
    if not isValid:
        raise SoftException(item)
    bonus[b'customization'] = {b'styleId': (custData[b'id']), 
       b'customCompensation': (custData[b'customCompensation'])}
    if b'serialNumberSequence' in custData:
        bonus[b'customization'][b'serialNumberSequence'] = custData[b'serialNumberSequence']
    return


def __readBonus_tankmen(bonus, vehTypeCompDescr, section, eventType, checkLimit):
    lst = []
    for subsection in section.values():
        tmanDescr = subsection.asString
        if tmanDescr:
            try:
                tman = tankmen.TankmanDescr(tmanDescr)
                if isinstance(vehTypeCompDescr, int):
                    _, vehNationID, vehicleTypeID = vehicles.parseIntCompactDescr(vehTypeCompDescr)
                    if vehNationID != tman.nationID or vehicleTypeID != tman.vehicleTypeID:
                        raise SoftException(b'Vehicle and tankman mismatch.')
            except Exception as e:
                raise SoftException(b'Invalid tankmen compact descr. Error: %s' % (e,))

            lst.append(tmanDescr)
            continue
        tmanData = {b'isFemale': (subsection.readBool(b'isFemale', False)), 
           b'firstNameID': (subsection.readInt(b'firstNameID', -1)), 
           b'lastNameID': (subsection.readInt(b'lastNameID', -1)), 
           b'role': (subsection.readString(b'role', b'')), 
           b'iconID': (subsection.readInt(b'iconID', -1)), 
           b'freeXP': (subsection.readInt(b'freeXP', 0)), 
           b'fnGroupID': (subsection.readInt(b'fnGroupID', 0)), 
           b'lnGroupID': (subsection.readInt(b'lnGroupID', 0)), 
           b'iGroupID': (subsection.readInt(b'iGroupID', 0)), 
           b'isPremium': (subsection.readBool(b'isPremium', False)), 
           b'nationID': (subsection.readInt(b'nationID', -1)), 
           b'vehicleTypeID': (subsection.readInt(b'vehicleTypeID', -1)), 
           b'skills': (subsection.readString(b'skills', b'').split()), 
           b'freeSkills': (subsection.readString(b'freeSkills', b'').split())}
        if subsection.has_key(b'bonusSkills'):
            tmanData[b'bonusSkills'] = bonusSkills = {}
            for bonusSkill in subsection.readString(b'bonusSkills', b'').split():
                skillRole = next(role for role in ROLES_BY_SKILLS[bonusSkill])
                bonusSkills.setdefault(skillRole, []).append(bonusSkill)

        if checkLimit and tmanData[b'freeXP'] > INVOICE_LIMITS.TMAN_FREEXP_MAX:
            raise SoftException(b'Invalid count of tankman free xp with amount %d when limit is %d.' % (
             tmanData[b'freeXP'], INVOICE_LIMITS.TMAN_FREEXP_MAX))
        if checkLimit and len(tmanData[b'skills']) > INVOICE_LIMITS.TMAN_SKILLS_MAX:
            raise SoftException(b'Invalid count of tankman skills with amount %d when limit is %d.' % (
             len(tmanData[b'skills']), INVOICE_LIMITS.TMAN_SKILLS_MAX))
        for record in (b'firstNameID', b'lastNameID', b'iconID'):
            if tmanData[record] == -1:
                tmanData[record] = None

        try:
            if isinstance(vehTypeCompDescr, int):
                _, vehNationID, vehicleTypeID = vehicles.parseIntCompactDescr(vehTypeCompDescr)
                if vehNationID != tmanData[b'nationID'] or vehicleTypeID != tmanData[b'vehicleTypeID']:
                    raise SoftException(b'Vehicle and tankman mismatch.')
            if eventType != EVENT_TYPE.PERSONAL_MISSION:
                tmanData = tankmen.makeTmanDescrByTmanData(tmanData)
            lst.append(tmanData)
        except Exception as e:
            raise SoftException(b'%s: %s' % (e, tmanData))

    bonus[b'tankmen'] = lst
    return


def __readBonus_seasonRent(outRent, section):
    if section.has_key(b'season'):
        try:
            seasonData = section[b'season'].asString.split(b':', 1)
            seasonType = SEASON_TYPE_BY_NAME[seasonData[0].strip()]
            strID = seasonData[1]
            if strID.startswith(b'season_'):
                rentType = b'season'
            elif strID.startswith(b'cycle_'):
                rentType = b'cycle'
            else:
                raise SoftException(b'Invalid season / cycle ID in rent bonus <rent><season>. Expected format: GameSeasonType:season_YYYYMM or                 GameSeasonType:cycle_YYYYMMDD')
            ID = int(strID.split(b'_', 1)[1].strip())
            outRent[rentType] = [(seasonType, ID)]
        except (KeyError, ValueError):
            raise SoftException(b'Failed to parse season rent bonus for <rent><{type}>. Expected format: GameSeasonType:season_YYYYMM or                 GameSeasonType:cycle_YYYYMMDD')

    return


def __readBonus_rent(bonus, _name, section):
    rent = {}
    anySectionExist = False
    if section.has_key(b'anyExpires'):
        rent[b'anyExpires'] = anySectionExist = True
    if section.has_key(b'time'):
        rent[b'time'] = section[b'time'].asFloat
    if section.has_key(b'battles'):
        rent[b'battles'] = section[b'battles'].asInt
    if section.has_key(b'wins'):
        rent[b'wins'] = section[b'wins'].asInt
    if anySectionExist:
        for key in (b'time', b'battles', b'wins'):
            rent[key] = rent[key] if key in rent and rent[key] > 0 else float(b'inf')

    if section.has_key(b'compensation'):
        credits = section[b'compensation'].readInt(b'credits', 0)
        gold = section[b'compensation'].readInt(b'gold', 0)
        rent[b'compensation'] = (credits, gold)
    __readBonus_seasonRent(rent, section)
    bonus[b'rent'] = rent
    return


def __readBonus_outfits(bonus, _name, section):
    outfits = {}
    for seasonTypeName, seasonTypeID in viewitems({b'winter': (SeasonType.WINTER), 
       b'summer': (SeasonType.SUMMER), 
       b'desert': (SeasonType.DESERT), 
       b'event': (SeasonType.EVENT)}):
        if section.has_key(seasonTypeName):
            outfits[seasonTypeID] = base64compat.b64decode(section[seasonTypeName].asString)

    bonus[b'outfits'] = outfits
    return


def __readBonus_customizations(bonus, _name, section, eventType, checkLimit):
    lst = []
    for subsection in section.values():
        custData = {b'value': (subsection.readInt(b'value', 0)), 
           b'custType': (subsection.readString(b'custType', b'')), 
           b'id': (subsection.readInt(b'id', -1))}
        if subsection.has_key(b'boundVehicle'):
            custData[b'vehTypeCompDescr'] = vehicles.makeIntCompactDescrByID(b'vehicle', *vehicles.g_list.getIDsByName(subsection.readString(b'boundVehicle', b'')))
        elif subsection.has_key(b'boundToCurrentVehicle'):
            if eventType in EVENT_TYPE.LIKE_TOKEN_QUESTS:
                raise SoftException(b"Unsupported tag 'boundToCurrentVehicle' in 'like token' quests")
            custData[b'boundToCurrentVehicle'] = True
        if subsection.has_key(b'customCompensation'):
            __readBonus_customCompensation(custData, None, subsection[b'customCompensation'])
        if subsection.has_key(b'serialNumberSequence'):
            custData[b'serialNumberSequence'] = subsection.readString(b'serialNumberSequence', b'')
        isValid, item = validateCustomizationItem(custData)
        if not isValid:
            raise SoftException(item)
        lst.append(custData)

    bonus[b'customizations'] = lst
    return


def __readBonus_crewSkin(bonus, _name, section, eventType, checkLimit):
    crewSkinID = section.readInt(b'id', NO_CREW_SKIN_ID)
    skinData = {b'id': crewSkinID, 
       b'count': (section.readInt(b'count', 0))}
    if crewSkinID not in tankmen.g_cache.crewSkins().skins:
        raise SoftException(b"Unknown crew skin id '%s'" % crewSkinID)
    if skinData[b'count'] == 0:
        raise SoftException(b"Invalid count for crew skin id '%s'" % crewSkinID)
    if checkLimit and skinData[b'count'] > INVOICE_LIMITS.CREW_SKINS:
        raise SoftException(b'Invalid count of crew skin id %s with amount %d when limit is %d.' % (
         crewSkinID, skinData[b'count'], INVOICE_LIMITS.CREW_SKINS))
    bonus.setdefault(b'crewSkins', []).append(skinData)
    return


def __readBonus_tokens(bonus, _name, section, eventType, checkLimit):
    tokenID = section[b'id'].asString
    checkLogExtInfoLen(tokenID, b'token')
    if tokenID.startswith(tankmen.RECRUIT_TMAN_TOKEN_PREFIX) and tankmen.getRecruitInfoFromToken(tokenID) is None:
        raise SoftException((b'Invalid tankman token format: {}').format(tokenID))
    token = bonus.setdefault(b'tokens', {})[tokenID] = {}
    expires = token.setdefault(b'expires', {})
    __readBonus_expires(tokenID, expires, section)
    if section.has_key(b'limit'):
        token[b'limit'] = section[b'limit'].asInt
    token[b'count'] = 1
    if section.has_key(b'count'):
        token[b'count'] = section[b'count'].asInt
    res = validateCustomizationQuestToken(tokenID, token)
    if not res[0]:
        raise SoftException(res[1])
    if checkLimit and token[b'count'] > INVOICE_LIMITS.TOKENS_MAX:
        raise SoftException(b'Invalid count of tankman token with id %s with amount %d when limit is %d.' % (
         tokenID, token[b'count'], INVOICE_LIMITS.TOKENS_MAX))
    return


def __readBonus_goodies(bonus, _name, section, eventType, checkLimit):
    goodieID = section[b'id'].asInt
    goodies = bonus.setdefault(b'goodies', {})
    if goodieID in goodies:
        raise SoftException((b'Duplicated goodie with id {}').format(goodieID))
    goodie = goodies.setdefault(goodieID, {})
    if section.has_key(b'limit'):
        goodie[b'limit'] = max(goodie.get(b'limit', 0), section[b'limit'].asInt)
    if section.has_key(b'count'):
        goodie[b'count'] = __readIntWithTokenExpansion(section[b'count'])
    else:
        goodie[b'count'] = 1
    if checkLimit and goodie[b'count'] > INVOICE_LIMITS.GOODIES_MAX:
        raise SoftException(b'Invalid count for goodie with id %d with amount %d when limit is %d.' % (
         goodieID, goodie[b'count'], INVOICE_LIMITS.GOODIES_MAX))
    return


def __readBonus_enhancement(bonus, _name, section, eventType, checkLimit):
    enhancementID = section.asInt
    count = 1
    wipe = False
    if section.has_key(b'count'):
        count = section[b'count'].asInt
    if section.has_key(b'wipe'):
        wipe = section[b'wipe'].asBool
    bonus.setdefault(b'enhancements', {})[enhancementID] = {b'count': count, 
       b'wipe': wipe}
    return


def __readBonus_entitlement(bonus, _name, section, eventType, checkLimit):
    entID, entData = _readEntitlementSection(section, checkLimit)
    bonus.setdefault(b'entitlements', {})[entID] = entData
    return


def __readBonus_entitlementList(bonus, _name, section, eventType, checkLimit):
    entItems = bonus.setdefault(b'entitlementList', {}).setdefault(b'items', [])
    for name, itemSection in section.items():
        if name != b'item':
            raise SoftException(b'Not expected element', name)
        entID, entData = _readEntitlementSection(itemSection, checkLimit, readOp=True)
        if entData[b'count'] <= 0:
            raise SoftException(b'Not positive count for entitlement with operation', entID, entData)
        entData[b'id'] = entID
        entItems.append(entData)

    return


def _readEntitlementSection(section, checkLimit, readOp=False):
    entitlement = {}
    entID = section[b'id'].asString
    checkLogExtInfoLen(entID, b'entitlement')
    if section.has_key(b'count'):
        entitlement[b'count'] = section[b'count'].asInt
    else:
        entitlement[b'count'] = 1
    if readOp:
        entitlement[b'op'] = operation = section.readString(b'operation', b'')
        if operation not in ENTITLEMENT_OPS.ALL:
            raise SoftException(b'Invalid op for entitlement:', entID, operation, ENTITLEMENT_OPS.ALL)
    if checkLimit and entitlement[b'count'] > INVOICE_LIMITS.ENTITLEMENTS_MAX:
        raise SoftException(b'Invalid count of entitlement id %s with amount %d when limit is %d.' % (
         entID, entitlement[b'count'], INVOICE_LIMITS.ENTITLEMENTS_MAX))
    if section.has_key(b'expires'):
        entitlement[b'expires'] = expires = {}
        __readBonus_expires(entID, expires, section)
    return (entID, entitlement)


def __readBonus_currency(bonus, _name, section, eventType, checkLimit):
    currencyCode = section[b'code'].asString
    if not g_dynamicCurrenciesData.isCurrencyCodeCorrect(currencyCode):
        raise SoftException(b'Incorrect code "%(code)s" has been provided in section <currency> in quests xml - it does not exist at platform.' % {b'code': currencyCode})
    currency = bonus.setdefault(b'currencies', {})[currencyCode] = {}
    currency[b'count'] = section[b'count'].asInt
    return


def __readBonus_expires(bonusID, expires, section):
    if section[b'expires'].has_key(b'endOfGameDay'):
        expires[b'endOfGameDay'] = True
        return
    else:
        if section[b'expires'].has_key(b'after'):
            expires[b'after'] = section[b'expires'][b'after'].asInt
        else:
            expires[b'at'] = readUTC(section, b'expires')
            if expires[b'at'] is None:
                raise SoftException(b'Invalid expiry time for %s' % bonusID)
        return


def __readBonus_dossier(bonus, _name, section, eventType, checkLimit):
    blockName, record = section[b'name'].asString.split(b':')
    operation = b'add'
    if section.has_key(b'type'):
        operation = section[b'type'].asString
    if operation not in (b'add', b'append', b'set'):
        raise SoftException(b'Invalid dossier record %s' % operation)
    strValue = section[b'value'].asString
    value = int(strValue) if strValue not in (b'timestamp',) else strValue
    unique = False
    if section.has_key(b'unique'):
        unique = section[b'unique'].asBool
    dossierType = DOSSIER_TYPE.ACCOUNT
    if section.has_key(b'dossierType'):
        dossierType = section[b'dossierType'].asInt
    if dossierType == DOSSIER_TYPE.ACCOUNT:
        if blockName in ACCOUNT_DOSSIER_DICT_BLOCKS:
            try:
                record = int(record)
            except ValueError:
                pass

        isValid, message = checkAccountDossierOperation(dossierType, blockName, record, operation)
        if not isValid:
            raise SoftException(b'Invalid dossier bonus %s: %s' % (blockName + b':' + record, message))
    else:
        raise SoftException(b'Dossier type %s not supported in bonus reader' % dossierType)
    bonus.setdefault(b'dossier', {}).setdefault(dossierType, {})[(blockName, record)] = {b'value': value, 
       b'unique': unique, 
       b'type': operation}
    return


def __readBonus_blueprint(bonus, _name, section, eventType, checkLimit):
    bonus.setdefault(b'blueprints', {})
    compDescr = section.readInt(b'compDescr', 0) or vehicles.makeVehicleTypeCompDescrByName(section.readString(b'vehType'))
    if not dossiers2.custom.cache.getCache():
        dossiers2.custom.cache.buildCache()
    cache = dossiers2.custom.cache.getCache()
    if compDescr == 0:
        raise SoftException(b'Invalid vehicle type name or description %s' % section)
    if not isUniversalFragment(compDescr):
        _ = vehicles.getVehicleType(compDescr)
        if compDescr not in cache[b'vehiclesInTrees']:
            raise SoftException(b'Invalid vehicle type %s. Vehicle is not in research tree.' % section)
    count = section.readInt(b'count', 0)
    if checkLimit and count > INVOICE_LIMITS.BLUEPRINTS_MAX:
        raise SoftException(b'Invalid count of blueprint id %s with amount %d when limit is %d.' % (
         compDescr, count, INVOICE_LIMITS.BLUEPRINTS_MAX))
    if count != 0:
        bonus[b'blueprints'].update({compDescr: count})
    return


def __readBonus_blueprintAny(bonus, _name, section, eventType, checkLimit):
    bonus.setdefault(b'blueprintsAny', {})
    count = section.readInt(b'count', 1)
    if count < 1:
        raise SoftException(b'Any blueprint count must be positive, got %s' % count)
    if checkLimit and count > INVOICE_LIMITS.BLUEPRINTS_MAX:
        raise SoftException(b'Invalid count of any blueprint with amount %d when limit is %d.' % (
         count, INVOICE_LIMITS.BLUEPRINTS_MAX))
    fragmentType = section.readInt(b'fragmentType', 1)
    if fragmentType not in [BlueprintTypes.VEHICLE, BlueprintTypes.NATIONAL]:
        raise SoftException(b'Fragment type should be in range [1, 2], where 1 is Vehicle and 2 is National fragment. Given value is %s' % fragmentType)
    bonus[b'blueprintsAny'].update({fragmentType: count})
    return


def __readBonus_vehicleChoice(bonus, _name, section, eventType, checkLimit):
    extra = {}
    if section.has_key(b'levels'):
        for level in section[b'levels'].asString.split():
            if 1 <= int(level) <= 10:
                extra.setdefault(b'levels', set()).add(int(level))

    if section.has_key(b'crewLvl'):
        extra[b'crewLvl'] = section[b'crewLvl'].asInt
    bonus[b'demandedVehicles'] = extra
    return


def __readMetaSection(bonus, _name, section, eventType, checkLimit):
    if section is None:
        return
    else:
        meta = {}
        for local, sub in section.items():
            if local != b'actions':
                meta[local.strip()] = sub.readString(b'', b'').strip()
            else:
                meta[b'actions'] = actions = {}
                for action, params in sub.items():
                    actions[action.strip()] = {k.strip(): v.readString(b'', b'').strip() for k, v in params.items()}

        bonus[b'meta'] = meta
        return


def __readBonus_optionalData(config, bonusReaders, section, eventType):
    limitIDs, bonus = __readBonusSubSection(config, bonusReaders, section, eventType)
    probabilityStageCount = config.get(b'probabilityStageCount', 1)
    probabilitiesList = None
    if section.has_key(b'probability'):
        probabilities = lmap(float, section.readString(b'probability', b'').split())
        probabilitiesLen = len(probabilities)
        if probabilitiesLen > probabilityStageCount or probabilitiesLen == 0:
            raise SoftException((b'Expected {} probabilities, received {}').format(probabilityStageCount, probabilitiesLen))
        for probability in probabilities:
            if not 0 <= probability <= 100:
                raise SoftException((b'Probability is out of range: {}').format(probability))

        probabilitiesList = lmap((lambda probability: probability / 100.0), probabilities)
        probabilitiesList.extend([probabilitiesList[-1]] * (probabilityStageCount - probabilitiesLen))
    bonusProbability = None
    if section.has_key(b'bonusProbability'):
        if not config.get(b'useBonusProbability', False):
            raise SoftException(b'Redundant option useBonusProbability')
        bonusProbability = section[b'bonusProbability'].asFloat
        if not 0 <= bonusProbability <= 100:
            raise SoftException((b'Bonus probability is out of range: {}').format(bonusProbability))
        bonusProbability /= 100.0
    properties = {}
    if section.has_key(b'compensation'):
        properties[b'compensation'] = section[b'compensation'].asBool
    if section.has_key(b'shouldCompensated'):
        properties[b'shouldCompensated'] = section[b'shouldCompensated'].asBool
    name = section.readString(b'name', b'')
    if name:
        properties[b'name'] = name
    if section.has_key(b'limitID'):
        limitID = section[b'limitID'].asString
        limitConfig = config.get(b'limits', {}).get(limitID, {})
        if not limitConfig:
            raise SoftException((b'Unknown limitID: {}').format(limitID))
        properties[b'limitID'] = limitID
        if b'guaranteedFrequency' in limitConfig:
            limitIDs.add(limitID)
    if section.has_key(b'depthLevel'):
        properties[b'depthLevel'] = depthLevel = section[b'depthLevel'].asInt
        if depthLevel < 0:
            raise SoftException((b"Invalid value for 'checkDepth' option: {}").format(depthLevel))
    if section.has_key(b'probabilityStageDependence'):
        properties[b'probabilityStageDependence'] = section[b'probabilityStageDependence'].asBool
    if section.has_key(b'dropInGroup'):
        properties[b'dropInGroup'] = section[b'dropInGroup'].asBool
    if section.has_key(b'trackedByNameLimit'):
        trackedByNameLimit = section.readInt(b'trackedByNameLimit', 0)
        if trackedByNameLimit <= 0:
            raise SoftException((b'Incorrect trackedByNameLimit value for <optional> with name={}').format(name))
        if not name:
            raise SoftException(b'name is mandatory for <optional> with "trackedByNameLimit" option used')
        if properties.get(b'dropInGroup'):
            raise SoftException((b'dropInGroup and trackedByName flags should not be used in the same <optional> (name={}).').format(name))
        properties[b'trackedByNameLimit'] = trackedByNameLimit
    if properties:
        bonus[b'properties'] = properties
    return (limitIDs, probabilitiesList, bonusProbability, bonus)


def __readBonus_optional(config, bonusReaders, bonus, section, eventType):
    limitIDs, probabilitiesList, bonusProbability, subBonus = __readBonus_optionalData(config, bonusReaders, section, eventType)
    if probabilitiesList is None:
        raise SoftException(b"Missing probability attribute in 'optional'")
    if config.get(b'useBonusProbability', False) and bonusProbability is None:
        raise SoftException(b"Missing bonusProbability attribute in 'optional'")
    properties = subBonus.get(b'properties', {})
    for property in (b'compensation', b'shouldCompensated', b'depthLevel'):
        if properties.get(property, None) is not None:
            raise SoftException((b"Property '{}' not allowed for standalone 'optional'").format(property))

    bonus.setdefault(b'allof', []).append((probabilitiesList, bonusProbability, limitIDs if limitIDs else None,
     subBonus))
    return limitIDs


def __readBonus_oneof(config, bonusReaders, bonus, section, eventType):
    equalProbabilityCount = 0
    equalBonusProbabilityCount = 0
    oneOfBonus = []
    resultLimitIDs = set()
    useBonusProbability = config.get(b'useBonusProbability', False)
    probabilityStageCount = config.get(b'probabilityStageCount', 1)
    equalProbabilityValues = [0.0] * probabilityStageCount
    equalBonusProbabilityValue = 0.0
    for name, subsection in section.items():
        if name != b'optional':
            raise SoftException((b"Unexpected section (or property) inside 'oneof': {}").format(name))
        limitIDs, probabilitiesList, bonusProbability, subBonus = __readBonus_optionalData(config, bonusReaders, subsection, eventType)
        if probabilitiesList is None:
            equalProbabilityCount += 1
        else:
            for i in xrange(probabilityStageCount):
                equalProbabilityValues[i] += probabilitiesList[i]

        if useBonusProbability:
            if bonusProbability is None:
                equalBonusProbabilityCount += 1
            else:
                equalBonusProbabilityValue += bonusProbability
        if limitIDs:
            if resultLimitIDs:
                raise SoftException(b'Guaranteed limits conflict', resultLimitIDs, limitIDs)
            limitID = subBonus.get(b'properties', {}).get(b'limitID', None)
            if limitID and b'guaranteedFrequency' not in config[b'limits'][limitID]:
                raise SoftException(b'Limits conflict', limitID, limitIDs)
            resultLimitIDs.update(limitIDs)
        oneOfBonus.append((probabilitiesList, bonusProbability, limitIDs if limitIDs else None, subBonus))

    if equalProbabilityCount:
        equalProbabilityValues = [(1.0 - equalProbabilityValue) / equalProbabilityCount for equalProbabilityValue in equalProbabilityValues]
    if equalBonusProbabilityCount:
        equalBonusProbabilityValue = (1.0 - equalBonusProbabilityValue) / equalBonusProbabilityCount
    oneOfTemp = []
    maximumProbabilities = [0.0] * probabilityStageCount
    maximumBonusProbability = 0.0
    for probabilities, bonusProbability, limitIDs, subBonus in oneOfBonus:
        if probabilities is None:
            probabilitiesList = equalProbabilityValues
        else:
            probabilitiesList = probabilities
        for i in xrange(probabilityStageCount):
            maximumProbabilities[i] += probabilitiesList[i]

        if useBonusProbability:
            if bonusProbability is None:
                maximumBonusProbability += equalBonusProbabilityValue
            else:
                maximumBonusProbability += bonusProbability
        values = maximumProbabilities if probabilities != [0.0] * probabilityStageCount else probabilities
        bonusValue = maximumBonusProbability if bonusProbability != 0.0 and useBonusProbability else bonusProbability
        oneOfTemp.append(([min(1.0, value) for value in values], min(1.0, bonusValue), limitIDs, subBonus))

    for maximumProbability in maximumProbabilities:
        if abs(1.0 - maximumProbability) >= 1e-06:
            raise SoftException(b'Sum of probabilities != 100', maximumProbability)

    if useBonusProbability and abs(1.0 - maximumBonusProbability) >= 1e-06:
        raise SoftException(b'Sum of bonus probabilities != 100', maximumBonusProbability)
    bonus.setdefault(b'groups', []).append({b'oneof': (resultLimitIDs if resultLimitIDs else None, oneOfTemp)})
    return resultLimitIDs


def __readBonus_dogTag(bonus, _name, section, eventType, checkLimit):
    componentId = section[b'id'].asInt
    data = {b'id': componentId}
    value = section.readFloat(b'value', 0.0)
    grade = section.readInt(b'grade', 0)
    unlock = section.readBool(b'unlock', False)
    needRecalculate = section.readBool(b'needRecalculate', False)
    if value:
        data[b'value'] = value
    if grade:
        data[b'grade'] = grade
    if unlock:
        data[b'unlock'] = unlock
    if needRecalculate:
        data[b'needRecalculate'] = needRecalculate
    bonus.setdefault(b'dogTagComponents', []).append(data)
    return


def __readBonus_battlePassPoints(bonus, _name, section, eventType, checkLimit):
    count = __readIntWithTokenExpansion(section)
    if checkLimit and count > INVOICE_LIMITS.BATTLE_PASS_POINTS:
        raise SoftException(b'Invalid count of battlePassPoints with amount %d when limit is %d.' % (
         count, INVOICE_LIMITS.BATTLE_PASS_POINTS))
    bonus[b'battlePassPoints'] = {b'vehicles': {NON_VEH_CD: count}}
    return


def __readBonus_dailyQuestReroll(bonus, name, section, eventType, checkLimit):
    data = section.asString
    levels = set(data.strip().split())
    if set(levels).intersection(DailyQuestsLevels.ALL) != levels:
        raise SoftException((b'Invalid daily quest level {}').format(levels))
    bonus[name] = levels
    return


def __readBonus_noviceReset(bonus, name, section, eventType, checkLimit):
    noviceType = section[b'noviceType'].asInt
    noviceRating = section[b'noviceRating'].asInt
    bonus[name] = {b'noviceType': noviceType, b'noviceRating': noviceRating}
    return


def __readBonus_freePremiumCrew(bonus, _name, section, eventType, checkLimit):
    vehLevel = section[b'vehLevel'].asInt
    count = section.readInt(b'count', 1)
    if b'freePremiumCrew' in bonus and vehLevel in bonus[b'freePremiumCrew']:
        raise SoftException(b'Duplicate free premium crew vehLevel', vehLevel)
    freePremiumCrewBonus = bonus.setdefault(b'freePremiumCrew', {})
    freePremiumCrewBonus[vehLevel] = count
    return


def __readBonus_pets(bonus, name, section, eventType, checkLimit):
    pets = lmap(int, section.asString.strip().split())
    if any(pID <= 0 for pID in pets):
        raise SoftException(b'pet id in pets bonus section less or equal zero')
    bonus[name] = set(pets)
    return


def __readBonus_group(config, bonusReaders, bonus, section, eventType):
    limitIDs, subBonus = __readBonusSubSection(config, bonusReaders, section, eventType)
    bonus.setdefault(b'groups', []).append(subBonus)
    return limitIDs


__BONUS_READERS = {b'meta': __readMetaSection, 
   b'buyAllVehicles': __readBonus_bool, 
   b'buySecretVehicles': __readBonus_bool, 
   b'buySpecialVehicles': __readBonus_bool, 
   b'buyCommonVehicles': __readBonus_bool, 
   b'researchAllVehicles': __readBonus_bool, 
   b'equipGold': __readBonus_bool, 
   b'ultimateLoginPriority': __readBonus_bool, 
   b'provideXPpp': __readBonus_signed_int, 
   b'addTankmanSkills': __readBonus_bool, 
   b'buySpecial': __readBonus_string_set, 
   b'premiumAmmo': __readBonus_int, 
   b'gold': (bonusReaderLimitDecorator(INVOICE_LIMITS.GOLD_MAX, __readBonus_int)), 
   b'credits': (bonusReaderLimitDecorator(INVOICE_LIMITS.CREDITS_MAX, __readBonus_int)), 
   b'crystal': (bonusReaderLimitDecorator(INVOICE_LIMITS.CRYSTAL_MAX, __readBonus_int)), 
   b'eventCoin': (bonusReaderLimitDecorator(INVOICE_LIMITS.EVENT_COIN_MAX, __readBonus_int)), 
   b'bpcoin': (bonusReaderLimitDecorator(INVOICE_LIMITS.BPCOIN_MAX, __readBonus_int)), 
   b'equipCoin': (bonusReaderLimitDecorator(INVOICE_LIMITS.EQUIP_COIN_MAX, __readBonus_int)), 
   b'freeXP': (bonusReaderLimitDecorator(INVOICE_LIMITS.FREEXP_MAX, __readBonus_int)), 
   b'slots': (bonusReaderLimitDecorator(INVOICE_LIMITS.SLOTS_MAX, __readBonus_int)), 
   b'berths': (bonusReaderLimitDecorator(INVOICE_LIMITS.BERTHS_MAX, __readBonus_int)), 
   b'premium': __readBonus_int, 
   b'premium_plus': __readBonus_int, 
   b'premium_vip': __readBonus_int, 
   b'xp': __readBonus_int, 
   b'tankmenXP': __readBonus_int, 
   b'vehicleXP': __readBonus_int, 
   b'trainCommander': __readBonus_int, 
   b'maxVehicleLevel': __readBonus_int, 
   b'xpFactor': __readBonus_factor, 
   b'creditsFactor': __readBonus_factor, 
   b'freeXPFactor': __readBonus_factor, 
   b'tankmenXPFactor': __readBonus_factor, 
   b'vehicleXPFactor': __readBonus_factor, 
   b'item': __readBonus_item, 
   b'enhancement': __readBonus_enhancement, 
   b'equipment': __readBonus_equipment, 
   b'optionalDevice': __readBonus_optionalDevice, 
   b'token': __readBonus_tokens, 
   b'goodie': __readBonus_goodies, 
   b'vehicle': __readBonus_vehicle, 
   b'dossier': __readBonus_dossier, 
   b'tankmen': __readBonus_tankmen, 
   b'customizations': __readBonus_customizations, 
   b'crewSkin': __readBonus_crewSkin, 
   b'entitlement': __readBonus_entitlement, 
   b'entitlementList': __readBonus_entitlementList, 
   b'rankedDailyBattles': (bonusReaderLimitDecorator(INVOICE_LIMITS.RANKED_DAILY_BATTLES_MAX, __readBonus_int)), 
   b'rankedBonusBattles': (bonusReaderLimitDecorator(INVOICE_LIMITS.RANKED_BONUS_BATTLES_MAX, __readBonus_int)), 
   b'dogTagComponent': __readBonus_dogTag, 
   b'battlePassPoints': __readBonus_battlePassPoints, 
   b'dailyQuestReroll': __readBonus_dailyQuestReroll, 
   b'noviceReset': __readBonus_noviceReset, 
   b'vehicleChoice': __readBonus_vehicleChoice, 
   b'blueprint': __readBonus_blueprint, 
   b'blueprintAny': __readBonus_blueprintAny, 
   b'currency': __readBonus_currency, 
   b'freePremiumCrew': __readBonus_freePremiumCrew, 
   b'pets': __readBonus_pets}
__PROBABILITY_READERS = {b'optional': __readBonus_optional, 
   b'oneof': __readBonus_oneof, 
   b'group': __readBonus_group}
_RESERVED_NAMES = frozenset([139, 140, 141, 142, 143, 144, 
 145, 146, 147, 148, 
 149, 150])
SUPPORTED_BONUSES = frozenset(__BONUS_READERS)
__SORTED_BONUSES = sorted(SUPPORTED_BONUSES)
SUPPORTED_BONUSES_IDS = dict((n, i) for i, n in enumerate(__SORTED_BONUSES))
SUPPORTED_BONUSES_NAMES = dict(enumerate(__SORTED_BONUSES))

def __readBonusLimit(section):
    properties = {}
    name = section.readString(b'name', b'')
    if not name:
        raise SoftException(b'Limit name missing')
    for property in (b'maxFrequency', b'guaranteedFrequency', b'bonusLimit', b'useBonusProbabilityAfter'):
        value = section[property]
        if value is not None:
            properties[property] = value.asInt

    for property in (b'countDuplicates', b'isForPlayers'):
        value = section[property]
        if value is not None:
            properties[property] = value.asBool

    if not properties:
        raise SoftException((b'Empty limit section: {}').format(name))
    if sum(True for property in properties if property in (b'maxFrequency', b'guaranteedFrequency', b'bonusLimit', b'useBonusProbabilityAfter')) > 1:
        raise SoftException((b'Too many limits: {}').format(name))
    return (name, properties)


def __readBonusConfig(section):
    config = {}
    for name, data in section.items():
        if name == b'limit':
            limits = config.setdefault(b'limits', {})
            limitName, limitConfig = __readBonusLimit(data)
            if limitName in limits:
                raise SoftException((b'Bonus limit already defined: {}').format(limitName))
            limits[limitName] = limitConfig
        elif name == b'needsBonusExpansion':
            config.setdefault(b'needsBonusExpansion', False)
            config[b'needsBonusExpansion'] = data.asBool
        elif name == b'probabilityStageCount':
            config.setdefault(b'probabilityStageCount', 1)
            probabilityStageCount = data.asInt
            if probabilityStageCount < 1:
                raise SoftException((b'Invalid probabilityStageCount value {}, expected greater or equal 1').format(probabilityStageCount))
            config[b'probabilityStageCount'] = probabilityStageCount
        elif name == b'useBonusProbability':
            config.setdefault(b'useBonusProbability', False)
            config[b'useBonusProbability'] = data.asBool
        elif name == b'showBonusInfo':
            config[b'showBonusInfo'] = data.asBool
        elif name == b'showProbabilitiesInfo':
            config[b'showProbabilitiesInfo'] = data.asBool
        elif name == b'dropInGroupItemsCount':
            config[b'dropInGroupItemsCount'] = data.asInt
        else:
            raise SoftException((b'Unknown config section: {}').format(name))

    limitIDsLen = sum([len(limitID) for limitID in config.get(b'limits', {})])
    if limitIDsLen > 200:
        raise SoftException((b'Limit IDs (len = {}) might not fit to token len ({}) for logging purposes').format(limitIDsLen, MAX_LOG_EXT_INFO_LEN))
    return config


def readBonusSection(bonusRange, section, eventType=None, checkLimit=True):
    if section is None:
        return {}
    else:
        bonusReaders = getBonusReaders(bonusRange)
        config = __readBonusConfig(section[b'config']) if section.has_key(b'config') else {}
        _, bonus = __readBonusSubSection(config, bonusReaders, section, eventType, checkLimit)
        if config:
            bonus[b'config'] = config
        return bonus


def __readBonusSubSection(config, bonusReaders, section, eventType=None, checkLimit=True):
    bonus = {}
    resultLimitIDs = set()
    for name, subSection in section.items():
        if name in __PROBABILITY_READERS:
            limitIDs = __PROBABILITY_READERS[name](config, bonusReaders, bonus, subSection, eventType)
            if limitIDs:
                resultLimitIDs.update(limitIDs)
        elif name in bonusReaders:
            bonusReaders[name](bonus, name, subSection, eventType, checkLimit=checkLimit)
        elif name in _RESERVED_NAMES:
            pass
        else:
            raise SoftException((b'Bonus {} not in bonus readers: {}').format(name, bonusReaders.keys()))

    return (
     resultLimitIDs, bonus)
