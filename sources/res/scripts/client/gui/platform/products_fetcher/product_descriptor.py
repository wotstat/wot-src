from helpers.events_handler import EventsHandler
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from typing import Dict

class ProductDescriptor(EventsHandler):
    STOREFRONT_NAMESPACE = b'wot_subscriptions'

    def __init__(self, params):
        self._params = params
        self._isFull = False
        self._subscribe()
        return

    @property
    def productCode(self):
        return self._getFromParams(b'product_code', b'')

    @property
    def productID(self):
        return self._getFromParams(b'product_id', b'')

    @property
    def productUrl(self):
        return self._getFromParams(b'product_url', b'')

    @property
    def metadata(self):
        return self._getFromParams(b'metadata', {}).get(self.STOREFRONT_NAMESPACE, {})

    @property
    def description(self):
        return self._getFromMetadata(b'description')

    @property
    def largeImageURL(self):
        return self._getImageURL(b'large')

    @property
    def smallImageURL(self):
        return self._getImageURL(b'small')

    @property
    def mediumImageURL(self):
        return self._getImageURL(b'medium')

    @property
    def shortDescription(self):
        return self._getFromMetadata(b'short_description')

    @property
    def name(self):
        return self._getFromMetadata(b'name')

    @property
    def claimURL(self):
        return self.metadata.get(b'claimURL', {}).get(b'data', b'')

    @property
    def isDescriptorFull(self):
        return self._isFull

    def destroy(self):
        self._unsubscribe()
        return

    def extendData(self, data):
        self._isFull = True
        self._params.update(data)
        return

    def _getImageURL(self, size):
        return self.metadata.get(b'image_' + size, {}).get(b'data', {}).get(b'url', {}).get(b'value', b'')

    def _getFromParams(self, name, default=None):
        return self._params.get(name, default)

    def _getFromMetadata(self, valueName):
        return self.metadata.get(valueName, {}).get(b'data', {}).get(b'value', b'')
