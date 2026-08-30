import types
from gui import makeHtmlString
from gui.shared.money import Currency
from helpers import i18n
from soft_exception import SoftException
__all__ = (
 b'standard',
 b'main',
 b'mainBig',
 b'neutral',
 b'stats',
 b'statInfo',
 b'statusAttention',
 b'statusAlert',
 b'statusAttention',
 b'middleTitle',
 b'highTitle',
 b'highTitleRegular',
 b'highTitleAccented',
 b'highTitleDisabled',
 b'disabled',
 b'promoTitle',
 b'promoSubTitle',
 b'alert',
 b'alertBig',
 b'success',
 b'statsIncrease',
 b'error',
 b'warning',
 b'critical',
 b'expText',
 b'statsDecrease',
 b'expTextBig',
 Currency.GOLD,
 Currency.CREDITS,
 Currency.CRYSTAL,
 b'defRes',
 b'counter',
 b'titleFont',
 b'tutorial',
 b'playerOnline',
 b'getRawStyles',
 b'getStyles',
 b'concatStylesToSingleLine',
 b'concatStylesToMultiLine',
 b'superPromoTitle',
 b'superPromoTitleEm',
 b'highlightText',
 b'unavailable',
 b'missionStatusAvailable',
 b'epicTitle',
 b'epicTitleYellow',
 b'heroTitle',
 b'heroTitleYellow',
 b'heroTitleTK',
 b'grandTitle',
 b'grandTitleYellow',
 b'grandTitleTK',
 b'grandTitleRed',
 b'textEpic',
 b'yellowText',
 b'greenText',
 b'poiCapturedBoldText',
 b'poiCapturedRegularText',
 b'whiteTitle15',
 b'whiteTitle12')

def _getStyle(style, ctx=None):
    if ctx is None:
        ctx = {}
    return makeHtmlString(b'html_templates:lobby/textStyle', style, ctx)


def _formatText(style, text=b''):
    if isinstance(text, types.StringTypes) and i18n.isValidKey(text):
        text = i18n.makeString(text)
    return _getStyle(style, {b'message': text})


def standard(text):
    return _formatText(b'standardText', text)


def locked(text):
    return _formatText(b'lockedText', text)


def main(text):
    return _formatText(b'mainText', text)


def mainSmall(text):
    return _formatText(b'mainTextSmall', text)


def mainBig(text):
    return _formatText(b'mainBigText', text)


def neutral(text):
    return _formatText(b'neutralText', text)


def neutralBig(text):
    return _formatText(b'neutralTextBig', text)


def goodPing(text):
    return _formatText(b'goodPingText', text)


def standartPing(text):
    return _formatText(b'standartPingText', text)


def stats(text):
    return _formatText(b'statsText', text)


def rewards(text):
    return _formatText(b'rewardsText', text)


def h15ParSecondary(text):
    return _formatText(b'h15ParSecondary', text)


def statInfo(text):
    return _formatText(b'statusInfoText', text)


def statusAlert(text):
    return _formatText(b'statusAlert', text)


def statusAttention(text):
    return _formatText(b'statusAttention', text)


def middleTitle(text):
    return _formatText(b'middleTitle', text)


def middleTitleLocked(text):
    return _formatText(b'middleTitleLocked', text)


def middleBonusTitle(text):
    return _formatText(b'middleBonusTitle', text)


def highTitle(text):
    return _formatText(b'highTitle', text)


def highTitleRegular(text):
    return _formatText(b'highTitleRegular', text)


def highTitleAccented(text):
    return _formatText(b'highTitleAccented', text)


def highTitleDisabled(text):
    return _formatText(b'highTitleDisabled', text)


def goldTextBig(text):
    return _formatText(b'goldTextBig', text)


def creditsTextBig(text):
    return _formatText(b'creditsTextBig', text)


def goldTextNormalCard(text):
    return _formatText(b'goldTextNormalCard', text)


def creditsTextNormalCard(text):
    return _formatText(b'creditsTextNormalCard', text)


def expTextBig(text):
    return _formatText(b'expTextBig', text)


def errCurrencyTextBig(text):
    return _formatText(b'errCurrencyTextBig', text)


def disabled(text):
    return _formatText(b'disabledText', text)


def promoTitle(text):
    return _formatText(b'promoTitle', text)


def bonusLocalText(text):
    return _formatText(b'bonusLocalText', text)


def bonusLocalInfoTipText(text):
    return _formatText(b'bonusLocalInfoTipText', text)


def bonusAppliedText(text):
    return _formatText(b'bonusAppliedText', text)


def bonusPreviewText(text):
    return _formatText(b'bonusPreviewText', text)


def promoSubTitle(text):
    return _formatText(b'promoSubTitle', text)


def promoSubTitlePlain(text):
    return _formatText(b'promoSubTitlePlain', text)


def alert(text):
    return _formatText(b'alertText', text)


def alertBig(text):
    return _formatText(b'alertBigText', text)


def success(text):
    return _formatText(b'successText', text)


def successBright(text):
    return _formatText(b'successBrightText', text)


def statsIncrease(text):
    return _formatText(b'statsIncrease', text)


def error(text):
    return _formatText(b'errorText', text)


def statsDecrease(text):
    return _formatText(b'statsDecrease', text)


def warning(text):
    return _formatText(b'statusWarningText', text)


def critical(text):
    return _formatText(b'statusCriticalText', text)


def expText(text):
    return _formatText(b'expText', text)


def gold(text):
    return _formatText(b'goldText', text)


def goldSmall(text):
    return _formatText(b'goldTextSmall', text)


def demountKitText(text):
    return _formatText(b'demountKitText', text)


def wotPlusText(text):
    return _formatText(b'wotPlusText', text)


def credits(text):
    return _formatText(b'creditsText', text)


