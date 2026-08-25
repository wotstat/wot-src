import typing, enum

class EnumWithValues(enum.Enum):

    @classmethod
    def values(cls):
        return [obj.value for obj in cls.__members__.values()]


@enum.unique
class ImageVfxs(str, EnumWithValues):
    DUST = b'dust'
    FIRE = b'fire'
    FOG = b'fog'
    RAIN = b'rain'
    SNOW = b'snow'
    SUNSHINE = b'sunshine'


@enum.unique
class LoadingTypes(str, EnumWithValues):
    CLIENT = b'client'
    PLAYER = b'player'


@enum.unique
class MilestonesTypes(str, EnumWithValues):
    DEFAULT = b'default'
    STANDARD = b'standard'


@enum.unique
class Milestones(str, EnumWithValues):
    CLIENT_LOADING = b'client_loading'
    SAVING_PDC = b'saving_pdc'
    CONNECTION = b'connection'
    ENTER = b'enter'
    INVENTORY = b'inventory'
    SHOP = b'shop'
    DOSSIER = b'dossier'
    DISCOUNTS = b'discounts'
    RECYCLE_BIN = b'recycleBin'
    PLAYER_DATA = b'playerData'
    HANGAR_SPACE = b'loadHangarSpace'
    UPDATE_VEHICLE = b'updateVehicle'
    HANGAR_SPACE_VEHICLE = b'loadHangarSpaceVehicle'
    HANGAR_UI_READY = b'hangarUIReady'
    HANGAR_READY = b'hangarReady'
    LOAD_CONTENT = b'loadContent'
    SYNCHRONIZE = b'synchronize'
    ONBOARDING_ENQUEUED = b'onboardingEnqueued'


@enum.unique
class InfoStyles(str, EnumWithValues):
    DEFAULT = b'default'
    KOREA = b'korea'
    CHINA = b'china'
