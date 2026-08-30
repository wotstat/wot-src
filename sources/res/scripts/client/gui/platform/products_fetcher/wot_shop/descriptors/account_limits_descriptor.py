from gui.platform.products_fetcher.product_descriptor import ProductDescriptor

class AccountLimitsDescriptor(ProductDescriptor):

    @property
    def limitedQuantity(self):
        return self._getFromParams(b'limited_quantity', {})

    @property
    def purchaseAllowed(self):
        return self.limitedQuantity[b'purchase_allowed']

    @property
    def personalCount(self):
        return self.limitedQuantity[b'personal_count']

    @property
    def personalLimit(self):
        return self.limitedQuantity[b'personal_limit']
