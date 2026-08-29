import itertools
from collections import namedtuple
from enum import Enum, unique
from gui.shared.money import MONEY_UNDEFINED
from shared_utils import CONST_CONTAINER
SPA_ID_TYPES = (
 int, long)
VehicleOfferEntry = namedtuple(b'VehicleOfferEntry', (b'id', b'eventType', b'rent', b'crew', b'name', b'label', b'left', b'buyPrice', b'bestOffer', b'buyParams', b'preferred'))
VehicleOfferEntry.__new__.__defaults__ = (
 b'', None, None, None, b'Unnamed', b'Unnamed', (), MONEY_UNDEFINED, None, None, False)
ItemPackEntry = namedtuple(b'ItemPackEntry', (b'type', b'id', b'count', b'groupID', b'compensation', b'iconSource', b'title', b'description', b'extra'))
ItemPackEntry.__new__.__defaults__ = (
 None, None, None, None, None, None, b'', b'', {})

class _Enum(Enum):

    @classmethod
    def hasValue(cls, value):
        return value in cls._value2member_map_


@unique
class TManLocation(_Enum):
    NEWBIES = b'newbies'
    BARRACKS = b'barracks'
    TANKS = b'tanks'
    DEMOBILIZED = b'demobilized'


@unique
class TManGender(_Enum):
    MALE = b'male'
    FEMALE = b'female'


class ShopItemType(CONST_CONTAINER):
    VEHICLE = b'vehicle'
    CREW = b'crew'
    EQUIPMENT = b'equipment'
    DEVICE = b'device'
    BOOSTER = b'booster'
    BATTLE_BOOSTER = b'battleBooster'
    MODULE = b'module'
    SHELL = b'shell'
    PREMIUM = b'premium'
    PAINT = b'paint'
    CAMOUFLAGE = b'camouflage'
    MODIFICATION = b'modification'
    STYLE = b'style'
    DECAL = b'decal'
    EMBLEM = b'emblem'
    INSCRIPTION = b'inscription'
    PROJECTION_DECAL = b'projectionDecal'
    ENHANCEMENT = b'enhancements'
    CREW_BOOKS = b'crew_books'


