import json, logging
from typing import TYPE_CHECKING, Set
from helpers.base64_utils import base64UrlDecode
from uilogging.base.logger import MetricsLogger
from uilogging.shop.base_loggers import ShopPreviewFlowLogger, ShopPreviewMetricsLogger
from uilogging.shop.logging_constants import FEATURE, ShopLogActions, ShopLogKeys, ShopLogButtons, ShopLogItemStates, ShopCloseItemStates
from wotdecorators import noexcept
if TYPE_CHECKING:
    from uilogging.types import ItemType, ItemStateType, InfoType
_logger = logging.getLogger(__name__)

class ShopMetricsLogger(MetricsLogger):
    __slots__ = (b'_item',)

    def __init__(self, item):
        super(ShopMetricsLogger, self).__init__(FEATURE)
        self._item = item
        return

    @noexcept
    def onViewClosed(self):
        self.log(action=ShopLogActions.CLOSED, item=self._item)
        return


class ShopBuyVehicleMetricsLogger(MetricsLogger):
    __slots__ = (b'_uniqueItemCode', b'_itemStates')

    def __init__(self, uniqueItemCode):
        super(ShopBuyVehicleMetricsLogger, self).__init__(FEATURE)
        self._itemStates = set()
        self._uniqueItemCode = uniqueItemCode
        return

    def reset(self):
        super(ShopBuyVehicleMetricsLogger, self).reset()
        self.clearItemStates()
        return

    def clearItemStates(self):
        self._itemStates.clear()
        return

    @noexcept
    def onViewOpen(self):
        self.log(action=ShopLogActions.DISPLAYED, item=ShopLogKeys.VEHICLE_BUY_VIEW, info=(b'vehicle_{0}').format(self._uniqueItemCode), itemState=ShopLogItemStates.CLIENT_PRODUCT)
        return

    @noexcept
    def onViewClosed(self):
        self.log(action=ShopLogActions.CLOSED, item=ShopLogKeys.VEHICLE_BUY_VIEW, info=(b'vehicle_{0}').format(self._uniqueItemCode), itemState=ShopLogItemStates.CLIENT_PRODUCT)
        return

    @noexcept
    def logVehiclePurchaseButtonClicked(self):
        self.addItemState(ShopLogItemStates.CLIENT_PRODUCT.value)
        self.log(action=ShopLogActions.VEHICLE_BUY_VIEW_PURCHASE_BUTTON_CLICKED, item=ShopLogKeys.VEHICLE_BUY_VIEW, info=(b'vehicle_{0}').format(self._uniqueItemCode), itemState=(b';').join(self._itemStates))
        return

    def addItemState(self, itemState):
        self._itemStates.add(itemState)
        return


class ShopVehiclePreviewFlowLogger(ShopPreviewFlowLogger):
    __slots__ = ()

    @noexcept
    def logOpenPreview(self):
        self.log(action=ShopLogActions.DISPLAYED, sourceItem=ShopLogKeys.SHOP, destinationItem=ShopLogKeys.VEHICLE_PREVIEW, transitionMethod=ShopLogButtons.TO_PREVIEW_BUTTON)
        return


class ShopBundleVehiclePreviewFlowLogger(ShopPreviewFlowLogger):
    __slots__ = ()

    @noexcept
    def logOpenPreview(self):
        self.log(action=ShopLogActions.DISPLAYED, sourceItem=ShopLogKeys.SHOP, destinationItem=ShopLogKeys.VEHICLE_PACK_PREVIEW, transitionMethod=ShopLogButtons.TO_PREVIEW_BUTTON)
        return


class ShopVehicleStylePreviewFlowLogger(ShopPreviewFlowLogger):
    __slots__ = ()

    @noexcept
    def logOpenPreview(self):
        self.log(action=ShopLogActions.DISPLAYED, sourceItem=ShopLogKeys.SHOP, destinationItem=ShopLogKeys.STYLE_PREVIEW, transitionMethod=ShopLogButtons.TO_PREVIEW_BUTTON)
        return


class ShopVehiclePreviewMetricsLogger(ShopPreviewMetricsLogger):
    __slots__ = (b'_uniqueItemCode',)

    def __init__(self, uniqueItemCode):
        super(ShopVehiclePreviewMetricsLogger, self).__init__()
        self._uniqueItemCode = uniqueItemCode
        return

    @noexcept
    def onViewOpen(self):
        self.log(action=ShopLogActions.DISPLAYED, item=ShopLogKeys.VEHICLE_PREVIEW, info=(b'vehicle_{0}').format(self._uniqueItemCode), itemState=ShopLogItemStates.CLIENT_PRODUCT)
        return

    @noexcept
    def onViewClosed(self, closeItemState):
        self.log(action=ShopLogActions.CLOSED, item=ShopLogKeys.VEHICLE_PREVIEW, info=(b'vehicle_{0}').format(self._uniqueItemCode), itemState=(b'{0};{1}').format(ShopLogItemStates.CLIENT_PRODUCT.value, closeItemState))
        return


