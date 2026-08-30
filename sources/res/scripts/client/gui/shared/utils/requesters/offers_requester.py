from __future__ import absolute_import
import BigWorld
from gui.shared.utils.requesters.abstract import AbstractSyncDataRequester
from skeletons.gui.shared.utils.requesters import IOffersRequester

class OffersRequester(AbstractSyncDataRequester, IOffersRequester):

    def getReceivedGifts(self, offerID):
        return self.__getOffer(offerID).get(b'gifts', {})

    def isBannerSeen(self, offerID):
        return self.__getOffer(offerID).get(b'bannerSeen', False)

    def _requestCache(self, callback=None):
        BigWorld.player().offers.getCache((lambda resID, value: self._response(resID, value, callback)))
        return

    def __getOffer(self, offerID):
        return self.getCacheValue(b'offersData', {}).get(offerID, {})
