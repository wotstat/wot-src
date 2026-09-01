from __future__ import absolute_import
from functools import partial
import SoundGroups
from constants import GF_RES_PROTOCOL
from gui.impl.gen.view_models.views.lobby.hangar.sub_views.teaser_model import TeaserModel, Type
from gui.impl.pub.view_component import ViewComponent
from gui.promo.constants import PROMO_SOUNDS
from gui.promo.promo_logger import PromoLogActions
from gui.shared.image_helper import ImageHelper, getTextureLinkByID
from helpers import dependency
from skeletons.gui.game_control import IPromoController
from skeletons.gui.shared.promo import IPromoLogger

class TeaserPresenter(ViewComponent[TeaserModel]):
    _SALE_PROMO_TYPE = b'hot_stock'
    _promoController = dependency.descriptor(IPromoController)

    def __init__(self):
        super(TeaserPresenter, self).__init__(model=TeaserModel, enabled=False)
        self.__imageId = None
        self.__teaserData = None
        self.__promoCount = 0
        self.__showCallback = None
        self.__closeCallback = None
        self.__shouldShow = False
        return

    def prepare(self):
        self._promoController.subscribePresenter(self.__onTeaserReceived)
        return

    @property
    def viewModel(self):
        return super(TeaserPresenter, self).getViewModel()

    def _finalize(self):
        self._promoController.unsubscribePresenter(self.__onTeaserReceived)
        self.__clear()
        super(TeaserPresenter, self)._finalize()
        return

    def _getEvents(self):
        return (
         (
          self.viewModel.onClose, self.__onClose),
         (
          self.viewModel.onClick, self.__onClick))

    def __clear(self):
        if self.__imageId:
            ImageHelper.removeTextureFromMemory(self.__imageId)
        if self.__teaserData:
            dependency.instance(IPromoLogger).logTeaserAction(self.__teaserData, action=PromoLogActions.KILLED_BY_SYSTEM)
            self.__closeCallback(False)
        self.__teaserData = None
        self.__promoCount = 0
        self.__imageId = None
        self.__showCallback = None
        self.__closeCallback = None
        self.__shouldShow = False
        return

    def __onTeaserReceived(self, teaserData, showCallback, closeCallback):
        self.__shouldShow = True
        self.setEnabled(self._promoController.isActive() and self.__shouldShow)
        self.__showCallback = showCallback
        self.__closeCallback = closeCallback
        self.__prepareData(teaserData, self._promoController.getPromoCount())
        return

    def __prepareData(self, teaserData, promoCount):
        self.__teaserData = teaserData
        self.__promoCount = promoCount
        teaserID = teaserData[b'promoID']
        ImageHelper.requestImageByUrl(self.__teaserData[b'image'], partial(self.__onImageLoaded, teaserID))
        return

    def __onImageLoaded(self, requestedTeaserID, image):
        if not self.__teaserData or self.__teaserData[b'promoID'] != requestedTeaserID:
            return
        if self.__imageId:
            ImageHelper.removeTextureFromMemory(self.__imageId)
        self.__imageId = ImageHelper.getMemoryTexturePath(image, False)
        isSalesPromoType = self.__teaserData.get(b'promoType') == self._SALE_PROMO_TYPE
        with self.viewModel.transaction() as model:
            model.setPostCounter(self.__promoCount)
            model.setDescription(self.__teaserData[b'description'])
            model.setText(self.__teaserData.get(b'version', b''))
            model.setIsVideo(bool(self.__teaserData.get(b'video')))
            if self.__teaserData.get(b'finishTime'):
                model.setFinishTime(self.__teaserData.get(b'finishTime', -1))
            model.setType(Type.SHOPPROMO if isSalesPromoType else Type.NEWS)
            model.setImage(getTextureLinkByID(self.__imageId, GF_RES_PROTOCOL.CACHED_IMG))
        SoundGroups.g_instance.playSound2D(PROMO_SOUNDS.SALE_TEASER if isSalesPromoType else PROMO_SOUNDS.INFO_TEASER)
        self.__showCallback(self.__teaserData.get(b'promoID'))
        return

    def __onClose(self, byUser=True):
        logAction = PromoLogActions.CLOSED_BY_USER if byUser else PromoLogActions.KILLED_BY_SYSTEM
        dependency.instance(IPromoLogger).logTeaserAction(self.__teaserData, action=logAction)
        if self.__closeCallback:
            self.__closeCallback(byUser)
        self.__teaserData = None
        self.__shouldShow = False
        self.setEnabled(False)
        self.__clear()
        return

    def __onClick(self):
        self._promoController.showLastTeaserPromo()
        if self.__closeCallback:
            self.__closeCallback(True)
        return
