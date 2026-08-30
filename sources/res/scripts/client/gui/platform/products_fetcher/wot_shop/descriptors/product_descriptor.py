from gui.platform.products_fetcher.product_descriptor import ProductDescriptor as BaseDescriptor

class ProductDescriptor(BaseDescriptor):

    @property
    def productID(self):
        return self._getFromParams(b'id', b'')

    @property
    def productCode(self):
        return self._getFromParams(b'code', b'')

    @property
    def categories(self):
        return self._getFromParams(b'categories', [])

    @property
    def category(self):
        return self.categories[0]

    @property
    def purchasable(self):
        return self._getFromParams(b'purchasable', False)

    @property
    def price(self):
        return self._getFromParams(b'price', {})

    @property
    def currencyName(self):
        return self.price.get(b'currency')

    @property
    def originalPrice(self):
        return self.price.get(b'value')

    @property
    def promotion(self):
        return self._getFromParams(b'promotion', {})

    @property
    def discountPrice(self):
        if self.promotion:
            return self.promotion.get(b'discounted_cost', 0)
        return 0

    @property
    def entitlements(self):
        return self._getFromParams(b'entitlements', [])

    @property
    def description(self):
        return self._getFromParams(b'description', b'')
