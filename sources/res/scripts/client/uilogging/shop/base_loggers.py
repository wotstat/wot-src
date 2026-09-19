from __future__ import absolute_import
import logging
from uilogging.base.logger import FlowLogger, MetricsLogger
from uilogging.shop.logging_constants import FEATURE
_logger = logging.getLogger(__name__)

class ShopPreviewFlowLogger(FlowLogger):
    __slots__ = ()

    def __init__(self):
        super(ShopPreviewFlowLogger, self).__init__(FEATURE)
        return

    def logOpenPreview(self):
        raise NotImplementedError
        return


class ShopPreviewMetricsLogger(MetricsLogger):
    __slots__ = ()

    def __init__(self):
        super(ShopPreviewMetricsLogger, self).__init__(FEATURE)
        return

    def onViewOpen(self, *args, **kwargs):
        raise NotImplementedError
        return

    def onViewClosed(self, *args, **kwargs):
        raise NotImplementedError
        return

    def logOpenPurchaseConfirmation(self):
        _logger.warning(b'[SHOPUILOG] %s not implemented logOpenPurchaseConfirmation.', self.__class__.__name__)
        return

    def logBundlePurchased(self):
        _logger.warning(b'[SHOPUILOG] %s not implemented logBundlePurchased.', self.__class__.__name__)
        return

    def logPurchaseConfirmationClosed(self):
        _logger.warning(b'[SHOPUILOG] %s not implemented logPurchaseConfirmationClosed.', self.__class__.__name__)
        return
