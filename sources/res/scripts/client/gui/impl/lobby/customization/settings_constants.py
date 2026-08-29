from shared_utils import getFullClassName
from skeletons.account_helpers.settings_repository import SettingsSerializable
APPLY_TO_ALL_SEASONS_ENABLED = b'applyToAllSeasonsEnabled'
CAROUSEL_ARROWS_HINT_SHOWN_FIELD = b'isCarouselsArrowsHintShown'
CUSTOMIZATION_STYLE_ITEMS_VISITED = b'CustomizationStyleItemsVisited'
IS_CUSTOMIZATION_INTRO_VIEWED = b'isCustomizationIntroViewed'
IS_AUTO_RENT_ENABLED_SET = b'isAutoRentEnabledSet'
AUTO_RENT_GLOBAL_CD = 0

class CustomizationFilter(object):
    CUSTOMIZATION_FILTER = b'customizationFilter'
    CAMOUFLAGE_GROUP = b'camouflageGroup'
    PAINTS_GROUP = b'paintsGroup'
    PROJECTION_DECALS_GROUP = b'projectionDecalsGroup'
    EMBLEMS_GROUP = b'emblemsGroup'
    INSCRIPTIONS_GROUP = b'inscriptionsGroup'
    STYLES_2D_GROUP = b'styles2dGroup'
    STYLES_3D_GROUP = b'styles3dGroup'
    DISPLAY_GROUP = b'displayGroup'
    FORMFACTOR_SQUARE = b'formfactor_square'
    FORMFACTOR_RECT1X2 = b'formfactor_rect1x2'
    FORMFACTOR_RECT1X3 = b'formfactor_rect1x3'
    FORMFACTOR_RECT1X4 = b'formfactor_rect1x4'
    FORMFACTOR_RECT1X6 = b'formfactor_rect1x6'
    HISTORIC = b'historic'
    NON_HISTORIC = b'nonHistoric'
    FANTASTICAL = b'fantastical'
    INVENTORY = b'inventory'
    SALE = b'sale'
    APPLIED = b'applied'
    FAVORITE = b'favorite'
    ON_ANOTHER_VEH = b'onAnotherVeh'
    ONLY_PROGRESSION_DECALS = b'onlyProgressionDecals'
    ONLY_EDITABLE_STYLES = b'onlyEditableStyles'
    ONLY_NON_EDITABLE_STYLES = b'onlyNonEditableStyles'
    ONLY_PROGRESSION_STYLES = b'onlyProgressionStyles'


def getCustomizationFilterDefaults():
    return {(CustomizationFilter.CAMOUFLAGE_GROUP): (-1), 
       (CustomizationFilter.PAINTS_GROUP): (-1), 
       (CustomizationFilter.PROJECTION_DECALS_GROUP): (-1), 
       (CustomizationFilter.EMBLEMS_GROUP): (-1), 
       (CustomizationFilter.INSCRIPTIONS_GROUP): (-1), 
       (CustomizationFilter.STYLES_2D_GROUP): (-1), 
       (CustomizationFilter.STYLES_3D_GROUP): (-1), 
       (CustomizationFilter.DISPLAY_GROUP): 0, 
       (CustomizationFilter.FORMFACTOR_SQUARE): False, 
       (CustomizationFilter.FORMFACTOR_RECT1X2): False, 
       (CustomizationFilter.FORMFACTOR_RECT1X3): False, 
       (CustomizationFilter.FORMFACTOR_RECT1X4): False, 
       (CustomizationFilter.FORMFACTOR_RECT1X6): False, 
       (CustomizationFilter.HISTORIC): False, 
       (CustomizationFilter.NON_HISTORIC): False, 
       (CustomizationFilter.FANTASTICAL): False, 
       (CustomizationFilter.INVENTORY): False, 
       (CustomizationFilter.APPLIED): False, 
       (CustomizationFilter.SALE): False, 
       (CustomizationFilter.FAVORITE): False, 
       (CustomizationFilter.ON_ANOTHER_VEH): False, 
       (CustomizationFilter.ONLY_PROGRESSION_DECALS): False, 
       (CustomizationFilter.ONLY_EDITABLE_STYLES): False, 
       (CustomizationFilter.ONLY_NON_EDITABLE_STYLES): False, 
       (CustomizationFilter.ONLY_PROGRESSION_STYLES): False}


class CustomizationSettingsSerializable(SettingsSerializable):

    @classmethod
    def getSettingsID(cls):
        return getFullClassName(CustomizationSettingsSerializable)