def creditsSmall(text):
    return _formatText(b'creditsTextSmall', text)


def crystal(text):
    return _formatText(b'crystalText', text)


def equipCoin(text):
    return _formatText(b'equipCoinText', text)


def textEpic(text):
    return _formatText(b'textEpic', text)


def eventCoin(text):
    return _formatText(b'eventCoinText', text)


def bpcoin(text):
    return _formatText(b'bpcoinText', text)


def brcoin(text):
    return _formatText(b'creditsText', text)


def brProgressionToken(text):
    return _formatText(b'brProgressionToken', text)


def battlePassPoints(text):
    return _formatText(b'battlePassPointsText', text)


def defRes(text):
    return _formatText(b'defresText', text)


def counter(text):
    return _formatText(b'counterText', text)


def boosterText(text):
    return _formatText(b'boosterText', text)


def counterLabelText(text):
    return _formatText(b'counterLabelText', text)


def titleFont(text):
    return _formatText(b'titleFont', text)


def tutorial(text):
    return _formatText(b'tutorialText', text)


def playerOnline(text):
    return _formatText(b'playerOnline', text)


def hightlight(text):
    return _formatText(b'highlightText', text)


def alignText(text, align):
    return _getStyle(b'alignText', {b'message': text, b'align': align})


def leadingText(text, leading):
    return _getStyle(b'leadingText', {b'message': text, b'leading': leading})


def alignStandartText(text, align):
    return alignText(standard(text), align)


def vehicleStatusSimpleText(text):
    return _formatText(b'vehicleStatusSimpleText', text)


def vehicleStatusInfoText(text):
    return _formatText(b'vehicleStatusInfoText', text)


def vehicleStatusCriticalText(text):
    return _formatText(b'vehicleStatusCriticalText', text)


def vehicleStatusCriticalTextSmall(text):
    return _formatText(b'vehicleStatusCriticalTextSmall', text)


def vehicleName(text):
    return _formatText(b'vehicleName', text)


def premiumVehicleName(text):
    return _formatText(b'premiumVehicleName', text)


def superPromoTitle(text):
    return _formatText(b'superPromoTitle', text)


def superPromoTitleEm(text):
    return _formatText(b'superPromoTitleEm', text)


def superPromoTitleErr(text):
    return _formatText(b'superPromoTitleErr', text)


def highlightText(text):
    return _formatText(b'highlightText', text)


def highlightTextPlain(text):
    return _formatText(b'highlightTextPlain', text)


def unavailable(text):
    return _formatText(b'missionStatusUnavailable', text)


def missionStatusAvailable(text):
    return _formatText(b'missionStatusAvailable', text)


def epicTitle(text):
    return _formatText(b'epicTitle', text)


def epicTitleYellow(text):
    return _formatText(b'epicTitleYellow', text)


def heroTitle(text):
    return _formatText(b'heroTitle', text)


def heroTitleYellow(text):
    return _formatText(b'heroTitleYellow', text)


def heroTitleTK(text):
    return _formatText(b'heroTitleTK', text)


def grandTitle(text):
    return _formatText(b'grandTitle', text)


def grandTitleYellow(text):
    return _formatText(b'grandTitleYellow', text)


def grandTitleTK(text):
    return _formatText(b'grandTitleTK', text)


def grandTitleRed(text):
    return _formatText(b'grandTitleRed', text)


def failedStatusText(text):
    return _formatText(b'failedStatusText', text)


def yellowText(text):
    return _formatText(b'yellowText', text)


def greenText(text):
    return _formatText(b'greenText', text)


def brownText(text):
    return _formatText(b'brownText', text)


def discountText(text):
    return _formatText(b'discountText', text)


def goldTitle(text):
    return _formatText(b'goldTitle', text)


def creditsTitle(text):
    return _formatText(b'creditsTitle', text)


def crystalTitle(text):
    return _formatText(b'crystalTitle', text)


def expTitle(text):
    return _formatText(b'expTitle', text)


def poiCapturedBoldText(text):
    return _formatText(b'poiCapturedBoldText', text)


def poiCapturedRegularText(text):
    return _formatText(b'poiCapturedRegularText', text)


def whiteTitle15(text):
    return _formatText(b'whiteTitle15', text)


def whiteTitle12(text):
    return _formatText(b'whiteTitle12', text)


def cream15(text):
    return _formatText(b'cream15', text)


def styleName(text):
    return _formatText(b'styleName', text)


def getRawStyles(names):
    return dict((name, _getStyle(name)) for name in names)


def getStyles(names):
    return dict((name, _formatText(name)) for name in names)


def _processStyle(style):
    if hasattr(style, b'__iter__'):
        if not style:
            raise SoftException(b'Empty sequence')
        return _formatText(*style[:1])
    else:
        return _formatText(style)

    return


def concatStylesToSingleLine(*styles):
    return (b'').join(map(_processStyle, styles))


def concatStylesToMultiLine(*styles):
    return (b'\n').join(map(_processStyle, styles))


def concatStylesWithSpace(*styles):
    return (b' ').join(map(_processStyle, styles))


def concatStylesWithNBSP(*styles):
    return (b'&nbsp;').join(map(_processStyle, styles))


class _StylesBuilder(object):

    def __init__(self, delimiter=b''):
        super(_StylesBuilder, self).__init__()
        self.__chunks = []
        self.__delimiter = delimiter
        return

    def addStyledText(self, style, text=b''):
        self.__chunks.append((style, text))
        return self

    def render(self):
        result = []
        for style, text in self.__chunks:
            if isinstance(style, types.FunctionType):
                result.append(style(text))
            else:
                result.append(_formatText(style, text))

        return self.__delimiter.join(result)


def builder(delimiter=b''):
    return _StylesBuilder(delimiter)
