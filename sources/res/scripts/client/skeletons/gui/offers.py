import typing
from skeletons.gui import INovelty
if typing.TYPE_CHECKING:
    from typing import Callable, Dict, Iterable, Optional, Union, List
    from account_helpers.offers.events_data import OfferEventData
    from Event import Event

class IOffersNovelty(INovelty):

    def saveAsSeen(self, offerId):
        raise NotImplementedError
        return


class IOffersBannerController(object):
    onShowBanners = None
    onHideBanners = None

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def isEnabled(self):
        raise NotImplementedError
        return

    def showBanners(self):
        raise NotImplementedError
        return

    def hideBanners(self):
        raise NotImplementedError
        return


class IOffersDataProvider(object):
    onOffersUpdated = None

    def init(self):
        raise NotImplementedError
        return

    def fini(self):
        raise NotImplementedError
        return

    def start(self):
        raise NotImplementedError
        return

    def stop(self):
        raise NotImplementedError
        return

    def update(self, diff):
        raise NotImplementedError
        return

    @property
    def isSynced(self):
        raise NotImplementedError
        return

    def getReceivedGifts(self, offerID):
        raise NotImplementedError
        return

    def isBannerSeen(self, offerID):
        raise NotImplementedError
        return

    def isCdnResourcesReady(self, callback=None, timeout=0):
        raise NotImplementedError
        return

    def getCdnResourcePath(self, cdnRelativePath, relative=True):
        raise NotImplementedError
        return

    def getOffer(self, offerID):
        raise NotImplementedError
        return

    def getOfferByToken(self, token):
        raise NotImplementedError
        return

    def getOfferByGiftToken(self, giftToken):
        raise NotImplementedError
        return

    def getAllOffers(self):
        raise NotImplementedError
        return

    def iAvailableOffers(self, onlyVisible=True):
        raise NotImplementedError
        return

    def getAvailableOffers(self, onlyVisible=True):
        raise NotImplementedError
        return

    def getAvailableOffersByToken(self, token):
        raise NotImplementedError
        return

    def isOfferAvailable(self, tokenID):
        raise NotImplementedError
        return

    def getAmountOfGiftsGenerated(self, tokenID, mainTokenCount):
        raise NotImplementedError
        return