class ShopBundleVehiclePreviewMetricsLogger(ShopPreviewMetricsLogger):
    __slots__ = (b'_uniqueItemCode',)

    def __init__(self, uniqueItemCode):
        super(ShopBundleVehiclePreviewMetricsLogger, self).__init__()
        self._uniqueItemCode = uniqueItemCode
        return

    @noexcept
    def onViewOpen(self):
        self.log(action=ShopLogActions.DISPLAYED, item=ShopLogKeys.VEHICLE_PACK_PREVIEW, info=self._uniqueItemCode, itemState=ShopLogItemStates.PLATFORM_PRODUCT)
        return

    @noexcept
    def onViewClosed(self, closeItemState):
        self.log(action=ShopLogActions.CLOSED, item=ShopLogKeys.VEHICLE_PACK_PREVIEW, info=self._uniqueItemCode, itemState=(b'{0};{1}').format(ShopLogItemStates.PLATFORM_PRODUCT.value, closeItemState))
        return

    @noexcept
    def logOpenPurchaseConfirmation(self):
        self.log(action=ShopLogActions.DISPLAYED, item=ShopLogKeys.VEHICLE_PACK_PURCHASE_CONFIRMATION, info=self._uniqueItemCode, itemState=ShopLogItemStates.PLATFORM_PRODUCT)
        return

    @noexcept
    def logBundlePurchased(self):
        self.log(action=ShopLogActions.VEHICLE_PACK_PURCHASE_CONFIRMATION_ACCEPTED, item=ShopLogKeys.VEHICLE_PACK_PURCHASE_CONFIRMATION, info=self._uniqueItemCode, itemState=ShopLogItemStates.PLATFORM_PRODUCT)
        return

    @noexcept
    def logPurchaseConfirmationClosed(self):
        self.log(action=ShopLogActions.CLOSED, item=ShopLogKeys.VEHICLE_PACK_PURCHASE_CONFIRMATION, info=self._uniqueItemCode, itemState=ShopLogItemStates.PLATFORM_PRODUCT)
        return


class ShopVehicleStylePreviewMetricsLogger(ShopPreviewMetricsLogger):
    __slots__ = (b'_uniqueItemCode',)

    def __init__(self, uniqueItemCode):
        super(ShopVehicleStylePreviewMetricsLogger, self).__init__()
        self._uniqueItemCode = uniqueItemCode
        return

    @noexcept
    def onViewOpen(self):
        self.log(action=ShopLogActions.DISPLAYED, item=ShopLogKeys.STYLE_PREVIEW, info=(b'style_{0}').format(self._uniqueItemCode), itemState=ShopLogItemStates.CLIENT_PRODUCT)
        return

    @noexcept
    def onViewClosed(self):
        self.log(action=ShopLogActions.CLOSED, item=ShopLogKeys.STYLE_PREVIEW, info=(b'style_{0}').format(self._uniqueItemCode), itemState=(b'{0};{1}').format(ShopLogItemStates.CLIENT_PRODUCT.value, ShopCloseItemStates.BACK_BUTTON.value))
        return


def getPreviewUILoggers(isBundlePack, vehicleCD, buyParams):
    if isBundlePack:
        productCode = getProductCodeForPreviewLog(buyParams)
        if not productCode:
            _logger.warning(b'[SHOPUILOG] ShopBundleVehiclePreviewMetricsLogger expects uniqueItemCode but it is none.')
            productCode = (b'UNKNOWN_PRODUCT_CODE_{0}').format(vehicleCD)
        return (ShopBundleVehiclePreviewMetricsLogger(productCode), ShopBundleVehiclePreviewFlowLogger())
    return (
     ShopVehiclePreviewMetricsLogger(vehicleCD), ShopVehiclePreviewFlowLogger())


@noexcept
def getProductCodeForPreviewLog(buyParams):
    if buyParams is not None:
        partialProduct = buyParams.get(b'partialProduct')
        if partialProduct:
            decodeValue = base64UrlDecode(partialProduct)
            if decodeValue:
                return json.loads(decodeValue).get(b'productCode')
    return
