from __future__ import absolute_import
import logging
from collections import namedtuple
from enum import Enum
from gui.impl.gen import R
_logger = logging.getLogger(__name__)
ObtainingMethodInfo = namedtuple(b'ObtainingMethodInfo', (b'confirmation_key', b'btn_label'))

class _Enum(Enum):

    @classmethod
    def hasValue(cls, value):
        return value in cls._value2member_map_


class ObtainingMethods(_Enum):
    BUY = b'buy'
    OBTAIN_FOR_COINS = b'obtain_for_coins'
    OBTAIN_FOR_FREE = b'obtain_for_free'


SHOWCASE_STYLE_OBTAINING_METHOD_INFO = {(ObtainingMethods.BUY.value): (ObtainingMethodInfo(b'buyConfirmation', R.strings.vehicle_preview.showcaseStyleBuying.actionBtn.label.buy())), 
   (ObtainingMethods.OBTAIN_FOR_COINS.value): (ObtainingMethodInfo(b'forCoinsObtainConfirmation', R.strings.vehicle_preview.buyingPanel.buyBtn.label.forCoinsObtain())), 
   (ObtainingMethods.OBTAIN_FOR_FREE.value): (ObtainingMethodInfo(b'freeObtainConfirmation', R.strings.vehicle_preview.buyingPanel.buyBtn.label.freeObtain()))}
ITEM_PACK_OBTAINING_METHOD_INFO = {(ObtainingMethods.BUY.value): (ObtainingMethodInfo(b'buyConfirmation', R.strings.vehicle_preview.buyingPanel.buyBtn.label.buyItemPack())), 
   (ObtainingMethods.OBTAIN_FOR_FREE.value): (ObtainingMethodInfo(b'freeObtainConfirmation', R.strings.vehicle_preview.buyingPanel.buyBtn.label.freeObtain()))}

def getItemPackObtainingInfo(obtainingMethod=ObtainingMethods.BUY.value):
    return ITEM_PACK_OBTAINING_METHOD_INFO.get(obtainingMethod)


def getShowcaseStyleObtainingInfo(obtainingMethod=ObtainingMethods.BUY.value):
    return SHOWCASE_STYLE_OBTAINING_METHOD_INFO.get(obtainingMethod)
