from __future__ import absolute_import
from gui import makeHtmlString
from gui.impl import backport
from gui.impl.gen import R
from gui.shared.money import Currency
from gui.shared.utils.functions import getAbsoluteUrl
from gui.Scaleform.genConsts.COMPONENTS import COMPONENTS
__all__ = (b'noSeason', b'swords', b'alert', b'arrow', b'xp', b'notAvailable', b'notAvailableRed', b'checkmark', b'info', b'premiumIgrBig', b'premiumIgrSmall', b'freeXP', b'nut', b'clock', b'makeImageTag', b'getRoleIcon') + Currency.ALL
_IMG_TAG_TPL = b"<img src='{0}' width='{1}' height='{2}' vspace='{3}' hspace='{4}'/>"

def _getIcon(icon, width=None, height=None, vspace=None, hspace=None):
    ctx = {}
    if width is not None:
        ctx[b'width'] = width
    if height is not None:
        ctx[b'height'] = height
    if vspace is not None:
        ctx[b'vspace'] = vspace
    if hspace is not None:
        ctx[b'hspace'] = hspace
    return makeHtmlString(b'html_templates:lobby/iconText', icon, ctx)


def noSeason():
    return _getIcon(b'noSeason')


def swords(vspace=-4):
    return _getIcon(b'swords', vspace=vspace)


def alert(vspace=-4):
    return _getIcon(b'alert', vspace=vspace)


def alertBig(vspace=-6):
    return _getIcon(b'alertBig', vspace=vspace)


def arrow(vspace=-5):
    return _getIcon(b'arrowButton', vspace=vspace)


def attention(vspace=-3):
    return _getIcon(b'attention', vspace=vspace)


def xp():
    return _getIcon(b'xp')


def credits():
    return _getIcon(Currency.CREDITS)


def creditsBig():
    return _getIcon(b'creditsBig')


def creditsExtraBig():
    return _getIcon(b'creditsExtraBig')


def notAvailable():
    return _getIcon(b'notAvailable')


def notAvailableRed():
    return _getIcon(b'notAvailableRed')


def checkmark(vspace=-4):
    return _getIcon(b'checkmark', vspace=vspace)


def check(vspace=-6, hspace=-6):
    return _getIcon(b'check', vspace=vspace, hspace=hspace)


def envelop():
    return _getIcon(b'envelope')


def info():
    return _getIcon(b'info')


def premiumIgrBig():
    return _getIcon(b'premiumIgrBig')


def premiumIgrSmall():
    return _getIcon(b'premiumIgrSmall')


def freeXP():
    return _getIcon(b'freeXP')


def freeXPExtraBig():
    return _getIcon(b'freeXPExtraBig')


def xpCost():
    return _getIcon(b'xpCost')


def xpCostBig():
    return _getIcon(b'xpCostBig')


def gold():
    return _getIcon(Currency.GOLD)


def goldBig():
    return _getIcon(b'goldBig')


def goldExtraBig():
    return _getIcon(b'goldExtraBig')


def crystal():
    return _getIcon(Currency.CRYSTAL)


def crystalBig():
    return _getIcon(b'crystalBig')


def crystalExtraBig():
    return _getIcon(b'crystalExtraBig')


def eventCoin():
    return _getIcon(Currency.EVENT_COIN)


def eventCoinBig():
    return _getIcon(b'eventCoinBig')


def bpcoin():
    return _getIcon(Currency.BPCOIN)


def bpcoinBig():
    return _getIcon(b'bpcoinBig')


def demountKit():
    return _getIcon(b'demountKit')


def wotPlus(vspace=-3):
    return _getIcon(b'wotPlus', vspace=vspace)


def divisor(vspace=-7):
    return _getIcon(b'divisor', vspace=vspace)


def nut():
    return _getIcon(b'nut')


def nutStat():
    return _getIcon(b'nutStat')


def clock():
    return _getIcon(b'clock')


def clockGold():
    return _getIcon(b'clockGold')


def quest():
    return _getIcon(b'quest')


def serverAlert():
    return _getIcon(b'serverAlert')


def markerBlocked(vspace=-2):
    return _getIcon(b'markerBlocked', vspace=vspace)


def awardList():
    return _getIcon(b'awardList')


def inProgress(vspace=-2):
    return _getIcon(b'inProgress', vspace=vspace)


def doubleCheckmark(vspace=0):
    return _getIcon(b'doubleCheckmark', vspace=vspace)


def actionBlue():
    return _getIcon(b'actionBlueBg')


def actionRed():
    return _getIcon(b'actionBlueBg')


def starYellow(vspace=-4):
    return _getIcon(b'starYellow', vspace=vspace)


def equipCoin():
    return _getIcon(b'equipIcon')


def webLink():
    return _getIcon(b'webLink')


def makeImageTag(source, width=16, height=16, vSpace=-4, hSpace=0):
    return _IMG_TAG_TPL.format(getAbsoluteUrl(source), width, height, vSpace, hSpace)


def getRoleIcon(role, vSpace=-6, width=24, height=24):
    if role == b'role_' + COMPONENTS.SPG:
        return b''
    source = backport.image(R.images.gui.maps.icons.roleExp.roles.c_24x24.dyn(role)())
    return makeImageTag(source, width=width, height=height, vSpace=vSpace)


def lightning(vSpace=-4):
    source = backport.image(R.images.gui.maps.icons.library.lightning())
    return makeImageTag(source, width=10, height=16, vSpace=vSpace)


def serverBlockerIcon():
    source = backport.image(R.images.gui.maps.icons.library.blocker())
    return makeImageTag(source, width=14, height=14, vSpace=-3)
