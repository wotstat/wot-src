from enum import Enum
FEATURE = b'shop'

class ShopLogActions(Enum):
    CLOSED = b'closed'
    DISPLAYED = b'displayed'
    VEHICLE_BUY_VIEW_PURCHASE_BUTTON_CLICKED = b'vehicle_buy_view_purchase_button_clicked'
    VEHICLE_PACK_PURCHASE_CONFIRMATION_ACCEPTED = b'vehicle_pack_purchase_confirmation_accepted'


class ShopLogKeys(Enum):
    SHOP = b'shop'
    SHOP_VIEW = b'shop_view'
    SHOP_OVERLAY = b'shop_overlay'
    STYLE_PREVIEW = b'style_preview'
    VEHICLE_BUY_VIEW = b'vehicle_buy_view'
    VEHICLE_PREVIEW = b'vehicle_preview'
    VEHICLE_PACK_PREVIEW = b'vehicle_pack_preview'
    VEHICLE_PACK_PURCHASE_CONFIRMATION = b'vehicle_pack_purchase_confirmation'


class ShopLogButtons(Enum):
    TO_PREVIEW_BUTTON = b'to_preview_button'


class ShopLogItemStates(Enum):
    CLIENT_PRODUCT = b'client_product'
    PLATFORM_PRODUCT = b'platform_product'
    WITHOUT_CREW = b'without_crew'
    WITH_SLOT = b'with_slot'
    WITH_AMMO = b'with_ammo'
    WITH_EQUIPMENT = b'with_equipment'


class ShopCloseItemStates(Enum):
    CLOSE_BUTTON = b'close_button'
    BACK_BUTTON = b'back_button'