class ItemPackType(CONST_CONTAINER):
    VEHICLE = b'vehicle'
    VEHICLE_LIGHT = b'vehicle/lightTank'
    VEHICLE_MEDIUM = b'vehicle/mediumTank'
    VEHICLE_HEAVY = b'vehicle/heavyTank'
    VEHICLE_AT_SPG = b'vehicle/AT-SPG'
    VEHICLE_SPG = b'vehicle/SPG'
    ITEM_EQUIPMENT = b'item/equipment'
    ITEM_DEVICE = b'item/optionalDevice'
    ITEM_SHELL = b'item/shell'
    ITEM_CREW_SKIN = b'item/crewSkin'
    GOODIE_GOLD = b'goodie/gold'
    GOODIE_CREDITS = b'goodie/credits'
    GOODIE_EXPERIENCE = b'goodie/experience'
    GOODIE_FREE_EXPERIENCE = b'goodie/free_experience'
    GOODIE_CREW_EXPERIENCE = b'goodie/crew_experience'
    GOODIE_FREE_AND_CREW_EXPERIENCE = b'goodie/free_xp_and_crew_xp'
    GOODIE_FRONTLINE_EXPERIENCE = b'goodie/fl_experience'
    GOODIE_RECERTIFICATIONFORM = b'goodie/recertificationForm'
    CREW_50 = b'crew/50'
    CREW_75 = b'crew/75'
    CREW_100 = b'crew/100'
    CUSTOM_CREW_100 = b'custom_crew/100'
    CREW_BUNDLE = b'crew/bundle'
    CREW_CUSTOM = b'crew/custom'
    CUSTOM_PREMIUM = b'custom/premium'
    CUSTOM_PREMIUM_PLUS = b'custom/premium_plus'
    CUSTOM_CRYSTAL = b'custom/crystal'
    CUSTOM_GOLD = b'custom/gold'
    CUSTOM_CREDITS = b'custom/credits'
    CUSTOM_FREE_XP = b'custom/freeXP'
    CUSTOM_DOG_TAG = b'custom/dogTagComponents'
    CUSTOM_EVENT_COIN = b'custom/eventCoin'
    CUSTOM_EVENT_COIN_EXTERNAL = b'custom/event_coin'
    CUSTOM_BPCOIN = b'custom/bpcoin'
    CUSTOM_EQUIP_COIN = b'custom/equip_coin'
    EQUIP_COIN = b'custom/equipCoin'
    CUSTOM_SLOT = b'custom/slot'
    CUSTOM_SEVERAL_SLOTS = b'custom/slots'
    CUSTOM_REFERRAL_CREW = b'custom/crew'
    CUSTOM_SUPPLY_POINT = b'custom/supply_point'
    CUSTOM_BATTLE_PASS_POINTS = b'custom/battlePassPoints'
    CUSTOM_X5_BATTLE_BONUS = b'custom/X5_battle'
    CUSTOM_COLLECTION_ENTITLEMENT = b'custom/collectionItem'
    CUSTOM_ANY_COLLECTION_ITEM = b'custom/anyCollectionItem'
    CUSTOM_X3_CREW_BONUS = b'custom/X3_crew'
    CUSTOM_LOOTBOX = b'custom/lootbox'
    CUSTOM_LOOTBOXKEY = b'custom/LootBoxKey'
    CUSTOM_BERTHS = b'custom/berths'
    CUSTOM_GOLDENTICKET = b'custom/goldenticket'
    CUSTOM_CURRENCIES = b'custom/currencies'
    TOKEN = b'token'
    PAINT_ALL = b'paint/all'
    PAINT_SUMMER = b'paint/summer'
    PAINT_WINTER = b'paint/winter'
    PAINT_DESERT = b'paint/desert'
    CAMOUFLAGE_ALL = b'camouflage/all'
    CAMOUFLAGE_SUMMER = b'camouflage/summer'
    CAMOUFLAGE_WINTER = b'camouflage/winter'
    CAMOUFLAGE_DESERT = b'camouflage/desert'
    DECAL_1 = b'decal/1'
    DECAL_2 = b'decal/2'
    PROJECTION_DECAL = b'projection_decal/all'
    PERSONAL_NUMBER = b'personal_number/all'
    MODIFICATION = b'modification/all'
    STYLE = b'style/all'
    LB_STYLE_PROGRESS = b'custom/lbStyleProgress'
    ACHIEVEMENT = b'achievement'
    BADGE = b'badge'
    REFERRAL_BADGE = b'referralBadge'
    PLAYER_BADGE = b'playerBadges'
    SINGLE_ACHIEVEMENTS = b'singleAchievements'
    FRONTLINE_TOKEN = b'frontline_token'
    TRADE_IN_INFO = b'tradeInInfo'
    CREW_BOOK = b'crewBook'
    CREW_BOOK_BROCHURE = b'crew_book/brochure'
    CREW_BOOK_GUIDE = b'crew_book/guide'
    CREW_BOOK_CREW_BOOK = b'crew_book/crewBook'
    CREW_BOOK_PERSONAL_BOOK = b'crew_book/personalBook'
    CREW_BOOK_UNIVERSAL_BOOK = b'crew_book/universalBook'
    CREW_BOOK_RANDOM = b'crew_book/random'
    CREW_BOOK_UNIVERSAL_GUIDE = b'crew_book/universalGuide'
    CREW_BOOK_UNIVERSAL_BROCHURE = b'crew_book/universalBrochure'
    BLUEPRINT = b'blueprint'
    BLUEPRINT_NATIONAL = b'blueprint/national'
    BLUEPRINT_INTELEGENCE_DATA = b'blueprint/intelligence_data'
    BLUEPRINT_ANY = b'blueprint/any'
    BLUEPRINT_NATIONAL_ANY = b'blueprint/nationalAny'
    DEMOUNT_KIT = b'demountKit'
    REFERRAL_AWARDS = b'referral_awards'
    DEMOUNT_KITS = b'demountKit/common'
    OFFER = b'offer'
    OFFER_BROCHURE = b'offer/crew_book/brochure'
    OFFER_BATTLE_BOOSTER = b'offer/item/equipment'
    TMAN_TOKEN = b'tmanToken'
    ENTITLEMENTS = b'custom/entitlements'
    CUSTOM_BUMBLEE_COIN = b'custom/bumblebee_coin'
    CUSTOM_HONEY_COIN = b'custom/honey_coin'


