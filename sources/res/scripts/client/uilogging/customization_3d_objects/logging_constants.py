from enum import Enum
from gui.filters.carousel_filter import FILTER_KEYS
from gui.Scaleform.daapi.view.lobby.customization.shared import CustomizationTabs, CustomizationModes
from items.components.c11n_constants import AttachmentType
FEATURE = b'customization_3d_objects'

class CustomizationViewKeys(Enum):
    CUSTOMIZATION_BOTTOM_PANEL = b'customization_bottom_panel'
    HANGAR = b'hangar'
    EXTERIOR = b'exterior_view'
    ATTACHMENTS_VIDEO = b'3d_attachments_video_view'
    VEHICLES_LIST = b'vehicles_list_view'
    CUSTOMIZATION_HANGAR_3D_SCENE = b'customization_hangar_3d_scene'
    CUSTOMIZATION_FILTER_POPOVER = b'customization_filter_popover'
    VEHICLE_CAROUSEL = b'vehicle_carousel'
    VEHICLE_FILTER = b'vehicle_filter'
    CUSTOMIZATION_RARITY_REWARD_VIEW = b'customization_rarity_reward_view'


class CustomizationActions(Enum):
    CLICK = b'click'
    OPEN = b'open'
    CLOSE = b'close'


class CustomizationButtons(Enum):
    TO_THE_VIDEO = b'to_the_video_button'
    TO_EXTERIOR = b'to_exterior_button'
    TO_GARAGE = b'to_garage_button'
    VEHICLE_FILTER = b'vehicle_filter_button'
    EXTERIOR = b'exterior_button'
    VEHICLES_LIST = b'vehicles_list_button'


class CustomizationChamomileButtons(object):
    ROTATE = b'rotate_button'
    MOVE = b'move_button'
    REMOVE = b'remove_button'
    CLOSE = b'close_button'
    SCALE_1X = b'1x_scale_button'
    SCALE_2X = b'2x_scale_button'
    SCALE_3X = b'3x_scale_button'
    ALL_SCALE = (
     SCALE_1X, SCALE_2X, SCALE_3X)


class CustomizationCarouselStates(Enum):
    TOTAL_ZERO_STATE = b'total_zero_state'
    VEHICLE_ZERO_STATE = b'vehicle_zero_state'
    NON_ZERO_STATE = b'non_zero_state'
    NONE = None


class CustomizationTutorialStates(Enum):
    IS_NOT_TUTORIAL = b'is_not_tutorial'
    IS_TUTORIAL = b'is_tutorial'


class CustomizationCarouselTabs(Enum):
    PAINTS = b'paints_tab'
    CAMOUFLAGES = b'camouflage_tab'
    DECALS = b'decals_tab'
    EMBLEMS = b'emblems_tab'
    INSCRIPTIONS = b'inscriptions_tab'
    EFFECTS = b'effects_tab'
    STYLES_2D = b'2d_styles_tab'
    STYLES_3D = b'3d_styles_tab'
    ATTACHMENTS = b'3d_attachments_tab'
    STAT_TRACKERS = b'statTracker_tab'


class CustomizationCarouselModes(Enum):
    STYLE_3D = b'3d_style_mode'
    STYLE_2D = b'2d_style_mode'
    CUSTOM = b'custom_mode'
    EDITABLE_STYLE = b'editable_style_mode'


class VehicleCustomizationFilterButtons(Enum):
    OWN_3D_STYLE = b'vehicle_3d_style_filter_button'
    CAN_INSTALL_ATTACHMENTS = b'vehicle_3d_attachment_filter_button'


class CustomizationAttachmentSlots(Enum):
    UNIVERSAL = b'3d_attachment_universal_anchor'
    GUN_MANTLET = b'3d_attachment_gun_mantlet_anchor'
    TURRET = b'3d_attachment_turret_anchor'
    GUN = b'3d_attachment_gun_anchor'


class CustomizationFilterButtons(Enum):
    FANTASTICAL = b'fictional_button'
    NON_HISTORIC = b'non_historic_button'
    HISTORIC = b'historic_button'
    IN_DEPOT = b'in_depot_button'
    APPLIED = b'applied_button'
    RESET_FILTER = b'reset_filter_button'
    RARITY_TEMPLATE = b'{}_button'
    ALL_GROUPS = b'all_groups'
    GROUP_TEMPLATE = b'{}_button'


class CustomizationFilterTypes(Enum):
    GROUPS = b'groups'
    RARITY = b'rarity'
    PRIMARY = b'primary'


CUSTOMIZATION_CAROUSEL_TAB_MAPPING = {(CustomizationTabs.PAINTS): (CustomizationCarouselTabs.PAINTS), 
   (CustomizationTabs.CAMOUFLAGES): (CustomizationCarouselTabs.CAMOUFLAGES), 
   (CustomizationTabs.PROJECTION_DECALS): (CustomizationCarouselTabs.DECALS), 
   (CustomizationTabs.EMBLEMS): (CustomizationCarouselTabs.EMBLEMS), 
   (CustomizationTabs.INSCRIPTIONS): (CustomizationCarouselTabs.INSCRIPTIONS), 
   (CustomizationTabs.MODIFICATIONS): (CustomizationCarouselTabs.EFFECTS), 
   (CustomizationTabs.STYLES_2D): (CustomizationCarouselTabs.STYLES_2D), 
   (CustomizationTabs.STYLES_3D): (CustomizationCarouselTabs.STYLES_3D), 
   (CustomizationTabs.ATTACHMENTS): (CustomizationCarouselTabs.ATTACHMENTS), 
   (CustomizationTabs.STAT_TRACKERS): (CustomizationCarouselTabs.STAT_TRACKERS)}
CUSTOMIZATION_CAROUSEL_MODE_MAPPING = {(CustomizationModes.STYLE_3D): (CustomizationCarouselModes.STYLE_3D), 
   (CustomizationModes.STYLE_2D): (CustomizationCarouselModes.STYLE_2D), 
   (CustomizationModes.CUSTOM): (CustomizationCarouselModes.CUSTOM), 
   (CustomizationModes.STYLE_2D_EDITABLE): (CustomizationCarouselModes.EDITABLE_STYLE)}
VEHICLE_CUSTOMIZATION_FILTER_MAPPING = {(FILTER_KEYS.OWN_3D_STYLE): (VehicleCustomizationFilterButtons.OWN_3D_STYLE), 
   (FILTER_KEYS.CAN_INSTALL_ATTACHMENTS): (VehicleCustomizationFilterButtons.CAN_INSTALL_ATTACHMENTS)}
ATTACHMENT_TYPE_MAPPING = {(AttachmentType.UNIVERSAL): (CustomizationAttachmentSlots.UNIVERSAL), 
   (AttachmentType.GUN_MANTLET): (CustomizationAttachmentSlots.GUN_MANTLET), 
   (AttachmentType.TURRET): (CustomizationAttachmentSlots.TURRET), 
   (AttachmentType.GUN): (CustomizationAttachmentSlots.GUN), 
   (AttachmentType.GUN_STATIC): (CustomizationAttachmentSlots.GUN)}