class ItemPackTypeGroup(CONST_CONTAINER):
    ITEM = (
     ItemPackType.ITEM_SHELL,
     ItemPackType.ITEM_DEVICE,
     ItemPackType.ITEM_EQUIPMENT)
    VEHICLE = (
     ItemPackType.VEHICLE,
     ItemPackType.VEHICLE_SPG,
     ItemPackType.VEHICLE_AT_SPG,
     ItemPackType.VEHICLE_HEAVY,
     ItemPackType.VEHICLE_MEDIUM,
     ItemPackType.VEHICLE_LIGHT)
    GOODIE = (
     ItemPackType.GOODIE_GOLD,
     ItemPackType.GOODIE_CREDITS,
     ItemPackType.GOODIE_EXPERIENCE,
     ItemPackType.GOODIE_CREW_EXPERIENCE,
     ItemPackType.GOODIE_FREE_EXPERIENCE,
     ItemPackType.GOODIE_FREE_AND_CREW_EXPERIENCE,
     ItemPackType.GOODIE_FRONTLINE_EXPERIENCE)
    CAMOUFLAGE = (
     ItemPackType.CAMOUFLAGE_ALL,
     ItemPackType.CAMOUFLAGE_DESERT,
     ItemPackType.CAMOUFLAGE_SUMMER,
     ItemPackType.CAMOUFLAGE_WINTER)
    PAINT = (
     ItemPackType.PAINT_ALL,
     ItemPackType.PAINT_DESERT,
     ItemPackType.PAINT_SUMMER,
     ItemPackType.PAINT_WINTER)
    STYLE = (
     ItemPackType.STYLE,
     ItemPackType.LB_STYLE_PROGRESS)
    MODIFICATION = (
     ItemPackType.MODIFICATION,)
    DECAL = (
     ItemPackType.DECAL_1,
     ItemPackType.DECAL_2)
    PROJECTION_DECAL = (
     ItemPackType.PROJECTION_DECAL,)
    PERSONAL_NUMBER = (
     ItemPackType.PERSONAL_NUMBER,)
    CUSTOMIZATION = tuple(itertools.chain(STYLE, CAMOUFLAGE, PAINT, DECAL, PROJECTION_DECAL, PERSONAL_NUMBER, MODIFICATION))
    CUSTOM = (
     ItemPackType.CUSTOM_PREMIUM,
     ItemPackType.CUSTOM_PREMIUM_PLUS,
     ItemPackType.CUSTOM_CRYSTAL,
     ItemPackType.CUSTOM_GOLD,
     ItemPackType.CUSTOM_CREDITS,
     ItemPackType.CUSTOM_EVENT_COIN,
     ItemPackType.CUSTOM_EVENT_COIN_EXTERNAL,
     ItemPackType.CUSTOM_REFERRAL_CREW,
     ItemPackType.CUSTOM_SLOT,
     ItemPackType.CUSTOM_SUPPLY_POINT,
     ItemPackType.CUSTOM_BUMBLEE_COIN,
     ItemPackType.CUSTOM_HONEY_COIN,
     ItemPackType.CUSTOM_GOLDENTICKET)
    CREW = (
     ItemPackType.CREW_50,
     ItemPackType.CREW_75,
     ItemPackType.CREW_100,
     ItemPackType.CUSTOM_CREW_100,
     ItemPackType.CREW_BUNDLE,
     ItemPackType.CREW_CUSTOM)
    TOKEN = (
     ItemPackType.TOKEN,)
    DISCOUNT = (
     ItemPackType.FRONTLINE_TOKEN,)
    TRADE_IN = (
     ItemPackType.TRADE_IN_INFO,)
    CREW_BOOKS = (
     ItemPackType.CREW_BOOK,
     ItemPackType.CREW_BOOK_BROCHURE,
     ItemPackType.CREW_BOOK_GUIDE,
     ItemPackType.CREW_BOOK_CREW_BOOK,
     ItemPackType.CREW_BOOK_PERSONAL_BOOK,
     ItemPackType.CREW_BOOK_UNIVERSAL_BOOK,
     ItemPackType.CREW_BOOK_UNIVERSAL_GUIDE,
     ItemPackType.CREW_BOOK_UNIVERSAL_BROCHURE)
    BLUEPRINTS = (
     ItemPackType.BLUEPRINT,
     ItemPackType.BLUEPRINT_ANY,
     ItemPackType.BLUEPRINT_NATIONAL,
     ItemPackType.BLUEPRINT_NATIONAL_ANY,
     ItemPackType.BLUEPRINT_INTELEGENCE_DATA)
    OFFER = (
     ItemPackType.OFFER_BATTLE_BOOSTER,
     ItemPackType.OFFER_BROCHURE)
    TMAN_TOKEN = {
     ItemPackType.TMAN_TOKEN}


CompensationSpec = namedtuple(b'CompensationSpec', (b'type', b'value', b'count'))

def getItemPackByGroupAndName(group, name, default=None):
    return next((itemPackName for itemPackName in group if name in itemPackName), default)


class CompensationType(CONST_CONTAINER):
    MONEY = b'money'


def sanitizeResPath(relPath):
    if relPath:
        if relPath.startswith(b'img://'):
            relPath = relPath.replace(b'img://', b'')
        if relPath.startswith(b'..'):
            relPath = b'gui' + relPath[2:]
        return relPath
    return b''
